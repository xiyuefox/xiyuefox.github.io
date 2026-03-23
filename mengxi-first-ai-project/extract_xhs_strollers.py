import requests
import json
import time

API = "http://localhost:18060/api/v1"
KEYWORDS = ["婴儿推车测评", "婴儿车避震对比", "新生儿推车推荐", "Anex推车测评", "Anex婴儿车"]

# Expected Brands
BRANDS = ["巧儿宜", "Joie", "Silver Cross", "Anex", "Cybex", "Bugaboo", "Stokke", "好孩子", "Hamilton"]

def search(keyword):
    print(f"Searching: {keyword}")
    r = requests.get(f"{API}/feeds/search", params={"keyword": keyword})
    return r.json()

def detail(feed_id, token):
    print(f"Detail: {feed_id}")
    r = requests.post(f"{API}/feeds/detail", json={"feed_id": feed_id, "xsec_token": token})
    return r.json()

all_feeds = []
for kw in KEYWORDS:
    res = search(kw)
    if res.get("success"):
        feeds = res.get("data", {}).get("feeds", [])
        all_feeds.extend(feeds)
    time.sleep(2)

print(f"Total search results: {len(all_feeds)}")

def parse_likes(likes_str):
    likes_str = str(likes_str) if likes_str else "0"
    if "w" in likes_str.lower() or "万" in likes_str.lower():
        try:
            return int(float(likes_str.lower().replace("w", "").replace("万", "")) * 10000)
        except ValueError:
            return 0
    elif "k" in likes_str.lower():
        try:
            return int(float(likes_str.lower().replace("k", "")) * 1000)
        except ValueError:
            return 0
    else:
        try:
            return int(likes_str)
        except ValueError:
            return 0

# Filter and deduplicate
unique_feeds = {}
for f in all_feeds:
    fid = f.get("id")
    if not fid: continue
    
    interact = f.get("noteCard", {}).get("interactInfo", {})
    likes = parse_likes(interact.get("likedCount"))
    if likes >= 500:
        if fid not in unique_feeds:
            unique_feeds[fid] = f

print(f"Unique high-like feeds (>500): {len(unique_feeds)}")

# Sort by likes
sorted_feeds = sorted(unique_feeds.values(), key=lambda x: parse_likes(x.get("noteCard", {}).get("interactInfo", {}).get("likedCount")), reverse=True)

# Fetch details for the top 15 posts
target_feeds = sorted_feeds[:15]
collected_data = []

for i, f in enumerate(target_feeds):
    fid = f.get("id")
    token = f.get("xsecToken")
    likes = parse_likes(f.get("noteCard", {}).get("interactInfo", {}).get("likedCount"))
    title = f.get("noteCard", {}).get("displayTitle", "")
    
    dres = detail(fid, token)
    if dres.get("success"):
        note = dres.get("data", {}).get("data", {}).get("note", {})
        desc = note.get("desc", note.get("description", ""))
        collected_data.append({
            "id": fid,
            "title": title,
            "desc": desc,
            "likes": likes,
            "url": f"https://www.xiaohongshu.com/explore/{fid}"
        })
    time.sleep(1)

with open("/Users/hulimofaqiu/mengxi-first-ai-project/xhs_stroller_data.json", "w", encoding="utf-8") as out:
    json.dump(collected_data, out, ensure_ascii=False, indent=2)

print("Saved data to xhs_stroller_data.json")
