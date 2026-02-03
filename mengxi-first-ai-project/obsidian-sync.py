#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Obsidian笔记转时间轴JSON同步脚本
将Obsidian Vault中的.md文件转换为时间轴所需的JSON格式
支持YAML Frontmatter和无Frontmatter两种笔记格式
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

# Obsidian Vault目录
VAULT_PATH = os.getenv("OBSIDIAN_VAULT_PATH", "/Users/hulimofaqiu/Documents/obisidian笔记文件/")
# 输出JSON路径
# Get absolute path to the project root
PROJECT_ROOT = Path(__file__).parent.absolute()
OUTPUT_JSON = os.getenv("TIMELINE_JSON_PATH", str(PROJECT_ROOT / "blog/static/timeline-data.json"))
# 忽略的目录和文件
IGNORE_PATTERNS = [".git", ".obsidian", ".DS_Store", ".smart-connections", ".smart-env", ".smtcmp_json_db", ".smtcmp_vector_db.tar.gz", ".vscode"]

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

    # 解析YAML Frontmatter
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
                # 处理数组类型（如tags）
                if value.startswith('[') and value.endswith(']'):
                    value = [v.strip().strip("'\"") for v in value[1:-1].split(',')]
                # 处理逗号分隔的tags（如：tags: Python, 编程）
                elif ',' in value and key in ['tags', 'categories']:
                    value = [v.strip() for v in value.split(',')]
                frontmatter[key.lower()] = value

    return frontmatter, body

def extract_note_info(file_path, frontmatter, body):
    """提取笔记的关键信息"""
    file_name = os.path.basename(file_path)

    # 从Frontmatter获取信息
    title = frontmatter.get('title', os.path.splitext(file_name)[0])
    date = frontmatter.get('date')
    tags = frontmatter.get('tags', [])
    if isinstance(tags, str):
        tags = [tags]
    category = frontmatter.get('category', '默认')
    description = frontmatter.get('description', '')

    # 如果Frontmatter没有日期，使用文件修改时间
    if not date:
        mtime = os.path.getmtime(file_path)
        date = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')

    # 从body提取摘要（前100字）
    if not description:
        # 去除Markdown和HTML格式
        plain_text = re.sub(r'!\[\[.*?\]\]', '', body) # 移除Obsidian图片 ![[...]]
        plain_text = re.sub(r'!\[.*?\]\(.*?\)', '', plain_text)  # 移除Markdown图片
        plain_text = re.sub(r'\!\[.*?\]\[.*?\]', '', plain_text)  # 移除Markdown图片引用
        plain_text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', plain_text)  # 移除链接，保留文本
        plain_text = re.sub(r'#+\s', '', plain_text)  # 移除标题符号
        plain_text = re.sub(r'```.*?```', '', plain_text, flags=re.DOTALL)  # 移除代码块
        plain_text = re.sub(r'\*+', '', plain_text)  # 移除强调符号
        plain_text = re.sub(r'<[^>]+>', '', plain_text) # 移除HTML标签
        plain_text = plain_text.strip()
        description = plain_text[:100] + '...' if len(plain_text) > 100 else plain_text

    # 确定笔记类型
    note_type = "学习笔记" if category in ["教程", "编程", "数据科学", "技术"] else "灵感"

    # 分配颜色
    color = CATEGORY_COLORS.get(category, CATEGORY_COLORS["默认"])

    # Extract internal connections (Wikilinks)
    # Matches [[Target]] or [[Target|Alias]]
    wikilink_pattern = r'\[\[(.*?)(?:\|.*?)?\]\]'
    links = re.findall(wikilink_pattern, body)
    
    # Clean links (remove anchors #...)
    clean_links = []
    for link in links:
        link_target = link.split('#')[0].strip()
        if link_target:
            clean_links.append(link_target)

    return {
        "date": date,
        "time": "00:00",  # 如果没有时间信息，默认00:00
        "type": note_type,
        "title": title,
        "content": description,
        "tags": tags,
        "color": color,
        "links": clean_links, # Connections for Knowledge Graph
        "file_path": str(file_path)  # 保留原文件路径
    }

def main():
    """主函数：遍历目录并生成JSON"""
    timeline_data = []

    # 遍历Obsidian目录
    for root, dirs, files in os.walk(VAULT_PATH):
        # 忽略特定目录
        dirs[:] = [d for d in dirs if d not in IGNORE_PATTERNS]

        for file in files:
            if file.endswith('.md'):
                # Blacklist filter (Quality Control)
                blacklist = ["外高桥", "租房", "看房"]
                if any(keyword in file for keyword in blacklist):
                    continue

                file_path = os.path.join(root, file)
                
                # --- Quality Control Filtering ---
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        raw_content = f.read()
                except Exception:
                    continue # Skip unreadable files

                # 1. Check Completeness (Empty files)
                if not raw_content or len(raw_content.strip()) == 0:
                    continue

                # 2. Check Word Count (Min 100 characters roughly)
                # Simple heuristic: remove whitespace and count
                if len(re.sub(r'\s+', '', raw_content)) < 100:
                    continue

                # 3. Check for specific placeholders or "Draft" markers
                if "Untitled" in file or "未命名" in file:
                    continue
                
                # Check Blacklist (Existing logic)
                blacklist = ["外高桥", "租房", "看房"]
                if any(keyword in file for keyword in blacklist):
                    continue

                # Pass quality check -> Process
                frontmatter, body = read_md_file(file_path)
                
                # Double check body content after frontmatter extraction
                if not body or len(body.strip()) < 50:
                    continue
                
                # Check for Draft status in Frontmatter
                is_draft = str(frontmatter.get('draft', '')).lower() == 'true'
                if is_draft:
                    print(f"🚫 Draft excluded: {file}")
                    continue

                note_info = extract_note_info(file_path, frontmatter, body)
                timeline_data.append(note_info)

    # 按日期排序（最新的在最前）
    timeline_data.sort(key=lambda x: x['date'], reverse=True)

    # 写入JSON文件
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(timeline_data, f, ensure_ascii=False, indent=2)

    print(f"✅ 同步完成！共处理 {len(timeline_data)} 篇笔记")
    print(f"📁 生成的JSON文件：{OUTPUT_JSON}")

if __name__ == "__main__":
    main()
