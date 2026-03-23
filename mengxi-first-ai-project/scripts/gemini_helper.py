#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import ark_helper

def generate_summary(text_content):
    system_prompt = """
你是一个专业的育儿和教育AI助手。请针对以下拉取到的小红书贴子内容，提供一个**详细的要点总结**。
总结应当：
1. **提炼核心观点**（博主的核心建议、知识点）。
2. **整理热门讨论/避坑指南**（如果有提及实操经验、注意事项、避坑点）。
3. 结构清晰，使用 Markdown 符号分点表达，语言通俗易懂，带有亲和力。
"""
    return ark_helper.call_ark_summarize(text_content, system_prompt=system_prompt)
