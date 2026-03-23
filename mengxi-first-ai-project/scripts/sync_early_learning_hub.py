#!/usr/bin/env python3
import os
import re
from datetime import datetime

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HUB_HTML_PATH = os.path.join(PROJECT_DIR, "early-learning-hub", "ages", "0-1.html")
MONGSHI_MD_PATH = os.path.join(PROJECT_DIR, "posts", "md", "meng-shi-0-1-sui-nido-jia-ting-fang-an-zi-dong-hua-tong-bu.md")
MATH_MD_PATH = os.path.join(PROJECT_DIR, "posts", "md", "math-puzzles-feed.md")

def extract_games(md_path, category_emoji, bg_color, border_color):
    """提取 markdown 中由 AI 生成的核心 0-1 岁游戏卡片"""
    if not os.path.exists(md_path):
        return []

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    games = []
    
    # 按照分隔线 '---' 分块
    blocks = content.split('---')
    
    for block in blocks:
        block = block.strip()
        if not block: continue
        
        title = ""
        link = ""
        summary = ""
        
        # 匹配标题和链接
        if '📌 ' in block and '🌐 点击直达' in block:
            t_match = re.search(r'📌 (.*)', block)
            l_match = re.search(r'➡️ (https?://\S+)', block)
            if t_match: title = t_match.group(1).strip()
            if l_match: link = l_match.group(1).strip()
            
            s_match = re.search(r'🧠 婴儿解谜与干货总结：(.*)', block)
            if s_match: summary = s_match.group(1).strip()
            
        elif '### 🧩 [' in block:
            t_match = re.search(r'### 🧩 \[(.*?)\]\((.*?)\)', block)
            if t_match: 
                title = t_match.group(1).strip()
                link = t_match.group(2).strip()
            
            s_match = re.search(r'> \*\*🤖 逻辑解析.*?\n(.*?)\n', block)
            if s_match: summary = s_match.group(1).strip()
            
            # AI 模式
            if not summary or '📌 **核心概览' in block:
                s_match2 = re.search(r'🇨🇳 \*\*中文.*?\*\*: (.*?)(?=\n|$)', block)
                if s_match2: 
                    summary = s_match2.group(1).strip()
                else:
                    g_match = re.search(r'🎮 \*\*详细带娃玩法.*?\n(.*?)(?=\n<details|$)', block, re.DOTALL)
                    if g_match: 
                        summary = g_match.group(1).strip().replace('- 🇨🇳 **中文规则**: ', '').replace('1. ', '')
        
        if not title or not link or not summary:
            continue
            
        # 截断长文本
        if len(summary) > 130:
            summary = summary[:127] + "..."
            
        if summary and "载入中" not in summary:
            # 去除 markdown
            summary = re.sub(r'\*\*(.*?)\*\*', r'\1', summary)
            
            html = f"""
                <a href="{link}" target="_blank" class="activity-card" style="border-top-color: {border_color}; cursor: pointer; text-decoration: none;">
                    <div class="activity-emoji">{category_emoji}</div>
                    <div class="activity-title" style="color: {border_color}; font-size: 1rem; margin-bottom: 0.5rem; font-weight: bold;">{title[:25]}..</div>
                    <div class="activity-description" style="color: #555; font-size: 0.85rem; line-height: 1.5; margin-bottom: 1rem;">{summary}</div>
                    <div class="activity-time" style="background: {border_color}; opacity: 0.9; border-radius: 4px;">AI 硬核提炼</div>
                </a>
            """
            games.append(html)
            
        if len(games) >= 4:
            break
            
    return games

def main():
    print("=== 🌱 开始同步 Early Learning Hub: 0-1岁 AI 活动榜 ===")
    
    montessori_games = extract_games(MONGSHI_MD_PATH, "🧩", "#FDF2F5", "#B8788C")
    math_games = extract_games(MATH_MD_PATH, "🧮", "#f3ebf6", "#9b59b6")
    
    all_games = (montessori_games + math_games)
    
    # 我们只显示最新的 6 个
    if len(all_games) > 6:
        # 为了错开显示，我们交替取一个蒙氏一个数学
        combined = []
        for i in range(max(len(montessori_games), len(math_games))):
            if i < len(montessori_games): combined.append(montessori_games[i])
            if i < len(math_games): combined.append(math_games[i])
        all_games = combined[:6]
        
    if not all_games:
        print("   ⚠️ 没有解析到有效游戏数据。")
        return
        
    cards_html = "\n".join(all_games)
    
    if not os.path.exists(HUB_HTML_PATH):
        print("   ⚠️ 找不到早教 Hub 的 0-1岁 html 文件。")
        return
        
    with open(HUB_HTML_PATH, 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    # 注：我们在 HTML 里插入了 <div class="activities-grid" id="ai-dynamic-games"> ... </div>
    pattern = r'(<div class="activities-grid" id="ai-dynamic-games">)(.*?)(</div>\s*</section>\s*<!-- AI_SYNC_GAMES_END -->)'
    
    def repl(match):
        return match.group(1) + "\n" + cards_html + "\n            " + match.group(3)
        
    new_html, count = re.subn(pattern, repl, html_content, flags=re.DOTALL)
    
    if count > 0:
        with open(HUB_HTML_PATH, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print("✅ 成功将最新全球 0-1岁硬核游戏提炼卡片写入 Early Learning Hub！")
    else:
        print("⚠️ 未能在 HTML 中找到插入标识符，跳过写入。")

if __name__ == "__main__":
    main()
