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

# 爬虫/RSS源配置
FEEDS = {
    "Raspberry Pi Blog": "https://www.raspberrypi.org/feed/",
    "Make: Magazine": "https://makezine.com/feed/",
    "Montessori From The Heart": "https://montessorifromtheheart.com/feed/"
}

def summarize_with_gemini(title, content):
    """根据定制的 Prompt 调用 Gemini API 提炼摘要"""
    if not GEMINI_API_KEY:
        return "❌ 没找到 GEMINI_API_KEY 环境变量，无法生成 AI 摘要。"

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {'Content-Type': 'application/json'}

    prompt = f"""
你是一个专属的内容策展人。你的受众是一位拥有建筑学背景、即将成为新手妈妈的创客老师。
请阅读这篇文章，并以 Markdown 格式输出不超过 300 字的中文摘要。

摘要必须包含且严格按照以下结构输出：
💡 **核心亮点**：用一句话总结这篇文章最有价值的信息。

🛠️ **创客/教学灵感**（如果文章相关）：这个项目/概念可以如何融入“未来城市或空间设计”的儿童创客课程中？（若无关则写“暂无直接创客灵感，但有...启发”）

🍼 **育儿/生活启发**（如果文章相关）：这对新手妈妈或家庭管理有什么可以借用的思路？（若无关则写“暂无直接育儿启发，但有...启发”）

---
文章内容：
标题: {title}
内容: {content[:3000]}  # 截取前3000字防止超出 token 限制
"""

    try:
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        res = requests.post(url, headers=headers, json=payload, timeout=20)
        if res.status_code == 200:
            data = res.json()
            parts = data.get('candidates', [{}])[0].get('content', {}).get('parts', [])
            if parts:
                return parts[0].get('text', '').strip()
    except Exception as e:
        return f"⚠️ API 调用发生异常: {e}"
        
    return "⚠️ AI 未能正常返回内容。"

def main():
    print("🚀 启动 创客与育儿 AI 摘要自动收集引擎...")
    if not os.path.exists(OBSIDIAN_VAULT):
        print(f"❌ 警告: 未能找到 Obsidian 目录 {OBSIDIAN_VAULT}，将在本地保存。")
        out_dir = os.path.join(PROJECT_DIR, "posts", "ai-summaries")
    else:
        out_dir = os.path.join(OBSIDIAN_VAULT, "00-Inbox", "AI摘要汇总") # 指定保存到 Inbox/AI摘要汇总
        
    os.makedirs(out_dir, exist_ok=True)
    today_str = datetime.now().strftime("%Y-%m-%d")
    md_filename = os.path.join(out_dir, f"AI-Summary-{today_str}.md")

    output_lines = [
        f"---",
        f"title: \"创客与育儿每日 AI 摘要 (Curated)\"",
        f"date: {today_str}",
        f"tags: [AI-Summary, Maker, Parenting]",
        f"---",
        f"\n# 💡 创客与育儿每日 AI 摘要\n"
    ]

    count = 0
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
    }
    for name, url in FEEDS.items():
        print(f"📡 正在拉取 [{name}] 订阅源: {url}...")
        try:
            res = requests.get(url, headers=headers, timeout=15, verify=False)
            if res.status_code != 200:
                print(f"⚠️ [{name}] 状态码异常: {res.status_code}")
                continue
                
            feed = feedparser.parse(res.text)
            if not feed.entries:
                print(f"⚠️ [{name}] RSS 解析为空，跳过。")
                continue

            # 每个源只提炼最新的 1 篇进行快速测试聚合
            entry = feed.entries[0]
            title = entry.get('title', '无标题')
            link = entry.get('link', '#')
            content = entry.get('summary', entry.get('description', ''))
            
            # 去除 HTML tag
            clean_content = re.sub('<[^>]*>', '', content).strip()
            
            print(f"🤖 正在调用 Gemini 摘要核心: {title[:25]}...")
            summary = summarize_with_gemini(title, clean_content)
            
            output_lines.append(f"## [{title}]({link})")
            output_lines.append(f"> **📰 来源: {name}**\n")
            output_lines.append(f"{summary}\n")
            output_lines.append(f"---\n")
            count += 1
            
        except Exception as e:
            print(f"❌ 处理 [{name}] 失败: {e}")

    if count > 0:
        with open(md_filename, 'w', encoding='utf-8') as f:
            f.write("\n".join(output_lines))
        print(f"✅ 成功写入 Obsidian 归档: {md_filename}")
    else:
        print("⚠️ 未拉取到有效提炼，跳过写入。")

if __name__ == "__main__":
    main()
