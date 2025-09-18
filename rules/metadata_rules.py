"""
Metadata-related data quality rules for JIRA EPICs.

These rules check for issues related to components, versions, labels, and other metadata.
"""

from typing import Dict, List, Any
from rules.base_rule import BaseRule, RuleResult, RuleSeverity, RuleCategory


class MissingComponentsRule(BaseRule):
    """Check if EPIC has components assigned"""
    
    def get_category(self) -> RuleCategory:
        return RuleCategory.METADATA
        
    def get_severity(self) -> RuleSeverity:
        return RuleSeverity.WARNING
        
    def get_description(self) -> str:
        return "Check if EPIC has components assigned"
        
    def check(self, issue: Dict[str, Any], context: Dict[str, Any]) -> List[RuleResult]:
        components = issue.get('components', [])
        issue_key = str(issue.get('key', 'UNKNOWN'))
        summary = issue.get('summary', '')
        
        if not components:
            # Try to suggest components based on TMF number in title
            suggestion = None
            if 'TMF' in summary:
                tmf_number = summary.split('TMF')[-1].strip().split(' ')[0].strip('E')
                component_names = context.get('components', [])
                matching_components = [name for name in component_names if name and tmf_number in name]
                
                if matching_components:
                    suggestion = f"Consider adding component(s): {', '.join(matching_components)}"
                else:
                    suggestion = f"No matching components found for TMF number {tmf_number}"
            else:
                suggestion = "Add relevant component(s) to categorize this EPIC"
            
            return [RuleResult(
                rule_id=self.rule_id,
                severity=self.severity,
                message=f"EPIC [{issue_key}] has no components set",
                issue_key=issue_key,
                passed=False,
                suggestion=suggestion
            )]
        
        component_names = [comp.get('name', 'Unknown') for comp in components if isinstance(comp, dict)]
        return [RuleResult(
            rule_id=self.rule_id,
            severity=RuleSeverity.INFO,
            message=f"Has {len(component_names)} components: {', '.join(component_names)}",
            issue_key=issue_key,
            passed=True
        )]


class MissingFixVersionRule(BaseRule):
    """Check if EPIC has a fix version set"""
    
    def get_category(self) -> RuleCategory:
        return RuleCategory.METADATA
        
    def get_severity(self) -> RuleSeverity:
        return RuleSeverity.WARNING
        
    def get_description(self) -> str:
        return "Check if EPIC has a fix version set"
        
    def check(self, issue: Dict[str, Any], context: Dict[str, Any]) -> List[RuleResult]:
        fix_versions = issue.get('fixVersions', [])
        issue_key = str(issue.get('key', 'UNKNOWN'))
        
        if not fix_versions:
            return [RuleResult(
                rule_id=self.rule_id,
                severity=self.severity,
                message=f"EPIC [{issue_key}] has no FixVersion set",
                issue_key=issue_key,
                passed=False,
                suggestion="Set a target release version for this EPIC"
            )]
        
        version_names = [version.get('name', 'Unknown') for version in fix_versions]
        return [RuleResult(
            rule_id=self.rule_id,
            severity=RuleSeverity.INFO,
            message=f"FixVersion(s): {', '.join(version_names)}",
            issue_key=issue_key,
            passed=True
        )]


class LegacyFixVersionRule(BaseRule):
    """Check if EPIC fix version is less than 5.0"""
    
    def get_category(self) -> RuleCategory:
        return RuleCategory.METADATA
        
    def get_severity(self) -> RuleSeverity:
        return RuleSeverity.WARNING
        
    def get_description(self) -> str:
        return "Check if EPIC fix version is less than 5.0 (legacy)"
        
    def check(self, issue: Dict[str, Any], context: Dict[str, Any]) -> List[RuleResult]:
        fix_versions = issue.get('fixVersions', [])
        issue_key = str(issue.get('key', 'UNKNOWN'))
        results = []
        
        if not fix_versions:
            return []  # Handled by MissingFixVersionRule
            
        for version in fix_versions:
            version_name = version.get('name', '').strip('vVxX')
            version_number = version_name.split('.')[0] if '.' in version_name else version_name
            
            try:
                version_float = float(version_number)
                if version_float < 5.0:
                    results.append(RuleResult(
                        rule_id=self.rule_id,
                        severity=self.severity,
                        message=f"EPIC [{issue_key}] has legacy FixVersion {version_name} (< 5.0)",
                        issue_key=issue_key,
                        passed=False,
                        suggestion="Consider updating to a current release version"
                    ))
                else:
                    results.append(RuleResult(
                        rule_id=self.rule_id,
                        severity=RuleSeverity.INFO,
                        message=f"FixVersion {version_name} is current",
                        issue_key=issue_key,
                        passed=True
                    ))
            except ValueError:
                # Version name is not a number, skip validation
                results.append(RuleResult(
                    rule_id=self.rule_id,
                    severity=RuleSeverity.INFO,
                    message=f"FixVersion {version_name} format could not be validated",
                    issue_key=issue_key,
                    passed=True
                ))
        
        return results


class MissingDescriptionRule(BaseRule):
    """Check if EPIC has a description"""
    
    def get_category(self) -> RuleCategory:
        return RuleCategory.CONTENT
        
    def get_severity(self) -> RuleSeverity:
        return RuleSeverity.WARNING
        
    def get_description(self) -> str:
        return "Check if EPIC has a description"
        
    def check(self, issue: Dict[str, Any], context: Dict[str, Any]) -> List[RuleResult]:
        description = issue.get('description')
        issue_key = str(issue.get('key', 'UNKNOWN'))
        
        if not description or not description.strip():
            return [RuleResult(
                rule_id=self.rule_id,
                severity=self.severity,
                message=f"EPIC [{issue_key}] has no description",
                issue_key=issue_key,
                passed=False,
                suggestion="Add a clear description explaining the EPIC's purpose and acceptance criteria"
            )]
        
        # Check if description is too short
        min_length = context.get('thresholds', {}).get('min_description_length', 10)
        if len(description.strip()) < min_length:
            return [RuleResult(
                rule_id=self.rule_id,
                severity=RuleSeverity.WARNING,
                message=f"EPIC [{issue_key}] has a very short description ({len(description.strip())} chars)",
                issue_key=issue_key,
                passed=False,
                suggestion=f"Expand description to at least {min_length} characters with clear details"
            )]
        
        return [RuleResult(
            rule_id=self.rule_id,
            severity=RuleSeverity.INFO,
            message=f"Has description ({len(description.strip())} characters)",
            issue_key=issue_key,
            passed=True
        )]