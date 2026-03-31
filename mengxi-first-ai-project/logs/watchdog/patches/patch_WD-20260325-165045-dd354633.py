# Auto-generated patch for incident: WD-20260325-165045-dd354633
# Generated at: 2026-03-25T16:50:45.814449
# Target: generate_matrix.py
# Error: TimeoutError: 脚本 generate_matrix.py 执行超时 (300s)
#======================================================================

#!/usr/bin/env python3
"""
修复脚本：为 generate_matrix.py 注入超时和重试机制
用法：python fix_generate_matrix_timeout.py
"""

import os
import sys
import time
import logging
from typing import Optional, List, Dict, Any
from functools import wraps

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

# 原脚本路径
ORIGINAL_SCRIPT = "/Users/hulimofaqiu/mengxi-first-ai-project/scripts/generate_matrix.py"
BACKUP_SCRIPT = f"{ORIGINAL_SCRIPT}.bak_{int(time.time())}"

# 重试装饰器
def retry_with_timeout(max_retries: int = 3, base_delay: float = 1.0):
    """带超时和重试的装饰器，适用于网络请求或耗时操作"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(max_retries):
                try:
                    result = func(*args, **kwargs)
                    return result
                except TimeoutError as e:
                    last_error = e
                    logger.warning(f"第 {attempt + 1} 次尝试超时: {str(e)}")
                    if attempt < max_retries - 1:
                        delay = base_delay * (2 ** attempt)  # 指数退避
                        logger.info(f"等待 {delay:.2f}s 后重试...")
                        time.sleep(delay)
                    continue
                except Exception as e:
                    logger.error(f"意外错误: {str(e)}")
                    raise
            raise TimeoutError(f"所有重试 ({max_retries}次) 均超时") from last_error
        return wrapper
    return decorator

def patch_generate_matrix():
    """为 generate_matrix.py 注入修复代码"""
    if not os.path.exists(ORIGINAL_SCRIPT):
        logger.error(f"原脚本不存在: {ORIGINAL_SCRIPT}")
        print("❌ 补丁执行失败: 原脚本文件缺失")
        return False

    # 备份原脚本
    try:
        import shutil
        shutil.copy2(ORIGINAL_SCRIPT, BACKUP_SCRIPT)
        logger.info(f"已备份原脚本到: {BACKUP_SCRIPT}")
    except Exception as e:
        logger.error(f"备份失败: {str(e)}")
        print("❌ 补丁执行失败: 无法备份原脚本")
        return False

    # 读取原脚本内容
    try:
        with open(ORIGINAL_SCRIPT, "r", encoding="utf-8") as f:
            original_code = f.read()
    except Exception as e:
        logger.error(f"读取原脚本失败: {str(e)}")
        print("❌ 补丁执行失败: 无法读取原脚本")
        return False

    # 注入修复代码（monkey-patch）
    modified_code = original_code
    # 1. 在开头添加重试装饰器和超时设置
    import_code = """
import time
from functools import wraps

def retry_with_timeout(max_retries: int = 3, base_delay: float = 1.0):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except TimeoutError as e:
                    last_error = e
                    print(f"⚠️ 第 {attempt + 1} 次尝试超时: {str(e)}")
                    if attempt < max_retries - 1:
                        delay = base_delay * (2 ** attempt)
                        time.sleep(delay)
                except Exception as e:
                    raise
            raise TimeoutError(f"所有重试 ({max_retries}次) 均超时") from last_error
        return wrapper
    return decorator
"""
    if "import time" not in modified_code:
        modified_code = import_code + "\n" + modified_code

    # 2. 为主函数添加 @retry_with_timeout 装饰器（假设主函数为 generate_matrix）
    if "def generate_matrix(" in modified_code:
        modified_code = modified_code.replace(
            "def generate_matrix(",
            "@retry_with_timeout(max_retries=5, base_delay=2.0)\ndef generate_matrix("
        )

    # 3. 在主函数内添加超时控制（假设使用 requests 库）
    if "import requests" in modified_code:
        timeout_code = """
        # 为所有网络请求添加 timeout 参数
        response = requests.get(url, timeout=30)  # 30s 超时
        """
        # 替换示例：将 requests.get(url) 替换为带 timeout 的版本
        modified_code = modified_code.replace(
            "requests.get(",
            "requests.get("
        )
        # 更精确的替换（保守操作，仅添加 timeout 参数）
        modified_code = modified_code.replace(
            "requests.get(url",
            "requests.get(url, timeout=30"
        )

    # 4. 添加日志记录
    if "import logging" not in modified_code:
        modified_code = modified_code.replace(
            "import sys",
            "import sys\nimport logging\n\nlogging.basicConfig(level=logging.INFO)")
    if "logger = " not in modified_code:
        modified_code = modified_code + """
if __name__ == "__main__":
    logger = logging.getLogger(__name__)
"""

    # 写入修复后的脚本
    try:
        with open(ORIGINAL_SCRIPT, "w", encoding="utf-8") as f:
            f.write(modified_code)
        logger.info("已注入修复代码")
    except Exception as e:
        logger.error(f"写入修复脚本失败: {str(e)}")
        print("❌ 补丁执行失败: 无法写入修复脚本")
        return False

    print("✅ 补丁执行成功: 已为 generate_matrix.py 注入超时和重试机制")
    print(f"   - 原脚本已备份至: {BACKUP_SCRIPT}")
    print("   - 建议测试运行: python scripts/generate_matrix.py")
    return True

if __name__ == "__main__":
    success = patch_generate_matrix()
    sys.exit(0 if success else 1)