#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI 自动代笔引擎 (Autonomous Ghostwriter)
监控指定目录（如 Inbox），将用户的碎片化灵感自动扩写为结构完整的爆款长文。
"""
import os
import re
import sys
import json
import urllib.request

OBSIDIAN_VAULT = "/Users/hulimofaqiu/Documents/obisidian笔记文件/"
INBOX_DIR = os.path.join(OBSIDIAN_VAULT, "Inbox")
# 加载 .env
ENV_PATH = "/Users/hulimofaqiu/mengxi-first-ai-project/.env"
if os.path.exists(ENV_PATH):
    with open(ENV_PATH) as f:
        for line in f:
            if '=' in line and not line.startswith('#'):
                k, v = line.strip().split('=', 1)
                os.environ[k.strip()] = v.strip().strip('"')

API_KEY = os.environ.get("MISTRAL_API_KEY", "")

def expand_article_with_llm(content):
    if not API_KEY: 
        print("未找到 MISTRAL_API_KEY")
        return None
    
    proxy_handler = urllib.request.ProxyHandler({'http': 'http://127.0.0.1:7897', 'https': 'http://127.0.0.1:7897'})
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)

    url = "https://api.mistral.ai/v1/chat/completions"
    
    prompt = f"""
    你是一个极其出色的代笔作家与内容架构师。你的雇主是一位充满温度的新手妈妈（她同时也是具备极客素养的探索者）。
    她平时非常忙碌，只能随手在 Obsidian 里记录一些【碎片化的想法、流水账或关键词】。
    
    你的任务是将下面这段粗糙的“碎片灵感”，彻底扩写并润色成一篇高质量、结构清晰、引人入胜的博客文章。
    
    【写作要求】
    1. 语气：温暖、极客、有洞察力、娓娓道来，符合高素养女性的口吻。一定要用中文输出。
    2. 结构：必须有一个吸引人的标题（一级标题 #），清晰的段落，适当使用加粗、引言（>）或列表。
    3. 深度：如果她提到育儿，适当结合一点点科学育儿规律或个人感悟；如果是日常，写出深刻的体悟。字数建议在 600 - 1500字之间。
    4. 格式：在开头必须输出标准的 YAML Frontmatter，包括：
       title: "想一个棒极了的文章标题"
       date: "2026-03-31" 
       tags: [灵感, 生活] (请根据内容自动生成)
       type: "article"
       publish: true
       
       注意：一定要加上 publish: true，确保这篇扩写后的文章进入自动发布管线！
    
    【用户的原始碎片灵感】
    ---
    {content}
    ---
    
    请直接输出完整的 Markdown 文件内容（包含 Frontmatter 和正文），不要有多余的解释。
    """
    
    payload = {
        "model": "mistral-large-latest",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.65
    }
    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}'
        })
        with urllib.request.urlopen(req, timeout=90) as res:
            data = json.loads(res.read().decode('utf-8'))
            text = data['choices'][0]['message']['content']
            
            if text.startswith("```markdown"): text = text[len("```markdown"):].strip()
            if text.endswith("```"): text = text[:-3].strip()
            return text
    except Exception as e:
        print(f" LLM 代笔失败: {e}")
        return None

def main():
    if not os.path.exists(INBOX_DIR):
        os.makedirs(INBOX_DIR, exist_ok=True)
        print(f"📦 已为您创建灵感收件箱 Inbox: {INBOX_DIR}")
        
    for filename in os.listdir(INBOX_DIR):
        if not filename.endswith('.md'):
            continue
            
        filepath = os.path.join(INBOX_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            
        # 如果没有内容或已经写了 Frontmatter (说明已经是一篇正式文章)，或者字数>1000，则跳过
        if not content or content.startswith("---") or len(content) > 1000:
            continue
             
        print(f"💡 发现灵感碎片 [{filename}]，字数 {len(content)}，正在呼叫 Gemini Pro 引擎扩写...")
        expanded_content = expand_article_with_llm(content)
        
        if expanded_content:
            title_match = re.search(r'title:\s*["\']([^"\']+)["\']', expanded_content)
            if not title_match:
                title_match = re.search(r'title:\s*([^\n]+)', expanded_content)
                
            new_title = title_match.group(1) if title_match else filename.replace('.md', '')
            safe_title = re.sub(r'[\\/*?:"<>|#\n]', "", new_title).strip()
            
            publish_dir = os.path.join(OBSIDIAN_VAULT, "AI生成稿件")
            os.makedirs(publish_dir, exist_ok=True)
            
            new_filepath = os.path.join(publish_dir, f"{safe_title}.md")
            counter = 1
            while os.path.exists(new_filepath):
                new_filepath = os.path.join(publish_dir, f"{safe_title}-{counter}.md")
                counter += 1
                
            with open(new_filepath, 'w', encoding='utf-8') as f:
                f.write(expanded_content)
                
            print(f"✅ 扩写成功！已保存完整的文章至: {new_filepath}")
            os.rename(filepath, filepath + '.bak')

if __name__ == "__main__":
    main()
