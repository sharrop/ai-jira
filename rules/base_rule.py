"""
Base classes and enums for JIRA data quality rules.

This module provides the foundation for implementing modular data quality checks
for JIRA issues. Each rule inherits from BaseRule and implements specific validation logic.
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
from enum import Enum
from datetime import datetime


class RuleSeverity(Enum):
    """Severity levels for rule violations"""
    INFO = "INFO"
    WARNING = "WARNING" 
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class RuleCategory(Enum):
    """Categories to group related rules"""
    ASSIGNMENT = "assignment"
    METADATA = "metadata"
    WORKFLOW = "workflow"
    BUSINESS = "business"
    CONTENT = "content"
    PERFORMANCE = "performance"
    COMPLIANCE = "compliance"


class RuleResult:
    """Result of running a rule against an issue"""
    
    def __init__(self, rule_id: str, severity: RuleSeverity, 
                 message: str, issue_key: str, passed: bool = False,
                 suggestion: Optional[str] = None):
        self.rule_id = rule_id
        self.severity = severity
        self.message = message
        self.issue_key = issue_key
        self.passed = passed
        self.suggestion = suggestion  # Optional suggestion for fixing the issue
        self.timestamp = datetime.now()
    
    def __str__(self):
        status = "[PASS]" if self.passed else self._get_severity_icon()
        base = f"{status} {self.message}"
        if self.suggestion and not self.passed:
            base += f"\n      [SUGGESTION] {self.suggestion}"
        return base
    
    def _get_severity_icon(self) -> str:
        """Get icon for severity level"""
        icons = {
            RuleSeverity.INFO: "[INFO]",
            RuleSeverity.WARNING: "[WARNING]",
            RuleSeverity.ERROR: "[ERROR]",
            RuleSeverity.CRITICAL: "[CRITICAL]"
        }
        return icons.get(self.severity, "[UNKNOWN]")


class BaseRule(ABC):
    """Abstract base class for all data quality rules"""
    
    def __init__(self):
        self.rule_id = self.__class__.__name__
        self.category = self.get_category()
        self.severity = self.get_severity()
        self.description = self.get_description()
        
    @abstractmethod
    def check(self, issue: Dict[str, Any], context: Dict[str, Any]) -> List[RuleResult]:
        """
        Check the rule against an issue and return results.
        
        Args:
            issue: Processed JIRA issue data
            context: Additional context (components, users, etc.)
            
        Returns:
            List of RuleResult objects
        """
        pass
    
    @abstractmethod 
    def get_category(self) -> RuleCategory:
        """Return the category this rule belongs to"""
        pass
        
    @abstractmethod
    def get_severity(self) -> RuleSeverity:
        """Return the default severity for this rule"""
        pass
        
    @abstractmethod
    def get_description(self) -> str:
        """Return human-readable description of what this rule checks"""
        pass
    
    def is_applicable(self, issue: Dict[str, Any]) -> bool:
        """
        Check if this rule applies to the given issue.
        Override this method if the rule only applies to certain issue types.
        
        Args:
            issue: Processed JIRA issue data
            
        Returns:
            True if rule should be applied to this issue
        """
        return True
    
    def __str__(self):
        return f"{self.rule_id} ({self.category.value}, {self.severity.value}): {self.description}"