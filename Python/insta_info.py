"""
Instagram Account Information Extractor - Updated Version
Extracts comprehensive profile information from Instagram accounts
"""

import instaloader
import json
from datetime import datetime
import sys
import time

class InstagramExtractor:
    def __init__(self):
        """Initialize Instaloader instance with custom settings"""
        self.loader = instaloader.Instaloader(
            quiet=False,
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            download_pictures=False,
            download_videos=False,
            download_video_thumbnails=False,
            download_geotags=False,
            download_comments=False,
            save_metadata=False,
            compress_json=False,
            max_connection_attempts=3
        )
        self.is_logged_in = False
        
    def login(self, username, password):
        """
        Login to Instagram (REQUIRED for most operations now)
        """
        try:
            print(f"🔐 Logging in as {username}...")
            self.loader.login(username, password)
            self.is_logged_in = True
            print(f"✓ Successfully logged in as {username}")
            
            # Save session for future use
            self.loader.save_session_to_file(f"session_{username}")
            print("✓ Session saved for future use")
            return True
        except instaloader.exceptions.BadCredentialsException:
            print(f"✗ Login failed: Invalid username or password")
            return False
        except instaloader.exceptions.TwoFactorAuthRequiredException:
            print(f"✗ Two-factor authentication required. Please disable 2FA temporarily or use session file.")
            return False
        except Exception as e:
            print(f"✗ Login failed: {e}")
            return False
    
    def load_session(self, username):
        """Load previously saved session"""
        try:
            self.loader.load_session_from_file(username, f"session_{username}")
            self.is_logged_in = True
            print(f"✓ Session loaded for {username}")
            return True
        except Exception as e:
            print(f"✗ Could not load session: {e}")
            return False
    
    def extract_profile_info(self, target_username):
        """
        Extract comprehensive profile information
        """
        if not self.is_logged_in:
            print("⚠ Warning: Not logged in. Some data may not be accessible.")
        
        try:
            print(f"📥 Fetching profile data for @{target_username}...")
            
            # Load profile
            profile = instaloader.Profile.from_username(
                self.loader.context, 
                target_username
            )
            
            # Compile profile data
            profile_data = {
                'basic_info': {
                    'username': profile.username,
                    'full_name': profile.full_name,
                    'user_id': profile.userid,
                    'biography': profile.biography,
                    'external_url': profile.external_url,
                    'is_verified': profile.is_verified,
                    'is_private': profile.is_private,
                    'is_business_account': profile.is_business_account,
                },
                'statistics': {
                    'followers': profile.followers,
                    'following': profile.followees,
                    'total_posts': profile.mediacount,
                },
                'profile_media': {
                    'profile_pic_url': profile.profile_pic_url,
                    'has_profile_pic': profile.has_profile_pic,
                    'has_public_story': profile.has_public_story,
                    'has_viewable_story': profile.has_viewable_story,
                },
                'business_info': {
                    'business_category': profile.business_category_name if profile.is_business_account else None,
                },
                'additional_info': {
                    'is_followed_by_viewer': profile.followed_by_viewer if self.is_logged_in else None,
                    'follows_viewer': profile.follows_viewer if self.is_logged_in else None,
                }
            }
            
            print("✓ Profile data extracted successfully!")
            return profile_data
            
        except instaloader.exceptions.ProfileNotExistsException:
            print(f"✗ Profile '@{target_username}' does not exist")
            return None
        except instaloader.exceptions.PrivateProfileNotFollowedException:
            print(f"✗ Profile '@{target_username}' is private and you don't follow it")
            return None
        except instaloader.exceptions.LoginRequiredException:
            print(f"✗ Login required to access this profile. Please login first.")
            return None
        except Exception as e:
            print(f"✗ Error extracting profile: {e}")
            return None
    
    def get_recent_posts(self, target_username, max_posts=12):
        """
        Extract information from recent posts
        """
        try:
            print(f"📸 Fetching recent posts (max {max_posts})...")
            
            profile = instaloader.Profile.from_username(
                self.loader.context, 
                target_username
            )
            
            if profile.is_private and not profile.followed_by_viewer:
                print("⚠ This is a private account. Cannot access posts.")
                return []
            
            posts_data = []
            for idx, post in enumerate(profile.get_posts()):
                if idx >= max_posts:
                    break
                
                try:
                    post_info = {
                        'post_number': idx + 1,
                        'shortcode': post.shortcode,
                        'url': f"https://www.instagram.com/p/{post.shortcode}/",
                        'caption': post.caption[:200] + '...' if post.caption and len(post.caption) > 200 else post.caption,
                        'likes': post.likes,
                        'comments': post.comments,
                        'date': post.date.isoformat(),
                        'is_video': post.is_video,
                        'video_views': post.video_view_count if post.is_video else None,
                        'tagged_users': [user.username for user in post.tagged_users],
                        'location': post.location.name if post.location else None,
                    }
                    posts_data.append(post_info)
                    print(f"  ✓ Post {idx + 1}/{max_posts} extracted")
                    time.sleep(1)  # Rate limiting
                except Exception as e:
                    print(f"  ✗ Error on post {idx + 1}: {e}")
                    continue
            
            print(f"✓ Extracted {len(posts_data)} posts successfully!")
            return posts_data
            
        except Exception as e:
            print(f"✗ Error extracting posts: {e}")
            return []
    
    def get_followers_list(self, target_username, max_followers=50):
        """
        Get list of followers (requires login)
        """
        if not self.is_logged_in:
            print("✗ Login required to fetch followers list")
            return []
        
        try:
            print(f"👥 Fetching followers (max {max_followers})...")
            profile = instaloader.Profile.from_username(
                self.loader.context, 
                target_username
            )
            
            followers = []
            for idx, follower in enumerate(profile.get_followers()):
                if idx >= max_followers:
                    break
                followers.append({
                    'username': follower.username,
                    'full_name': follower.full_name,
                    'is_verified': follower.is_verified
                })
                if (idx + 1) % 10 == 0:
                    print(f"  ✓ {idx + 1} followers fetched...")
                time.sleep(2)  # Rate limiting
            
            print(f"✓ Extracted {len(followers)} followers")
            return followers
            
        except Exception as e:
            print(f"✗ Error extracting followers: {e}")
            return []
    
    def get_following_list(self, target_username, max_following=50):
        """
        Get list of accounts being followed (requires login)
        """
        if not self.is_logged_in:
            print("✗ Login required to fetch following list")
            return []
        
        try:
            print(f"👤 Fetching following (max {max_following})...")
            profile = instaloader.Profile.from_username(
                self.loader.context, 
                target_username
            )
            
            following = []
            for idx, followee in enumerate(profile.get_followees()):
                if idx >= max_following:
                    break
                following.append({
                    'username': followee.username,
                    'full_name': followee.full_name,
                    'is_verified': followee.is_verified
                })
                if (idx + 1) % 10 == 0:
                    print(f"  ✓ {idx + 1} following fetched...")
                time.sleep(2)  # Rate limiting
            
            print(f"✓ Extracted {len(following)} following")
            return following
            
        except Exception as e:
            print(f"✗ Error extracting following list: {e}")
            return []
    
    def save_to_json(self, data, filename):
        """Save extracted data to JSON file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"✓ Data saved to {filename}")
            return True
        except Exception as e:
            print(f"✗ Error saving file: {e}")
            return False


# Usage Example
if __name__ == "__main__":
    # Initialize extractor
    extractor = InstagramExtractor()
    
    # Get target account from user input
    print("\n" + "="*60)
    print("     Instagram Account Information Extractor")
    print("="*60)
    
    # Check for saved session
    use_session = input("\nDo you have a saved session? (y/n): ").strip().lower()
    if use_session == 'y':
        session_user = input("Enter your Instagram username for saved session: ").strip()
        if not extractor.load_session(session_user):
            print("\nSession not found. Please login.")
            username = input("Enter your Instagram username: ").strip()
            password = input("Enter your Instagram password: ").strip()
            if not extractor.login(username, password):
                print("\n✗ Cannot proceed without login. Exiting...")
                sys.exit(1)
    else:
        login_choice = input("\nLogin to Instagram? (HIGHLY RECOMMENDED) (y/n): ").strip().lower()
        if login_choice == 'y':
            username = input("Enter your Instagram username: ").strip()
            password = input("Enter your Instagram password: ").strip()
            if not extractor.login(username, password):
                print("\n⚠ Continuing without login (limited data available)...")
        else:
            print("\n⚠ Warning: Without login, most features won't work due to Instagram restrictions")
    
    target_account = input("\nEnter the Instagram username to extract: ").strip()
    
    if not target_account:
        print("✗ Error: Username cannot be empty")
        sys.exit(1)
    
    # Remove @ symbol if user included it
    target_account = target_account.lstrip('@')
    
    print(f"\n{'='*60}")
    print(f"  Extracting information for: @{target_account}")
    print(f"{'='*60}\n")
    
    # Extract profile information
    print("📊 STEP 1: Extracting profile information...")
    print("-" * 60)
    profile_info = extractor.extract_profile_info(target_account)
    
    if profile_info:
        print(f"\n✓ Profile Summary:")
        print(f"  • Username: @{profile_info['basic_info']['username']}")
        print(f"  • Full Name: {profile_info['basic_info']['full_name']}")
        print(f"  • Followers: {profile_info['statistics']['followers']:,}")
        print(f"  • Following: {profile_info['statistics']['following']:,}")
        print(f"  • Posts: {profile_info['statistics']['total_posts']:,}")
        print(f"  • Verified: {'✓ Yes' if profile_info['basic_info']['is_verified'] else '✗ No'}")
        print(f"  • Private: {'✓ Yes' if profile_info['basic_info']['is_private'] else '✗ No'}")
        print(f"  • Business: {'✓ Yes' if profile_info['basic_info']['is_business_account'] else '✗ No'}")
    
    # Extract recent posts
    print(f"\n📷 STEP 2: Extracting recent posts...")
    print("-" * 60)
    recent_posts = extractor.get_recent_posts(target_account, max_posts=12)
    
    # Ask for followers/following
    if extractor.is_logged_in:
        get_followers = input("\nDo you want to extract followers list? (y/n): ").strip().lower()
        followers_list = []
        if get_followers == 'y':
            max_f = input("How many followers to extract? (max 100, recommended 50): ").strip()
            max_f = int(max_f) if max_f.isdigit() else 50
            followers_list = extractor.get_followers_list(target_account, max_followers=max_f)
        
        get_following = input("\nDo you want to extract following list? (y/n): ").strip().lower()
        following_list = []
        if get_following == 'y':
            max_f = input("How many following to extract? (max 100, recommended 50): ").strip()
            max_f = int(max_f) if max_f.isdigit() else 50
            following_list = extractor.get_following_list(target_account, max_following=max_f)
    else:
        followers_list = []
        following_list = []
    
    # Combine all data
    all_data = {
        'profile': profile_info,
        'recent_posts': recent_posts,
        'followers': followers_list,
        'following': following_list,
        'extraction_date': datetime.now().isoformat(),
        'extracted_by': 'Instagram Account Info Extractor'
    }
    
    # Save to JSON
    print(f"\n💾 STEP 3: Saving data...")
    print("-" * 60)
    filename = f"{target_account}_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    extractor.save_to_json(all_data, filename)
    
    print(f"\n{'='*60}")
    print("✓ EXTRACTION COMPLETE!")
    print(f"{'='*60}")
    print(f"\n📁 Data saved to: {filename}")
    print(f"📊 Profile extracted: {'✓' if profile_info else '✗'}")
    print(f"📷 Posts extracted: {len(recent_posts)}")
    print(f"👥 Followers extracted: {len(followers_list)}")
    print(f"👤 Following extracted: {len(following_list)}")
    print(f"\n{'='*60}\n")