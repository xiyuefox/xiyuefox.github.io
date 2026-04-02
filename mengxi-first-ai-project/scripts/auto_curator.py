#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI 每日策展人 & 跨界合成引擎 (The Synthesis Engine)
从 Tech (HN/YouTube) 和 Parenting (Busy Toddler/Fun with Mama) 中提取内容，
由 LLM 化身“数字花园首席 AI 架构师”寻找科技与育儿之间的隐藏共鸣。
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

# Mistral API Config
API_KEY = os.environ.get("MISTRAL_API_KEY", "")

# RSS SOURCES
FEEDS = {
    "hn": "https://news.ycombinator.com/rss",
    "youtube": "https://www.youtube.com/feeds/videos.xml?channel_id=UClO1BdHv42-rlV5rTNeyr3Q",
    "busy_toddler": "https://busytoddler.com/feed/",
    "fun_with_mama": "https://www.funwithmama.com/feed/",
    "poche": "https://site.poche.app/explore/rss"
}

def fetch_recent_rss_items(hours=24):
    all_items = []
    now = datetime.datetime.now(datetime.timezone.utc)
    time_limit = now - datetime.timedelta(hours=hours)

    for source, url in FEEDS.items():
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                published_tuple = entry.get('published_parsed') or entry.get('updated_parsed')
                if published_tuple:
                    published_dt = datetime.datetime.fromtimestamp(time.mktime(published_tuple), datetime.timezone.utc)
                    if published_dt > time_limit:
                        clean_summary = re.sub(r'<[^>]+>', '', entry.get('summary', ''))
                        all_items.append({
                            "title": entry.get('title', ''),
                            "link": entry.get('link', ''),
                            "summary": clean_summary[:800],
                            "source": source
                        })
        except Exception:
            continue # 优雅休眠，跳过错误源
    return all_items

def generate_synthesis_article(items):
    if not API_KEY or not items: 
        return None
        
    items_text = ""
    for idx, item in enumerate(items, 1):
        items_text += f"[{item['source'].upper()}] {item['title']}\n   URL: {item['link']}\n   Content: {item['summary']}\n\n"

    # 代理配置
    proxy_handler = urllib.request.ProxyHandler({'http': 'http://127.0.0.1:7897', 'https': 'http://127.0.0.1:7897'})
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)

    url = "https://api.mistral.ai/v1/chat/completions"
    
    prompt = f"""
    你是一位“L5 级数字花园首席 AI 架构师”兼“🤖 AI 跨界主编”。你拥有极高的跨领域洞察力。
    今天，雷达捕捉到了以下过去 24 小时的全球情报：
    
    {items_text}
    
    【你的撰稿任务】
    请根据这些素材写出一篇深度的“跨界合成笔记”。
    
    【核心执行逻辑】
    1. HN 强效降噪：自动丢弃所有常规融资、代码库小更新或低价值争论。只聚焦 AGI 进展、大模型认知科学、未来工作形态或人类行为学。
    2. 隐藏共鸣策略 (Synthesis Engine)：
       - 结合科技情报与育儿策略。例如：将 AGI 认知升级映射到早期教育；或将育儿策略应用到产品管理/利益相关者关系中。
       - 创造类似《AGI 时代的育儿启示》或《像对待幼儿一样管理产品边界》的跨界话题。
    
    【格式与结构红线】
    1. Frontmatter：
       title: "🤖 AI 跨界主编 | [兼具张力与深度的跨界标题]"
       tags: [pm-learning, tech-parenting, automated]
       type: "daily-summary"
       publish: true
       
    2. 内容结构：前瞻洞察层 -> 跨界融合逻辑 -> 实践建议 -> 每日要点溯源。
    
    3. 强制溯源策略：【绝对红线】每一个核心观点或引述内容，必须在其后紧跟 Markdown 格式的原文有效 URL。
       - 示例：[博文原标题](http...) 或 [视频来源](https...)
       - 如果无法从中提取到合法 source 链接，直接返回空字符串触发熔断。
    
    要求：请直接输出带有 --- 包裹的 YAML 头和纯 Markdown 正文。
    """
    
    payload = {
        "model": "mistral-large-latest",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.72
    }
    
    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}'
        })
        with urllib.request.urlopen(req, timeout=150) as res:
            data = json.loads(res.read().decode('utf-8'))
            text = data['choices'][0]['message']['content']
            if text.startswith("```markdown"): text = text[len("```markdown"):].strip()
            if text.endswith("```"): text = text[:-3].strip()
            
            # 链接熔断检查
            if not re.search(r'https?://[^\s)\]]+', text):
                return None
            return text
    except Exception:
        return None

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    today_str = datetime.datetime.now().strftime('%Y-%m-%d')
    
    # 检测是否已生成今日的“跨界主编”笔记
    exists = any(f.startswith(f"{today_str}-") and "AI 跨界主编" in f for f in os.listdir(OUTPUT_DIR))
    if exists:
        return

    items = fetch_recent_rss_items(hours=24)
    if not items:
        return
        
    content = generate_synthesis_article(items)
    if content:
        save_article(content, today_str)

def save_article(content, today_str):
    title_match = re.search(r'title:\s*["\']([^"\']+)["\']', content)
    if not title_match: title_match = re.search(r'title:\s*([^\n]+)', content)
    new_title = title_match.group(1) if title_match else "AI 跨界合成"
    safe_title = re.sub(r'[\\/*?:"<>|#\n]', "", new_title).strip()
    
    filepath = os.path.join(OUTPUT_DIR, f"{today_str}-{safe_title}.md")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"🎉 跨界合成引擎已完成: {filepath}")

if __name__ == "__main__":
    main()
