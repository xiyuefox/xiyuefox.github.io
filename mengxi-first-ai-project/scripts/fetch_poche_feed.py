#!/usr/bin/env python3
import urllib.request
import urllib.error
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
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_PATH = os.path.join(PROJECT_DIR, "posts", "md", "poche-feed.md")

RSS_FEEDS = [
    {
        "url": "https://site.poche.app/explore/rss",
        "name": "poche.app",
        "tag": "poche",
        "system_prompt": "你现在是一个精通极简主义和终端美学(Terminal Garden)的架构师。请对这段 poche.app 的内容进行摘要。\n处理规则：\n1. 提炼核心的设计理念、极优配置或思考。\n2. 保留原作者的“电子农夫”/“极简园艺”精神。\n3. 使用无序列表 - 输出，每条硬核干货不超过 30 字，剔除废话。"
    },
    {
        "url": "https://zenhabits.net/feed/",
        "name": "Zen Habits",
        "tag": "minimalism",
        "system_prompt": "你现在是一位极简主义哲学导师。请提炼文章的核心生活哲学或习惯法则。\n1. 提取最核心的行动指南（如：减少物品、专注当下、克服拖延）。\n2. 剥离所有抒情和故事，仅保留实操方法。\n3. 使用无序列表 - 输出，每条不超过 30 字。"
    },
    {
        "url": "https://hackaday.com/category/raspberry-pi/feed/",
        "name": "Hackaday (Raspberry Pi)",
        "tag": "geek_hardware",
        "system_prompt": "你现在是一位硬核创客与极客工程师。请解析这个树莓派/硬件 DIY 项目的底层逻辑。\n1. 提取最核心的硬件构成或算法亮点。\n2. 提取最具有创意或可复用的工程实操点。\n3. 使用无序列表 - 输出，每条不超过 30 字，避免学术黑话。"
    }
]

MAX_ENTRIES_PER_FEED = 3

def main():
    print("=== 🌟 开始拉取极简主义与极客硬件矩阵 ===")
    
    if not feedparser:
        print("⚠️ 无法拉取 RSS (未安装 feedparser)")
        return

    import sys
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    import ark_helper

    import requests
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    cards_md = []
    
    for item in RSS_FEEDS:
        url = item["url"]
        name = item["name"]
        print(f"📡 正在拉取 RSS: {url} ({name})")
        try:
            res = requests.get(url, headers=headers, timeout=15)
            if res.status_code != 200:
                print(f"   HTTP 异常: {res.status_code}")
                continue
                
            feed = feedparser.parse(res.text)
            author = feed.feed.title if hasattr(feed, 'feed') and hasattr(feed.feed, 'title') else name
            cards_md.append(f"\n## 📡 来源: {author}\n")
            entries_count = 0
            
            for entry in feed.entries:
                if entries_count >= MAX_ENTRIES_PER_FEED:
                    break
                    
                title = entry.get("title", "未命名文章")
                link = entry.get("link", "#")
                summary_text = entry.get("summary", entry.get("description", ""))
                
                # 清理 HTML 标签
                clean_content = summary_text.replace("<p>", "").replace("</p>", "\n").replace("<br/>", "\n")
                if not clean_content and hasattr(entry, 'content'):
                    clean_content = entry.content[0].value
                    
                print(f"👉 详情拉取 [{title[:15]}...]")
                print(f"🧠 Ark 逻辑提炼中...")
                
                summary = ark_helper.call_ark_summarize(clean_content, system_prompt=item["system_prompt"])
                time.sleep(1)
                
                tags = [t.term for t in entry.get("tags", [])] if "tags" in entry else []
                tags.append(item["tag"])
                tag_str = ", ".join(set(tags))
                truncated_raw = clean_content[:300] + ("..." if len(clean_content) > 300 else "")
                
                md_card = f"""
### 🌿 [{title}]({link})
**🧠 思维矩阵**: 📡 来源: {author} | 🏷️ 标签: {tag_str}

> **🤖 干货提炼 (Takeaways)：**
{summary.strip()}

<details>
<summary>📂 查看原始卷宗 (Raw Data)</summary>

{truncated_raw.strip()}

</details>

---
"""
                cards_md.append(md_card)
                entries_count += 1
                
        except Exception as e:
            print(f"[RSS Engine Error] 处理 {url} 失败: {e}")
            continue

    if not cards_md:
        print("\n⚠️ 警报: 未能获取到任何有效内容。")
        return

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    final_output = f"""---
title: "🌿 极简哲学与极客硬件看板"
date: {today}
tags: ["minimalism", "hardware", "geek", "philosophy"]
category: "obsidian"
badge: "极简极客"
---

这里汇集了关于 **极简主义哲学、高效生活习惯与硬核极客硬件/创客项目** 的提炼干货。动态脱水，剥离故事泡沫，仅保留实操理念与工程脑洞。

---

{''.join(cards_md)}
"""

    os.makedirs(os.path.dirname(MD_PATH), exist_ok=True)
    with open(MD_PATH, 'w', encoding='utf-8') as f:
        f.write(final_output)
        
    print(f"\n✅ 成功建立并覆盖了 poche feed 文档: {MD_PATH}")

if __name__ == "__main__":
    main()
