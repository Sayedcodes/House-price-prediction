# # import requests
# # import re
# # import json
# # from urllib.parse import quote

# # def get_email_from_instagram_username(username):
# #     """
# #     Extract email address from Instagram username by scraping the profile page.
    
# #     Args:
# #         username (str): Instagram username without @ symbol
        
# #     Returns:
# #         str or None: Email address if found, None otherwise
# #     """
    
# #     # Clean username (remove @ if present)
# #     username = username.lstrip('@')
    
# #     # Headers to mimic a real browser
# #     headers = {
# #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
# #         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
# #         'Accept-Language': 'en-US,en;q=0.5',
# #         'Accept-Encoding': 'gzip, deflate',
# #         'Connection': 'keep-alive',
# #     }
    
# #     try:
# #         # Instagram profile URL
# #         url = f"https://www.instagram.com/{username}/"
        
# #         # Make request to Instagram profile
# #         response = requests.get(url, headers=headers, timeout=10)
        
# #         if response.status_code != 200:
# #             print(f"Error: Could not access profile. Status code: {response.status_code}")
# #             return None
            
# #         html_content = response.text
        
# #         # Method 1: Look for email in the biography/contact info
# #         # Instagram sometimes displays email in the bio or contact button
# #         email_patterns = [
# #             r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # Standard email regex
# #             r'"email":"([^"]+)"',  # JSON format
# #             r"'email':'([^']+)'",  # JSON format with single quotes
# #         ]
        
# #         found_emails = []
        
# #         for pattern in email_patterns:
# #             matches = re.findall(pattern, html_content)
# #             found_emails.extend(matches)
        
# #         # Method 2: Try to extract from JSON data embedded in the page
# #         try:
# #             # Look for JSON data in script tags
# #             json_match = re.search(r'window\._sharedData\s*=\s*({.+?});', html_content)
# #             if json_match:
# #                 json_data = json.loads(json_match.group(1))
                
# #                 # Navigate through the JSON structure to find email
# #                 entry_data = json_data.get('entry_data', {})
# #                 profile_page = entry_data.get('ProfilePage', [])
                
# #                 if profile_page:
# #                     user_data = profile_page[0].get('graphql', {}).get('user', {})
# #                     business_email = user_data.get('business_email')
# #                     if business_email:
# #                         found_emails.append(business_email)
        
# #         except (json.JSONDecodeError, KeyError, IndexError):
# #             pass
        
# #         # Remove duplicates and filter valid emails
# #         unique_emails = list(set(found_emails))
# #         valid_emails = []
        
# #         for email in unique_emails:
# #             # Validate email format
# #             if re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$', email):
# #                 valid_emails.append(email)
        
# #         if valid_emails:
# #             return valid_emails[0]  # Return the first valid email found
# #         else:
# #             return None
            
# #     except requests.RequestException as e:
# #         print(f"Network error: {e}")
# #         return None
# #     except Exception as e:
# #         print(f"Unexpected error: {e}")
# #         return None

# # def get_multiple_emails_from_instagram(username):
# #     """
# #     Get all email addresses found on an Instagram profile.
    
# #     Args:
# #         username (str): Instagram username without @ symbol
        
# #     Returns:
# #         list: List of email addresses found
# #     """
# #     username = username.lstrip('@')
    
# #     headers = {
# #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
# #     }
    
# #     try:
# #         url = f"https://www.instagram.com/{username}/"
# #         response = requests.get(url, headers=headers, timeout=10)
        
# #         if response.status_code != 200:
# #             print(f"Error: Could not access profile. Status code: {response.status_code}")
# #             return []
            
# #         html_content = response.text
        
# #         # Find all email addresses in the content
# #         email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# #         found_emails = re.findall(email_pattern, html_content)
        
# #         # Remove duplicates and validate
# #         unique_emails = []
# #         for email in set(found_emails):
# #             if re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$', email):
# #                 unique_emails.append(email)
        
# #         return unique_emails
        
# #     except Exception as e:
# #         print(f"Error: {e}")
# #         return []

# # def validate_instagram_username(username):
# #     """
# #     Validate if the username format is correct for Instagram.
    
# #     Args:
# #         username (str): Username to validate
        
# #     Returns:
# #         bool: True if valid format, False otherwise
# #     """
# #     username = username.lstrip('@')
    
# #     # Instagram username rules: 
# #     # - 1-30 characters
# #     # - Only letters, numbers, periods, and underscores
# #     # - Cannot end with a period
# #     # - Cannot have two periods in a row
    
# #     if len(username) < 1 or len(username) > 30:
# #         return False
    
# #     if not re.match(r'^[a-zA-Z0-9._]+$', username):
# #         return False
    
# #     if username.endswith('.'):
# #         return False
    
# #     if '..' in username:
# #         return False
    
# #     return True

# # def search_email_with_retry(username, max_retries=3):
# #     """
# #     Search for email with retry mechanism.
    
# #     Args:
# #         username (str): Instagram username
# #         max_retries (int): Maximum number of retry attempts
        
# #     Returns:
# #         str or None: Email address if found
# #     """
# #     if not validate_instagram_username(username):
# #         print("Invalid Instagram username format.")
# #         return None
    
# #     for attempt in range(max_retries):
# #         print(f"Attempt {attempt + 1}/{max_retries}")
        
# #         email = get_email_from_instagram_username(username)
# #         if email:
# #             return email
        
# #         if attempt < max_retries - 1:
# #             print("Retrying...")
# #             import time
# #             time.sleep(2)  # Wait 2 seconds before retry
    
# #     return None

# # # Main execution - Target: Cristiano Ronaldo's Instagram
# # if __name__ == "__main__":
# #     # Target Instagram username: Cristiano Ronaldo
# #     username = "the.parivartan"
    
# #     print("=" * 50)
# #     print(f"INSTAGRAM EMAIL EXTRACTOR")
# #     print(f"Target: @{username} (Cristiano Ronaldo)")
# #     print("=" * 50)
    
# #     # Validate username first
# #     if validate_instagram_username(username):
# #         print(f"✓ Username '{username}' is valid")
# #     else:
# #         print(f"✗ Username '{username}' is invalid")
# #         exit()
    
# #     print(f"\nSearching for email address...")
    
# #     # Method 1: Get single email
# #     print("\n--- Method 1: Single Email Search ---")
# #     email = get_email_from_instagram_username(username)
# #     if email:
# #         print(f"✓ Found email: {email}")
# #     else:
# #         print("✗ No email address found.")
    
# #     # Method 2: Get all emails found
# #     print("\n--- Method 2: Multiple Emails Search ---")
# #     all_emails = get_multiple_emails_from_instagram(username)
# #     if all_emails:
# #         print(f"✓ All emails found:")
# #         for i, email in enumerate(all_emails, 1):
# #             print(f"   {i}. {email}")
# #     else:
# #         print("✗ No email addresses found.")
    
# #     # Method 3: Search with retry
# #     print("\n--- Method 3: Search with Retry ---")
# #     email_retry = search_email_with_retry(username, max_retries=2)
# #     if email_retry:
# #         print(f"✓ Found email with retry: {email_retry}")
# #     else:
# #         print("✗ No email found even with retries.")
    
# #     print("\n" + "=" * 50)
# #     print("SEARCH COMPLETED")
# #     print("=" * 50)
    
# #     # Additional note for Cristiano's profile
# #     print(f"\nNote: @{username} is a high-profile celebrity account.")
# #     print("Email addresses are typically not publicly displayed")
# #     print("for privacy and security reasons.")



# import requests
# import re
# import json
# import time
# from urllib.parse import quote
# import random

# def get_instagram_email_advanced(username):
#     """
#     Advanced Instagram email extraction with multiple strategies.
#     """
#     username = username.lstrip('@')
    
#     # Multiple User-Agent strings to rotate
#     user_agents = [
#         'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#         'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#         'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
#     ]
    
#     headers = {
#         'User-Agent': random.choice(user_agents),
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
#         'Accept-Language': 'en-US,en;q=0.9',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'DNT': '1',
#         'Connection': 'keep-alive',
#         'Upgrade-Insecure-Requests': '1',
#         'Sec-Fetch-Dest': 'document',
#         'Sec-Fetch-Mode': 'navigate',
#         'Sec-Fetch-Site': 'none',
#         'Cache-Control': 'max-age=0',
#     }
    
#     session = requests.Session()
#     session.headers.update(headers)
    
#     try:
#         print(f"🔍 Attempting to access @{username}...")
        
#         # Method 1: Direct profile access
#         url = f"https://www.instagram.com/{username}/"
        
#         # Add random delay
#         time.sleep(random.uniform(1, 3))
        
#         response = session.get(url, timeout=15)
        
#         print(f"📡 Response status: {response.status_code}")
        
#         if response.status_code == 200:
#             html_content = response.text
#             print(f"📄 Page loaded successfully ({len(html_content)} characters)")
            
#             # Look for various email patterns
#             email_patterns = [
#                 r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # Standard email
#                 r'"email":"([^"]+)"',  # JSON format
#                 r"'email':'([^']+)'",  # Single quotes
#                 r'email["\']?\s*[:=]\s*["\']?([^"\'<>\s]+@[^"\'<>\s]+)',  # Various formats
#             ]
            
#             found_emails = []
            
#             for pattern in email_patterns:
#                 matches = re.findall(pattern, html_content, re.IGNORECASE)
#                 if isinstance(matches[0], tuple) if matches else False:
#                     matches = [match[0] if isinstance(match, tuple) else match for match in matches]
#                 found_emails.extend(matches)
            
#             # Check for business contact info
#             business_patterns = [
#                 r'"business_email":"([^"]+)"',
#                 r'"public_email":"([^"]+)"',
#                 r'"contact_phone_number":"([^"]+)"',
#             ]
            
#             for pattern in business_patterns:
#                 matches = re.findall(pattern, html_content)
#                 found_emails.extend(matches)
            
#             # Look for structured data
#             if 'application/ld+json' in html_content:
#                 print("📋 Found structured data, analyzing...")
#                 json_ld_matches = re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', html_content, re.DOTALL)
#                 for json_str in json_ld_matches:
#                     try:
#                         data = json.loads(json_str)
#                         # Look for email in structured data
#                         if isinstance(data, dict) and 'email' in str(data).lower():
#                             email_match = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', str(data))
#                             found_emails.extend(email_match)
#                     except:
#                         pass
            
#             # Filter and validate emails
#             valid_emails = []
#             for email in set(found_emails):
#                 if re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$', email):
#                     # Skip common false positives
#                     if not any(skip in email.lower() for skip in ['noreply', 'no-reply', 'donotreply', 'example.com']):
#                         valid_emails.append(email)
            
#             return valid_emails
        
#         elif response.status_code == 429:
#             print("⚠️ Rate limited by Instagram")
#             return None
#         elif response.status_code == 404:
#             print("❌ Profile not found")
#             return None
#         else:
#             print(f"❌ Unexpected status code: {response.status_code}")
#             return None
            
#     except requests.RequestException as e:
#         print(f"🌐 Network error: {e}")
#         return None
#     except Exception as e:
#         print(f"💥 Unexpected error: {e}")
#         return None

# def try_instagram_api_approach(username):
#     """
#     Attempt to use Instagram's basic display API approach (requires setup).
#     This is a placeholder showing the proper way to access Instagram data.
#     """
#     print("📱 API Approach:")
#     print("To properly access Instagram data, you should:")
#     print("1. Register as a Facebook Developer")
#     print("2. Create an Instagram Basic Display App")
#     print("3. Get proper access tokens")
#     print("4. Use official Instagram API endpoints")
#     print("5. Follow Instagram's terms of service")
    
#     # This would be the proper approach but requires API setup
#     return None

# def alternative_methods(username):
#     """
#     Suggest alternative methods to find contact information.
#     """
#     print("🔄 Alternative Methods to Find Contact Info:")
#     print(f"1. Visit https://www.instagram.com/{username}/ directly in browser")
#     print("2. Look for 'Contact' button on profile")
#     print("3. Check bio for website links")
#     print("4. Look for business category information")
#     print("5. Check if there's a 'Contact' or 'Email' button")
#     print("6. Look at recent posts for contact information")
#     print("7. Check Instagram Stories highlights")
#     print("8. Look for linked website in bio")

# def search_related_platforms(username):
#     """
#     Search for the same username on other platforms that might have public email.
#     """
#     platforms = [
#         f"https://twitter.com/{username}",
#         f"https://youtube.com/@{username}",
#         f"https://tiktok.com/@{username}",
#         f"https://facebook.com/{username}",
#         f"https://linkedin.com/in/{username}",
#     ]
    
#     print("🔗 Try checking these platforms for contact info:")
#     for platform in platforms:
#         print(f"   • {platform}")

# # Main execution
# if __name__ == "__main__":
#     username = "the.parivartan"  
    
#     print("=" * 60)
#     print("📧 INSTAGRAM EMAIL FINDER - ADVANCED VERSION")
#     print(f"🎯 Target: @{username}")
#     print("=" * 60)
    
#     # Try advanced scraping
#     print("\n🚀 Method 1: Advanced Scraping")
#     emails = get_instagram_email_advanced(username)
    
#     if emails:
#         print(f"✅ Found {len(emails)} email(s):")
#         for i, email in enumerate(emails, 1):
#             print(f"   {i}. {email}")
#     else:
#         print("❌ No emails found via scraping")
    
#     print("\n" + "-" * 40)
    
#     # Show API approach
#     print("\n🔧 Method 2: Official API (Recommended)")
#     try_instagram_api_approach(username)
    
#     print("\n" + "-" * 40)
    
#     # Show alternative methods
#     print("\n💡 Method 3: Manual Alternatives")
#     alternative_methods(username)
    
#     print("\n" + "-" * 40)
    
#     # Show related platforms
#     print("\n🌐 Method 4: Check Other Platforms")
#     search_related_platforms(username)
    
#     print("\n" + "=" * 60)
#     print("📝 IMPORTANT NOTES:")
#     print("• Instagram heavily restricts automated access")
#     print("• Celebrity accounts rarely show public emails")
#     print("• For business inquiries, use official channels")
#     print("• Consider using Instagram's official API")
#     print("• Always respect privacy and terms of service")
#     print("=" * 60)

#     # Reality check for Cristiano specifically
#     if username.lower() == "the.parivartan":
#         print("\n⭐ CRISTIANO RONALDO SPECIFIC INFO:")
#         print("• Business inquiries: Through his management team")
#         print("• Official website: cristianoronaldo.com")
#         print("• Brand partnerships: Through Jorge Mendes (agent)")
#         print("• Media: Through Manchester United or Portugal FA")
#         print("• His profile likely has NO public email for security")


import requests
import re
import json
import time
from urllib.parse import quote
import random

def get_instagram_email_advanced(username):
    """
    Advanced Instagram email extraction with multiple strategies.
    """
    username = username.lstrip('@')
    
    # Multiple User-Agent strings to rotate
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
    ]
    
    headers = {
        'User-Agent': random.choice(user_agents),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Cache-Control': 'max-age=0',
    }
    
    session = requests.Session()
    session.headers.update(headers)
    
    try:
        print(f"🔍 Attempting to access @{username}...")
        
        # Method 1: Direct profile access
        url = f"https://www.instagram.com/{username}/"
        
        # Add random delay
        time.sleep(random.uniform(1, 3))
        
        response = session.get(url, timeout=15)
        
        print(f"📡 Response status: {response.status_code}")
        
        if response.status_code == 200:
            html_content = response.text
            print(f"📄 Page loaded successfully ({len(html_content)} characters)")
            
            # Look for various email patterns
            email_patterns = [
                r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # Standard email
                r'"email":"([^"]+)"',  # JSON format
                r"'email':'([^']+)'",  # Single quotes
                r'email["\']?\s*[:=]\s*["\']?([^"\'<>\s]+@[^"\'<>\s]+)',  # Various formats
            ]
            
            found_emails = []
            
            for pattern in email_patterns:
                matches = re.findall(pattern, html_content, re.IGNORECASE)
                if isinstance(matches[0], tuple) if matches else False:
                    matches = [match[0] if isinstance(match, tuple) else match for match in matches]
                found_emails.extend(matches)
            
            # Check for business contact info
            business_patterns = [
                r'"business_email":"([^"]+)"',
                r'"public_email":"([^"]+)"',
                r'"contact_phone_number":"([^"]+)"',
            ]
            
            for pattern in business_patterns:
                matches = re.findall(pattern, html_content)
                found_emails.extend(matches)
            
            # Look for structured data
            if 'application/ld+json' in html_content:
                print("📋 Found structured data, analyzing...")
                json_ld_matches = re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', html_content, re.DOTALL)
                for json_str in json_ld_matches:
                    try:
                        data = json.loads(json_str)
                        # Look for email in structured data
                        if isinstance(data, dict) and 'email' in str(data).lower():
                            email_match = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', str(data))
                            found_emails.extend(email_match)
                    except:
                        pass
            
            # Filter and validate emails
            valid_emails = []
            for email in set(found_emails):
                if re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$', email):
                    # Skip common false positives
                    if not any(skip in email.lower() for skip in ['noreply', 'no-reply', 'donotreply', 'example.com']):
                        valid_emails.append(email)
            
            return valid_emails
        
        elif response.status_code == 429:
            print("⚠️ Rate limited by Instagram")
            return None
        elif response.status_code == 404:
            print("❌ Profile not found")
            return None
        else:
            print(f"❌ Unexpected status code: {response.status_code}")
            return None
            
    except requests.RequestException as e:
        print(f"🌐 Network error: {e}")
        return None
    except Exception as e:
        print(f"💥 Unexpected error: {e}")
        return None

def try_instagram_api_approach(username):
    """
    Attempt to use Instagram's basic display API approach (requires setup).
    This is a placeholder showing the proper way to access Instagram data.
    """
    print("📱 API Approach:")
    print("To properly access Instagram data, you should:")
    print("1. Register as a Facebook Developer")
    print("2. Create an Instagram Basic Display App")
    print("3. Get proper access tokens")
    print("4. Use official Instagram API endpoints")
    print("5. Follow Instagram's terms of service")
    
    # This would be the proper approach but requires API setup
    return None

def alternative_methods(username):
    """
    Suggest alternative methods to find contact information.
    """
    print("🔄 Alternative Methods to Find Contact Info:")
    print(f"1. Visit https://www.instagram.com/{username}/ directly in browser")
    print("2. Look for 'Contact' button on profile")
    print("3. Check bio for website links")
    print("4. Look for business category information")
    print("5. Check if there's a 'Contact' or 'Email' button")
    print("6. Look at recent posts for contact information")
    print("7. Check Instagram Stories highlights")
    print("8. Look for linked website in bio")

def search_related_platforms(username):
    """
    Search for the same username on other platforms that might have public email.
    """
    platforms = [
        f"https://twitter.com/{username}",
        f"https://youtube.com/@{username}",
        f"https://tiktok.com/@{username}",
        f"https://facebook.com/{username}",
        f"https://linkedin.com/in/{username}",
    ]
    
    print("🔗 Try checking these platforms for contact info:")
    for platform in platforms:
        print(f"   • {platform}")

# Main execution
if __name__ == "__main__":
    username = "the.parivartan"
    
    print("=" * 60)
    print("📧 INSTAGRAM EMAIL FINDER - ADVANCED VERSION")
    print(f"🎯 Target: @{username}")
    print("=" * 60)
    
    # Try advanced scraping
    print("\n🚀 Method 1: Advanced Scraping")
    emails = get_instagram_email_advanced(username)
    
    if emails:
        print(f"✅ Found {len(emails)} email(s):")
        for i, email in enumerate(emails, 1):
            print(f"   {i}. {email}")
    else:
        print("❌ No emails found via scraping")
    
    print("\n" + "-" * 40)
    
    # Show API approach
    print("\n🔧 Method 2: Official API (Recommended)")
    try_instagram_api_approach(username)
    
    print("\n" + "-" * 40)
    
    # Show alternative methods
    print("\n💡 Method 3: Manual Alternatives")
    alternative_methods(username)
    
    print("\n" + "-" * 40)
    
    # Show related platforms
    print("\n🌐 Method 4: Check Other Platforms")
    search_related_platforms(username)
    
    print("\n" + "=" * 60)
    print("📝 IMPORTANT NOTES:")
    print("• Instagram heavily restricts automated access")
    print("• Celebrity accounts rarely show public emails")
    print("• For business inquiries, use official channels")
    print("• Consider using Instagram's official API")
    print("• Always respect privacy and terms of service")
    print("=" * 60)

    # Reality check for the.parivartan specifically
    if username.lower() == "the.parivartan":
        print("\n⭐ THE.PARIVARTAN SPECIFIC INFO:")
        print("• Appears to be a smaller/personal account")
        print("• More likely to have public contact info")
        print("• Check bio for website or business info")
        print("• May have contact button if it's a business account")
        print("• Success rate higher for non-celebrity accounts")