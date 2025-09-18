"""
JQL (JIRA Query Language) Input Validation Module

This module provides comprehensive validation for JQL queries to prevent
injection attacks, unauthorized data access, and performance issues.
"""

import re
from typing import List, Set, Optional, Dict, Any
from exceptions import JiraValidationError


class JQLValidator:
    """
    Validates JQL queries for security and performance concerns.
    
    Provides multiple validation levels:
    - Syntax validation
    - Security validation (injection prevention)
    - Performance validation (resource limits)
    - Access control validation (allowed projects/fields)
    """
    
    # JQL keywords that should be carefully validated
    SENSITIVE_FUNCTIONS = {
        'currentUser', 'membersOf', 'currentLogin', 'now', 'startOfDay',
        'startOfWeek', 'startOfMonth', 'startOfYear', 'endOfDay',
        'endOfWeek', 'endOfMonth', 'endOfYear'
    }
    
    # JQL operators
    VALID_OPERATORS = {
        '=', '!=', '>', '>=', '<', '<=', '~', '!~', 'IN', 'NOT IN',
        'IS', 'IS NOT', 'WAS', 'WAS IN', 'WAS NOT IN', 'WAS NOT',
        'CHANGED', 'AND', 'OR', 'NOT', 'ORDER BY'
    }
    
    # Dangerous patterns that could indicate injection attempts
    DANGEROUS_PATTERNS = [
        r';\s*(DROP|DELETE|UPDATE|INSERT|CREATE|ALTER)',  # SQL injection patterns
        r'(UNION|EXEC|EXECUTE)',  # SQL injection
        r'<script[^>]*>.*?</script>',  # XSS attempts
        r'javascript:',  # JavaScript injection
        r'(eval|Function)\s*\(',  # Code execution
        r'<!--.*?-->',  # HTML comments (could hide malicious code)
    ]
    
    def __init__(self, allowed_projects: Optional[Set[str]] = None, 
                 max_query_length: int = 1000,
                 allowed_fields: Optional[Set[str]] = None):
        """
        Initialize JQL validator with security constraints.
        
        Args:
            allowed_projects: Set of project keys user is allowed to query
            max_query_length: Maximum allowed JQL query length
            allowed_fields: Set of field names user is allowed to query
        """
        self.allowed_projects = allowed_projects or {'AP'}  # Default to AP project
        self.max_query_length = max_query_length
        self.allowed_fields = allowed_fields or {
            'key', 'summary', 'status', 'assignee', 'created', 'updated',
            'priority', 'issuetype', 'description', 'component', 'labels',
            'reporter', 'resolution', 'comment', 'fixVersions', 'project'
        }
    
    def validate_jql_query(self, jql: str, strict_mode: bool = True) -> Dict[str, Any]:
        """
        Comprehensive JQL query validation.
        
        Args:
            jql: JQL query string to validate
            strict_mode: If True, applies stricter security rules
            
        Returns:
            Dict containing validation results and metadata
            
        Raises:
            JiraValidationError: If query fails validation
        """
        if not jql or not jql.strip():
            raise JiraValidationError("JQL query cannot be empty", field_name="jql")
        
        jql = jql.strip()
        
        # Run all validation checks
        validation_result = {
            'original_query': jql,
            'sanitized_query': jql,
            'warnings': [],
            'security_issues': [],
            'performance_warnings': [],
            'is_valid': True
        }
        
        try:
            # 1. Length validation
            self._validate_length(jql)
            
            # 2. Security validation
            self._validate_security(jql, validation_result)
            
            # 3. Syntax validation
            self._validate_syntax(jql, validation_result)
            
            # 4. Project access validation
            if strict_mode:
                self._validate_project_access(jql, validation_result)
            
            # 5. Field validation
            if strict_mode:
                self._validate_field_access(jql, validation_result)
            
            # 6. Performance validation
            self._validate_performance(jql, validation_result)
            
        except JiraValidationError:
            validation_result['is_valid'] = False
            raise
        
        return validation_result
    
    def _validate_length(self, jql: str) -> None:
        """Validate query length to prevent DoS attacks."""
        if len(jql) > self.max_query_length:
            raise JiraValidationError(
                f"JQL query too long: {len(jql)} characters (max: {self.max_query_length})",
                field_name="jql",
                invalid_value=f"{jql[:50]}..."
            )
    
    def _validate_security(self, jql: str, result: Dict[str, Any]) -> None:
        """Check for potential injection attacks and malicious patterns."""
        jql_lower = jql.lower()
        
        # Check for dangerous patterns
        for pattern in self.DANGEROUS_PATTERNS:
            if re.search(pattern, jql, re.IGNORECASE):
                result['security_issues'].append(f"Potentially dangerous pattern detected: {pattern}")
                raise JiraValidationError(
                    f"JQL query contains dangerous pattern: {pattern}",
                    field_name="jql",
                    invalid_value=jql
                )
        
        # Check for excessive wildcards (performance risk)
        wildcard_count = jql.count('*') + jql.count('%')
        if wildcard_count > 3:
            result['performance_warnings'].append(f"High wildcard usage: {wildcard_count}")
        
        # Check for unescaped quotes (injection risk)
        quote_pattern = r'(?<!\\)["\'].*?(?<!\\)["\']'
        quotes = re.findall(quote_pattern, jql)
        for quote in quotes:
            if '\\' not in quote and (';' in quote or '--' in quote):
                result['security_issues'].append("Potentially malicious quote content")
                raise JiraValidationError(
                    "JQL query contains potentially malicious quoted content",
                    field_name="jql"
                )
    
    def _validate_syntax(self, jql: str, result: Dict[str, Any]) -> None:
        """Basic JQL syntax validation."""
        # Check balanced parentheses
        if jql.count('(') != jql.count(')'):
            raise JiraValidationError(
                "JQL query has unbalanced parentheses",
                field_name="jql",
                invalid_value=jql
            )
        
        # Check balanced quotes
        double_quotes = jql.count('"') - jql.count('\\"')
        single_quotes = jql.count("'") - jql.count("\\'")
        
        if double_quotes % 2 != 0:
            raise JiraValidationError(
                "JQL query has unbalanced double quotes",
                field_name="jql"
            )
        
        if single_quotes % 2 != 0:
            raise JiraValidationError(
                "JQL query has unbalanced single quotes",
                field_name="jql"
            )
        
        # Check for empty operators
        empty_operators = re.findall(r'\s+(AND|OR)\s+(AND|OR)\s+', jql, re.IGNORECASE)
        if empty_operators:
            result['warnings'].append("Adjacent logical operators detected")
    
    def _validate_project_access(self, jql: str, result: Dict[str, Any]) -> None:
        """Validate that user can only access allowed projects."""
        if not self.allowed_projects:
            return
        
        # Extract project references from JQL
        project_pattern = r'project\s*[=!~]\s*["\']?([A-Z][A-Z0-9]*)["\']?'
        project_matches = re.findall(project_pattern, jql, re.IGNORECASE)
        
        for project in project_matches:
            if project.upper() not in {p.upper() for p in self.allowed_projects}:
                raise JiraValidationError(
                    f"Access denied to project '{project}'. Allowed projects: {self.allowed_projects}",
                    field_name="project",
                    invalid_value=project
                )
        
        # Check for project wildcards or dangerous patterns
        if re.search(r'project\s*[!~]\s*["\']?\*', jql, re.IGNORECASE):
            result['security_issues'].append("Project wildcard usage detected")
            raise JiraValidationError(
                "Project wildcard queries are not allowed",
                field_name="jql"
            )
    
    def _validate_field_access(self, jql: str, result: Dict[str, Any]) -> None:
        """Validate that only allowed fields are being queried."""
        if not self.allowed_fields:
            return
        
        # Extract field names (simplified pattern)
        field_pattern = r'([a-zA-Z][a-zA-Z0-9_]*)\s*[=!~<>]'
        field_matches = re.findall(field_pattern, jql)
        
        for field in field_matches:
            if field.lower() not in {f.lower() for f in self.allowed_fields}:
                result['warnings'].append(f"Field '{field}' may not be accessible")
                # Note: Don't raise error here as JIRA has many custom fields
    
    def _validate_performance(self, jql: str, result: Dict[str, Any]) -> None:
        """Check for potential performance issues."""
        jql_lower = jql.lower()
        
        # Check for potentially expensive operations
        if 'order by' not in jql_lower and ('created' in jql_lower or 'updated' in jql_lower):
            result['performance_warnings'].append("Date queries without ORDER BY may be slow")
        
        # Check for broad date ranges
        broad_patterns = [
            r'created\s*>=\s*["\']?19\d\d',  # Queries from 1900s
            r'updated\s*>=\s*["\']?19\d\d',
            r'created\s*>=\s*["\']?-\d{3,}d',  # More than 100 days ago
        ]
        
        for pattern in broad_patterns:
            if re.search(pattern, jql, re.IGNORECASE):
                result['performance_warnings'].append("Very broad date range detected")
        
        # Check for inefficient text searches
        if re.search(r'summary\s*~\s*["\'].*\*.*\*', jql, re.IGNORECASE):
            result['performance_warnings'].append("Inefficient text search pattern (multiple wildcards)")
    
    def sanitize_jql_parameter(self, value: str, parameter_type: str = "string") -> str:
        """
        Sanitize individual JQL parameter values.
        
        Args:
            value: Parameter value to sanitize
            parameter_type: Type of parameter ("string", "number", "project", "user")
            
        Returns:
            Sanitized parameter value
            
        Raises:
            JiraValidationError: If parameter cannot be safely sanitized
        """
        if not isinstance(value, str):
            value = str(value)
        
        # Remove null bytes and control characters
        value = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', value)
        
        if parameter_type == "string":
            # Escape quotes and special characters
            value = value.replace('"', '\\"').replace("'", "\\'")
            # Remove potential injection patterns
            value = re.sub(r'[;\\\r\n]', '', value)
            
        elif parameter_type == "project":
            # Project keys should be alphanumeric
            if not re.match(r'^[A-Z][A-Z0-9]*$', value):
                raise JiraValidationError(
                    f"Invalid project key format: {value}",
                    field_name="project",
                    invalid_value=value
                )
                
        elif parameter_type == "number":
            # Ensure it's a valid number
            try:
                float(value)
            except ValueError:
                raise JiraValidationError(
                    f"Invalid number format: {value}",
                    field_name="number",
                    invalid_value=value
                )
                
        elif parameter_type == "user":
            # Basic user validation (email or username format)
            if not re.match(r'^[a-zA-Z0-9._@-]+$', value):
                raise JiraValidationError(
                    f"Invalid user format: {value}",
                    field_name="user",
                    invalid_value=value
                )
        
        return value
    
    def build_safe_jql(self, template: str, **parameters) -> str:
        """
        Build JQL query using parameterized template to prevent injection.
        
        Args:
            template: JQL template with {parameter} placeholders
            **parameters: Parameter values to substitute
            
        Returns:
            Safe JQL query string
            
        Example:
            >>> validator.build_safe_jql(
            ...     "project = {project} AND assignee = {user}",
            ...     project="AP",
            ...     user="john.doe@company.com"
            ... )
            'project = "AP" AND assignee = "john.doe@company.com"'
        """
        # Sanitize all parameters
        safe_params = {}
        for key, value in parameters.items():
            if key.endswith('_project'):
                safe_params[key] = f'"{self.sanitize_jql_parameter(value, "project")}"'
            elif key.endswith('_user'):
                safe_params[key] = f'"{self.sanitize_jql_parameter(value, "user")}"'
            elif key.endswith('_number'):
                safe_params[key] = self.sanitize_jql_parameter(value, "number")
            else:
                safe_params[key] = f'"{self.sanitize_jql_parameter(value, "string")}"'
        
        # Build the query
        try:
            jql = template.format(**safe_params)
        except KeyError as e:
            raise JiraValidationError(
                f"Missing parameter in JQL template: {e}",
                field_name="template"
            )
        
        # Validate the final query
        validation_result = self.validate_jql_query(jql)
        
        return validation_result['sanitized_query']


# Convenience functions for common use cases
def validate_jql_for_ap_project(jql: str) -> Dict[str, Any]:
    """Quick validation for AP project queries."""
    validator = JQLValidator(allowed_projects={'AP'})
    return validator.validate_jql_query(jql)


def build_safe_ap_query(template: str, **parameters) -> str:
    """Build safe JQL query for AP project."""
    validator = JQLValidator(allowed_projects={'AP'})
    return validator.build_safe_jql(template, **parameters)


# Example usage and testing
if __name__ == "__main__":
    validator = JQLValidator(allowed_projects={'AP'})
    
    # Test cases
    test_queries = [
        'project = "AP" AND status = "Open"',  # Safe
        'project = AP AND type = Epic',  # Safe
        'project = "AP"; DROP TABLE users;',  # Malicious
        'project = "AP" AND summary ~ "*test*"',  # Performance warning
        'project != "NONEXISTENT"',  # Potential data exposure
    ]
    
    for jql in test_queries:
        try:
            result = validator.validate_jql_query(jql)
            print(f"✅ VALID: {jql}")
            if result['warnings']:
                print(f"   Warnings: {result['warnings']}")
            if result['performance_warnings']:
                print(f"   Performance: {result['performance_warnings']}")
        except JiraValidationError as e:
            print(f"❌ INVALID: {jql}")
            print(f"   Error: {e}")
        print()