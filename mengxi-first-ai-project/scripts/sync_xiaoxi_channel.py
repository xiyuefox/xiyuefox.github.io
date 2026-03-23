#!/usr/bin/env python3
import os
import re
import sys
import glob
from datetime import datetime
import requests
import feedparser
import urllib3

# 配置区域
MODEL_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("❌ 错误: 未设置 GEMINI_API_KEY 环境变量")
    sys.exit(1)

# 路径配置
PROJECT_DIR = "/Users/hulimofaqiu/mengxi-first-ai-project"
LENNY_DIR = os.path.join(PROJECT_DIR, "xiaoxi-channel", "data", "23个Lenny文件按时间合并")
POSTS_MD_DIR = os.path.join(PROJECT_DIR, "posts", "md")
INDEX_HTML = os.path.join(PROJECT_DIR, "index.html")

def get_latest_lenny_content():
    """读取最高的 Lenny 归档内容 snippet，支持 RSS 动态拉取。"""
    
    # 1. 尝试拉取 Lenny's Newsletter RSS 订阅以实现自动总结
    try:
        print("📡 正在尝试拉取 Lenny's Newsletter RSS 订阅板...")
        res = requests.get("https://www.lennysnewsletter.com/feed", timeout=15)
        if res.status_code == 200:
            feed = feedparser.parse(res.text)
            feed_items = []
            for entry in feed.entries[:3]: # 获取前 3 篇最新文章作为提炼源
                title = entry.get('title', '无标题')
                summary = entry.get('summary', '').strip()
                clean_summary = re.sub('<[^>]*>', '', summary).strip()
                feed_items.append(f"### {title}\n{clean_summary}\n")
            if feed_items:
                print("✅ 成功拉取 RSS 动态文章。")
                return "\n\n".join(feed_items)
    except Exception as e:
        print(f"⚠️ RSS 加载异常: {e}，将回退到本地归档数据目录。")

    # 2. 查找 2025 年的 newsletter (Fallback)
    newsletter_file = os.path.join(LENNY_DIR, "newsletters-2025.md")
    if not os.path.exists(newsletter_file):
        newsletter_file = os.path.join(LENNY_DIR, "newsletters-2024.md")
        
    if not os.path.exists(newsletter_file):
        return "未能找到 Lenny 的 Newsletter 归档文件。"

    with open(newsletter_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 提取前 2 篇文章进行总结展现
    blocks = content.split('---')
    if len(blocks) > 2:
        return "---".join(blocks[1:3]) # 提取第一和第二篇文章
    return content[:3000]

def summarize_with_gemini(lenny_snippet, tech_context):
    """使用 AI 总结生成小溪的学习面板大纲和核心解读"""
    url = f"{MODEL_ENDPOINT}?key={GEMINI_API_KEY}"
    headers = {'Content-Type': 'application/json'}
    
    prompt = f"""
你现在是 小溪 的专属 AI 学习管家。小溪是一位孕妈妈，同时也是一位对产品、增长、AI 以及前沿技术有极高热情的硅谷范极客。她利用这段时期为自己进行专业上的充电与成长。

我将为你提供：
1. **Lenny Newsletter 深度干货片段**：
{lenny_snippet}

2. **《科技之巅：全球突破性创新》背景**：
{tech_context}

请写出一个极其硬核、优雅且适配孕期充电节奏的【面板摘要点】、【详细阅读文章摘要】和【每日随机一问 Q&A】。

### 要求：
1. **面板大纲 (HTML 颗粒，只需要 4 个点)**：
   - 必须以 `<li>` 结构返回，内容中文。
   - 关注于：Product / Growth 落地、或 2025 年 AI Prototyping 工具落地。
   - 语言凝练而深刻。

2. **详细 feed 归档内容 (Markdown 格式)**：
   - 这是一个放在 `xiaoxi-product-feed.md` 中的文章。
   - 包含【📌 核心摘要】、【🛠️ Lenny 的硅谷产品心法】、【🔮 前沿创新视角】、【💆‍♀️ 孕妈专属充电建议】。
   - 整体字数控制在 1000 字左右，逻辑清晰，分段考究。

3. **每日一问 Q&A Pair (用于 index.html 的 Q&A Card 展示)**：
   - 构建一个跟今日内容相关的硬核产品或增长思维问题。
   - 格式按下方 [Question] 和 [Answer] 标注，Answer 使用精炼的 <ul> 列表包覆。

输出格式必须严格如下分块，使用 `[[[DIVIDER]]]` 隔开：

#### 1. 面板 HTML 点 (4个 li)
<li><strong>...</strong>: ...</li>
<li><strong>...</strong>: ...</li>
...

[[[DIVIDER]]]

#### 2. Markdown 详细全屏 Feed 页面
---
title: "🥑 小溪的极客成长板 | 产品、增长与科技观察"
...

[[[DIVIDER]]]

#### 3. 每日一问 Q&A
[Question]
产品-市场匹配的滞后指标和领先指标应该如何协同？
[Answer]
<ul>
  <li><strong>领先指标</strong>: ...</li>
  <li><strong>滞后指标</strong>: ...</li>
</ul>
"""
    try:
        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        res = requests.post(url, headers=headers, json=payload, timeout=60)
        if res.status_code == 200:
            data = res.json()
            parts = data.get('candidates', [{}])[0].get('content', {}).get('parts', [])
            if parts:
                return parts[0].get('text', '').strip()
        print(f"Gemini API 异常, 状态码: {res.status_code}")
        return None
    except Exception as e:
        print(f"Gemini API 错误: {e}")
        return None

def main():
    print("🌱 启动 小溪的学习频道 一键聚合与渲染模块...")
    
    # 增加缓存/频率保护：因为所读取的 Lenny 数据是静态 Downloads 压缩包，不必每次都向 Gemini 发起消费。
    md_path = os.path.join(POSTS_MD_DIR, "xiaoxi-product-feed.md")
    # 移除缓存保护，以支持每天根据 RSS 动态进行自动更新总结
    pass

    lenny_content = get_latest_lenny_content()
    
    # 科技之巅背景（来自于前 30 页 pdf 抽取的核心段落）
    tech_context = """
    XR 混合现实：AR(增强)、VR(虚拟)、MR(混合)在元宇宙、创作领域的高自主度研发和币种互通。
    《麻省理工科技评论》20年里程碑：从往年的全球十大突破性技术观察，覆盖弦理论、生物遗传时钟、DNA设计组装。
    跨学科孤岛的边界拆卸：未来10年极高比例的学科打破，AI、生物、计算的算力复合，主导产业预判。
    """
    
    print("🤖 正在向 Gemini 请求同步摘要...")
    ai_response = summarize_with_gemini(lenny_content, tech_context)
    
    if not ai_response:
        print("❌ AI 生成失败，卡死")
        return

    try:
        parts = ai_response.split('[[[DIVIDER]]]')
        html_points = parts[0].strip()
        md_content = parts[1].strip()
        qa_content = parts[2].strip() if len(parts) > 2 else ""
    except Exception as e:
        print(f"❌ AI 返回内容分块解析失败: {e}")
        return
        
    # 解析 QA 内容
    qa_question = "产品-市场匹配滞后指标如何协同？"
    qa_answer = "<ul><li>暂无解析</li></ul>"
    if qa_content:
        q_match = re.search(r'\[Question\](.*?)\[Answer\]', qa_content, re.DOTALL)
        a_match = re.search(r'\[Answer\](.*)', qa_content, re.DOTALL)
        if q_match:
            qa_question = q_match.group(1).strip()
        if a_match:
            qa_answer = a_match.group(1).strip()
        
    # 1. 写入 Markdown Feed
    md_path = os.path.join(POSTS_MD_DIR, "xiaoxi-product-feed.md")
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"✅ 成功写入详细 Feed: {md_path}")

    # 2. 更新 index.html 面板大纲
    updated_html_points = ""
    for line in html_points.split('\n'):
        if '<li>' in line:
            updated_html_points += line.strip() + "\n"
            
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        content = f.read()

    xiaoxi_card_html = f"""
                        <a href="post.html?post=xiaoxi-product-feed" class="tg-card tg-fade-in" style="transform: translateY(0); border-top: 2px solid #3498db;">
                            <div class="tg-card-header">
                                <span class="tg-card-icon">🧠</span>
                                <span class="tg-card-source">Lenny & Tech</span>
                            </div>
                            <h3 class="tg-card-title">小溪的极客成长板 (Product & Tech)</h3>
                            <p class="tg-card-desc">💡 AI 提炼硅谷产品、增长心法与前沿科技，孕妈的高端充电特刊。</p>
                            <div class="summary-toggle-btn" onclick="event.preventDefault(); event.stopPropagation(); toggleSummary(this);" style="font-size: 0.8rem; color: #3498db; cursor: pointer; display: inline-block; margin-top: 0.5rem; font-weight: 500;">
                                📂 展开 最新 Product & AI 摘要
                            </div>
                            <div class="expandable-summary" style="display: none; font-size: 0.82rem; color: var(--tg-text-main); margin-top: 0.8rem; padding: 0.8rem; background: rgba(0,0,0,0.15); border-radius: 6px; border: 1px dashed rgba(52, 152, 219, 0.3);">
                                <ul style="margin: 0; padding-left: 1.2rem; list-style-type: disc;">
{updated_html_points}                                </ul>
                            </div>
                            <div class="tg-card-footer">
                                <span class="tg-badge" style="background: #3498db; color: white;">Geek Growth</span>
                            </div>
                        </a>

                        <a href="https://github.com/joeseesun/lennys-podcast-newsletter" target="_blank" class="tg-card tg-fade-in" style="transform: translateY(0); border-top: 2px solid #9b59b6;">
                            <div class="tg-card-header">
                                <span class="tg-card-icon">🛠️</span>
                                <span class="tg-card-source">Claude Code Tool</span>
                            </div>
                            <h3 class="tg-card-title">Lenny 知识库 Skill 安装板</h3>
                            <p class="tg-card-desc">💡 绑定 Claude Code，开启 Lenny 专属全局对话学习通道。</p>
                            <div class="summary-toggle-btn" onclick="event.preventDefault(); event.stopPropagation(); toggleSummary(this);" style="font-size: 0.8rem; color: #9b59b6; cursor: pointer; display: inline-block; margin-top: 0.5rem; font-weight: 500;">
                                📂 展开 安装与使用指令
                            </div>
                            <div class="expandable-summary" style="display: none; font-size: 0.82rem; color: var(--tg-text-main); margin-top: 0.8rem; padding: 0.8rem; background: rgba(0,0,0,0.15); border-radius: 6px; border: 1px dashed rgba(155, 89, 182, 0.3);">
                                <p style="margin: 0 0 0.5rem 0;">终端运行以下命令进行安装：</p>
                                <code style="display: block; background: rgba(0,0,0,0.3); padding: 0.5rem; border-radius: 4px; color: #e74c3c;">npx skills add joeseesun/lennys-podcast-newsletter</code>
                                <p style="margin: 0.5rem 0 0 0; font-size: 0.75rem; color: var(--tg-text-muted);">* 依赖: Claude Code, 数据集需解压配置。</p>
                            </div>
                            <div class="tg-card-footer">
                                <span class="tg-badge" style="background: #9b59b6; color: white;">Dev Tool</span>
                            </div>
                        </a>
"""

    qa_card_html = f"""
                        <a href="#" class="tg-card tg-fade-in" style="transform: translateY(0); border-top: 2px solid #2ecc71;" onclick="event.preventDefault();">
                            <div class="tg-card-header">
                                <span class="tg-card-icon">📖</span>
                                <span class="tg-card-source">Daily Q&A</span>
                            </div>
                            <h3 class="tg-card-title">每日一问：{qa_question}</h3>
                            <p class="tg-card-desc">💡 碰撞产品增长与前沿技术，每日一卡深度思考。</p>
                            <div class="summary-toggle-btn" onclick="event.preventDefault(); event.stopPropagation(); toggleSummary(this);" style="font-size: 0.8rem; color: #2ecc71; cursor: pointer; display: inline-block; margin-top: 0.5rem; font-weight: 500;">
                                📂 展开 详细解析 (Answer)
                            </div>
                            <div class="expandable-summary" style="display: none; font-size: 0.82rem; color: var(--tg-text-main); margin-top: 0.8rem; padding: 0.8rem; background: rgba(0,0,0,0.15); border-radius: 6px; border: 1px dashed rgba(46, 204, 113, 0.3);">
                                {qa_answer}
                            </div>
                            <div class="tg-card-footer">
                                <span class="tg-badge" style="background: #2ecc71; color: white;">Interactive</span>
                            </div>
                        </a>"""

    xiaoxi_card_html += qa_card_html

    # 直接做正则替换，让每次运行都能刷新卡片上的摘要和问答对
    grid_pattern = r'(<!-- Section: Xiao Xi\'s Learning Channel -->.*?<div class="tg-grid">)(.*?)(</div>\s*</section>)'
    
    if re.search(grid_pattern, content, re.DOTALL):
        print("♻️ 检出到已有卡片 Grid 行，正在动态更新摘要与 Q&A 排版...")
        def repl(match):
            # Preserve indentation for the inserted HTML
            indent = " " * 20 # Indentation level of the cards within tg-grid
            return match.group(1) + "\n" + "\n".join([indent + line for line in xiaoxi_card_html.splitlines()]) + "\n" + match.group(3)
        new_content = re.sub(grid_pattern, repl, content, flags=re.DOTALL)
    else:
        # 为了美观，我们找 `</a>\n                    </div>\n                </section>` 之类的地方插入。
        # 具体来说，在 `<section id="articles"` 上方，插入一个板块。
        
        insert_marker = r'(<!-- Section: Articles \(Digital Garden\) -->)'
        replacement = f"""<!-- Section: Xiao Xi's Learning Channel -->
                <section class="tg-section" style="margin-top: 3rem; background: rgba(52, 152, 219, 0.04); padding: 1.5rem; border-radius: 12px; border: 1px solid rgba(52, 152, 219, 0.2);">
                    <h2 class="tg-section-title" style="color: #3498db; display: flex; align-items: center; gap: 0.5rem;">🧠 小溪的极客成长板</h2>
                    <p style="font-size: 0.9rem; color: var(--tg-text-muted); margin-bottom: 1.5rem;">为孕期的小溪定制，打通 AI 与硅谷一流 Product/Growth 观察，保持极致的职场竞争力与前瞻见地。</p>
                    <div class="tg-grid">
{xiaoxi_card_html}
                    </div>
                </section>\n\n                \\1"""
                
        new_content = re.sub(insert_marker, replacement, content)
        with open(INDEX_HTML, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✅ 已经完成一键注入 index.html 卡片面板！")

if __name__ == "__main__":
    main()
