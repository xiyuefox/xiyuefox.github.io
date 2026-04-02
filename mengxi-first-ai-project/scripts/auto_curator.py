#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI 每日策展人 (Autonomous Curator)
从 Poche RSS 和 YouTube (PM Mentor) 中提取过去 24 小时的精选内容，
由 LLM 化身不同人格撰写深度笔记。
"""
import os
import re
import sys
import json
import time
import datetime
import urllib.request
import feedparser

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OBSIDIAN_VAULT = "/Users/hulimofaqiu/Documents/obisidian笔记文件/"
OUTPUT_DIR = os.path.join(OBSIDIAN_VAULT, "Daily_Summary")

# 加载 .env
ENV_PATH = os.path.join(PROJECT_DIR, ".env")
if os.path.exists(ENV_PATH):
    with open(ENV_PATH) as f:
        for line in f:
            if '=' in line and not line.startswith('#'):
                k, v = line.strip().split('=', 1)
                os.environ[k.strip()] = v.strip().strip('"')

# 复用经过实测非常稳定的 Mistral API
API_KEY = os.environ.get("MISTRAL_API_KEY", "")
POCHE_RSS_URL = "https://site.poche.app/explore/rss"
YOUTUBE_RSS_URL = "https://www.youtube.com/feeds/videos.xml?channel_id=UClO1BdHv42-rlV5rTNeyr3Q"

def fetch_recent_rss_items(url, hours=24, source_type="poche"):
    feed = feedparser.parse(url)
    recent_items = []
    now = datetime.datetime.now(datetime.timezone.utc)
    time_limit = now - datetime.timedelta(hours=hours)

    for entry in feed.entries:
        try:
            # 解析发布时间
            published_tuple = entry.get('published_parsed') or entry.get('updated_parsed')
            if published_tuple:
                published_dt = datetime.datetime.fromtimestamp(time.mktime(published_tuple), datetime.timezone.utc)
                if published_dt > time_limit:
                    clean_summary = re.sub(r'<[^>]+>', '', entry.get('summary', ''))
                    recent_items.append({
                        "title": entry.get('title', ''),
                        "link": entry.get('link', ''),
                        "summary": clean_summary[:800], # 适当加长以获取更多上下文
                        "source": source_type
                    })
        except Exception:
            continue
    return recent_items

def generate_curation_article(items, source_type="poche"):
    if not API_KEY: 
        return None
        
    items_text = ""
    for idx, item in enumerate(items, 1):
        items_text += f"{idx}. 标题：{item['title']}\n   链接：{item['link']}\n   摘要：{item['summary']}\n\n"

    # 强制代理，避免访问限制
    proxy_handler = urllib.request.ProxyHandler({'http': 'http://127.0.0.1:7897', 'https': 'http://127.0.0.1:7897'})
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)

    url = "https://api.mistral.ai/v1/chat/completions"
    
    if source_type == "youtube":
        prompt = f"""
        你是一位资深产品经理导师 (Senior PM Mentor)。你擅长深挖技术背后的产品商业逻辑。
        今天，你为你的学员从 @ColinMattthewsAI 的频道中捕捉到了以下过去 24 小时的视频教学素材：
        
        {items_text}
        
        【你的撰稿任务】
        请根据以上视频内容，撰写一份结构化、可操作性强的“PM 导师学习笔记”。
        
        【核心提炼方向】
        1. 产品经理思维 (PM Thinking)：视频中体现了什么样的用户洞察或商业考量？
        2. 技术基础知识 (Tech Foundation)：涉及了哪些 API、系统架构或技术实现要点？
        3. AI 原型制作 (AI Prototyping)：有哪些具体的 AI 工具利用或原型搭建技巧？
        
        【格式与结构红线】
        1. 前置 Frontmatter：
           title: "PM 导师笔记 | [视频核心主题]"
           date: "{datetime.datetime.now().strftime('%Y-%m-%d')}"
           type: "daily-summary"
           tags: [pm-learning, automated]
           publish: true
           
        2. 深度提炼：不要简单罗列。将视频内容转化为结构化的硬核知识点。
        3. 强制溯源：【绝对红线】在笔记末尾或核心内容中，必须附上该视频的真实有效播放链接（Markdown 格式：[观看原视频](链接)）。
        
        注意：如果没有找到合法的 http/https 链接，请停止生成。
        请直接输出带有 --- 包裹的 YAML 头和纯 Markdown 正文。
        """
    else:
        prompt = f"""
        你是一位定居在硅谷的“资深极客独立编辑”。你拥有极高的内容品味，极度讨厌“AI生成感”。
        今天，你从信息流中捕捉到了以下过去 24 小时文章：
        
        {items_text}
        
        【你的撰稿任务】
        请撰写一篇充满主观洞察力的“每日极客拾遗”专栏文章。
        
        【格式与结构红线】
        1. 前置 Frontmatter：
           title: "[标题]"
           date: "{datetime.datetime.now().strftime('%Y-%m-%d')}"
           type: "daily-summary"
           tags: [daily-summary, automated, 极客早报]
           publish: true
           
        2. 内容：导语、核心洞察（3-5个底层 Insights）、原文链接穿插、极简结语。
        
        请直接输出带有 --- 包裹的 YAML 头和纯 Markdown 正文。
        """
    
    payload = {
        "model": "mistral-large-latest",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    
    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}'
        })
        with urllib.request.urlopen(req, timeout=120) as res:
            data = json.loads(res.read().decode('utf-8'))
            text = data['choices'][0]['message']['content']
            if text.startswith("```markdown"): text = text[len("```markdown"):].strip()
            if text.endswith("```"): text = text[:-3].strip()
            
            # 针对 YouTube 源的强制溯源熔断检查
            if source_type == "youtube":
                if not re.search(r'https?://[^\s)\]]+', text):
                    print("⚠️ 熔断触发：YouTube 笔记中未找到合法溯源链接，中止发布。")
                    return None
                    
            return text
    except Exception:
        # 优雅休眠，不产生报错日志
        return None

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    today_str = datetime.datetime.now().strftime('%Y-%m-%d')
    
    # 1. 处理 Poche Curation (极客早报)
    poche_exists = any(f.startswith(f"{today_str}-") and "PM 导师笔记" not in f for f in os.listdir(OUTPUT_DIR))
    if not poche_exists:
        items = fetch_recent_rss_items(POCHE_RSS_URL, hours=24, source_type="poche")
        if items:
            content = generate_curation_article(items, source_type="poche")
            if content:
                save_article(content, today_str, "poche")
    
    # 2. 处理 YouTube PM Mentor (PM 导师笔记)
    yt_exists = any(f.startswith(f"{today_str}-") and "PM 导师笔记" in f for f in os.listdir(OUTPUT_DIR))
    if not yt_exists:
        items = fetch_recent_rss_items(YOUTUBE_RSS_URL, hours=24, source_type="youtube")
        if items:
            content = generate_curation_article(items, source_type="youtube")
            if content:
                save_article(content, today_str, "youtube")

def save_article(content, today_str, source_type):
    title_match = re.search(r'title:\s*["\']([^"\']+)["\']', content)
    if not title_match:
         title_match = re.search(r'title:\s*([^\n]+)', content)
         
    new_title = title_match.group(1) if title_match else f"{source_type.capitalize()} 拾遗"
    safe_title = re.sub(r'[\\/*?:"<>|#\n]', "", new_title).strip()
    
    filepath = os.path.join(OUTPUT_DIR, f"{today_str}-{safe_title}.md")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"🎉 {source_type} 专栏撰写完成: {filepath}")

if __name__ == "__main__":
    main()
