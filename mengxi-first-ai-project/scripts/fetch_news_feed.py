#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动资讯流整合脚本 (Universal Feed Fetcher)
读取 config/news_feeds.yaml 自动抓取更新，并存储为带有 Frontmatter 的 .md
"""

import os
import re
import yaml
import time
import requests
import feedparser
from datetime import datetime

# ==========================================
# 📐 配置变量
# ==========================================
PROJECT_DIR_FALLBACK = "/Users/hulimofaqiu/mengxi-first-ai-project"
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if not os.path.exists(os.path.join(PROJECT_DIR, "config")):
    PROJECT_DIR = PROJECT_DIR_FALLBACK

CONFIG_FILE = os.path.join(PROJECT_DIR, "config", "news_feeds.yaml")
POSTS_DIR = os.path.join(PROJECT_DIR, "posts", "md")

# 确保输出目录存在
os.makedirs(POSTS_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
    'Accept': 'application/rss+xml, application/rdf+xml, application/atom+xml, application/xml, text/xml'
}

def load_config():
    if not os.path.exists(CONFIG_FILE):
        print(f"配置文件不存在: {CONFIG_FILE}")
        return []
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config.get('feeds', [])

def sanitize_filename(title):
    # 移除非法字符，供作为 slug 或文件名
    slug = re.sub(r'[\\/*?:"<>|#]', "", title)
    # 取前 60 个字符防止文件名过长
    return slug.strip()[:60]

def clean_html(raw_html):
    # 极简清洗，移除复杂的 tag 和样式，只保留纯文本
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', str(raw_html))
    return cleantext.replace('\n', ' ').strip()

def process_feed(feed_config):
    name = feed_config.get("name", "Unknown Feed")
    url = feed_config.get("url")
    feed_type = feed_config.get("type", "news_feed")
    tags = feed_config.get("tags", [])
    
    if not url:
        print(f"⚠️ 订阅源 {name} 缺失 URL，跳过。")
        return
        
    print(f"\n🔄 正在拉取: {name} ({url})")
    
    try:
        # 使用 requests 加入 header 获取更稳定，如果是部分网站拦截了 feedparser 的原生 ua
        res = requests.get(url, headers=HEADERS, timeout=15)
        parsed = feedparser.parse(res.content)
    except Exception as e:
        print(f"❌ 拉取失败 {name}: {e}")
        return

    # 抓取前 5 篇即可
    entries = parsed.entries[:5]
    print(f"   => 成功解析 {len(entries)} 篇文章。")
    
    for entry in entries:
        title = entry.get('title', 'Untitled')
        link = entry.get('link', '')
        summary = entry.get('summary', '') or entry.get('description', '')
        
        # 尝试提取发布时间
        published = entry.get('published_parsed') or entry.get('updated_parsed')
        if published:
            pub_date = datetime.fromtimestamp(time.mktime(published)).strftime("%Y-%m-%d %H:%M:%S")
        else:
            pub_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
        desc = clean_html(summary)[:200]
        if len(desc) == 200: desc += "..."
        
        # 生成标准化 md 文件
        safe_title = sanitize_filename(title)
        md_filename = f"{safe_title}.md"
        md_filepath = os.path.join(POSTS_DIR, md_filename)
        
        # 为了防重，采用时间戳做为前缀或者直接检查是否已经存在
        # 因为我们是拉取最近 5 篇，可以直接跳过存在的
        if os.path.exists(md_filepath):
            # 已经拉取过
            continue
            
        content = f"""---
title: "{title.replace('"', '')}"
date: {pub_date}
tags: [{", ".join(tags)}]
badge: "{tags[0] if tags else 'news'}"
type: {feed_type}
source_link: "{link}"
source_name: "{name}"
---

### {title}

**[{name}]** 发表于 `{pub_date}`

{desc}

> [🔗 阅读原文链接 / Read Original Article]({link})
"""
        with open(md_filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"   ✔️ 自动收录: {safe_title}")

def main():
    feeds = load_config()
    if not feeds:
        print("没有可用的订阅源。")
        return
        
    for feed in feeds:
        process_feed(feed)
        
    print("\n✅ 综合资讯流自动拉取完成！")

if __name__ == "__main__":
    main()
