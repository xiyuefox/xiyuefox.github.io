#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
privacy_filter.py — 统一私密过滤模块
被 sync_obsidian.py 和 obsidian-sync.py 共同引用

判断规则（满足任意一条 → 不发布）：
  1. Frontmatter: private: true
  2. Frontmatter: status: private
  3. Frontmatter: draft: true
  4. Frontmatter: publish: false
  5. 内容中含 #private 或 #draft 标签
  6. 文件位于私密文件夹下（private/私密/个人/日记/diary/personal）
  7. 文件名含 Untitled / 未命名
  8. 文件名黑名单关键词（外高桥/租房/看房）
"""

import re
from pathlib import Path

# ── 配置常量 ────────────────────────────────────────────────

# 私密文件夹名（任意一级父目录匹配即拦截）
PRIVATE_FOLDERS = {
    "private", "Private",
    "私密", "个人", "日记",
    "diary", "personal",
}

# 文件名黑名单关键词
FILENAME_BLACKLIST = ["外高桥", "租房", "看房"]

# 文件名排除前缀 / 模式（系统文件、未命名等）
FILENAME_EXCLUDE_PATTERNS = [
    "Untitled", "未命名", "Drawing", "!Pasted", "Excalidraw",
]


# ── 核心判断函数 ────────────────────────────────────────────

def parse_frontmatter(content: str) -> dict:
    """
    从 Markdown 内容中提取 YAML Frontmatter，返回字典。
    不依赖 yaml 库，使用简单正则解析（够用且无外部依赖）。
    """
    frontmatter = {}
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return frontmatter

    for line in match.group(1).split('\n'):
        line = line.strip()
        if not line or ':' not in line:
            continue
        key, _, value = line.partition(':')
        key = key.strip().lower()
        value = value.strip()
        # 处理数组: [a, b, c]
        if value.startswith('[') and value.endswith(']'):
            value = [v.strip().strip("'\"") for v in value[1:-1].split(',')]
        # 处理逗号分隔的 tags
        elif ',' in value and key in ('tags', 'categories'):
            value = [v.strip() for v in value.split(',')]
        frontmatter[key] = value

    return frontmatter


def is_private(file_path: str, vault_root: str, content: str = None) -> tuple[bool, str]:
    """
    判断一个文件是否应被屏蔽（私密/草稿/黑名单）。

    参数：
        file_path  — 文件绝对路径
        vault_root — Obsidian Vault 根目录（用于计算相对路径）
        content    — 文件内容字符串（可选；不传则自动读取）

    返回：
        (True, 原因字符串)  → 应屏蔽
        (False, "")         → 可以发布
    """
    filename = Path(file_path).name

    # ── 1. 文件名快速拦截 ──────────────────────────────────
    if any(kw in filename for kw in FILENAME_BLACKLIST):
        return True, f"blacklist keyword in filename: {filename}"

    if any(p in filename for p in FILENAME_EXCLUDE_PATTERNS):
        return True, f"excluded filename pattern: {filename}"

    # ── 2. 私密文件夹拦截 ─────────────────────────────────
    try:
        rel = Path(file_path).relative_to(vault_root)
        # 只检查父目录部分（排除文件名本身）
        parent_parts = set(rel.parts[:-1])
        matched = parent_parts & PRIVATE_FOLDERS
        if matched:
            return True, f"private folder: {matched.pop()}"
    except ValueError:
        pass  # file_path 不在 vault_root 内，跳过文件夹检查

    # ── 3. 读取文件内容（如未传入）────────────────────────
    if content is None:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return True, f"unreadable file: {e}"

    # ── 4. Frontmatter 拦截 ───────────────────────────────
    fm = parse_frontmatter(content)

    if str(fm.get('private', '')).lower() == 'true':
        return True, "frontmatter: private: true"

    status = str(fm.get('status', '')).lower()
    if status in ('private', 'draft'):
        return True, f"frontmatter: status: {status}"

    if str(fm.get('draft', '')).lower() == 'true':
        return True, "frontmatter: draft: true"

    if str(fm.get('publish', '')).lower() == 'false':
        return True, "frontmatter: publish: false"

    # ── 5. 内容 hashtag 拦截 ──────────────────────────────
    content_lower = content.lower()
    if '#private' in content_lower:
        return True, "content tag: #private"
    if '#draft' in content_lower:
        return True, "content tag: #draft"

    # ── 6. private-briefing 标签拦截 (邮箱降噪私人简报) ───
    tags = fm.get('tags', [])
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(',')]
    if 'private-briefing' in tags:
        return True, "tag: private-briefing (私人简报，不公开)"

    return False, ""


def should_publish(file_path: str, vault_root: str, content: str = None) -> bool:
    """
    is_private 的反向封装，语义更直观。
    返回 True 表示可以发布。
    """
    blocked, reason = is_private(file_path, vault_root, content)
    if blocked:
        print(f"🔒 Skipped [{reason}]: {Path(file_path).name}")
    return not blocked
