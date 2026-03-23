import requests
import feedparser
import urllib3

# Suppress insecure warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def test_insecure():
    url = "https://www.howwemontessori.com/how-we-montessori/atom.xml"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    print(f"Testing with verify=False: {url}...")
    try:
        res = requests.get(url, headers=headers, timeout=10, verify=False)
        print(f"HTTP Status: {res.status_code}")
        if res.status_code == 200:
            feed = feedparser.parse(res.text)
            print(f"Feed Title: {getattr(feed, 'feed', {}).get('title', 'N/A')}")
            if hasattr(feed, 'entries') and feed.entries:
                print(f"✅ Found {len(feed.entries)} entries!")
                for entry in feed.entries[:2]:
                    print(f" - Title: {entry.get('title')}")
                return
            else:
                print("❌ No entries inside.")
        else:
             print("❌ Failed HTTP.")
    except Exception as e:
         print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_insecure()
