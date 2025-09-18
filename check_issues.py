"""
JIRA Issue Data Quality Checker for AP Project

This script runs data quality checks on various JIRA issue types in the AP project
using the modular rule engine. It's designed to work with Stories, Tasks, Bugs, 
and other issue types in addition to EPICs.
"""

import asyncio
from jira_api import JiraApiClient
import json
import pandas as pd
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


# Global variable to cache the TMF APIs dataframe
_tmf_apis_df = None


def load_tmf_apis():
    """
    Load the TMF APIs CSV file into a pandas DataFrame.
    
    Returns:
        pd.DataFrame: DataFrame containing TMF API information
    """
    global _tmf_apis_df
    
    if _tmf_apis_df is None:
        try:
            _tmf_apis_df = pd.read_csv('data/tmf_apis.csv')
            print(f"📊 Loaded {len(_tmf_apis_df)} TMF APIs from data/tmf_apis.csv")
        except FileNotFoundError:
            print("⚠️  Warning: data/tmf_apis.csv not found. TMF API lookup will not be available.")
            _tmf_apis_df = pd.DataFrame()  # Empty dataframe
        except Exception as e:
            print(f"⚠️  Warning: Error loading data/tmf_apis.csv: {e}")
            _tmf_apis_df = pd.DataFrame()  # Empty dataframe
    
    return _tmf_apis_df


def get_tmf_api_info(tmf_code):
    """
    Get the highest version number and URL for a given TMF API code.
    
    Args:
        tmf_code (str): TMF API code (e.g., "TMF646", "646", or just "646")
    
    Returns:
        dict: Dictionary with 'highest_version', 'url', 'long_name' or None if not found
    """
    df = load_tmf_apis()
    
    if df.empty:
        return None
    
    # Normalize the TMF code input
    if isinstance(tmf_code, str):
        # Remove any non-numeric characters and ensure it's a 3-digit number
        numeric_part = ''.join(filter(str.isdigit, tmf_code))
        if len(numeric_part) > 0:
            normalized_code = f"TMF{numeric_part.zfill(3)}"
        else:
            return None
    elif isinstance(tmf_code, int):
        normalized_code = f"TMF{tmf_code:03d}"
    else:
        return None
    
    # Find the API in the dataframe
    api_row = df[df['Short Name (TMF Code)'] == normalized_code]
    
    if api_row.empty:
        return None
    
    # Get the first (and should be only) match
    api_info = api_row.iloc[0]
    
    # Parse versions to find the highest one
    versions_str = api_info['Versions']
    if pd.isna(versions_str) or versions_str == 'Unknown':
        highest_version = 'Unknown'
    else:
        # Split versions by semicolon and clean up
        versions = [v.strip() for v in versions_str.split(';')]
        # Extract numeric parts of versions (e.g., "v4" -> 4)
        version_numbers = []
        for v in versions:
            if v.startswith('v') and v[1:].isdigit():
                version_numbers.append(int(v[1:]))
        
        if version_numbers:
            highest_version = f"v{max(version_numbers)}"
        else:
            highest_version = versions[0] if versions else 'Unknown'
    
    return {
        'long_name': api_info['Long Name'],
        'tmf_code': normalized_code,
        'highest_version': highest_version,
        'url': api_info['URL'],
        'all_versions': versions_str
    }


def find_tmf_references_in_text(text):
    """
    Find TMF API references in text (e.g., in descriptions, summaries).
    
    Args:
        text (str): Text to search for TMF references
    
    Returns:
        list: List of TMF API codes found in the text
    """
    import re
    
    if not text:
        return []
    
    # Pattern to match TMF followed by 3 digits
    tmf_pattern = r'TMF\s*(\d{3})'
    matches = re.findall(tmf_pattern, text, re.IGNORECASE)
    
    # Return unique TMF codes
    return list(set([f"TMF{match}" for match in matches]))


def enrich_issue_with_tmf_info(issue):
    """
    Enrich an issue with TMF API information if TMF references are found.
    
    Args:
        issue (dict): Issue data
    
    Returns:
        dict: Issue data enriched with TMF API information
    """
    enriched_issue = issue.copy()
    enriched_issue['tmf_apis'] = []
    
    # Search for TMF references in summary and description
    search_text = f"{issue.get('summary', '')} {issue.get('description', '')}"
    tmf_refs = find_tmf_references_in_text(search_text)
    
    for tmf_code in tmf_refs:
        api_info = get_tmf_api_info(tmf_code)
        if api_info:
            enriched_issue['tmf_apis'].append(api_info)
    
    return enriched_issue


async def main():
    """Run data quality checks on various JIRA issue types in the AP project"""
    print("Checking for JIRA Issue data quality issues in AP project")
    print("=" * 70)
    
    try:
        # Create the API client
        client = JiraApiClient()
        
        # Initialize rule engine
        print("🔍 Debug: Creating rule engine...")
        rule_engine = RuleEngine(config=DEFAULT_CONFIG)
        print("🔍 Debug: Getting rule summary...")
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
        
        # Get project components for context
        print("\n📦 Step 2: Loading project components...")
        components = await client.get_project_components("AP")
        component_names = [comp.get('name') for comp in components if comp.get('name')]
        print(f"   Found {len(component_names)} Components in AP project")
        
        # Define issue types to check
        issue_types_to_check = [
            {"name": "Story", "jql_filter": 'type = "Story"'},
            {"name": "Task", "jql_filter": 'type = "Task"'},
            {"name": "Bug", "jql_filter": 'type = "Bug"'},
            {"name": "Epic", "jql_filter": 'type = "Epic"'},
            {"name": "Sub-task", "jql_filter": 'type = "Sub-task"'}
        ]
        
        # Allow user to choose which issue types to check
        print(f"\n🎯 Step 3: Selecting issue types to check...")
        print("Available issue types:")
        for i, issue_type in enumerate(issue_types_to_check, 1):
            print(f"   {i}. {issue_type['name']}")
        
        # For automation, check all types. In interactive mode, you could ask for input
        selected_types = issue_types_to_check  # Check all types
        
        print(f"   Checking {len(selected_types)} issue types: {', '.join([t['name'] for t in selected_types])}")
        
        # Process each issue type
        for issue_type_config in selected_types:
            issue_type_name = issue_type_config['name']
            jql_filter = issue_type_config['jql_filter']
            
            print(f"\n" + "=" * 80)
            print(f"🔍 CHECKING {issue_type_name.upper()} ISSUES")
            print("=" * 80)
            
            # Build JQL query for this issue type
            # Focus on active issues (not closed/resolved) for data quality
            base_jql = f'project = AP AND {jql_filter} AND status not in ("Closed", "Resolved", "Done")'
            
            # Add time filter to focus on recent/active issues
            time_filter = ' AND (updated >= "-6M" OR status = "In Progress")'  # Last 6 months or in progress
            full_jql = base_jql + time_filter
            
            print(f"📊 JQL Query: {full_jql}")
            
            # Get issues
            try:
                search_results = await client.search_issues(full_jql, max_results=100)
                
                if search_results and search_results.get('issues'):
                    issues_raw = search_results.get('issues', [])
                    total = search_results.get('total', 0)
                    
                    print(f"\n📈 Results: Found {len(issues_raw)} {issue_type_name} issues to check (Total matching: {total})")
                    
                    if len(issues_raw) == 0:
                        print(f"   ✅ No {issue_type_name} issues found matching criteria")
                        continue
                    
                    # Initialize counters for summary
                    total_issues_checked = 0
                    total_violations = 0
                    violations_by_severity = {'WARNING': 0, 'ERROR': 0, 'CRITICAL': 0}
                    
                    # Process each issue
                    for i, issue in enumerate(issues_raw, 1):
                        fields = issue.get('fields', {})
                        
                        # Create processed issue data
                        assignee_info = fields.get('assignee', {})
                        assignee_name = assignee_info.get('displayName') if assignee_info else 'Unassigned'
                        assignee_email = assignee_info.get('emailAddress') if assignee_info else None
                        
                        reporter_info = fields.get('reporter', {})
                        reporter_name = reporter_info.get('displayName') if reporter_info else 'Unassigned'
                        reporter_email = reporter_info.get('emailAddress') if reporter_info else None
                        
                        processed_issue = {
                            'key': issue.get('key'),
                            'summary': fields.get('summary'),
                            'status': fields.get('status', {}).get('name') if fields.get('status') else None,
                            'assignee': assignee_name,
                            'assignee_email': assignee_email,
                            'reporter': reporter_name,
                            'reporter_email': reporter_email,
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
                        
                        print(f"\n{i:2}. {issue_type_name}: {processed_issue['key']}")
                        print(f"    Title: {processed_issue['summary']}")
                        print(f"    Status: {processed_issue['status']}")
                        
                        # Display assignee with email if available
                        if processed_issue['assignee_email']:
                            print(f"    Assignee: {processed_issue['assignee']} ({processed_issue['assignee_email']})")
                        else:
                            print(f"    Assignee: {processed_issue['assignee']}")
                        
                        print(f"    URL: {processed_issue['url']}")
                        
                        # Check for TMF API references and enrich the issue
                        enriched_issue = enrich_issue_with_tmf_info(processed_issue)
                        if enriched_issue['tmf_apis']:
                            print(f"    🔗 TMF APIs Referenced:")
                            for api_info in enriched_issue['tmf_apis']:
                                print(f"       • {api_info['tmf_code']}: {api_info['long_name']} (Latest: {api_info['highest_version']})")
                                print(f"         📖 Documentation: {api_info['url']}")
                        
                        # Run all rules against this issue
                        context = {
                            'components': component_names,
                            'thresholds': DEFAULT_CONFIG.get('thresholds', {}),
                            'issue_type': issue_type_name  # Pass issue type for rule filtering
                        }
                        
                        rule_results = rule_engine.run_rules(processed_issue, context)
                        
                        # Count violations
                        total_issues_checked += 1
                        failed_results = [r for r in rule_results if not r.passed]
                        if failed_results:
                            total_violations += len(failed_results)
                            for result in failed_results:
                                violations_by_severity[result.severity.value] = violations_by_severity.get(result.severity.value, 0) + 1
                        
                        # Display results
                        output_config = DEFAULT_CONFIG.get('output', {})
                        RuleReporter.display_results(
                            rule_results,
                            show_passed=output_config.get('show_passed', False),
                            group_by_severity=output_config.get('group_by_severity', True)
                        )
                        
                        # Add a small separator between issues
                        if i < len(issues_raw):
                            print("    " + "-" * 60)
                    
                    # Print summary for this issue type
                    print(f"\n📊 {issue_type_name} Summary:")
                    print(f"   Issues checked: {total_issues_checked}")
                    print(f"   Total violations: {total_violations}")
                    if violations_by_severity:
                        print("   Violations by severity:")
                        for severity, count in violations_by_severity.items():
                            if count > 0:
                                print(f"     {severity}: {count}")
                    
                    violation_rate = (total_violations / total_issues_checked) if total_issues_checked > 0 else 0
                    print(f"   Average violations per issue: {violation_rate:.1f}")
                    
                    # Quality assessment
                    if violation_rate == 0:
                        print("   🏆 Data Quality: EXCELLENT - No issues found!")
                    elif violation_rate < 2:
                        print("   ✅ Data Quality: GOOD - Minor issues found")
                    elif violation_rate < 5:
                        print("   ⚠️  Data Quality: NEEDS ATTENTION - Multiple issues found")
                    else:
                        print("   ❌ Data Quality: POOR - Many issues require immediate attention")
                
                else:
                    print(f"   ✅ No {issue_type_name} issues found matching the criteria")
                    
            except JiraApiError as e:
                print(f"   ❌ Error fetching {issue_type_name} issues: {e}")
                continue
        
        print("\n" + "=" * 100)
        print("✅ Multi-issue type data quality check completed successfully!")
        print("\n💡 Tips for improving data quality:")
        print("   - Ensure all issues are properly assigned")
        print("   - Add meaningful descriptions to all issues")
        print("   - Set appropriate components and fix versions")
        print("   - Keep issues updated and review stale items")
        print("   - Link related issues together")
        
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
        print(f"\n❌ Unexpected Error during multi-issue check: {e}")
        import traceback
        traceback.print_exc()
        raise


async def check_specific_issue_type(issue_type: str, max_results: int = 50):
    """
    Helper function to check a specific issue type only.
    
    Args:
        issue_type: The JIRA issue type to check (e.g., "Story", "Task", "Bug")
        max_results: Maximum number of issues to check
    """
    print(f"Checking {issue_type} issues in AP project")
    print("=" * 50)
    
    try:
        client = JiraApiClient()
        rule_engine = RuleEngine(config=DEFAULT_CONFIG)
        
        if not await client.authenticate():
            print("❌ Authentication failed")
            return
        
        components = await client.get_project_components("AP")
        component_names = [comp.get('name') for comp in components if comp.get('name')]
        
        jql = f'project = AP AND type = "{issue_type}" AND status not in ("Closed", "Resolved", "Done") AND updated >= "-3M"'
        search_results = await client.search_issues(jql, max_results=max_results)
        
        if search_results and search_results.get('issues'):
            issues = search_results.get('issues', [])
            print(f"📊 Found {len(issues)} {issue_type} issues to check")
            
            for i, issue in enumerate(issues, 1):
                fields = issue.get('fields', {})
                
                assignee_info = fields.get('assignee', {})
                assignee_name = assignee_info.get('displayName') if assignee_info else 'Unassigned'
                assignee_email = assignee_info.get('emailAddress') if assignee_info else None
                
                processed_issue = {
                    'key': issue.get('key'),
                    'summary': fields.get('summary'),
                    'status': fields.get('status', {}).get('name') if fields.get('status') else None,
                    'assignee': assignee_name,
                    'assignee_email': assignee_email,
                    'description': fields.get('description'),
                    'components': fields.get('components'),
                    'fixVersions': fields.get('fixVersions', []),
                    'issues': fields.get('issuelinks', []),
                    'created': fields.get('created'),
                    'updated': fields.get('updated'),
                    'url': f"{client.base_url}/browse/{issue.get('key')}",
                    'raw_fields': fields
                }
                
                # Display issue info with email
                if processed_issue['assignee_email']:
                    print(f"\n{i}. {processed_issue['key']}: {processed_issue['summary']}")
                    print(f"    Assignee: {processed_issue['assignee']} ({processed_issue['assignee_email']})")
                else:
                    print(f"\n{i}. {processed_issue['key']}: {processed_issue['summary']}")
                    print(f"    Assignee: {processed_issue['assignee']}")
                
                context = {
                    'components': component_names,
                    'thresholds': DEFAULT_CONFIG.get('thresholds', {}),
                    'issue_type': issue_type
                }
                
                results = rule_engine.run_rules(processed_issue, context)
                RuleReporter.display_results(results, show_passed=False, group_by_severity=True)
        else:
            print(f"✅ No {issue_type} issues found")
            
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    import sys
    
    # Check if user wants to check a specific issue type
    if len(sys.argv) > 1:
        issue_type = sys.argv[1]
        max_results = int(sys.argv[2]) if len(sys.argv) > 2 else 50
        
        print(f"🎯 Checking specific issue type: {issue_type}")
        try:
            asyncio.run(check_specific_issue_type(issue_type, max_results))
        except (JiraApiError, JiraAuthenticationError, JiraNetworkError, JiraValidationError, JiraConfigurationError) as e:
            print(f"\n❌ JIRA Error: {e}")
            exit(1)
        except Exception as e:
            print(f"\n❌ Unexpected Error: {e}")
            exit(1)
    else:
        # Run full multi-issue type check
        try:
            asyncio.run(main())
        except (JiraApiError, JiraAuthenticationError, JiraNetworkError, JiraValidationError, JiraConfigurationError) as e:
            print(f"\n❌ JIRA Error: {e}")
            exit(1)
        except Exception as e:
            print(f"\n❌ Unexpected Error: {e}")
            exit(1)