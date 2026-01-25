import instaloader

# Create an Instaloader instance
L = instaloader.Instaloader()

# 🔑 Login required (for reels this is now almost always required)
USERNAME = "your_username"
PASSWORD = "your_password"

try:
    L.login(USERNAME, PASSWORD)  # login
    print("✅ Logged in successfully!")
except Exception as e:
    print("❌ Login failed:", e)


def download_reel(reel_url):
    try:
        shortcode = reel_url.split("/")[-2]
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        L.download_post(post, target="Reels")
        print("✅ Reel downloaded successfully!")

    except Exception as e:
        print("❌ Error:", e)


if __name__ == "__main__":
    url = input("Enter Instagram Reel URL: ")
    download_reel(url)
