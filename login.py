import asyncio
import os
import json
from dotenv import load_dotenv
from playwright.async_api import async_playwright

# Load environment variables
load_dotenv()

class JiraLoginBot:
    def __init__(self, headless=True):
        self.username = os.getenv('JIRA_USERNAME')
        self.password = os.getenv('JIRA_PASSWORD')
        self.http_proxy = os.getenv('HTTP_PROXY')
        self.https_proxy = os.getenv('HTTPS_PROXY')
        self.base_url = 'https://projects.tmforum.org/jira/'
        self.cookies = {}
        self.headless = headless
        
        if not self.username or not self.password:
            raise ValueError("Username and password must be set in .env file")
    
    async def get_cookies(self, force_refresh=False):
        """Get cookies either from cache, file, or by performing fresh login"""
        if not force_refresh and self.cookies:
            return self.cookies
        
        # Try to load from file first
        if not force_refresh and self.load_cookies():
            return self.cookies
        
        # Perform fresh login
        return await self.login_and_capture_cookies()
    
    async def login_and_capture_cookies(self):
        """Login to Jira and capture session cookies"""
        print("Performing fresh login to JIRA...")
        async with async_playwright() as p:
            # Configure proxy settings if available
            proxy_config = None
            if self.http_proxy:
                proxy_url = self.http_proxy
                print(f"Using proxy: {proxy_url}")
                proxy_config = {"server": proxy_url}
            
            # Launch browser
            if proxy_config:
                browser = await p.chromium.launch(headless=self.headless, proxy=proxy_config)  # type: ignore
            else:
                browser = await p.chromium.launch(headless=self.headless)
            page = None
            
            try:
                # Create a new browser context
                context = await browser.new_context()
                page = await context.new_page()
                
                print(f"Navigating to {self.base_url}")
                await page.goto(self.base_url)
                
                # Wait for the page to load
                await page.wait_for_load_state('networkidle')
                
                # Now look for login elements (no cookie handling on main page)
                print("Looking for login elements...")
                # Check if we're already on a login page or need to find login link
                # Look for the specific login link structure you identified
                login_link = page.locator('#user-options > a.login-link, a.login-link')
                
                # If we see a login form directly
                username_field = page.locator('input[name="username"], input[id="username"], input[name="j_username"]')
                password_field = page.locator('input[name="password"], input[id="password"], input[name="j_password"]')
                
                if await username_field.count() > 0:
                    print("Found login form on current page")
                else:
                    print("Looking for login link...")
                    # Try to find and click the specific login link
                    if await login_link.count() > 0:
                        print("Found login link, clicking...")
                        await login_link.click()
                        await page.wait_for_load_state('networkidle')
                        
                    else:
                        # Fallback: try other common login link patterns
                        fallback_link = page.locator('a:has-text("Log in"), a:has-text("Login"), a[href*="login"]').first
                        if await fallback_link.count() > 0:
                            print("Found fallback login link, clicking...")
                            await fallback_link.click()
                            await page.wait_for_load_state('networkidle')
                            
                        else:
                            # Try going directly to login URL
                            login_url = f"{self.base_url}login.jsp"
                            print(f"No login link found, navigating directly to login page: {login_url}")
                            await page.goto(login_url)
                            await page.wait_for_load_state('networkidle')
                
                # NOW handle cookie consent popup on the login page
                print("Checking for cookie consent popup on login page...")
                try:
                    # Common Cookiebot selectors for "Allow all" or "Accept all" buttons
                    cookie_selectors = [
                        '#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll',
                        '#CybotCookiebotDialogBodyButtonAccept',
                        'button[id*="CybotCookiebot"][id*="Accept"]',
                        'button[id*="CybotCookiebot"][id*="Allow"]',
                        'button:has-text("Allow all")',
                        'button:has-text("Accept all")',
                        'button:has-text("Accept")',
                        '.CybotCookiebotDialogBodyButton',
                        '[data-cy="accept-all-button"]'
                    ]
                    
                    cookie_accepted = False
                    for selector in cookie_selectors:
                        cookie_button = page.locator(selector)
                        if await cookie_button.count() > 0:
                            print(f"Found cookie consent button with selector: {selector}")
                            await cookie_button.click()
                            await page.wait_for_load_state('networkidle')
                            await asyncio.sleep(2)  # Give time for popup to disappear
                            cookie_accepted = True
                            break
                    
                    if not cookie_accepted:
                        print("No cookie consent popup found on login page")
                        
                except Exception as e:
                    print(f"Cookie consent handling error (continuing anyway): {str(e)}")
                
                # Small delay to ensure any popup animations complete
                await asyncio.sleep(1)
                
                # Wait for login form elements
                await page.wait_for_selector('input[name="username"], input[id="username"], input[name="j_username"]', timeout=10000)
                
                # Fill in credentials
                print("Filling in login credentials...")
                username_field = page.locator('input[name="username"], input[id="username"], input[name="j_username"]').first
                password_field = page.locator('input[name="password"], input[id="password"], input[name="j_password"]').first
                
                if self.username and self.password:
                    await username_field.fill(self.username)
                    await password_field.fill(self.password)
                
                # Submit the form
                submit_button = page.locator('#btnSubmit')
                
                print("Submitting login form...")
                if await submit_button.count() > 0:
                    print("Found #btnSubmit, clicking...")
                    await submit_button.click()
                else:
                    # Fallback to other submit button patterns
                    print("btnSubmit not found, trying fallback selectors...")
                    fallback_submit = page.locator('input[type="submit"], button[type="submit"], button:has-text("Log"), a:has-text("Log in")').first
                    if await fallback_submit.count() > 0:
                        await fallback_submit.click()
                    else:
                        print("No submit button found!")
                        raise Exception("Could not find submit button")
                
                # Wait for login to complete
                await page.wait_for_load_state('networkidle')
                
                # Check if login was successful (look for typical post-login elements)
                await asyncio.sleep(3)  # Give time for any redirects
                
                # Capture all cookies
                cookies = await context.cookies()
                self.cookies = {cookie.get('name', ''): cookie.get('value', '') for cookie in cookies if cookie.get('name')}
                
                print("Login completed! Captured cookies:")
                for name, value in self.cookies.items():
                    if 'session' in name.lower() or name == 'JSESSIONID':
                        print(f"  {name}: {value}")
                    else:
                        print(f"  {name}: {value[:20]}..." if len(value) > 20 else f"  {name}: {value}")
                
                # Save cookies to file for later use
                self.save_cookies()
                
                return self.cookies
                
            except Exception as e:
                print(f"Error during login: {str(e)}")
                # Take a screenshot for debugging
                if page:
                    await page.screenshot(path="login_error.png")
                raise
            finally:
                await browser.close()
    
    def save_cookies(self, filename="jira_cookies.json"):
        """Save cookies to a JSON file"""
        with open(filename, 'w') as f:
            json.dump(self.cookies, f, indent=2)
        print(f"Cookies saved to {filename}")
    
    def load_cookies(self, filename="jira_cookies.json"):
        """Load cookies from a JSON file"""
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                self.cookies = json.load(f)
            print(f"Cookies loaded from {filename}")
            return self.cookies
        else:
            print(f"Cookie file {filename} not found")
            return {}
    
    def get_jsessionid(self):
        """Get the JSESSIONID specifically"""
        return self.cookies.get('JSESSIONID')
    
    def get_cookie_header(self):
        """Get cookies formatted as a Cookie header string"""
        return '; '.join([f"{name}={value}" for name, value in self.cookies.items()])

async def main():
    """Main function to run the login process"""
    try:
        jira_bot = JiraLoginBot(headless=False)  # Set to False for debugging
        
        print("Starting Jira login process...")
        cookies = await jira_bot.get_cookies()
        
        print("\n" + "="*50)
        print("LOGIN SUCCESSFUL!")
        print("="*50)
        
        jsessionid = jira_bot.get_jsessionid()
        if jsessionid:
            print(f"JSESSIONID: {jsessionid}")
        
        print(f"\nTotal cookies captured: {len(cookies)}")
        print(f"Cookie header format: {jira_bot.get_cookie_header()}")
        
        # Example of how to use cookies in requests
        print("\nExample usage with requests library:")
        print("```python")
        print("import requests")
        print("cookies = {")
        for name, value in cookies.items():
            print(f"    '{name}': '{value}',")
        print("}")
        print("response = requests.get('https://projects.tmforum.org/jira/rest/api/2/myself', cookies=cookies)")
        print("```")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = asyncio.run(main())