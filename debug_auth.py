#!/usr/bin/env python3
"""
Debug script to test JIRA authentication step by step
"""

import asyncio
import requests
import json
from login import JiraLoginBot
from jira_api import JiraApiClient


async def debug_authentication():
    """Debug the authentication process step by step"""
    print("🔍 JIRA Authentication Debug")
    print("=" * 50)
    
    # Step 1: Test fresh login
    print("\n1️⃣ Testing fresh login (force refresh)...")
    try:
        login_bot = JiraLoginBot(headless=False)
        cookies = await login_bot.get_cookies(force_refresh=True)
        
        if cookies:
            print(f"✅ Got {len(cookies)} cookies from fresh login")
            
            # Show important cookies
            for name, value in cookies.items():
                if any(keyword in name.lower() for keyword in ['session', 'jsession', 'auth', 'token']):
                    print(f"   🔑 {name}: {value[:20]}...")
        else:
            print("❌ No cookies received from login")
            return False
            
    except Exception as e:
        print(f"❌ Fresh login failed: {str(e)}")
        return False
    
    # Step 2: Test API call with fresh cookies
    print("\n2️⃣ Testing API call with fresh cookies...")
    try:
        session = requests.Session()
        
        # Set up proxy if needed
        import os
        http_proxy = os.getenv('HTTP_PROXY')
        if http_proxy:
            session.proxies = {'http': http_proxy, 'https': http_proxy}
            print(f"   🌐 Using proxy: {http_proxy}")
        
        # Add cookies to session
        for name, value in cookies.items():
            session.cookies.set(name, value)
        
        # Add headers that might be required
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        
        # Add XSRF token if available
        for cookie_name, cookie_value in cookies.items():
            if 'xsrf' in cookie_name.lower() or 'csrf' in cookie_name.lower():
                if '_' in cookie_value:
                    xsrf_token = cookie_value.split('_')[0]
                else:
                    xsrf_token = cookie_value
                headers['X-Atlassian-Token'] = 'no-check'
                headers['X-XSRF-TOKEN'] = xsrf_token
                print(f"   🔑 Using XSRF token: {xsrf_token[:20]}...")
                break
        
        # Test different API endpoints
        test_urls = [
            "https://projects.tmforum.org/jira/rest/api/2/myself",
            "https://projects.tmforum.org/jira/rest/api/latest/myself", 
            "https://projects.tmforum.org/jira/rest/auth/latest/session",
            "https://projects.tmforum.org/jira/secure/Dashboard.jspa"  # Try a regular page first
        ]
        
        for i, api_url in enumerate(test_urls, 1):
            print(f"   📡 Test {i}: {api_url}")
            
            try:
                response = session.get(api_url, headers=headers, timeout=30)
                print(f"      📊 Status: {response.status_code}")
                
                if response.status_code == 200:
                    if 'json' in response.headers.get('content-type', '').lower():
                        try:
                            data = response.json()
                            if 'displayName' in data:
                                print(f"      ✅ Success! User: {data.get('displayName', 'Unknown')}")
                                return True
                            else:
                                print(f"      ✅ Success! Response: {str(data)[:100]}...")
                        except:
                            print(f"      ✅ Success! Non-JSON response: {response.text[:100]}...")
                    else:
                        print(f"      ✅ Success! HTML response (length: {len(response.text)})")
                        # For HTML responses, check if we can see logged-in content
                        if 'dashboard' in response.text.lower() or 'logout' in response.text.lower():
                            print("      🎉 Appears to be logged in (found dashboard/logout)")
                            
                elif response.status_code == 401:
                    print(f"      ❌ Unauthorized: {response.text[:100]}...")
                else:
                    print(f"      ⚠️  Other status: {response.text[:100]}...")
                    
            except Exception as e:
                print(f"      ❌ Request failed: {str(e)}")
                
            print()  # Empty line for readability
            
        return False
            
    except Exception as e:
        print(f"❌ API test failed: {str(e)}")
        return False
    
    # Step 3: Test with JiraApiClient
    print("\n3️⃣ Testing with JiraApiClient...")
    try:
        client = JiraApiClient()
        success = await client.authenticate(force_refresh=True)
        
        if success:
            print("   ✅ JiraApiClient authentication successful!")
            
            # Try a simple API call
            user_info = client.get_user_info()
            if user_info:
                print(f"   👤 User info retrieved: {user_info.get('displayName')}")
            
        else:
            print("   ❌ JiraApiClient authentication failed")
            
        return success
        
    except Exception as e:
        print(f"❌ JiraApiClient test failed: {str(e)}")
        return False


async def main():
    """Main debug function"""
    try:
        success = await debug_authentication()
        
        if success:
            print("\n" + "=" * 50)
            print("🎉 All authentication tests passed!")
            print("You can now run example.py successfully")
        else:
            print("\n" + "=" * 50)
            print("❌ Authentication tests failed")
            print("Please check the errors above and fix the issues")
            
    except KeyboardInterrupt:
        print("\n\n⏹️  Debug interrupted by user")
    except Exception as e:
        print(f"\n❌ Debug failed: {str(e)}")


if __name__ == "__main__":
    asyncio.run(main())