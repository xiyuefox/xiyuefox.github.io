import feedparser
import requests

url = "https://www.thekavanaughreport.com/feeds/posts/default?alt=rss"
headers = { 'User-Agent': 'Mozilla/5.0' }
res = requests.get(url, headers=headers)
print("Status:", res.status_code)
feed = feedparser.parse(res.text)
if hasattr(feed, 'entries') and feed.entries:
    print("Success! Found entries:", len(feed.entries))
    for entry in feed.entries[:3]:
        print("-", entry.get('title'))
else:
    print("No entries or failure.")
