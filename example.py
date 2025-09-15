#!/usr/bin/env python3
"""
Example script demonstrating how to use the JIRA login and API functionality.
This script shows how to:
1. Authenticate with JIRA using the login bot
2. Use the API client to retrieve issues
3. Display the results in a formatted way
"""

import asyncio
from jira_api import JiraApiClient
import json


async def main():
    """Main example function"""
    print("🚀 JIRA API Example - Getting AP Project Issues")
    print("=" * 60)
    
    # Create the API client
    client = JiraApiClient()
    
    # Step 1: Authenticate
    print("\n🔐 Step 1: Authenticating with JIRA...")
    if not await client.authenticate():
        print("❌ Authentication failed. Please check your credentials in .env file.")
        return
    
    # Step 2: Get user info
    print("\n👤 Step 2: Getting user information...")
    user_info = client.get_user_info()
    if user_info:
        print(f"   Logged in as: {user_info.get('displayName', 'Unknown')}")
        print(f"   Email: {user_info.get('emailAddress', 'Not provided')}")
        print(f"   Account ID: {user_info.get('accountId', 'Not provided')}")
    
    # Step 3: Get project info
    print("\n📁 Step 3: Getting AP project information...")
    project_info = client.get_project_info('AP')
    if project_info:
        print(f"   Project Name: {project_info.get('name', 'Unknown')}")
        print(f"   Project Key: {project_info.get('key', 'Unknown')}")
        print(f"   Project Lead: {project_info.get('lead', {}).get('displayName', 'Unknown')}")
    else:
        print("   ⚠️  Could not retrieve AP project info (might not exist or no access)")
    
    # Step 4: Get issues from last month
    print("\n📋 Step 4: Getting AP project issues from last month...")
    issues = client.get_ap_issues_last_month(max_results=10)
    
    if issues:
        print(f"\n📊 Results: Found {len(issues)} issues")
        print("=" * 80)
        
        for i, issue in enumerate(issues, 1):
            print(f"\n{i:2}. Issue: {issue['key']}")
            print(f"    Title: {issue['summary']}")
            print(f"    Status: {issue['status']}")
            print(f"    Assignee: {issue['assignee']}")
            print(f"    Priority: {issue['priority']}")
            print(f"    Type: {issue['issue_type']}")
            print(f"    Created: {issue['created'][:10] if issue['created'] else 'Unknown'}")
            print(f"    URL: {issue['url']}")
            print("=" * 80)
            print(json.dumps(issue, indent=2))
            print("=" * 80)
            
            if i >= 10:  # Limit display to first 10 for readability
                remaining = len(issues) - 10
                if remaining > 0:
                    print(f"\n    ... and {remaining} more issues")
                break
        
        print("\n" + "=" * 100)
        print("✅ Example completed successfully!")
        
        # Show how to use the data programmatically
        print("\n🔧 Programmatic usage example:")
        print("```python")
        print("from jira_api import JiraApiClient")
        print("")
        print("async def get_issues():")
        print("    client = JiraApiClient()")
        print("    await client.authenticate()")
        print("    return client.get_ap_issues_last_month()")
        print("```")
        
    else:
        print("❌ No issues found or error occurred")
        print("   Possible reasons:")
        print("   - No issues in AP project from last month")
        print("   - AP project doesn't exist")
        print("   - Insufficient permissions")
        print("   - Network/authentication issues")


def run_example():
    """Convenience function to run the example"""
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⏹️  Script interrupted by user")
    except Exception as e:
        print(f"\n❌ Error running example: {str(e)}")


if __name__ == "__main__":
    run_example()