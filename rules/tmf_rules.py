"""
TMF API related validation rules for JIRA issues
"""

import re
import pandas as pd
from datetime import datetime
from .base_rule import BaseRule, RuleCategory, RuleSeverity, RuleResult
from typing import Dict, Any, Optional, List


class TmfApiVersionRule(BaseRule):
    """Check if JIRA issues referencing TMF APIs have outdated version information"""
    
    def get_category(self) -> RuleCategory:
        return RuleCategory.BUSINESS
    
    def get_severity(self) -> RuleSeverity:
        return RuleSeverity.WARNING
    
    def get_description(self) -> str:
        return "Validates that issues referencing TMF APIs use current versions"
    
    def check(self, issue: Dict[str, Any], context: Dict[str, Any]) -> List[RuleResult]:
        """
        Check if the issue references TMF APIs and validate version information
        
        Args:
            issue: Issue data dictionary
            context: Validation context
            
        Returns:
            List of RuleResult objects
        """
        results = []
        
        try:
            # Import here to avoid circular imports
            from check_issues import find_tmf_references_in_text, get_tmf_api_info
            
            # Search for TMF references in title and description
            title = issue.get('summary', '') or ''
            description = issue.get('description', '') or ''
            search_text = f"{title} {description}"
            
            tmf_refs = find_tmf_references_in_text(search_text)
            
            if not tmf_refs:
                return results  # No TMF references found
            
            for tmf_code in tmf_refs:
                api_info = get_tmf_api_info(tmf_code)
                
                if not api_info:
                    results.append(RuleResult(
                        rule_id=self.rule_id,
                        severity=self.severity,
                        message=f"Referenced TMF API '{tmf_code}' not found in API database",
                        issue_key=issue.get('key', 'Unknown'),
                        passed=False
                    ))
                    continue
                
                # Extract version information from various places
                issue_versions = self._extract_versions_from_issue(issue, title, description)
                latest_version = api_info.get('highest_version', 'Unknown')
                
                if latest_version == 'Unknown':
                    continue  # Skip if we don't know the latest version
                
                # Check if any referenced versions are outdated
                outdated_versions = self._check_for_outdated_versions(issue_versions, latest_version)
                
                if outdated_versions:
                    api_name = api_info.get('long_name', tmf_code)
                    results.append(RuleResult(
                        rule_id=self.rule_id,
                        severity=self.severity,
                        message=(
                            f"Issue references {tmf_code} ({api_name}) with version(s) {', '.join(outdated_versions)} "
                            f"but latest available is {latest_version}"
                        ),
                        issue_key=issue.get('key', 'Unknown'),
                        passed=False,
                        suggestion=f"Consider updating to use current version {latest_version}"
                    ))
                elif not issue_versions:
                    # Issue references TMF API but doesn't specify version
                    api_name = api_info.get('long_name', tmf_code)
                    results.append(RuleResult(
                        rule_id=self.rule_id,
                        severity=RuleSeverity.INFO,
                        message=(
                            f"Issue references {tmf_code} ({api_name}) but doesn't specify version. "
                            f"Latest available is {latest_version}"
                        ),
                        issue_key=issue.get('key', 'Unknown'),
                        passed=False,
                        suggestion=f"Consider specifying version {latest_version} for clarity"
                    ))
            
            return results
            
        except Exception as e:
            # Don't fail the rule engine if TMF lookup fails
            results.append(RuleResult(
                rule_id=self.rule_id,
                severity=RuleSeverity.ERROR,
                message=f"Error checking TMF API versions: {str(e)}",
                issue_key=issue.get('key', 'Unknown'),
                passed=False
            ))
            return results
    
    def _extract_versions_from_issue(self, issue: Dict[str, Any], title: str, description: str) -> list:
        """Extract version information from issue data"""
        versions = []
        
        # Look for versions in fix versions
        fix_versions = issue.get('fixVersions', [])
        if fix_versions:
            for version in fix_versions:
                if isinstance(version, dict):
                    version_name = version.get('name', '')
                else:
                    version_name = str(version)
                
                # Extract version numbers that look like TMF versions (v1, v2, etc.)
                version_matches = re.findall(r'v(\d+)', version_name, re.IGNORECASE)
                versions.extend([f"v{v}" for v in version_matches])
        
        # Look for versions in title and description
        text_to_search = f"{title} {description}"
        version_patterns = [
            r'v(\d+)(?:\.\d+)*',  # v1, v1.0, v1.2.3
            r'version\s*(\d+)',   # version 1, version 2
            r'V(\d+)',            # V1, V2
        ]
        
        for pattern in version_patterns:
            matches = re.findall(pattern, text_to_search, re.IGNORECASE)
            versions.extend([f"v{v}" for v in matches])
        
        # Remove duplicates and return
        return list(set(versions))
    
    def _check_for_outdated_versions(self, issue_versions: list, latest_version: str) -> list:
        """Check which versions are outdated compared to latest"""
        if not issue_versions or latest_version == 'Unknown':
            return []
        
        outdated = []
        
        # Extract numeric part of latest version
        latest_match = re.search(r'v(\d+)', latest_version)
        if not latest_match:
            return []
        
        latest_num = int(latest_match.group(1))
        
        for version in issue_versions:
            version_match = re.search(r'v(\d+)', version)
            if version_match:
                version_num = int(version_match.group(1))
                if version_num < latest_num:
                    outdated.append(version)
        
        return outdated


class TmfApiReferenceRule(BaseRule):
    """Provide information about TMF APIs referenced in issues"""
    
    def get_category(self) -> RuleCategory:
        return RuleCategory.METADATA
    
    def get_severity(self) -> RuleSeverity:
        return RuleSeverity.INFO
    
    def get_description(self) -> str:
        return "Provides information about TMF APIs referenced in issues"
    
    def check(self, issue: Dict[str, Any], context: Dict[str, Any]) -> List[RuleResult]:
        """
        Provide information about TMF APIs referenced in the issue
        
        Args:
            issue: Issue data dictionary
            context: Validation context
            
        Returns:
            List of RuleResult objects with TMF API information
        """
        results = []
        
        try:
            # Import here to avoid circular imports
            from check_issues import find_tmf_references_in_text, get_tmf_api_info
            
            # Search for TMF references in title (prioritize title over description)
            title = issue.get('summary', '') or ''
            tmf_refs = find_tmf_references_in_text(title)
            
            if not tmf_refs:
                # If no references in title, check description
                description = issue.get('description', '') or ''
                tmf_refs = find_tmf_references_in_text(description)
            
            if not tmf_refs:
                return results  # No TMF references found
            
            for tmf_code in tmf_refs:
                api_info = get_tmf_api_info(tmf_code)
                
                if api_info:
                    api_name = api_info.get('long_name', 'Unknown API')
                    latest_version = api_info.get('highest_version', 'Unknown')
                    url = api_info.get('url', '')
                    
                    message = f"References {tmf_code}: {api_name}"
                    if latest_version != 'Unknown':
                        message += f" (Latest: {latest_version})"
                    
                    results.append(RuleResult(
                        rule_id=self.rule_id,
                        severity=self.severity,
                        message=message,
                        issue_key=issue.get('key', 'Unknown'),
                        passed=True,  # This is informational, always "passed"
                        suggestion=f"Documentation: {url}" if url else None
                    ))
                else:
                    results.append(RuleResult(
                        rule_id=self.rule_id,
                        severity=RuleSeverity.WARNING,
                        message=f"References {tmf_code}: API not found in database",
                        issue_key=issue.get('key', 'Unknown'),
                        passed=False
                    ))
            
            return results
            
        except Exception as e:
            # Don't fail the rule engine if TMF lookup fails
            results.append(RuleResult(
                rule_id=self.rule_id,
                severity=RuleSeverity.ERROR,
                message=f"Error retrieving TMF API info: {str(e)}",
                issue_key=issue.get('key', 'Unknown'),
                passed=False
            ))
            return results


class TmfGitCommitInfoRule(BaseRule):
    """Provide Git commit information for TMF APIs referenced in issues"""
    
    def get_category(self) -> RuleCategory:
        return RuleCategory.METADATA
    
    def get_severity(self) -> RuleSeverity:
        return RuleSeverity.INFO
    
    def get_description(self) -> str:
        return "Provides Git commit information for TMF APIs referenced in issues"
    
    def check(self, issue: Dict[str, Any], context: Dict[str, Any]) -> List[RuleResult]:
        """
        Provide Git commit information for TMF APIs referenced in the issue
        
        Args:
            issue: Issue data dictionary
            context: Validation context
            
        Returns:
            List of RuleResult objects with TMF Git commit information
        """
        results = []
        
        try:
            # Import here to avoid circular imports
            from check_issues import find_tmf_references_in_text, find_tmf_references_in_components, get_tmf_rules_info
            
            # Search for TMF references in title, description, and components
            title = issue.get('summary', '') or ''
            description = issue.get('description', '') or ''
            components = issue.get('components', [])
            
            # Find TMF references in title and description
            tmf_refs_text = find_tmf_references_in_text(f"{title} {description}")
            
            # Find TMF references in components
            tmf_refs_components = find_tmf_references_in_components(components)
            
            # Combine all TMF references
            all_tmf_refs = list(set(tmf_refs_text + tmf_refs_components))
            
            if not all_tmf_refs:
                return results  # No TMF references found
            
            # Get issue creation date for comparison
            issue_created = issue.get('created')
            issue_created_dt = None
            if issue_created:
                try:
                    # Parse JIRA datetime format
                    issue_created_dt = pd.to_datetime(issue_created)
                except:
                    pass
            
            for tmf_code in all_tmf_refs:
                rules_info = get_tmf_rules_info(tmf_code)
                
                if rules_info:
                    # Format the Git information message
                    file_path = rules_info['file_path']
                    commit_date = rules_info['last_commit_date']
                    commit_author = rules_info['last_author']
                    commit_message = rules_info['last_commit_message']
                    commit_sha = rules_info['commit_sha']
                    
                    # Format the commit date for display
                    if isinstance(commit_date, str):
                        commit_date_dt = pd.to_datetime(commit_date)
                    else:
                        commit_date_dt = commit_date
                    
                    commit_date_str = commit_date_dt.strftime('%Y-%m-%d %H:%M:%S')
                    
                    message = (
                        f"The rules file {file_path} in Git associated with {tmf_code} "
                        f"was last committed to the main branch on {commit_date_str} "
                        f"by {commit_author} with a comment of '{commit_message}'"
                    )
                    
                    results.append(RuleResult(
                        rule_id=self.rule_id,
                        severity=self.severity,
                        message=message,
                        issue_key=issue.get('key', 'Unknown'),
                        passed=True,  # This is informational, always "passed"
                        suggestion=f"Commit SHA: {commit_sha}"
                    ))
                    
                    # Check if commit date is after issue creation date
                    if issue_created_dt and commit_date_dt > issue_created_dt:
                        time_diff = commit_date_dt - issue_created_dt
                        days_diff = time_diff.days
                        
                        warning_message = (
                            f"WARNING: The rules file for {tmf_code} was updated {days_diff} days "
                            f"AFTER this JIRA was created. The issue may have since been addressed "
                            f"in the latest commit ({commit_date_str})."
                        )
                        
                        results.append(RuleResult(
                            rule_id=self.rule_id,
                            severity=RuleSeverity.WARNING,
                            message=warning_message,
                            issue_key=issue.get('key', 'Unknown'),
                            passed=False,
                            suggestion="Consider reviewing if this issue is still relevant given the recent Git updates"
                        ))
                else:
                    results.append(RuleResult(
                        rule_id=self.rule_id,
                        severity=RuleSeverity.WARNING,
                        message=f"No Git rules file found for {tmf_code} in the TMF repository data",
                        issue_key=issue.get('key', 'Unknown'),
                        passed=False
                    ))
            
            return results
            
        except Exception as e:
            # Don't fail the rule engine if TMF lookup fails
            results.append(RuleResult(
                rule_id=self.rule_id,
                severity=RuleSeverity.ERROR,
                message=f"Error retrieving TMF Git info: {str(e)}",
                issue_key=issue.get('key', 'Unknown'),
                passed=False
            ))
            return results