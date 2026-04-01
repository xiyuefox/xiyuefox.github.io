#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📊 私人仪表盘生成器 (Private Dashboard Generator)

扫描 Obsidian daily_brief/ 目录中的所有私人简报，
生成一个本地可访问的 private-dashboard.html 页面。

⚠️ 此文件仅保存于项目根目录，不会被部署到 Cloudflare。
   sync.sh 的 Phase 6 部署的是 public/ 目录，而此文件在根目录。
"""
import os
import re
import datetime
import glob

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OBSIDIAN_VAULT = "/Users/hulimofaqiu/Documents/obisidian笔记文件/"
BRIEF_DIR = os.path.join(OBSIDIAN_VAULT, "daily_brief")
OUTPUT_HTML = os.path.join(PROJECT_DIR, "private-dashboard.html")


def parse_frontmatter(content):
    """提取 YAML frontmatter"""
    fm = {}
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return fm, content
    for line in match.group(1).split('\n'):
        if ':' in line:
            key, _, value = line.partition(':')
            fm[key.strip().lower()] = value.strip().strip('"').strip("'")
    body = content[match.end():].strip()
    return fm, body


def markdown_to_html(md_text):
    """极简 Markdown → HTML 转换"""
    html = md_text
    # Headers
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    # Blockquotes
    html = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)
    # Bold
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    # Italic
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    # Links
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', html)
    # Line breaks
    html = re.sub(r'\n\n', '</p><p>', html)
    html = re.sub(r'\n', '<br>', html)
    # Horizontal rule
    html = html.replace('<br>---<br>', '<hr>')
    return f'<p>{html}</p>'


def generate_dashboard():
    """生成私人仪表盘 HTML"""
    if not os.path.exists(BRIEF_DIR):
        print("📭 暂无私人简报目录，跳过仪表盘生成。")
        return

    briefs = []
    for filepath in sorted(glob.glob(os.path.join(BRIEF_DIR, "*.md")), reverse=True):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            fm, body = parse_frontmatter(content)
            briefs.append({
                'title': fm.get('title', os.path.basename(filepath)),
                'date': fm.get('date', ''),
                'body_html': markdown_to_html(body),
                'filename': os.path.basename(filepath),
            })
        except Exception as e:
            continue

    if not briefs:
        print("📭 暂无私人简报，跳过仪表盘生成。")
        return

    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    cards_html = ""
    for b in briefs:
        cards_html += f"""
        <article class="brief-card">
            <div class="brief-header">
                <span class="brief-date">{b['date']}</span>
                <span class="brief-badge">🔒 PRIVATE</span>
            </div>
            <h2 class="brief-title">{b['title']}</h2>
            <div class="brief-body">{b['body_html']}</div>
            <div class="brief-footer">
                <span class="brief-source">📄 {b['filename']}</span>
            </div>
        </article>
"""

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="noindex, nofollow">
    <title>📥 私人主编仪表盘 — mengxi.space</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-primary: #0a0a0f;
            --bg-card: #12121a;
            --bg-card-hover: #1a1a28;
            --text-primary: #e8e6e3;
            --text-secondary: #8b8a87;
            --text-muted: #5a5957;
            --accent-gold: #f0c674;
            --accent-purple: #b39ddb;
            --accent-blue: #64b5f6;
            --accent-red: #ef5350;
            --border: #2a2a35;
            --font-sans: 'Inter', -apple-system, sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        body {{
            font-family: var(--font-sans);
            background: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            line-height: 1.7;
        }}

        .dashboard-header {{
            background: linear-gradient(135deg, #12121a 0%, #1a1530 50%, #12121a 100%);
            border-bottom: 1px solid var(--border);
            padding: 2.5rem 2rem;
            text-align: center;
        }}

        .dashboard-header h1 {{
            font-size: 1.8rem;
            font-weight: 300;
            letter-spacing: 0.05em;
            color: var(--accent-gold);
        }}

        .dashboard-header .subtitle {{
            font-family: var(--font-mono);
            font-size: 0.75rem;
            color: var(--text-muted);
            margin-top: 0.5rem;
            text-transform: uppercase;
            letter-spacing: 0.15em;
        }}

        .privacy-banner {{
            background: rgba(239, 83, 80, 0.08);
            border: 1px solid rgba(239, 83, 80, 0.2);
            border-radius: 8px;
            padding: 0.8rem 1.5rem;
            margin: 1.5rem auto;
            max-width: 800px;
            text-align: center;
            font-family: var(--font-mono);
            font-size: 0.72rem;
            color: var(--accent-red);
            letter-spacing: 0.08em;
        }}

        .container {{
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem 1.5rem;
        }}

        .stats-bar {{
            display: flex;
            gap: 1.5rem;
            margin-bottom: 2rem;
            padding: 1rem;
            background: var(--bg-card);
            border-radius: 10px;
            border: 1px solid var(--border);
        }}

        .stat {{
            font-family: var(--font-mono);
            font-size: 0.75rem;
        }}

        .stat-value {{
            color: var(--accent-blue);
            font-weight: 600;
            font-size: 1.2rem;
        }}

        .stat-label {{
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.1em;
            font-size: 0.65rem;
        }}

        .brief-card {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 2rem;
            margin-bottom: 1.5rem;
            transition: all 0.3s ease;
        }}

        .brief-card:hover {{
            background: var(--bg-card-hover);
            border-color: var(--accent-purple);
            transform: translateY(-2px);
            box-shadow: 0 8px 32px rgba(179, 157, 219, 0.08);
        }}

        .brief-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }}

        .brief-date {{
            font-family: var(--font-mono);
            font-size: 0.75rem;
            color: var(--accent-blue);
        }}

        .brief-badge {{
            font-family: var(--font-mono);
            font-size: 0.65rem;
            background: rgba(239, 83, 80, 0.1);
            color: var(--accent-red);
            padding: 0.2rem 0.6rem;
            border-radius: 4px;
            letter-spacing: 0.08em;
        }}

        .brief-title {{
            font-size: 1.15rem;
            font-weight: 600;
            color: var(--accent-gold);
            margin-bottom: 1rem;
            line-height: 1.4;
        }}

        .brief-body {{
            font-size: 0.88rem;
            color: var(--text-secondary);
            line-height: 1.8;
        }}

        .brief-body h2 {{
            color: var(--accent-purple);
            font-size: 1rem;
            margin: 1.2rem 0 0.6rem;
            font-weight: 600;
        }}

        .brief-body h3 {{
            color: var(--text-primary);
            font-size: 0.92rem;
            margin: 1rem 0 0.4rem;
        }}

        .brief-body blockquote {{
            border-left: 3px solid var(--accent-gold);
            padding-left: 1rem;
            color: var(--text-muted);
            font-style: italic;
            margin: 1rem 0;
        }}

        .brief-body a {{
            color: var(--accent-blue);
            text-decoration: none;
            border-bottom: 1px dotted var(--accent-blue);
        }}

        .brief-body a:hover {{
            color: var(--accent-gold);
        }}

        .brief-body hr {{
            border: none;
            border-top: 1px solid var(--border);
            margin: 1.5rem 0;
        }}

        .brief-footer {{
            margin-top: 1.2rem;
            padding-top: 0.8rem;
            border-top: 1px solid var(--border);
        }}

        .brief-source {{
            font-family: var(--font-mono);
            font-size: 0.68rem;
            color: var(--text-muted);
        }}

        .empty-state {{
            text-align: center;
            padding: 4rem 2rem;
            color: var(--text-muted);
        }}

        .empty-state .icon {{
            font-size: 3rem;
            margin-bottom: 1rem;
        }}

        @media (max-width: 640px) {{
            .dashboard-header h1 {{ font-size: 1.3rem; }}
            .brief-card {{ padding: 1.2rem; }}
            .stats-bar {{ flex-direction: column; gap: 0.8rem; }}
        }}
    </style>
</head>
<body>
    <header class="dashboard-header">
        <h1>📥 私人主编仪表盘</h1>
        <p class="subtitle">Private Inbox Digest Dashboard · Last refreshed: {now}</p>
    </header>

    <div class="privacy-banner">
        🔒 THIS PAGE IS LOCAL-ONLY · NOT DEPLOYED TO CLOUDFLARE · CONTAINS PRIVATE EMAIL DIGESTS
    </div>

    <div class="container">
        <div class="stats-bar">
            <div class="stat">
                <div class="stat-value">{len(briefs)}</div>
                <div class="stat-label">Total Briefs</div>
            </div>
            <div class="stat">
                <div class="stat-value">{briefs[0]['date'] if briefs else 'N/A'}</div>
                <div class="stat-label">Latest Brief</div>
            </div>
            <div class="stat">
                <div class="stat-value">🔒</div>
                <div class="stat-label">Privacy Level</div>
            </div>
        </div>

        {cards_html if cards_html else '<div class="empty-state"><div class="icon">📭</div><p>暂无私人简报<br>运行 auto_gmail_digest.py 生成首份简报</p></div>'}
    </div>

    <script>
        // 极简搜索过滤
        document.addEventListener('keydown', (e) => {{
            if (e.key === 'Escape') {{
                document.querySelectorAll('.brief-card').forEach(c => c.style.display = '');
            }}
        }});
    </script>
</body>
</html>"""

    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"📊 私人仪表盘已生成: {OUTPUT_HTML}")
    print(f"   共 {len(briefs)} 份简报 | 最新: {briefs[0]['date'] if briefs else 'N/A'}")
    print(f"   ⚠️  此文件仅本地可访问，不会部署到 Cloudflare")


def main():
    print("📊 正在生成私人仪表盘...")
    generate_dashboard()


if __name__ == "__main__":
    main()
