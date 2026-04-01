#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
quality_guard.py — 🛡️ 内容质量护栏（LLM-as-a-Judge）
═══════════════════════════════════════════════════════════
"""

import sys
import logging
from pathlib import Path

# 路径配置
PROJECT_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = PROJECT_DIR / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

try:
    from inference_helper import ask_llm
except ImportError:
    from scripts.inference_helper import ask_llm

logger = logging.getLogger(__name__)

# ══════════════════════════════════════════════════════════
# 📚 少样本示例库 (Few-Shot Calibration)
# ──────────────────────────────────────────────────────────
# 提示：在这里填入你认为“烂”和“好”的真实案例，校准 AI 裁判的品味。
# ══════════════════════════════════════════════════════════

FEW_SHOT_EXAMPLES = """
### [BAD_EXAMPLE: AI Slop / 令人尴尬的废料]
"🔥 绝绝子！一定要看！今天给大家分享一个 Python 循环的小技巧，真的好用到哭！😭 
小白也能秒懂，快动动小手收藏起来吧！✨ #Python #编程启蒙 #极客妈妈"
➡️ 判定理据：过度使用俗套 Emoji、毫无信息密度的营销话术、典型的 AI 工业糖精。

### [GOOD_EXAMPLE: 真诚自然 / 高信息密度]
"写了 10 年代码，我发现 Python 的 for 循环本质上是一场关于‘数据契约’的博弈。
相比于 C 风格的下标递增，Pythonic 的迭代更像是在阅读一份清晰的清单。
如果你还在为 Index 出界而苦恼，可能需要重新理解 Iterator 模式。"
➡️ 判定理据：观点鲜明、专业主义、语气真诚、不堆砌流行词。
"""

JUDGE_PROMPT_TEMPLATE = """
你是一位拥有极高品味的资深内容主编，极其厌恶无脑的“AI 工业废料（AI Slop）”。
请评估以下生成的宣发内容。

## 品味准则：
- **拒绝**: 俗套的 Emoji 堆砌（如“绝绝子”、“好用到哭”）、空洞的废话、典型的营销号口吻、让人感到尴尬的代码解释。
- **认可**: 见解独到、真诚自然、具备专业主义、信息密度高、能引起读者深度共鸣。

## 参考示例：
{few_shot}

## 待评估内容：
{content}

## 任务：
1. 进行二元判定（PASS/FAIL）：
   - 如果内容读起来像机器废料或令人尴尬，请输出 FAIL。
   - 如果内容真诚、专业且高质量，请输出 PASS。
2. 如果判定为 FAIL，请给出一句尖锐的、针对性的批评意见，指出哪里最尴尬。

## 输出格式（严格 JSON）：
{{
  "decision": "PASS" 或 "FAIL",
  "critique": "如果不通过，提供具体的重构建议"
}}
"""

def quality_guardrail_check(content_json_str: str) -> dict:
    """
    内容质量护栏：调用 LLM 进行二元裁判。
    返回: {"decision": "PASS"/"FAIL", "critique": "..."}
    """
    prompt = JUDGE_PROMPT_TEMPLATE.format(
        few_shot=FEW_SHOT_EXAMPLES,
        content=content_json_str
    )
    
    response = ask_llm(prompt)
    if not response:
        return {"decision": "FAIL", "critique": "LLM 裁判未响应"}
    
    import json
    import re
    try:
        # 解析 JSON 判定
        json_match = re.search(r'\{(?:.|\n)*?\}', response)
        if json_match:
            return json.loads(json_match.group(0))
    except Exception as e:
        logger.error(f"❌ 裁判逻辑异常: {e}")
        
    return {"decision": "FAIL", "critique": "解析裁判意见失败"}
