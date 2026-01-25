import requests

url = "https://archive.org/download/kitab-ut-tawheed-1/Kitab%20Ut%20Tawheed%20%281%29.pdf"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers, timeout=30)
with open("Kitab Ut Tawheed (1).pdf", "wb") as file:
    file.write(response.content)

print("Download completed successfully!")      