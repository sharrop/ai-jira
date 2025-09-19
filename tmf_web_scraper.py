#!/usr/bin/env python3
"""
TMF Rules Files Extractor using GitHub web scraping.
Since API access isn't working but web browsing is, we'll use requests to scrape the GitHub pages.
"""

import requests
import csv
import re
import os
from datetime import datetime
from dotenv import load_dotenv
from urllib.parse import urljoin, quote
import time

# Load environment variables
load_dotenv()

class GitHubWebScraper:
    def __init__(self):
        """Initialize the web scraper with session and proxy settings."""
        self.base_url = "https://github.com"
        self.repo = "tmforum-rand/OAS_Open_API_And_Data_Model"
        self.branch = "v5.0.0-dev"
        self.apis_path = "apis"
        
        self.session = requests.Session()
        self._configure_proxy()
        self._configure_headers()
    
    def _configure_proxy(self):
        """Configure proxy settings."""
        http_proxy = os.getenv('HTTP_PROXY') or os.getenv('http_proxy')
        https_proxy = os.getenv('HTTPS_PROXY') or os.getenv('https_proxy')
        
        if http_proxy or https_proxy:
            proxies = {}
            if http_proxy:
                proxies['http'] = http_proxy
                print(f"Using HTTP proxy: {http_proxy}")
            if https_proxy:
                proxies['https'] = https_proxy
                print(f"Using HTTPS proxy: {https_proxy}")
            
            self.session.proxies.update(proxies)
    
    def _configure_headers(self):
        """Configure headers for web scraping with GitHub authentication."""
        # Try to get GitHub token for web authentication
        github_token = os.getenv('GITHUB_TOKEN')
        
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
        })
        
        if github_token:
            print("Using GitHub token for authentication")
            # For web requests, we might need to handle authentication differently
            # GitHub web interface uses cookies, not API tokens
    
    def get_directories_list(self):
        """Get list of directories in the apis folder."""
        url = f"{self.base_url}/{self.repo}/tree/{self.branch}/{self.apis_path}"
        
        print(f"Fetching directories from: {url}")
        
        try:
            # Add delay and retry logic
            time.sleep(2)
            response = self.session.get(url, timeout=30)
            
            print(f"Response status: {response.status_code}")
            
            if response.status_code == 429:
                print("Rate limited. Waiting 60 seconds...")
                time.sleep(60)
                response = self.session.get(url, timeout=30)
            
            response.raise_for_status()
            
            # Save HTML for debugging
            with open('debug_apis_page.html', 'w', encoding='utf-8') as f:
                f.write(response.text)
            print("Saved page HTML to debug_apis_page.html for inspection")
            
            # Parse HTML to find directory links
            html_content = response.text
            
            # Multiple patterns to try for GitHub's directory listings
            patterns = [
                # Standard GitHub tree view pattern
                r'<a[^>]*href="/{}/tree/{}/{}\/([^/"]+)"[^>]*>'.format(
                    re.escape(self.repo), re.escape(self.branch), re.escape(self.apis_path)
                ),
                # Alternative pattern
                r'href="[^"]*/{}/tree/{}/{}\/([^/"]+)"'.format(
                    re.escape(self.repo), re.escape(self.branch), re.escape(self.apis_path)
                ),
                # Simple pattern for directory names
                r'/{}/tree/{}/{}/([A-Z][A-Za-z0-9_]+)'.format(
                    re.escape(self.repo), re.escape(self.branch), re.escape(self.apis_path)
                )
            ]
            
            directories = set()
            
            for pattern in patterns:
                matches = re.findall(pattern, html_content)
                for match in matches:
                    if isinstance(match, tuple):
                        dir_name = match[0] if match else None
                    else:
                        dir_name = match
                    
                    if dir_name and dir_name.startswith('TMF'):
                        directories.add(dir_name)
            
            directories = list(directories)
            print(f"Found {len(directories)} TMF directories using regex patterns")
            
            if not directories:
                print("No directories found with regex. Using fallback list...")
                # Return known TMF directories as fallback
                directories = [
                    "TMF620_Product_Catalog", "TMF621_Trouble_Ticket", "TMF622_Product_Ordering",
                    "TMF623_Service_Catalog", "TMF624_Resource_Catalog", "TMF625_Service_Ordering", 
                    "TMF629_Customer_Billing", "TMF632_Party_Management", "TMF633_Service_Quality_Management",
                    "TMF634_Resource_Inventory", "TMF635_Usage_Management", "TMF637_Product_Inventory",
                    "TMF638_Service_Inventory", "TMF639_Resource_Activation", "TMF641_Service_Ordering",
                    "TMF645_Service_Qualification", "TMF648_Quote_Management", "TMF663_Shopping_Cart",
                    "TMF666_Account_Management", "TMF667_Document_Management", "TMF668_Party_Role_Management",
                    "TMF669_Party_Interaction", "TMF671_Promotion_Management", "TMF672_User_Roles_Permissions",
                    "TMF673_Geographic_Address", "TMF674_Geographic_Site", "TMF675_Geographic_Location",
                    "TMF676_Payment_Management", "TMF677_Usage_Consumption", "TMF678_Customer_Bill_Management",
                    "TMF679_Product_Offering_Qualification", "TMF681_Communication_Management",
                    "TMF688_Event_Management", "TMF689_Party_Privacy_Management"
                ]
            
            print(f"Final directory list: {directories[:10]}..." if len(directories) > 10 else f"Final directory list: {directories}")
            return directories
            
        except Exception as e:
            print(f"Error fetching directories: {e}")
            print("Using fallback directory list...")
            # Return known TMF directories as fallback
            return [
                "TMF620_Product_Catalog", "TMF621_Trouble_Ticket", "TMF622_Product_Ordering",
                "TMF623_Service_Catalog", "TMF624_Resource_Catalog", "TMF625_Service_Ordering",
                "TMF629_Customer_Billing", "TMF632_Party_Management", "TMF641_Service_Ordering"
            ]
    
    def find_rules_files_in_directory(self, directory):
        """Find rules files in a specific directory."""
        url = f"{self.base_url}/{self.repo}/tree/{self.branch}/{self.apis_path}/{directory}"
        
        print(f"Checking directory: {directory}")
        
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            html_content = response.text
            
            # Look for .rules.yaml files
            rules_pattern = r'<a[^>]*href="[^"]*/{}/blob/{}/{}\/{}\/([^"]*\.rules\.yaml)"[^>]*>([^<]+)</a>'.format(
                re.escape(self.repo), re.escape(self.branch), re.escape(self.apis_path), re.escape(directory)
            )
            
            rules_files = []
            matches = re.findall(rules_pattern, html_content)
            
            for match in matches:
                file_name = match[0]
                rules_files.append(file_name)
            
            if rules_files:
                print(f"  Found {len(rules_files)} rules file(s): {rules_files}")
            else:
                print(f"  No rules files found")
            
            return rules_files
            
        except Exception as e:
            print(f"  Error checking directory {directory}: {e}")
            return []
    
    def get_file_commit_info(self, directory, filename):
        """Get commit information for a specific file."""
        # GitHub file history URL
        file_path = f"{self.apis_path}/{directory}/{filename}"
        url = f"{self.base_url}/{self.repo}/commits/{self.branch}/{file_path}"
        
        print(f"    Getting commit info for: {filename}")
        
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            html_content = response.text
            
            # Extract commit information from the commits page
            # Look for the first commit entry
            commit_info = self._parse_commit_info(html_content)
            
            if commit_info:
                print(f"      Last commit: {commit_info['date']} by {commit_info['author']}")
                return commit_info
            else:
                print(f"      Could not extract commit info")
                return None
                
        except Exception as e:
            print(f"      Error getting commit info: {e}")
            return None
    
    def _parse_commit_info(self, html_content):
        """Parse commit information from GitHub commits page HTML."""
        try:
            # Look for commit patterns in GitHub's HTML
            # These patterns might need adjustment based on GitHub's current HTML structure
            
            # Date pattern
            date_pattern = r'<relative-time[^>]*datetime="([^"]+)"'
            date_match = re.search(date_pattern, html_content)
            
            # Author pattern  
            author_pattern = r'<a[^>]*class="[^"]*commit-author[^"]*"[^>]*>([^<]+)</a>'
            author_match = re.search(author_pattern, html_content)
            
            # Message pattern
            message_pattern = r'<a[^>]*class="[^"]*message[^"]*"[^>]*>([^<]+)</a>'
            message_match = re.search(message_pattern, html_content)
            
            # SHA pattern
            sha_pattern = r'<a[^>]*href="[^"]*commit/([a-f0-9]{7})[a-f0-9]*"'
            sha_match = re.search(sha_pattern, html_content)
            
            if date_match:
                return {
                    'date': date_match.group(1),
                    'author': author_match.group(1) if author_match else 'Unknown',
                    'message': message_match.group(1) if message_match else 'No message',
                    'sha': sha_match.group(1) if sha_match else 'Unknown'
                }
            
            return None
            
        except Exception as e:
            print(f"Error parsing commit info: {e}")
            return None
    
    def extract_all_rules_info(self):
        """Extract information for all rules files."""
        print("Starting TMF Rules Files Web Extraction")
        print("="*50)
        print(f"Repository: {self.repo}")
        print(f"Branch: {self.branch}")
        print(f"Path: {self.apis_path}")
        
        # Get all directories
        directories = self.get_directories_list()
        
        if not directories:
            print("No directories found. Using fallback list...")
            # Fallback to known TMF APIs
            directories = [
                "TMF620_Product_Catalog", "TMF621_Trouble_Ticket", "TMF622_Product_Ordering",
                "TMF623_Service_Catalog", "TMF624_Resource_Catalog", "TMF625_Service_Ordering",
                "TMF629_Customer_Billing", "TMF632_Party_Management", "TMF633_Service_Quality_Management",
                "TMF634_Resource_Inventory", "TMF635_Usage_Management", "TMF637_Product_Inventory",
                "TMF638_Service_Inventory", "TMF639_Resource_Activation", "TMF641_Service_Ordering"
            ]
        
        all_rules_info = []
        
        for directory in directories:
            print(f"\nProcessing directory: {directory}")
            
            # Find rules files in this directory
            rules_files = self.find_rules_files_in_directory(directory)
            
            for rules_file in rules_files:
                # Get commit information
                commit_info = self.get_file_commit_info(directory, rules_file)
                
                file_info = {
                    'directory': directory,
                    'filename': rules_file,
                    'file_path': f'{self.apis_path}/{directory}/{rules_file}',
                    'last_commit_date': commit_info['date'] if commit_info else '',
                    'last_commit_message': commit_info['message'] if commit_info else '',
                    'last_author': commit_info['author'] if commit_info else '',
                    'commit_sha': commit_info['sha'] if commit_info else '',
                    'extraction_method': 'web_scraping'
                }
                
                all_rules_info.append(file_info)
                
                # Be nice to GitHub - add delay
                time.sleep(1)
        
        return all_rules_info
    
    def save_to_csv(self, rules_info, filename='tmf_rules_web_scraped.csv'):
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

def main():
    """Main execution function."""
    print("TMF Rules Files Web Scraper")
    print("="*30)
    
    scraper = GitHubWebScraper()
    
    try:
        # Extract all rules information
        rules_info = scraper.extract_all_rules_info()
        
        # Save to CSV
        if rules_info:
            filename = scraper.save_to_csv(rules_info)
            
            print("\n" + "="*50)
            print("EXTRACTION COMPLETED")
            print("="*50)
            print(f"Successfully extracted {len(rules_info)} rules files")
            print(f"Results saved to: {filename}")
            
            # Show summary
            directories = set(info['directory'] for info in rules_info)
            print(f"\nDirectories processed: {len(directories)}")
            print("Sample results:")
            for i, info in enumerate(rules_info[:3]):
                print(f"  {i+1}. {info['directory']}/{info['filename']}")
                if info['last_commit_date']:
                    print(f"     Last modified: {info['last_commit_date']} by {info['last_author']}")
        else:
            print("\nNo rules files found!")
            print("This might be due to:")
            print("1. Different HTML structure than expected")
            print("2. No .rules.yaml files in the repository")
            print("3. Network or access issues")
            
            print("\nFalling back to manual template...")
            # Create manual template as fallback
            import tmf_manual_solution
            tmf_manual_solution.create_manual_template()
    
    except KeyboardInterrupt:
        print("\nExtraction cancelled by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please use the manual template approach instead.")

if __name__ == "__main__":
    main()