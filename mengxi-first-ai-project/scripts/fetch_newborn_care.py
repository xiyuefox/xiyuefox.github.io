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
MEDICAL_RSS_MATRIX = {
    "🔬 循证医学与前沿儿科": [
        "https://www.healthychildren.org/_layouts/15/syndication.ashx",  # AAP 美国儿科学会
        "https://parentingscience.com/feed/",                            # Parenting Science
    ],
    "🏥 本地权威与实操 S.O.P": [
        "https://www.janetlansbury.com/feed/",                           # Janet Lansbury (RIE 育儿)
        "https://www.mayoclinic.org/rss/all-tips-headlines",              # 修正拼写：Mayo Clinic
    ],
    "🧠 脑神经与心理成长": [
         "https://digest.bps.org.uk/category/developmental/feed/",        # BPS Research Digest
    ]
}

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_PATH = os.path.join(PROJECT_DIR, "posts", "md", "newborn-care-feed.md") 
MAX_ENTRIES_PER_FEED = 10

def summarize_with_gemini(title, summary_text):
    """使用 Gemini 进行医学脱水提纯。"""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
         return ""
         
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
        headers = {'Content-Type': 'application/json'}
        prompt = f"""你现在是一位拥有 20 年三甲医院临床经验的儿科主任兼极简主义者。请对这段资讯进行医疗级脱水。
文章标题: {title}
文章内容: {summary_text}

过滤规则：
1. 自动屏蔽任何无现代医学/生物学数据支撑的偏方或焦虑营销。如果整篇笔记毫无科学依据，请直接返回‘⚠️ 该内容缺乏循证医学支持，已过滤’。
2. 重点提取与【新生儿与0-1岁婴儿护理】高度相关的可量化操作（如：具体温度、毫升数、喂养间隔时间），并仔细提取适合 0-1岁 婴儿的任何护理类互动游戏。
3. 将提取内容转化为结构化的【月嫂交接 S.O.P】或【避坑 CheckList】。
4. 使用无序列表 - 输出，每条控制在 30 字以内，语言必须极度冷峻、精确。如果涉及英文文献，请翻译为专业中文。绝对不要感叹号和废话。
"""
        import inference_helper
        return inference_helper.ask_llm(prompt)
    except Exception as e:
         print(f"   ⚠️ Gemini/Mistral 摘要异常: {e}")
    return ""

def main():
    print("=== 🌟 开始拉取新生儿权威护理与医疗级脱水 S.O.P ===")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    cards_md = []
    
    for category, urls in MEDICAL_RSS_MATRIX.items():
        cards_md.append(f"\n## {category}\n")
        for url in urls:
            print(f"📡 正在拉取 RSS: {url}")
            try:
                res = requests.get(url, headers=headers, timeout=20, verify=False)
                if res.status_code != 200:
                    print(f"   HTTP 异常: {res.status_code}")
                    continue
                    
                feed = feedparser.parse(res.text)
                author = feed.feed.title if hasattr(feed, 'feed') and hasattr(feed.feed, 'title') else url
                cards_md.append(f"\n### 📡 来源: {author}\n")
                
                entries_count = 0
                for entry in feed.entries:
                    if entries_count >= MAX_ENTRIES_PER_FEED:
                        break
                    
                    title = entry.get("title", "未命名文章")
                    link = entry.get("link", "#")
                    summary_text = entry.get("summary", entry.get("description", ""))
                    clean_content = re.sub('<[^>]*>', '', summary_text).strip()
                    
                    # 格式化发布时间
                    pub_date = entry.get('published', '') or entry.get('updated', '')
                    if not pub_date and 'published_parsed' in entry and entry.published_parsed:
                        pub_date = datetime(*entry.published_parsed[:6]).strftime("%Y-%m-%d")
                    elif pub_date:
                        pub_date = pub_date[:10]  # 只取到日期
                    else:
                        pub_date = datetime.now().strftime("%Y-%m-%d")

                    print(f"👉 详情拉取 [{title[:15]}...]")
                    print(f"🧠 AI 医疗提炼中...")
                    summary = summarize_with_gemini(title, clean_content)
                    time.sleep(1)
                    
                    md_card = f"""
#### [{title}]({link})
> **⚕️ 医疗级提炼 (S.O.P) | ⏰ 发布时间: {pub_date}**
{summary.strip() if summary else '（总结未生成，具体请查阅原帖）'}

<details>
<summary>📂 查看原始卷宗 (Raw Data)</summary>

{clean_content[:400] + ("..." if len(clean_content) > 400 else "")}

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
title: "👶 新生儿权威护理与医学级 S.O.P"
date: {today}
tags: ["Newborn", "SOP", "Science", "SIDS"]
category: "obsidian"
badge: "医疗级脱水"
---

这里汇集了由 AAP、哈佛大学儿童发展中心及国内循证医学专栏生成的 **医疗级新生儿护理 S.O.P**。自动过滤任何营销与伪科学，专注于 52 天周期内的量化指标与避坑校验。

---

{''.join(cards_md)}
"""

    os.makedirs(os.path.dirname(MD_PATH), exist_ok=True)
    with open(MD_PATH, 'w', encoding='utf-8') as f:
        f.write(final_output)
        
    print(f"\n✅ 成功建立并覆盖了医疗级反馈文档: {MD_PATH}")
    
    # 获取第一篇或者最新的文章标题进行首页更新
    try:
        if os.path.exists(MD_PATH):
             with open(MD_PATH, 'r', encoding='utf-8') as f:
                  m_content = f.read()
                  
                  summary_source_text = m_content[:6000]
                  
                  title_match = re.search(r'#### \[(.*?)\]', m_content)
                  latest_title = title_match.group(1).strip() if title_match else "近期新生儿护理 S.O.P"
                  
                  update_index_html_card(latest_title, summary_source_text)
    except Exception as e:
         print(f"⚠️ 刷新首页卡片异常: {e}")

def update_index_html_card(latest_entry_title, generated_summary_text):
    """同步更新 index.html 上的新生儿卡片描述，实现自动化接入首页更新提示"""
    index_path = "/Users/hulimofaqiu/mengxi-first-ai-project/index.html"
    if not os.path.exists(index_path):
        return
        
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 匹配对应的卡片 href 和 description
    pattern = r'(<a href="post.html\?post=newborn-care-feed"[^>]*>(?:(?!</a>).)*?<p class="tg-card-desc">)(.*?)(</p>)'
    
    def repl_desc(match):
        prefix = match.group(1)
        today = datetime.now().strftime("%Y-%m-%d")
        new_desc = f"🎯 最新 AI 护理提炼: {latest_entry_title} (同步 {today})"
        return prefix + new_desc + match.group(3)
        
    new_content, count = re.subn(pattern, repl_desc, content, flags=re.DOTALL)
    
    # 同样更新 expandable-summary
    sm_pattern = r'(<a href="post.html\?post=newborn-care-feed"[^>]*>.*?<div class="expandable-summary"[^>]*>\s*<ul[^>]*>)(.*?)(</ul>\s*</div>)'
    
    api_key = os.environ.get("GEMINI_API_KEY")
    summary_li_html = ""
    if api_key and generated_summary_text:
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
            prompt = f"请根据以下今日抓取的0-1岁新生儿护理与医疗SOP内容，总结出 4 条核心干货。只输出 4 个 <li>...</li> HTML 标签，里面用带 <strong> 的加粗标题跟简短解释，重点点出护理数据和互动游戏，不要任何 markdown 引用或外层 <ul> 包裹！\n\n内容库:\n{generated_summary_text[:4000]}"
            res = requests.post(url, headers={'Content-Type': 'application/json'}, json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=15)
            if res.status_code == 200:
                summary_li_html = res.json().get('candidates', [{}])[0].get('content', {}).get('parts', [])[0].get('text', '').strip()
                summary_li_html = summary_li_html.replace('```html', '').replace('```', '').strip()
            else:
                print(f"⚠️ API请求失败状态码: {res.status_code}, 返回: {res.text}")
        except Exception as e:
            print(f"⚠️ 生成主页摘要时失败: {e}")
            
    if summary_li_html:
        def repl_sm(match):
            return match.group(1) + "\n" + summary_li_html + "\n                             " + match.group(3)
        new_content, count2 = re.subn(sm_pattern, repl_sm, new_content, flags=re.DOTALL)
        if count2 > 0:
            print("✅ index.html 主页新生儿护理 summary 生成并同步更新成功。")
        else:
            print("⚠️ 未能在 index.html 中匹配到 newborn-care-feed 的 expandable-summary")
            
    if count > 0:
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✅ index.html 首页卡片标题同步更新成功。")
    else:
        print("⚠️ 未能在 index.html 中匹配到卡片描述，跳过首页更新。")

if __name__ == "__main__":
    main()
