#!/usr/bin/env python3
"""
TMF API Lookup Tool

Demonstrates the TMF API lookup functionality added to check_issues.py
"""

import sys
import os

# Add the current directory to the path so we can import from check_issues
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from check_issues import load_tmf_apis, get_tmf_api_info, find_tmf_references_in_text

def main():
    """Main function for TMF API lookup tool"""
    print("🔍 TMF API Lookup Tool")
    print("=" * 50)
    
    # Load the APIs
    df = load_tmf_apis()
    if df.empty:
        print("❌ Could not load TMF APIs. Make sure data/tmf_apis.csv exists.")
        return
    
    print(f"📊 Loaded {len(df)} TMF APIs")
    
    # Interactive mode if no arguments provided
    if len(sys.argv) == 1:
        print("\n🎯 Interactive Mode")
        print("Enter TMF codes to lookup (e.g., TMF646, 646) or 'quit' to exit:")
        print("You can also enter text to search for TMF references.")
        
        while True:
            user_input = input("\n> ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
            
            if not user_input:
                continue
            
            # Check if it looks like a TMF code
            if user_input.upper().startswith('TMF') or user_input.isdigit():
                # Direct TMF lookup
                result = get_tmf_api_info(user_input)
                if result:
                    print(f"\n✅ Found: {result['long_name']}")
                    print(f"   TMF Code: {result['tmf_code']}")
                    print(f"   Latest Version: {result['highest_version']}")
                    print(f"   All Versions: {result['all_versions']}")
                    print(f"   Documentation: {result['url']}")
                else:
                    print(f"❌ TMF API '{user_input}' not found")
            else:
                # Text search
                refs = find_tmf_references_in_text(user_input)
                if refs:
                    print(f"\n🔍 Found TMF references in text: {', '.join(refs)}")
                    for tmf_code in refs:
                        result = get_tmf_api_info(tmf_code)
                        if result:
                            print(f"\n  📖 {result['tmf_code']}: {result['long_name']}")
                            print(f"     Latest: {result['highest_version']} | Docs: {result['url']}")
                else:
                    print("❌ No TMF references found in the text")
    
    else:
        # Command line mode
        for arg in sys.argv[1:]:
            result = get_tmf_api_info(arg)
            if result:
                print(f"\n✅ {arg} -> {result['long_name']}")
                print(f"   TMF Code: {result['tmf_code']}")
                print(f"   Latest Version: {result['highest_version']}")
                print(f"   Documentation: {result['url']}")
            else:
                print(f"❌ {arg} -> Not found")


if __name__ == "__main__":
    main()