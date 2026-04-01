#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
智能大纲生成器 (Autonomous Diagram Generator)
利用 LLM 阅读文章，提取信息架构，转为 Mermaid 语法，
并调用 Kroki 渲染为漂亮的 SVG 存放在 Markdown 同级目录。
"""

import os
import re
import sys
import json
import time
import requests
from urllib import request

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PROJECT_DIR, 'scripts'))
from privacy_filter import should_publish

OBSIDIAN_VAULT = "/Users/hulimofaqiu/Documents/obisidian笔记文件/"
API_KEY = os.environ.get("GEMINI_API_KEY", "")

def ask_llm_mermaid(content):
    if not API_KEY: return None
    proxy_handler = request.ProxyHandler({'http': 'http://127.0.0.1:7897', 'https': 'http://127.0.0.1:7897'})
    opener = request.build_opener(proxy_handler)
    request.install_opener(opener)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}"
    prompt = f"""
    你是一个擅长提炼信息架构的高级产品经理。
    请阅读以下文章片段，将其核心逻辑、步骤或概念结构提炼为一个极其精简的逻辑图。
    
    【要求】
    1. 必须使用 Mermaid 语法 (推荐使用 graph TD 或 mindmap)。
    2. 节点文字必须极度简短（控制在 8 个字以内）。
    3. 只需刻画核心的 3~6 个关键节点。
    4. 可以使用简单的色彩和样式（比如为头节点加上 classDef）。
    5. 只输出 ```mermaid ... ``` 代码块，不要任何多余废话。
    
    【文章内容】
    {content[:3000]}
    """
    payload = {"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"temperature": 0.2}}
    try:
        req = request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
        with request.urlopen(req, timeout=30) as res:
            data = json.loads(res.read().decode('utf-8'))
            text = data['candidates'][0]['content']['parts'][0]['text']
            match = re.search(r'```mermaid\n(.*?)\n```', text, re.DOTALL)
            return match.group(1).strip() if match else None
    except Exception as e:
        print(f" LLM 生成失败: {e}")
        return None

def render_to_svg(mermaid_code):
    try:
        import json as _json
        payload = _json.dumps({"diagram_source": mermaid_code, "diagram_type": "mermaid", "output_format": "svg"}).encode('utf-8')
        # 使用 Kroki (非常稳定的开源绘图 API) — 走代理避免 GFW 超时
        proxy_handler = request.ProxyHandler({'http': 'http://127.0.0.1:7897', 'https': 'http://127.0.0.1:7897'})
        opener = request.build_opener(proxy_handler)
        req = request.Request("https://kroki.io/", data=payload, headers={'Content-Type': 'application/json'})
        with opener.open(req, timeout=15) as res:
            return res.read().decode('utf-8')
    except Exception as e:
        print(f" Kroki 渲染失败: {e}")
    return None

def is_valid_article(filepath, content):
    if not should_publish(filepath, OBSIDIAN_VAULT, content): return False
    exclude_patterns = ['00', '01', 'Drawing', '!Pasted', 'Excalidraw']
    if any(p in os.path.basename(filepath) for p in exclude_patterns): return False
    
    if re.search(r'^publish:\s*true\s*$', content, re.MULTILINE | re.IGNORECASE): return True
    if '#publish' in content.lower() or len(content) > 1200: return True
    return False

def main():
    print("开始扫描缺失结构图的文章...")
    processed = 0
    max_batch = 3 # 每次只生成 3 篇，防超时
    
    for root, _, files in os.walk(OBSIDIAN_VAULT):
        if processed >= max_batch: break
        for f in files:
            if processed >= max_batch: break
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                base_name = os.path.splitext(f)[0]
                
                # 如果已经存在大纲图，则跳过
                has_diagram = any(os.path.exists(os.path.join(root, base_name + ext)) 
                                  for ext in ['.svg', '.excalidraw', '.excalidraw.svg'])
                if has_diagram: continue
                
                with open(filepath, 'r', encoding='utf-8') as mf:
                    content = mf.read()
                
                if not is_valid_article(filepath, content):
                    continue
                    
                print(f" 🎯 发现待生成大纲文章: {f}")
                mermaid_code = ask_llm_mermaid(content)
                if mermaid_code:
                    svg_content = render_to_svg(mermaid_code)
                    if svg_content:
                        svg_path = os.path.join(root, f"{base_name}.svg")
                        with open(svg_path, 'w', encoding='utf-8') as sf:
                            sf.write(svg_content)
                        print(f"   => ✅ SVG 大纲生成成功: {base_name}.svg")
                        processed += 1
                        time.sleep(2) # 礼貌延迟

    print(f"自动绘图检查完成。本次新生成了 {processed} 张大纲图。")

if __name__ == "__main__":
    main()
