# Multi-Issue Type Data Quality Checker Usage Guide

## Overview

The `check_issues.py` script extends the modular rule engine to work with **all JIRA issue types** in the AP project, not just EPICs. It uses the same robust rule architecture but applies it across Stories, Tasks, Bugs, Sub-tasks, and EPICs.

## 🚀 Usage

### **Check All Issue Types** (Default)
```bash
python check_issues.py
```

This will check all issue types:
- Stories
- Tasks  
- Bugs
- EPICs
- Sub-tasks

### **Check Specific Issue Type**
```bash
python check_issues.py Story 25          # Check 25 Stories
python check_issues.py Task 50           # Check 50 Tasks  
python check_issues.py Bug 10            # Check 10 Bugs
python check_issues.py "Sub-task" 20     # Check 20 Sub-tasks
```

## 📊 What It Checks

### **Universal Rules** (Apply to All Issue Types)
- ✅ Assignment validation (assigned to active users)
- ✅ Component assignments 
- ✅ Description quality
- ✅ Fix version management
- ✅ Staleness detection
- ✅ Priority validation
- ✅ Update frequency

### **Issue-Type Specific Rules**
- ✅ **Sub-tasks**: Must have parent issues
- ✅ **Stories**: Large stories should consider sub-tasks
- ✅ **High Priority**: More frequent update requirements
- ✅ **In Progress Timeframes**: Different limits per issue type
  - EPICs: 365 days
  - Stories: 60 days
  - Tasks: 30 days
  - Bugs: 14 days
  - Sub-tasks: 7 days

## 🎯 Sample Output

```
🔍 CHECKING STORY ISSUES
================================================================================
📊 JQL Query: project = AP AND type = "Story" AND status not in ("Closed", "Resolved", "Done") AND (updated >= "-6M" OR status = "In Progress")

📈 Results: Found 15 Story issues to check (Total matching: 15)

 1. Story: AP-12345
    Title: Implement user authentication
    Status: In Progress
    Assignee: John Doe
    URL: https://jira.company.com/browse/AP-12345
    ✅ Assigned to: John Doe
    ✅ Has 2 components: Authentication, Security
    ✅ Has description (156 characters)
    ✅ Priority: High
    ⚠️ Story [AP-12345] in progress for 45 days (>60 day threshold)
       💡 Suggestion: Review story scope and progress

📊 Story Summary:
   Issues checked: 15
   Total violations: 8
   Violations by severity:
     WARNING: 6
     ERROR: 2
   Average violations per issue: 0.5
   ✅ Data Quality: GOOD - Minor issues found
```

## 🔧 New Rules Added

### **HighPriorityStaleRule**
- **Purpose**: High priority issues should be updated frequently
- **Threshold**: 7 days for high/highest/critical/blocker priorities
- **Severity**: ERROR

### **MissingPriorityRule**  
- **Purpose**: All issues should have priorities for planning
- **Severity**: WARNING

### **InProgressTooLongRule**
- **Purpose**: Different issue types have different reasonable timeframes
- **Adaptive Thresholds**: Based on issue complexity
- **Severity**: WARNING

### **SubTaskOrphanRule**
- **Purpose**: Maintain proper parent-child relationships
- **Applies To**: Sub-tasks (must have parents) and large Stories (should consider sub-tasks)
- **Severity**: ERROR for sub-tasks, INFO for stories

## 📈 Quality Assessment

The script provides automatic quality assessment:

- 🏆 **EXCELLENT**: No violations found
- ✅ **GOOD**: < 2 violations per issue  
- ⚠️ **NEEDS ATTENTION**: 2-5 violations per issue
- ❌ **POOR**: > 5 violations per issue

## 🛠️ Configuration

Same configuration system as `check_epics.py`:

### **Enable/Disable Rules**
```python
# In rule_config.py
'HighPriorityStaleRule': {'enabled': True},
'SubTaskOrphanRule': {'enabled': False},
```

### **Adjust Thresholds**
```python
'thresholds': {
    'stale_days': 180,
    'long_running_days': 365,
    'min_description_length': 10,
}
```

## 🎯 Benefits

### **Unified Quality Management**
- Same rule engine for all issue types
- Consistent quality standards
- Centralized configuration

### **Issue-Type Awareness**
- Rules adapt to issue type context
- Appropriate thresholds for different work items
- Relevant suggestions for each type

### **Scalable Architecture**
- Easy to add new issue types
- Simple to create type-specific rules
- Maintainable rule organization

## 📝 Examples

### **Development Team Workflow**
```bash
# Daily check for active development items
python check_issues.py Story 50
python check_issues.py Task 30
python check_issues.py Bug 20
```

### **QA Team Workflow**  
```bash
# Focus on bugs and testing items
python check_issues.py Bug 100
python check_issues.py "Sub-task" 50
```

### **Project Manager Workflow**
```bash
# Full project health check
python check_issues.py  # All types
```

## 🔄 Integration

The script integrates seamlessly with:
- Existing JIRA API client
- Same authentication system
- Same error handling
- Same output formatting
- Same rule configuration

## 💡 Pro Tips

1. **Regular Checks**: Run weekly for each team's primary issue types
2. **CI/CD Integration**: Add to automated quality gates
3. **Team Dashboards**: Parse output for metrics tracking
4. **Custom Rules**: Extend for team-specific quality requirements
5. **Filtering**: Use JQL customization for specific project areas

Your JIRA data quality system now supports **comprehensive multi-issue type validation** with the same robust, modular architecture! 🎉