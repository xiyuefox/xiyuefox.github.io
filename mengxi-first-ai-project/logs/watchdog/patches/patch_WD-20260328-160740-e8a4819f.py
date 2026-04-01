# Auto-generated patch for incident: WD-20260328-160740-e8a4819f
# Generated at: 2026-03-28T16:07:40.133665
# Target: fetch_hn_feed.py
# Error: TimeoutError: 脚本 fetch_hn_feed.py 执行超时 (300s)
#======================================================================

#!/usr/bin/env python3
"""
修复脚本：fetch_hn_feed.py 超时问题
通过重试机制和请求优化，避免网络波动导致的脚本执行超时
"""

import os
import json
import time
import logging
import requests
from typing import Optional, Dict, Any

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# 重试配置
MAX_RETRIES = 3
INITIAL_RETRY_DELAY = 2  # 秒
BACKOFF_FACTOR = 2

# Hacker News API 配置
HN_API_BASE = "https://hacker-news.firebaseio.com/v0/"
ENDPOINTS = {
    "top_stories": "topstories.json",
    "item": "item/{}.json"
}

def fetch_with_retry(url: str, params: Optional[Dict] = None, timeout: int = 10) -> Optional[Dict]:
    """
    带重试机制的 HTTP GET 请求
    :param url: 请求 URL
    :param params: 查询参数
    :param timeout: 单次请求超时（秒）
    :return: JSON 响应或 None（失败）
    """
    retry_count = 0
    last_exception = None

    while retry_count < MAX_RETRIES:
        try:
            response = requests.get(
                url,
                params=params,
                timeout=timeout,
                headers={"User-Agent": "MengxiSpace-FetchBot/1.0"}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            last_exception = e
            retry_count += 1
            if retry_count < MAX_RETRIES:
                delay = INITIAL_RETRY_DELAY * (BACKOFF_FACTOR ** (retry_count - 1))
                logger.warning(f"请求失败 (尝试 {retry_count}/{MAX_RETRIES}): {e}. {delay}秒后重试...")
                time.sleep(delay)
            continue

    logger.error(f"请求最终失败: {last_exception}")
    return None

def fetch_top_stories() -> Optional[list]:
    """获取热门故事 ID 列表"""
    url = f"{HN_API_BASE}{ENDPOINTS['top_stories']}"
    return fetch_with_retry(url)

def fetch_story_details(story_id: int) -> Optional[Dict]:
    """获取单个故事的详细信息"""
    url = f"{HN_API_BASE}{ENDPOINTS['item'].format(story_id)}"
    return fetch_with_retry(url)

def process_stories(story_ids: list) -> list:
    """处理故事列表，过滤无效数据"""
    stories = []
    for story_id in story_ids[:50]:  # 限制处理前50条避免超时
        story = fetch_story_details(story_id)
        if not story:
            continue
        # 基础过滤：必须包含标题和URL
        if not all([story.get("title"), story.get("url")]):
            continue
        stories.append({
            "id": story["id"],
            "title": story["title"],
            "url": story["url"],
            "score": story.get("score", 0),
            "by": story.get("by", ""),
            "time": story.get("time", int(time.time()))
        })
    return stories

def save_to_json(data: list, filename: str) -> bool:
    """将数据保存为 JSON 文件"""
    output_dir = "data"
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logger.info(f"数据已保存: {filepath}")
        return True
    except Exception as e:
        logger.error(f"保存文件失败: {e}")
        return False

def main():
    """主执行函数"""
    logger.info("开始抓取 Hacker News 热门故事...")

    # 第一步：获取热门故事 ID
    story_ids = fetch_top_stories()
    if not story_ids:
        logger.error("无法获取热门故事列表")
        return False

    logger.info(f"获取到 {len(story_ids)} 个热门故事")

    # 第二步：获取故事详情并处理
    stories = process_stories(story_ids)
    logger.info(f"成功处理 {len(stories)} 条故事")

    # 第三步：保存结果
    if not save_to_json(stories, "hn_top_stories.json"):
        return False

    return True

if __name__ == "__main__":
    success = main()
    if success:
        print("✅ 补丁执行成功")
    else:
        print("❌ 补丁执行失败: 数据抓取或保存过程中出现错误")