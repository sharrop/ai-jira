# Jira Login Bot

A Python script that uses Playwright to automatically login to TMForum Jira and capture session cookies for later use.

## Features

- Automated login to https://projects.tmforum.org/jira/
- Captures all cookies including JSESSIONID
- Saves cookies to JSON file for reuse
- Provides cookie data in multiple formats for easy integration

## Setup

### Prerequisites
- Python 3.7+
- pip

### Corporate Network Setup
If you're behind a corporate firewall/proxy, the setup script will automatically configure pip to use your proxy settings. The script looks for proxy settings in your `.env` file.

### Installation

1. **Clone or download this repository**

2. **Install dependencies** (choose one method):
   
   **Windows:**
   ```cmd
   setup.bat
   ```
   
   **Linux/Mac:**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```
   
   **Manual installation:**
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

3. **Configure credentials**
   
   Edit the `.env` file and add your Jira credentials:
   ```
   JIRA_USERNAME=your_username_here
   JIRA_PASSWORD=your_password_here
   ```

## Usage

### Basic Usage

Run the script to login and capture cookies:

```bash
python login.py
```

The script will:
1. Open a browser window
2. Navigate to the Jira login page
3. Fill in your credentials
4. Submit the login form
5. Capture all cookies
6. Save cookies to `jira_cookies.json`
7. Display the captured cookies

### Using Captured Cookies

The script provides several ways to use the captured cookies:

#### 1. Python requests library
```python
import json
import requests

# Load cookies from file
with open('jira_cookies.json', 'r') as f:
    cookies = json.load(f)

# Use with requests
response = requests.get(
    'https://projects.tmforum.org/jira/rest/api/2/myself', 
    cookies=cookies
)
```

#### 2. Using the JiraLoginBot class
```python
from login import JiraLoginBot

# Create instance and load existing cookies
bot = JiraLoginBot()
cookies = bot.load_cookies()

# Get specific cookies
jsessionid = bot.get_jsessionid()
cookie_header = bot.get_cookie_header()

# Use in HTTP requests
headers = {'Cookie': cookie_header}
```

## Files Created

- `jira_cookies.json` - Saved cookies in JSON format
- `login_error.png` - Screenshot if login fails (for debugging)

## Configuration Options

You can modify the script behavior by editing these variables in `main.py`:

- `headless=False` - Set to `True` to run browser in headless mode
- Browser type - Change from `chromium` to `firefox` or `webkit` if needed

## Troubleshooting

### Common Issues

1. **Login fails**
   - Check your credentials in `.env` file
   - Verify the Jira URL is accessible
   - Check the screenshot `login_error.png` for visual debugging

2. **Browser doesn't open**
   - Run `playwright install chromium` to install browser
   - Check if you have sufficient permissions

3. **Import errors**
   - Make sure all dependencies are installed: `pip install -r requirements.txt`

### Debug Mode

The script runs with `headless=False` by default, so you can see what's happening. For production use, change to `headless=True`.

## Security Notes

- Never commit your `.env` file with real credentials
- Store credentials securely
- The captured cookies are sensitive - protect the `jira_cookies.json` file
- Cookies may expire - re-run the script if you get authentication errors

## License

This project is for educational and automation purposes. Ensure you comply with your organization's policies regarding automated access.
