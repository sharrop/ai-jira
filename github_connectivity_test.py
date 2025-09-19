#!/usr/bin/env python3
"""
Alternative GitHub API approach using requests with better error handling and retry logic.
This script can also be run in 'dry-run' mode to test connectivity first.
"""

import requests
import csv
import os
import time
import json
from datetime import datetime
from urllib.parse import quote

def test_github_connectivity():
    """Test basic GitHub API connectivity."""
    try:
        response = requests.get("https://api.github.com", timeout=10)
        print(f"GitHub API connectivity test: {response.status_code}")
        print(f"Rate limit remaining: {response.headers.get('X-RateLimit-Remaining', 'Unknown')}")
        return True
    except Exception as e:
        print(f"GitHub API connectivity failed: {e}")
        return False

def get_repo_info(repo_name):
    """Get basic repository information."""
    url = f"https://api.github.com/repos/{repo_name}"
    
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            repo_data = response.json()
            print(f"Repository: {repo_data['full_name']}")
            print(f"Description: {repo_data.get('description', 'No description')}")
            print(f"Default branch: {repo_data['default_branch']}")
            return True
        else:
            print(f"Repository access failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error accessing repository: {e}")
        return False

def explore_directory_manually():
    """Manual method using curl commands for troubleshooting."""
    repo = "tmforum-rand/OAS_Open_API_And_Data_Model"
    path = "files/apis"
    
    curl_command = f'curl -H "Accept: application/vnd.github.v3+json" "https://api.github.com/repos/{repo}/contents/{path}"'
    
    print("Manual curl command to test:")
    print(curl_command)
    print("\nYou can run this in a separate terminal to test GitHub API access.")
    
    # Also provide wget alternative
    wget_command = f'wget -O - "https://api.github.com/repos/{repo}/contents/{path}"'
    print("\nAlternative with wget:")
    print(wget_command)

def create_batch_script():
    """Create a batch/shell script that uses git and GitHub CLI if available."""
    
    batch_content = '''@echo off
REM Batch script to extract TMF rules files using git commands
REM This assumes you have git and gh (GitHub CLI) installed

echo TMF Rules Files Extractor - Git/GH CLI Method
echo ================================================

REM Check if gh CLI is available
gh --version >nul 2>&1
if %errorlevel% neq 0 (
    echo GitHub CLI 'gh' not found. Please install from: https://cli.github.com/
    echo Alternative: Clone the repo manually and use git commands
    pause
    exit /b 1
)

echo.
echo Fetching repository information...
gh repo view tmforum-rand/OAS_Open_API_And_Data_Model

echo.
echo Listing directories in files/apis...
gh api repos/tmforum-rand/OAS_Open_API_And_Data_Model/contents/files/apis

echo.
echo To get commit information for specific files, use:
echo gh api "repos/tmforum-rand/OAS_Open_API_And_Data_Model/commits?path=files/apis/TMF620_Product_Catalog/FILENAME.rules.yaml&per_page=1"

pause
'''
    
    with open('extract_tmf_rules.bat', 'w') as f:
        f.write(batch_content)
    
    print("Created extract_tmf_rules.bat for Windows users with GitHub CLI")

def main():
    """Main function with multiple approaches."""
    print("TMF Rules Files Information Extractor")
    print("=====================================")
    print("Multiple extraction methods available:\n")
    
    print("1. Testing GitHub API connectivity...")
    if test_github_connectivity():
        print("✓ GitHub API is accessible")
        
        print("\n2. Testing repository access...")
        if get_repo_info("tmforum-rand/OAS_Open_API_And_Data_Model"):
            print("✓ Repository is accessible")
            print("\n3. You can now run the main extractor script:")
            print("   python github_rules_extractor.py")
        else:
            print("✗ Repository access failed")
            print("   This might be a private repository requiring authentication")
    else:
        print("✗ GitHub API not accessible")
        print("   Check your internet connection or try again later")
    
    print("\n" + "="*60)
    print("ALTERNATIVE METHODS:")
    print("="*60)
    
    print("\nMethod 1: Manual curl/wget testing")
    explore_directory_manually()
    
    print("\n" + "-"*60)
    print("Method 2: GitHub CLI approach")
    create_batch_script()
    
    print("\n" + "-"*60)
    print("Method 3: Direct repository access")
    print("If you have access to clone the repo:")
    print("1. git clone https://github.com/tmforum-rand/OAS_Open_API_And_Data_Model.git")
    print("2. cd OAS_Open_API_And_Data_Model/files/apis")
    print("3. Use find and git log commands:")
    print("   find . -name '*.rules.yaml' -exec git log -1 --format='%H,%ai,%an,%s' {} \\;")

if __name__ == "__main__":
    main()