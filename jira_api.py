import requests
import json
import os
import asyncio
import time
import re
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from dotenv import load_dotenv
from login import JiraLoginBot
from jql_validator import JQLValidator, validate_jql_for_ap_project, build_safe_ap_query
from exceptions import (
    JiraApiError, JiraAuthenticationError, JiraNetworkError, 
    JiraConfigurationError, JiraValidationError, JiraRateLimitError,
    JiraPermissionError, classify_http_error, handle_requests_exception
)

# Load environment variables
load_dotenv()


def safe_encode_for_cp1252(text):
    """
    Safely encode text for Windows CP1252 compatibility when redirecting output to files.
    
    Args:
        text: Input text that may contain Unicode characters
        
    Returns:
        str: Text with Unicode characters replaced by '?' for CP1252 compatibility
    """
    if not text:
        return text
    
    # Convert to string if not already
    if not isinstance(text, str):
        text = str(text)
    
    # Encode to CP1252 with 'replace' error handling, then decode back to string
    # This will replace any Unicode characters that can't be encoded with '?'
    return text.encode('cp1252', errors='replace').decode('cp1252')


class JiraApiClient:
    def __init__(self, base_url: str = "https://projects.tmforum.org/jira/", 
                 enable_jql_validation: bool = True,
                 allowed_projects: Optional[List[str]] = None):
        # Validate base URL
        if not base_url or not base_url.startswith(('http://', 'https://')):
            raise JiraConfigurationError(
                f"Invalid base URL: {base_url}. Must start with http:// or https://",
                config_key="base_url"
            )
            
        self.base_url = base_url.rstrip('/')
        self.api_base = f"{self.base_url}/rest/api/2"
        self.cookies: Dict[str, str] = {}
        self.session = requests.Session()
        
        # Initialize JQL validator
        self.enable_jql_validation = enable_jql_validation
        if enable_jql_validation:
            self.jql_validator = JQLValidator(
                allowed_projects=set(allowed_projects) if allowed_projects else {'AP'},
                max_query_length=2000,  # Reasonable limit for JQL queries
            )
        else:
            self.jql_validator = None
        
        # Set up proxy if available
        self._configure_proxy()
    
    def _configure_proxy(self) -> None:
        """Configure proxy settings from environment variables"""
        try:
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
        except Exception as e:
            raise JiraConfigurationError(
                f"Failed to configure proxy settings: {e}",
                config_key="proxy"
            )
    
    async def authenticate(self, force_refresh: bool = False) -> bool:
        """
        Authenticate with JIRA using the login bot
        
        Args:
            force_refresh: Force a fresh login even if cookies exist
            
        Returns:
            bool: True if authentication successful
            
        Raises:
            JiraAuthenticationError: If authentication fails
            JiraConfigurationError: If login module is missing
            JiraNetworkError: If network issues occur
        """
        try:
            login_bot = JiraLoginBot(headless=False)
            self.cookies = await login_bot.get_cookies(force_refresh=force_refresh)
            
            if not self.cookies:
                raise JiraAuthenticationError("Failed to obtain authentication cookies")
            
            # Update session cookies
            for name, value in self.cookies.items():
                self.session.cookies.set(name, value)
            
            # Test authentication
            try:
                response = await self._make_request_with_retry('GET', '/myself')
                
                if response.status_code == 200:
                    user_info = response.json()
                    print(f"[AUTH] Authenticated as: {user_info.get('displayName', 'Unknown')} ({user_info.get('emailAddress', 'No email')})")
                    return True
                elif response.status_code == 401 and not force_refresh:
                    # Cookies expired, try fresh login
                    print("[RETRY] Cookies expired, attempting fresh login...")
                    return await self.authenticate(force_refresh=True)
                else:
                    error_msg = f"Authentication failed with status {response.status_code}"
                    if response.status_code == 401:
                        error_msg += ". This could be due to invalid credentials, account locked, or JIRA configuration changes."
                    raise JiraAuthenticationError(error_msg)
                    
            except JiraNetworkError as e:
                raise JiraAuthenticationError(f"Network error during authentication test: {e}")
                
        except ImportError:
            raise JiraConfigurationError(
                "JiraLoginBot not available. Ensure login.py is in the same directory.",
                config_key="login_module"
            )
        except Exception as e:
            if isinstance(e, (JiraAuthenticationError, JiraConfigurationError)):
                raise
            raise JiraAuthenticationError(f"Unexpected authentication error: {e}")
    
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
            print("[WARNING] Authentication may have expired. Consider refreshing cookies.")
        elif response.status_code >= 400:
            print(f"[WARNING] API request failed: {response.status_code} - {response.text[:200]}...")
        
        return response
    
    async def _make_request_with_retry(self, method: str, endpoint: str, max_retries: int = 3, **kwargs) -> requests.Response:
        """
        Make an authenticated request to JIRA API with retry logic and exponential backoff
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint (without base URL)
            max_retries: Maximum number of retry attempts
            **kwargs: Additional arguments for the request
            
        Returns:
            requests.Response: Response object
            
        Raises:
            JiraNetworkError: For network/connection issues
            JiraRateLimitError: For rate limiting (429) responses
            JiraPermissionError: For permission denied (403) responses
            JiraApiError: For other API errors
        """
        import asyncio
        import time
        
        last_exception = None
        
        for attempt in range(max_retries + 1):
            try:
                response = self._make_request(method, endpoint, **kwargs)
                
                # Check for specific HTTP status codes
                if response.status_code == 200:
                    return response
                elif response.status_code == 401:
                    raise JiraAuthenticationError("Authentication failed - invalid or expired credentials")
                elif response.status_code == 403:
                    raise JiraPermissionError(
                        f"Permission denied for {method} {endpoint}",
                        resource=f"{method} {endpoint}"
                    )
                elif response.status_code == 429:
                    retry_after = int(response.headers.get('Retry-After', 60))
                    if attempt < max_retries:
                        print(f"[RATE-LIMIT] Rate limited, waiting {retry_after} seconds before retry {attempt + 1}/{max_retries}")
                        await asyncio.sleep(retry_after)
                        continue
                    else:
                        raise JiraRateLimitError(
                            f"Rate limit exceeded for {method} {endpoint}",
                            retry_after=retry_after
                        )
                elif response.status_code >= 500:
                    # Server error - retry with exponential backoff
                    if attempt < max_retries:
                        wait_time = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s
                        print(f"[RETRY] Server error ({response.status_code}), retrying in {wait_time}s (attempt {attempt + 1}/{max_retries})")
                        await asyncio.sleep(wait_time)
                        continue
                    else:
                        raise JiraNetworkError(
                            f"Server error after {max_retries} retries: {response.status_code}"
                        )
                else:
                    # Other 4xx errors
                    raise JiraApiError(
                        f"API request failed: {response.status_code}",
                        status_code=response.status_code,
                        response_data={'response_text': response.text[:500]}
                    )
                    
            except requests.exceptions.ConnectionError as e:
                last_exception = e
                if attempt < max_retries:
                    wait_time = 2 ** attempt
                    print(f"[NETWORK] Connection error, retrying in {wait_time}s (attempt {attempt + 1}/{max_retries})")
                    await asyncio.sleep(wait_time)
                    continue
                else:
                    raise JiraNetworkError(f"Connection failed after {max_retries} retries: {e}")
                    
            except requests.exceptions.Timeout as e:
                last_exception = e
                if attempt < max_retries:
                    wait_time = 2 ** attempt
                    print(f"[TIMEOUT] Request timeout, retrying in {wait_time}s (attempt {attempt + 1}/{max_retries})")
                    await asyncio.sleep(wait_time)
                    continue
                else:
                    raise JiraNetworkError(f"Request timeout after {max_retries} retries: {e}")
                    
            except requests.exceptions.RequestException as e:
                last_exception = e
                if attempt < max_retries:
                    wait_time = 2 ** attempt
                    print(f"[REQUEST] Request error, retrying in {wait_time}s (attempt {attempt + 1}/{max_retries})")
                    await asyncio.sleep(wait_time)
                    continue
                else:
                    raise JiraNetworkError(f"Request failed after {max_retries} retries: {e}")
        
        # This should never be reached, but just in case
        if last_exception:
            raise JiraNetworkError(f"All retry attempts failed: {last_exception}")
        else:
            raise JiraApiError("Unexpected error in retry logic")
    
    async def get_project_components(self, project_key: str) -> List[Dict[str, Any]]:
        """
        Get components of a specific project
        
        Args:
            project_key: The project key (e.g., 'AP')
            
        Returns:
            List of project components
            
        Raises:
            JiraValidationError: If project_key is invalid
            JiraApiError: For API-related errors
            JiraNetworkError: For network issues
        """
        if not project_key or not project_key.strip():
            raise JiraValidationError("Project key cannot be empty", field_name="project_key")
            
        try:
            response = await self._make_request_with_retry('GET', f'/project/{project_key}/components')
            return response.json()
        except (JiraApiError, JiraNetworkError, JiraAuthenticationError, JiraPermissionError):
            # Re-raise specific JIRA exceptions
            raise
        except Exception as e:
            raise JiraApiError(f"Unexpected error getting project components: {e}")

    async def search_issues(self, jql: str, max_results: int = 50, start_at: int = 0, fields: Optional[List[str]] = None, 
                          validate_jql: Optional[bool] = None) -> Dict[str, Any]:
        """
        Search for issues using JQL (JIRA Query Language)
        
        Args:
            jql: JIRA Query Language string
            max_results: Maximum number of results to return
            start_at: Starting index for pagination
            fields: List of fields to include in results
            validate_jql: Override global JQL validation setting
            
        Returns:
            Dictionary containing search results
            
        Raises:
            JiraValidationError: If JQL query is invalid or fails security checks
            JiraApiError: For API-related errors
            JiraNetworkError: For network issues
        """
        if not jql or not jql.strip():
            raise JiraValidationError("JQL query cannot be empty", field_name="jql")
        
        # Apply JQL validation if enabled
        should_validate = validate_jql if validate_jql is not None else self.enable_jql_validation
        if should_validate and self.jql_validator:
            try:
                validation_result = self.jql_validator.validate_jql_query(jql, strict_mode=True)
                
                # Log warnings if any
                if validation_result['warnings']:
                    print(f"[WARNING] JQL Warnings: {', '.join(validation_result['warnings'])}")
                if validation_result['performance_warnings']:
                    print(f"[PERFORMANCE] Performance Warnings: {', '.join(validation_result['performance_warnings'])}")
                
                # Use sanitized query
                jql = validation_result['sanitized_query']
                
            except JiraValidationError as e:
                print(f"[ERROR] JQL Validation Failed: {e}")
                raise
            
        if max_results <= 0:
            raise JiraValidationError("max_results must be greater than 0", field_name="max_results")
            
        if start_at < 0:
            raise JiraValidationError("start_at must be >= 0", field_name="start_at")
        
        if fields is None:
            fields = [
                'key', 'summary', 'status', 'assignee', 'created',
                'updated', 'priority', 'issuetype', 'description',
                'components', 'labels', 'reporter', 'resolution',
                'comment', 'issuelinks', 'issues', 'fixVersions' ]
        
        params = {
            'jql': jql,
            'maxResults': max_results,
            'startAt': start_at,
            'fields': ','.join(fields)
        }
        
        try:
            response = await self._make_request_with_retry('GET', '/search', params=params)
            return response.json()
        except (JiraApiError, JiraNetworkError, JiraAuthenticationError, JiraPermissionError):
            # Re-raise specific JIRA exceptions
            raise
        except Exception as e:
            raise JiraApiError(f"Unexpected error during issue search: {e}")
    
    async def get_ap_issues_last_month(self, max_results: int = 100) -> List[Dict[str, Any]]:
        """
        Get all issues from AP project created in the last month
        
        Args:
            max_results: Maximum number of results to return
            
        Returns:
            List of processed issue dictionaries
            
        Raises:
            JiraValidationError: If max_results is invalid
            JiraApiError: For API-related errors
            JiraNetworkError: For network issues
        """
        if max_results <= 0:
            raise JiraValidationError("max_results must be greater than 0", field_name="max_results")
        
        # Calculate date one month ago
        one_month_ago = datetime.now() - timedelta(days=30)
        date_str = one_month_ago.strftime('%Y-%m-%d')
        
        # Build JQL query using safe construction if validator is available
        if self.jql_validator:
            # Use parameterized query building for safety
            jql = self.jql_validator.build_safe_jql(
                'project = {project} AND created >= {date} ORDER BY created DESC',
                project="AP",
                date=date_str
            )
        else:
            # Fallback to direct construction (with manual sanitization)
            # Validate date format
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
                raise JiraValidationError(f"Invalid date format: {date_str}", field_name="date")
            jql = f'project = "AP" AND created >= "{date_str}" ORDER BY created DESC'
        
        print(f"[SEARCH] Searching for AP project issues created since {date_str}")
        print(f"[JQL] JQL Query: {jql}")
        
        try:
            result = await self.search_issues(jql, max_results=max_results, validate_jql=False)  # Already validated
            
            issues = result.get('issues', [])
            total = result.get('total', 0)
            
            print(f"[RESULTS] Found {len(issues)} issues (Total: {total})")
            
            # Process and return simplified issue data
            processed_issues = []
            for issue in issues:
                try:
                    issue_json = json.dumps(issue, indent=2, ensure_ascii=True)
                    print(f"Raw Issue:\n{safe_encode_for_cp1252(issue_json)}")
                except Exception as e:
                    print(f"[WARNING] Could not serialize issue JSON: {e}")
                fields = issue.get('fields', {})
                # Process comments first
                comment_data = []
                comment_count = fields.get('comment', {}).get('total', 0) if fields.get('comment') else 0
                
                if comment_count > 0:
                    print(f"[COMMENTS] Found {comment_count} comments:")
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
                        print(f"  Comment by {safe_encode_for_cp1252(comment_info['author'])} at {comment_info['created']}:")
                        print(f"    {safe_encode_for_cp1252(comment_info['body'][:100])}...")
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
                try:
                    processed_json = json.dumps(processed_issue, indent=2, ensure_ascii=True)
                    print(f"Processed Issue:\n{safe_encode_for_cp1252(processed_json)}")
                except Exception as e:
                    print(f"[WARNING] Could not serialize processed issue JSON: {e}")
            
            return processed_issues
            
        except (JiraApiError, JiraNetworkError, JiraAuthenticationError, JiraPermissionError, JiraValidationError):
            # Re-raise specific JIRA exceptions
            raise
        except Exception as e:
            raise JiraApiError(f"Unexpected error getting AP issues: {e}")
    
    async def get_project_info(self, project_key: str) -> Optional[Dict[str, Any]]:
        """
        Get information about a specific project
        
        Args:
            project_key: The project key (e.g., 'AP')
            
        Returns:
            Project information dictionary or None if not found
            
        Raises:
            JiraValidationError: If project_key is invalid
            JiraApiError: For API-related errors
            JiraNetworkError: For network issues
        """
        if not project_key or not project_key.strip():
            raise JiraValidationError("Project key cannot be empty", field_name="project_key")
            
        try:
            response = await self._make_request_with_retry('GET', f'/project/{project_key}')
            return response.json()
        except JiraPermissionError:
            # Convert permission error to return None for project not found/accessible
            return None
        except (JiraApiError, JiraNetworkError, JiraAuthenticationError):
            # Re-raise specific JIRA exceptions
            raise
        except Exception as e:
            raise JiraApiError(f"Unexpected error getting project info: {e}")
    
    async def get_user_info(self) -> Optional[Dict[str, Any]]:
        """
        Get current user information
        
        Returns:
            User information dictionary or None if not available
            
        Raises:
            JiraApiError: For API-related errors
            JiraNetworkError: For network issues
            JiraAuthenticationError: If not authenticated
        """
        try:
            response = await self._make_request_with_retry('GET', '/myself')
            return response.json()
        except (JiraApiError, JiraNetworkError, JiraAuthenticationError, JiraPermissionError):
            # Re-raise specific JIRA exceptions
            raise
        except Exception as e:
            raise JiraApiError(f"Unexpected error getting user info: {e}")
    
    def build_safe_jql(self, template: str, **parameters) -> str:
        """
        Build a safe JQL query using parameterized templates.
        
        Args:
            template: JQL template with {parameter} placeholders
            **parameters: Parameter values to substitute safely
            
        Returns:
            Safe JQL query string
            
        Raises:
            JiraValidationError: If validation is enabled and query fails validation
            JiraConfigurationError: If JQL validation is disabled
            
        Example:
            >>> client.build_safe_jql(
            ...     "project = {project} AND assignee = {user} AND created >= {date}",
            ...     project="AP",
            ...     user="john.doe@company.com",
            ...     date="2025-01-01"
            ... )
        """
        if not self.jql_validator:
            raise JiraConfigurationError(
                "JQL validation is disabled. Cannot build safe queries.",
                config_key="jql_validation"
            )
        
        return self.jql_validator.build_safe_jql(template, **parameters)
    
    def validate_jql(self, jql: str, strict_mode: bool = True) -> Dict[str, Any]:
        """
        Validate a JQL query without executing it.
        
        Args:
            jql: JQL query to validate
            strict_mode: Enable strict validation rules
            
        Returns:
            Validation result dictionary
            
        Raises:
            JiraValidationError: If query fails validation
            JiraConfigurationError: If JQL validation is disabled
        """
        if not self.jql_validator:
            raise JiraConfigurationError(
                "JQL validation is disabled. Cannot validate queries.",
                config_key="jql_validation"
            )
        
        return self.jql_validator.validate_jql_query(jql, strict_mode=strict_mode)
    
    async def search_issues_safe(self, template: str, max_results: int = 50, 
                               start_at: int = 0, fields: Optional[List[str]] = None,
                               **parameters) -> Dict[str, Any]:
        """
        Search for issues using a safe parameterized JQL template.
        
        Args:
            template: JQL template with {parameter} placeholders
            max_results: Maximum number of results to return
            start_at: Starting index for pagination
            fields: List of fields to include in results
            **parameters: Parameter values to substitute safely
            
        Returns:
            Dictionary containing search results
            
        Raises:
            JiraValidationError: If template or parameters are invalid
            JiraApiError: For API-related errors
            
        Example:
            >>> results = await client.search_issues_safe(
            ...     "project = {project} AND status = {status}",
            ...     project="AP",
            ...     status="In Progress"
            ... )
        """
        safe_jql = self.build_safe_jql(template, **parameters)
        return await self.search_issues(safe_jql, max_results, start_at, fields, validate_jql=False)


# Convenience function for quick usage
async def get_ap_issues_quick() -> List[Dict[str, Any]]:
    """Quick function to get AP issues - handles authentication automatically"""
    client = JiraApiClient()
    
    if await client.authenticate():
        return await client.get_ap_issues_last_month()
    else:
        print("[ERROR] Failed to authenticate with JIRA")
        return []


if __name__ == "__main__":
    # Example usage when run directly
    async def main():
        client = JiraApiClient()
        
        print("[AUTH] Authenticating with JIRA...")
        if await client.authenticate():
            print("\n[DATA] Getting AP project issues from last month...")
            issues = await client.get_ap_issues_last_month()
            
            if issues:
                print(f"\n[RESULTS] Found {len(issues)} issues in AP project:")
                print("=" * 80)
                
                for i, issue in enumerate(issues, 1):
                    print(f"{i:2}. {issue['key']}: {safe_encode_for_cp1252(issue['summary'][:60])}...")
                    print(f"    Status: {issue['status']} | Assignee: {safe_encode_for_cp1252(issue['assignee'])}")
                    print(f"    Created: {issue['created'][:10]} | Type: {issue['issue_type']}")
                    print(f"    URL: {issue['url']}")
                    print()
            else:
                print("[ERROR] No issues found or error occurred")
        else:
            print("[ERROR] Authentication failed")
    
    # Run the example
    asyncio.run(main())