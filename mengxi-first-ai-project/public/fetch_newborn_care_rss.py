import os
import requests
import feedparser
import re
from datetime import datetime
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 配置区域：国外/国内顶级科学育儿 RSS
RSS_URLS = [
    # 🌟 循证医学与新生儿护理
    "https://www.healthychildren.org/_layouts/15/syndication.ashx",  # AAP 美国儿科学会
    "https://rsshub.app/zhihu/people/distinct-clinic/answers",       # 卓正医疗
    "https://parentingscience.com/feed/",                            # Parenting Science
    "https://evidencebasedbirth.com/feed/",                          # Evidence Based Birth
    "https://www.janetlansbury.com/feed/",                           # Janet Lansbury (RIE 育儿)
    
    # 🌿 蒙台梭利居家与早期启蒙
    "http://www.howwemontessori.com/how-we-montessori/rss.xml",
    "http://www.thekavanaughreport.com/feeds/posts/default?alt=rss",
    
    # 🧠 脑神经科学与早期发育 (Neuroscience & Growth)
    "https://digest.bps.org.uk/category/developmental/feed/",        # BPS Research Digest
    "https://api.quantamagazine.org/feed/biology/",                  # Quanta Magazine (Biology)
    
    # 📦 国内高赞待产与硬核经验 (Zhihu via RSSHub)
    "https://rsshub.app/zhihu/topic/19555513/top-answers"
]

TARGET_DIR = "posts/md"
TARGET_FILE = os.path.join(TARGET_DIR, "newborn-care-feed.md")

def summarize_with_gemini(title, summary_text):
    """使用 Gemini 提炼科学育儿与新生儿护理干货。"""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return ""
        
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
        headers = {'Content-Type': 'application/json'}
        prompt = f"""请作为权威的三甲医院儿科学专家、新生儿护理顾问或脑发育研究员。帮助我从以下文章提炼出核心干货。
文章标题: {title}
文章摘要: {summary_text}

请极其精准地精炼出一句【核心干货总结】，要求如下：
1. 聚焦于 0-1岁 新生儿护理（喂养、睡眠、湿疹等）或 脑发育、认知心理 的科学实操。
2. 提亮该方案是否具备【循证医学(Evidence-Based)】、【蒙氏理论】或【神经科学依据】。
3. 如果原文涉及脑神经科学或认知发育，请聚焦于**底层机制（如神经可塑性、感觉剥夺等）**，并剥离复杂的学术名词，转化为对家长**实用的早教/心理引导 S.O.P**。
4. 如果原文是英文，请直接将提取出的核心 S.O.P 指南和所需物品清单翻译为**简洁流畅的中文**。
5. 避免废话、废标点，总结在一到两句话内：
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
        print(f"   ⚠️ Gemini 摘要提炼异常: {e}")
    return ""

def generate_full_markdown():
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"🔄 开启自动化拉取科学育儿与新生儿权威护理指南... (日期: {today})")
    
    md_content = f"""---
title: "科学育儿与新生儿权威护理指南"
tags: ["Newborn", "Science", "育儿", "RSS"]
category: "obsidian"
badge: "权威医疗"
---

这里汇聚了来自 **AAP (美国儿科学会)**、**卓正医疗**、**Evidence-Based Birth**、**蒙特梭利**等顶级科学/循证医学育儿专栏的最新资讯。动态脱水提炼，杜绝营销和偏方，给新生儿最安全的落地呵护。

---

"""

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    collected_entries = []
    has_content = False

    for r_url in RSS_URLS:
        print(f"   --> 抓取源: {r_url}")
        try:
            res = requests.get(r_url, headers=headers, timeout=12, verify=False)
            if res.status_code == 200:
                 feed = feedparser.parse(res.text)
                 if hasattr(feed, 'entries') and feed.entries:
                     for entry in feed.entries[:3]: 
                         title = entry.get('title', '无标题')
                         clean_summary = re.sub('<[^>]*>', '', entry.get('description', '') or entry.get('summary', ''))
                         collected_entries.append({
                             "title": title,
                             "summary": clean_summary.strip(),
                             "author": feed.feed.get('title', 'Authoritative Expert'),
                             "link": entry.get('link', r_url)
                         })
                         has_content = True
        except Exception as e:
            print(f"   ❌ 抓取源 {r_url} 异常: {e}")

    if not has_content:
         md_content += "\n> 👶 暂未接入最新的实时科学育儿看板，请稍后刷新重试。\n"
    else:
        for entry in collected_entries:
            print(f"      💡 正在由 AI 提炼干货: {entry['title'][:20]}...")
            summary_txt = summarize_with_gemini(entry['title'], entry['summary'])
            if not summary_txt:
                summary_txt = f"{entry['summary'][:100]}..."

            md_content += f"""📌 {entry['title']}
发布者：{entry['author']}
热度/推荐指数：🌟 推荐 5/5 | 👍 循证科学 5/5 
💡 核心干货总结：{summary_txt}
命中标签：#新生儿护理 #循证医学 #科学育儿 
🌐 点击直达阅读 full page ➡️ {entry['link']}

---

"""

    target_dir = os.path.dirname(TARGET_FILE)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)
        
    with open(TARGET_FILE, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"✅ 新生儿护理 Markdown 看板已刷新并写入: {TARGET_FILE}")

def update_index_html_card(latest_entry_title):
    index_path = "/Users/hulimofaqiu/mengxi-first-ai-project/index.html"
    if not os.path.exists(index_path):
        return
        
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 使用 (?:(?!</a>).)*? 确保匹配不跨越 </a> 边界，防止在 re.DOTALL 下贪婪跨卡片匹配
    pattern = r'(<a href="post.html\?post=newborn-care-feed"[^>]*>(?:(?!</a>).)*?<p class="tg-card-desc">)(.*?)(</p>)'
    
    def repl(match):
        prefix = match.group(1)
        today = datetime.now().strftime("%Y-%m-%d")
        new_desc = f"🛡️ 最新循证指南: {latest_entry_title} (同步 {today})"
        return prefix + new_desc + match.group(3)
        
    new_content, count = re.subn(pattern, repl, content, flags=re.DOTALL)
    if count > 0:
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✅ index.html 首页卡片摘要同步更新成功。")

if __name__ == "__main__":
    generate_full_markdown()
    
    try:
        if os.path.exists(TARGET_FILE):
             with open(TARGET_FILE, 'r', encoding='utf-8') as f:
                  m_content = f.read()
                  title_match = re.search(r'📌 (.*?)\n', m_content)
                  if title_match:
                       latest_title = title_match.group(1).strip()
                       update_index_html_card(latest_title)
    except Exception as e:
        print(f"⚠️ 刷新首页卡片异常: {e}")
