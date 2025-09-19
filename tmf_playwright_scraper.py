#!/usr/bin/env python3
"""
TMF Rules Files Extractor using Playwright.
Playwright can handle JavaScript and bypass many anti-bot measures.
"""

import asyncio
import csv
import os
import re
from datetime import datetime
from dotenv import load_dotenv
from playwright.async_api import async_playwright
import time

# Load environment variables
load_dotenv()

class TMFPlaywrightScraper:
    def __init__(self):
        """Initialize the Playwright scraper."""
        self.base_url = "https://github.com"
        self.repo = "tmforum-rand/OAS_Open_API_And_Data_Model"
        self.branch = "v5.0.0-dev"
        self.apis_path = "apis"
        
        # GitHub credentials
        self.github_username = os.getenv('GITHUB_USERNAME')
        self.github_password = os.getenv('GITHUB_PASSWORD')
        
        # Proxy configuration
        self.proxy_config = None
        http_proxy = os.getenv('HTTP_PROXY') or os.getenv('http_proxy')
        https_proxy = os.getenv('HTTPS_PROXY') or os.getenv('https_proxy')
        
        if https_proxy:
            # Extract proxy details for Playwright
            proxy_url = https_proxy.replace('http://', '')
            if '@' in proxy_url:
                auth, server = proxy_url.split('@')
                username, password = auth.split(':')
                server_host, server_port = server.split(':')
            else:
                server_host, server_port = proxy_url.split(':')
                username, password = None, None
            
            self.proxy_config = {
                "server": f"http://{server_host}:{server_port}",
                "username": username,
                "password": password
            } if username else {"server": f"http://{server_host}:{server_port}"}
            
            print(f"Using proxy: {server_host}:{server_port}")
    
    async def setup_browser(self):
        """Setup Playwright browser with appropriate configuration."""
        playwright = await async_playwright().start()
        
        # Use Chromium with stealth settings and proxy
        browser_args = [
            '--no-sandbox',
            '--disable-blink-features=AutomationControlled',
            '--disable-features=VizDisplayCompositor',
            '--disable-web-security',
            '--disable-extensions'
        ]
        
        # Add proxy args if configured
        if self.proxy_config:
            browser_args.extend([
                f'--proxy-server={self.proxy_config["server"]}',
                '--ignore-certificate-errors-spki-list',
                '--ignore-certificate-errors',
                '--ignore-ssl-errors'
            ])
        
        browser = await playwright.chromium.launch(
            headless=False,  # Set to False for debugging - let's see what's happening
            args=browser_args
        )
        
        # Create context with realistic browser fingerprint
        context = await browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            viewport={'width': 1920, 'height': 1080},
            ignore_https_errors=True,
            extra_http_headers={
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'DNT': '1',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1'
            }
        )
        
        page = await context.new_page()
        
        # Add stealth JavaScript
        await page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined,
            });
        """)
        
        return playwright, browser, context, page
    
    async def login_to_github(self, page):
        """Login to GitHub with 2FA support."""
        print("Logging in to GitHub...")
        
        # Go to GitHub login page
        await page.goto("https://github.com/login", wait_until='networkidle')
        
        # Check if we need to log in or if already logged in
        if await page.query_selector('[data-testid="header-search-button"]'):
            print("Already logged in to GitHub!")
            return True
        
        # Fill in username
        if self.github_username:
            await page.fill('#login_field', self.github_username)
            print(f"Entered username: {self.github_username}")
        else:
            print("Please enter your GitHub username:")
            username = input("Username: ")
            await page.fill('#login_field', username)
        
        # Fill in password
        if self.github_password:
            await page.fill('#password', self.github_password)
            print("Entered password from environment variable")
        else:
            print("Please enter your GitHub password:")
            import getpass
            password = getpass.getpass("Password: ")
            await page.fill('#password', password)
        
        # Click sign in
        await page.click('input[type="submit"][value="Sign in"]')
        
        # Wait for potential 2FA challenge
        print("Waiting for login response...")
        await asyncio.sleep(3)
        
        # Debug: Check what URL we're on
        current_url = page.url
        print(f"Current URL after login attempt: {current_url}")
        
        # Check if we're already logged in successfully (be more specific)
        if ("github.com" in current_url and 
            "/login" not in current_url and 
            "/sessions" not in current_url and
            "/signup" not in current_url and
            ("/" == current_url.split("github.com")[-1] or current_url.endswith("github.com"))):
            print("✅ Login successful - already on main GitHub page!")
            return True
        
        # Check if 2FA is required
        try:
            # Wait a bit longer for the page to settle
            await asyncio.sleep(5)
            
            # Look for 2FA input field with multiple attempts
            totp_field = None
            sms_field = None
            
            for attempt in range(3):
                totp_field = await page.query_selector('#app_totp')
                sms_field = await page.query_selector('#sms_totp')
                
                if totp_field or sms_field:
                    break
                    
                print(f"Checking for 2FA fields... attempt {attempt + 1}")
                await asyncio.sleep(2)
            
            if totp_field:
                print("\n🔐 Two-Factor Authentication Required!")
                print("Please enter your 6-digit code directly in the browser window.")
                print("The script will wait for you to complete the 2FA process...")
                
                # Wait for the user to complete 2FA manually in the browser
                # Check periodically if we've moved past the login page
                for wait_count in range(30):  # Wait up to 60 seconds
                    await asyncio.sleep(2)
                    current_url = page.url
                    
                    # Check if we're no longer on login/2FA pages
                    if "/login" not in current_url and "/sessions/two-factor" not in current_url:
                        print("✅ 2FA completed successfully!")
                        break
                    
                    if wait_count % 5 == 0:  # Print status every 10 seconds
                        print(f"Waiting for 2FA completion... ({wait_count * 2}s elapsed)")
                
                # Check if we're still on a login page after waiting
                final_url = page.url
                if "/login" in final_url or "/sessions/two-factor" in final_url:
                    print("❌ 2FA process seems incomplete. Please complete it manually.")
                    return False
            
            elif sms_field:
                print("\n📱 SMS Two-Factor Authentication Required!")
                print("Please enter your SMS code directly in the browser window.")
                print("The script will wait for you to complete the SMS verification...")
                
                # Wait for the user to complete SMS verification manually
                for wait_count in range(30):  # Wait up to 60 seconds
                    await asyncio.sleep(2)
                    current_url = page.url
                    
                    if "/login" not in current_url and "/sessions/two-factor" not in current_url:
                        print("✅ SMS verification completed successfully!")
                        break
                    
                    if wait_count % 5 == 0:
                        print(f"Waiting for SMS verification... ({wait_count * 2}s elapsed)")
                
                final_url = page.url
                if "/login" in final_url or "/sessions/two-factor" in final_url:
                    print("❌ SMS verification seems incomplete. Please complete it manually.")
                    return False
            
        except Exception as e:
            print(f"Error during 2FA process: {e}")
            print("Attempting to continue anyway...")
        
        # Verify login was successful
        try:
            # Wait for successful login redirect with longer timeout
            print("Verifying login success...")
            
            # Try to navigate to a simple GitHub page to test if login worked
            test_url = "https://github.com/settings/profile"
            try:
                await page.goto(test_url, wait_until='domcontentloaded', timeout=15000)
                current_url = page.url
                
                # If we can access settings, we're definitely logged in
                if "/settings/" in current_url:
                    print("✅ Login verified - can access GitHub settings!")
                    return True
                    
            except:
                # If settings doesn't work, try the main GitHub page
                try:
                    await page.goto("https://github.com/", wait_until='domcontentloaded', timeout=15000)
                    current_url = page.url
                    
                    # Check if we're on GitHub main page (not login page)
                    if current_url == "https://github.com/" or current_url.endswith("github.com/"):
                        print("✅ Login appears successful - on GitHub main page!")
                        return True
                        
                except:
                    pass
            
            print("⚠️ Cannot verify login status, but attempting to continue...")
            return True  # Always try to continue since manual verification showed it worked
                
        except Exception as e:
            print(f"⚠️ Login verification failed: {e}")
            print("Attempting to continue anyway since login may have worked...")
            return True  # Always try to continue
    
    async def get_tmf_directories(self, page):
        """Get list of TMF directories from the APIs folder."""
        
        # First, let's check if we can access the main repository
        repo_url = f"{self.base_url}/{self.repo}"
        print(f"First checking if repository exists: {repo_url}")
        
        try:
            await page.goto(repo_url, wait_until='domcontentloaded', timeout=20000)
            page_title = await page.title()
            print(f"Repository page title: {page_title}")
            
            if "404" in page_title or "not found" in page_title.lower():
                print("❌ Repository not found or not accessible")
                return []
                
        except Exception as e:
            print(f"⚠️ Repository check failed: {e}")
            print("Attempting to continue to APIs directory anyway...")
            # Don't return here - try to continue
        
        # Now try the APIs folder
        url = f"{self.base_url}/{self.repo}/tree/{self.branch}/{self.apis_path}"
        
        print(f"Navigating to: {url}")
        
        try:
            # Navigate to the APIs directory with faster loading
            print(f"Loading page...")
            await page.goto(url, wait_until='domcontentloaded', timeout=30000)  # Much faster than networkidle
            
            # Wait just a bit for content to appear
            await asyncio.sleep(2)
            
            # Debug: Print page title and URL to confirm we're in the right place
            page_title = await page.title()
            print(f"Page title: {page_title}")
            print(f"Current URL: {page.url}")
            
            if "404" in page_title or "not found" in page_title.lower():
                print("❌ APIs directory not found")
                return []
            
            # Try different selectors to find the file tree (with shorter waits)
            selectors_to_try = [
                '[data-testid="file-tree-container"]',
                '.js-navigation-container',
                '[aria-labelledby="folders-and-files"]',
                'div[role="grid"]',
                '.Box-row',
                '.react-directory-row'
            ]
            
            content_loaded = False
            for selector in selectors_to_try:
                try:
                    await page.wait_for_selector(selector, timeout=5000)  # Much shorter timeout
                    print(f"Found content using selector: {selector}")
                    content_loaded = True
                    break
                except:
                    continue
            
            if not content_loaded:
                print("Could not find file tree container, trying to get links anyway...")
            
            # Debug: Print page title and URL to confirm we're in the right place
            page_title = await page.title()
            print(f"Page title: {page_title}")
            print(f"Current URL: {page.url}")
            
            # Try multiple approaches to find TMF directories
            print("Searching for TMF directories...")
            
            # Approach 1: Look for directory links containing TMF
            directory_links = await page.query_selector_all('a[href*="/tree/"][href*="/apis/TMF"]')
            print(f"Found {len(directory_links)} links with /tree/ and /apis/TMF")
            
            # Approach 2: Look for any links containing TMF
            tmf_links = await page.query_selector_all('a[href*="TMF"]')
            print(f"Found {len(tmf_links)} links containing TMF")
            
            # Approach 3: Get all directory/folder links in general
            all_dir_links = await page.query_selector_all('a[href*="/tree/"]')
            print(f"Found {len(all_dir_links)} total directory links")
            
            # Approach 4: Look for span or div elements containing TMF text
            tmf_elements = await page.query_selector_all('*:has-text("TMF")')
            print(f"Found {len(tmf_elements)} elements containing TMF text")
            
            directories = []
            
            # Process the directory links we found
            for link in directory_links:
                href = await link.get_attribute('href')
                if href:
                    # Extract directory name from href
                    match = re.search(r'/apis/(TMF[^/]+)', href)
                    if match:
                        dir_name = match.group(1)
                        directories.append(dir_name)
            
            # If no TMF directories found, try a broader search
            if not directories:
                print("No TMF directories found in standard links, trying broader search...")
                for link in all_dir_links:
                    href = await link.get_attribute('href')
                    text = await link.text_content()
                    if href and 'TMF' in (href + ' ' + (text or '')):
                        print(f"  Found potential TMF link: {href} ({text})")
                        match = re.search(r'(TMF[^/\s]+)', href + ' ' + (text or ''))
                        if match:
                            dir_name = match.group(1)
                            directories.append(dir_name)
            
            # Remove duplicates and sort
            directories = sorted(list(set(directories)))
            
            print(f"Found {len(directories)} TMF directories:")
            for dir_name in directories:
                print(f"  - {dir_name}")
            
            return directories
            
        except Exception as e:
            print(f"Error getting directories: {e}")
            print("Using fallback directory list...")
            
            # Fallback to known TMF directories
            return [
                "TMF620_Product_Catalog", "TMF621_Trouble_Ticket", "TMF622_Product_Ordering",
                "TMF623_Service_Catalog", "TMF624_Resource_Catalog", "TMF625_Service_Ordering",
                "TMF629_Customer_Billing", "TMF632_Party_Management", "TMF633_Service_Quality_Management",
                "TMF634_Resource_Inventory", "TMF635_Usage_Management", "TMF637_Product_Inventory",
                "TMF638_Service_Inventory", "TMF639_Resource_Activation", "TMF641_Service_Ordering"
            ]
    
    async def find_rules_files_in_directory(self, page, directory):
        """Find rules files in a specific TMF directory."""
        url = f"{self.base_url}/{self.repo}/tree/{self.branch}/{self.apis_path}/{directory}"
        
        print(f"Checking directory: {directory}")
        
        try:
            await page.goto(url, wait_until='domcontentloaded', timeout=20000)  # Much faster loading
            
            # Check if page loaded successfully
            page_title = await page.title()
            if "404" in page_title or "not found" in page_title.lower():
                print(f"  Directory not found: {directory}")
                return []
            
            # Wait for file listing to load (much shorter timeout)
            await asyncio.sleep(1)  # Just a brief wait
            
            # Look for rules files with multiple selector attempts
            rules_files = []
            
            # Try different selectors for finding .rules.yaml files
            rules_selectors = [
                'a[href*="/blob/"][href$=".rules.yaml"]',
                'a[href$=".rules.yaml"]'
            ]
            
            found_files = set()  # Use set to avoid duplicates
            
            for selector in rules_selectors:
                try:
                    file_links = await page.query_selector_all(selector)
                    if file_links:
                        print(f"  Found rules files using selector: {selector}")
                        for link in file_links:
                            href = await link.get_attribute('href')
                            if href and '.rules.yaml' in href:
                                # Extract filename from href
                                filename = href.split('/')[-1]
                                if filename.endswith('.rules.yaml'):
                                    found_files.add(filename)
                        break  # Stop after first successful selector
                except:
                    continue
            
            rules_files = list(found_files)  # Convert set back to list
            
            if rules_files:
                print(f"  Found {len(rules_files)} rules file(s): {rules_files}")
            else:
                print(f"  No rules files found")
            
            return rules_files
            
        except Exception as e:
            print(f"  Error checking directory {directory}: {e}")
            return []
    
    async def get_file_commit_info(self, page, directory, filename):
        """Get commit information for a specific rules file."""
        file_path = f"{self.apis_path}/{directory}/{filename}"
        
        print(f"    Getting commit info for: {filename}")
        
        # First, verify the file exists by going to its blob page
        file_url = f"{self.base_url}/{self.repo}/blob/{self.branch}/{file_path}"
        
        try:
            print(f"      Verifying file exists: {file_url}")
            await page.goto(file_url, wait_until='domcontentloaded', timeout=20000)
            await asyncio.sleep(2)
            
            page_title = await page.title()
            current_url = page.url
            print(f"      File page title: {page_title}")
            
            # Check if the file exists (not 404)
            if "404" in page_title or "not found" in page_title.lower():
                print(f"      File does not exist at: {file_path}")
                return None
            
            # File exists, try to get commit info from the file page header
            commit_info = {}
            
            print(f"      File exists, extracting commit info from file header...")
            
            # Look for commit info in the file header area
            try:
                # Method 1: Look for commit link in file actions area
                commit_selectors = [
                    'a[href*="/commit/"]',
                    '[data-testid="latest-commit"] a',
                    '.commit-tease a',
                    '.file-navigation a[href*="/commit/"]'
                ]
                
                for selector in commit_selectors:
                    try:
                        commit_element = await page.query_selector(selector)
                        if commit_element:
                            href = await commit_element.get_attribute('href')
                            if href and '/commit/' in href:
                                sha_match = re.search(r'/commit/([a-f0-9]+)', href)
                                if sha_match:
                                    commit_info['sha'] = sha_match.group(1)[:7]
                                    print(f"      Found SHA using selector: {selector}")
                                    
                                    # Try to get commit message from this element or nearby
                                    commit_text = await commit_element.text_content()
                                    if commit_text and commit_text.strip():
                                        commit_info['message'] = commit_text.strip()
                                        print(f"      Found commit message: {commit_text.strip()[:50]}...")
                                    break
                    except Exception as e:
                        print(f"      Commit selector '{selector}' failed: {e}")
                        continue
                
                # Method 2: Look for author info with expanded selectors including history summary
                author_selectors = [
                    'a[data-hovercard-type="user"]',
                    '.commit-author a',
                    '[data-testid="latest-commit"] a[data-hovercard-type="user"]',
                    '.commit-meta a[data-hovercard-type="user"]',
                    '.file-history-tease a[data-hovercard-type="user"]',
                    '[data-testid="author-name"]',
                    '.author a',
                    'span.commit-author a',
                    '.commit-tease .commit-author a',
                    '.Box-header .commit-author a',
                    # Target the history summary area you found
                    'div.d-flex.flex-column.border.rounded-2 a[data-hovercard-type="user"]',
                    'div.border.rounded-2 a[data-hovercard-type="user"]',
                    '.border.rounded-2 a[data-hovercard-type="user"]',
                    # Even broader selectors for the history area
                    'div:nth-child(3) a[data-hovercard-type="user"]',
                    'div.mb-3 a[data-hovercard-type="user"]'
                ]
                
                print(f"      Looking for author with {len(author_selectors)} selectors...")
                for i, selector in enumerate(author_selectors):
                    try:
                        author_element = await page.query_selector(selector)
                        if author_element:
                            author_text = await author_element.text_content()
                            if author_text and author_text.strip() and len(author_text.strip()) > 1:
                                commit_info['author'] = author_text.strip()
                                print(f"      ✅ Found author using selector {i+1}: {selector}")
                                print(f"      Author: {author_text.strip()}")
                                break
                            else:
                                print(f"      Author element found but no text: {selector}")
                        else:
                            print(f"      No author element found: {selector}")
                    except Exception as e:
                        print(f"      Author selector '{selector}' failed: {e}")
                        continue
                
                # If no author found yet, try a broader search including the history summary area
                if 'author' not in commit_info:
                    print(f"      No author found with standard selectors, trying broader search...")
                    
                    # Take a screenshot for debugging
                    await page.screenshot(path='debug_file_page.png')
                    print(f"      Saved screenshot of file page for debugging")
                    
                    # Try to find the specific history summary area you mentioned
                    history_area_selectors = [
                        'div.d-flex.flex-column.border.rounded-2.mb-3.pl-1 > div',
                        'div.d-flex.flex-column.border.rounded-2 > div',
                        'div.border.rounded-2.mb-3 > div',
                        'div.border.rounded-2 > div'
                    ]
                    
                    print(f"      Checking history summary areas...")
                    for i, selector in enumerate(history_area_selectors):
                        try:
                            history_element = await page.query_selector(selector)
                            if history_element:
                                history_text = await history_element.text_content()
                                print(f"      History area {i+1} found with text: '{history_text}'")
                                
                                # Extract author name from the text pattern
                                # Pattern examples:
                                # "Latest commit Jonathan GoldbergandJonathan GoldbergExample corrections following Pierre review"
                                # "Latest commitrsivaji-tmforum uypdateMay 5, 2025"
                                # "Latest commitolivier-arnaudPierre review comments updateSep 12, 2023"
                                if history_text and 'Latest commit' in history_text:
                                    # Remove "Latest commit" and try to extract the author part
                                    text_after_commit = history_text.replace('Latest commit', '').strip()
                                    
                                    author_candidate = None
                                    
                                    # Method 1: Handle the "AuthorNameandAuthorName" pattern (like Jonathan GoldbergandJonathan Goldberg)
                                    if 'and' in text_after_commit:
                                        # Split on 'and' and take the first part
                                        potential_author = text_after_commit.split('and')[0].strip()
                                        # Make sure it looks like a reasonable author name (not too long, not empty)
                                        if 2 <= len(potential_author) <= 50 and potential_author.replace(' ', '').replace('-', '').replace('_', '').isalnum():
                                            author_candidate = potential_author
                                    
                                    # Method 2: Handle cases without 'and' by looking for username patterns
                                    if not author_candidate:
                                        # Common patterns: username followed by commit message starting with lowercase words
                                        # rsivaji-tmforum uypdateMay -> "rsivaji-tmforum"
                                        # olivier-arnaudPierre -> "olivier-arnaud"
                                        
                                        # First try: Look for common commit message start patterns and split there
                                        commit_patterns = [
                                            r'([a-zA-Z][a-zA-Z0-9\-_.]{2,30})(Pierre)',
                                            r'([a-zA-Z][a-zA-Z0-9\-_.]{2,30})(update)',
                                            r'([a-zA-Z][a-zA-Z0-9\-_.]{2,30})(fix)',
                                            r'([a-zA-Z][a-zA-Z0-9\-_.]{2,30})(add)',
                                            r'([a-zA-Z][a-zA-Z0-9\-_.]{2,30})(correct)',
                                            r'([a-zA-Z][a-zA-Z0-9\-_.]{2,30})(change)',
                                            r'([a-zA-Z][a-zA-Z0-9\-_.]{2,30})(Create)',
                                            r'([a-zA-Z][a-zA-Z0-9\-_.]{2,30})(Merge)',
                                        ]
                                        
                                        for pattern in commit_patterns:
                                            match = re.match(pattern, text_after_commit, re.IGNORECASE)
                                            if match:
                                                author_candidate = match.group(1)
                                                print(f"      Found author using pattern '{pattern}': {author_candidate}")
                                                break
                                        
                                        # If pattern matching didn't work, try word-based approach
                                        if not author_candidate:
                                            # Look for the first "word" that could be a username
                                            words = text_after_commit.split()
                                            if words:
                                                first_word = words[0]
                                                # Check if it looks like a username (contains letters, may have hyphens/underscores)
                                                if re.match(r'^[a-zA-Z][a-zA-Z0-9\-_.]*$', first_word) and len(first_word) >= 3:
                                                    author_candidate = first_word
                                        
                                        # If that doesn't work either, try regex to extract username at the beginning
                                        if not author_candidate:
                                            username_match = re.match(r'^([a-zA-Z][a-zA-Z0-9\-_.]{2,30})', text_after_commit)
                                            if username_match:
                                                author_candidate = username_match.group(1)
                                    
                                    if author_candidate and len(author_candidate.strip()) > 1:
                                        commit_info['author'] = author_candidate.strip()
                                        print(f"      ✅ Extracted author from history text: '{author_candidate.strip()}'")
                                        break
                                
                                # Also look for user links within this history area (original approach)
                                user_links_in_history = await history_element.query_selector_all('a[data-hovercard-type="user"]')
                                print(f"      Found {len(user_links_in_history)} user links in this history area")
                                
                                if user_links_in_history:
                                    first_user = user_links_in_history[0]
                                    user_text = await first_user.text_content()
                                    if user_text and user_text.strip():
                                        commit_info['author'] = user_text.strip()
                                        print(f"      ✅ Found author in history area user link: {user_text.strip()}")
                                        break
                            else:
                                print(f"      History area selector {i+1} found no element")
                        except Exception as e:
                            print(f"      History area selector {i+1} error: {e}")
                    
                    # If still no author, try the general approach
                    if 'author' not in commit_info:
                        try:
                            # Look for any user links on the page
                            user_links = await page.query_selector_all('a[data-hovercard-type="user"]')
                            print(f"      Found {len(user_links)} total user links on page")
                            
                            if user_links:
                                # Take the first user link as likely to be the author
                                first_user = user_links[0]
                                user_text = await first_user.text_content()
                                if user_text and user_text.strip():
                                    commit_info['author'] = user_text.strip()
                                    print(f"      ✅ Found author from first user link: {user_text.strip()}")
                        except Exception as broad_error:
                            print(f"      Broader author search failed: {broad_error}")
                
                if 'author' not in commit_info:
                    print(f"      ❌ Could not find author information")
                
                # Method 3: Look for date info
                date_selectors = [
                    'relative-time[datetime]',
                    'time[datetime]',
                    '[data-testid="latest-commit"] relative-time'
                ]
                
                for selector in date_selectors:
                    try:
                        time_element = await page.query_selector(selector)
                        if time_element:
                            date_attr = await time_element.get_attribute('datetime')
                            if date_attr:
                                commit_info['date'] = date_attr
                                print(f"      Found date using selector: {selector}")
                                break
                    except Exception as e:
                        print(f"      Date selector '{selector}' failed: {e}")
                        continue
                
                if commit_info:
                    print(f"      Successfully extracted commit info: {commit_info}")
                    
                    # If we don't have author info, try to get it from commits page
                    if 'author' not in commit_info and commit_info.get('sha'):
                        print(f"      No author on file page, trying commits page for author...")
                        author_info = await self.get_author_from_commits_page(page, commit_info['sha'])
                        if author_info:
                            commit_info['author'] = author_info
                            print(f"      ✅ Found author from commits page: {author_info}")
                    
                    return commit_info
                else:
                    print(f"      Could not find commit info on file page")
                    
                    # Try going to commits page as fallback
                    return await self.try_commits_page_fallback(page, file_path)
                    
            except Exception as header_error:
                print(f"      Error extracting from file header: {header_error}")
                return await self.try_commits_page_fallback(page, file_path)
                
        except Exception as e:
            print(f"      Error accessing file: {e}")
            return None
    
    async def get_author_from_commits_page(self, page, commit_sha):
        """Get author info from the specific commit page."""
        try:
            commit_url = f"{self.base_url}/{self.repo}/commit/{commit_sha}"
            print(f"        Visiting commit page: {commit_url}")
            
            await page.goto(commit_url, wait_until='domcontentloaded', timeout=15000)
            await asyncio.sleep(2)
            
            # Look for author on commit page
            author_selectors = [
                'a[data-hovercard-type="user"]',
                '.commit-author a',
                '.author a',
                '[data-testid="author-name"]',
                '.user-mention',
                '.commit-meta .text-mono',
                '.commit-author',
                'strong a'
            ]
            
            print(f"        Checking {len(author_selectors)} author selectors...")
            for i, selector in enumerate(author_selectors):
                try:
                    author_element = await page.query_selector(selector)
                    if author_element:
                        author_text = await author_element.text_content()
                        print(f"        Selector {i+1} found element with text: '{author_text}'")
                        if author_text and author_text.strip() and len(author_text.strip()) > 1:
                            # Make sure it's not just "committed" or other non-name text
                            if not any(word in author_text.lower() for word in ['committed', 'authored', 'ago', 'commit']):
                                print(f"        ✅ Found author on commit page: {author_text.strip()}")
                                return author_text.strip()
                    else:
                        print(f"        Selector {i+1} ({selector}): No element found")
                except Exception as e:
                    print(f"        Selector {i+1} error: {e}")
                    continue
            
            # Last resort: try to find any text that looks like a username
            try:
                print(f"        Trying to find any username-like text...")
                page_content = await page.content()
                # Look for patterns like @username or common GitHub username patterns
                import re
                username_matches = re.findall(r'@([a-zA-Z0-9\-_]+)', page_content)
                if username_matches:
                    first_username = username_matches[0]
                    print(f"        Found potential username in content: @{first_username}")
                    return first_username
            except Exception as content_error:
                print(f"        Content parsing failed: {content_error}")
            
            print(f"        No author found on commit page")
            return None
            
        except Exception as e:
            print(f"        Error getting author from commit page: {e}")
            return None
    
    async def try_commits_page_fallback(self, page, file_path):
        """Fallback method to try commits history page."""
        try:
            commits_url = f"{self.base_url}/{self.repo}/commits/{self.branch}/{file_path}"
            print(f"      Trying commits page as fallback: {commits_url}")
            
            await page.goto(commits_url, wait_until='domcontentloaded', timeout=20000)
            await asyncio.sleep(3)
            
            page_title = await page.title()
            print(f"      Commits page title: {page_title}")
            
            # Check if it's a real 404 (not just containing "404" somewhere)
            if ("404" in page_title and "not found" in page_title.lower()) or \
               ("not found" in page_title.lower() and len(page_title) < 50):
                print(f"      Commits page returned real 404 error")
                return None
            
            # If we have a history page title, we're on the right page
            if "history" in page_title.lower():
                print(f"      ✅ Successfully on commits history page")
            else:
                print(f"      ⚠️ Unexpected page title, but continuing...")
            
            # Try to find commit elements on commits page with better debugging
            commit_selectors = [
                'div[data-testid="commit-row"]',
                'li[data-testid="commit-row"]', 
                '.Box-row--focus-gray.py-2',
                '.js-navigation-item',
                'div.Box-row',
                '.commit-group-item',
                'div.d-table',
                '.Box-row',
                # Additional selectors for newer GitHub layout
                'article',
                '.commit-item',
                '[data-testid="commit-item"]',
                '.commit',
                'li.Box-row',
                'div[class*="commit"]'
            ]
            
            first_commit = None
            print(f"      Trying {len(commit_selectors)} different selectors to find commits...")
            for i, selector in enumerate(commit_selectors):
                try:
                    print(f"        Trying selector {i+1}/{len(commit_selectors)}: {selector}")
                    elements = await page.query_selector_all(selector)
                    print(f"        Found {len(elements)} elements with this selector")
                    
                    if elements:
                        first_commit = elements[0]
                        print(f"      ✅ Found commit using selector: {selector}")
                        break
                        
                    # If we didn't find any with wait_for_selector, try a quicker approach
                    await page.wait_for_selector(selector, timeout=2000)
                    first_commit = await page.query_selector(selector)
                    if first_commit:
                        print(f"      ✅ Found commit using selector (with wait): {selector}")
                        break
                except Exception as e:
                    print(f"        Selector failed: {e}")
                    continue
            
            if not first_commit:
                print(f"      No commit elements found with standard selectors")
                print(f"      Trying alternative approach - looking for any commit links...")
                
                # Alternative approach: find any links to commits and extract info from them
                try:
                    all_commit_links = await page.query_selector_all('a[href*="/commit/"]')
                    print(f"      Found {len(all_commit_links)} commit links on page")
                    
                    if all_commit_links:
                        # Use the first commit link as our "commit element"
                        first_commit_link = all_commit_links[0]
                        href = await first_commit_link.get_attribute('href')
                        text = await first_commit_link.text_content()
                        print(f"      First commit link: {href}")
                        print(f"      Commit link text: {text}")
                        
                        # Try to extract commit info from this approach
                        commit_info = {}
                        
                        # Get SHA from href
                        sha_match = re.search(r'/commit/([a-f0-9]+)', href)
                        if sha_match:
                            commit_info['sha'] = sha_match.group(1)[:7]
                            print(f"      Extracted SHA: {commit_info['sha']}")
                        
                        # Get message from link text
                        if text and text.strip():
                            commit_info['message'] = text.strip()
                            print(f"      Extracted message: {commit_info['message'][:50]}...")
                        
                        # Try to find author and date near this link
                        parent_element = await first_commit_link.evaluate_handle('el => el.closest("li, div, tr")')
                        if parent_element:
                            # Look for relative-time in the parent
                            time_element = await parent_element.query_selector('relative-time')
                            if time_element:
                                date_attr = await time_element.get_attribute('datetime')
                                if date_attr:
                                    commit_info['date'] = date_attr
                                    print(f"      Extracted date: {date_attr}")
                            
                            # Look for author link in the parent
                            author_element = await parent_element.query_selector('a[data-hovercard-type="user"]')
                            if author_element:
                                author_text = await author_element.text_content()
                                if author_text and author_text.strip():
                                    commit_info['author'] = author_text.strip()
                                    print(f"      Extracted author: {commit_info['author']}")
                        
                        if commit_info:
                            print(f"      ✅ Successfully extracted commit info using alternative method")
                            return commit_info
                        
                except Exception as alt_error:
                    print(f"      Alternative approach failed: {alt_error}")
                
                print(f"      ❌ Could not find commit elements using any method")
                return None
            
            # Extract commit info from the found commit element
            commit_info = {}
            
            # Get commit message
            message_selectors = [
                'p[data-testid="commit-title"]',
                'a[data-testid="commit-title"]',
                '.commit-title a',
                'a.Link--primary',
                'a[href*="/commit/"]'
            ]
            
            for selector in message_selectors:
                try:
                    message_element = await first_commit.query_selector(selector)
                    if message_element:
                        message_text = await message_element.text_content()
                        if message_text and message_text.strip():
                            commit_info['message'] = message_text.strip()
                            break
                except:
                    continue
            
            # Get author with expanded selectors
            author_selectors = [
                'a[data-testid="author-name"]',
                'a[data-hovercard-type="user"]',
                '.commit-author a',
                '.author a',
                'span.commit-author a',
                '.commit-meta a[data-hovercard-type="user"]'
            ]
            
            for selector in author_selectors:
                try:
                    author_element = await first_commit.query_selector(selector)
                    if author_element:
                        author_text = await author_element.text_content()
                        if author_text and author_text.strip():
                            commit_info['author'] = author_text.strip()
                            print(f"      Found author in commits page: {author_text.strip()}")
                            break
                except:
                    continue
            
            # Get date
            date_selectors = [
                'relative-time[datetime]',
                'time[datetime]'
            ]
            
            for selector in date_selectors:
                try:
                    time_element = await first_commit.query_selector(selector)
                    if time_element:
                        date_attr = await time_element.get_attribute('datetime')
                        if date_attr:
                            commit_info['date'] = date_attr
                            break
                except:
                    continue
            
            # Get SHA
            sha_selectors = [
                'a[data-testid="commit-sha"]',
                'a[href*="/commit/"]'
            ]
            
            for selector in sha_selectors:
                try:
                    sha_element = await first_commit.query_selector(selector)
                    if sha_element:
                        href = await sha_element.get_attribute('href')
                        if href:
                            sha_match = re.search(r'/commit/([a-f0-9]+)', href)
                            if sha_match:
                                commit_info['sha'] = sha_match.group(1)[:7]
                                break
                except:
                    continue
            
            return commit_info if commit_info else None
            
        except Exception as e:
            print(f"      Error in commits page fallback: {e}")
            return None

    async def extract_all_rules_info(self):
        """Extract information for all rules files using Playwright."""
        print("TMF Rules Files Playwright Extractor")
        print("=" * 40)
        
        playwright, browser, context, page = await self.setup_browser()
        
        try:
            # First, login to GitHub
            login_success = await self.login_to_github(page)
            if not login_success:
                print("❌ Failed to login to GitHub. Cannot continue with private repository access.")
                return []
            
            # Get all TMF directories
            directories = await self.get_tmf_directories(page)
            
            print(f"Processing all {len(directories)} TMF directories...")
            
            all_rules_info = []
            
            for directory in directories:
                print(f"\nProcessing directory: {directory}")
                
                # Find rules files in this directory
                rules_files = await self.find_rules_files_in_directory(page, directory)
                
                for rules_file in rules_files:
                    # Get commit information
                    commit_info = await self.get_file_commit_info(page, directory, rules_file)
                    
                    file_info = {
                        'directory': directory,
                        'filename': rules_file,
                        'file_path': f'{self.apis_path}/{directory}/{rules_file}',
                        'last_commit_date': commit_info.get('date', '') if commit_info else '',
                        'last_commit_message': commit_info.get('message', '') if commit_info else '',
                        'last_author': commit_info.get('author', '') if commit_info else '',
                        'commit_sha': commit_info.get('sha', '') if commit_info else '',
                        'extraction_method': 'playwright'
                    }
                    
                    all_rules_info.append(file_info)
                    
                    # Small delay between requests
                    await asyncio.sleep(0.5)  # Shorter delay
                
                # Small delay between directories
                await asyncio.sleep(1)
            
            return all_rules_info
            
        except Exception as e:
            print(f"Error during extraction: {e}")
            return []
            
        finally:
            # Clean up safely
            try:
                await context.close()
            except:
                pass
            try:
                await browser.close()
            except:
                pass
            try:
                await playwright.stop()
            except:
                pass
    
    def save_to_csv(self, rules_info, filename='tmf_rules_playwright.csv'):
        """Save the extracted information to CSV."""
        if not rules_info:
            print("No rules information to save.")
            return
        
        fieldnames = [
            'directory',
            'filename',
            'file_path',
            'last_commit_date',
            'last_commit_message',
            'last_author',
            'commit_sha',
            'extraction_method'
        ]
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rules_info)
        
        print(f"\n✓ Results saved to: {filename}")
        print(f"  Total files processed: {len(rules_info)}")
        
        return filename

async def main():
    """Main execution function."""
    print("TMF Rules Files Playwright Scraper")
    print("=" * 35)
    
    scraper = TMFPlaywrightScraper()
    
    try:
        # Extract all rules information
        rules_info = await scraper.extract_all_rules_info()
        
        # Save to CSV
        if rules_info:
            filename = scraper.save_to_csv(rules_info)
            
            print("\n" + "=" * 50)
            print("EXTRACTION COMPLETED")
            print("n" * 50)
            print(f"Successfully extracted {len(rules_info)} rules files")
            print(f"Results saved to: {filename}")
            
            # Show summary
            directories = set(info['directory'] for info in rules_info)
            print(f"\nDirectories processed: {len(directories)}")
            print("Sample results:")
            for i, info in enumerate(rules_info[:5]):
                print(f"  {i+1}. {info['directory']}/{info['filename']}")
                if info['last_commit_date']:
                    print(f"     Last modified: {info['last_commit_date']} by {info['last_author']}")
        else:
            print("\nNo rules files found!")
            print("This might indicate:")
            print("1. No .rules.yaml files exist in the repository")
            print("2. Network or access issues")
            print("3. Changes in GitHub's page structure")
    
    except KeyboardInterrupt:
        print("\nExtraction cancelled by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Consider running with headless=False for debugging")

if __name__ == "__main__":
    # Install Playwright browsers if needed
    print("Ensuring Playwright browsers are installed...")
    os.system("python -m playwright install chromium")
    
    # Run the async main function
    asyncio.run(main())