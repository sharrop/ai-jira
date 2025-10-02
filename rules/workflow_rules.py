"""
Workflow and timeline-related data quality rules for JIRA EPICs.

These rules check for issues related to statu    def check(self, issue: Dict[str, Any], context: Dict[str, Any]) -> List[RuleResult]:
        status = issue.get('status')
        created = issue.get('created')
        issue_key = str(issue.get('key', 'UNKNOWN'))
        issue_type = context.get('issue_type', 'issue')
        
        # Only check EPICs that are "In Progress"
        if status != "In Progress":
            return []
            
        if not created:
            return [RuleResult(
                rule_id=self.rule_id,
                severity=self.severity,
                message=f"{issue_type.upper()} [{issue_key}] has no creation timestamp",
                issue_key=issue_key,
                passed=False
            )]rkflow management.
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
        issue_type = context.get('issue_type', 'issue')
        
        if not updated:
            return [RuleResult(
                rule_id=self.rule_id,
                severity=self.severity,
                message=f"{issue_type.upper()} [{issue_key}] has no update timestamp",
                issue_key=issue_key,
                passed=False,
                suggestion=f"Verify {issue_type.lower()} status and update if necessary"
            )]
        
        # Get threshold from context or use default
        stale_days = context.get('thresholds', {}).get('stale_days', 180)
        
        try:
            # Parse the full JIRA datetime format for more accurate calculation
            import re
            
            # Clean the date string to handle JIRA's ISO format
            clean_date = re.sub(r'\.\d{3}\+\d{4}$|Z$', '', updated)
            
            if 'T' in clean_date:
                # Full datetime format
                updated_date = datetime.strptime(clean_date, '%Y-%m-%dT%H:%M:%S')
            else:
                # Date only format (fallback)
                updated_date = datetime.strptime(updated[:10], '%Y-%m-%d')
            
            # Calculate more precise time difference
            time_diff = datetime.now() - updated_date
            days_since_update = int(time_diff.total_seconds() / 86400)  # 86400 seconds = 1 day
            hours_since_update = time_diff.total_seconds() / 3600
            
            if days_since_update > stale_days:
                return [RuleResult(
                    rule_id=self.rule_id,
                    severity=self.severity,
                    message=f"{issue_type.upper()} [{issue_key}] has not been updated in {days_since_update} days (since {updated[:10]})",
                    issue_key=issue_key,
                    passed=False,
                    suggestion=f"Review and update {issue_type.lower()} status - no activity for over {stale_days} days"
                )]
            
            # More informative message showing both days and hours for recent updates
            if days_since_update == 0:
                return [RuleResult(
                    rule_id=self.rule_id,
                    severity=RuleSeverity.INFO,
                    message=f"Updated {hours_since_update:.1f} hours ago (today)",
                    issue_key=issue_key,
                    passed=True
                )]
            elif days_since_update == 1:
                return [RuleResult(
                    rule_id=self.rule_id,
                    severity=RuleSeverity.INFO,
                    message=f"Updated {days_since_update} day ago ({hours_since_update:.1f} hours)",
                    issue_key=issue_key,
                    passed=True
                )]
            else:
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
                message=f"{issue_type.upper()} [{issue_key}] has invalid update date format: {updated}",
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
        issue_type = context.get('issue_type', 'issue')
        
        # Only check EPICs that are "In Progress"
        if status != "In Progress":
            return []
            
        if not created:
            return [RuleResult(
                rule_id=self.rule_id,
                severity=self.severity,
                message=f"{issue_type.upper()} [{issue_key}] has no creation timestamp",
                issue_key=issue_key,
                passed=False
            )]
        
        # Get threshold from context or use default
        long_running_days = context.get('thresholds', {}).get('long_running_days', 365)
        
        try:
            # Parse the full JIRA datetime format for more accurate calculation
            import re
            
            # Clean the date string to handle JIRA's ISO format
            clean_date = re.sub(r'\.\d{3}\+\d{4}$|Z$', '', created)
            
            if 'T' in clean_date:
                # Full datetime format
                created_date = datetime.strptime(clean_date, '%Y-%m-%dT%H:%M:%S')
            else:
                # Date only format (fallback)
                created_date = datetime.strptime(created[:10], '%Y-%m-%d')
            
            # Calculate more precise time difference
            time_diff = datetime.now() - created_date
            days_in_progress = int(time_diff.total_seconds() / 86400)
            
            if days_in_progress > long_running_days:
                return [RuleResult(
                    rule_id=self.rule_id,
                    severity=self.severity,
                    message=f"{issue_type.upper()} [{issue_key}] has been 'In Progress' for {days_in_progress} days (created {created[:10]})",
                    issue_key=issue_key,
                    passed=False,
                    suggestion=f"Review {issue_type.lower()} scope - in progress for over {long_running_days} days. Consider breaking into smaller items."
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
                message=f"{issue_type.upper()} [{issue_key}] has invalid creation date format: {created}",
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
        issue_type = context.get('issue_type', 'issue')
        
        # Only check Epics for linked issues (Epics should coordinate multiple work items)
        if issue_type.upper() != 'EPIC':
            return []
        
        if not issues:
            return [RuleResult(
                rule_id=self.rule_id,
                severity=self.severity,
                message=f"{issue_type.upper()} [{issue_key}] has no linked JIRAs",
                issue_key=issue_key,
                passed=False,
                suggestion=f"Link related stories, tasks, or bugs to this {issue_type.lower()}"
            )]
        
        return [RuleResult(
            rule_id=self.rule_id,
            severity=RuleSeverity.INFO,
            message=f"Has {len(issues)} linked issues",
            issue_key=issue_key,
            passed=True
        )]