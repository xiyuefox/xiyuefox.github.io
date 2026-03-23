import requests
import json
import time
import os

API = "http://localhost:18060/api/v1"
OUTPUT_DIR = "/Users/hulimofaqiu/xhs_data/car_search"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 搜索关键词 - 覆盖上海购车、家庭用车、二手车性价比等
KEYWORDS = [
    "上海买车攻略 家庭",
    "上海购车指南 预算",
    "上海家庭用车推荐",
    "上海二手车 性价比",
    "上海买车 沪牌 省钱",
    "家用车推荐 10万以内",
    "二手车推荐 家庭 性价比",
    "上海新能源车 家庭推荐",
]

all_feeds = []

for i, kw in enumerate(KEYWORDS):
    print(f"\n🔍 [{i+1}/{len(KEYWORDS)}] 搜索: {kw}")
    try:
        r = requests.get(f"{API}/feeds/search", params={"keyword": kw}, timeout=30)
        res = r.json()
        if res.get("success"):
            feeds = res.get("data", {}).get("feeds", [])
            print(f"   ✅ 获取到 {len(feeds)} 条结果")
            # 保存原始结果
            with open(os.path.join(OUTPUT_DIR, f"search_{i+1:02d}_{kw[:10]}.json"), "w", encoding="utf-8") as f:
                json.dump(res, f, ensure_ascii=False, indent=2)
            all_feeds.extend(feeds)
        else:
            print(f"   ⚠️ 搜索失败: {res.get('message', '未知错误')}")
    except Exception as e:
        print(f"   ❌ 异常: {e}")
    time.sleep(3)

print(f"\n📊 总共获取 {len(all_feeds)} 条搜索结果")

# ========== 去重和筛选 ==========
def parse_count(count_str):
    """解析点赞/收藏数"""
    s = str(count_str) if count_str else "0"
    s = s.strip()
    if "万" in s or "w" in s.lower():
        try:
            return int(float(s.lower().replace("万", "").replace("w", "")) * 10000)
        except:
            return 0
    elif "k" in s.lower():
        try:
            return int(float(s.lower().replace("k", "")) * 1000)
        except:
            return 0
    else:
        try:
            return int(s)
        except:
            return 0

# 去重
unique = {}
for f in all_feeds:
    fid = f.get("id")
    if not fid:
        continue
    note_card = f.get("noteCard", {})
    interact = note_card.get("interactInfo", {})
    likes = parse_count(interact.get("likedCount"))
    collects = parse_count(interact.get("collectedCount", 0))
    title = note_card.get("displayTitle", "")
    
    # 计算综合分数
    score = likes + collects * 2  # 收藏权重更高（代表实用性）
    
    if fid not in unique or score > unique[fid]["score"]:
        unique[fid] = {
            "id": fid,
            "title": title,
            "likes": likes,
            "collects": collects,
            "score": score,
            "xsecToken": f.get("xsecToken", ""),
            "raw": f
        }

print(f"🔄 去重后: {len(unique)} 条")

# 按分数排序，取 TOP 20
sorted_feeds = sorted(unique.values(), key=lambda x: x["score"], reverse=True)
top_feeds = sorted_feeds[:20]

print(f"\n🏆 TOP {len(top_feeds)} 高赞/高收藏帖子:")
for i, f in enumerate(top_feeds):
    print(f"  {i+1}. [👍{f['likes']} ⭐{f['collects']}] {f['title'][:50]}")

# ========== 获取详情 ==========
print(f"\n📖 获取帖子详情...")
details = []
for i, f in enumerate(top_feeds):
    fid = f["id"]
    token = f["xsecToken"]
    print(f"  [{i+1}/{len(top_feeds)}] {f['title'][:40]}...", end=" ")
    try:
        r = requests.post(f"{API}/feeds/detail", 
                         json={"feed_id": fid, "xsec_token": token}, 
                         timeout=30)
        res = r.json()
        if res.get("success"):
            detail_data = res.get("data", {})
            note = detail_data.get("data", {}).get("note", {})
            desc = note.get("desc", "") or note.get("description", "")
            title = note.get("title", "") or f["title"]
            
            # 提取标签
            tags = []
            for tag in note.get("tagList", []):
                tags.append(tag.get("name", ""))
            
            details.append({
                "id": fid,
                "title": title,
                "desc": desc,
                "likes": f["likes"],
                "collects": f["collects"],
                "score": f["score"],
                "tags": tags,
                "url": f"https://www.xiaohongshu.com/explore/{fid}",
            })
            print("✅")
        else:
            print(f"⚠️ {res.get('message', '')}")
    except Exception as e:
        print(f"❌ {e}")
    time.sleep(3)

# 保存详情
with open(os.path.join(OUTPUT_DIR, "car_details.json"), "w", encoding="utf-8") as f:
    json.dump(details, f, ensure_ascii=False, indent=2)

print(f"\n💾 保存了 {len(details)} 条帖子详情到 {OUTPUT_DIR}/car_details.json")
print("🎉 搜索阶段完成!")
