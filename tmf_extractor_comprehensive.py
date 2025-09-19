#!/usr/bin/env python3
"""
Comprehensive solution for extracting TMF rules files information.
Supports multiple methods including direct repository access.
"""

import requests
import csv
import os
import subprocess
import json
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def method_1_github_api_with_auth():
    """Method 1: GitHub API with authentication token."""
    print("\n" + "="*60)
    print("METHOD 1: GitHub API with Authentication")
    print("="*60)
    
    github_token = input("Enter your GitHub personal access token (or press Enter to skip): ").strip()
    
    if not github_token:
        print("Skipping GitHub API method - no token provided")
        return False
    
    # Add token to .env for future use
    print(f"Adding GITHUB_TOKEN to .env file...")
    with open('.env', 'a') as f:
        f.write(f"\nGITHUB_TOKEN={github_token}\n")
    
    # Update the main script and run it
    os.environ['GITHUB_TOKEN'] = github_token
    
    try:
        result = subprocess.run(['python', 'github_rules_extractor.py'], 
                              capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            print("✓ GitHub API extraction completed successfully!")
            print(result.stdout)
            return True
        else:
            print("✗ GitHub API extraction failed:")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"✗ Error running GitHub API extraction: {e}")
        return False

def method_2_clone_and_extract():
    """Method 2: Clone repository and use git commands."""
    print("\n" + "="*60)
    print("METHOD 2: Clone Repository and Use Git Commands")
    print("="*60)
    
    repo_url = input("Enter the full repository URL (e.g., https://github.com/org/repo.git): ").strip()
    
    if not repo_url:
        print("Skipping clone method - no URL provided")
        return False
    
    try:
        # Clone the repository
        print(f"Cloning repository: {repo_url}")
        subprocess.run(['git', 'clone', repo_url, 'temp_repo'], check=True)
        
        # Change to the repository directory
        os.chdir('temp_repo')
        
        # Find all .rules.yaml files
        print("Finding all .rules.yaml files...")
        find_result = subprocess.run(['find', 'files/apis', '-name', '*.rules.yaml'], 
                                   capture_output=True, text=True)
        
        if find_result.returncode != 0:
            print("Using Windows-compatible file search...")
            # Windows alternative using PowerShell
            find_result = subprocess.run(['powershell', '-Command', 
                                        'Get-ChildItem -Path "files/apis" -Recurse -Filter "*.rules.yaml"'], 
                                       capture_output=True, text=True)
        
        rules_files = find_result.stdout.strip().split('\n') if find_result.stdout.strip() else []
        
        if not rules_files or rules_files == ['']:
            print("No .rules.yaml files found")
            return False
        
        print(f"Found {len(rules_files)} rules files")
        
        # Extract git information for each file
        results = []
        for file_path in rules_files:
            if not file_path.strip():
                continue
                
            print(f"Processing: {file_path}")
            
            # Get last commit info for this file
            git_cmd = ['git', 'log', '-1', '--format=%H|%ai|%an|%s', '--', file_path]
            git_result = subprocess.run(git_cmd, capture_output=True, text=True)
            
            if git_result.returncode == 0 and git_result.stdout.strip():
                commit_info = git_result.stdout.strip().split('|', 3)
                if len(commit_info) == 4:
                    results.append({
                        'file_path': file_path,
                        'directory': os.path.dirname(file_path).split('/')[-1],
                        'filename': os.path.basename(file_path),
                        'commit_sha': commit_info[0][:7],
                        'last_commit_date': commit_info[1],
                        'last_author': commit_info[2],
                        'last_commit_message': commit_info[3]
                    })
        
        # Go back to original directory
        os.chdir('..')
        
        # Save results to CSV
        if results:
            save_results_to_csv(results, 'tmf_rules_git_method.csv')
            return True
        else:
            print("No commit information could be extracted")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"✗ Git command failed: {e}")
        return False
    except Exception as e:
        print(f"✗ Error in clone method: {e}")
        return False

def method_3_manual_csv_template():
    """Method 3: Create a manual CSV template for user to fill."""
    print("\n" + "="*60)
    print("METHOD 3: Manual CSV Template")
    print("="*60)
    
    # Create a template with known TMF API directories
    known_tmf_apis = [
        "TMF620_Product_Catalog",
        "TMF621_Trouble_Ticket", 
        "TMF622_Product_Ordering",
        "TMF623_Service_Catalog",
        "TMF624_Resource_Catalog",
        "TMF625_Service_Ordering",
        "TMF629_Customer_Billing",
        "TMF632_Party_Management",
        "TMF633_Service_Quality_Management",
        "TMF634_Resource_Inventory",
        "TMF635_Usage_Management",
        "TMF637_Product_Inventory",
        "TMF638_Service_Inventory",
        "TMF639_Resource_Activation",
        "TMF641_Service_Ordering",
        "TMF645_Service_Qualification",
        "TMF648_Quote_Management",
        "TMF649_Customer_Data_Management",
        "TMF651_Agreement_Management",
        "TMF663_Shopping_Cart",
        "TMF666_Account_Management",
        "TMF667_Document_Management",
        "TMF668_Party_Role_Management",
        "TMF669_Party_Interaction",
        "TMF671_Promotion_Management",
        "TMF672_User_Roles_Permissions",
        "TMF673_Geographic_Address",
        "TMF674_Geographic_Site",
        "TMF675_Geographic_Location",
        "TMF676_Payment_Management",
        "TMF677_Usage_Consumption",
        "TMF678_Customer_Bill_Management",
        "TMF679_Product_Offering_Qualification",
        "TMF681_Communication_Management",
        "TMF688_Event_Management",
        "TMF689_Party_Privacy_Management"
    ]
    
    template_data = []
    for api in known_tmf_apis:
        template_data.append({
            'directory': api,
            'filename': f'{api}.rules.yaml',
            'file_path': f'files/apis/{api}/{api}.rules.yaml',
            'last_commit_date': 'YYYY-MM-DD HH:MM:SS',
            'last_commit_message': 'Fill in manually',
            'last_author': 'Fill in manually',
            'commit_sha': 'Fill in manually'
        })
    
    save_results_to_csv(template_data, 'tmf_rules_template.csv')
    
    print(f"✓ Created template CSV with {len(template_data)} known TMF APIs")
    print("You can manually fill in the commit information for files that exist")
    return True

def save_results_to_csv(results, filename):
    """Save results to CSV file."""
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
        writer.writerows(results)
    
    print(f"✓ Results saved to: {filename}")
    print(f"  Total entries: {len(results)}")

def main():
    """Main function offering multiple extraction methods."""
    print("TMF Rules Files Information Extractor")
    print("Multiple Methods Available")
    print("====================================")
    
    print("\nAvailable extraction methods:")
    print("1. GitHub API with authentication token (recommended)")
    print("2. Clone repository and use git commands")
    print("3. Generate manual CSV template")
    print("4. Exit")
    
    while True:
        choice = input("\nSelect method (1-4): ").strip()
        
        if choice == '1':
            if method_1_github_api_with_auth():
                break
        elif choice == '2':
            if method_2_clone_and_extract():
                break
        elif choice == '3':
            if method_3_manual_csv_template():
                break
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select 1-4.")
    
    print("\n" + "="*60)
    print("NEXT STEPS")
    print("="*60)
    print("1. Check the generated CSV file")
    print("2. If using method 3, manually fill in the commit information")
    print("3. The CSV can be opened in Excel or any spreadsheet application")

if __name__ == "__main__":
    main()