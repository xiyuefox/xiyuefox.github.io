#!/usr/bin/env python3
"""
generate_matrix.py - 生成站点数据矩阵
用于生成标签关联、分类统计等矩阵数据
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any
import yaml

# 项目根目录
PROJECT_ROOT = Path(__file__).parent.parent
POSTS_DIR = PROJECT_ROOT / "posts" / "md"
DATA_DIR = PROJECT_ROOT / "data"

def load_posts_frontmatter() -> List[Dict[str, Any]]:
    """加载所有文章的 frontmatter"""
    posts = []
    for md_file in POSTS_DIR.glob("*.md"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # 提取 frontmatter
            if content.startswith('---'):
                frontmatter_end = content.find('---', 3)
                if frontmatter_end != -1:
                    frontmatter = content[3:frontmatter_end].strip()
                    fm = yaml.safe_load(frontmatter)
                    fm['file_name'] = md_file.name
                    posts.append(fm)
        except Exception as e:
            print(f"⚠️ 解析 {md_file.name} 失败: {e}")

    return posts

def generate_tag_matrix(posts: List[Dict[str, Any]]) -> Dict[str, Any]:
    """生成标签关联矩阵"""
    tag_counts: Dict[str, int] = {}
    tag_post_map: Dict[str, List[str]] = {}

    for post in posts:
        badges = post.get('badge', '').split(',') if post.get('badge') else []
        for badge in badges:
            badge = badge.strip()
            if badge:
                tag_counts[badge] = tag_counts.get(badge, 0) + 1
                if badge not in tag_post_map:
                    tag_post_map[badge] = []
                tag_post_map[badge].append(post['file_name'])

    # 生成共现矩阵
    tags = sorted(tag_counts.keys())
    cooccurrence = [[0] * len(tags) for _ in range(len(tags))]

    for post in posts:
        badges = post.get('badge', '').split(',')
        badge_indices = [tags.index(b.strip()) for b in badges if b.strip() in tags]
        for i in badge_indices:
            for j in badge_indices:
                if i != j:
                    cooccurrence[i][j] += 1

    return {
        "tags": tags,
        "counts": tag_counts,
        "cooccurrence": cooccurrence,
        "post_mapping": tag_post_map
    }

def generate_type_matrix(posts: List[Dict[str, Any]]) -> Dict[str, int]:
    """生成文章类型统计矩阵"""
    type_counts = {}
    for post in posts:
        post_type = post.get('type', 'article')
        type_counts[post_type] = type_counts.get(post_type, 0) + 1
    return type_counts

def generate_date_matrix(posts: List[Dict[str, Any]]) -> Dict[str, int]:
    """生成日期统计矩阵"""
    from datetime import datetime
    date_counts = {}

    for post in posts:
        try:
            date_str = post.get('date')
            if date_str:
                date = datetime.strptime(date_str[:10], "%Y-%m-%d").date()
                year_month = date.strftime("%Y-%m")
                date_counts[year_month] = date_counts.get(year_month, 0) + 1
        except Exception:
            continue

    return dict(sorted(date_counts.items()))

def save_matrix_data(matrix_data: Dict[str, Any]) -> None:
    """保存矩阵数据到 JSON 文件"""
    output_path = DATA_DIR / "matrices.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(matrix_data, f, ensure_ascii=False, indent=2)
    print(f"💾 矩阵数据已保存到 {output_path}")

def main():
    """主函数"""
    print("🔄 加载文章 frontmatter...")
    posts = load_posts_frontmatter()
    if not posts:
        print("⚠️ 未找到任何文章，跳过矩阵生成")
        return

    print(f"📊 找到 {len(posts)} 篇文章")
    print("🔧 生成标签矩阵...")
    tag_matrix = generate_tag_matrix(posts)

    print("🔧 生成类型矩阵...")
    type_matrix = generate_type_matrix(posts)

    print("🔧 生成日期矩阵...")
    date_matrix = generate_date_matrix(posts)

    matrix_data = {
        "tags": tag_matrix,
        "types": type_matrix,
        "dates": date_matrix,
        "total_posts": len(posts)
    }

    print("💾 保存矩阵数据...")
    save_matrix_data(matrix_data)
    print("✅ 矩阵生成完成")

if __name__ == "__main__":
    main()
