import json, os, glob, time, requests

API = "http://localhost:18060/api/v1"
SEARCH_DIR = "/Users/hulimofaqiu/xhs_data/car_search"
VAULT = "/Users/hulimofaqiu/Documents/obisidian笔记文件"
OUT_DIR = os.path.join(VAULT, "生活决策", "上海购车指南")
os.makedirs(OUT_DIR, exist_ok=True)

# ========== 1. 读取所有搜索结果 ==========
print("📖 读取所有搜索数据...")
all_feeds = []
for f in sorted(glob.glob(os.path.join(SEARCH_DIR, "search_*.json"))):
    try:
        data = json.load(open(f, encoding="utf-8"))
        feeds = data.get("data", {}).get("feeds", [])
        all_feeds.extend(feeds)
        print(f"  ✅ {os.path.basename(f)}: {len(feeds)} 条")
    except Exception as e:
        print(f"  ⚠️ {os.path.basename(f)}: {e}")

print(f"\n📊 总共 {len(all_feeds)} 条搜索结果")

# ========== 2. 去重+评分+排序 ==========
def parse_count(s):
    s = str(s) if s else "0"
    s = s.strip()
    for unit, mult in [("万", 10000), ("w", 10000), ("k", 1000)]:
        if unit in s.lower():
            try: return int(float(s.lower().replace(unit, "")) * mult)
            except: return 0
    try: return int(s)
    except: return 0

unique = {}
for f in all_feeds:
    fid = f.get("id")
    if not fid:
        continue
    nc = f.get("noteCard", {})
    interact = nc.get("interactInfo", {})
    likes = parse_count(interact.get("likedCount"))
    collects = parse_count(interact.get("collectedCount", 0))
    title = nc.get("displayTitle", "")
    score = likes + collects * 2

    if fid not in unique or score > unique[fid]["score"]:
        unique[fid] = {
            "id": fid, "title": title, "likes": likes, "collects": collects,
            "score": score, "xsecToken": f.get("xsecToken", ""), "raw": f
        }

print(f"🔄 去重后: {len(unique)} 条")

# 按分数排序
sorted_all = sorted(unique.values(), key=lambda x: x["score"], reverse=True)

# 打印 TOP 30
print("\n🏆 TOP 30:")
for i, f in enumerate(sorted_all[:30]):
    print(f"  {i+1}. [👍{f['likes']} ⭐{f['collects']}] {f['title'][:60]}")

# ========== 3. 获取详情 (TOP 25) ==========
# 先加载已有详情以避免重复请求
existing_details = []
existing_file = os.path.join(SEARCH_DIR, "car_details.json")
if os.path.exists(existing_file):
    existing_details = json.load(open(existing_file, encoding="utf-8"))
existing_ids = {d["id"] for d in existing_details}

top_feeds = sorted_all[:25]
new_details = []

print(f"\n📖 获取帖子详情 (已有 {len(existing_ids)} 条缓存)...")
for i, f in enumerate(top_feeds):
    fid = f["id"]
    if fid in existing_ids:
        print(f"  [{i+1}/25] {f['title'][:40]}... 📋缓存")
        continue
    
    token = f["xsecToken"]
    print(f"  [{i+1}/25] {f['title'][:40]}...", end=" ")
    try:
        r = requests.post(f"{API}/feeds/detail",
                         json={"feed_id": fid, "xsec_token": token}, timeout=60)
        res = r.json()
        if res.get("success"):
            note = res.get("data", {}).get("data", {}).get("note", {})
            desc = note.get("desc", "") or note.get("description", "")
            title = note.get("title", "") or f["title"]
            tags = [t.get("name", "") for t in note.get("tagList", [])]
            
            new_details.append({
                "id": fid, "title": title, "desc": desc,
                "likes": f["likes"], "collects": f["collects"],
                "score": f["score"], "tags": tags,
                "url": f"https://www.xiaohongshu.com/explore/{fid}",
            })
            print("✅")
        else:
            # 依然记录基本信息
            new_details.append({
                "id": fid, "title": f["title"], "desc": "",
                "likes": f["likes"], "collects": f["collects"],
                "score": f["score"], "tags": [],
                "url": f"https://www.xiaohongshu.com/explore/{fid}",
            })
            print("⚠️ (保留标题)")
    except Exception as e:
        new_details.append({
            "id": fid, "title": f["title"], "desc": "",
            "likes": f["likes"], "collects": f["collects"],
            "score": f["score"], "tags": [],
            "url": f"https://www.xiaohongshu.com/explore/{fid}",
        })
        print(f"❌ (保留标题)")
    time.sleep(3)

# 合并
all_details = existing_details + new_details
# 按 score 排序
all_details.sort(key=lambda x: x.get("score", 0), reverse=True)

# 保存
with open(os.path.join(SEARCH_DIR, "car_details_all.json"), "w", encoding="utf-8") as f:
    json.dump(all_details, f, ensure_ascii=False, indent=2)

print(f"\n💾 共 {len(all_details)} 条帖子详情")

# ========== 4. 分类整理 ==========
categories = {
    "上海牌照政策": {
        "emoji": "🪪",
        "keywords": ["沪牌", "牌照", "拍牌", "额度", "上牌", "绿牌", "沪C", "限行", "外牌", "临牌"]
    },
    "新能源车推荐": {
        "emoji": "🔋",
        "keywords": ["新能源", "电动", "混动", "纯电", "插混", "比亚迪", "特斯拉", "Tesla", "绿牌", "充电", "续航", "五菱", "宏光", "零跑", "哪吒", "蔚来", "小鹏", "理想", "埃安"]
    },
    "二手车避坑攻略": {
        "emoji": "🔍",
        "keywords": ["二手车", "避坑", "验车", "车况", "里程", "过户", "事故车", "泡水", "检测", "车贩", "套路"]
    },
    "高性价比车型": {
        "emoji": "💰",
        "keywords": ["性价比", "便宜", "省钱", "划算", "预算", "万以内", "万块", "穷人", "经济", "月薪", "低价", "实惠"]
    },
    "家用车体验分享": {
        "emoji": "👨‍👩‍👧",
        "keywords": ["家用", "家庭", "空间", "后排", "后备箱", "安全座椅", "带娃", "省油", "油耗", "保养", "使用感受", "真实", "提车", "用车"]
    },
}

cat_items = {k: [] for k in categories}
uncategorized = []

for d in all_details:
    text = (d.get("title", "") + " " + d.get("desc", "")).lower()
    matched = False
    for cat, info in categories.items():
        if any(kw.lower() in text for kw in info["keywords"]):
            cat_items[cat].append(d)
            matched = True
            break  # 每篇只归入一个最优类
    if not matched:
        uncategorized.append(d)

# 未分类的放入"高性价比车型"
cat_items["高性价比车型"].extend(uncategorized)

# ========== 5. 生成 Obsidian 笔记 ==========
print("\n✍️ 生成 Obsidian 笔记...")

fm = """---
tags: [生活决策, 购车, 上海, 二手车, 性价比]
created: 2026-03-04
source: 小红书
draft: false
---

"""

# 主索引
readme = fm + """# 🚗 上海城市购车指南

> 📅 整理时间：2026-03-04 | 来源：小红书高赞帖子
> 🎯 目标：普通家庭购车参考，预算有限，新车/二手车均可

## 📋 导航

"""

readme += "| 分类 | 笔记 | 帖子数 | 说明 |\n|:---|:---|:---|:---|\n"
cat_desc = {
    "上海牌照政策": "沪牌、绿牌、限行等上海特色政策",
    "新能源车推荐": "免拍牌+省油，家庭首选",
    "二手车避坑攻略": "买二手车必看的验车/选车经验",
    "高性价比车型": "各价位段值得买的车型推荐",
    "家用车体验分享": "真实车主用车感受和建议",
}

for cat, info in categories.items():
    readme += f"| {info['emoji']} | [[{cat}]] | {len(cat_items[cat])}篇 | {cat_desc.get(cat, '')} |\n"

readme += """

## 🔑 购车核心建议（综合高赞帖总结）

### 上海购车特殊考量
1. **牌照问题是第一位** - 沪牌拍卖价格高昂（约10万），新能源车免费绿牌是巨大优势
2. **限行政策** - 外省市号牌在上海有限行时段，考虑日常通勤需求
3. **新能源补贴** - 关注上海和国家最新的新能源购车补贴政策

### 预算有限的家庭建议
1. **新能源 > 燃油车**（沪牌省10万+，用电省油费）
2. **二手车**是不错的选择，但一定要做好验车功课
3. **关注保值率**，日系车保值率通常较高
4. **考虑后期成本** - 保险、保养、停车费也是重要开支

## 📚 参考来源
详见 [[帖子来源索引]]
"""

with open(os.path.join(OUT_DIR, "README.md"), "w", encoding="utf-8") as fp:
    fp.write(readme)
print("  ✅ README.md")

# 各品类笔记
for cat, info in categories.items():
    content = fm.replace("tags: [生活决策, 购车, 上海, 二手车, 性价比]",
                         f"tags: [生活决策, 购车, 上海, {cat}]")
    content += f"# {info['emoji']} {cat}\n\n"
    content += f"返回 [[README|🚗 购车指南总览]]\n\n---\n\n"
    items = cat_items[cat]
    if not items:
        content += "> 暂未从搜索结果中匹配到该品类的内容\n"
    else:
        for idx, d in enumerate(items, 1):
            title = d.get("title", "未知标题")
            desc = d.get("desc", "") or ""
            likes = d.get("likes", 0)
            collects = d.get("collects", 0)
            url = d.get("url", "")
            tags = d.get("tags", [])

            content += f"## {idx}. {title}\n\n"
            content += f"**👍 {likes}** | **⭐ {collects}** | "
            if url:
                content += f"[🔗 原帖链接]({url})\n\n"
            else:
                content += "\n\n"
            
            if desc:
                # 截取前800字，清理格式
                desc_clean = desc[:800].replace("\n\n\n", "\n\n")
                content += f"{desc_clean}\n\n"
            
            if tags:
                content += f"🏷️ 标签: {', '.join(tags[:6])}\n\n"
            
            content += "---\n\n"

    with open(os.path.join(OUT_DIR, f"{cat}.md"), "w", encoding="utf-8") as fp:
        fp.write(content)
    print(f"  ✅ {cat}.md ({len(items)}篇)")

# 帖子来源索引
index = fm + "# 📚 帖子来源索引\n\n"
index += "返回 [[README|🚗 购车指南总览]]\n\n"
index += "| # | 标题 | 👍 点赞 | ⭐ 收藏 | 链接 |\n|:---|:---|:---|:---|:---|\n"
for i, d in enumerate(all_details, 1):
    title = d.get("title", "")[:45]
    likes = d.get("likes", 0)
    collects = d.get("collects", 0)
    url = d.get("url", "")
    link = f"[查看]({url})" if url else ""
    index += f"| {i} | {title} | {likes} | {collects} | {link} |\n"

index += f"\n\n> 共计 {len(all_details)} 篇帖子 | 采集时间 2026-03-04\n"

with open(os.path.join(OUT_DIR, "帖子来源索引.md"), "w", encoding="utf-8") as fp:
    fp.write(index)
print("  ✅ 帖子来源索引.md")

print(f"\n🎉 全部完成！笔记路径：{OUT_DIR}")
print(f"📁 共生成 {len(os.listdir(OUT_DIR))} 个文件")
print("打开 Obsidian 即可查看「生活决策 → 上海购车指南」")
