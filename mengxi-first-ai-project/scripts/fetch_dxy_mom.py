import feedparser
import json
import os
import re
from datetime import datetime

import requests

# 配置
# Kindle4RSS 的 DingXiangMaMi 路由
RSS_URL = "http://feedmaker.kindle4rss.com/feeds/DingXiangMaMi.weixin.xml"
TARGET_DIR = "posts/md"
FILE_PATH = os.path.join(TARGET_DIR, "dxy-mom-feed.md")

def summarize_dxy_with_gemini(summary_text):
    """根据丁香妈妈文章的截击摘要，提炼 3 个核心科普避坑点。"""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return ""
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
        headers = {'Content-Type': 'application/json'}
        prompt = f"""请作为硬核儿科与孕产护理专家，帮我从以下丁香妈妈文章的科普摘要中，极其精炼地提取出 3 个最核心的【科普卡点、选购要点或避坑要点】。
用极其简明、结构化的 123 列表呈现，不要废话，直接开始列表：

{summary_text}
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
        print(f"   ⚠️ Dxy Gemini 摘要异常: {e}")
    return ""

def fetch_dxy_mom():
    print("🔄 正在拉取 丁香妈妈 微信 RSS 内容...")
    try:
        # 1. 解析 RSS
        feed = feedparser.parse(RSS_URL)
        items = feed.entries[:5] # 掐取最新的 5 篇
        
        if not items:
            print("⚠️ 未拉取到丁香妈妈最新的 RSS 节点数据。")
            return

        today_str = datetime.now().strftime("%Y-%m-%d")
        md_content = f"""# 🍼 丁香妈妈 科普热点追踪

> [!TIP]
> 这是一个基于微信公开流自动渲染的板块，旨在提供落地、避坑的孕晚期 & 新生儿科普信息。

---

"""
        json_data = []

        for entry in items:
            title = entry.get('title', '无标题')
            link = entry.get('link', '#')
            published = entry.get('published', '') # e.g., "Sun, 15 Mar 2026 12:00:00 GMT"
            summary = entry.get('description', '') or entry.get('summary', '')

            # 纯文本化处理 summary，防止 HTML 嵌套导致卡片变形
            clean_summary = re.sub('<[^>]*>', '', summary)
            clean_summary = clean_summary.replace('&quot;', '"').replace('&#x27;', "'").replace('&amp;', '&')
            
            if len(clean_summary) > 200:
                clean_summary = clean_summary[:200] + "..."

            # 格式化日期：有些发布时间不规范，直接截取或留空
            post_date = published[:16] if published else today_str

            # 🪐 调用 Gemini 提炼核心提点
            print(f"      💡 正在由 AI 提炼科普要点: {title[:20]}...")
            ai_insight = summarize_dxy_with_gemini(clean_summary)
            # 给 AI 的答案换行加上 blockquote 前缀
            ai_insight_formatted = ai_insight.replace('\n', '\n    > ') if ai_insight else ""
            summary_formatted = f"\n*   💡 **AI 科普提要**：\n    > {ai_insight_formatted}\n" if ai_insight else ""

            md_content += f"""### 📌 [{title}]({link})
*   **发布时间**：📅 `{post_date}`
*   **内容摘要**：
    > {clean_summary.strip()}
{summary_formatted}
[🌐 点击阅读微信原作全篇 ➡️]({link})

"""
            json_data.append({
                "url": link,
                "date": post_date[:10], # 精确到日
                "title": title,
                "summary": clean_summary.strip(),
                "author": "丁香妈妈",
                "tags": ["dxy_mom"],
                "points": 9999 # 给个极高 Points 假卡，或者前台根据 tags 判定
            })

        # 1. 写入 Markdown 文件
        if not os.path.exists(TARGET_DIR):
            os.makedirs(TARGET_DIR, exist_ok=True)
        with open(FILE_PATH, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"✅ 丁香妈妈抗辩指南 Markdown看板已生成: {FILE_PATH}")

        # 自动化注入 YAML Frontmatter (Dataview 联动支持)
        try:
            from utils import append_frontmatter
            append_frontmatter(FILE_PATH, {
                "title": "🥣 丁香妈妈 孕育指南速递 (自动更新)",
                "date": today_str,
                "category": ["Parenting"],
                "tags": ["Parenting", "Nutrition", "Automated"],
                "dataview_enabled": True
            })
        except ImportError:
            pass

        # 2. 写入 JSON 数据源给 Hugo
        data_dir = "data"
        os.makedirs(data_dir, exist_ok=True)
        json_path = os.path.join(data_dir, "dxy_mom.json")
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)
        print(f"✅ 丁香妈妈 JSON 数据已同步至: {json_path}")
        
        # 3. 更新 index.html 上的卡片摘要
        if json_data:
            update_index_html(json_data)

    except Exception as e:
        print(f"❌ 丁香妈妈 RSS 抓取失败: {e}")

def update_index_html(json_data):
    """自动将最新 2 篇丁香妈妈标题或内容融入首页卡片摘要"""
    index_path = "/Users/hulimofaqiu/mengxi-first-ai-project/index.html"
    if not os.path.exists(index_path):
        return

    today_str = datetime.now().strftime("%Y-%m-%d")
    top_entries = [item['title'] for item in json_data[:2]]
    new_desc = f"🎯 最新看板: {', '.join(top_entries)} (同步 {today_str})"

    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 首先尝试更精确的匹配：基于卡片元素周围的特征
    pattern = r'(<h3 class="tg-card-title">🥣 丁香妈妈 孕育指南速递 \(自动更新\)</h3>\s*<p class="tg-card-desc">)(.*?)(</p>)'
    
    if re.search(pattern, content):
        content = re.sub(pattern, r'\g<1>' + new_desc + r'\g<3>', content)
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ index.html 丁香妈妈看板 摘要同步更新成功。")
    else:
        print("⚠️ 未能在 index.html 中匹配到 🥣 丁香妈妈 卡片描述，跳过首页更新。")

if __name__ == "__main__":
    fetch_dxy_mom()
