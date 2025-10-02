"""
Markdown Report Generator for JIRA Issue Data Quality Checker

This module provides markdown formatting functions to convert the console output
from check_issues.py into a properly formatted markdown report.
"""

import re
from datetime import datetime
from typing import Dict, List, Any


class MarkdownReporter:
    """Handles conversion of console output to markdown format"""
    
    def __init__(self):
        self.sections = []
        self.current_section = None
        self.issue_count = 0
        self.violation_count = 0
        
    def start_report(self, title: str = "JIRA Issue Data Quality Report"):
        """Start a new markdown report"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        markdown = f"""# {title}

**Generated:** {timestamp}  
**Project:** AP (TM Forum JIRA)

---

"""
        return markdown
    
    def format_section_header(self, text: str, level: int = 2) -> str:
        """Format a section header based on the original format"""
        # Convert [CHECK] CHECKING STORY ISSUES to ## Checking Story Issues
        # Remove brackets and convert to title case
        clean_text = re.sub(r'\[.*?\]\s*', '', text)
        clean_text = clean_text.title()
        
        header_chars = "#" * level
        return f"\n{header_chars} {clean_text}\n\n"
    
    def format_authentication_section(self, user_name: str, email: str) -> str:
        """Format authentication information"""
        return f"""## Authentication Status

✅ **Successfully authenticated with JIRA**

- **User:** {user_name}
- **Email:** {email}

"""
    
    def format_rule_engine_summary(self, summary: Dict[str, Any]) -> str:
        """Format rule engine initialization summary"""
        rules_text = ""
        for category, rules in summary.get('rules_by_category', {}).items():
            rules_text += f"- **{category}:** {len(rules)} rules\n"
        
        return f"""## Rule Engine Configuration

**Status:** ✅ Initialized  
**Rules:** {summary.get('enabled_rules', 0)}/{summary.get('total_rules', 0)} enabled

### Rules by Category
{rules_text}

"""
    
    def format_issue_type_section(self, issue_type: str, jql_query: str, found_count: int, total_matching: int) -> str:
        """Format the start of an issue type section"""
        return f"""## {issue_type} Issues Analysis

**JQL Query:** `{jql_query}`  
**Issues Found:** {found_count} (Total matching: {total_matching})

"""
    
    def format_issue_details(self, issue_num: int, issue_data: Dict[str, Any], 
                           tmf_apis: List[Dict[str, Any]] = None) -> str:
        """Format individual issue details"""
        
        # Build assignee info
        assignee_text = issue_data.get('assignee', 'Unassigned')
        if issue_data.get('assignee_email'):
            assignee_text += f" ({issue_data['assignee_email']})"
        
        # Build basic issue info
        markdown = f"""### {issue_num}. {issue_data.get('key', 'Unknown')}

**Title:** {issue_data.get('summary', 'No title')}  
**Status:** {issue_data.get('status', 'Unknown')}  
**Assignee:** {assignee_text}  
**URL:** [{issue_data.get('key', 'Link')}]({issue_data.get('url', '#')})

"""
        
        # Add TMF API information if present
        if tmf_apis:
            markdown += "**TMF APIs Referenced:**\n"
            for api_info in tmf_apis:
                markdown += f"- **{api_info.get('tmf_code', 'Unknown')}:** {api_info.get('long_name', 'No description')} (Latest: {api_info.get('highest_version', 'Unknown')})\n"
                markdown += f"  - Documentation: [{api_info.get('url', '#')}]({api_info.get('url', '#')})\n"
            markdown += "\n"
        
        return markdown
    
    def format_rule_violations(self, violations: List[Dict[str, Any]]) -> str:
        """Format rule violation results"""
        if not violations:
            return "✅ **No violations found**\n\n"
        
        markdown = "#### Rule Violations\n\n"
        
        # Group by severity
        by_severity = {}
        for violation in violations:
            severity = violation.get('severity', 'UNKNOWN')
            if severity not in by_severity:
                by_severity[severity] = []
            by_severity[severity].append(violation)
        
        # Display by severity (Critical first)
        severity_order = ['CRITICAL', 'ERROR', 'WARNING']
        severity_icons = {
            'CRITICAL': '🔴',
            'ERROR': '🟠', 
            'WARNING': '🟡'
        }
        
        for severity in severity_order:
            if severity in by_severity:
                icon = severity_icons.get(severity, '❓')
                markdown += f"##### {icon} {severity}\n\n"
                
                for violation in by_severity[severity]:
                    rule_name = violation.get('rule_name', 'Unknown Rule')
                    message = violation.get('message', 'No message')
                    details = violation.get('details', '')
                    
                    markdown += f"- **{rule_name}:** {message}\n"
                    if details:
                        markdown += f"  - *Details:* {details}\n"
                
                markdown += "\n"
        
        return markdown
    
    def format_issue_type_summary(self, issue_type: str, total_checked: int, 
                                 total_violations: int, violations_by_severity: Dict[str, int]) -> str:
        """Format summary for an issue type"""
        
        severity_text = ""
        for severity, count in violations_by_severity.items():
            if count > 0:
                icon = {'CRITICAL': '🔴', 'ERROR': '🟠', 'WARNING': '🟡'}.get(severity, '❓')
                severity_text += f"- {icon} {severity}: {count}\n"
        
        if not severity_text:
            severity_text = "- ✅ No violations found\n"
        
        return f"""### {issue_type} Summary

- **Issues Checked:** {total_checked}
- **Total Violations:** {total_violations}

**Violations by Severity:**
{severity_text}

---

"""
    
    def format_label_usage_report(self, label_data: Dict[str, List[Dict[str, Any]]]) -> str:
        """Format the label usage report section"""
        
        if not label_data:
            return """## Label Usage Report

No labels found in any checked issues.

"""
        
        total_labels = len(label_data)
        total_usages = sum(len(issues) for issues in label_data.values())
        
        markdown = f"""## Label Usage Report

### Summary
- **Total unique labels:** {total_labels}
- **Total label usages:** {total_usages}
- **Average labels per issue:** {total_usages / len(set(issue['key'] for issues in label_data.values() for issue in issues)):.1f}

### Label Details
*(Sorted by usage count)*

"""
        
        # Sort labels by usage count
        sorted_labels = sorted(label_data.items(), key=lambda x: len(x[1]), reverse=True)
        
        for i, (label, issues) in enumerate(sorted_labels, 1):
            markdown += f"#### {i}. Label: `{label}` (used {len(issues)} times)\n\n"
            
            # Group by issue type
            by_type = {}
            for issue in issues:
                issue_type = issue.get('type', 'Unknown')
                if issue_type not in by_type:
                    by_type[issue_type] = []
                by_type[issue_type].append(issue)
            
            for issue_type, type_issues in sorted(by_type.items()):
                if len(type_issues) > 0:
                    markdown += f"**{issue_type}s ({len(type_issues)}):**\n"
                    
                    # Limit to first 10 issues to avoid extremely long reports
                    display_issues = type_issues[:10]
                    for issue in display_issues:
                        summary = issue.get('summary', 'No title')[:80]
                        if len(issue.get('summary', '')) > 80:
                            summary += "..."
                        markdown += f"- [{issue['key']}]({issue['url']}): {summary}\n"
                    
                    if len(type_issues) > 10:
                        markdown += f"- *... and {len(type_issues) - 10} more {issue_type}s*\n"
                    
                    markdown += "\n"
        
        return markdown
    
    def format_insights_section(self, insights: List[str]) -> str:
        """Format insights and recommendations"""
        if not insights:
            return ""
        
        markdown = "### Label Insights\n\n"
        for insight in insights:
            markdown += f"- {insight}\n"
        markdown += "\n"
        
        return markdown
    
    def finish_report(self) -> str:
        """Add footer to the report"""
        return f"""---

*Report generated by JIRA Issue Data Quality Checker*  
*For more information, see the project documentation.*
"""


def convert_console_output_to_markdown(console_text: str) -> str:
    """
    Convert the existing console output format to markdown.
    This is a utility function for converting existing report.txt files.
    """
    reporter = MarkdownReporter()
    lines = console_text.split('\n')
    
    markdown_content = reporter.start_report()
    current_section = None
    in_issue_details = False
    issue_buffer = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if not line:
            i += 1
            continue
        
        # Skip the initial title and separator
        if line.startswith('Checking for JIRA Issue data quality') or line == '=' * 70:
            i += 1
            continue
            
        # Detect main section headers
        if line.startswith('[CHECK]') and 'CHECKING' in line:
            issue_type = line.replace('[CHECK] CHECKING', '').replace('ISSUES', '').strip()
            markdown_content += reporter.format_section_header(f"Checking {issue_type} Issues")
            
        elif line.startswith('[AUTH]') and 'Logged in as:' in line:
            user_name = line.split('Logged in as:')[1].strip()
            # Look for email in next line
            email = ""
            if i + 1 < len(lines) and 'Email:' in lines[i + 1]:
                email = lines[i + 1].split('Email:')[1].strip()
                i += 1  # Skip the email line
            markdown_content += reporter.format_authentication_section(user_name, email)
            
        elif line.startswith('[RULES]') and 'Rule Engine initialized:' in line:
            # Look ahead for rule summary information
            summary_data = {'enabled_rules': 0, 'total_rules': 0, 'rules_by_category': {}}
            j = i + 1
            while j < len(lines) and j < i + 10:  # Look ahead max 10 lines
                next_line = lines[j].strip()
                if '/' in next_line and 'rules enabled' in next_line:
                    # Parse "X/Y rules enabled"
                    match = re.search(r'(\d+)/(\d+) rules enabled', next_line)
                    if match:
                        summary_data['enabled_rules'] = int(match.group(1))
                        summary_data['total_rules'] = int(match.group(2))
                elif next_line.startswith('- ') and ':' in next_line:
                    # Parse "- category: X rules"
                    category_match = re.search(r'- ([^:]+): (\d+) rules', next_line)
                    if category_match:
                        category = category_match.group(1).strip()
                        count = int(category_match.group(2))
                        summary_data['rules_by_category'][category] = list(range(count))
                elif next_line.startswith('[') or next_line == '':
                    break
                j += 1
            i = j - 1  # Set i to the last line we processed
            markdown_content += reporter.format_rule_engine_summary(summary_data)
            
        elif line.startswith('[QUERY]') and 'JQL Query:' in line:
            jql = line.replace('[QUERY] JQL Query:', '').strip()
            markdown_content += f"**JQL Query:** `{jql}`\n\n"
            
        elif line.startswith('[RESULTS]') and 'Found' in line:
            # Extract count information
            match = re.search(r'Found (\d+) (\w+) issues.*Total matching: (\d+)', line)
            if match:
                found_count, issue_type, total_count = match.groups()
                markdown_content += f"**Found:** {found_count} {issue_type} issues to check (Total matching: {total_count})\n\n"
                
        elif re.match(r'^\s*\d+\.\s+\w+:', line):
            # Issue details line (e.g., "1. Story: AP-1234")
            issue_match = re.match(r'^\s*(\d+)\.\s+(\w+):\s+(\w+-\d+)', line)
            if issue_match:
                issue_num, issue_type, issue_key = issue_match.groups()
                markdown_content += f"### {issue_num}. {issue_type}: {issue_key}\n\n"
            else:
                markdown_content += f"### {line}\n\n"
                
        elif line.startswith('Title:'):
            title = line.replace('Title:', '').strip()
            markdown_content += f"**Title:** {title}\n"
        elif line.startswith('Status:'):
            status = line.replace('Status:', '').strip()
            markdown_content += f"**Status:** {status}\n"
        elif line.startswith('Assignee:'):
            assignee = line.replace('Assignee:', '').strip()
            markdown_content += f"**Assignee:** {assignee}\n"
        elif line.startswith('URL:'):
            url = line.replace('URL:', '').strip()
            markdown_content += f"**URL:** [{url}]({url})\n\n"
            
        elif line.startswith('[TMF]') and 'TMF APIs Referenced:' in line:
            markdown_content += "**TMF APIs Referenced:**\n"
            # Look ahead for API details
            j = i + 1
            while j < len(lines):
                next_line = lines[j].strip()
                if next_line.startswith('- ') and ':' in next_line:
                    # API line like "- TMF622: Product Ordering Management (Latest: 4.1.0)"
                    api_info = next_line[2:].strip()  # Remove "- "
                    markdown_content += f"- **{api_info}**\n"
                elif next_line.startswith('Documentation:'):
                    doc_url = next_line.replace('Documentation:', '').strip()
                    markdown_content += f"  - Documentation: [{doc_url}]({doc_url})\n"
                elif not next_line.startswith(' ') and next_line != '':
                    break
                j += 1
            i = j - 1
            markdown_content += "\n"
            
        elif line.startswith('[VIOLATION]') or 'Rule Violation' in line:
            # Rule violation details - format as alert box
            violation_text = line.replace('[VIOLATION]', '').strip()
            markdown_content += f"⚠️ **{violation_text}**\n\n"
            
        elif line.startswith('[REPORT] LABEL USAGE REPORT'):
            markdown_content += "## Label Usage Report\n\n"
            
        elif line.startswith('Total unique labels:'):
            count = line.split(':')[1].strip()
            markdown_content += f"- **Total unique labels:** {count}\n"
        elif line.startswith('Total label usages:'):
            count = line.split(':')[1].strip()
            markdown_content += f"- **Total label usages:** {count}\n"
        elif line.startswith('Average labels per issue:'):
            avg = line.split(':')[1].strip()
            markdown_content += f"- **Average labels per issue:** {avg}\n\n"
            
        elif re.match(r'^\s*\d+\.\s+Label:', line):
            # Label details like "1. Label: 'api-first' (used 5 times)"
            label_match = re.search(r"Label: '([^']+)' \(used (\d+) times\)", line)
            if label_match:
                label_name, usage_count = label_match.groups()
                markdown_content += f"#### {line.split('.')[0].strip()}. Label: `{label_name}` (used {usage_count} times)\n\n"
                
        elif line.endswith('s (') and ')' in line:
            # Issue type grouping like "Stories (3):"
            markdown_content += f"**{line}**\n"
            
        elif line.startswith('- ') and ':' in line and 'http' in line:
            # Issue link line like "- AP-1234: Title... URL: http://..."
            parts = line.split('URL:')
            if len(parts) == 2:
                issue_info = parts[0].strip()[2:]  # Remove "- "
                url = parts[1].strip()
                # Extract issue key if present
                issue_key_match = re.match(r'(\w+-\d+):', issue_info)
                if issue_key_match:
                    issue_key = issue_key_match.group(1)
                    title = issue_info.replace(f'{issue_key}:', '').strip()
                    markdown_content += f"- [{issue_key}]({url}): {title}\n"
                else:
                    markdown_content += f"- {issue_info} - [Link]({url})\n"
                    
        elif line.startswith('[INSIGHTS]'):
            markdown_content += "### Label Insights\n\n"
            
        # Skip over separator lines and other formatting
        elif line.startswith('=') or line.startswith('-'):
            pass
        elif line.startswith('[') and line.endswith(']'):
            # Other bracketed sections - treat as subheadings
            section_name = line[1:-1]
            markdown_content += f"### {section_name}\n\n"
        else:
            # Regular text line
            if line.strip():
                markdown_content += f"{line}\n"
        
        i += 1
    
    markdown_content += reporter.finish_report()
    return markdown_content