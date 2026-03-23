#!/usr/bin/env python3
import urllib.request
import urllib.error
import json
import os
import time

def call_gemini_fallback(text_content, system_prompt):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return "⚠️ 未配置 GEMINI_API_KEY，无法生成 AI 视图"
    
    g_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    prompt = f"{system_prompt}\n\n以下是需要处理的文本内容：\n{text_content}"
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    
    import urllib.request
    try:
        req = urllib.request.Request(
            g_url,
            data=json.dumps(payload).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        with urllib.request.urlopen(req, timeout=12) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            candidates = res_data.get('candidates', [])
            if candidates:
                text = candidates[0].get('content', {}).get('parts', [{}])[0].get('text', '')
                return text.strip()
            return "⚠️ Gemini 生成未返回候选项"
    except Exception as e:
        return f"⚠️ AI 会话均异常: {e}"

def call_ark_summarize(text_content, system_prompt="你是一个专业的总结助手。请精准提取核心要点和避坑指南，剔除修饰语。"):
    if text_content and len(text_content) > 600:
        # print(f"[Ark Skip] Text too large ({len(text_content)} chars), bypassing to Gemini.")
        return call_gemini_fallback(text_content, system_prompt)

    api_key = os.environ.get("ARK_API_KEY")
    if not api_key:
        print("[Ark Warning] ARK_API_KEY is missing. Falling back to Gemini.")
        return call_gemini_fallback(text_content, system_prompt)
    
    url = "https://ark.cn-beijing.volces.com/api/coding/v3/chat/completions"
    req_body = {
        "model": "ark-code-latest",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text_content}
        ],
        "temperature": 0.4
    }
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    
    attempts = 2 # 减少重试次数
    backoff = 3
    for i in range(attempts):
        req = urllib.request.Request(
            url,
            data=json.dumps(req_body).encode('utf-8'),
            headers=headers
        )
        try:
            with urllib.request.urlopen(req, timeout=5) as response: # 锁定 5s 超时快降级
                res_data = json.loads(response.read().decode('utf-8'))
                choices = res_data.get("choices", [])
                if choices:
                    return choices[0].get("message", {}).get("content", "")
                return "⚠️ AI 生成未返回候选项"
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print(f"[Ark 429] 限流，休眠 {backoff}s...")
                time.sleep(backoff)
                backoff *= 1.5
            else:
                print(f"[Ark Fallback] HTTP {e.code} Error. Trying Gemini...")
                return call_gemini_fallback(text_content, system_prompt)
        except Exception as e:
            print(f"[Ark Fallback] Exception: {e}. Trying Gemini...")
            return call_gemini_fallback(text_content, system_prompt)
    
    return call_gemini_fallback(text_content, system_prompt)
