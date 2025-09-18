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


async def main():
    """Run through all API Epics in the AP project, checking for data quality issues"""
    print("Checking for EPIC data quality issues in AP project")
    print("=" * 60)
    
    try:
        # Create the API client
        client = JiraApiClient()
        
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
                    'fixVersions': fields.get('fixVersions', [])
                }
                
                print("=" * 80)
                print(f"\n{i:2}. Issue: {processed_issue['key']}")
                print(f"    Title: {processed_issue['summary']}")
                #print(f"    Status: {processed_issue['status']}")
                print(f"    Assignee: {processed_issue['assignee']}")
                #print(f"    Priority: {processed_issue['priority']}")
                #print(f"    Type: {processed_issue['issue_type']}")
                #print(f"    Created: {processed_issue['created'][:10] if processed_issue['created'] else 'Unknown'}")
                print(f"    URL: {processed_issue['url']}")
                #print(f"Raw JIRA data:\n{json.dumps(issue, indent=2)}")

                # EPIC data quality checks
                issue_id = f"{processed_issue['key']}"
                #print(f"    Processing EPIC [{issue_id}: \"{processed_issue['summary']}\"]\n    [{processed_issue['url']}] for data quality issues...")

                # - No assignee
                if not processed_issue['assignee'] or processed_issue['assignee'] == 'Unassigned':
                    print(f"    ⚠️  Data Quality Issue: EPIC [{issue_id}] is not assigned to anyone")
                else:
                    # Assigned to someone who is "inactive"
                    if fields.get('assignee', {}).get('active') == False:
                        print(f"    ⚠️  Data Quality Issue: EPIC [{issue_id}] is assigned to an inactive user")
                    else:
                        print(f"    👤 Assigned to: {processed_issue['assignee']}")

                # No issues linked
                if not processed_issue['issues']:
                    print(f"    ⚠️  Data Quality Issue: EPIC [{issue_id}] has no linked JIRAs")
                else:
                    print(f"    🔗 Linked issues: {len(processed_issue['issues'])} connected JIRAs found")
                    # {json.dumps(processed_issue['issues'], indent=2)}
                # No Components
                if not fields.get('components'):
                    print(f"    ⚠️  Data Quality Issue: EPIC [{issue_id}] has no components set")
                    # Try to find text in the title like "TMFxxx"
                    if 'TMF' in processed_issue['summary']:
                        # Extract the XXX number
                        tmf_number = processed_issue['summary'].split('TMF')[-1].strip().split(' ')[0].strip('E')
                        # Is there a component matching this?
                        matching_components = [name for name in component_names if name and tmf_number in name]
                        if matching_components:
                            print(f"      ✅ Propose adding component(s): {', '.join(str(comp) for comp in matching_components if comp)}")
                        else:
                            print(f"      ❌ No matching components found for TMF number {tmf_number}")
                    else:
                        print(f"      🔍 No 'TMF' number found in title: [{processed_issue['summary']}]")
                else:
                    component_names_in_issue = [comp.get('name') for comp in fields.get('components', []) if comp.get('name')]
                    print(f"    🏷️  Has {len(component_names_in_issue)} Components: {', '.join(component_names_in_issue)}")
                # No description
                if not processed_issue['description']:
                    print(f"    ⚠️  Data Quality Issue: EPIC [{issue_id}] has no description")
                # No "Issues in epic"
                if fields.get('issuelinks') and len(fields.get('issuelinks')) == 0:
                    print(f"    ⚠️  Data Quality Issue: EPIC [{issue_id}] has no 'Issues in Epic' links")
                    print(json.dumps(issue, indent=2))
                # FixVersion is less than 5.0
                if fields.get('fixVersions'):
                    for version in fields.get('fixVersions'):
                        version_name = version.get('name', '').strip('vVxX')
                        # Take the first number as the major version
                        version_number = version_name.split('.')[0] if '.' in version_name else version_name
                        try:
                            version_number = float(version_number)
                            if version_number < 5.0:
                                print(f"    ⚠️  Data Quality Issue: EPIC [{issue_id}] has FixVersion {version_name} which is less than 5.0")
                            else:
                                print(f"    ✅ FixVersion {version_name} looks good")
                        except ValueError:
                            print(f"    Tried to parse FixVersion {version_name} as a float - but failed")
                            # Not a number, ignore
                            pass
                else:
                    print(f"    ⚠️  Data Quality Issue: EPIC [{issue_id}] has no FixVersion set")
                # In Progress for over a year
                if processed_issue['created']:
                    created_date = datetime.strptime(processed_issue['created'][:10], '%Y-%m-%d')
                    if created_date < datetime.now() - timedelta(days=365):
                        print(f"    ⚠️  Data Quality Issue: EPIC [{issue_id}] is \"In Progress\" but is over a year old (created {processed_issue['created'][:10]}))")
                # Not updated in over 6 months
                if processed_issue['updated']:
                    updated_date = datetime.strptime(processed_issue['updated'][:10], '%Y-%m-%d')
                    if updated_date < datetime.now() - timedelta(days=180):
                        print(f"    ⚠️  Data Quality Issue: EPIC [{issue_id}] has not been updated in over 6 months (since {processed_issue['updated'][:10]})")

        
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