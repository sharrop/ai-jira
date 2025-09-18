"""
Workflow and timeline-related data quality rules for JIRA EPICs.

These rules check for issues related to status, timing, and workflow management.
"""

from typing import Dict, List, Any
from datetime import datetime, timedelta
from rules.base_rule import BaseRule, RuleResult, RuleSeverity, RuleCategory


class StaleEpicRule(BaseRule):
    """Check if EPIC has not been updated in a long time"""
    
    def get_category(self) -> RuleCategory:
        return RuleCategory.WORKFLOW
        
    def get_severity(self) -> RuleSeverity:
        return RuleSeverity.WARNING
        
    def get_description(self) -> str:
        return "Check if EPIC has not been updated recently"
        
    def check(self, issue: Dict[str, Any], context: Dict[str, Any]) -> List[RuleResult]:
        updated = issue.get('updated')
        issue_key = str(issue.get('key', 'UNKNOWN'))
        
        if not updated:
            return [RuleResult(
                rule_id=self.rule_id,
                severity=self.severity,
                message=f"EPIC [{issue_key}] has no update timestamp",
                issue_key=issue_key,
                passed=False,
                suggestion="Verify EPIC status and update if necessary"
            )]
        
        # Get threshold from context or use default
        stale_days = context.get('thresholds', {}).get('stale_days', 180)
        
        try:
            updated_date = datetime.strptime(updated[:10], '%Y-%m-%d')
            days_since_update = (datetime.now() - updated_date).days
            
            if days_since_update > stale_days:
                return [RuleResult(
                    rule_id=self.rule_id,
                    severity=self.severity,
                    message=f"EPIC [{issue_key}] has not been updated in {days_since_update} days (since {updated[:10]})",
                    issue_key=issue_key,
                    passed=False,
                    suggestion=f"Review and update EPIC status - no activity for over {stale_days} days"
                )]
            
            return [RuleResult(
                rule_id=self.rule_id,
                severity=RuleSeverity.INFO,
                message=f"Updated {days_since_update} days ago",
                issue_key=issue_key,
                passed=True
            )]
            
        except (ValueError, TypeError) as e:
            return [RuleResult(
                rule_id=self.rule_id,
                severity=RuleSeverity.WARNING,
                message=f"EPIC [{issue_key}] has invalid update date format: {updated}",
                issue_key=issue_key,
                passed=False
            )]


class LongRunningEpicRule(BaseRule):
    """Check if EPIC has been in progress for too long"""
    
    def get_category(self) -> RuleCategory:
        return RuleCategory.WORKFLOW
        
    def get_severity(self) -> RuleSeverity:
        return RuleSeverity.WARNING
        
    def get_description(self) -> str:
        return "Check if EPIC has been in progress for too long"
        
    def check(self, issue: Dict[str, Any], context: Dict[str, Any]) -> List[RuleResult]:
        created = issue.get('created')
        status = issue.get('status')
        issue_key = str(issue.get('key', 'UNKNOWN'))
        
        # Only check EPICs that are "In Progress"
        if status != "In Progress":
            return []
            
        if not created:
            return [RuleResult(
                rule_id=self.rule_id,
                severity=self.severity,
                message=f"EPIC [{issue_key}] has no creation timestamp",
                issue_key=issue_key,
                passed=False
            )]
        
        # Get threshold from context or use default
        long_running_days = context.get('thresholds', {}).get('long_running_days', 365)
        
        try:
            created_date = datetime.strptime(created[:10], '%Y-%m-%d')
            days_in_progress = (datetime.now() - created_date).days
            
            if days_in_progress > long_running_days:
                return [RuleResult(
                    rule_id=self.rule_id,
                    severity=self.severity,
                    message=f"EPIC [{issue_key}] has been 'In Progress' for {days_in_progress} days (created {created[:10]})",
                    issue_key=issue_key,
                    passed=False,
                    suggestion=f"Review EPIC scope - in progress for over {long_running_days} days. Consider breaking into smaller EPICs."
                )]
            
            return [RuleResult(
                rule_id=self.rule_id,
                severity=RuleSeverity.INFO,
                message=f"In progress for {days_in_progress} days (reasonable timeframe)",
                issue_key=issue_key,
                passed=True
            )]
            
        except (ValueError, TypeError) as e:
            return [RuleResult(
                rule_id=self.rule_id,
                severity=RuleSeverity.WARNING,
                message=f"EPIC [{issue_key}] has invalid creation date format: {created}",
                issue_key=issue_key,
                passed=False
            )]


class NoLinkedIssuesRule(BaseRule):
    """Check if EPIC has linked issues"""
    
    def get_category(self) -> RuleCategory:
        return RuleCategory.CONTENT
        
    def get_severity(self) -> RuleSeverity:
        return RuleSeverity.WARNING
        
    def get_description(self) -> str:
        return "Check if EPIC has linked issues or child items"
        
    def check(self, issue: Dict[str, Any], context: Dict[str, Any]) -> List[RuleResult]:
        issues = issue.get('issues', [])
        issue_key = str(issue.get('key', 'UNKNOWN'))
        
        if not issues:
            return [RuleResult(
                rule_id=self.rule_id,
                severity=self.severity,
                message=f"EPIC [{issue_key}] has no linked JIRAs",
                issue_key=issue_key,
                passed=False,
                suggestion="Link related stories, tasks, or bugs to this EPIC"
            )]
        
        return [RuleResult(
            rule_id=self.rule_id,
            severity=RuleSeverity.INFO,
            message=f"Has {len(issues)} linked issues",
            issue_key=issue_key,
            passed=True
        )]