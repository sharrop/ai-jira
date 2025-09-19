#!/usr/bin/env python3
"""
Script to explore the TMF repository structure and verify the correct paths.
"""

import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def setup_session():
    """Setup requests session with proxy configuration."""
    session = requests.Session()
    
    # Configure proxy
    http_proxy = os.getenv('HTTP_PROXY') or os.getenv('http_proxy')
    https_proxy = os.getenv('HTTPS_PROXY') or os.getenv('https_proxy')
    
    if http_proxy or https_proxy:
        proxies = {}
        if http_proxy:
            proxies['http'] = http_proxy
        if https_proxy:
            proxies['https'] = https_proxy
        session.proxies.update(proxies)
        print(f"Using proxy: {https_proxy}")
    
    session.headers.update({
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "TMF-Repository-Explorer"
    })
    
    return session

def test_repo_access(session, repo_name):
    """Test access to the repository."""
    url = f"https://api.github.com/repos/{repo_name}"
    
    try:
        response = session.get(url, timeout=30)
        print(f"Repository access test for {repo_name}: {response.status_code}")
        
        if response.status_code == 200:
            repo_data = response.json()
            print(f"✓ Repository found: {repo_data['full_name']}")
            print(f"  Description: {repo_data.get('description', 'No description')}")
            print(f"  Default branch: {repo_data['default_branch']}")
            print(f"  Private: {repo_data['private']}")
            return True
        elif response.status_code == 404:
            print("✗ Repository not found (404)")
            return False
        elif response.status_code == 403:
            print("✗ Access forbidden (403) - may be private")
            return False
        else:
            print(f"✗ Unexpected response: {response.status_code}")
            print(response.text[:200])
            return False
            
    except Exception as e:
        print(f"✗ Error accessing repository: {e}")
        return False

def explore_root_contents(session, repo_name):
    """Explore the root contents of the repository."""
    url = f"https://api.github.com/repos/{repo_name}/contents"
    
    try:
        response = session.get(url, timeout=30)
        print(f"\nRoot directory exploration: {response.status_code}")
        
        if response.status_code == 200:
            contents = response.json()
            print(f"✓ Found {len(contents)} items in root directory:")
            
            directories = [item for item in contents if item['type'] == 'dir']
            files = [item for item in contents if item['type'] == 'file']
            
            print(f"  Directories ({len(directories)}):")
            for item in directories:
                print(f"    📁 {item['name']}")
            
            print(f"  Files ({len(files)}):")
            for item in files[:10]:  # Show first 10 files
                print(f"    📄 {item['name']}")
            
            if len(files) > 10:
                print(f"    ... and {len(files) - 10} more files")
            
            return contents
        else:
            print(f"✗ Failed to access root directory: {response.status_code}")
            return []
            
    except Exception as e:
        print(f"✗ Error exploring root directory: {e}")
        return []

def explore_specific_path(session, repo_name, path):
    """Explore a specific path in the repository."""
    url = f"https://api.github.com/repos/{repo_name}/contents/{path}"
    
    try:
        response = session.get(url, timeout=30)
        print(f"\nExploring path '{path}': {response.status_code}")
        
        if response.status_code == 200:
            contents = response.json()
            print(f"✓ Found {len(contents)} items in {path}:")
            
            for item in contents:
                type_icon = "📁" if item['type'] == 'dir' else "📄"
                print(f"    {type_icon} {item['name']}")
            
            return contents
        elif response.status_code == 404:
            print(f"✗ Path '{path}' not found (404)")
            return []
        else:
            print(f"✗ Failed to access path '{path}': {response.status_code}")
            return []
            
    except Exception as e:
        print(f"✗ Error exploring path '{path}': {e}")
        return []

def main():
    """Main exploration function."""
    print("TMF Repository Explorer")
    print("======================")
    
    session = setup_session()
    
    # Try different possible repository names
    possible_repos = [
        "tmforum-rand/OAS_Open_API_And_Data_Model",
        "tmforum/OAS_Open_API_And_Data_Model", 
        "TMForum/OAS_Open_API_And_Data_Model",
        "tmforum-rand/OpenAPI_And_DataModel",
        "tmforum/OpenAPI_And_DataModel"
    ]
    
    working_repo = None
    
    for repo in possible_repos:
        print(f"\n{'='*50}")
        print(f"Testing repository: {repo}")
        print('='*50)
        
        if test_repo_access(session, repo):
            working_repo = repo
            break
    
    if working_repo:
        print(f"\n{'='*50}")
        print(f"Exploring working repository: {working_repo}")
        print('='*50)
        
        # Explore root contents
        root_contents = explore_root_contents(session, working_repo)
        
        # Try to find the APIs directory
        possible_paths = [
            "files/apis",
            "APIs",
            "apis", 
            "files/APIs",
            "OpenAPI"
        ]
        
        for path in possible_paths:
            explore_specific_path(session, working_repo, path)
    
    else:
        print("\n" + "="*50)
        print("TROUBLESHOOTING SUGGESTIONS")
        print("="*50)
        print("1. The repository might be private - check if you need authentication")
        print("2. The repository name might be different")
        print("3. Try browsing GitHub directly to verify the exact repository name")
        print("4. You might need a GitHub token for private repositories")

if __name__ == "__main__":
    main()