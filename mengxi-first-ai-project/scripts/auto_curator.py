#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI 每日策展人 (Autonomous Curator)
从 Poche RSS 中提取过去 24 小时的精选内容，
由 LLM 化身“硅谷资深科技编辑”撰写极具主观品味和深度的每日科技/极客早报。
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
RSS_URL = "https://site.poche.app/explore/rss"

def fetch_recent_rss_items(url, hours=24):
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
                        "summary": clean_summary[:500] # 截断防过长
                    })
        except Exception as e:
            continue
    return recent_items

def generate_curation_article(items):
    if not API_KEY: 
        print("未找到 MISTRAL_API_KEY，跳过策展。")
        return None
        
    items_text = ""
    for idx, item in enumerate(items, 1):
        items_text += f"{idx}. 标题：{item['title']}\n   链接：{item['link']}\n   摘要：{item['summary']}\n\n"

    # 强制代理，避免墙
    proxy_handler = urllib.request.ProxyHandler({'http': 'http://127.0.0.1:7897', 'https': 'http://127.0.0.1:7897'})
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)

    url = "https://api.mistral.ai/v1/chat/completions"
    
    prompt = f"""
    你是一位定居在硅谷的“资深极客独立编辑”。你拥有极高的内容品味（Taste），极度讨厌陈词滥调和典型的“AI生成感（AI 废料）”。
    今天，你从信息流中捕捉到了以下过去 24 小时的精粹文章：
    
    {items_text}
    
    【你的撰稿任务】
    请根据以上内容，写一篇排版精美、充满强烈主观洞察力的“每日极客拾遗”专栏文章。
    
    【格式与结构红线】
    1. 前置 Frontmatter（不要遗漏）：必须包含标准的 YAML 头：
       title: "想一个兼具文艺与极客感的好标题（例如：硅谷拾遗 | 当算法遇见心智）"
       date: "{datetime.datetime.now().strftime('%Y-%m-%d')}"
       type: "article"
       tags: [daily-summary, automated, 极客早报]
       publish: true
       
    2. 引人入胜的导语 (Intro)：使用一种慵懒、透彻但老练的语气开场（可以使用 `>` 引用你自己想的一句金句）。
    3. 核心洞察 (Deep Analysis)：【最核心要求】绝不要简单翻译或罗列这几篇文章！你要把它们揉碎，提炼出 3-5 个真正有价值的底层 Insights。进行具有批判性和思辨价值的点评。
    4. 每日要点追踪：在阐述洞察的过程中，自然地将原文的 Markdown 链接穿插进去，如 [文章原标题](链接)，让读者可以追溯来源。
    5. 极简结语 (Outro)：用一两句话收尾，留有余味。
    
    要求：请直接输出带有 --- 包裹的 YAML 头和纯 Markdown 正文，绝对禁止多余的外部解释或对话式回答。
    """
    
    payload = {
        "model": "mistral-large-latest", # 使用最强大杯模型保证质量
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.75
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
            return text
    except Exception as e:
        print(f" LLM 策展深度推演失败: {e}")
        return None

def main():
    print("📡 开始启动『AI 每日策展人』雷达...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # 限制每日只生成一篇：检测前缀日期
    today_str = datetime.datetime.now().strftime('%Y-%m-%d')
    for f in os.listdir(OUTPUT_DIR):
        if f.startswith(today_str) and f.endswith('.md'):
            print(f"✅ 今日的策展专栏已存在 ({f})，触发防御机制，优雅跳过。")
            return

    # 从 poche RSS 获取近 24 小时的内容
    items = fetch_recent_rss_items(RSS_URL, hours=24)
    if not items:
        print("🤷‍♂️ 过去 24 小时未发现新的高价值 RSS 更新，中止今日策展。")
        return
        
    print(f"💡 捕获到 {len(items)} 篇高价值文章素材，正在呼叫大语言模型主笔...")
    article_content = generate_curation_article(items)
    
    if article_content:
        title_match = re.search(r'title:\s*["\']([^"\']+)["\']', article_content)
        if not title_match:
             title_match = re.search(r'title:\s*([^\n]+)', article_content)
             
        new_title = title_match.group(1) if title_match else f"硅谷拾遗"
        safe_title = re.sub(r'[\\/*?:"<>|#\n]', "", new_title).strip()
        
        filepath = os.path.join(OUTPUT_DIR, f"{today_str}-{safe_title}.md")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(article_content)
            
        print(f"🎉 专栏撰写完成！已高光投递至数字花园: {filepath}")

if __name__ == "__main__":
    main()
