#!/usr/bin/env python3
"""
示例脚本：使用环境变量中配置的 ark-code-latest 模型进行对话和代码优化
"""

import os
import httpx
import argparse
import json
from typing import Optional

def get_env_variable(name: str) -> Optional[str]:
    """获取环境变量"""
    value = os.getenv(name)
    if not value:
        print(f"错误：未设置 {name} 环境变量")
    return value

def call_ark_code_model(api_key: str, base_url: str, model: str, messages: list, max_tokens: int = 1024) -> dict:
    """
    调用 ark-code-latest 模型

    Args:
        api_key: API 密钥
        base_url: API 基础 URL
        model: 模型名称
        messages: 对话消息列表
        max_tokens: 最大生成 token 数

    Returns:
        模型响应字典
    """
    try:
        url = f"{base_url}/v1/messages"
        headers = {
            "Content-Type": "application/json",
            "x-api-key": api_key
        }
        data = {
            "model": model,
            "max_tokens": max_tokens,
            "messages": messages
        }

        response = httpx.post(url, headers=headers, json=data, timeout=60)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"API 请求失败 (状态码: {response.status_code})")
            print(f"响应内容: {response.text}")
            return None

    except httpx.TimeoutException:
        print("错误：请求超时")
        return None
    except httpx.NetworkError:
        print("错误：网络连接失败")
        return None
    except Exception as e:
        print(f"错误：{e}")
        import traceback
        print(traceback.format_exc())
        return None

def print_response(response: dict):
    """打印模型响应"""
    if not response:
        return

    print(f"\n模型回复：")
    for content_block in response['content']:
        if content_block['type'] == 'text':
            print(content_block['text'])

    print(f"\n回复信息：")
    print(f"  模型: {response.get('model', '未知')}")
    print(f"  输入 tokens: {response['usage']['input_tokens']}")
    print(f"  输出 tokens: {response['usage']['output_tokens']}")
    print(f"  总 tokens: {response['usage']['input_tokens'] + response['usage']['output_tokens']}")

def code_optimization_example():
    """代码优化示例"""
    print("=== 代码优化示例 ===")
    print()

    # 待优化的代码
    original_code = """
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    """.strip()

    messages = [
        {
            "role": "user",
            "content": f"""
你是一位资深的 Python 代码优化专家。请分析以下 Python 代码，并进行优化。

优化要求：
1. 提高执行效率
2. 提升代码可读性
3. 修复潜在的性能问题
4. 加入适当的注释说明

原始代码：
```python
{original_code}
```

请提供优化后的代码，并详细说明修改点。
"""
        }
    ]

    return messages

def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="调用 ark-code-latest 模型进行代码优化")
    parser.add_argument("--task", type=str, default="code_optimization", help="任务类型：code_optimization 或 custom")
    parser.add_argument("--message", type=str, help="自定义消息（当 task=custom 时需要）")
    parser.add_argument("--max-tokens", type=int, default=2048, help="最大生成 token 数")
    args = parser.parse_args()

    # 获取环境变量配置
    api_key = get_env_variable("ANTHROPIC_AUTH_TOKEN")
    base_url = get_env_variable("ANTHROPIC_BASE_URL")
    model = get_env_variable("ANTHROPIC_MODEL")

    if not all([api_key, base_url, model]):
        return

    print(f"使用配置：")
    print(f"  API Key: {api_key[:8]}...")
    print(f"  Base URL: {base_url}")
    print(f"  Model: {model}")
    print()

    # 准备对话消息
    if args.task == "code_optimization":
        messages = code_optimization_example()
    elif args.task == "custom" and args.message:
        messages = [{"role": "user", "content": args.message}]
    else:
        print("错误：任务类型无效或自定义消息未提供")
        return

    # 调用模型
    print("正在调用 ark-code-latest 模型...")
    response = call_ark_code_model(api_key, base_url, model, messages, args.max_tokens)

    # 打印响应
    print_response(response)

if __name__ == "__main__":
    main()
