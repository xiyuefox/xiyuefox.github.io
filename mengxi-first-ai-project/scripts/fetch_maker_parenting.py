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

    prompt = f"""你现在不仅仅是一个内容策展人，你是一位极具幽默感、拥有硬核建筑学背景且充满极客精神的创客妈妈。请阅读这篇文章，并输出不超过 300 字的中文摘要。

在撰写时，你必须严格遵守以下“趣味性”原则：
1. **拒绝废话与平庸**：不要写“正确的废话”。请专门提取文章中最反直觉、最硬核或最让人“哇哦”的细节（追求极高的 Information Gain）。
2. **注入极客与生活之盐**：在总结“创客灵感”或“育儿启发”时，请使用生动、接地气的语言。可以适度带一点幽默的调侃，或者融入一些建筑设计、科幻或树莓派的小众梗，让文字充满温度和生命力。
3. **自我批评 (Self-Criticism)**：在输出最终结果前，请在内心审视一遍：“这段摘要读起来像无聊的公文吗？”如果是，请重写，直到它变得足够有趣、让人有强烈的点击欲。

输出结构依然保持：
💡 **核心亮点**：一句话（必须一针见血或足够有趣）。
🛠️ **创客/教学脑洞**：一个具体的、疯狂的或可落地的点子。
🍼 **育儿/生活吐槽与启发**：接地气的生活折射。

下方是一个【1-Shot 优秀输出范例】，请作为你输出摘要的“灵魂基线”：
=== 范例开始 ===
【输入文章】：一篇关于用废纸板搭建大跨度测地线穹顶(Geodesic Dome)的创客教程。
【期望输出的优质摘要】：
💡 **核心亮点**：这篇文章教你用废弃快递箱搭建一个受巴克敏斯特·富勒启发的测地线穹顶，纯靠几何力学支撑，不用一滴胶水就能承受一个成年人的重量，绝对的反直觉！
🛠️ **创客/教学脑洞**：点子来了！在“未来城市”创客营里，我们可以升级这个概念。不仅仅是搭纸箱，我们可以用树莓派配合震动传感器（Accelerometer），让孩子们在纸箱穹顶上做“抗震测试”。当地震指数超标时，穹顶内的 LED 灯带自动闪烁红色警报。这才是建筑学与物理计算的完美结合！
🍼 **育儿/生活吐槽与启发**：说真的，在家搭这个测地线穹顶不仅是个绝佳的“秘密基地”，更是新晋爸妈的“降噪静音舱”。当神兽在里面安静拆箱时，你终于可以泡杯咖啡享受 5 分钟的绝对静音了。
=== 范例结束 ===

---
现在，请严格阅读下方真正的文章内容，执行上述 Prompt 及自我批评机制，并输出你的摘要：
标题: {title}
内容: {content[:3000]}
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
            print(f"\n✨ [AI 灵感输出测试] ✨\n{summary}\n")
            
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
