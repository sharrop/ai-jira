# JIRA API Integration

Complete Python toolkit for TMForum JIRA automation - from login to API interactions.

## Features

- **Automated Login**: Uses Playwright to handle authentication with cookie consent
- **Session Management**: Captures and reuses cookies for API calls
- **JIRA REST API**: Full client for searching issues, projects, and user management
- **Corporate Proxy Support**: Works behind corporate firewalls
- **Type Hints**: Full typing support for better development experience

## Quick Start

### 1. Setup

```bash
# Install dependencies
pip install -r requirements.txt
playwright install chromium

# Configure credentials
# Edit .env file with your JIRA credentials
```

### 2. Basic Usage

```python
from jira_api import JiraApiClient

async def main():
    client = JiraApiClient()
    
    # Authenticate (handles login automatically)
    if await client.authenticate():
        # Get issues from AP project (last 30 days)
        issues = client.get_ap_issues_last_month()
        
        for issue in issues:
            print(f"{issue['key']}: {issue['summary']}")

# Run it
import asyncio
asyncio.run(main())
```

### 3. Run the Example

```bash
python example.py
```

## File Structure

```
├── login.py          # JiraLoginBot class for authentication
├── jira_api.py       # JiraApiClient for REST API operations  
├── example.py        # Complete usage example
├── .env              # Your credentials (DO NOT COMMIT)
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## API Usage Examples

### Getting Issues from a Project

```python
from jira_api import JiraApiClient

async def get_recent_issues():
    client = JiraApiClient()
    await client.authenticate()
    
    # Get AP project issues from last month
    issues = client.get_ap_issues_last_month(max_results=50)
    return issues
```

### Custom JQL Queries

```python
# Search with custom JQL
jql = 'project = "AP" AND status = "In Progress" AND assignee = currentUser()'
results = client.search_issues(jql, max_results=100)

for issue in results['issues']:
    print(f"{issue['key']}: {issue['fields']['summary']}")
```

### Project Information

```python
# Get project details
project = client.get_project_info('AP')
print(f"Project: {project['name']}")
print(f"Lead: {project['lead']['displayName']}")
```

### User Information

```python
# Get current user info
user = client.get_user_info()
print(f"Logged in as: {user['displayName']}")
```

## JQL Examples

The JIRA Query Language (JQL) is powerful for finding specific issues:

```python
# Issues created this week
jql = 'project = "AP" AND created >= startOfWeek()'

# High priority bugs
jql = 'project = "AP" AND priority = High AND type = Bug'

# Issues assigned to you
jql = 'project = "AP" AND assignee = currentUser()'

# Issues updated recently
jql = 'project = "AP" AND updated >= -7d'

# Complex query
jql = '''project = "AP" 
         AND status IN ("To Do", "In Progress") 
         AND priority >= High 
         AND created >= -30d
         ORDER BY priority DESC, created ASC'''
```

## Authentication Flow

1. **Check Cache**: Uses existing cookies if available
2. **Load from File**: Loads saved cookies from `jira_cookies.json`
3. **Fresh Login**: If needed, opens browser and performs full login
4. **Cookie Management**: Automatically saves and reuses session cookies

## Classes

### JiraLoginBot

Handles authentication with TMForum JIRA:

```python
from login import JiraLoginBot

bot = JiraLoginBot(headless=True)  # Set False for debugging
cookies = await bot.get_cookies()
```

**Methods:**
- `get_cookies(force_refresh=False)` - Get authentication cookies
- `login_and_capture_cookies()` - Perform fresh browser login
- `save_cookies(filename)` - Save cookies to file
- `load_cookies(filename)` - Load cookies from file

### JiraApiClient

Makes authenticated REST API calls:

```python
from jira_api import JiraApiClient

client = JiraApiClient()
await client.authenticate()
```

**Methods:**
- `authenticate(force_refresh=False)` - Authenticate with JIRA
- `search_issues(jql, max_results=50)` - Search issues with JQL
- `get_ap_issues_last_month(max_results=100)` - Get recent AP issues
- `get_project_info(project_key)` - Get project information
- `get_user_info()` - Get current user information

## Configuration

### Environment Variables (.env)

```bash
# Required
JIRA_USERNAME=your.email@vodafone.com
JIRA_PASSWORD=your_password

# Optional - Corporate Proxy
HTTP_PROXY=http://proxy-server:8080
HTTPS_PROXY=http://proxy-server:8080
```

### Proxy Configuration

The tools automatically detect and use corporate proxy settings from environment variables.

## Error Handling

The clients include comprehensive error handling:

- **Authentication Errors**: Clear messages when login fails
- **Network Issues**: Proxy and timeout handling
- **API Errors**: Meaningful error messages for failed requests
- **Rate Limiting**: Automatic handling of JIRA rate limits

## Common Use Cases

### 1. Daily Issue Report

```python
async def daily_report():
    client = JiraApiClient()
    await client.authenticate()
    
    # Get today's updates
    jql = 'project = "AP" AND updated >= startOfDay()'
    results = client.search_issues(jql)
    
    print(f"Issues updated today: {results['total']}")
    for issue in results['issues']:
        fields = issue['fields']
        print(f"- {issue['key']}: {fields['summary']}")
```

### 2. Bulk Issue Analysis

```python
async def analyze_issues():
    client = JiraApiClient()
    await client.authenticate()
    
    # Get all open issues
    jql = 'project = "AP" AND status != Closed'
    all_issues = []
    start_at = 0
    max_results = 100
    
    while True:
        results = client.search_issues(jql, max_results, start_at)
        all_issues.extend(results['issues'])
        
        if len(results['issues']) < max_results:
            break
        start_at += max_results
    
    print(f"Total open issues: {len(all_issues)}")
```

### 3. Issue Monitoring

```python
async def monitor_high_priority():
    client = JiraApiClient()
    await client.authenticate()
    
    # Monitor high priority issues
    jql = 'project = "AP" AND priority = Highest AND status != Closed'
    issues = client.search_issues(jql)
    
    if issues['total'] > 0:
        print("🚨 HIGH PRIORITY ISSUES FOUND:")
        for issue in issues['issues']:
            fields = issue['fields']
            assignee = fields.get('assignee', {}).get('displayName', 'Unassigned')
            print(f"- {issue['key']}: {fields['summary']} (Assigned: {assignee})")
```

## Troubleshooting

### Common Issues

1. **Login Fails**
   - Check credentials in `.env` file
   - Verify proxy settings if behind corporate firewall
   - Check for CAPTCHA or additional security measures

2. **API Calls Fail**
   - Ensure cookies are fresh (try `force_refresh=True`)
   - Check project permissions
   - Verify project key exists

3. **No Issues Found**
   - Check JQL syntax
   - Verify project access permissions
   - Try broader date ranges

### Debug Mode

```python
# Enable debug mode for login
bot = JiraLoginBot(headless=False)  # Shows browser window

# Check authentication status
user_info = client.get_user_info()
if user_info:
    print("✅ Authenticated successfully")
else:
    print("❌ Authentication failed")
```

## Security Notes

- Never commit your `.env` file with real credentials
- Cookies are sensitive - protect `jira_cookies.json`
- Use environment variables or secure vaults in production
- Cookies expire - the tools handle refresh automatically

## License

This project is for educational and automation purposes. Ensure compliance with your organization's policies regarding automated access to JIRA systems.