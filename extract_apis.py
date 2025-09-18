#!/usr/bin/env python3
"""
Extract API information from TMForum directory HTML file.
Creates a CSV file with API long names, short names (TMF codes), and versions.
"""

import re
import csv
from pathlib import Path

def extract_api_info(html_content):
    """Extract API information from HTML content."""
    apis = []
    
    # Find all anchor tags with href attributes and their content
    anchor_pattern = r'<a class="w-full"\s+href="([^"]+)"[^>]*>.*?<h5 class="pb-1 text-core-blue text-sm leading-tight">([^<]+(?:\s*[^<]+)*)</h5>.*?</a>'
    anchor_matches = re.findall(anchor_pattern, html_content, re.DOTALL)
    
    for href, api_name in anchor_matches:
        # Clean up API names by removing extra whitespace and newlines
        cleaned_name = re.sub(r'\s+', ' ', api_name.strip())
        
        # Find the section containing this API name to extract TMF code and versions
        # Escape special regex characters in the API name for pattern matching
        escaped_name = re.escape(api_name)
        api_section_pattern = rf'<h5 class="pb-1 text-core-blue text-sm leading-tight">{escaped_name}</h5>.*?</div>\s*</div>\s*</div>'
        api_match = re.search(api_section_pattern, html_content, re.DOTALL)
        
        if api_match:
            api_section = api_match.group(0)
            
            # Extract TMF code
            tmf_pattern = r'<span>(TMF\d{3})</span>'
            tmf_match = re.search(tmf_pattern, api_section)
            tmf_code = tmf_match.group(1) if tmf_match else 'Unknown'
            
            # Extract versions
            version_pattern = r'<span>(v\d+(?:\.\d+)*)</span>'
            versions = re.findall(version_pattern, api_section)
            
            if versions:
                # Sort versions to find the highest one
                # Convert versions to tuples of integers for proper sorting
                def version_key(v):
                    # Remove 'v' prefix and split by '.'
                    parts = v[1:].split('.')
                    # Convert to integers, padding with 0s if needed
                    return tuple(int(part) for part in parts) + (0,) * (3 - len(parts))
                
                sorted_versions = sorted(versions, key=version_key)
                highest_version = sorted_versions[-1]
                versions_str = '; '.join(sorted(versions, key=version_key))
                
                # Construct URL with the highest version
                # Extract base path from href and replace version
                base_url_pattern = r'(/oda/open-apis/directory/[^/]+)/v[\d.]+$'
                base_match = re.search(base_url_pattern, href)
                if base_match:
                    base_path = base_match.group(1)
                    # Create URL with highest version
                    full_url = f"https://www.tmforum.org{base_path}/{highest_version}"
                else:
                    # Fallback to original href if pattern doesn't match
                    full_url = f"https://www.tmforum.org{href}"
            else:
                versions_str = 'Unknown'
                full_url = f"https://www.tmforum.org{href}"
            
            apis.append({
                'long_name': cleaned_name,
                'short_name': tmf_code,
                'url': full_url,
                'versions': versions_str
            })
    
    return apis

def main():
    """Main function to extract API data and create CSV."""
    html_file = Path('data/directory.htm')
    
    if not html_file.exists():
        print(f"Error: {html_file} not found")
        return
    
    print(f"Reading HTML file: {html_file}")
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    print("Extracting API information...")
    apis = extract_api_info(html_content)
    
    # Create CSV file
    csv_file = Path('data/tmf_apis.csv')
    print(f"Writing to CSV file: {csv_file}")
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Write header
        writer.writerow(['Long Name', 'Short Name (TMF Code)', 'URL', 'Versions'])
        
        # Write API data
        for api in apis:
            writer.writerow([api['long_name'], api['short_name'], api['url'], api['versions']])
    
    print(f"Extracted {len(apis)} APIs")
    print(f"CSV file created: {csv_file}")
    
    # Display first few entries for verification
    if apis:
        print("\nFirst few entries:")
        print("-" * 120)
        for i, api in enumerate(apis[:5]):
            print(f"{i+1:2d}. {api['long_name']} ({api['short_name']}) - {api['versions']}")
            print(f"    URL: {api['url']}")
        
        if len(apis) > 5:
            print(f"... and {len(apis) - 5} more")

if __name__ == '__main__':
    main()