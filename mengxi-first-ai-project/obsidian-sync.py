#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Obsidian笔记转时间轴JSON同步脚本
将Obsidian Vault中的.md文件转换为时间轴所需的JSON格式
支持YAML Frontmatter和无Frontmatter两种笔记格式
"""

import os
import re
import sys
import json
from pathlib import Path
from datetime import datetime

# 引入统一私密过滤模块
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "scripts"))
from privacy_filter import is_private

# Obsidian Vault目录
VAULT_PATH = os.getenv("OBSIDIAN_VAULT_PATH", "/Users/hulimofaqiu/Documents/obisidian笔记文件/")
# 输出JSON路径
PROJECT_ROOT = Path(__file__).parent.absolute()
OUTPUT_JSON = os.getenv("TIMELINE_JSON_PATH", str(PROJECT_ROOT / "blog/static/timeline-data.json"))
# 忽略的目录和文件
IGNORE_PATTERNS = [".git", ".obsidian", ".DS_Store", ".smart-connections", ".smart-env",
                   ".smtcmp_json_db", ".smtcmp_vector_db.tar.gz", ".vscode"]

# 颜色映射（用于不同类型的笔记）
CATEGORY_COLORS = {
    "学习笔记": "#b4d4a0",
    "灵感": "#b8a084",
    "教程": "#f0d9b5",
    "编程": "#d6e0f5",
    "数据科学": "#ffd9b3",
    "默认": "#e4e6eb"
}

def read_md_file(file_path):
    """读取Markdown文件并解析YAML Frontmatter"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    yaml_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    frontmatter = {}
    body = content

    if yaml_match:
        yaml_content = yaml_match.group(1)
        body = content[yaml_match.end():]
        for line in yaml_content.split('\n'):
            line = line.strip()
            if line and ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()
                if value.startswith('[') and value.endswith(']'):
                    value = [v.strip().strip("'\"") for v in value[1:-1].split(',')]
                elif ',' in value and key in ['tags', 'categories']:
                    value = [v.strip() for v in value.split(',')]
                frontmatter[key.lower()] = value

    return frontmatter, body

def extract_note_info(file_path, frontmatter, body):
    """提取笔记的关键信息"""
    file_name = os.path.basename(file_path)

    title = frontmatter.get('title', os.path.splitext(file_name)[0])
    date = frontmatter.get('date')
    tags = frontmatter.get('tags', [])
    if isinstance(tags, str):
        tags = [tags]
    category = frontmatter.get('category', '默认')
    description = frontmatter.get('description', '')

    if not date:
        mtime = os.path.getmtime(file_path)
        date = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')

    if not description:
        plain_text = re.sub(r'!\[\[.*?\]\]', '', body)
        plain_text = re.sub(r'!\[.*?\]\(.*?\)', '', plain_text)
        plain_text = re.sub(r'\!\[.*?\]\[.*?\]', '', plain_text)
        plain_text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', plain_text)
        plain_text = re.sub(r'#+\s', '', plain_text)
        plain_text = re.sub(r'```.*?```', '', plain_text, flags=re.DOTALL)
        plain_text = re.sub(r'\*+', '', plain_text)
        plain_text = re.sub(r'<[^>]+>', '', plain_text)
        plain_text = plain_text.strip()
        description = plain_text[:100] + '...' if len(plain_text) > 100 else plain_text

    note_type = "学习笔记" if category in ["教程", "编程", "数据科学", "技术"] else "灵感"
    color = CATEGORY_COLORS.get(category, CATEGORY_COLORS["默认"])

    wikilink_pattern = r'\[\[(.*?)(?:\|.*?)?\]\]'
    links = re.findall(wikilink_pattern, body)
    clean_links = []
    for link in links:
        link_target = link.split('#')[0].strip()
        if link_target:
            clean_links.append(link_target)

    return {
        "date": date,
        "time": "00:00",
        "type": note_type,
        "title": title,
        "content": description,
        "tags": tags,
        "color": color,
        "links": clean_links,
        "file_path": str(file_path)
    }

def main():
    """主函数：遍历目录并生成JSON"""
    timeline_data = []

    for root, dirs, files in os.walk(VAULT_PATH):
        dirs[:] = [d for d in dirs if d not in IGNORE_PATTERNS]

        for file in files:
            if not file.endswith('.md'):
                continue

            file_path = os.path.join(root, file)

            # ── 读取文件 ──────────────────────────────────
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    raw_content = f.read()
            except Exception:
                continue

            # ── 基础质量过滤 ──────────────────────────────
            if not raw_content or len(raw_content.strip()) == 0:
                continue
            if len(re.sub(r'\s+', '', raw_content)) < 100:
                continue

            # ── 统一私密过滤（privacy_filter 模块）─────────
            blocked, reason = is_private(file_path, VAULT_PATH, raw_content)
            if blocked:
                print(f"🔒 Skipped [{reason}]: {file}")
                continue

            # ── Frontmatter + body 解析 ───────────────────
            frontmatter, body = read_md_file(file_path)

            if not body or len(body.strip()) < 50:
                continue

            note_info = extract_note_info(file_path, frontmatter, body)
            timeline_data.append(note_info)

    timeline_data.sort(key=lambda x: x['date'], reverse=True)

    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(timeline_data, f, ensure_ascii=False, indent=2)

    print(f"✅ 同步完成！共处理 {len(timeline_data)} 篇笔记")
    print(f"📁 生成的JSON文件：{OUTPUT_JSON}")

if __name__ == "__main__":
    main()
