"""
Rule engine for executing data quality rules against JIRA issues.

This module orchestrates the execution of rules and provides reporting capabilities.
"""

from typing import List, Dict, Any, Optional
from collections import defaultdict
import importlib
import pkgutil
from pathlib import Path

from rules.base_rule import BaseRule, RuleResult, RuleSeverity, RuleCategory


class RuleEngine:
    """Engine for running data quality rules against JIRA issues"""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the rule engine.
        
        Args:
            config: Configuration dictionary for enabling/disabling rules
        """
        self.config = config or {}
        self.rules: List[BaseRule] = []
        self._load_rules()
        
    def _load_rules(self):
        """Automatically discover and load all rule classes"""
        try:
            # Import specific rule modules manually for now
            rule_modules = [
                'rules.assignment_rules',
                'rules.metadata_rules', 
                'rules.workflow_rules',
                'rules.business_rules',
                'rules.tmf_rules'
            ]
            
            for module_name in rule_modules:
                try:
                    module = importlib.import_module(module_name)
                    # Find all classes that inherit from BaseRule
                    for attr_name in dir(module):
                        attr = getattr(module, attr_name)
                        if (isinstance(attr, type) and 
                            issubclass(attr, BaseRule) and 
                            attr != BaseRule):
                            # Check if rule is enabled in config
                            if self._is_rule_enabled(attr.__name__):
                                self.rules.append(attr())
                except ImportError as e:
                    print(f"Warning: Could not import rule module {module_name}: {e}")
                        
        except Exception as e:
            print(f"Warning: Error loading rules: {e}")
            
    def _is_rule_enabled(self, rule_name: str) -> bool:
        """Check if a rule is enabled in the configuration"""
        rules_config = self.config.get('rules', {})
        rule_config = rules_config.get(rule_name, {})
        return rule_config.get('enabled', True)  # Default to enabled
        
    def add_rule(self, rule: BaseRule):
        """Manually add a rule to the engine"""
        self.rules.append(rule)
        
    def remove_rule(self, rule_id: str):
        """Remove a rule by its ID"""
        self.rules = [rule for rule in self.rules if rule.rule_id != rule_id]
        
    def run_rules(self, issue: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> List[RuleResult]:
        """
        Run all applicable rules against an issue.
        
        Args:
            issue: Processed JIRA issue data
            context: Additional context data (components, users, etc.)
            
        Returns:
            List of RuleResult objects
        """
        context = context or {}
        all_results = []
        
        for rule in self.rules:
            try:
                # Check if rule applies to this issue
                if rule.is_applicable(issue):
                    results = rule.check(issue, context)
                    all_results.extend(results)
            except Exception as e:
                # Log error but continue with other rules
                print(f"⚠️ Error running rule {rule.rule_id}: {e}")
                # Create an error result
                error_result = RuleResult(
                    rule_id=rule.rule_id,
                    severity=RuleSeverity.ERROR,
                    message=f"Rule execution failed: {str(e)}",
                    issue_key=issue.get('key', 'UNKNOWN'),
                    passed=False
                )
                all_results.append(error_result)
                
        return all_results
    
    def get_rule_summary(self) -> Dict[str, Any]:
        """Get summary of loaded rules"""
        by_category = defaultdict(list)
        by_severity = defaultdict(list)
        
        for rule in self.rules:
            by_category[rule.category.value].append(rule.rule_id)
            by_severity[rule.severity.value].append(rule.rule_id)
            
        return {
            'total_rules': len(self.rules),
            'enabled_rules': len(self.rules),  # All loaded rules are enabled
            'rules_by_category': dict(by_category),
            'rules_by_severity': dict(by_severity),
            'loaded_rules': [rule.rule_id for rule in self.rules]
        }
    
    def get_rules_by_category(self, category: RuleCategory) -> List[BaseRule]:
        """Get all rules for a specific category"""
        return [rule for rule in self.rules if rule.category == category]
        
    def get_rules_by_severity(self, severity: RuleSeverity) -> List[BaseRule]:
        """Get all rules for a specific severity level"""
        return [rule for rule in self.rules if rule.severity == severity]


class RuleReporter:
    """Helper class for formatting and displaying rule results"""
    
    @staticmethod
    def display_results(results: List[RuleResult], 
                       show_passed: bool = False,
                       group_by_severity: bool = True) -> None:
        """
        Display rule results in a formatted way.
        
        Args:
            results: List of rule results to display
            show_passed: Whether to show passed checks
            group_by_severity: Whether to group results by severity
        """
        if not results:
            print("    ✅ No issues found")
            return
            
        if group_by_severity:
            RuleReporter._display_grouped_results(results, show_passed)
        else:
            RuleReporter._display_linear_results(results, show_passed)
    
    @staticmethod
    def _display_grouped_results(results: List[RuleResult], show_passed: bool):
        """Display results grouped by severity"""
        by_severity = defaultdict(list)
        
        for result in results:
            if result.passed and not show_passed:
                continue
            by_severity[result.severity].append(result)
            
        # Display in order of severity
        severity_order = [RuleSeverity.CRITICAL, RuleSeverity.ERROR, 
                         RuleSeverity.WARNING, RuleSeverity.INFO]
        
        for severity in severity_order:
            if severity in by_severity:
                for result in by_severity[severity]:
                    print(f"    {result}")
    
    @staticmethod
    def _display_linear_results(results: List[RuleResult], show_passed: bool):
        """Display results in linear order"""
        for result in results:
            if result.passed and not show_passed:
                continue
            print(f"    {result}")
    
    @staticmethod
    def get_summary_stats(results: List[RuleResult]) -> Dict[str, Any]:
        """Get summary statistics for rule results"""
        total = len(results)
        passed = sum(1 for r in results if r.passed)
        failed = total - passed
        
        by_severity = defaultdict(int)
        for result in results:
            if not result.passed:
                by_severity[result.severity.value] += 1
                
        return {
            'total_checks': total,
            'passed': passed,
            'failed': failed,
            'pass_rate': round((passed / total * 100) if total > 0 else 0, 1),
            'failures_by_severity': dict(by_severity)
        }