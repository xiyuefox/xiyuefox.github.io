#!/usr/bin/env python3
import os
import re
import sys
import requests
import feedparser
from datetime import datetime

# 基础路径配置
PROJECT_DIR = "/Users/hulimofaqiu/mengxi-first-ai-project"
OBSIDIAN_VAULT = "/Users/hulimofaqiu/Documents/obisidian笔记文件/"
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# 📡 播客 RSS 源配制 (双轨)
PODCAST_FEEDS = {
    "Huberman Lab": {
        "url": "https://feeds.megaphone.fm/hubermanlab",
        "audience": "adult",
        "icon": "🧠"
    },
    "Sleep Sounds": {
        "url": "https://feed.podbean.com/blissfulrelaxationmusic/feed.xml", 
        "audience": "baby",
        "icon": "🌙"
    }
}

def summarize_with_gemini(title, content, audience):
    """根据定制的 Prompt 调用 Gemini API 提炼播客摘要"""
    if not GEMINI_API_KEY:
        return "❌ 没找到 GEMINI_API_KEY 环境变量，无法生成 AI 摘要。"

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {'Content-Type': 'application/json'}

    # 针对受众调整前置引导
    audience_context = "针对成年人、极客妈妈，偏向硬核、理性与科普。" if audience == 'adult' else "针对小月龄婴儿/孕妇，偏向白噪音、轻音乐和伴眠环境音效果。"

    prompt = f"""你现在不仅仅是一个内容策展人，你是一位极具幽默感、拥有硬核建筑学背景且充满极客精神的创客妈妈。
请阅读下方播客单集的标题与简介，并输出不超过 250 字的中文摘要。
受众背景：{audience_context}

在撰写时，你必须严格遵守以下“趣味性”原则：
1. **拒绝废话**：不要写“在这集里...”。请专门提取单集中最反直觉、最硬核或最让人“哇哦”的细节（追求极高的 Information Gain）。
2. **注入极客与生活之盐**：在总结时，请适度加入一点幽默的调侃，或者融入一些建筑设计、物理学或极客自动化（树莓派等）梗，让文字充满生命力。

输出结构如下（必须保持！）：
💡 **核心亮点**：一句话排版（必须一针见血或足够有趣）。
🛠️ **创客/教学脑洞**：一个具体的、落地的互动点子。
🍼 **育儿/生活启发**：接地气的生活折射。

---
下方是真正的播客单集内容，请输出你的摘要：
标题: {title}
简介: {content[:2000]}
"""

    try:
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        res = requests.post(url, json=payload, headers=headers, timeout=20)
        if res.status_code == 200:
            data = res.json()
            parts = data.get('candidates', [{}])[0].get('content', {}).get('parts', [])
            if parts:
                return parts[0].get('text', '').strip()
    except Exception as e:
        return f"⚠️ API 摘要生成异常: {e}"
    return "⚠️ AI 未能正常返回内容。"

def sanitize_slug(title):
    import pypinyin
    title_cleaned = re.sub(r'[^\w\s-]', '', title).strip()
    pinyin_list = pypinyin.lazy_pinyin(title_cleaned)
    slug = '-'.join(pinyin_list).lower()
    return re.sub(r'[-]+', '-', slug)

def main():
    print("🚀 启动 播客自动化抓取引擎...")
    output_dir = os.path.join(OBSIDIAN_VAULT, "00-Inbox", "Podcasts")
    if not os.path.exists(OBSIDIAN_VAULT):
        print(f"❌ 警告: 未能找到 Obsidian 目录，将在本地保存。")
        output_dir = os.path.join(PROJECT_DIR, "posts", "podcasts")
        
    os.makedirs(output_dir, exist_ok=True)

    for name, config in PODCAST_FEEDS.items():
        print(f"📡 正在拉取 [{name}] 订阅源: {config['url']}...")
        try:
            # 💡 升级 1：添加真实浏览器 User-Agent，绕过 Simplecast 的反爬防火墙
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }
            res_feed = requests.get(config['url'], headers=headers, timeout=15)
            feed = feedparser.parse(res_feed.content)
            
            # 抓取最新的 1 个单集做示范测试
            entries = feed.entries[:1] if getattr(feed, 'entries', []) else []
            if not entries:
                 print(f"⚠️ [{name}] 未找到任何单集内容。")
                 continue

            for entry in entries:
                title = entry.get('title', 'Untitled Episode')
                # 💡 升级 2：更宽松的音频探测逻辑 (MIME Type 放宽)
                audio_src = ""
                if hasattr(entry, 'links'):
                    for link in entry.links:
                        if ('audio' in link.get('type', '') or link.get('rel') == 'enclosure') and link.get('href'):
                            audio_src = link.get('href')
                            break
                
                if not audio_src:
                    # Fallback enclosure
                    enclosures = entry.get('enclosures', [])
                    if enclosures:
                        audio_url = enclosures[0].get('href', '')
                        if audio_url:
                            audio_src = audio_url

                summary_text = entry.get('summary', entry.get('description', ''))
                summary_cleaned = re.sub(r'<[^>]+>', '', summary_text)

                print(f"🤖 正在为单集《{title}》生成 AI 节点...")
                ai_summary = summarize_with_gemini(title, summary_cleaned, config['audience'])

                slug = sanitize_slug(title)
                filepath = os.path.join(output_dir, f"podcast-{slug}.md")

                # 构建 Frontmatter 骨骼
                content = f"""---
title: "{title}"
type: podcast
audience: {config['audience']}
date: {datetime.now().strftime("%Y-%m-%d")}
audio_src: "{audio_src}"
tags: [podcast, ai-curated]
---

# 🎙️ {name}: {title}

{ai_summary}

---
🔗 **音频直达节点**：[点击播放音频]({audio_src})
"""
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ 已成功生成: {os.path.basename(filepath)}")

        except Exception as e:
            print(f"⚠️ 抓取 [{name}] 发生异常: {e}")

    print("Sync Podcasts Flow DONE! 🎉")

if __name__ == "__main__":
    main()
