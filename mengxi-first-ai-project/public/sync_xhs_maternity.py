#!/usr/bin/env python3
import urllib.request
import json
import os
import datetime
import time

# ---------------- CONFIGURATION ----------------
MCP_BASE_URL = "http://localhost:18060"
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS_DIR = os.path.join(PROJECT_DIR, "posts", "md")
CATEGORY = "xiaohongshu-maternity"
BADGE = "小红书·母婴"

# 关注的母婴博主列表
INFLUENCERS = [
    "熊钰医生", 
    "崔玉涛", 
    "猴哥聊孕产", 
    "段涛", 
    "红房子医院", # 或者是“复旦大学附属妇产科医院”
    "袋鼠新生"
]

MAX_POSTS_PER = 3 # 每个博主同步的最新的笔记数，避免初次运行撑爆页面

def call_api(endpoint, method="GET", body=None):
    url = f"{MCP_BASE_URL}{endpoint}"
    req = urllib.request.Request(url)
    req.method = method
    req.add_header('Content-Type', 'application/json')
    
    data = None
    if body:
        data = json.dumps(body).encode('utf-8')
        
    try:
        with urllib.request.urlopen(req, data=data) as response:
            return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"API Error ({url}): {e}")
        return None

def fetch_influencer_posts(name):
    print(f"正在搜索博主: {name}")
    res = call_api(f"/api/v1/feeds/search?keyword={urllib.parse.quote(name)}")
    if not res or not res.get("success"):
        print(f"搜索失败: {name}")
        return []
    
    feeds = res.get("data", {}).get("feeds", [])
    matched_feeds = []
    
    for feed in feeds:
        if feed.get("modelType") != "note":
            continue
        note_card = feed.get("noteCard", {})
        user = note_card.get("user", {})
        nickname = user.get("nickname", "") or user.get("nickName", "")
        
        # 精确匹配博主名称
        if name in nickname or nickname in name:
            matched_feeds.append({
                "feed_id": feed.get("id"),
                "xsec_token": feed.get("xsecToken"),
                "title": note_card.get("displayTitle", "")
            })
            
    print(f"博主 {name} 匹配到 {len(matched_feeds)} 篇笔记")
    return matched_feeds[:MAX_POSTS_PER]

def sync_feed_detail(feed_id, xsec_token):
    body = {"feed_id": feed_id, "xsec_token": xsec_token}
    res = call_api("/api/v1/feeds/detail", method="POST", body=body)
    if not res or not res.get("success"):
        return None
    return res.get("data", {}).get("data", {}).get("note", {})

def save_as_markdown(note):
    feed_id = note.get("noteId")
    title = note.get("title") or note.get("desc", "")[:15] or "未命名笔记"
    desc = note.get("desc", "")
    timestamp = note.get("time", time.time()*1000) / 1000
    date_str = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
    author = note.get("user", {}).get("nickname", "未知博主")
    
    # 获取 Gemini AI 总结要点
    print(f"正在使用 Gemini 生成 AI 总结: {title[:20]}...")
    from gemini_helper import generate_summary
    summary_ai = generate_summary(desc)
    
    summary_section = ""
    if summary_ai:
        summary_section = f"""
---
### 🤖 Gemini AI 观点要点提炼
{summary_ai}
"""

    slug = f"xhs-{feed_id}"
    filepath = os.path.join(POSTS_DIR, f"{slug}.md")
    
    tags = ["小红书", "母婴", author]
    tags_str = ", ".join([f'"{t}"' for t in tags])
    
    md_content = f"""---
title: "📕 {title} | {author}的小红书"
date: {date_str}
tags: [{tags_str}]
category: "obsidian"
badge: "{BADGE}"
---

{desc}

{summary_section}

---
> 💡 *小红书博主 **{author}** 同步。原笔记 ID: {feed_id}*
"""
    
    os.makedirs(POSTS_DIR, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md_content)
        
    print(f"已同步：{title} -> {slug}.md")

def main():
    print("=== 开始同步小红书母婴内容 ===")
    all_pulled_feeds = []
    
    for name in INFLUENCERS:
        posts = fetch_influencer_posts(name)
        all_pulled_feeds.extend(posts)
        
    print(f"\n共匹配到 {len(all_pulled_feeds)} 篇待请求详情的笔记")
    
    success_count = 0
    for feed in all_pulled_feeds:
        print(f"正在拉取详情: {feed['title']} ({feed['feed_id']})")
        note_detail = sync_feed_detail(feed['feed_id'], feed['xsec_token'])
        
        if note_detail:
            save_as_markdown(note_detail)
            success_count += 1
            time.sleep(1) # 增加延迟，避免触发限流
            
    print(f"\n=== 同步完成！共新增/更新了 {success_count} 篇小红书笔记 ===")

if __name__ == "__main__":
    main()
