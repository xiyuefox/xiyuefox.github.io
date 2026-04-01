#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
import json
import os
import re
from datetime import datetime

# 配置多关键词
TOPICS = {
    "🛠️ 极客爸妈：树莓派与智能看护": ["raspberry pi baby", "baby monitor opencv", "baby crying detection"],
    "👩‍💻 科技圈女性与妈妈：热门探讨": ["women tech startup", "moms in tech", "career break motherhood", "tech startup balance"]
}
FILE_PATH = "posts/md/hn-topics-feed.md"
TARGET_DIR = os.path.dirname(FILE_PATH)

import requests

def translate_to_zh(text):
    """使用 gtx 免密钥 Google 翻译接口，将英文转为中文。带有超时保障。"""
    if not text or len(text.strip()) == 0:
        return ""
    try:
        encoded_text = urllib.parse.quote(text)
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=zh-CN&dt=t&q={encoded_text}"
        
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=8) as response:
            data = json.loads(response.read().decode('utf-8'))
            results = data[0]
            translated_text = "".join([sentence[0] for sentence in results if sentence[0]])
            return translated_text.strip()
    except Exception as e:
        return ""

def summarize_hn_with_gemini(title, comments):
    """根据 HN 的标题和前 3 条高赞评论，总结多方观点作为看点摘要。"""
    import sys
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    import ark_helper

    system_prompt = """你是一个资深的硅谷极客与技术观察员。请阅读这篇 Hacker News 帖子及其前 3 条高赞评论。请以客观、精炼的语言（不超过 150 字），输出：
1. 核心看点：这个项目/观点为什么引起了 HN 社区的关注？
2. 观点碰撞：提炼评论区里最有价值的延伸讨论或反方观点。
使用无序列表输出，风格保持极客、冷峻、直击要害。绝对杜绝感叹号和废话。
"""
    combined_text = f"【主贴标题】：{title}\n【网友高赞评论总结】：\n{comments}"
    return ark_helper.call_ark_summarize(combined_text, system_prompt=system_prompt)

def fetch_hn_stories(query):
    print(f"🔄 正在从 Hacker News Algolia API 抓取 '{query}' 的最新讨论...")
    encoded_query = urllib.parse.quote(query)
    
    # 2025-01-01 00:00:00 UTC 的时间戳
    TIMESTAMP_2025 = 1735689600 
    
    # 💡 强行增加 numericFilters 锁死 2025~2026 年份（%3E%3D 即为 >= 符号）
    url = f"https://hn.algolia.com/api/v1/search?query={encoded_query}&tags=story&numericFilters=created_at_i%3E%3D{TIMESTAMP_2025}&hitsPerPage=18"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            hits = data.get('hits', [])
            
            # 💡 核心步骤一：在 Topic 单一关键词内，按照 Points (点赞数) 降序排列
            hits = sorted(hits, key=lambda x: x.get('points', 0), reverse=True)
            return hits[:3] # 仅截取降序后的【前 3 名优质热帖】
    except Exception as e:
        print(f"❌ 抓取 Hacker News 失败: {e}")
        return []

def fetch_top_comments(object_id):
    """抓取单条 Story 的前 3 条一级高赞评论内容"""
    url = f"https://hn.algolia.com/api/v1/items/{object_id}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            children = data.get('children', [])
            top_comments = []
            
            for child in children[:3]: 
                text_html = child.get('text', '')
                if not text_html:
                    continue
                author = child.get('author', '匿名')
                
                # 💡 先把 HTML 换行标签显式拆解为 \n，再进行标签过滤
                text_html = text_html.replace('<p>', '\n\n').replace('</p>', '').replace('<br>', '\n')
                
                clean_text = re.sub('<[^>]*>', '', text_html)
                clean_text = clean_text.replace('&quot;', '"').replace('&#x27;', "'").replace('&amp;', '&')
                
                top_comments.append({
                    "author": author,
                    "text": clean_text.strip(),
                    "created_at": child.get('created_at', '')
                })
            return top_comments
    except Exception as e:
        print(f"⚠️ 抓取评论树 {object_id} 失败: {e}")
        return []

def fetch_github_baby_projects():
    """从 GitHub API 检索树莓派母婴看护、哭声检测的高赞项目方案。"""
    print("🔄 正在从 GitHub API 拉取树莓派智能看压看护项目...")
    headers = {'User-Agent': 'Mozilla/5.0'}
    projects_md = "\n## 🛠️ GitHub 极客开源：树莓派智能看护 DIY 方案\n\n"
    projects_md += "> [!IMPORTANT]\n> 以下为全球极客在 GitHub 开源的智能看护、哭声检测、深度学习等热点项目。\n\n"
    
    try:
        url = "https://api.github.com/search/repositories?q=raspberry+pi+baby+monitor&sort=stars&order=desc"
        res = requests.get(url, headers=headers, timeout=12)
        if res.status_code == 200:
            items = res.json().get('items', [])[:3] # 取前3个最火的
            for item in items:
                name = item.get('name')
                full_name = item.get('full_name')
                link = item.get('html_url')
                desc = item.get('description', '无简介')
                stars = item.get('stargazers_count')
                
                updated_at = item.get('updated_at', '')[:10] if item.get('updated_at') else "未知"
                
                # 调用 Gemini 进行项目一句话看点
                api_key = os.environ.get("GEMINI_API_KEY")
                ai_sum = ""
                if api_key:
                    try:
                        g_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
                        prompt = f"请总结以下 GitHub 项目的核心看点/功能实现原理：\n项目名: {full_name}\n简介: {desc}"
                        payload = {"contents": [{"parts": [{"text": prompt}]}]}
                        g_res = requests.post(g_url, json=payload, timeout=8)
                        if g_res.status_code == 200:
                            parts = g_res.json().get('candidates', [{}])[0].get('content', {}).get('parts', [])
                            if parts:
                                ai_sum = parts[0].get('text', '').strip()
                    except Exception:
                        pass
                
                ai_sum_md = f"\n💡 **AI 项目看点**：{ai_sum}\n" if ai_sum else ""
                
                projects_md += f"### 📌 [{full_name}]({link})\n"
                projects_md += f"*   **项目星标**：🌟 `{stars}` Stars | ⏰ **更新时间**：`{updated_at}`\n"
                projects_md += f"*   **项目描述**：{desc}\n"
                projects_md += f"{ai_sum_md}\n"
    except Exception as e:
        projects_md += f"⚠️ GitHub 数据拉取超时或失败: {e}\n"
    
    return projects_md

def render_hn_item(item, json_data):
    """根据 Poche 风格渲染单条 HN 帖子"""
    object_id = item.get('objectID')
    title_en = item.get('title', '无标题')
    link = item.get('url') or f"https://news.ycombinator.com/item?id={object_id}"
    author = item.get('author', '未知')
    points = item.get('points', 0)
    num_comments = item.get('num_comments', 0)
    hn_link = f"https://news.ycombinator.com/item?id={object_id}"
    
    comments_list = fetch_top_comments(object_id)
    comments_text_bulk = "\n".join([f"- {c['text']}" for c in comments_list])
    
    # 🪐 调用 Gemini 总结核心观点
    ai_insights = summarize_hn_with_gemini(title_en, comments_text_bulk)
    if not ai_insights or "超时" in ai_insights or "异常" in ai_insights:
        ai_insights = "无摘要"
        
    is_github = "github.com" in link.lower()
    github_badge = ' <code style="color: #2ea043; background: transparent; border: 1px solid #30363d; padding: 2px 6px; font-size: 11px;">[📦 OPEN SOURCE / GITHUB]</code>' if is_github else ""
    
    created_at_str = item.get('created_at', '')
    post_date = created_at_str[:10] if created_at_str else datetime.now().strftime("%Y-%m-%d")

    # 汉化标题支持
    title_zh = translate_to_zh(title_en)
    # 采用用户最喜欢的格式：English Title （译：中文翻译）
    final_title = f"{title_en} （译：{title_zh}）" if title_zh else title_en

    # 拼凑 JSON (供 Hugo 渲染)
    json_data.append({
        "url": link,
        "date": post_date,
        "title": final_title,
        "summary": ai_insights,
        "points": points,
        "comments": num_comments,
        "author": author,
        "tags": ["geek_mom" if "raspberry" in title_en.lower() or "baby" in title_en.lower() else "career"]
    })

    comments_md = ""
    if comments_list:
        comments_md = "> **💬 部分网友高赞观点：**\n"
        for c in comments_list:
            time_str = c.get('created_at', '')[:10] if c.get('created_at') else "未知"
            text = c['text'].replace('\n', ' ')
            if len(text) > 150:
                text = text[:150] + "..."
            comments_md += f"> * `{c['author']}` ({time_str}): {text}\n"
        comments_md += ">\n"

    ai_insights_formatted = ai_insights.replace('\n', '\n> ')
    return f"""### [🚀 {final_title}]({link})
<p style="font-family: ui-monospace, monospace; font-size: 12px; color: #666; margin-top: -10px;">
  ▲ {points} pts | 💬 {num_comments} comments | 🔗 <a href="{hn_link}" style="color: #666; text-decoration: underline;">HN Discussion</a>{github_badge}
</p>

> **🤖 社区交锋与脱水总结：**
> {ai_insights_formatted}
>
{comments_md}---

"""

def fetch_hn_rss():
    print("🔄 正在从 Hacker News 官方 RSS 抓取最新讨论...")
    url = "https://news.ycombinator.com/rss"
    try:
        import feedparser
        feed = feedparser.parse(url)
        hits = []
        for entry in feed.entries[:6]: # 最新 6 条
            object_id = ""
            comments_url = getattr(entry, "comments", "")
            if "id=" in comments_url:
                import urllib.parse
                parsed = urllib.parse.urlparse(comments_url)
                qs = urllib.parse.parse_qs(parsed.query)
                if "id" in qs:
                    object_id = qs["id"][0]
            
            hits.append({
                "objectID": object_id,
                "title": entry.title,
                "url": getattr(entry, "link", getattr(entry, "comments", "")),
                "author": "RSS Feed",
                "points": 100, # 官方首页默认高优
                "num_comments": 0,
                "created_at": ""
            })
        return hits
    except Exception as e:
        print(f"❌ 抓取 HN RSS 失败: {e}")
        return []

def generate_markdown():
    today = datetime.now().strftime("%Y-%m-%d")
    md_content = f"# 🤖 Hacker News & GitHub 极客智能看护看板\n\n"
    md_content += "> [!NOTE]\n> 本页面由自动化脚本同步，拉取 Hacker News (含官方 RSS) 及 GitHub 的最新技术讨论。\n\n---\n\n"

    seen_ids = set()
    json_data = []

    # 1. 抓取官方 RSS
    rss_hits = fetch_hn_rss()
    md_content += '<h2 id="hn-frontpage">🌍 Hacker News 官方最新 (RSS)</h2>\n\n'
    if rss_hits:
        for item in rss_hits:
            seen_ids.add(item.get('objectID'))
            md_content += render_hn_item(item, json_data)
    else:
        md_content += "> （暂无 RSS 数据）\n\n"

    # 2. 多关键词拉取
    all_queries = ["raspberry pi baby", "baby monitor opencv", "parenting", "women startup"]
    all_hits = []
    for q in all_queries:
        hits = fetch_hn_stories(q)
        if hits:
            all_hits.extend(hits)
            
    all_hits = sorted(all_hits, key=lambda x: x.get('points', 0), reverse=True)
    
    geek_lab = []
    career_science = []
    
    # 3. 板块分类逻辑
    for item in all_hits:
        object_id = item.get('objectID')
        if object_id and object_id in seen_ids:
            continue
        if object_id:
            seen_ids.add(object_id)
        
        title_en = item.get('title', '无标题')
        link = item.get('url') or ""
        
        is_geek = False
        if "raspberry" in title_en.lower() or "monitor" in title_en.lower() or "opencv" in title_en.lower() or "github.com" in link.lower():
            is_geek = True
            
        if is_geek:
            geek_lab.append(item)
        else:
            career_science.append(item)

    # ---------------------------
    # 板块 A: Geek Lab
    # ---------------------------
    md_content += '<h2 id="geek-mom">👩💻 极客父母 DIY 实验室 (Geek Lab)</h2>\n\n'
    if geek_lab:
        for item in geek_lab[:4]: # 限制数量防 429
            md_content += render_hn_item(item, json_data)
    else:
        md_content += "> （暂无最新极客实验室项目讨论）\n\n"

    # 植入 GitHub 树莓派开源看护方案
    github_md = fetch_github_baby_projects()
    md_content += github_md + "\n\n"

    # ---------------------------
    # 板块 B: Career & Science
    # ---------------------------
    md_content += '<h2>💡 职场与硬核育儿 (Career & Science)</h2>\n\n'
    if career_science:
        for item in career_science[:4]: # 限制数量防 429
            md_content += render_hn_item(item, json_data)
    else:
        md_content += "> （暂无最新育儿讨论）\n\n"

    md_content += """
---
*💡 排行榜由优质度 (Points) 排行榜自动更新与官方 RSS 聚合生成。*
"""

    if not geek_lab and not career_science and not rss_hits:
        print("⚠️ 未发现任何 Hacker News 讨论，略过生成。")
        return

    # 1. 写入 Markdown 文件
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR, exist_ok=True)
        
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"✅ Hacker News 优质排行榜看板已生成至: {FILE_PATH}")

    # 自动化注入 YAML Frontmatter (Dataview 联动支持)
    try:
        from utils import append_frontmatter
        append_frontmatter(FILE_PATH, {
            "title": "Hacker News 极客智能看护看板 (自动更新)",
            "date": today,
            "category": ["Hacker News"],
            "tags": ["RaspberryPi", "OpenCV", "SmartHome", "Automated"],
            "dataview_enabled": True
        })
    except ImportError:
        pass

    # 2. 写入 JSON 数据源给 Hugo
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)
    json_path = os.path.join(data_dir, "hackernews.json")
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    print(f"✅ Hacker News JSON 数据(Points降序)已同步至: {json_path}")

if __name__ == "__main__":
    generate_markdown()
