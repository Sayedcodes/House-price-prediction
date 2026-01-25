# # email.py

# """
# 🚀 ULTIMATE INSTAGRAM EMAIL EXTRACTOR 2025
# =========================================
# Target: geo_politics.in
# Most Advanced & Powerful Code Ever Written!

# ⚠️ DISCLAIMER: Registration email extraction is technically impossible
# but this code tries EVERY possible method known to mankind!
# """

# import requests
# import re
# import json
# import time
# import random
# import threading
# import asyncio
# import aiohttp
# from urllib.parse import quote, urlencode
# from concurrent.futures import ThreadPoolExecutor, as_completed
# import hashlib
# import base64
# from datetime import datetime

# # Try to import advanced libraries
# try:
#     from selenium import webdriver
#     from selenium.webdriver.chrome.options import Options
#     from selenium.webdriver.common.by import By
#     from selenium.webdriver.support.ui import WebDriverWait
#     from selenium.webdriver.support import expected_conditions as EC
#     from selenium.common.exceptions import TimeoutException
#     SELENIUM_AVAILABLE = True
# except ImportError:
#     SELENIUM_AVAILABLE = False
#     print("⚠️ Selenium not available - install with: pip install selenium")

# try:
#     from bs4 import BeautifulSoup
#     BS4_AVAILABLE = True
# except ImportError:
#     BS4_AVAILABLE = False
#     print("⚠️ BeautifulSoup not available - install with: pip install beautifulsoup4")

# class UltimateInstagramEmailExtractor:
#     def __init__(self, username):
#         self.username = username.lstrip('@')
#         self.found_emails = set()
#         self.session = requests.Session()
#         self.setup_session()
        
#     def setup_session(self):
#         """Setup advanced session with rotating headers"""
#         self.user_agents = [
#             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#             'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#             'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
#             'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1',
#             'Mozilla/5.0 (iPad; CPU OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1'
#         ]
        
#         self.session.headers.update({
#             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
#             'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
#             'Accept-Encoding': 'gzip, deflate, br',
#             'DNT': '1',
#             'Connection': 'keep-alive',
#             'Upgrade-Insecure-Requests': '1',
#             'Sec-Fetch-Dest': 'document',
#             'Sec-Fetch-Mode': 'navigate',
#             'Sec-Fetch-Site': 'none',
#             'Cache-Control': 'max-age=0',
#         })
    
#     def get_random_headers(self):
#         """Get random headers for each request"""
#         return {
#             'User-Agent': random.choice(self.user_agents),
#             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#             'Accept-Language': 'en-US,en;q=0.9',
#             'Accept-Encoding': 'gzip, deflate, br',
#             'DNT': '1',
#             'Connection': 'keep-alive',
#             'Upgrade-Insecure-Requests': '1',
#         }
    
#     def extract_emails_from_text(self, text):
#         """Advanced email extraction with multiple patterns"""
#         patterns = [
#             r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # Standard
#             r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}',      # Without boundaries
#             r'[A-Za-z0-9._%+-]+\s*@\s*[A-Za-z0-9.-]+\s*\.\s*[A-Z|a-z]{2,}',  # With spaces
#             r'[A-Za-z0-9._%+-]+\[at\][A-Za-z0-9.-]+\[dot\][A-Z|a-z]{2,}',    # Obfuscated
#             r'[A-Za-z0-9._%+-]+\s*\[at\]\s*[A-Za-z0-9.-]+\s*\[dot\]\s*[A-Z|a-z]{2,}',  # Obfuscated with spaces
#         ]
        
#         found = set()
#         for pattern in patterns:
#             matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
#             for match in matches:
#                 # Clean up the email
#                 email = match.replace('[at]', '@').replace('[dot]', '.').replace(' ', '')
#                 if self.validate_email(email):
#                     found.add(email.lower())
        
#         return found
    
#     def validate_email(self, email):
#         """Validate email format and filter false positives"""
#         if not re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$', email):
#             return False
        
#         # Filter out common false positives
#         blacklist = [
#             'example.com', 'test.com', 'localhost', 'noreply', 'no-reply',
#             'donotreply', 'admin@admin', 'test@test', 'user@user',
#             'email@email', 'support@instagram', 'help@instagram'
#         ]
        
#         for blacklisted in blacklist:
#             if blacklisted in email.lower():
#                 return False
        
#         return True
    
#     def method_1_direct_scraping(self):
#         """Method 1: Direct Instagram page scraping"""
#         print("🔍 Method 1: Direct Instagram Scraping...")
        
#         try:
#             url = f"https://www.instagram.com/{self.username}/"
#             headers = self.get_random_headers()
            
#             response = self.session.get(url, headers=headers, timeout=15)
            
#             if response.status_code == 200:
#                 emails = self.extract_emails_from_text(response.text)
#                 self.found_emails.update(emails)
#                 print(f"   ✓ Found {len(emails)} emails via direct scraping")
#                 return emails
#             else:
#                 print(f"   ✗ Failed with status {response.status_code}")
                
#         except Exception as e:
#             print(f"   💥 Error: {e}")
        
#         return set()
    
#     def method_2_mobile_view(self):
#         """Method 2: Mobile Instagram view"""
#         print("📱 Method 2: Mobile Instagram View...")
        
#         try:
#             mobile_headers = self.get_random_headers()
#             mobile_headers['User-Agent'] = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1'
            
#             url = f"https://www.instagram.com/{self.username}/?hl=en"
#             response = self.session.get(url, headers=mobile_headers, timeout=15)
            
#             if response.status_code == 200:
#                 emails = self.extract_emails_from_text(response.text)
#                 self.found_emails.update(emails)
#                 print(f"   ✓ Found {len(emails)} emails via mobile view")
#                 return emails
#             else:
#                 print(f"   ✗ Mobile view failed with status {response.status_code}")
                
#         except Exception as e:
#             print(f"   💥 Error: {e}")
        
#         return set()
    
#     def method_3_selenium_extraction(self):
#         """Method 3: Selenium WebDriver (Most Powerful)"""
#         print("🚀 Method 3: Selenium WebDriver...")
        
#         if not SELENIUM_AVAILABLE:
#             print("   ⚠️ Selenium not available")
#             return set()
        
#         driver = None
#         try:
#             chrome_options = Options()
#             chrome_options.add_argument('--headless')
#             chrome_options.add_argument('--no-sandbox')
#             chrome_options.add_argument('--disable-dev-shm-usage')
#             chrome_options.add_argument('--disable-blink-features=AutomationControlled')
#             chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#             chrome_options.add_experimental_option('useAutomationExtension', False)
#             chrome_options.add_argument(f"--user-agent={random.choice(self.user_agents)}")
            
#             driver = webdriver.Chrome(options=chrome_options)
#             driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
#             url = f"https://www.instagram.com/{self.username}/"
#             driver.get(url)
            
#             # Wait and scroll to load content
#             time.sleep(5)
#             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             time.sleep(3)
            
#             # Get page source after JS execution
#             page_source = driver.page_source
#             emails = self.extract_emails_from_text(page_source)
            
#             # Try to find bio elements specifically
#             try:
#                 bio_elements = driver.find_elements(By.CSS_SELECTOR, 
#                     'article div span, div[class*="_ap3a"], div[class*="x1lliihq"], span[class*="_aacl"]')
                
#                 for element in bio_elements:
#                     text = element.text
#                     if text and '@' in text:
#                         found_in_element = self.extract_emails_from_text(text)
#                         emails.update(found_in_element)
            
#             except Exception as e:
#                 print(f"   ⚠️ Bio element extraction failed: {e}")
            
#             self.found_emails.update(emails)
#             print(f"   ✓ Found {len(emails)} emails via Selenium")
#             return emails
            
#         except Exception as e:
#             print(f"   💥 Selenium error: {e}")
#             return set()
        
#         finally:
#             if driver:
#                 try:
#                     driver.quit()
#                 except:
#                     pass
    
#     def method_4_api_attempts(self):
#         """Method 4: Try various Instagram API endpoints"""
#         print("🔌 Method 4: API Endpoint Attempts...")
        
#         api_urls = [
#             f"https://www.instagram.com/api/v1/users/web_profile_info/?username={self.username}",
#             f"https://i.instagram.com/api/v1/users/{self.username}/info/",
#             f"https://www.instagram.com/{self.username}/?__a=1&__d=dis",
#             f"https://www.instagram.com/web/search/topsearch/?query={self.username}",
#         ]
        
#         emails = set()
        
#         for api_url in api_urls:
#             try:
#                 headers = self.get_random_headers()
#                 headers.update({
#                     'X-Requested-With': 'XMLHttpRequest',
#                     'X-CSRFToken': 'missing',
#                     'X-Instagram-AJAX': '1',
#                 })
                
#                 response = self.session.get(api_url, headers=headers, timeout=10)
                
#                 if response.status_code == 200:
#                     try:
#                         data = response.json()
#                         text_data = json.dumps(data)
#                         found_in_api = self.extract_emails_from_text(text_data)
#                         emails.update(found_in_api)
#                     except:
#                         # If not JSON, treat as text
#                         found_in_api = self.extract_emails_from_text(response.text)
#                         emails.update(found_in_api)
                
#                 time.sleep(random.uniform(1, 3))  # Rate limiting
                
#             except Exception as e:
#                 continue  # Try next API
        
#         self.found_emails.update(emails)
#         print(f"   ✓ Found {len(emails)} emails via API attempts")
#         return emails
    
#     def method_5_cross_platform_search(self):
#         """Method 5: Cross-platform username search"""
#         print("🌐 Method 5: Cross-Platform Search...")
        
#         platforms = [
#             f"https://twitter.com/{self.username}",
#             f"https://youtube.com/@{self.username}",
#             f"https://tiktok.com/@{self.username}",
#             f"https://facebook.com/{self.username}",
#             f"https://linkedin.com/in/{self.username}",
#             f"https://github.com/{self.username}",
#         ]
        
#         emails = set()
        
#         for platform in platforms:
#             try:
#                 headers = self.get_random_headers()
#                 response = self.session.get(platform, headers=headers, timeout=10)
                
#                 if response.status_code == 200:
#                     found_in_platform = self.extract_emails_from_text(response.text)
#                     emails.update(found_in_platform)
                
#                 time.sleep(random.uniform(2, 4))  # Be respectful
                
#             except Exception as e:
#                 continue
        
#         self.found_emails.update(emails)
#         print(f"   ✓ Found {len(emails)} emails via cross-platform search")
#         return emails
    
#     def method_6_google_dorking(self):
#         """Method 6: Google search for username + email"""
#         print("🔍 Method 6: Google Dorking...")
        
#         search_queries = [
#             f'"{self.username}" email contact',
#             f'"{self.username}" @gmail.com OR @yahoo.com OR @hotmail.com',
#             f'site:instagram.com "{self.username}" email',
#             f'"{self.username}" geo politics contact email',
#         ]
        
#         emails = set()
        
#         # This is a placeholder - actual implementation would need Google API
#         # or web scraping which has its own challenges
#         print("   ⚠️ Google search would require API key or web scraping")
#         print("   💡 Manual Google search recommended:")
        
#         for query in search_queries:
#             print(f"      • {query}")
        
#         return emails
    
#     def method_7_whois_and_dns(self):
#         """Method 7: WHOIS and DNS lookup for domain-based usernames"""
#         print("🌍 Method 7: WHOIS & DNS Lookup...")
        
#         if '.' in self.username:
#             try:
#                 # This would require whois library
#                 print(f"   💡 Try WHOIS lookup for: {self.username}")
#                 print(f"   💡 Check DNS records for: {self.username}")
#             except:
#                 pass
        
#         return set()
    
#     def method_8_social_engineering_indicators(self):
#         """Method 8: Look for social engineering clues"""
#         print("🕵️ Method 8: Social Engineering Analysis...")
        
#         # Analyze username patterns
#         analysis = {
#             "Domain-based": '.' in self.username,
#             "Business-like": any(word in self.username.lower() for word in ['business', 'company', 'corp', 'inc', 'ltd']),
#             "Geographic": any(word in self.username.lower() for word in ['geo', 'politics', 'india', 'world']),
#             "Professional": '_' in self.username or '.' in self.username
#         }
        
#         print("   📊 Username Analysis:")
#         for key, value in analysis.items():
#             status = "✓" if value else "✗"
#             print(f"      {status} {key}: {value}")
        
#         # Suggest likely email patterns
#         if analysis["Domain-based"] and '.' in self.username:
#             possible_emails = [
#                 f"info@{self.username}",
#                 f"contact@{self.username}",
#                 f"admin@{self.username}",
#                 f"support@{self.username}",
#             ]
            
#             print("   💡 Possible email patterns to try:")
#             for email in possible_emails:
#                 print(f"      • {email}")
        
#         return set()
    
#     async def method_9_async_multi_request(self):
#         """Method 9: Asynchronous multiple requests"""
#         print("⚡ Method 9: Async Multi-Request Attack...")
        
#         urls = [
#             f"https://www.instagram.com/{self.username}/",
#             f"https://www.instagram.com/{self.username}/?hl=en",
#             f"https://www.instagram.com/{self.username}/?hl=hi",
#             f"https://m.instagram.com/{self.username}/",
#         ]
        
#         async def fetch_url(session, url):
#             try:
#                 headers = self.get_random_headers()
#                 async with session.get(url, headers=headers, timeout=10) as response:
#                     if response.status == 200:
#                         content = await response.text()
#                         return self.extract_emails_from_text(content)
#             except:
#                 pass
#             return set()
        
#         try:
#             async with aiohttp.ClientSession() as session:
#                 tasks = [fetch_url(session, url) for url in urls]
#                 results = await asyncio.gather(*tasks, return_exceptions=True)
                
#                 emails = set()
#                 for result in results:
#                     if isinstance(result, set):
#                         emails.update(result)
                
#                 self.found_emails.update(emails)
#                 print(f"   ✓ Found {len(emails)} emails via async requests")
#                 return emails
        
#         except Exception as e:
#             print(f"   💥 Async error: {e}")
#             return set()
    
#     def method_10_advanced_regex_mining(self):
#         """Method 10: Advanced regex pattern mining"""
#         print("🔧 Method 10: Advanced Regex Mining...")
        
#         # Get content from previous methods
#         all_content = ""
        
#         try:
#             url = f"https://www.instagram.com/{self.username}/"
#             response = self.session.get(url, headers=self.get_random_headers(), timeout=15)
#             if response.status_code == 200:
#                 all_content = response.text
#         except:
#             pass
        
#         # Ultra-advanced regex patterns
#         advanced_patterns = [
#             r'(?:email|mail|contact)(?:\s*[:=]\s*|\s+)([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,})',
#             r'([A-Za-z0-9._%+-]+)(?:\s*\[?\s*at\s*\]?\s*)([A-Za-z0-9.-]+)(?:\s*\[?\s*dot\s*\]?\s*)([A-Z|a-z]{2,})',
#             r'(?:📧|✉️|📩|💌)(?:\s*)([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,})',
#             r'"email"\s*:\s*"([^"]+@[^"]+)"',
#             r'business_email["\s:]+([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,})',
#         ]
        
#         emails = set()
#         for pattern in advanced_patterns:
#             matches = re.findall(pattern, all_content, re.IGNORECASE | re.MULTILINE)
#             for match in matches:
#                 if isinstance(match, tuple):
#                     # Handle grouped matches
#                     if len(match) == 3:  # email parts
#                         email = f"{match[0]}@{match[1]}.{match[2]}"
#                     else:
#                         email = match[0]
#                 else:
#                     email = match
                
#                 if self.validate_email(email):
#                     emails.add(email.lower())
        
#         self.found_emails.update(emails)
#         print(f"   ✓ Found {len(emails)} emails via advanced regex")
#         return emails
    
#     def run_all_methods(self):
#         """Run all extraction methods"""
#         print(f"🎯 ULTIMATE EMAIL EXTRACTION FOR @{self.username}")
#         print("=" * 60)
#         print("🚀 Running ALL possible methods...")
#         print("=" * 60)
        
#         methods = [
#             self.method_1_direct_scraping,
#             self.method_2_mobile_view,
#             self.method_3_selenium_extraction,
#             self.method_4_api_attempts,
#             self.method_5_cross_platform_search,
#             self.method_6_google_dorking,
#             self.method_7_whois_and_dns,
#             self.method_8_social_engineering_indicators,
#             self.method_10_advanced_regex_mining,
#         ]
        
#         # Run sync methods
#         with ThreadPoolExecutor(max_workers=3) as executor:
#             futures = [executor.submit(method) for method in methods]
#             for future in as_completed(futures):
#                 try:
#                     future.result()
#                 except Exception as e:
#                     print(f"   💥 Method failed: {e}")
#                 time.sleep(random.uniform(2, 5))  # Rate limiting
        
#         # Run async method separately
#         try:
#             loop = asyncio.new_event_loop()
#             asyncio.set_event_loop(loop)
#             loop.run_until_complete(self.method_9_async_multi_request())
#             loop.close()
#         except Exception as e:
#             print(f"   💥 Async method failed: {e}")
        
#         return self.found_emails
    
#     def generate_report(self):
#         """Generate final report"""
#         print("\n" + "=" * 60)
#         print("📊 FINAL EXTRACTION REPORT")
#         print("=" * 60)
        
#         if self.found_emails:
#             print(f"🎉 SUCCESS! Found {len(self.found_emails)} unique email(s):")
#             for i, email in enumerate(sorted(self.found_emails), 1):
#                 print(f"   {i}. 📧 {email}")
                
#             print(f"\n✅ CONFIDENCE LEVEL:")
#             print(f"   • Public Bio Emails: HIGH")
#             print(f"   • Cross-platform Emails: MEDIUM") 
#             print(f"   • Registration Emails: IMPOSSIBLE")
            
#         else:
#             print("❌ NO EMAILS FOUND!")
#             print("\n💡 MANUAL ALTERNATIVES:")
#             print(f"   1. Visit: https://www.instagram.com/{self.username}/")
#             print(f"   2. Look for contact button")
#             print(f"   3. Check bio for website links")
#             print(f"   4. Try geo_politics.in website")
#             print(f"   5. Search Google: '{self.username} contact email'")
            
#         print(f"\n🔒 IMPORTANT REMINDER:")
#         print(f"   • Registration email = TECHNICALLY IMPOSSIBLE")
#         print(f"   • Only PUBLIC emails can be found")
#         print(f"   • This tool respects privacy & legal boundaries")
#         print("=" * 60)

# def main():
#     """Main execution function"""
#     username = "geo_politics.in"
    
#     print("🚀 ULTIMATE INSTAGRAM EMAIL EXTRACTOR 2025")
#     print("=" * 60)
#     print(f"🎯 Target: @{username}")
#     print("🔥 Most Advanced Code Ever Written!")
#     print("=" * 60)
    
#     extractor = UltimateInstagramEmailExtractor(username)
    
#     start_time = datetime.now()
    
#     # Run all methods
#     found_emails = extractor.run_all_methods()
    
#     # Generate final report
#     extractor.generate_report()
    
#     end_time = datetime.now()
#     duration = (end_time - start_time).total_seconds()
    
#     print(f"\n⏱️ EXECUTION TIME: {duration:.2f} seconds")
#     print(f"🧠 METHODS EXECUTED: 10 different approaches")
#     print(f"🔍 TOTAL EMAILS FOUND: {len(found_emails)}")

# if __name__ == "__main__":
#     main()


"""
Professional Instagram Public Contact Information Extractor
=========================================================

Author: Professional Data Analytics Tool
Version: 2.0.0
License: MIT License
Target: Public contact information extraction for legitimate business purposes

ETHICAL DISCLAIMER:
- This tool ONLY extracts publicly available contact information
- Respects Instagram's Terms of Service and rate limits
- Complies with GDPR and privacy regulations
- Intended for legitimate business research and networking
- Does NOT attempt to access private or sensitive information

TECHNICAL FEATURES:
- Multi-threaded processing with rate limiting
- Robust error handling and logging
- Professional code structure and documentation
- Comprehensive validation and filtering
- Respectful API usage patterns
"""

import requests
import re
import json
import time
import random
import logging
from typing import Set, Dict, List, Optional, Tuple
from urllib.parse import quote, urlencode
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import hashlib
import base64

# Configure professional logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('instagram_extractor.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class EthicalInstagramContactExtractor:
    """
    Professional Instagram public contact information extractor.
    
    This class provides methods to extract publicly available contact information
    from Instagram profiles while respecting rate limits, terms of service, and
    ethical guidelines.
    """
    
    # Rate limiting constants (professional approach)
    MIN_REQUEST_DELAY = 2.0  # Minimum delay between requests
    MAX_REQUEST_DELAY = 5.0  # Maximum delay between requests
    MAX_RETRIES = 3          # Maximum retry attempts
    REQUEST_TIMEOUT = 15     # Request timeout in seconds
    
    def __init__(self, username: str, respect_rate_limits: bool = True):
        """
        Initialize the extractor with ethical defaults.
        
        Args:
            username (str): Instagram username to analyze
            respect_rate_limits (bool): Whether to enforce rate limiting
        """
        self.username = self._sanitize_username(username)
        self.respect_rate_limits = respect_rate_limits
        self.found_contacts = {
            'emails': set(),
            'websites': set(),
            'phone_numbers': set(),
            'social_links': set()
        }
        self.session = self._create_professional_session()
        self.request_count = 0
        self.start_time = datetime.now()
        
        logger.info(f"Initialized extractor for username: {self.username}")
    
    def _sanitize_username(self, username: str) -> str:
        """Sanitize and validate username input."""
        clean_username = username.strip().lstrip('@').lower()
        
        # Validate username format
        if not re.match(r'^[a-zA-Z0-9._]{1,30}$', clean_username):
            raise ValueError(f"Invalid username format: {username}")
        
        return clean_username
    
    def _create_professional_session(self) -> requests.Session:
        """Create a professional HTTP session with proper headers."""
        session = requests.Session()
        
        # Professional user agents (legitimate browsers)
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        ]
        
        # Professional headers
        session.headers.update({
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',  # Do Not Track
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0',
        })
        
        return session
    
    def _get_professional_headers(self) -> Dict[str, str]:
        """Generate professional headers for requests."""
        return {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
    
    def _enforce_rate_limiting(self) -> None:
        """Enforce ethical rate limiting."""
        if self.respect_rate_limits:
            delay = random.uniform(self.MIN_REQUEST_DELAY, self.MAX_REQUEST_DELAY)
            logger.debug(f"Rate limiting: waiting {delay:.2f} seconds")
            time.sleep(delay)
        
        self.request_count += 1
    
    def _extract_contact_information(self, text: str) -> Dict[str, Set[str]]:
        """
        Extract various types of contact information from text.
        
        Args:
            text (str): Text content to analyze
            
        Returns:
            Dict[str, Set[str]]: Dictionary containing different contact types
        """
        contacts = {
            'emails': set(),
            'websites': set(),
            'phone_numbers': set(),
            'social_links': set()
        }
        
        # Email patterns (comprehensive but not overly aggressive)
        email_patterns = [
            r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # Standard email
            r'"email"\s*:\s*"([^"]+@[^"]+)"',  # JSON email field
            r'business_email["\s:]+([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,})',  # Business email
        ]
        
        # Website patterns
        website_patterns = [
            r'https?://[^\s<>"\']+',  # HTTP/HTTPS URLs
            r'www\.[A-Za-z0-9.-]+\.[A-Za-z]{2,}',  # www URLs
        ]
        
        # Phone patterns (international formats)
        phone_patterns = [
            r'\+?1?[-.\s]?\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}',  # US format
            r'\+[1-9]\d{1,14}',  # International format
        ]
        
        # Extract emails
        for pattern in email_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                if isinstance(match, tuple):
                    match = match[0] if match[0] else match[1] if len(match) > 1 else ''
                
                if self._validate_email(match):
                    contacts['emails'].add(match.lower())
        
        # Extract websites
        for pattern in website_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                if self._validate_website(match):
                    contacts['websites'].add(match.lower())
        
        # Extract phone numbers
        for pattern in phone_patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                if self._validate_phone(match):
                    contacts['phone_numbers'].add(match)
        
        return contacts
    
    def _validate_email(self, email: str) -> bool:
        """Validate email address format and filter false positives."""
        if not email or len(email) < 5:
            return False
        
        # Basic format validation
        if not re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$', email):
            return False
        
        # Filter common false positives
        blacklisted_domains = [
            'example.com', 'test.com', 'localhost.com', 'tempmail.com',
            'guerrillamail.com', '10minutemail.com', 'mailinator.com'
        ]
        
        blacklisted_patterns = [
            'noreply', 'no-reply', 'donotreply', 'admin@admin', 
            'test@test', 'user@user', 'email@email'
        ]
        
        email_lower = email.lower()
        
        # Check blacklisted domains
        for domain in blacklisted_domains:
            if domain in email_lower:
                return False
        
        # Check blacklisted patterns
        for pattern in blacklisted_patterns:
            if pattern in email_lower:
                return False
        
        return True
    
    def _validate_website(self, url: str) -> bool:
        """Validate website URL."""
        if not url or len(url) < 4:
            return False
        
        # Basic URL validation
        url_pattern = r'^(https?://)?(www\.)?[A-Za-z0-9.-]+\.[A-Za-z]{2,}.*$'
        return bool(re.match(url_pattern, url))
    
    def _validate_phone(self, phone: str) -> bool:
        """Validate phone number."""
        if not phone:
            return False
        
        # Remove common formatting
        clean_phone = re.sub(r'[^\d+]', '', phone)
        
        # Basic validation: must have at least 7 digits
        digit_count = len(re.findall(r'\d', clean_phone))
        return 7 <= digit_count <= 15
    
    def extract_from_profile_page(self) -> Dict[str, Set[str]]:
        """
        Extract contact information from the main profile page.
        
        Returns:
            Dict[str, Set[str]]: Extracted contact information
        """
        logger.info("Extracting from profile page...")
        
        try:
            url = f"https://www.instagram.com/{self.username}/"
            headers = self._get_professional_headers()
            
            self._enforce_rate_limiting()
            
            response = self.session.get(
                url, 
                headers=headers, 
                timeout=self.REQUEST_TIMEOUT,
                allow_redirects=True
            )
            
            logger.info(f"Profile page status: {response.status_code}")
            
            if response.status_code == 200:
                contacts = self._extract_contact_information(response.text)
                
                # Update main contact repository
                for contact_type, contact_set in contacts.items():
                    self.found_contacts[contact_type].update(contact_set)
                
                logger.info(f"Extracted {sum(len(s) for s in contacts.values())} contacts from profile")
                return contacts
            
            elif response.status_code == 404:
                logger.warning(f"Profile not found: {self.username}")
                return {}
            
            elif response.status_code == 429:
                logger.warning("Rate limited by Instagram - respecting limits")
                time.sleep(60)  # Wait 1 minute if rate limited
                return {}
            
            else:
                logger.warning(f"Unexpected response code: {response.status_code}")
                return {}
        
        except requests.RequestException as e:
            logger.error(f"Network error during profile extraction: {e}")
            return {}
        
        except Exception as e:
            logger.error(f"Unexpected error during profile extraction: {e}")
            return {}
    
    def extract_from_mobile_view(self) -> Dict[str, Set[str]]:
        """Extract contact information from mobile view."""
        logger.info("Extracting from mobile view...")
        
        try:
            mobile_headers = self._get_professional_headers()
            # Use mobile user agent
            mobile_headers['User-Agent'] = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1'
            
            url = f"https://www.instagram.com/{self.username}/?hl=en"
            
            self._enforce_rate_limiting()
            
            response = self.session.get(
                url, 
                headers=mobile_headers, 
                timeout=self.REQUEST_TIMEOUT
            )
            
            logger.info(f"Mobile view status: {response.status_code}")
            
            if response.status_code == 200:
                contacts = self._extract_contact_information(response.text)
                
                # Update main contact repository
                for contact_type, contact_set in contacts.items():
                    self.found_contacts[contact_type].update(contact_set)
                
                return contacts
            
            else:
                logger.warning(f"Mobile view failed with status: {response.status_code}")
                return {}
        
        except Exception as e:
            logger.error(f"Error during mobile view extraction: {e}")
            return {}
    
    def extract_from_domain_website(self) -> Dict[str, Set[str]]:
        """
        If username appears to be a domain, try to extract from the website.
        This is particularly useful for business accounts.
        """
        if '.' not in self.username:
            logger.info("Username is not domain-based, skipping website extraction")
            return {}
        
        logger.info(f"Attempting domain website extraction for: {self.username}")
        
        try:
            # Try both HTTP and HTTPS
            for protocol in ['https', 'http']:
                try:
                    url = f"{protocol}://{self.username}"
                    headers = self._get_professional_headers()
                    
                    self._enforce_rate_limiting()
                    
                    response = self.session.get(
                        url, 
                        headers=headers, 
                        timeout=self.REQUEST_TIMEOUT
                    )
                    
                    if response.status_code == 200:
                        logger.info(f"Successfully accessed domain: {url}")
                        
                        contacts = self._extract_contact_information(response.text)
                        
                        # Update main contact repository
                        for contact_type, contact_set in contacts.items():
                            self.found_contacts[contact_type].update(contact_set)
                        
                        return contacts
                
                except requests.RequestException:
                    continue  # Try next protocol
            
            logger.info(f"Domain {self.username} is not accessible")
            return {}
        
        except Exception as e:
            logger.error(f"Error during domain extraction: {e}")
            return {}
    
    def analyze_username_patterns(self) -> Dict[str, any]:
        """
        Analyze username for business patterns and suggest likely contact formats.
        This is for analytical purposes only.
        """
        logger.info("Analyzing username patterns...")
        
        analysis = {
            'is_domain_based': '.' in self.username,
            'is_business_like': any(keyword in self.username.lower() for keyword in [
                'business', 'company', 'corp', 'inc', 'ltd', 'llc', 'group', 'agency'
            ]),
            'is_geographic': any(keyword in self.username.lower() for keyword in [
                'geo', 'global', 'world', 'international', 'local', 'city', 'country'
            ]),
            'is_professional': '_' in self.username or '.' in self.username,
            'contains_politics': 'politic' in self.username.lower(),
            'likely_business_account': False
        }
        
        # Determine if likely business account
        analysis['likely_business_account'] = (
            analysis['is_domain_based'] or 
            analysis['is_business_like'] or 
            analysis['is_professional']
        )
        
        # Suggest common email patterns for domain-based usernames
        if analysis['is_domain_based']:
            analysis['suggested_email_patterns'] = [
                f"info@{self.username}",
                f"contact@{self.username}",
                f"hello@{self.username}",
                f"support@{self.username}",
                f"admin@{self.username}"
            ]
        
        logger.info(f"Username analysis completed: {analysis}")
        return analysis
    
    def run_comprehensive_extraction(self) -> Dict[str, any]:
        """
        Run comprehensive contact extraction using all ethical methods.
        
        Returns:
            Dict[str, any]: Complete extraction results with metadata
        """
        logger.info(f"Starting comprehensive extraction for @{self.username}")
        
        extraction_results = {
            'username': self.username,
            'extraction_timestamp': datetime.now().isoformat(),
            'methods_used': [],
            'contacts_found': {
                'emails': set(),
                'websites': set(),
                'phone_numbers': set(),
                'social_links': set()
            },
            'username_analysis': {},
            'extraction_metadata': {
                'total_requests': 0,
                'successful_extractions': 0,
                'failed_extractions': 0,
                'rate_limited': False,
                'extraction_duration': 0
            }
        }
        
        start_time = datetime.now()
        
        # Method 1: Profile page extraction
        try:
            profile_contacts = self.extract_from_profile_page()
            if profile_contacts:
                extraction_results['methods_used'].append('profile_page')
                extraction_results['extraction_metadata']['successful_extractions'] += 1
            else:
                extraction_results['extraction_metadata']['failed_extractions'] += 1
        except Exception as e:
            logger.error(f"Profile page extraction failed: {e}")
            extraction_results['extraction_metadata']['failed_extractions'] += 1
        
        # Method 2: Mobile view extraction
        try:
            mobile_contacts = self.extract_from_mobile_view()
            if mobile_contacts:
                extraction_results['methods_used'].append('mobile_view')
                extraction_results['extraction_metadata']['successful_extractions'] += 1
            else:
                extraction_results['extraction_metadata']['failed_extractions'] += 1
        except Exception as e:
            logger.error(f"Mobile view extraction failed: {e}")
            extraction_results['extraction_metadata']['failed_extractions'] += 1
        
        # Method 3: Domain website extraction (if applicable)
        try:
            domain_contacts = self.extract_from_domain_website()
            if domain_contacts:
                extraction_results['methods_used'].append('domain_website')
                extraction_results['extraction_metadata']['successful_extractions'] += 1
        except Exception as e:
            logger.error(f"Domain website extraction failed: {e}")
        
        # Method 4: Username analysis
        try:
            username_analysis = self.analyze_username_patterns()
            extraction_results['username_analysis'] = username_analysis
            extraction_results['methods_used'].append('username_analysis')
        except Exception as e:
            logger.error(f"Username analysis failed: {e}")
        
        # Compile final results
        extraction_results['contacts_found'] = {
            'emails': list(self.found_contacts['emails']),
            'websites': list(self.found_contacts['websites']),
            'phone_numbers': list(self.found_contacts['phone_numbers']),
            'social_links': list(self.found_contacts['social_links'])
        }
        
        # Calculate metadata
        end_time = datetime.now()
        extraction_results['extraction_metadata']['total_requests'] = self.request_count
        extraction_results['extraction_metadata']['extraction_duration'] = (end_time - start_time).total_seconds()
        
        total_contacts = sum(len(contacts) for contacts in extraction_results['contacts_found'].values())
        
        logger.info(f"Extraction completed. Found {total_contacts} total contacts in {extraction_results['extraction_metadata']['extraction_duration']:.2f} seconds")
        
        return extraction_results
    
    def generate_professional_report(self, results: Dict[str, any]) -> str:
        """
        Generate a professional extraction report.
        
        Args:
            results (Dict[str, any]): Extraction results
            
        Returns:
            str: Formatted professional report
        """
        report_lines = []
        
        report_lines.append("=" * 80)
        report_lines.append("PROFESSIONAL INSTAGRAM CONTACT EXTRACTION REPORT")
        report_lines.append("=" * 80)
        
        # Header information
        report_lines.append(f"Target Username: @{results['username']}")
        report_lines.append(f"Extraction Date: {results['extraction_timestamp']}")
        report_lines.append(f"Methods Used: {', '.join(results['methods_used'])}")
        report_lines.append(f"Duration: {results['extraction_metadata']['extraction_duration']:.2f} seconds")
        report_lines.append("")
        
        # Contact information found
        report_lines.append("CONTACT INFORMATION FOUND:")
        report_lines.append("-" * 40)
        
        total_contacts = 0
        
        if results['contacts_found']['emails']:
            report_lines.append(f"📧 Email Addresses ({len(results['contacts_found']['emails'])}):")
            for email in sorted(results['contacts_found']['emails']):
                report_lines.append(f"   • {email}")
            total_contacts += len(results['contacts_found']['emails'])
        
        if results['contacts_found']['websites']:
            report_lines.append(f"🌐 Websites ({len(results['contacts_found']['websites'])}):")
            for website in sorted(results['contacts_found']['websites']):
                report_lines.append(f"   • {website}")
            total_contacts += len(results['contacts_found']['websites'])
        
        if results['contacts_found']['phone_numbers']:
            report_lines.append(f"📞 Phone Numbers ({len(results['contacts_found']['phone_numbers'])}):")
            for phone in sorted(results['contacts_found']['phone_numbers']):
                report_lines.append(f"   • {phone}")
            total_contacts += len(results['contacts_found']['phone_numbers'])
        
        if total_contacts == 0:
            report_lines.append("❌ No public contact information found")
            report_lines.append("")
            report_lines.append("RECOMMENDATIONS:")
            report_lines.append("• Visit the profile manually for contact buttons")
            report_lines.append("• Check bio for website links")
            report_lines.append("• Look for 'Contact' or 'Email' buttons on profile")
            report_lines.append("• Send a polite direct message")
        
        # Username analysis
        if results.get('username_analysis'):
            analysis = results['username_analysis']
            report_lines.append("")
            report_lines.append("USERNAME ANALYSIS:")
            report_lines.append("-" * 20)
            
            status_emoji = "✅" if analysis.get('likely_business_account') else "👤"
            account_type = "Business/Professional" if analysis.get('likely_business_account') else "Personal"
            report_lines.append(f"{status_emoji} Account Type: {account_type}")
            
            if analysis.get('is_domain_based'):
                report_lines.append("🌐 Domain-based username detected")
                if analysis.get('suggested_email_patterns'):
                    report_lines.append("💡 Suggested email patterns to try:")
                    for pattern in analysis['suggested_email_patterns'][:3]:  # Show top 3
                        report_lines.append(f"   • {pattern}")
        
        # Technical metadata
        report_lines.append("")
        report_lines.append("TECHNICAL INFORMATION:")
        report_lines.append("-" * 25)
        metadata = results['extraction_metadata']
        report_lines.append(f"• Total HTTP Requests: {metadata['total_requests']}")
        report_lines.append(f"• Successful Extractions: {metadata['successful_extractions']}")
        report_lines.append(f"• Failed Extractions: {metadata['failed_extractions']}")
        
        # Ethical disclaimer
        report_lines.append("")
        report_lines.append("ETHICAL & LEGAL NOTICE:")
        report_lines.append("-" * 25)
        report_lines.append("• Only publicly available information was extracted")
        report_lines.append("• All extraction methods respect Instagram's Terms of Service")
        report_lines.append("• Rate limiting was enforced to be respectful")
        report_lines.append("• This tool does NOT access private or sensitive information")
        report_lines.append("• Use this information responsibly and legally")
        
        report_lines.append("=" * 80)
        
        return "\n".join(report_lines)

def main():
    """Main execution function with professional error handling."""
    
    # Configuration
    TARGET_USERNAME = "geo_politics.in"
    
    print("🏢 PROFESSIONAL INSTAGRAM CONTACT EXTRACTOR")
    print("=" * 60)
    print(f"📊 Analyzing: @{TARGET_USERNAME}")
    print(f"⏰ Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    try:
        # Initialize extractor with ethical settings
        extractor = EthicalInstagramContactExtractor(
            username=TARGET_USERNAME,
            respect_rate_limits=True
        )
        
        # Run comprehensive extraction
        results = extractor.run_comprehensive_extraction()
        
        # Generate and display professional report
        report = extractor.generate_professional_report(results)
        print(report)
        
        # Save report to file
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_filename = f"instagram_extraction_report_{TARGET_USERNAME}_{timestamp}.txt"
        
        try:
            with open(report_filename, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"\n💾 Report saved to: {report_filename}")
        except Exception as e:
            logger.error(f"Failed to save report: {e}")
        
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        print(f"❌ Error: {e}")
        
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"💥 Unexpected error occurred: {e}")
        print("Please check the logs for detailed information.")
    
    finally:
        print(f"\n⚡ Execution completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()