#!/usr/bin/env python3
import os
import requests
import feedparser
import re
from datetime import datetime
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Load environment variables from .env if it exists
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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

# ---------------- CONFIGURATION ----------------
DELIVERY_RSS_MATRIX = {
    "⚖️ 分娩决策 (顺 vs 剖)": [
        "https://rsshub.app/zhihu/people/dr-duan-tao/posts",
        "https://evidencebasedbirth.com/feed/"
    ],
    "🚨 临产征兆与入院触发": [
        "https://www.mayoclinic.org/rss/pregnancy-info",
        "https://rsshub.app/wechat/mps/gh_689108f97e2a"
    ]
}

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_PATH = os.path.join(PROJECT_DIR, "posts", "md", "labor-delivery-feed.md")
MAX_ENTRIES_PER_FEED = 3

def summarize_with_gemini(title, summary_text):
    """使用 Gemini 提炼分娩决策与临产触发监测 S.O.P。"""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return ""
        
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
        headers = {'Content-Type': 'application/json'}
        prompt = f"""你现在是上海红房子医院急诊科的资深分娩导乐。请对资讯进行极简提炼。
文章标题: {title}
文章内容: {summary_text}

提取要求：
1. 分辨【顺产/剖宫产选择】：提取具体的医学指征（如胎位、头盆关系、既往手术史）。
2. 构建【入院决策树】：清晰标注 36 周后的‘必入指征’（如：511 宫缩原则、高位破水、胎动减少）。
3. 生成【急诊 S.O.P】：罗列入院那一刻所需的证件（小卡、医保卡、核酸/抗原要求等上海本地实操）。
4. 语言风格：冷峻、量化、排除干扰项，直接输出结论性清单。不要感叹号和废话。
"""
        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        res = requests.post(url, headers=headers, json=payload, timeout=12)
        if res.status_code == 200:
            data = res.json()
            parts = data.get('candidates', [{}])[0].get('content', {}).get('parts', [])
            if parts:
                return parts[0].get('text', '').strip()
    except Exception as e:
        print(f"   ⚠️ Gemini 摘要异常: {e}")
    return ""

def main():
    print("=== 🌟 开始拉取分娩决策与临产触发监测矩阵 ===")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    cards_md = []
    
    for category, urls in DELIVERY_RSS_MATRIX.items():
        cards_md.append(f"\n## {category}\n")
        for url in urls:
            print(f"📡 正在拉取 RSS: {url}")
            try:
                res = requests.get(url, headers=headers, timeout=20, verify=False)
                if res.status_code != 200:
                    print(f"   HTTP 异常: {res.status_code}")
                    continue
                    
                feed = feedparser.parse(res.text)
                author = feed.feed.title if hasattr(feed, 'feed') and hasattr(feed.feed, 'title') else url
                cards_md.append(f"\n### 📡 来源: {author}\n")
                
                entries_count = 0
                for entry in feed.entries:
                    if entries_count >= MAX_ENTRIES_PER_FEED:
                        break
                    
                    title = entry.get("title", "未命名文章")
                    link = entry.get("link", "#")
                    summary_text = entry.get("summary", entry.get("description", ""))
                    clean_content = re.sub('<[^>]*>', '', summary_text).strip()
                    
                    print(f"👉 详情拉取 [{title[:15]}...]")
                    print(f"🧠 AI 决策提炼中...")
                    summary = summarize_with_gemini(title, clean_content)
                    time.sleep(1)
                    
                    urgent_tag = ""
                    if "宫缩" in title or "破水" in title or "胎动" in title or "急诊" in title:
                         urgent_tag = '<code style="color: #ff4757; border: 1px solid #ff4757;">[URGENT / TRIGGER]</code> '
                         
                    md_card = f"""
#### {urgent_tag}[{title}]({link})
> **⚕️ 分娩决策 S.O.P：**
{summary.strip() if summary else '（总结未生成，具体请查阅原帖）'}

<details>
<summary>📂 查看原始卷宗 (Raw Data)</summary>

{clean_content[:300] + ("..." if len(clean_content) > 300 else "")}

</details>

---
"""
                    cards_md.append(md_card)
                    entries_count += 1
                    
            except Exception as e:
                print(f"[RSS Error] 处理 {url} 失败: {e}")
                continue

    if not cards_md:
        print("\n⚠️ 警报: 未能获取到任何有效内容。")
        return

    today = datetime.now().strftime("%Y-%m-%d")
    final_output = f"""---
title: "🚨 分娩决策与临产急诊监测 (36周+ 专属)"
date: {today}
tags: ["Delivery", "Hospital", "SOP", "Emergency"]
category: "obsidian"
badge: "临产决策"
---

这里汇集了关于 **分娩方式选择、临产指征监控与急诊入院流程** 的量化干货。动态脱水并生成“决策树”，以便在 36 周临产时刻提供最冷峻、最理性的直达指引。

---

{''.join(cards_md)}
"""

    os.makedirs(os.path.dirname(MD_PATH), exist_ok=True)
    with open(MD_PATH, 'w', encoding='utf-8') as f:
        f.write(final_output)
        
    print(f"\n✅ 成功建立并覆盖了分娩决策文档: {MD_PATH}")

if __name__ == "__main__":
    main()
