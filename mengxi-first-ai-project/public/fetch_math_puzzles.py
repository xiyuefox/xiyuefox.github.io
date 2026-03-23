#!/usr/bin/env python3
import urllib.request
import urllib.error
import urllib.parse
import json
import os
import datetime
import time

# ----------------- OPTIONAL DEPENDENCIES -----------------
try:
    import feedparser
except ImportError:
    print("[Warning] feedparser is not installed. RSS engine will be skipped.")
    feedparser = None

# ---------------- CONFIGURATION ----------------
MCP_BASE_URL = "http://localhost:18060"
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_PATH = os.path.join(PROJECT_DIR, "posts", "md", "math-puzzles-feed.md")

# Load environment variables from .env if it exists
env_path = os.path.join(PROJECT_DIR, ".env")
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                try:
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value.replace('"', '').replace("'", "")
                except ValueError:
                    pass

KEYWORDS = [
    "硬核 逻辑谜题", 
    "儿童奥数思维训练", 
    "离散数学 趣味题",
    "Smart Games 经典玩法"
]

RSS_FEEDS = [
    "http://www.matrix67.com/blog/feed",
    "https://mathwithbaddrawings.com/feed/",
    "https://www.quantamagazine.org/mathematics/feed/"
]

MAX_POSTS_PER_KEYWORD = 3
MAX_RSS_ENTRIES_PER_FEED = 3

# ----------------- UTILS & API CALLS -----------------

def call_mcp_api(endpoint, method="GET", body=None):
    url = f"{MCP_BASE_URL}{endpoint}"
    req = urllib.request.Request(url)
    req.method = method
    req.add_header('Content-Type', 'application/json')
    req.add_header('User-Agent', 'Mozilla/5.0')
    
    data = None
    if body:
        data = json.dumps(body).encode('utf-8')
        
    try:
        with urllib.request.urlopen(req, data=data, timeout=15) as response:
            return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"[MCP Error] ({url}): {e}")
        return None

def call_gemini_summarize(text_content):
    import requests
    import hashlib
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return text_content[:200]
        
    # ---- 基础缓存逻辑 ----
    cache_dir = os.path.join(PROJECT_DIR, "data")
    os.makedirs(cache_dir, exist_ok=True)
    cache_path = os.path.join(cache_dir, "gemini_cache.json")
    cache = {}
    if os.path.exists(cache_path):
        try:
            with open(cache_path, 'r', encoding='utf-8') as f:
                cache = json.load(f)
        except: pass
        
    text_hash = hashlib.md5(text_content.encode('utf-8')).hexdigest()
    if text_hash in cache:
        print("   ✅ [Cache Hit]")
        return cache[text_hash]
        
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
        headers = {'Content-Type': 'application/json'}
        prompt = f"""你现在是一位乐观的 ‘Socratic (苏格拉底式) 数学导师’（借鉴沃顿商学院 General Tutor 主动学习理念）。
请对这段内容进行**中英对照级引导式提炼**，特别针对数学解谜、奥数、Smart Games 益智桌游，重点在于启发读者自主思考并理清玩法。

处理规则：
1. **📌 核心概览 (Overview)**：用一句话中英双语极简概括背景或矛盾，格式：`[中文] | [English]`，拒绝标题党。
2. **🧠 概念锚点 (Anchor)**：点出谜题背后考核的数学思想（如：抽屉原理、图论、拓扑、递归等），格式：`[中文] | [English]`。
3. **🎮 详细玩法/核心规则 (Detailed Rules)**：基于原文提炼 **2~3 条分步式核心玩法或判定逻辑**。必须严格使用 **中英对照** 列表分开。
4. **🪜 思考脚手架 (Scaffolding)**：绝不直接给答案！提炼 2 个【渐进式提示】：第一级提示给发散切入点；第二级提示给硬核破局点（无需双语，以英文或中文写明即可，主要看原文主要语言环境）。
5. **🔒 隐藏机关 (Details)**：如果原文存在解析过程，放置在 `<details><summary>💡 揭晓谜底与解析</summary> ... </details>` 标签内。

输出格式要求：
- 📌 **核心概览 (Overview)**：[中文] | [English]
- 🧠 **概念锚点 (Anchor)**：[中文] | [English]
- 🎮 **详细玩法 (Detailed Rules)**：
  - 🇨🇳 **中文规则**: [1. ... 2. ...]
  - 🇬🇧 **English Rules**: [1. ... 2. ...]
- 🪜 **思考脚手架 (Hints)**：
  - 🔸 **Hint 1**：[发散提示]
  - 🔸 **Hint 2**：[定量破局提示]
- <details><summary>💡 揭晓谜底与解析 (Answer)</summary>
[如果有答案，写在这里]
</details>

待解析内容:
{text_content}"""
        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        res = requests.post(url, headers=headers, json=payload, timeout=12)
        if res.status_code == 200:
            data = res.json()
            parts = data.get('candidates', [{}])[0].get('content', {}).get('parts', [])
            if parts:
                summary = parts[0].get('text', '').strip()
                # 写入缓存
                cache[text_hash] = summary
                try:
                    with open(cache_path, 'w', encoding='utf-8') as f:
                        json.dump(cache, f, ensure_ascii=False, indent=2)
                except: pass
                return summary
    except Exception as e:
        print(f"   ⚠️ Gemini 摘要异常: {e}")
    return text_content[:200] + "..."

def run_xhs_engine():
    print("\n--- 🌟 引擎 A: 小红书 MCP 正在检索 ---")
    cards_md = []
    seen_ids = set()
    
    for kw in KEYWORDS:
        print(f"🔍 正在检索关键词: 【{kw}】")
        res = call_mcp_api(f"/api/v1/feeds/search?keyword={urllib.parse.quote(kw)}")
        if not res or not res.get("success"):
            print(f"   检索失败: {kw}")
            continue
            
        feeds = res.get("data", {}).get("feeds", [])
        kw_nodes_count = 0
        
        for feed in feeds:
            if kw_nodes_count >= MAX_POSTS_PER_KEYWORD:
                break
                
            if feed.get("modelType") != "note":
                continue
                
            note_id = feed.get("id")
            if note_id in seen_ids:
                continue
                
            note_card = feed.get("noteCard", {})
            title = note_card.get("displayTitle", "") or "未命名解谜"
            xsec_token = feed.get("xsecToken")
            
            print(f"👉 正在详情拉取 [{title[:15]}...] (ID: {note_id})")
            detail_res = call_mcp_api("/api/v1/feeds/detail", method="POST", body={"feed_id": note_id, "feedId": note_id, "xsec_token": xsec_token})
            
            if not detail_res or not detail_res.get("success"):
                continue
                
            note = detail_res.get("data", {}).get("data", {}).get("note", {})
            desc = note.get("desc", "")
            if not desc:
                continue
                
            collected = note.get("interactInfo", {}).get("collectedCount", "0")
            
            print(f"🧠 Ark 逻辑提炼中...")
            summary = call_gemini_summarize(desc)
            time.sleep(1)
            
            url_real = f"https://www.xiaohongshu.com/explore/{note_id}"
            
            md_card = f"""
### 🧩 [{title}]({url_real})
**🔍 益智看板**: 🌟 {collected} 收藏 | 🏷️ {kw}

> **🤖 逻辑提炼 (Logic Breakdown)：**
{summary.strip()}

<details>
<summary>📂 查看原帖文本</summary>

{desc.strip()}

</details>

---
"""
            cards_md.append(md_card)
            seen_ids.add(note_id)
            kw_nodes_count += 1
            
    return cards_md

def run_rss_engine():
    print("\n--- 🌟 引擎 B: RSS 订阅 正在检索 ---")
    cards_md = []
    
    if not feedparser:
        return cards_md
        
    for url in RSS_FEEDS:
        print(f"📡 正在拉取 RSS: {url}")
        try:
            feed = feedparser.parse(url)
            if hasattr(feed, 'status') and feed.status != 200:
                print(f"   HTTP 异常: {feed.status}")
                continue
                
            author = feed.feed.title if hasattr(feed.feed, 'title') else "未知博客"
            cards_md.append(f"\n## 📡 来源: {author}\n")
            entries_count = 0
            
            for entry in feed.entries:
                if entries_count >= MAX_RSS_ENTRIES_PER_FEED:
                    break
                    
                title = entry.get("title", "未命名文章")
                link = entry.get("link", "#")
                summary_text = entry.get("summary", entry.get("description", ""))
                clean_content = summary_text.replace("<p>", "").replace("</p>", "\n")
                
                print(f"👉 详情拉取 [{title[:15]}...]")
                print(f"🧠 Ark 逻辑提炼中...")
                summary = call_gemini_summarize(clean_content)
                time.sleep(1)
                
                truncated_raw = clean_content[:300] + "..." if len(clean_content) > 300 else clean_content
                
                md_card = f"""
### 🧩 [{title}]({link})
**🧠 思维矩阵**: 🛰️ 来源: {author}

> **🤖 逻辑解析 (Logic Breakdown)：**
{summary.strip()}

<details>
<summary>📂 查看原贴数据</summary>

{truncated_raw.strip()}

</details>

---
"""
                cards_md.append(md_card)
                entries_count += 1
        except Exception as e:
            print(f"[RSS Error] ({url}): {e}")
            continue
            
    return cards_md

def main():
    print("=== 🌟 开始拉取数学解谜与益智内容 ===")
    
    xhs_cards = []  # run_xhs_engine()
    rss_cards = run_rss_engine()
    
    all_notecards_md = xhs_cards + rss_cards
    if not all_notecards_md:
        all_notecards_md = ["\n> 🧩 当前暂无最新解谜记录，稍后重试。\n"]

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    final_output = f"""---
title: "🧮 趣味数学解谜与逻辑思维"
date: {today}
tags: ["math", "puzzles", "logic"]
category: "obsidian"
badge: "数学逻辑"
---

这里汇集了关于 **数学思维、逻辑推理、奥数益智** 的硬核干货。自动提炼核心线索，供各位玩家挑战脑力。

---

{''.join(all_notecards_md)}
"""

    os.makedirs(os.path.dirname(MD_PATH), exist_ok=True)
    with open(MD_PATH, 'w', encoding='utf-8') as f:
        f.write(final_output)
        
    print(f"\n✅ 成功建立并覆盖了 feed 文档: {MD_PATH}")

if __name__ == "__main__":
    main()
