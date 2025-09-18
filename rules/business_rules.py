"""
Business and planning-related data quality rules for JIRA issues.

These rules check for issues related to business planning, priority management, 
and project alignment that apply to various issue types.
"""

from typing import Dict, List, Any
from rules.base_rule import BaseRule, RuleResult, RuleSeverity, RuleCategory


class HighPriorityStaleRule(BaseRule):
    """Check if high priority issues are stale (not updated recently)"""
    
    def get_category(self) -> RuleCategory:
        return RuleCategory.BUSINESS
        
    def get_severity(self) -> RuleSeverity:
        return RuleSeverity.ERROR
        
    def get_description(self) -> str:
        return "Check if high priority issues are stale"
        
    def check(self, issue: Dict[str, Any], context: Dict[str, Any]) -> List[RuleResult]:
        priority = issue.get('priority')
        updated = issue.get('updated')
        issue_key = str(issue.get('key', 'UNKNOWN'))
        
        # Only check high priority issues
        if not priority or priority.lower() not in ['high', 'highest', 'critical', 'blocker']:
            return []
        
        if not updated:
            return [RuleResult(
                rule_id=self.rule_id,
                severity=self.severity,
                message=f"High priority issue [{issue_key}] has no update timestamp",
                issue_key=issue_key,
                passed=False,
                suggestion="Verify issue status and update immediately"
            )]
        
        from datetime import datetime, timedelta
        
        try:
            updated_date = datetime.strptime(updated[:10], '%Y-%m-%d')
            days_since_update = (datetime.now() - updated_date).days
            
            # High priority issues should be updated within 7 days
            if days_since_update > 7:
                return [RuleResult(
                    rule_id=self.rule_id,
                    severity=self.severity,
                    message=f"High priority issue [{issue_key}] not updated in {days_since_update} days",
                    issue_key=issue_key,
                    passed=False,
                    suggestion="High priority issues should be updated weekly - review and update status"
                )]
            
            return [RuleResult(
                rule_id=self.rule_id,
                severity=RuleSeverity.INFO,
                message=f"High priority issue updated {days_since_update} days ago (acceptable)",
                issue_key=issue_key,
                passed=True
            )]
            
        except (ValueError, TypeError):
            return [RuleResult(
                rule_id=self.rule_id,
                severity=RuleSeverity.WARNING,
                message=f"Issue [{issue_key}] has invalid update date format: {updated}",
                issue_key=issue_key,
                passed=False
            )]


class MissingPriorityRule(BaseRule):
    """Check if issue has a priority set"""
    
    def get_category(self) -> RuleCategory:
        return RuleCategory.BUSINESS
        
    def get_severity(self) -> RuleSeverity:
        return RuleSeverity.WARNING
        
    def get_description(self) -> str:
        return "Check if issue has a priority set"
        
    def check(self, issue: Dict[str, Any], context: Dict[str, Any]) -> List[RuleResult]:
        priority = issue.get('priority')
        issue_key = str(issue.get('key', 'UNKNOWN'))
        issue_type = context.get('issue_type', 'Issue')
        
        if not priority:
            return [RuleResult(
                rule_id=self.rule_id,
                severity=self.severity,
                message=f"{issue_type} [{issue_key}] has no priority set",
                issue_key=issue_key,
                passed=False,
                suggestion="Set appropriate priority to help with planning and resource allocation"
            )]
        
        return [RuleResult(
            rule_id=self.rule_id,
            severity=RuleSeverity.INFO,
            message=f"Priority: {priority}",
            issue_key=issue_key,
            passed=True
        )]


class InProgressTooLongRule(BaseRule):
    """Check if issue has been in progress for too long based on issue type"""
    
    def get_category(self) -> RuleCategory:
        return RuleCategory.WORKFLOW
        
    def get_severity(self) -> RuleSeverity:
        return RuleSeverity.WARNING
        
    def get_description(self) -> str:
        return "Check if issue has been in progress too long for its type"
        
    def check(self, issue: Dict[str, Any], context: Dict[str, Any]) -> List[RuleResult]:
        status = issue.get('status')
        created = issue.get('created')
        issue_key = str(issue.get('key', 'UNKNOWN'))
        issue_type = context.get('issue_type', 'Issue')
        
        # Only check issues in progress-like states
        if not status or status.lower() not in ['in progress', 'in development', 'in review', 'testing']:
            return []
            
        if not created:
            return []
        
        from datetime import datetime
        
        try:
            created_date = datetime.strptime(created[:10], '%Y-%m-%d')
            days_in_progress = (datetime.now() - created_date).days
            
            # Different thresholds for different issue types
            thresholds = {
                'Epic': 365,      # 1 year for EPICs
                'Story': 60,      # 2 months for Stories
                'Task': 30,       # 1 month for Tasks
                'Bug': 14,        # 2 weeks for Bugs
                'Sub-task': 7     # 1 week for Sub-tasks
            }
            
            threshold = thresholds.get(issue_type, 30)  # Default 30 days
            
            if days_in_progress > threshold:
                return [RuleResult(
                    rule_id=self.rule_id,
                    severity=self.severity,
                    message=f"{issue_type} [{issue_key}] in progress for {days_in_progress} days (>{threshold} day threshold)",
                    issue_key=issue_key,
                    passed=False,
                    suggestion=f"Review {issue_type.lower()} scope and progress - consider breaking down or reassigning"
                )]
            
            return [RuleResult(
                rule_id=self.rule_id,
                severity=RuleSeverity.INFO,
                message=f"In progress for {days_in_progress} days (within {threshold} day threshold)",
                issue_key=issue_key,
                passed=True
            )]
            
        except (ValueError, TypeError):
            return [RuleResult(
                rule_id=self.rule_id,
                severity=RuleSeverity.WARNING,
                message=f"Issue [{issue_key}] has invalid creation date format: {created}",
                issue_key=issue_key,
                passed=False
            )]


class SubTaskOrphanRule(BaseRule):
    """Check if sub-tasks have parent issues and stories have child tasks"""
    
    def get_category(self) -> RuleCategory:
        return RuleCategory.WORKFLOW
        
    def get_severity(self) -> RuleSeverity:
        return RuleSeverity.ERROR
        
    def get_description(self) -> str:
        return "Check parent-child relationships for sub-tasks and stories"
        
    def is_applicable(self, issue: Dict[str, Any]) -> bool:
        """Only apply to Sub-tasks and Stories"""
        issue_type = issue.get('issue_type', '')
        return issue_type in ['Sub-task', 'Story']
        
    def check(self, issue: Dict[str, Any], context: Dict[str, Any]) -> List[RuleResult]:
        issue_type = issue.get('issue_type', '')
        issue_key = str(issue.get('key', 'UNKNOWN'))
        linked_issues = issue.get('issues', [])
        
        if issue_type == 'Sub-task':
            # Sub-tasks should have a parent
            has_parent = any(
                link.get('type', {}).get('name', '').lower() in ['parent', 'parent of', 'subtask of']
                for link in linked_issues
            )
            
            if not has_parent:
                return [RuleResult(
                    rule_id=self.rule_id,
                    severity=self.severity,
                    message=f"Sub-task [{issue_key}] has no parent issue",
                    issue_key=issue_key,
                    passed=False,
                    suggestion="Link this sub-task to its parent Story or Epic"
                )]
                
        elif issue_type == 'Story':
            # Large stories might benefit from having sub-tasks
            # This is a softer check - we'll make it INFO level
            has_subtasks = any(
                link.get('type', {}).get('name', '').lower() in ['subtask', 'sub-task of', 'child of']
                for link in linked_issues
            )
            
            # Only flag if it's a large story (has many components or long description)
            components = issue.get('components', [])
            description = issue.get('description', '')
            
            if (len(components) > 2 or len(description) > 500) and not has_subtasks:
                return [RuleResult(
                    rule_id=self.rule_id,
                    severity=RuleSeverity.INFO,
                    message=f"Large Story [{issue_key}] might benefit from sub-tasks",
                    issue_key=issue_key,
                    passed=True,  # This is just a suggestion
                    suggestion="Consider breaking this large story into smaller sub-tasks for better tracking"
                )]
        
        return [RuleResult(
            rule_id=self.rule_id,
            severity=RuleSeverity.INFO,
            message=f"{issue_type} relationships look good",
            issue_key=issue_key,
            passed=True
        )]