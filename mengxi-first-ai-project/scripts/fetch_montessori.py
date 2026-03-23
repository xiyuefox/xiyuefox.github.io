import os
import requests
import feedparser
import re
from datetime import datetime
import json
import urllib3

# 抑制不安全请求警告（针对某些 SSL 证书异常）
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

# 配置区域
RSS_URLS = [
    "https://www.howwemontessori.com/how-we-montessori/atom.xml",
    "https://www.thekavanaughreport.com/feeds/posts/default?alt=rss",  # The Kavanaugh Report
    "https://www.montessoriinreallife.com/home?format=rss",            # Montessori in Real Life
    "https://www.mariamontessori.com/feed/",                            # Maria Montessori
    "https://aidataballet.com/feed/"                                   # Aida Montessori 
]
# 写入静态站目录的路径 (用于 post.html?post= 渲染)
TARGET_DIR = "posts/md"
TARGET_FILE = os.path.join(TARGET_DIR, "meng-shi-0-1-sui-nido-jia-ting-fang-an-zi-dong-hua-tong-bu.md")

def summarize_with_gemini(title, summary_text, author="Unknown"):
    """使用 Gemini 提炼符合蒙氏 0-1 岁要求的核心干货，输出严格模板卡片。"""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("   ⚠️ 未找到 GEMINI_API_KEY 环境变量，跳过 AI 提炼。")
        return ""
        
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
        headers = {'Content-Type': 'application/json'}
        prompt = f"""# Role
你是一个运行在自动化工作流中的后台极客育儿内容解析引擎。你的任务是接收 0-1岁蒙台梭利（Nido阶段）的 RSS 图文或 API 纯文本输入（可能包含 Hacker News 极客论坛的评论），过滤冗杂信息，并将其重构为极其严谨、具有认知启发价值的格式。

# Processing Rules (核心多维评估逻辑)
接收到内容后，必须经过以下过滤与提炼：
1. **发育里程碑匹配**：甄别内容是否符合 0-1 岁婴儿的真实发展规律。
2. **0-1岁游戏提炼 (极度关键)**：必须仔细提取适合 0-1 岁婴儿的【具体游戏方式或互动道具】，尤其是能促进认知的小动作。
3. **前数学与逻辑启蒙 (Pre-Math & Logic)**：像雷达一样扫描文中涉及“客体永久性 (Object Permanence)”、“因果关系推导”、“几何/拓扑空间感知”及“大小递进规律”的教具或互动。将这些视为婴儿专属的“数学解谜”项目进行重点提取。
4. **空间折叠率**：评估方案在紧凑型住宅中的可行性。优先提取一物多用、不占核心动线的布置灵感。

# Output Protocol (严格双语卡片输出协议)
请仅仅输出以下段落的内容格式，不要任何问候语。

📌 **核心观点 (Core Idea)**: [中文极简观点作为标题] | [English core title]
ℹ️ **信息源 (Source)**: {author} | 🌟 推荐 [1-100] | 💡 实用 [1-100]

🧠 **干货总结 (Bilingual Insight)**:
  - 🇨🇳 **中文**: [总结适合0-1岁的具体游戏/互动方案。必须点明婴儿期背后的“前数学/认知神经规律”或小游戏具体做法。]
  - 🇬🇧 **English**: [Dense and summary for global accessiblity / core milestone]

🏷️ **细分标签 (Tags)**: #[精准细分标签，如 #0到1岁游戏 #前数学推理 #客体永久性投币盒 #省空间]

文章标题: {title}
文章内容: {summary_text}
"""
        import inference_helper
        return inference_helper.ask_llm(prompt)
    except Exception as e:
        print(f"   ⚠️ Gemini/Mistral 摘要提炼异常: {e}")
    return ""

def generate_full_markdown():
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"🔄 开启自动化拉取蒙氏家庭方案... (日期: {today})")
    
    # 基础 Markdown 框架
    md_content = f"""---
title: "蒙氏 0-1岁 Nido 家庭方案 (自动化同步)"
tags: ["Montessori", "Nido", "育儿", "自动化"]
---
{today}
📚
obsidian
[Parenting/yuji]
#Montessori
#Nido
#Automated
📌 蒙氏 0-1岁 Nido 家庭方案与认知启蒙
📝
CAUTION
列表项已按照【逻辑启蒙价值/空间实用度】智能排序。

"""

    has_content = False
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    collected_entries = []
    for r_url in RSS_URLS:
        print(f"   --> 抓取源: {r_url}")
        try:
            # 采用 requests 获取，规避部分 feedparser 异常
            res = requests.get(r_url, headers=headers, timeout=10, verify=False)
            if res.status_code == 200:
                 feed = feedparser.parse(res.text)
                 if hasattr(feed, 'entries') and feed.entries:
                     for entry in feed.entries[:15]: # 增加至15条进行过滤
                        title = entry.get('title', '无标题')
                        clean_summary = re.sub('<[^>]*>', '', entry.get('description', '') or entry.get('summary', ''))
                        
                        # 格式化时间
                        pub_date = entry.get('published', '') or entry.get('updated', '')
                        if not pub_date and 'published_parsed' in entry and entry.published_parsed:
                            pub_date = datetime(*entry.published_parsed[:6]).strftime("%Y-%m-%d")
                        elif pub_date:
                            pub_date = pub_date[:16] # 截取更精简
                        
                        # 过滤非 Nido 阶段 (0-1岁) 的关键字
                        blacklisted_keywords = ["toddler", "3 years", "4 years", "5 years", "elementary", "school", "preschool"]
                        is_blacklisted = any(kw in title.lower() or kw in clean_summary.lower() for kw in blacklisted_keywords)
                        if is_blacklisted:
                            print(f"      🚫 过滤非 Nido 阶段内容: {title[:15]}")
                            continue

                        collected_entries.append({
                            "title": title,
                            "summary": clean_summary.strip(),
                            "author": feed.feed.get('title', 'Montessori Blog'),
                            "link": entry.get('link', r_url),
                            "date": pub_date or today
                        })
                        has_content = True
        except Exception as e:
            print(f"   ❌ 抓取源 {r_url} 异常: {e}")

    # 1b. Fetch Hacker News (via Algolia API)
    print("   --> 抓取源: Hacker News (Algolia API)")
    try:
        # 使用更具极客风格的育儿/监控词组，结合蒙氏
        hn_query = 'montessori OR "baby monitor" OR "smart nursery" OR "baby tracker"'
        hn_res = requests.get(f"https://hn.algolia.com/api/v1/search?query={hn_query}&tags=story", timeout=10)
        if hn_res.status_code == 200:
            hn_data = hn_res.json()
            hits = hn_data.get('hits', [])
            for hit in hits[:5]: # 最新5条相关讨论
                title = hit.get('title', '无标题')
                story_text = hit.get('story_text', '') or hit.get('url', '')
                # 格式化 HN 时间
                hn_time = hit.get('created_at', '')[:10] if 'created_at' in hit else today
                
                collected_entries.append({
                    "title": title,
                    "summary": f"{story_text}\n(讨论链接: https://news.ycombinator.com/item?id={hit.get('objectID')})",
                    "author": "Hacker News",
                    "link": hit.get('url') or f"https://news.ycombinator.com/item?id={hit.get('objectID')}",
                    "date": hn_time
                })
                has_content = True
    except Exception as e:
        print(f"   ❌ 抓取 Hacker News 异常: {e}")

    # 给出一个备用的兜底方案，如果网络403无法拉取，记录异常信息而不是空白
    if not has_content:
        print("   ⚠️ 网络访问限制无法获取到实时 RSS 数据，暂时使用科学教具知识库汇总。")
        md_content += """
📌 【视觉追踪】蒙氏视觉吊饰 Munari/Octahedron 制作图解
发布者：How We Montessori (备用缓存)
热度/推荐指数：🌟 推荐 5/5 | 👍 实用 5/5 
💡 核心干货总结：Munari（黑白球）与 Octahedron（彩色八面体）分段刺激专注力。完全适合低成本 DIY 制作，常逛闲鱼打包收二手框架。
命中标签：#视觉吊饰 #低成本DIY #二手好物 
🌐 点击直达阅读 full page ➡️ https://www.howwemontessori.com/how-we-montessori/2012/03/montessori-infant-mobiles.html

---

📌 【环境布置】蒙氏婴儿房“地板床 (Floor Bed)”与安全Yes Space
发布者：The Kavanaugh Report (备用缓存)
热度/推荐指数：🌟 推荐 4.5/5 | 👍 实用 4/5 
💡 核心干货总结：落地床垫打破束缚，赋予婴儿清醒时自主权。床架建议略过或淘二手宜家童床垫，省下预算给插座防夹安全件。
命中标签：#地板床 #空间利用率 #居家安全 
🌐 点击直达阅读 full page ➡️ https://www.thekavanaughreport.com/2015/07/montessori-floor-bed-baby-proofing.html
"""
    else:
        # 如果成功抓取到了动态内容，进行 AI 汇总
        for entry in collected_entries:
            print(f"      💡 正在由 AI 提炼干货: {entry['title'][:20]}...")
            summary_txt = summarize_with_gemini(entry['title'], entry['summary'], author=entry['author'])
            if not summary_txt:
                summary_txt = f"📌 {entry['title']}\n🧠 婴儿解谜与干货总结：{entry['summary'][:100]}..." # 兜底摘要
                
            md_content += f"""{summary_txt}
⏰ **发布日期 (Published)**: {entry.get('date', '未知')}
🌐 点击直达 full page ➡️ {entry['link']}

---

"""

    # 写入文件
    target_dir = os.path.dirname(TARGET_FILE)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)
        
    with open(TARGET_FILE, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"✅ 蒙氏方案集 Markdown 看板已刷新并写入: {TARGET_FILE}")

def update_index_html_card(latest_entry_title, generated_summary_text):
    """同步更新 index.html 上的蒙氏卡片描述，实现自动化接入首页更新提示"""
    index_path = "/Users/hulimofaqiu/mengxi-first-ai-project/index.html"
    if not os.path.exists(index_path):
        return
        
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 替换主卡片描述
    pattern = r'(<a href="post.html\?post=meng-shi-0-1-sui-nido-jia-ting-fang-an-zi-dong-hua-tong-bu"[^>]*>(?:(?!</a>).)*?<p class="tg-card-desc">)(.*?)(</p>)'
    def repl_desc(match):
        prefix = match.group(1)
        today = datetime.now().strftime("%Y-%m-%d")
        new_desc = f"🎯 最新方案与0-1岁游戏: {latest_entry_title} (同步 {today})"
        return prefix + new_desc + match.group(3)
        
    new_content, count = re.subn(pattern, repl_desc, content, flags=re.DOTALL)
    
    # 替换 expandable-summary 中的 ul 内容
    # 定位到这个卡片的 expandable-summary ul，由于我们在卡片里，用特异性强的正则
    summary_pattern = r'(<a href="post.html\?post=meng-shi-0-1-sui-nido-jia-ting-fang-an-zi-dong-hua-tong-bu"[^>]*>.*?<div class="expandable-summary"[^>]*>\s*<ul[^>]*>)(.*?)(</ul>\s*</div>)'
    
    # 我们用 AI 生成四个 li: summary_li_html
    api_key = os.environ.get("GEMINI_API_KEY")
    summary_li_html = ""
    if api_key and generated_summary_text:
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
            prompt = f"请根据以下今日抓取的0-1岁蒙氏与游戏内容，总结出 4 条核心干货（特别关注适合0-1岁婴儿的具体游戏和前数学启蒙尝试）。只输出 4 个 <li>...</li> HTML 标签，里面用带 <strong> 的加粗标题跟简短解释，不要任何 markdown 引用或外层 <ul> 包裹！\n\n内容库:\n{generated_summary_text[:4000]}"
            res = requests.post(url, headers={'Content-Type': 'application/json'}, json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=15)
            if res.status_code == 200:
                summary_li_html = res.json().get('candidates', [{}])[0].get('content', {}).get('parts', [])[0].get('text', '').strip()
                summary_li_html = summary_li_html.replace('```html', '').replace('```', '').strip()
        except Exception as e:
            print(f"⚠️ 生成主页摘要时失败: {e}")
            
    if summary_li_html:
        def repl_summary(match):
            return match.group(1) + "\n" + summary_li_html + "\n                             " + match.group(3)
        new_content, count2 = re.subn(summary_pattern, repl_summary, new_content, flags=re.DOTALL)
        if count2 > 0:
            print("✅ index.html 主页蒙氏游戏与要点 summary 生成并同步更新成功。")
            
    if count > 0:
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✅ index.html 首页卡片标题同步更新成功。")
    else:
        print("⚠️ 未能在 index.html 中匹配到卡片描述，跳过首页更新。")

if __name__ == "__main__":
    generate_full_markdown()
    
    try:
        # 读取刚刚更新渲染出的文件，并在首页进行 description 打包摘要
        if os.path.exists(TARGET_FILE):
             with open(TARGET_FILE, 'r', encoding='utf-8') as f:
                  m_content = f.read()
                  
                  # 截取全部或部分文本以供 AI 总结（提取前5000字，避免超出 Gemini 短上下文，其实flash支持很长但为了快）
                  summary_source_text = m_content[:6000]
                  
                  # 获取文章列表中的第一篇（即最新一篇）作为副标题
                  title_match = re.search(r'📌 (.*?)\n', m_content)
                  latest_title = title_match.group(1).strip() if title_match else "近期蒙氏与0-1岁数学启蒙合集"
                  
                  update_index_html_card(latest_title, summary_source_text)
    except Exception as e:
        print(f"⚠️ 刷新首页卡片异常: {e}")
