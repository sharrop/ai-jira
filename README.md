# JIRA Data Quality Management System

A comprehensive Python framework for validating and monitoring JIRA issue data quality across multiple issue types using a modular rule-based architecture.

## Overview

This system provides automated data quality checks for JIRA projects, focusing on the AP (Applications Portfolio) project. It uses a sophisticated rule engine to validate assignments, metadata, workflow states, and business processes across all JIRA issue types including Stories, Tasks, Bugs, EPICs, and Sub-tasks.

## Recent Enhancements

### New Rules Added
- **CommentCountInfoRule**: Track community engagement by showing comment counts for each issue
- **ToolingTransferRule**: Identify issues labeled or categorized as "Tooling" that should be transferred to Git-based issue tracking

### System Improvements
- **Dynamic Issue Type Support**: All rules now dynamically adapt messaging based on actual issue type (Task, Bug, Epic, etc.) instead of hardcoded "EPIC" references
- **Enhanced Component Detection**: Fixed JIRA API field name issues for proper component retrieval
- **Better Unicode Support**: Improved Windows CP1252 encoding compatibility for file output redirection
- **Comprehensive Rule Coverage**: Now 18+ active validation rules across 5 categories

## Features

### Core Capabilities
- **Multi-Issue Type Support**: Validates Stories, Tasks, Bugs, EPICs, and Sub-tasks
- **Modular Rule Architecture**: Extensible rule system with 18+ pre-built validation rules
- **Configurable Severity Levels**: INFO, WARNING, ERROR, and CRITICAL classifications
- **Adaptive Thresholds**: Issue-type-aware validation with appropriate timeframes
- **Comprehensive Reporting**: Detailed summaries with severity-based categorization
- **Dynamic Issue Type Detection**: Rules automatically adapt to different JIRA issue types
- **Comment Tracking**: Monitor community engagement through comment count reporting
- **Tooling Detection**: Identify tooling-related issues for potential Git migration
- **JQL Security**: Input validation and parameterization for secure JIRA queries

### Rule Categories
1. **Assignment Rules**: Validate user assignments and assignee status (2 rules)
2. **Metadata Rules**: Check components, fix versions, descriptions, and info display (6 rules)  
3. **Workflow Rules**: Monitor issue lifecycle and timing (4 rules)
4. **Business Rules**: Enforce priority management, planning standards, and tooling detection (4 rules)
5. **TMF API Rules**: Validate TMF API references and version currency (2 rules)

**Total: 18+ active validation rules** providing comprehensive quality assurance across all JIRA issue types.

### TMF API Integration
- **Automatic API Detection**: Identifies TMF API references in issue titles and descriptions
- **Version Validation**: Compares referenced versions against latest available TMF API versions
- **Documentation Linking**: Provides direct links to TMForum API documentation
- **104 TMF APIs**: Complete database of TMF APIs with version information
- **Interactive Lookup**: Standalone tool for quick TMF API information retrieval

## Architecture

### Modular Rule System
```
rules/
├── base_rule.py          # Abstract base classes and enums
├── assignment_rules.py   # User assignment validation
├── metadata_rules.py     # Component and version checks
├── workflow_rules.py     # Status and timeline validation
└── business_rules.py     # Priority and business logic rules
```

### Core Components
- **Rule Engine** (`rule_engine.py`): Orchestrates rule execution and reporting
- **Configuration** (`rule_config.py`): Manages rule settings and thresholds
- **JIRA Integration** (`jira_api.py`): Secure API client with authentication
- **Validation** (`jql_validator.py`): JQL query security and validation

## Setup

### Prerequisites
- Python 3.8+
- JIRA access credentials
- Network access to TMForum JIRA instance

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-jira
   ```

2. **Set up virtual environment** (recommended)
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure credentials**
   Create a `.env` file with your JIRA credentials:
   ```
   JIRA_USERNAME=your_username_here
   JIRA_PASSWORD=your_password_here
   ```

5. **Initial authentication**
   ```bash
   python login.py
   ```
   This captures session cookies for API access.

## Usage

### Multi-Issue Type Checker (Recommended)

Check all issue types in the AP project:
```bash
python check_issues.py
```

Check specific issue type with custom count:
```bash
python check_issues.py Story 50        # Check 50 Stories
python check_issues.py Task 25         # Check 25 Tasks
python check_issues.py Bug 100         # Check 100 Bugs
```

Supported issue types: `Story`, `Task`, `Bug`, `Epic`, `Sub-task`

### EPIC-Specific Checker

For EPIC-focused validation:
```bash
python check_epics.py
```

### Output Examples

**Enhanced Multi-Issue Type Reports:**
```
🔍 JIRA Data Quality Report for Tasks (43 issues checked)
════════════════════════════════════════════════════════

📊 SUMMARY:
   Total Issues: 43
   ✅ Passed: 28 (65%)
   ⚠️  Issues Found: 15 (35%)
   
🚨 CRITICAL: 1 issues
🔴 ERROR: 3 issues  
🟡 WARNING: 8 issues
ℹ️  INFO: 3 issues

🔍 RULE RESULTS:
UnassignedIssueRule: 3 violations (🔴 ERROR)
MissingComponentsRule: 5 violations (🟡 WARNING)
ToolingTransferRule: 6 violations (🟡 WARNING)
CommentCountInfoRule: 43 info results (ℹ️ INFO)
```

**New Rule Examples:**

*Comment Count Tracking:*
```
[PASS] No comments
[PASS] Has 1 comment  
[PASS] Has 3 comments
```

*Tooling Detection:*
```
[WARNING] TASK [AP-6536] has 'Tooling' component and should be transferred to Git
  [SUGGESTION] Consider transferring this task to a Git repository issue tracker and closing it in JIRA. Tooling-related work is better managed in Git where code changes are tracked.
```

*Dynamic Issue Type Support:*
```
[WARNING] TASK [AP-7080] is in progress but not assigned to anyone
[WARNING] BUG [AP-6114] has 'Tooling' component and should be transferred to Git  
[ERROR] SUB-TASK [AP-6544] has no parent issue
```

### TMF API Features

**Interactive TMF API Lookup:**
```bash
python tmf_lookup.py TMF646           # Lookup specific API
python tmf_lookup.py                  # Interactive mode
```

**Example TMF API Integration Output:**
```
1. Story: AP-1234
   Title: Implement TMF646 Appointment Management v2
   Status: In Progress
   Assignee: John Doe (john.doe@vodafone.com)
   URL: https://jira.example.com/browse/AP-1234
   🔗 TMF APIs Referenced:
      • TMF646: Appointment Management API (Latest: v4)
        📖 Documentation: https://www.tmforum.org/oda/open-apis/directory/appointment-management-api-TMF646/v4.0
   🔍 TMF API Analysis:
      ✅ ℹ️ References TMF646: Appointment Management API (Latest: v4)
      ❌ ⚠️ Issue references TMF646 v2 but latest available is v4
         💡 Consider updating to use current version v4
```

**TMF API Functions in Code:**
```python
from check_issues import get_tmf_api_info, find_tmf_references_in_text

# Look up API information
api_info = get_tmf_api_info("TMF646")
print(f"Latest version: {api_info['highest_version']}")

# Find TMF references in text
refs = find_tmf_references_in_text("Implement TMF646 and TMF629")
print(refs)  # ['TMF646', 'TMF629']
```

## Rule Configuration

### Enabling/Disabling Rules

Edit `rule_config.py` to customize rule behavior:

```python
DEFAULT_CONFIG = {
    "enabled_rules": {
        "UnassignedEpicRule": True,
        "MissingComponentsRule": True,
        "StaleEpicRule": False,  # Disable this rule
        # ... other rules
    },
    "thresholds": {
        "stale_days": 30,
        "long_running_days": 90,
        # ... other thresholds
    }
}
```

### Custom Thresholds

Adjust validation thresholds for your team's needs:

```python
"thresholds": {
    "stale_days": 21,              # Consider issues stale after 21 days
    "long_running_days": 180,      # Flag long-running issues
    "min_description_length": 50,  # Minimum description length
    "inactive_assignee_days": 90   # Flag inactive assignees
}
```

## Available Rules

### Assignment Rules
- **UnassignedEpicRule**: Identifies unassigned issues across all issue types
- **InactiveAssigneeRule**: Flags issues assigned to inactive users

### Metadata Rules
- **MissingComponentsRule**: Ensures issues have appropriate TMF components
- **MissingFixVersionRule**: Validates fix version assignment
- **LegacyFixVersionRule**: Identifies outdated fix versions (< 5.0)
- **MissingDescriptionRule**: Checks for adequate descriptions
- **LabelsInfoRule**: Displays assigned labels for visibility (INFO level)
- **CommentCountInfoRule**: Shows comment counts to track community engagement (INFO level)

### Workflow Rules
- **StaleEpicRule**: Finds issues without recent updates
- **LongRunningEpicRule**: Identifies unusually long-running issues
- **NoLinkedIssuesRule**: Validates issue relationships

### Business Rules
- **HighPriorityStaleRule**: High-priority issues requiring updates
- **MissingPriorityRule**: Issues without priority assignment
- **InProgressTooLongRule**: In-progress issues exceeding timeframes
- **SubTaskOrphanRule**: Sub-tasks without valid parent relationships
- **ToolingTransferRule**: Identifies tooling-related issues (by label or component) for potential Git migration

### TMF API Rules
- **TmfApiReferenceRule**: Provides TMF API information for referenced APIs
- **TmfApiVersionRule**: Validates TMF API version currency and warns about outdated references

## Extending the System

### Adding Custom Rules

1. Create a new rule class inheriting from `BaseRule`:

```python
# rules/custom_rules.py
from .base_rule import BaseRule, RuleResult, RuleSeverity, RuleCategory

class MyCustomRule(BaseRule):
    def __init__(self):
        super().__init__(
            name="MyCustomRule",
            description="Custom validation logic",
            category=RuleCategory.BUSINESS,
            severity=RuleSeverity.WARNING
        )
    
    def check(self, issue, context=None):
        # Your validation logic here
        if condition_not_met:
            return RuleResult(
                rule_name=self.name,
                issue_key=issue['key'],
                severity=self.severity,
                message="Custom validation failed",
                details={"field": "value"}
            )
        return None
    
    def is_applicable(self, issue_type):
        return issue_type in ['Story', 'Task']  # Apply to specific types
```

2. Add the rule to configuration in `rule_config.py`
3. Update the rule engine to load your custom module

### Integration Options

The system can be integrated into:
- **CI/CD Pipelines**: Automated quality gates
- **Scheduled Reports**: Daily/weekly data quality summaries
- **Dashboard Systems**: Real-time quality metrics
- **Team Workflows**: Pre-sprint planning validation

## Files and Documentation

### Core Files
- `check_issues.py` - Multi-issue type checker (primary interface)
- `check_epics.py` - EPIC-specific checker
- `rule_engine.py` - Rule orchestration and reporting
- `rule_config.py` - Configuration management
- `jira_api.py` - JIRA API integration

### Documentation
- `MULTI_ISSUE_CHECKER_GUIDE.md` - Comprehensive usage guide
- `JQL_VALIDATION_GUIDE.md` - JQL security and validation
- `API_README.md` - JIRA API integration details

### Generated Files
- `jira_cookies.json` - Session authentication cookies
- Debug logs and error screenshots as needed

## Security and Best Practices

### JQL Security
- All JQL queries use parameterization to prevent injection
- Input validation for user-provided parameters
- Sanitization of special characters and operators

### Authentication
- Secure credential storage in environment variables
- Session-based authentication with automatic cookie management
- Error handling for authentication failures

### Data Privacy
- No sensitive data stored in logs
- Configurable output formats to exclude sensitive fields
- Secure handling of API responses

## Troubleshooting

### Common Issues

1. **Authentication failures**
   ```bash
   python login.py  # Re-capture session cookies
   ```

2. **Rule execution errors**
   - Check rule configuration in `rule_config.py`
   - Verify JIRA field availability
   - Review error logs for specific rule failures

3. **Performance issues**
   - Reduce issue count for large datasets
   - Disable unnecessary rules
   - Use more specific JQL filters

4. **Tooling migration suggestions**
   - The ToolingTransferRule identifies issues that may benefit from Git repository migration
   - Suggestions appear for issues with "Tooling" labels or components
   - Consider these recommendations for workflow modernization and development efficiency

### Debug Mode

Enable detailed logging by modifying the checker scripts:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Interpreting New Rule Outputs

**Comment Count Information (INFO level)**:
- Shows the number of comments on each issue
- Helps identify issues that may need attention or have active discussions
- No action required - informational only

**Tooling Migration Suggestions (WARNING level)**:
- Identifies issues marked with "Tooling" labels or components
- Suggests considering Git repository migration for development efficiency
- Review these issues for potential workflow modernization opportunities

## License

This project is for internal data quality management. Ensure compliance with your organization's JIRA usage policies and data governance requirements.
