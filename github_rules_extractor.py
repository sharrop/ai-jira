#!/usr/bin/env python3
"""
GitHub API script to extract TMF rules files information.
Creates a CSV with rules files, their last commit date, message, and author.
"""

import requests
import csv
import os
from datetime import datetime
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class GitHubRulesExtractor:
    def __init__(self, token=None):
        """Initialize with optional GitHub token for higher rate limits."""
        self.base_url = "https://api.github.com"
        self.repo = "tmforum-rand/OAS_Open_API_And_Data_Model"
        self.target_path = "apis"
        self.branch = "v5.0.0-dev"  # Specify the branch
        
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "TMF-Rules-Extractor"
        }
        
        if token:
            self.headers["Authorization"] = f"token {token}"
        
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        
        # Configure proxy settings from environment variables
        self._configure_proxy()
    
    def _configure_proxy(self):
        """Configure proxy settings from environment variables."""
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
        else:
            print("No proxy configuration found in environment variables")
    
    def get_directory_contents(self, path):
        """Get contents of a directory in the repository."""
        url = f"{self.base_url}/repos/{self.repo}/contents/{path}"
        
        # Add branch parameter
        params = {"ref": self.branch}
        
        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting directory contents for {path}: {e}")
            return []
    
    def find_subdirectories(self):
        """Find all subdirectories in the target path."""
        contents = self.get_directory_contents(self.target_path)
        subdirs = []
        
        for item in contents:
            if item['type'] == 'dir':
                subdirs.append(item['name'])
        
        print(f"Found {len(subdirs)} subdirectories in {self.target_path}")
        return subdirs
    
    def find_rules_files(self, subdirectory):
        """Find all *.rules.yaml files in a subdirectory."""
        path = f"{self.target_path}/{subdirectory}"
        contents = self.get_directory_contents(path)
        rules_files = []
        
        for item in contents:
            if item['type'] == 'file' and item['name'].endswith('.rules.yaml'):
                rules_files.append({
                    'name': item['name'],
                    'path': item['path'],
                    'sha': item['sha']
                })
        
        return rules_files
    
    def get_file_last_commit(self, file_path):
        """Get the last commit information for a specific file."""
        url = f"{self.base_url}/repos/{self.repo}/commits"
        params = {
            'path': file_path,
            'sha': self.branch,  # Specify the branch
            'per_page': 1  # Only get the most recent commit
        }
        
        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            commits = response.json()
            
            if commits:
                commit = commits[0]
                return {
                    'date': commit['commit']['committer']['date'],
                    'message': commit['commit']['message'],
                    'author': commit['commit']['author']['name'],
                    'sha': commit['sha'][:7]  # Short SHA
                }
            else:
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Error getting commit info for {file_path}: {e}")
            return None
    
    def extract_all_rules_info(self):
        """Extract information for all rules files."""
        print(f"Starting extraction of TMF rules files...")
        print(f"Repository: {self.repo}")
        print(f"Branch: {self.branch}")
        print(f"Target path: {self.target_path}")
        
        # Find all subdirectories
        subdirectories = self.find_subdirectories()
        
        all_rules_info = []
        total_files = 0
        
        for subdir in subdirectories:
            print(f"\nProcessing directory: {subdir}")
            
            # Find rules files in this subdirectory
            rules_files = self.find_rules_files(subdir)
            
            if rules_files:
                print(f"  Found {len(rules_files)} rules file(s)")
                
                for rules_file in rules_files:
                    print(f"    Processing: {rules_file['name']}")
                    
                    # Get commit information
                    commit_info = self.get_file_last_commit(rules_file['path'])
                    
                    if commit_info:
                        # Format the date
                        commit_date = datetime.fromisoformat(
                            commit_info['date'].replace('Z', '+00:00')
                        ).strftime('%Y-%m-%d %H:%M:%S UTC')
                        
                        all_rules_info.append({
                            'directory': subdir,
                            'filename': rules_file['name'],
                            'file_path': rules_file['path'],
                            'last_commit_date': commit_date,
                            'last_commit_message': commit_info['message'].strip(),
                            'last_author': commit_info['author'],
                            'commit_sha': commit_info['sha']
                        })
                        
                        total_files += 1
                    
                    # Be nice to the API - small delay between requests
                    time.sleep(0.1)
            else:
                print(f"  No rules files found in {subdir}")
        
        print(f"\nCompleted! Found {total_files} rules files total.")
        return all_rules_info
    
    def save_to_csv(self, rules_info, filename='tmf_rules_info.csv'):
        """Save the rules information to a CSV file."""
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
            'commit_sha'
        ]
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rules_info)
        
        print(f"Results saved to: {filename}")
        print(f"Total files processed: {len(rules_info)}")

def main():
    """Main execution function."""
    print("TMF Rules Files Information Extractor")
    print("=====================================")
    
    # Check for GitHub token in environment
    github_token = os.getenv('GITHUB_TOKEN')
    if github_token:
        print("Using GitHub token for authentication (higher rate limits)")
    else:
        print("No GitHub token found. Using unauthenticated requests (lower rate limits)")
        print("Set GITHUB_TOKEN environment variable for better performance")
    
    # Initialize extractor
    extractor = GitHubRulesExtractor(token=github_token)
    
    try:
        # Extract all rules information
        rules_info = extractor.extract_all_rules_info()
        
        # Save to CSV
        extractor.save_to_csv(rules_info)
        
        # Print summary
        print("\n" + "="*50)
        print("EXTRACTION SUMMARY")
        print("="*50)
        
        if rules_info:
            directories = set(info['directory'] for info in rules_info)
            print(f"Directories processed: {len(directories)}")
            print(f"Rules files found: {len(rules_info)}")
            print(f"Output file: tmf_rules_info.csv")
            
            # Show sample of results
            print("\nSample results:")
            for i, info in enumerate(rules_info[:3]):
                print(f"  {i+1}. {info['directory']}/{info['filename']}")
                print(f"     Last modified: {info['last_commit_date']} by {info['last_author']}")
        else:
            print("No rules files found!")
    
    except KeyboardInterrupt:
        print("\nExtraction cancelled by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()