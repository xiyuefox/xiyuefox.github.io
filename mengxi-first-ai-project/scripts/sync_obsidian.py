#!/usr/bin/env python3
import os
import re
import sys
import yaml
import shutil
import datetime
import urllib.parse
import json

# 引入统一私密过滤模块
sys.path.insert(0, os.path.dirname(__file__))
from privacy_filter import should_publish, parse_frontmatter

try:
    from pypinyin import lazy_pinyin, Style
except ImportError:
    print("pypinyin is not installed. Please install it using 'pip install pypinyin'.")
    exit(1)

# CONFIGURATION
OBSIDIAN_VAULT = "/Users/hulimofaqiu/Documents/obisidian笔记文件/"
PROJECT_DIR = "/Users/hulimofaqiu/mengxi-first-ai-project"
POSTS_DIR = os.path.join(PROJECT_DIR, "posts", "md")
PUBLIC_POSTS_DIR = os.path.join(PROJECT_DIR, "public", "posts", "md")
IMAGES_DIR = os.path.join(PROJECT_DIR, "public", "images", "obsidian")
INDEX_HTML = os.path.join(PROJECT_DIR, "index.html")

# Create required directories
os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(PUBLIC_POSTS_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

def sanitize_slug(text):
    pinyin_list = lazy_pinyin(text, style=Style.NORMAL)
    slug = '-'.join(pinyin_list).lower()
    slug = re.sub(r'[^a-z0-9\-]', '-', slug)
    slug = re.sub(r'\-+', '-', slug)
    return slug.strip('-')

def is_valid_article(filepath, content):
    """
    决定一篇文章是否应该发布。
    私密/草稿过滤统一交给 privacy_filter.should_publish()。
    此函数只负责「内容质量」判断。
    """
    # ── 私密过滤（统一模块）──────────────────────────────
    if not should_publish(filepath, OBSIDIAN_VAULT, content):
        return False

    filename = os.path.basename(filepath)

    # ── 内容质量：系统文件排除 ───────────────────────────
    exclude_patterns = ['00', '01', 'Drawing', '!Pasted', 'Excalidraw']
    if any(p in filename for p in exclude_patterns):
        return False

    # ── 排除占位符或系统工具等不需发布的标题 ─────────
    slug = sanitize_slug(filename)
    blacklist_slugs = [
        'wen-zhang-biao-ti', 'notion-api-guide', 'auto-layout', 'auto-draw-for-pen',
        'what-does-it-talk-20251211-173051',
        'provide-three-follow-up-questions-worded-as-if-i-m-asking-you-20251211-171723',
        'pdf-page-text-to-clipboard',
        'mindmap-connector',
        'listen',
        'lighten-background-color'
    ]
    if any(b in slug for b in blacklist_slugs):
        return False

    # ── 内容质量：检查 publish 显式声明 ─────────────────
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if match:
        header = match.group(1)
        if re.search(r'^publish:\s*true\s*$', header, re.MULTILINE | re.IGNORECASE):
            return True
        # publish: false 已在 privacy_filter 中处理，这里不重复

    # ── 内容质量：免除特定类型限制（播客/灵感等体裁通常短小精悍） ─
    if 'type: podcast' in content.lower() or 'type: idea' in content.lower():
        return True

    # ── 内容质量：字数或 #publish 标签 ──────────────────
    if '#publish' in content.lower() or len(content) > 1200:
        return True

    return False


def parse_existing_frontmatter(filepath):
    """Extract metadata from an already processed md file in posts/md/."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if not content.startswith('---'):
            return None
            
        header = content.split('---')[1]
        
        # Safe extraction
        title_m = re.search(r'title:\s*["\']?(.*?)["\']?$', header, re.MULTILINE)
        date_m = re.search(r'date:\s*(.*?)$', header, re.MULTILINE)
        badge_m = re.search(r'badge:\s*["\']?(.*?)["\']?$', header, re.MULTILINE)
        type_m = re.search(r'type:\s*["\']?(.*?)["\']?$', header, re.MULTILINE)
        audio_src_m = re.search(r'audio_src:\s*["\']?(.*?)["\']?$', header, re.MULTILINE)
        audience_m = re.search(r'audience:\s*["\']?(.*?)["\']?$', header, re.MULTILINE)
        
        title = title_m.group(1).replace('"', '') if title_m else "Untitled"
        date_str = date_m.group(1).strip() if date_m else "2026-03-02"
        badge = badge_m.group(1).strip() if badge_m else "obsidian"
        post_type = type_m.group(1).strip() if type_m else "article"
        audio_src = audio_src_m.group(1).strip() if audio_src_m else ""
        audience = audience_m.group(1).strip() if audience_m else ""
        
        # Month
        month_str = date_str[:7] if len(date_str) >= 7 else "2026-03"
        
        # Description
        body = content.split('---', 2)[2]
        desc = "A note from Obsidian."
        for p in body.split('\n\n'):
            p = p.strip()
            if p and not p.startswith('#') and not p.startswith('!') and not p.startswith('['):
                clean_p = re.sub(r'[*_`~]+', '', p)
                desc = clean_p[:80] + '...' if len(clean_p) > 80 else clean_p
                break
                
        slug = os.path.splitext(os.path.basename(filepath))[0]
        timestamp = os.path.getmtime(filepath)
        
        return {
            'title': title,
            'slug': slug,
            'date': date_str,
            'month': month_str,
            'tag': badge,
            'desc': desc.replace('\n', ' '),
            'content': content,
            'timestamp': timestamp,
            'source': 'existing',
            'type': post_type,
            'audio_src': audio_src,
            'audience': audience
        }
    except Exception as e:
        print(f"Error parsing existing file {filepath}: {e}")
        return None

def process_vault_article(filepath):
    """Process a new article from the Obsidian vault."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if not is_valid_article(filepath, content):
        return None

    # Parse YAML frontmatter
    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    existing_frontmatter = {}
    body_content = content
    
    if match:
        yaml_str = match.group(1)
        body_content = match.group(2)
        try:
            parsed = yaml.safe_load(yaml_str)
            if isinstance(parsed, dict):
                existing_frontmatter = parsed
        except Exception:
            pass

    filename = os.path.basename(filepath)
    title = existing_frontmatter.get('title')
    if not title:
        title = os.path.splitext(filename)[0]

    slug = sanitize_slug(title)
    if not slug:
        slug = sanitize_slug(filename)
        
    mtime = os.path.getmtime(filepath)
    date_str = str(existing_frontmatter.get('date', ''))
    if not date_str or date_str == 'None':
        date_obj = datetime.datetime.fromtimestamp(mtime)
        date_str = date_obj.strftime("%Y-%m-%d")
        
    month_str = date_str[:7] if len(date_str) >= 7 else "2026-03"
    
    # Extract tags
    fm_tags = existing_frontmatter.get('tags', [])
    if isinstance(fm_tags, str):
        fm_tags = [t.strip() for t in fm_tags.split(',')]
    if fm_tags is None: fm_tags = []
    
    tags = [str(t) for t in fm_tags if str(t).lower() not in ['publish', 'draft']]
    main_tag = tags[0] if tags else "obsidian"
    
    desc = "A note from Obsidian."
    paragraphs = body_content.split('\n\n')
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith('#') and not p.startswith('!') and not p.startswith('['):
            clean_p = re.sub(r'[*_`~]+', '', p)
            desc = clean_p[:80] + '...' if len(clean_p) > 80 else clean_p
            break

    images = re.findall(r'!\[\[(.*?)\]\]', body_content)
    for img in images:
        img_name = img.split('|')[0]
        img_source = None
        for root, _, files in os.walk(OBSIDIAN_VAULT):
            if img_name in files:
                img_source = os.path.join(root, img_name)
                break
        
        if img_source:
            safe_img_name = img_name.replace(' ', '-')
            dest_path = os.path.join(IMAGES_DIR, safe_img_name)
            shutil.copy2(img_source, dest_path)
            body_content = body_content.replace(f'![[{img}]]', f'![{img_name}](/images/obsidian/{safe_img_name})')

            
    post_type = existing_frontmatter.get('type', 'article')
    
    final_content = f"""---
title: "{title.replace('"', '')}"
date: {date_str}
tags: [{', '.join(tags)}]
category: "obsidian"
badge: "{main_tag}"
type: "{post_type}"
---

{body_content.lstrip()}
"""
    return {
        'title': title,
        'slug': slug,
        'date': date_str,
        'month': month_str,
        'tag': main_tag,
        'desc': desc.replace('\n', ' '),
        'content': final_content,
        'timestamp': mtime,
        'source': 'vault',
        'type': post_type,
        'audio_src': existing_frontmatter.get('audio_src', ''),
        'audience': existing_frontmatter.get('audience', 'adult')
    }

print("Scan starting...")
all_posts_dict = {}

# 1. Load all EXISTING posts in posts/md/
print("Loading previously synced posts...")
for filename in os.listdir(POSTS_DIR):
    if filename.endswith('.md'):
        filepath = os.path.join(POSTS_DIR, filename)
        if 'cloudflare-r2' in filename or 'james-phoenix' in filename:
            continue
        post_data = parse_existing_frontmatter(filepath)
        if post_data:
            all_posts_dict[post_data['slug']] = post_data

# 2. Scan Obsidian Vault
print("Scanning Obsidian Vault...")
for root, _, files in os.walk(OBSIDIAN_VAULT):
    for f in files:
        if f.endswith('.md'):
            filepath = os.path.join(root, f)
            post_data = process_vault_article(filepath)
            if post_data:
                slug = post_data['slug']
                if slug not in all_posts_dict or post_data['timestamp'] > all_posts_dict[slug]['timestamp'] or all_posts_dict[slug].get('source') == 'existing':
                    all_posts_dict[slug] = post_data

# 3. Scan Blog misc directory
BLOG_POSTS_DIR = os.path.join(PROJECT_DIR, "blog", "content", "posts", "misc")
if os.path.exists(BLOG_POSTS_DIR):
    print("Scanning Blog misc directory...")
    for f in os.listdir(BLOG_POSTS_DIR):
        if f.endswith('.md'):
            filepath = os.path.join(BLOG_POSTS_DIR, f)
            post_data = process_vault_article(filepath)
            if post_data:
                slug = post_data['slug']
                if slug not in all_posts_dict or post_data['timestamp'] > all_posts_dict[slug]['timestamp']:
                    all_posts_dict[slug] = post_data

def get_post_weight(post):
    title = post['title'].lower()
    slug = post['slug'].lower()
    
    # 强制置顶矩阵（精确分配次序，数字越小越前）
    featured_order = {
        'hn-topics-feed': 0,        # 1. HN 看板
        'dxy-mom': 1,               # 2. 丁香妈妈
        'xiaohongshu': 2,            # 3. 小红书
        '人物档案': 3,               # 4. 人物档案系列
        'math-puzzles-feed': 4      # 5. 数学解谜
    }
    
    for kw, weight in featured_order.items():
        if kw in title or kw in slug:
            return (weight, -post['timestamp'])
            
    return (999, -post['timestamp'])

all_posts = list(all_posts_dict.values())

# ── 1. 过滤屏蔽主题 ──────────────────────────────────
skip_keywords = ['租房', '车体', '户口']
all_posts = [p for p in all_posts if not any(kw in p['title'] or kw in p['slug'] for kw in skip_keywords)]

# ── 2. 隔离 HN 讨论板（已在专属区域渲染，不挤占主格）───
all_posts = [p for p in all_posts if p['slug'] != 'hn-topics-feed']

all_posts.sort(key=get_post_weight)

print(f"Total {len(all_posts)} articles prepared for publishing.")

for p in all_posts:
    if '喂猫机' in p['title']:
        print(f"DUMPING CAT FEEDER: {p['title']} -> type={p.get('type')}")


# Generate Cards HTML Categories
def match_category(post, cat_type, keywords):
    t = post.get('type', 'article').lower()
    if t == cat_type:
        return True
    title_lower = post['title'].lower()
    return any(kw in title_lower for kw in keywords)

showcases_posts = [p for p in all_posts if match_category(p, 'showcase', ['项目', 'showcase'])]
all_podcasts = [p for p in all_posts if match_category(p, 'podcast', ['播客', 'podcast', '音频'])]
ideas_posts = [p for p in all_posts if match_category(p, 'idea', ['灵感', 'idea', '想法'])]

# 🪐 Dual-Track Audio Sub-routing
adult_podcasts = [p for p in all_podcasts if p.get('audience', 'adult') == 'adult']
baby_podcasts = [p for p in all_podcasts if p.get('audience') == 'baby']

articles_posts = [p for p in all_posts if p not in showcases_posts and p not in all_podcasts and p not in ideas_posts]

def generate_card(post):
    is_hot = post['slug'] == 'hn-topics-feed'
    is_original = post.get('source') == 'vault'
    hot_border = "border: 1px solid #e74c3c; box-shadow: 0 4px 15px rgba(231, 76, 60, 0.2);" if is_hot else ""
    hot_badge = '<span class="tg-badge" style="background: #e74c3c; color: #fff;">🔥 重点推荐</span> ' if is_hot else ""
    original_badge = '<span class="tg-badge" style="background: #2ecc71; color: #fff;">🌿 原创</span> ' if is_original else ""
    icon = "🛠️" if post.get('type') == 'showcase' else "🎙️" if post.get('type') == 'podcast' else "💡" if post.get('type') == 'idea' else "📚"
    
    audience_badge = ""
    if post.get('type') == 'podcast' and post.get('audience'):
         audience_tag = "Adults" if post['audience'] == 'adult' else "Baby"
         audience_badge = f'<span class="tg-badge" style="background: var(--tg-accent-blue, #00d2d3); color: #000;">{audience_tag}</span> '

    audio_html = ""
    if post.get('type') == 'podcast' and post.get('audio_src'):
         audio_html = f"""
                        <div class="tg-audio-player" style="margin-top: 1rem; position: relative; z-index: 10;">
                            <audio id="audio-{post['slug']}" src="{post['audio_src']}" preload="none" ontimeupdate="updateTime('{post['slug']}')" onplay="onAudioPlay('{post['slug']}')" onpause="onAudioPause('{post['slug']}')"></audio>
                            <div class="tg-audio-controls" style="display: flex; align-items: center; gap: 0.8rem; font-family: var(--tg-font-mono); font-size: 0.78rem;">
                                <button class="btn-play" id="play-btn-{post['slug']}" onclick="event.preventDefault(); togglePlay('{post['slug']}')" style="background: var(--tg-accent-purple, #6C5CE7); color: #fff; border: none; padding: 0.35rem 0.8rem; border-radius: 4px; cursor: pointer; font-size: 0.75rem; transition: background 0.2s;">▶ Play</button>
                                <span id="time-{post['slug']}" style="color: var(--tg-text-secondary); font-variant-numeric: tabular-nums;">00:00</span>
                                <div class="audio-wave" id="wave-{post['slug']}" style="display: none; align-items: flex-end; gap: 3px; height: 14px; margin-left: auto;">
                                    <span style="display: block; width: 3px; height: 100%; background: var(--tg-accent-purple); animation: wave 0.6s infinite alternate;"></span>
                                    <span style="display: block; width: 3px; height: 60%; background: var(--tg-accent-purple); animation: wave 0.4s infinite alternate 0.2s;"></span>
                                    <span style="display: block; width: 3px; height: 80%; background: var(--tg-accent-purple); animation: wave 0.5s infinite alternate 0.1s;"></span>
                                </div>
                            </div>
                        </div>"""

    return f"""
                        <a href="post.html?post={post['slug']}" class="tg-card tg-fade-in" data-type="{post.get('type', 'article')}" style="{hot_border}">
                            <div class="tg-card-header">
                                <span class="tg-card-icon">{icon}</span>
                                <span class="tg-card-source">obsidian</span>
                                {hot_badge}{original_badge}{audience_badge}
                            </div>
                            <h3 class="tg-card-title">{post['title']}</h3>
                            <p class="tg-card-desc">{post['desc']}</p>
                            {audio_html}
                            <div class="tg-card-footer">
                                <span class="tg-card-meta">{post['month']} • {post.get('type', 'entry')}</span>
                                <span class="tg-badge tg-badge--new">{post['tag']}</span>
                            </div>
                        </a>"""

def build_grid_html(posts):
    if not posts:
        return '<p style="color: var(--tg-text-muted); font-size: 0.85rem; font-family: var(--tg-font-mono);">[ Empty / 暂无内容 ]</p>'
    html = '<div class="tg-grid">\n'
    for post in posts:
         filename = f"{post['slug']}.md"
         for dest_dir in [POSTS_DIR, PUBLIC_POSTS_DIR]:
             with open(os.path.join(dest_dir, filename), 'w', encoding='utf-8') as f:
                 f.write(post['content'])
         html += generate_card(post)
    html += '\n</div>'
    return html

showcase_html = build_grid_html(showcases_posts)
podcast_html = build_grid_html(all_podcasts)


ideas_html = build_grid_html(ideas_posts)
articles_html = build_grid_html(articles_posts[:30])

archived_posts = articles_posts[30:]
archived_cards_html = ""
if archived_posts:
    for post in archived_posts:
         filename = f"{post['slug']}.md"
         for dest_dir in [POSTS_DIR, PUBLIC_POSTS_DIR]:
             with open(os.path.join(dest_dir, filename), 'w', encoding='utf-8') as f:
                 f.write(post['content'])
         archived_cards_html += generate_card(post)

    articles_html += f"""
                    <details class="tg-profiles-details"
                        style="margin-top: 2rem; border-top: 1px solid var(--tg-border-color); padding-top: 1rem;">
                        <summary style="cursor: pointer; font-family: var(--tg-font-mono); font-size: 0.8rem; color: var(--tg-text-muted); text-transform: uppercase; letter-spacing: 0.1em; display: inline-flex; align-items: center; gap: 0.5rem; user-select: none;">
                            <span class="tg-details-chev">▼</span> 查看全部存档文章 (Show {len(archived_posts)} More Articles)
                        </summary>
                        <div class="tg-grid" style="margin-top: 1.5rem;">
{archived_cards_html}                        </div>
                    </details>
                    """

def generate_hn_category_grid():
    hn_data_path = os.path.join(PROJECT_DIR, 'data', 'hackernews.json')
    if not os.path.exists(hn_data_path):
        return "<!-- No HN Data Found -->"
    with open(hn_data_path, 'r', encoding='utf-8') as f:
        posts = json.load(f)
    html = ""
    for post in posts[:4]:
        points = post.get('points', post.get('score', 0))
        title_zh = post.get('title_zh', post.get('title', 'Unknown Title'))
        url = post.get('url', f"https://news.ycombinator.com/item?id={post.get('id', '')}")
        desc = post.get('summary_zh', '无摘要')
        html += f"""
            <a href="{url}" target="_blank" class="tg-card tg-fade-in hn-thread-card">
                <div class="tg-card-header">
                    <span class="tg-card-icon">💬</span>
                    <span class="tg-card-source">👍 {points} pts</span>
                </div>
                <h3 class="tg-card-title">{title_zh}</h3>
                <p class="tg-card-desc">{desc}</p>
                <div class="tg-card-footer">
                    <span class="tg-card-meta">Live Thread</span>
                    <span class="tg-badge">Parenting</span>
                </div>
            </a>
        """
    return html

# Inject into index.html
with open(INDEX_HTML, 'r', encoding='utf-8') as f:
    html_content = f.read()

# 1. 注入 Showcases
if '<!-- SHOWCASES_LIST_START -->' in html_content:
    html_content = re.sub(r'(<!-- SHOWCASES_LIST_START -->).*?(<!-- SHOWCASES_LIST_END -->)', f'\\1\n{showcase_html}\n\\2', html_content, flags=re.DOTALL)

# 2. 注入 Podcasts
if '<!-- PODCASTS_LIST_START -->' in html_content:
    html_content = re.sub(r'(<!-- PODCASTS_LIST_START -->).*?(<!-- PODCASTS_LIST_END -->)', f'\\1\n{podcast_html}\n\\2', html_content, flags=re.DOTALL)

# 2.5. 注入 Ideas
if '<!-- IDEAS_LIST_START -->' in html_content:
    ideas_html = build_grid_html(ideas_posts)
    html_content = re.sub(r'(<!-- IDEAS_LIST_START -->).*?(<!-- IDEAS_LIST_END -->)', f'\\1\n{ideas_html}\n\\2', html_content, flags=re.DOTALL)

# 3. 注入 Articles
if '<!-- ARTICLES_LIST_START -->' in html_content:
    html_content = re.sub(r'(<!-- ARTICLES_LIST_START -->).*?(<!-- ARTICLES_LIST_END -->)', f'\\1\n{articles_html}\n\\2', html_content, flags=re.DOTALL)

# Inject count for ALL articles
count_pattern = r'(<!-- ARTICLES_COUNT_START -->)\s*<span[^>]*>\[\d+\]</span>\s*(<!-- ARTICLES_COUNT_END -->)'
if '<!-- ARTICLES_COUNT_START -->' in html_content:
    html_content = re.sub(count_pattern, f'\\1<span class="tg-nav-count">[{len(all_posts)}]</span>\\2', html_content)

# 🛰️ Inject Automated HN Posts
hn_cards_html = generate_hn_category_grid()
if '<!-- HN_AUTOMATED_POSTS_START -->' in html_content:
    html_content = re.sub(
        r'(<!-- HN_AUTOMATED_POSTS_START -->).*?(<!-- HN_AUTOMATED_POSTS_END -->)',
        f'\\1\n{hn_cards_html}\n\\2',
        html_content,
        flags=re.DOTALL
    )

with open(INDEX_HTML, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updating UI assets and apps in public/...")
shutil.copy2(INDEX_HTML, os.path.join(PROJECT_DIR, "public", "index.html"))
shutil.copy2(os.path.join(PROJECT_DIR, "post.html"), os.path.join(PROJECT_DIR, "public", "post.html"))
shutil.copy2(os.path.join(PROJECT_DIR, "css", "terminal-garden.css"), os.path.join(PROJECT_DIR, "public", "css", "terminal-garden.css"))

# Sync design.html (poche-inspired bookmarks page)
design_html = os.path.join(PROJECT_DIR, "design.html")
if os.path.exists(design_html):
    shutil.copy2(design_html, os.path.join(PROJECT_DIR, "public", "design.html"))

# Sync directories to public/
sync_dirs = {
    "apps": "apps",
    "designer-showcase": "designer-showcase",
    "early-learning-hub": "early-learning-hub"
}

for src, dst in sync_dirs.items():
    src_path = os.path.join(PROJECT_DIR, src)
    dst_path = os.path.join(PROJECT_DIR, "public", dst)
    if os.path.exists(src_path):
        if os.path.exists(dst_path):
            shutil.rmtree(dst_path)
        shutil.copytree(src_path, dst_path)

# Special handling for legacy blog
blog_src = os.path.join(PROJECT_DIR, "blog", "public")
blog_dst = os.path.join(PROJECT_DIR, "public", "blog")
if os.path.exists(blog_src):
    if os.path.exists(blog_dst):
        shutil.rmtree(blog_dst)
    shutil.copytree(blog_src, blog_dst)

# Sync mascot if needed
public_images = os.path.join(PROJECT_DIR, "public", "images")
os.makedirs(public_images, exist_ok=True)
mascot_path = os.path.join(PROJECT_DIR, "images", "pony-mascot-v5.webp")
if os.path.exists(mascot_path):
    shutil.copy2(mascot_path, os.path.join(public_images, "pony-mascot-v5.webp"))

print("Sync complete! 🎉")
