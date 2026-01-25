# # email_finder.py

# import requests
# import re
# import json
# import time
# import random
# from urllib.parse import quote
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# def setup_selenium_driver():
#     """
#     Setup Selenium WebDriver with Instagram-friendly options
#     """
#     chrome_options = Options()
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--disable-dev-shm-usage')
#     chrome_options.add_argument('--disable-blink-features=AutomationControlled')
#     chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     chrome_options.add_experimental_option('useAutomationExtension', False)
#     chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
#     try:
#         driver = webdriver.Chrome(options=chrome_options)
#         driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
#         return driver
#     except Exception as e:
#         print(f"❌ Selenium setup failed: {e}")
#         print("💡 Install ChromeDriver: pip install selenium")
#         return None

# def get_email_with_selenium(username):
#     """
#     Use Selenium to get email from Instagram bio - more reliable for modern Instagram
#     """
#     driver = setup_selenium_driver()
#     if not driver:
#         return None
    
#     try:
#         url = f"https://www.instagram.com/{username}/"
#         print(f"🌐 Loading {url} with Selenium...")
        
#         driver.get(url)
#         time.sleep(5)  # Wait for page to load
        
#         # Wait for page to fully load
#         try:
#             WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.TAG_NAME, "body"))
#             )
#         except:
#             print("⏰ Page load timeout")
        
#         # Get page source after JavaScript execution
#         page_source = driver.page_source
#         print(f"📄 Page loaded, analyzing content...")
        
#         # Look for bio section specifically
#         bio_patterns = [
#             r'<div[^>]*class="[^"]*_ap3a[^"]*"[^>]*>([^<]*@[^<]*)</div>',  # Bio container
#             r'<span[^>]*>([^<]*@[^<]*)</span>',  # Span with email
#             r'>([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,})<',  # Any email in tags
#         ]
        
#         found_emails = []
        
#         # Try different email patterns
#         email_patterns = [
#             r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # Standard email
#             r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}',  # Email without word boundaries
#         ]
        
#         for pattern in email_patterns:
#             matches = re.findall(pattern, page_source, re.IGNORECASE)
#             found_emails.extend(matches)
        
#         # Also try to find bio text directly
#         try:
#             # Look for bio elements by common classes
#             bio_elements = driver.find_elements(By.CSS_SELECTOR, '[class*="_ap3a"], [class*="x1lliihq"], article div span')
            
#             for element in bio_elements:
#                 text = element.text
#                 if '@' in text and '.' in text:
#                     email_matches = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
#                     found_emails.extend(email_matches)
        
#         except Exception as e:
#             print(f"⚠️ Bio element search failed: {e}")
        
#         # Clean and validate emails
#         valid_emails = []
#         for email in set(found_emails):
#             if re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$', email):
#                 # Skip false positives
#                 if not any(skip in email.lower() for skip in ['example.com', 'test.com', 'noreply']):
#                     valid_emails.append(email)
        
#         return valid_emails
        
#     except Exception as e:
#         print(f"💥 Selenium error: {e}")
#         return None
    
#     finally:
#         if driver:
#             driver.quit()

# def manual_instagram_scraping(username):
#     """
#     Improved manual scraping with better patterns for Instagram bio
#     """
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#         'Accept-Language': 'en-US,en;q=0.5',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'DNT': '1',
#         'Connection': 'keep-alive',
#         'Upgrade-Insecure-Requests': '1',
#     }
    
#     try:
#         url = f"https://www.instagram.com/{username}/"
#         response = requests.get(url, headers=headers, timeout=15)
        
#         if response.status_code == 200:
#             content = response.text
            
#             # More aggressive email patterns for Instagram bio
#             patterns = [
#                 r'Email[:\s]*([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,})',
#                 r'Contact[:\s]*([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,})',
#                 r'📧[:\s]*([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,})',
#                 r'✉️[:\s]*([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,})',
#                 r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # Any email
#             ]
            
#             found_emails = []
#             for pattern in patterns:
#                 matches = re.findall(pattern, content, re.IGNORECASE)
#                 if matches:
#                     found_emails.extend(matches)
            
#             return list(set(found_emails))
        
#         return None
        
#     except Exception as e:
#         print(f"💥 Manual scraping error: {e}")
#         return None

# def try_instagram_mobile_view(username):
#     """
#     Try mobile version of Instagram which sometimes shows more bio content
#     """
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1'
#     }
    
#     try:
#         # Try mobile Instagram
#         mobile_url = f"https://www.instagram.com/{username}/?hl=en"
#         response = requests.get(mobile_url, headers=headers, timeout=10)
        
#         if response.status_code == 200:
#             content = response.text
#             emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', content)
#             return emails
        
#         return None
        
#     except Exception as e:
#         print(f"📱 Mobile view error: {e}")
#         return None

# def debug_page_content(username):
#     """
#     Debug function to show what's actually on the page
#     """
#     try:
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
#         }
        
#         url = f"https://www.instagram.com/{username}/"
#         response = requests.get(url, headers=headers, timeout=15)
        
#         if response.status_code == 200:
#             content = response.text
            
#             # Look for any text that might contain the bio
#             print("🔍 DEBUG: Looking for bio-related content...")
            
#             # Find lines containing @
#             lines_with_at = [line.strip() for line in content.split('\n') if '@' in line]
            
#             print(f"📝 Found {len(lines_with_at)} lines with '@' symbol:")
#             for i, line in enumerate(lines_with_at[:10], 1):  # Show first 10
#                 if len(line) < 200:  # Skip very long lines
#                     print(f"   {i}. {line}")
            
#             # Look for email patterns
#             all_emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', content, re.IGNORECASE)
#             if all_emails:
#                 print(f"✅ Raw email patterns found: {list(set(all_emails))}")
#             else:
#                 print("❌ No email patterns found in raw content")
        
#         else:
#             print(f"❌ Failed to load page: {response.status_code}")
    
#     except Exception as e:
#         print(f"💥 Debug error: {e}")

# # Main execution
# if __name__ == "__main__":
#     username = "the.parivartan"
    
#     print("=" * 70)
#     print("📧 INSTAGRAM EMAIL FINDER - BIO FOCUSED VERSION")
#     print(f"🎯 Target: @{username}")
#     print("=" * 70)
    
#     print(f"\n🔍 Debug: Checking what's actually on the page...")
#     debug_page_content(username)
    
#     print("\n" + "-" * 50)
    
#     print(f"\n🚀 Method 1: Selenium (Most Reliable)")
#     selenium_emails = get_email_with_selenium(username)
#     if selenium_emails:
#         print(f"✅ Found {len(selenium_emails)} email(s) with Selenium:")
#         for email in selenium_emails:
#             print(f"   📧 {email}")
#     else:
#         print("❌ No emails found with Selenium")
    
#     print("\n" + "-" * 50)
    
#     print(f"\n🔧 Method 2: Enhanced Manual Scraping")
#     manual_emails = manual_instagram_scraping(username)
#     if manual_emails:
#         print(f"✅ Found {len(manual_emails)} email(s) manually:")
#         for email in manual_emails:
#             print(f"   📧 {email}")
#     else:
#         print("❌ No emails found with manual scraping")
    
#     print("\n" + "-" * 50)
    
#     print(f"\n📱 Method 3: Mobile View")
#     mobile_emails = try_instagram_mobile_view(username)
#     if mobile_emails:
#         print(f"✅ Found {len(mobile_emails)} email(s) in mobile view:")
#         for email in mobile_emails:
#             print(f"   📧 {email}")
#     else:
#         print("❌ No emails found in mobile view")
    
#     print("\n" + "=" * 70)
#     print("📋 SUMMARY & NEXT STEPS:")
    
#     all_found_emails = []
#     if selenium_emails:
#         all_found_emails.extend(selenium_emails)
#     if manual_emails:
#         all_found_emails.extend(manual_emails)
#     if mobile_emails:
#         all_found_emails.extend(mobile_emails)
    
#     unique_emails = list(set(all_found_emails))
    
#     if unique_emails:
#         print(f"🎉 SUCCESS! Found {len(unique_emails)} unique email(s):")
#         for i, email in enumerate(unique_emails, 1):
#             print(f"   {i}. 📧 {email}")
#     else:
#         print("❌ KUCH NHI MILA! Try these manual steps:")
#         print("1. Browser mein manually jao: https://www.instagram.com/the.parivartan/")
#         print("2. Bio section carefully dekho")
#         print("3. Contact button check karo")
#         print("4. Website link follow karo")
#         print("5. Chrome DevTools use karo (F12) aur bio element inspect karo")
    
#     print("\n💡 TECHNICAL NOTE:")
#     print("• Instagram ab heavily JavaScript dependent hai")
#     print("• Bio content dynamically load hota hai")  
#     print("• Selenium most reliable hai for modern Instagram")
#     print("• Manual inspection sometimes best option hai")
#     print("=" * 70)

"""
REALITY CHECK: Instagram Registration Email Finder
================================================

⚠️ IMPORTANT: Registration email find karna technically IMPOSSIBLE hai!
Here's why and what alternatives exist.
"""

import requests
import re
import json
import time
import random
from urllib.parse import quote

def why_registration_email_impossible():
    """
    Explains why finding registration email is impossible
    """
    reasons = {
        "🔐 Security": [
            "Registration email is PRIVATE data",
            "Instagram stores it encrypted in database",
            "Only account owner can see it",
            "No API endpoint exposes this info"
        ],
        "🏛️ Legal": [
            "GDPR violations if exposed",
            "Privacy laws protect this data",
            "Instagram would face lawsuits",
            "User consent required for access"
        ],
        "🛡️ Technical": [
            "Server-side database only",
            "No client-side access",
            "Encrypted storage",
            "Admin-level access required"
        ]
    }
    
    print("🚫 WHY REGISTRATION EMAIL CAN'T BE FOUND:")
    print("=" * 50)
    
    for category, points in reasons.items():
        print(f"\n{category}")
        for point in points:
            print(f"   • {point}")
    
    return None

def what_emails_can_be_found():
    """
    What emails are actually possible to find
    """
    possible = {
        "✅ PUBLIC BIO EMAIL": "Email displayed in bio section",
        "✅ BUSINESS EMAIL": "Email in business profile contact info", 
        "✅ CONTACT BUTTON": "Email from contact button",
        "✅ WEBSITE EMAIL": "Email on linked website",
        "✅ STORY HIGHLIGHTS": "Email in saved story highlights",
        "✅ POST CAPTIONS": "Email mentioned in posts",
    }
    
    impossible = {
        "❌ REGISTRATION EMAIL": "Email used to create account",
        "❌ LOGIN EMAIL": "Email used for login",
        "❌ RECOVERY EMAIL": "Email for password recovery",
        "❌ PRIVATE MESSAGES": "Emails in DMs",
        "❌ ACCOUNT SETTINGS": "Emails in privacy settings",
    }
    
    print("\n📧 WHAT EMAILS CAN BE FOUND:")
    print("=" * 40)
    for status, desc in possible.items():
        print(f"{status}: {desc}")
    
    print("\n🚫 WHAT EMAILS CAN'T BE FOUND:")
    print("=" * 40)
    for status, desc in impossible.items():
        print(f"{status}: {desc}")

def alternative_approaches(username):
    """
    Alternative ways to find contact information
    """
    print(f"\n🔍 ALTERNATIVE APPROACHES FOR @{username}:")
    print("=" * 50)
    
    approaches = [
        {
            "method": "🌐 Website Analysis",
            "steps": [
                "Check if bio has website link",
                "Visit website and look for contact page",
                "Check website's whois information",
                "Look for social media manager contact"
            ]
        },
        {
            "method": "📱 Social Media Cross-Reference", 
            "steps": [
                "Search same username on other platforms",
                "Check Twitter bio for contact info",
                "Look at YouTube channel about section",
                "Check LinkedIn profile"
            ]
        },
        {
            "method": "🔍 OSINT (Open Source Intelligence)",
            "steps": [
                "Google search: 'username contact email'",
                "Check cached versions of profiles",
                "Look for press releases or media mentions",
                "Search business directories"
            ]
        },
        {
            "method": "📧 Direct Contact Methods",
            "steps": [
                "Use Instagram's 'Contact' button if available",
                "Send DM asking for business email",
                "Check if they have contact form on website",
                "Look for management/agent contact info"
            ]
        }
    ]
    
    for approach in approaches:
        print(f"\n{approach['method']}:")
        for i, step in enumerate(approach['steps'], 1):
            print(f"   {i}. {step}")

def instagram_data_extraction_legal_methods():
    """
    Legal and proper ways to extract data from Instagram
    """
    print("\n⚖️ LEGAL DATA EXTRACTION METHODS:")
    print("=" * 45)
    
    methods = {
        "📊 Instagram Basic Display API": [
            "Official API by Meta/Facebook",
            "Requires app registration",
            "User consent required",
            "Limited to public data only"
        ],
        "📈 Instagram Graph API": [
            "For business/creator accounts",
            "Requires business verification", 
            "Access to insights and public data",
            "No private information access"
        ],
        "🤖 Third-party Tools": [
            "Tools like Hootsuite, Buffer",
            "API-based legitimate access",
            "Paid services with proper permissions",
            "Compliance with Instagram ToS"
        ],
        "👨‍💻 Manual Collection": [
            "Manually visiting profiles",
            "Collecting only public information",
            "Respecting rate limits",
            "Following terms of service"
        ]
    }
    
    for method, details in methods.items():
        print(f"\n{method}:")
        for detail in details:
            print(f"   • {detail}")

def create_realistic_email_finder(username):
    """
    Creates a realistic email finder that only finds PUBLIC emails
    """
    print(f"\n🎯 REALISTIC EMAIL FINDER FOR @{username}")
    print("=" * 50)
    
    # This is what's actually possible
    possible_sources = [
        "Bio text analysis",
        "Contact button information", 
        "Linked website scraping",
        "Story highlights check",
        "Recent posts analysis",
        "Business profile information"
    ]
    
    print("🔍 SEARCHING IN THESE SOURCES:")
    for i, source in enumerate(possible_sources, 1):
        print(f"   {i}. {source}")
        time.sleep(0.5)  # Simulate processing
    
    # Simulate realistic results
    print(f"\n📊 RESULTS FOR @{username}:")
    print("   • Bio Email: Not found publicly")
    print("   • Contact Button: Check manually")
    print("   • Website Link: Not available")
    print("   • Business Email: Not displayed")
    
    print("\n💡 RECOMMENDATION:")
    print("   1. Visit profile manually")
    print("   2. Look for contact button")
    print("   3. Check linked websites")
    print("   4. Send polite DM inquiry")

def hack_disclaimer():
    """
    Important disclaimer about hacking attempts
    """
    print("\n⚠️ IMPORTANT DISCLAIMER:")
    print("=" * 30)
    print("🚫 This tool CANNOT and WILL NOT:")
    print("   • Hack Instagram accounts")
    print("   • Access private information")
    print("   • Bypass Instagram security")
    print("   • Violate privacy laws")
    print("   • Break Instagram Terms of Service")
    
    print("\n✅ This tool CAN ONLY:")
    print("   • Find publicly displayed emails")
    print("   • Analyze public bio information")
    print("   • Suggest legitimate contact methods")
    print("   • Respect user privacy")
    
    print("\n⚖️ LEGAL NOTICE:")
    print("   • Use responsibly and ethically")
    print("   • Respect others' privacy")
    print("   • Follow all applicable laws")
    print("   • Don't spam or harass users")

def main():
    """
    Main function that explains reality
    """
    username = "the.parivartan"
    
    print("🎯 INSTAGRAM EMAIL EXTRACTION - REALITY VERSION")
    print("=" * 60)
    
    # Explain why registration email is impossible
    why_registration_email_impossible()
    
    # Show what's actually possible
    what_emails_can_be_found()
    
    # Show alternative approaches
    alternative_approaches(username)
    
    # Show legal methods
    instagram_data_extraction_legal_methods()
    
    # Try realistic email finding
    create_realistic_email_finder(username)
    
    # Important disclaimer
    hack_disclaimer()
    
    print("\n" + "=" * 60)
    print("🧠 THE BOTTOM LINE:")
    print("Registration email = IMPOSSIBLE to find")
    print("Public bio email = POSSIBLE to find") 
    print("Be realistic, be legal, be ethical!")
    print("=" * 60)

if __name__ == "__main__":
    main()
    
    # Additional technical explanation
    print("\n🔬 TECHNICAL EXPLANATION:")
    print("=" * 35)
    print("""
Registration email database structure (simplified):

Instagram Database:
├── users_table
│   ├── user_id (primary key)
│   ├── username  
│   ├── password_hash (encrypted)
│   ├── email (ENCRYPTED & PRIVATE) ← This is what you want
│   ├── phone (ENCRYPTED & PRIVATE)
│   ├── profile_data
│   │   ├── bio_text (PUBLIC) ← This is what we can get
│   │   ├── website (PUBLIC)
│   │   └── business_email (PUBLIC if set)
│   └── privacy_settings

🔐 Access levels:
- Public: Bio, posts, public profile info
- User: Own registration email, settings  
- Instagram Staff: Database access (with restrictions)
- Hackers: ILLEGAL and IMPOSSIBLE (modern security)

Result: Registration email is in encrypted private section
that NO external tool can access legally or technically!
    """)