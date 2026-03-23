import feedparser

def test():
    # Try typical RSS URLs for TypePad/Blogger
    urls = [
        "https://www.howwemontessori.com/how-we-montessori/atom.xml",
        "https://www.howwemontessori.com/how-we-montessori/index.rdf"
    ]
    for url in urls:
        print(f"Testing {url}...")
        try:
            feed = feedparser.parse(url)
            print(f"Status: {getattr(feed, 'status', 'N/A')}")
            if hasattr(feed, 'entries') and feed.entries:
                print(f"✅ Found {len(feed.entries)} entries!")
                for entry in feed.entries[:2]:
                    print(f" - Title: {entry.get('title')}")
                    print(f" - Link: {entry.get('link')}")
                return
            else:
                print("❌ No entries found.")
        except Exception as e:
            print(f"❌ Error parsing {url}: {e}")

if __name__ == "__main__":
        test()
