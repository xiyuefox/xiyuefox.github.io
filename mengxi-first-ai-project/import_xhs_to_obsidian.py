import json, os, glob, time, requests

#========== 配置 ==========
VAULT = "/Users/hulimofaqiu/Documents/obisidian笔记文件"
XHS_DATA = "/Users/hulimofaqiu/xhs_data"
OUT_DIR = os.path.join(VAULT, "母婴准备", "新生儿采购清单")
API = "http://localhost:18060/api/v1"
os.makedirs(OUT_DIR, exist_ok=True)

#========== 1. 读取搜索结果，筛选高赞帖子 ==========
print("📖 读取搜索数据...")
all_feeds = []
for f in sorted(glob.glob(os.path.join(XHS_DATA, "search_*.json"))):
    try:
        data = json.load(open(f, encoding="utf-8"))
        feeds = data.get("data", {}).get("feeds", [])
        # 按互动量排序，取前5
        def get_score(x):
            likes = int(x.get("noteCard", {}).get("interactInfo", {}).get("likedCount", 0) or 0)
            collects = int(x.get("noteCard", {}).get("interactInfo", {}).get("collectedCount", 0) or 0)
            return likes + collects
        feeds.sort(key=get_score, reverse=True)
        top = feeds[:5]
        all_feeds.extend(top)
        print(f"  ✅ {os.path.basename(f)}: {len(feeds)}条, 取前{len(top)}条")
    except Exception as e:
        print(f"  ⚠️ {os.path.basename(f)} 读取失败: {e}")

print(f"\n📊 共筛选出 {len(all_feeds)} 篇优质帖子")

#========== 2. 获取帖子详情 ==========
print("\n🔍 获取帖子详情...")
details = []
for i, feed in enumerate(all_feeds):
    nid = feed.get("id", "")
    token = feed.get("xsecToken", "")
    title = feed.get("noteCard", {}).get("displayTitle", "无标题")
    likes = int(feed.get("noteCard", {}).get("interactInfo", {}).get("likedCount", 0) or 0)
    collects = int(feed.get("noteCard", {}).get("interactInfo", {}).get("collectedCount", 0) or 0)

    if not nid:
        continue
    try:
        r = requests.post(f"{API}/feeds/detail",
                          json={"feed_id": nid, "xsec_token": token}, timeout=15)
        d = r.json()
        if d.get("success"):
            detail = d.get("data", {})
            detail["_search_title"] = title
            detail["_search_like"] = likes
            detail["_search_collect"] = collects
            details.append(detail)
            print(f"  ✅ [{i+1}/{len(all_feeds)}] {title[:30]}")
        else:
            print(f"  ⚠️ [{i+1}] {title[:30]} - 获取失败: {d.get('msg', '未知错误')}")
    except Exception as e:
        print(f"  ❌ [{i+1}] {title[:30]} - {e}")
    time.sleep(3)

# 保存详情
json.dump(details, open(os.path.join(XHS_DATA, "all_details.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
print(f"\n💾 已保存 {len(details)} 篇详情到 all_details.json")

#========== 3. 按品类分类 ==========
print("\n📂 按品类整理...")
categories = {
    "喂养类好物": {"emoji": "🍼", "keywords": ["奶瓶","奶粉","吸奶器","消毒","温奶","奶嘴","母乳","喂养","防胀气","储奶"]},
    "穿着类好物": {"emoji": "👶", "keywords": ["衣服","连体","包被","帽子","袜子","和尚服","纱布衣","口水巾","手套","脚套","穿"]},
    "洗护类好物": {"emoji": "🛁", "keywords": ["浴盆","洗澡","护臀","面霜","沐浴","湿巾","洗衣","棉柔巾","润肤","洗护","纸巾"]},
    "寝具类好物": {"emoji": "🛏️", "keywords": ["婴儿床","床垫","睡袋","被子","枕","蚊帐","床围","床单","摇篮","睡"]},
    "医护类好物": {"emoji": "🏥", "keywords": ["体温计","指甲","脐带","棉签","退热","药","吸鼻","耳温","医","护理"]},
    "出行类好物": {"emoji": "🚗", "keywords": ["推车","安全座椅","背带","腰凳","遮阳","外出","出行","提篮"]},
    "妈妈用品":  {"emoji": "👩", "keywords": ["产褥","收腹","哺乳内衣","溢乳","卫生巾","月子","防溢","束腹","妈妈","产后","吸管"]},
}

cat_items = {k: [] for k in categories}

for d in details:
    # 处理不同的数据结构
    note = d.get("data", {}).get("note", {})
    desc = note.get("desc", "") or note.get("description", "") or d.get("_search_title", "")
    title = note.get("title", "") or d.get("title", "") or d.get("_search_title", "")
    text = (title + " " + desc).lower()
    matched = False
    for cat, info in categories.items():
        if any(kw in text for kw in info["keywords"]):
            cat_items[cat].append(d)
            matched = True
    if not matched:
        cat_items["喂养类好物"].append(d)  # 默认归类

#========== 4. 生成 Obsidian 笔记 ==========
print("\n✍️ 写入 Obsidian 笔记...")
fm = """---
tags: [母婴, 新生儿, 采购清单, 待产包]
created: 2026-02-28
source: 小红书
---

"""

# 主索引
readme = fm + "# 🍼 新生儿采购清单汇总\n\n"
readme += "> 来源：小红书高赞帖子整理 | 更新时间：2026-02-28\n\n"
readme += "## 品类导航\n\n"
readme += "| 品类 | 笔记 | 帖子数 |\n|:---|:---|:---|\n"
for cat, info in categories.items():
    readme += f"| {info['emoji']} | [[{cat}]] | {len(cat_items[cat])}篇 |\n"
readme += "\n## 参考来源\n详见 [[帖子来源索引]]\n"

with open(os.path.join(OUT_DIR, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme)
print("  ✅ README.md")

# 各品类子笔记
for cat, info in categories.items():
    content = fm + f"# {info['emoji']} {cat}\n\n"
    content += f"返回 [[README|📋 总清单]]\n\n---\n\n"
    items = cat_items[cat]
    if not items:
        content += "> 暂未从搜索结果中匹配到该品类的内容\n"
    else:
        for idx, d in enumerate(items, 1):
            title = d.get("title") or d.get("_search_title", "未知标题")
            desc = d.get("description", "") or d.get("desc", "")
            author = d.get("user", {}).get("nickname", "") if isinstance(d.get("user"), dict) else "未知"
            likes = d.get("_search_like", "?")
            collects = d.get("_search_collect", "?")

            content += f"## {idx}. {title}\n\n"
            content += f"**作者**: {author} | **👍 {likes}** | **⭐ {collects}**\n\n"
            if desc:
                content += f"{desc[:500]}\n\n"
            content += "---\n\n"

    with open(os.path.join(OUT_DIR, f"{cat}.md"), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✅ {cat}.md ({len(items)}篇)")

# 帖子来源索引
index = fm + "# 📚 帖子来源索引\n\n"
index += "返回 [[README|📋 总清单]]\n\n"
index += "| # | 标题 | 作者 | 👍 | ⭐ |\n|:---|:---|:---|:---|:---|\n"
for i, d in enumerate(details, 1):
    title = (d.get("title") or d.get("_search_title", ""))[:40]
    author = d.get("user", {}).get("nickname", "未知") if isinstance(d.get("user"), dict) else "未知"
    likes = d.get("_search_like", "?")
    collects = d.get("_search_collect", "?")
    index += f"| {i} | {title} | {author} | {likes} | {collects} |\n"

index += f"\n\n> 共计 {len(details)} 篇帖子 | 采集时间 2026-02-28\n"

with open(os.path.join(OUT_DIR, "帖子来源索引.md"), "w", encoding="utf-8") as f:
    f.write(index)
print("  ✅ 帖子来源索引.md")

print(f"\n🎉 全部完成！笔记路径：{OUT_DIR}")
print(f"📁 共生成 {len(os.listdir(OUT_DIR))} 个文件，打开 Obsidian 即可查看")
