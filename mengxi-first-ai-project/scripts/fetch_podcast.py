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
PODCAST_RSS_URLS = {
    "🎙️ 蒙氏与尊重育儿 (Respectful Parenting)": [
        "https://feeds.buzzsprout.com/1730746.rss",      # Janet Lansbury Unruffled
    ],
    "🎙️ 前沿认知与家庭动态 (Cognitive & Family)": [
        "https://plinkhq.com/i/716979718?to=rss",        # Mindful Mama
    ]
}

MD_PATH = os.path.join(PROJECT_DIR, "posts", "md", "podcast-parenting-feed.md") 
MAX_ENTRIES_PER_FEED = 5

def summarize_with_gemini(title, summary_text):
    """使用 Gemini 进行播客内容核心提取。"""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
         return ""
         
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
        headers = {'Content-Type': 'application/json'}
        prompt = f"""你是一位专注儿童早期教育（特别是0-1岁婴儿和幼儿认知发展）的数字播客主编。请对以下播客单集的描述进行高浓度提炼。
文章/播客标题: {title}
播客内容描述: {summary_text}

过滤规则：
1. 自动屏蔽纯广告或无意义宣传。如果全是广告，返回：⚠️ 营销信息，已过滤。
2. 重点提取播客中谈论的 **核心育儿理念、早教心理学应用、或者0-1岁的互动游戏干货**。
3. 请将内容转化为 2 到 3 条简明扼要的【必听价值点】（Why you should listen）。
4. 使用无序列表短句输出，每条控制在 35 字以内，如果涉及专业英文词汇请保留。语言专业、客观。
"""
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        res = requests.post(url, headers=headers, json=payload, timeout=12)
        if res.status_code == 200:
             data = res.json()
             parts = data.get('candidates', [{}])[0].get('content', {}).get('parts', [])
             if parts:
                  return parts[0].get('text', '').strip()
        elif res.status_code == 429:
             print("   ⚠️ Gemini 免费 API 额度已用尽 (Rate limit exceeded)，将保留原始摘要。")
             return ""
    except Exception as e:
         print(f"   ⚠️ Gemini 提炼异常: {e}")
    return ""

def main():
    print("=== 🎧 开始拉取全球育儿播客动态与总结 ===")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
    }

    cards_md = []
    
    for category, urls in PODCAST_RSS_URLS.items():
        cards_md.append(f"\n## {category}\n")
        for url in urls:
            print(f"📡 正在拉取播客 RSS: {url}")
            try:
                res = requests.get(url, headers=headers, timeout=20, verify=False)
                if res.status_code != 200:
                    print(f"   HTTP 异常: {res.status_code}")
                    continue
                    
                feed = feedparser.parse(res.text)
                author = feed.feed.title if hasattr(feed, 'feed') and hasattr(feed.feed, 'title') else url
                cards_md.append(f"\n### 🎙️ 频道: {author}\n")
                
                entries_count = 0
                for entry in feed.entries:
                    if entries_count >= MAX_ENTRIES_PER_FEED:
                        break
                    
                    title = entry.get("title", "未命名单集")
                    link = entry.get("link", "#")
                    summary_text = entry.get("summary", entry.get("description", ""))
                    clean_content = re.sub('<[^>]*>', '', summary_text).strip()
                    
                    # Try to get audio enclosure
                    audio_url = ""
                    if 'enclosures' in entry:
                        for enc in entry.enclosures:
                            if getattr(enc, 'type', '').startswith('audio/'):
                                audio_url = getattr(enc, 'href', '')
                                break
                    
                    pub_date = entry.get('published', '') or entry.get('updated', '')
                    if not pub_date and 'published_parsed' in entry and entry.published_parsed:
                        pub_date = datetime(*entry.published_parsed[:6]).strftime("%Y-%m-%d")
                    elif pub_date:
                        pub_date = pub_date[:16]
                    else:
                        pub_date = datetime.now().strftime("%Y-%m-%d")

                    print(f"👉 详情拉取 [{title[:25]}...]")
                    
                    summary = ""
                    # Optional AI summary to prevent rate limits hitting too hard on all items
                    if entries_count < 3:
                        print(f"🧠 AI 播客价值提炼中...")
                        summary = summarize_with_gemini(title, clean_content)
                        time.sleep(1)
                    
                    md_card = f"""
#### [{title}]({link})
> **🎧 播客速递 | ⏰ 发布时间: {pub_date}**

{f"[🔊 点击在此处收听音频原片]({audio_url})" if audio_url else ""}

**内容提取:**
{summary.strip() if summary else '（无 AI 生成重点，请查阅下方原始 Shownotes）'}

<details>
<summary>📂 查看 完整 Shownotes (Raw Data)</summary>

{clean_content[:500] + ("..." if len(clean_content) > 500 else "")}

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
title: "🎧 全球育儿与蒙氏播客精选 (Podcast Picks)"
date: {today}
tags: ["Podcast", "Parenting", "Audio", "Montessori"]
category: "obsidian"
badge: "播客精选"
---

这里汇总了海外优秀的“蒙氏”和“现代育儿”类的高分 Podcast 单集和核心价值点，带娃时也可以随时当白噪音磨耳朵。

---

{''.join(cards_md)}
"""

    os.makedirs(os.path.dirname(MD_PATH), exist_ok=True)
    with open(MD_PATH, 'w', encoding='utf-8') as f:
        f.write(final_output)
        
    print(f"\n✅ 成功建立并覆盖了播客订阅文档: {MD_PATH}")
    
    # Update index.html
    update_index_html_card(today)

def update_index_html_card(sync_date):
    """自动接入首页播客卡片并渲染提炼摘要"""
    index_path = "/Users/hulimofaqiu/mengxi-first-ai-project/index.html"
    if not os.path.exists(index_path):
        return
        
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    pattern = r'(<a href="post.html\?post=podcast-parenting-feed"[^>]*>(?:(?!</a>).)*?<p class="tg-card-desc">)(.*?)(</p>)'
    
    def repl_desc(match):
        prefix = match.group(1)
        new_desc = f"🎙️ 最新抓取海外育儿高分播客 (同步 {sync_date})"
        return prefix + new_desc + match.group(3)
        
    new_content, count = re.subn(pattern, repl_desc, content, flags=re.DOTALL)
    
    # Also update expandable-summary automatically
    sm_pattern = r'(<a href="post.html\?post=podcast-parenting-feed"[^>]*>.*?<div class="expandable-summary"[^>]*>\s*<ul[^>]*>)(.*?)(</ul>\s*</div>)'
    
    api_key = os.environ.get("GEMINI_API_KEY")
    summary_li_html = ""
    # Just read the generated md to summarize the podcasts
    MD_PATH = os.path.join(PROJECT_DIR, "posts", "md", "podcast-parenting-feed.md")
    with open(MD_PATH, 'r') as mdf:
        source_text = mdf.read()
        
    if api_key and source_text:
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
            prompt = f"请根据以下今日抓取的全球儿童教育、蒙氏和心理大咖播客合集内容，总结出 4 条你认为最具听感的价值点（重点包含任何关于0-1岁的认知或育儿心态知识）。\n\n要求：\n1. 必须只输出 4个 <li> ... </li>，每个 li 内部必须包含带 <strong>加粗的前缀标题</strong>。\n2. 不要任何 markdown 标记、列表符号或者外层 ul 包裹！直接输出 li 标签！\n\n内容库:\n{source_text[:4000]}"
            res = requests.post(url, headers={'Content-Type': 'application/json'}, json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=15)
            if res.status_code == 200:
                summary_li_html = res.json().get('candidates', [{}])[0].get('content', {}).get('parts', [])[0].get('text', '').strip()
                summary_li_html = summary_li_html.replace('```html', '').replace('```', '').strip()
        except Exception as e:
            print(f"⚠️ 生成播客首页摘要时失败: {e}")
            
    if summary_li_html:
        def repl_sm(match):
            return match.group(1) + "\n" + summary_li_html + "\n                             " + match.group(3)
        new_content, count2 = re.subn(sm_pattern, repl_sm, new_content, flags=re.DOTALL)
        if count2 > 0:
            print("✅ index.html 播客推荐 summary 生成并同步更新成功。")
            
    if count > 0:
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✅ index.html 播客卡片标题同步更新成功。")
    else:
        print("⚠️ 未能在 index.html 中找到 podcast 卡片描述，请手动在 index.html 添加 podcast 预留位。")

if __name__ == "__main__":
    main()
