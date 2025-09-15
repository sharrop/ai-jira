import requests
import json
import os
import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from dotenv import load_dotenv
from login import JiraLoginBot

# Load environment variables
load_dotenv()


class JiraApiClient:
    def __init__(self, base_url: str = "https://projects.tmforum.org/jira/"):
        self.base_url = base_url.rstrip('/')
        self.api_base = f"{self.base_url}/rest/api/2"
        self.cookies: Dict[str, str] = {}
        self.session = requests.Session()
        
        # Set up proxy if available
        http_proxy = os.getenv('HTTP_PROXY')
        https_proxy = os.getenv('HTTPS_PROXY')
        if http_proxy or https_proxy:
            proxies = {}
            if http_proxy:
                proxies['http'] = http_proxy
            if https_proxy:
                proxies['https'] = https_proxy
            elif http_proxy:
                proxies['https'] = http_proxy
            self.session.proxies = proxies
    
    async def authenticate(self, force_refresh: bool = False) -> bool:
        """Authenticate with JIRA using the login bot"""
        try:
            login_bot = JiraLoginBot(headless=False)
            self.cookies = await login_bot.get_cookies(force_refresh=force_refresh)
            
            # Update session cookies
            for name, value in self.cookies.items():
                self.session.cookies.set(name, value)
            
            # Test authentication
            response = self.session.get(f"{self.api_base}/myself")
            if response.status_code == 200:
                user_info = response.json()
                print(f"✅ Authenticated as: {user_info.get('displayName', 'Unknown')} ({user_info.get('emailAddress', 'No email')})")
                return True
            elif response.status_code == 401 and not force_refresh:
                # Cookies expired, try fresh login
                print("🔄 Cookies expired, attempting fresh login...")
                return await self.authenticate(force_refresh=True)
            else:
                print(f"❌ Authentication failed: {response.status_code}")
                if response.status_code == 401:
                    print("   This could be due to:")
                    print("   - Invalid credentials in .env file")
                    print("   - Account locked or requires additional authentication")
                    print("   - JIRA server configuration changes")
                print(f"   Response: {response.text[:200]}...")
                return False
                
        except Exception as e:
            print(f"❌ Authentication error: {str(e)}")
            return False
    
    def _make_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """Make an authenticated request to JIRA API"""
        url = f"{self.api_base}{endpoint}"
        
        # Add default headers
        headers = kwargs.get('headers', {})
        headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        
        # Add XSRF token if available
        xsrf_token = None
        for cookie_name, cookie_value in self.cookies.items():
            if 'xsrf' in cookie_name.lower() or 'csrf' in cookie_name.lower():
                # Extract token from cookie value if it contains metadata
                if '_' in cookie_value:
                    xsrf_token = cookie_value.split('_')[0]
                else:
                    xsrf_token = cookie_value
                headers['X-Atlassian-Token'] = 'no-check'  # Common Atlassian header
                headers['X-XSRF-TOKEN'] = xsrf_token
                break
        
        kwargs['headers'] = headers
        
        response = self.session.request(method, url, **kwargs)
        
        if response.status_code == 401:
            print("⚠️  Authentication may have expired. Consider refreshing cookies.")
        elif response.status_code >= 400:
            print(f"⚠️  API request failed: {response.status_code} - {response.text[:200]}...")
        
        return response
    
    def get_project_components(self, project_key: str) -> List[Dict[str, Any]]:
        """Get components of a specific project"""
        try:
            response = self._make_request('GET', f'/project/{project_key}/components')
            if response.status_code == 200:
                return response.json()
            return []
        except Exception as e:
            print(f"❌ Error getting project components: {str(e)}")
            return []

    def search_issues(self, jql: str, max_results: int = 50, start_at: int = 0, fields: Optional[List[str]] = None) -> Dict[str, Any]:
        """Search for issues using JQL (JIRA Query Language)"""
        if fields is None:
            fields = [
                'key', 'summary', 'status', 'assignee', 'created',
                'updated', 'priority', 'issuetype', 'description',
                'component', 'labels', 'reporter', 'resolution',
                'comment', 'issuelinks', 'issues', 'fixVersions' ]
        
        params = {
            'jql': jql,
            'maxResults': max_results,
            'startAt': start_at,
            'fields': ','.join(fields)
        }
        
        response = self._make_request('GET', '/search', params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
            return {}  # This won't be reached due to raise_for_status, but satisfies type checker
    
    def get_ap_issues_last_month(self, max_results: int = 100) -> List[Dict[str, Any]]:
        """Get all issues from AP project created in the last month"""
        # Calculate date one month ago
        one_month_ago = datetime.now() - timedelta(days=30)
        date_str = one_month_ago.strftime('%Y-%m-%d')
        
        # JQL to find issues in AP project created in last month
        jql = f'project = "AP" AND created >= "{date_str}" ORDER BY created DESC'
        
        print(f"🔍 Searching for AP project issues created since {date_str}")
        print(f"📝 JQL Query: {jql}")
        
        try:
            result = self.search_issues(jql, max_results=max_results)
            
            issues = result.get('issues', [])
            total = result.get('total', 0)
            
            print(f"📊 Found {len(issues)} issues (Total: {total})")
            
            # Process and return simplified issue data
            processed_issues = []
            for issue in issues:
                print(f"Raw Issue:\n{json.dumps(issue, indent=2)}")
                fields = issue.get('fields', {})
                # Process comments first
                comment_data = []
                comment_count = fields.get('comment', {}).get('total', 0) if fields.get('comment') else 0
                
                if comment_count > 0:
                    print(f"💬 Found {comment_count} comments:")
                    comments = fields.get('comment', {}).get('comments', [])                
                    for comment in comments:
                        comment_info = {
                            'author': comment.get('author', {}).get('displayName', 'Unknown'),
                            'author_email': comment.get('author', {}).get('emailAddress', ''),
                            'created': comment.get('created'),
                            'updated': comment.get('updated'),
                            'body': comment.get('body', '')
                        }
                        comment_data.append(comment_info)
                        
                        # Print comment for debugging
                        print(f"  Comment by {comment_info['author']} at {comment_info['created']}:")
                        print(f"    {comment_info['body'][:100]}...")
                        print()

                processed_issue = {
                    'key': issue.get('key'),
                    'summary': fields.get('summary'),
                    'status': fields.get('status', {}).get('name') if fields.get('status') else None,
                    'assignee': fields.get('assignee', {}).get('displayName') if fields.get('assignee') else 'Unassigned',
                    'reporter': fields.get('reporter', {}).get('displayName') if fields.get('reporter') else 'Unassigned',
                    'priority': fields.get('priority', {}).get('name') if fields.get('priority') else None,
                    'issue_type': fields.get('issuetype', {}).get('name') if fields.get('issuetype') else None,
                    'comment_count': comment_count,
                    'comments': comment_data,  # Add the collected comments
                    'created': fields.get('created'),
                    'updated': fields.get('updated'),
                    'url': f"{self.base_url}/browse/{issue.get('key')}"
                }
                
                processed_issues.append(processed_issue)
                print(f"Processed Issue:\n{json.dumps(processed_issue, indent=2)}")
            
            return processed_issues
            
        except Exception as e:
            print(f"❌ Error searching for issues: {str(e)}")
            return []
    
    def get_project_info(self, project_key: str) -> Optional[Dict[str, Any]]:
        """Get information about a specific project"""
        try:
            response = self._make_request('GET', f'/project/{project_key}')
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"❌ Error getting project info: {str(e)}")
            return None
    
    def get_user_info(self) -> Optional[Dict[str, Any]]:
        """Get current user information"""
        try:
            response = self._make_request('GET', '/myself')
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"❌ Error getting user info: {str(e)}")
            return None


# Convenience function for quick usage
async def get_ap_issues_quick() -> List[Dict[str, Any]]:
    """Quick function to get AP issues - handles authentication automatically"""
    client = JiraApiClient()
    
    if await client.authenticate():
        return client.get_ap_issues_last_month()
    else:
        print("❌ Failed to authenticate with JIRA")
        return []


if __name__ == "__main__":
    # Example usage when run directly
    async def main():
        client = JiraApiClient()
        
        print("🔐 Authenticating with JIRA...")
        if await client.authenticate():
            print("\n📋 Getting AP project issues from last month...")
            issues = client.get_ap_issues_last_month()
            
            if issues:
                print(f"\n📊 Found {len(issues)} issues in AP project:")
                print("=" * 80)
                
                for i, issue in enumerate(issues, 1):
                    print(f"{i:2}. {issue['key']}: {issue['summary'][:60]}...")
                    print(f"    Status: {issue['status']} | Assignee: {issue['assignee']}")
                    print(f"    Created: {issue['created'][:10]} | Type: {issue['issue_type']}")
                    print(f"    URL: {issue['url']}")
                    print()
            else:
                print("❌ No issues found or error occurred")
        else:
            print("❌ Authentication failed")
    
    # Run the example
    asyncio.run(main())