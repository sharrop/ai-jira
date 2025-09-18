"""
Assignment-related data quality rules for JIRA EPICs.

These rules check for issues related to assignee management and user assignments.
"""

from typing import Dict, List, Any
from rules.base_rule import BaseRule, RuleResult, RuleSeverity, RuleCategory


class UnassignedEpicRule(BaseRule):
    """Check if EPIC is assigned to someone"""
    
    def get_category(self) -> RuleCategory:
        return RuleCategory.ASSIGNMENT
        
    def get_severity(self) -> RuleSeverity:
        return RuleSeverity.WARNING
        
    def get_description(self) -> str:
        return "Check if EPIC is assigned to someone"
        
    def check(self, issue: Dict[str, Any], context: Dict[str, Any]) -> List[RuleResult]:
        assignee = issue.get('assignee')
        status = issue.get('status')
        issue_key = str(issue.get('key', 'UNKNOWN'))
        issue_type = context.get('issue_type', 'issue')
        
        # Only check issues that are in progress-like states
        if not status or status.lower() not in ['in progress', 'in development', 'in review', 'testing']:
            return []
        
        if not assignee or assignee == 'Unassigned':
            return [RuleResult(
                rule_id=self.rule_id,
                severity=self.severity,
                message=f"{issue_type.upper()} [{issue_key}] is in progress but not assigned to anyone",
                issue_key=issue_key,
                passed=False,
                suggestion=f"Assign the {issue_type.lower()} to a team member responsible for its delivery"
            )]
        
        return [RuleResult(
            rule_id=self.rule_id,
            severity=RuleSeverity.INFO,
            message=f"Assigned to: {assignee}",
            issue_key=issue_key,
            passed=True
        )]


class InactiveAssigneeRule(BaseRule):
    """Check if assignee is an active user"""
    
    def get_category(self) -> RuleCategory:
        return RuleCategory.ASSIGNMENT
        
    def get_severity(self) -> RuleSeverity:
        return RuleSeverity.ERROR
        
    def get_description(self) -> str:
        return "Check if assignee is an active user"
        
    def check(self, issue: Dict[str, Any], context: Dict[str, Any]) -> List[RuleResult]:
        assignee = issue.get('assignee')
        issue_key = str(issue.get('key', 'UNKNOWN'))
        
        # Skip if no assignee
        if not assignee or assignee == 'Unassigned':
            return []
            
        # Check if assignee is active (from raw fields)
        fields = issue.get('raw_fields', {})
        assignee_data = fields.get('assignee', {})
        is_active = assignee_data.get('active', True)
        issue_type = context.get('issue_type', 'issue')
        
        if not is_active:
            return [RuleResult(
                rule_id=self.rule_id,
                severity=self.severity,
                message=f"{issue_type.upper()} [{issue_key}] is assigned to an inactive user: {assignee}",
                issue_key=issue_key,
                passed=False,
                suggestion="Reassign to an active team member"
            )]
        
        return [RuleResult(
            rule_id=self.rule_id,
            severity=RuleSeverity.INFO,
            message=f"Assignee {assignee} is active",
            issue_key=issue_key,
            passed=True
        )]