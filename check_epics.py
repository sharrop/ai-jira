import asyncio
from jira_api import JiraApiClient
import json
from datetime import datetime, timedelta
from exceptions import (
    JiraApiError,
    JiraAuthenticationError,
    JiraNetworkError,
    JiraValidationError,
    JiraConfigurationError
)
from rule_engine import RuleEngine, RuleReporter
from rule_config import DEFAULT_CONFIG


async def main():
    """Run through all API Epics in the AP project, checking for data quality issues"""
    print("Checking for EPIC data quality issues in AP project")
    print("=" * 60)
    
    try:
        # Create the API client
        client = JiraApiClient()
        
        # Initialize rule engine
        print("🔍 Debug: Creating rule engine...")
        rule_engine = RuleEngine(config=DEFAULT_CONFIG)
        print("� Debug: Getting rule summary...")
        summary = rule_engine.get_rule_summary()
        print(f"🔍 Debug: Summary keys: {list(summary.keys())}")
        
        print(f"\n📋 Rule Engine initialized:")
        print(f"   {summary['enabled_rules']}/{summary['total_rules']} rules enabled")
        for category, rules in summary['rules_by_category'].items():
            print(f"   - {category}: {len(rules)} rules")
        
        # Authenticate
        print("\n🔐 Step 1: Authenticating with JIRA...")
        if not await client.authenticate():
            print("JIRA Authentication failed. Check your credentials in .env file.")
            return
        else:
            user_info = await client.get_user_info()
            if user_info:
                print(f"   Logged in as: {user_info.get('displayName', 'Unknown')}")
                print(f"   Email: {user_info.get('emailAddress', 'Not provided')}")
            else:
                print("   ❌ Could not retrieve user info after authentication")
                return
        
        # First extract a list of Components in the AP project
        components = await client.get_project_components("AP")
        component_names = [comp.get('name') for comp in components if comp.get('name')]
        print(f"   Found {len(component_names)} Components in AP project:")
        for component in components[:30]:    # limit to first 30 for brevity
            name = component.get('name')
            lead = component.get('lead', {}).get('displayName', 'No lead')
            if lead != "No lead":
                active = component.get('lead', {}).get('active', False) if lead != "No lead" else False
                display_name = component.get('lead', {}).get('displayName', 'No lead')
            else:
                active = False
                display_name = "No lead"
            # Print display name padded to 40 characters
            print(f"   - {name:40} {display_name} {'(inactive)' if not active else ''}")

        # Get EPICs
        # JQL to find issues in AP project created in last month
        jql = f'project = AP AND type = Epic AND status in ("In Progress")'
        
        # Get raw search results
        search_results = await client.search_issues(jql, max_results=50)
        
        if search_results and search_results.get('issues'):
            issues_raw = search_results.get('issues', [])
            total = search_results.get('total', 0)
            
            print(f"\n📊 Results: Found {len(issues_raw)} issues (Total: {total})")
            print("=" * 80)
            
            # Process each issue
            for i, issue in enumerate(issues_raw, 1):
                fields = issue.get('fields', {})
                
                # Create processed issue data
                processed_issue = {
                    'key': issue.get('key'),
                    'summary': fields.get('summary'),
                    'status': fields.get('status', {}).get('name') if fields.get('status') else None,
                    'assignee': fields.get('assignee', {}).get('displayName') if fields.get('assignee') else 'Unassigned',
                    'reporter': fields.get('reporter', {}).get('displayName') if fields.get('reporter') else 'Unassigned',
                    'priority': fields.get('priority', {}).get('name') if fields.get('priority') else None,
                    'issue_type': fields.get('issuetype', {}).get('name') if fields.get('issuetype') else None,
                    'description': fields.get('description'),
                    'labels': fields.get('labels'),
                    'components': fields.get('components'),
                    'versions': fields.get('versions'),
                    'created': fields.get('created'),
                    'updated': fields.get('updated'),
                    'url': f"{client.base_url}/browse/{issue.get('key')}",
                    'issues': fields.get('issuelinks', []),
                    'fixVersions': fields.get('fixVersions', []),
                    'raw_fields': fields  # Keep raw fields for rules that need them
                }
                
                print("=" * 80)
                print(f"\n{i:2}. Issue: {processed_issue['key']}")
                print(f"    Title: {processed_issue['summary']}")
                print(f"    Assignee: {processed_issue['assignee']}")
                print(f"    URL: {processed_issue['url']}")
                
                # Run all rules against this issue
                context = {
                    'components': component_names,
                    'thresholds': DEFAULT_CONFIG.get('thresholds', {})
                }
                rule_results = rule_engine.run_rules(processed_issue, context)
                
                # Display results
                output_config = DEFAULT_CONFIG.get('output', {})
                RuleReporter.display_results(
                    rule_results,
                    show_passed=output_config.get('show_passed', False),
                    group_by_severity=output_config.get('group_by_severity', True)
                )

        
        print("\n" + "=" * 100)
        print("✅ EPIC check completed successfully!")
        
    except JiraAuthenticationError as e:
        print(f"\n❌ Authentication Error: {e}")
        print("Please check your JIRA credentials in the .env file")
        raise
    except JiraNetworkError as e:
        print(f"\n❌ Network Error: {e}")
        print("Please check your network connection and proxy settings")
        raise
    except JiraValidationError as e:
        print(f"\n❌ Validation Error: {e}")
        raise
    except JiraConfigurationError as e:
        print(f"\n❌ Configuration Error: {e}")
        print("Please check your environment configuration")
        raise
    except JiraApiError as e:
        print(f"\n❌ JIRA API Error: {e}")
        raise
    except Exception as e:
        print(f"\n❌ Unexpected Error during EPIC check: {e}")
        raise


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (JiraApiError, JiraAuthenticationError, JiraNetworkError, JiraValidationError, JiraConfigurationError) as e:
        print(f"\n❌ JIRA Error: {e}")
        exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected Error: {e}")
        exit(1)