"""
Configuration and default settings for JIRA data quality rules.

This module provides default configurations and helper functions for managing rule settings.
"""

from typing import Dict, Any


# Default configuration for all rules
DEFAULT_CONFIG = {
    'rules': {
        # Assignment Rules
        'UnassignedEpicRule': {
            'enabled': True,
            'description': 'Check if EPIC is assigned to someone'
        },
        'InactiveAssigneeRule': {
            'enabled': True,
            'description': 'Check if assignee is an active user'
        },
        
        # Metadata Rules
        'MissingComponentsRule': {
            'enabled': True,
            'description': 'Check if EPIC has components assigned'
        },
        'MissingDescriptionRule': {
            'enabled': True,
            'description': 'Check if EPIC has a description'
        },
        'MissingFixVersionRule': {
            'enabled': True,
            'description': 'Check if EPIC has a fix version set'
        },
        'LegacyFixVersionRule': {
            'enabled': True,
            'description': 'Check if EPIC fix version is less than 5.0'
        },
        
        # Content Rules
        'NoLinkedIssuesRule': {
            'enabled': True,
            'description': 'Check if EPIC has linked issues'
        },
        
        # Workflow Rules
        'StaleEpicRule': {
            'enabled': True,
            'description': 'Check if EPIC is stale (old or not updated)'
        },
        'LongRunningEpicRule': {
            'enabled': True,
            'description': 'Check if EPIC has been in progress too long'
        },
        
        # Business Rules - these are new suggestions we can add later
        'EpicSizeRule': {
            'enabled': False,  # Disabled by default until implemented
            'description': 'Check if EPIC has appropriate number of child issues'
        },
        'PriorityAlignmentRule': {
            'enabled': False,
            'description': 'Check if high priority EPICs have recent activity'
        },
        'HighPriorityStaleRule': {
            'enabled': True,
            'description': 'Check if high priority issues are stale'
        },
        'MissingPriorityRule': {
            'enabled': True,
            'description': 'Check if issue has a priority set'
        },
        'InProgressTooLongRule': {
            'enabled': True,
            'description': 'Check if issue has been in progress too long for its type'
        },
        'SubTaskOrphanRule': {
            'enabled': True,
            'description': 'Check parent-child relationships for sub-tasks and stories'
        }
    },
    
    'output': {
        'show_passed': False,  # Only show failed checks by default
        'group_by_severity': True,  # Group results by severity level
        'show_summary': True,  # Show summary statistics
        'show_suggestions': True,  # Show improvement suggestions
    },
    
    'thresholds': {
        'stale_days': 180,  # Days without update to consider stale
        'long_running_days': 365,  # Days in progress to consider long-running
        'min_description_length': 10,  # Minimum description length
        'legacy_version_threshold': 5.0,  # Version below which is considered legacy
    }
}


def get_rule_config(rule_name: str) -> Dict[str, Any]:
    """Get configuration for a specific rule"""
    return DEFAULT_CONFIG.get('rules', {}).get(rule_name, {})


def is_rule_enabled(rule_name: str, config: Dict[str, Any] = None) -> bool:
    """Check if a rule is enabled in the given configuration"""
    config = config or DEFAULT_CONFIG
    rule_config = config.get('rules', {}).get(rule_name, {})
    return rule_config.get('enabled', True)


def get_threshold(threshold_name: str, config: Dict[str, Any] = None) -> Any:
    """Get a threshold value from configuration"""
    config = config or DEFAULT_CONFIG
    return config.get('thresholds', {}).get(threshold_name)


def get_output_config(config: Dict[str, Any] = None) -> Dict[str, Any]:
    """Get output configuration settings"""
    config = config or DEFAULT_CONFIG
    return config.get('output', {})


# Example of custom configuration for different environments
DEVELOPMENT_CONFIG = {
    **DEFAULT_CONFIG,
    'rules': {
        **DEFAULT_CONFIG['rules'],
        # More lenient in development
        'MissingDescriptionRule': {'enabled': False},
        'StaleEpicRule': {'enabled': False},
    },
    'thresholds': {
        **DEFAULT_CONFIG['thresholds'],
        'stale_days': 365,  # More lenient for development
    }
}

PRODUCTION_CONFIG = {
    **DEFAULT_CONFIG,
    'rules': {
        **DEFAULT_CONFIG['rules'],
        # Stricter in production
        'EpicSizeRule': {'enabled': True},
        'PriorityAlignmentRule': {'enabled': True},
    },
    'thresholds': {
        **DEFAULT_CONFIG['thresholds'],
        'stale_days': 90,  # Stricter for production
        'min_description_length': 50,  # Require longer descriptions
    }
}