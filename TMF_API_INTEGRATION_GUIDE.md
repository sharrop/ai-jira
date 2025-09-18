# TMF API Integration Guide

This document explains how to use the TMF API lookup functionality added to the JIRA data quality checker.

## Overview

The system now includes functionality to:
- Load TMF API information from `data/tmf_apis.csv`
- Look up API details by TMF code
- Find TMF API references in issue text
- Enrich JIRA issues with TMF API documentation links

## Functions Available

### Core Functions

#### `load_tmf_apis()`
Loads the TMF APIs CSV file into a pandas DataFrame. Called automatically by other functions.

```python
df = load_tmf_apis()
print(f"Loaded {len(df)} APIs")
```

#### `get_tmf_api_info(tmf_code)`
Gets the highest version number and URL for a given TMF API code.

**Parameters:**
- `tmf_code` (str/int): TMF API code in various formats:
  - "TMF646" (full format)
  - "646" (numeric only)
  - 646 (integer)

**Returns:**
Dictionary with API information or `None` if not found:
```python
{
    'long_name': 'Appointment Management API',
    'tmf_code': 'TMF646',
    'highest_version': 'v4',
    'url': 'https://www.tmforum.org/oda/open-apis/directory/...',
    'all_versions': 'v3; v4'
}
```

**Example:**
```python
from check_issues import get_tmf_api_info

# Various input formats work
api_info = get_tmf_api_info("TMF646")
api_info = get_tmf_api_info("646")
api_info = get_tmf_api_info(646)

if api_info:
    print(f"API: {api_info['long_name']}")
    print(f"Latest Version: {api_info['highest_version']}")
    print(f"Documentation: {api_info['url']}")
```

#### `find_tmf_references_in_text(text)`
Finds TMF API references in text using regex pattern matching.

**Parameters:**
- `text` (str): Text to search

**Returns:**
List of TMF codes found in the text.

**Example:**
```python
from check_issues import find_tmf_references_in_text

text = "This issue implements TMF646 and TMF717 APIs"
refs = find_tmf_references_in_text(text)
print(refs)  # ['TMF646', 'TMF717']
```

#### `enrich_issue_with_tmf_info(issue)`
Enriches a JIRA issue with TMF API information if references are found.

**Parameters:**
- `issue` (dict): Issue data dictionary

**Returns:**
Enhanced issue data with `tmf_apis` field containing found API information.

## Integration with JIRA Checker

The main `check_issues.py` script now automatically:

1. **Detects TMF References**: Scans issue summaries and descriptions for TMF API references
2. **Enriches Issues**: Adds TMF API information to issues when references are found
3. **Displays Links**: Shows TMF API documentation links in the output

### Example Output

When checking JIRA issues, you'll now see:

```
 1. Story: AP-1234
    Title: Implement customer management using TMF629
    Status: In Progress
    Assignee: John Doe
    URL: https://jira.example.com/browse/AP-1234
    🔗 TMF APIs Referenced:
       • TMF629: Customer Management API (Latest: v5)
         📖 Documentation: https://www.tmforum.org/oda/open-apis/directory/customer-management-api-TMF629/v5.0
```

## Standalone TMF Lookup Tool

Use the `tmf_lookup.py` script for quick TMF API lookups:

### Command Line Usage

```bash
# Look up specific APIs
python tmf_lookup.py TMF646 717 TMF629

# Interactive mode
python tmf_lookup.py
```

### Interactive Mode Example

```
🔍 TMF API Lookup Tool
==================================================
📊 Loaded 104 TMF APIs

🎯 Interactive Mode
Enter TMF codes to lookup (e.g., TMF646, 646) or 'quit' to exit:
You can also enter text to search for TMF references.

> TMF646
✅ Found: Appointment Management API
   TMF Code: TMF646
   Latest Version: v4
   Documentation: https://www.tmforum.org/oda/open-apis/directory/appointment-management-api-TMF646/v4.0

> We need to implement TMF629 and TMF717
🔍 Found TMF references in text: TMF629, TMF717

  📖 TMF629: Customer Management API
     Latest: v5 | Docs: https://www.tmforum.org/oda/open-apis/directory/customer-management-api-TMF629/v5.0

  📖 TMF717: Customer360 Management API
     Latest: v5 | Docs: https://www.tmforum.org/oda/open-apis/directory/customer360-management-api-TMF717/v4.0

> quit
```

## Data Source

The system uses `data/tmf_apis.csv` which contains:
- **Long Name**: Full API name
- **Short Name (TMF Code)**: TMF identifier
- **URL**: Link to TMForum documentation
- **Versions**: Available API versions

## Requirements

The TMF API functionality requires:
- `pandas >= 1.5.0` (added to requirements.txt)
- `data/tmf_apis.csv` file in the project data directory

## Error Handling

The system gracefully handles:
- Missing CSV file (warning message, continues without TMF features)
- Invalid TMF codes (returns None)
- Network issues (TMF features disabled)
- Malformed CSV data (warning message)

## Best Practices

1. **Keep CSV Updated**: Regularly update `data/tmf_apis.csv` with latest API information
2. **Use in Issue Descriptions**: Include TMF codes in JIRA issue descriptions for automatic linking
3. **Version Awareness**: The system identifies the highest available version automatically
4. **Documentation Links**: Use the provided URLs for accessing the latest API documentation

## Integration Examples

### Custom Rule Using TMF Data

```python
from check_issues import get_tmf_api_info, find_tmf_references_in_text

def check_tmf_version_consistency(issue, context):
    """Custom rule to check if issues reference current TMF API versions"""
    refs = find_tmf_references_in_text(issue.get('description', ''))
    
    for tmf_code in refs:
        api_info = get_tmf_api_info(tmf_code)
        if api_info:
            # Check if issue mentions the latest version
            if api_info['highest_version'] not in issue.get('description', ''):
                return f"Issue references {tmf_code} but doesn't mention latest version {api_info['highest_version']}"
    
    return None
```

### Batch Processing

```python
from check_issues import load_tmf_apis, get_tmf_api_info

# Pre-load for batch processing
df = load_tmf_apis()

# Process multiple TMF codes efficiently
tmf_codes = ["TMF646", "TMF629", "TMF717"]
for code in tmf_codes:
    info = get_tmf_api_info(code)
    if info:
        print(f"{code}: {info['long_name']} (v{info['highest_version']})")
```