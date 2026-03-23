import os
import requests

# 加载 .env 环境变量以防未读入
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(PROJECT_DIR, ".env")
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                try:
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value.replace('"', '').replace("'", "")
                except ValueError:
                    pass

def ask_llm(prompt):
    """
    统一推理接口：支持 Gemini 2.5 Flash 第一轮请求，如果失败/封锁/配额耗尽，
    自动平滑降级（Fallback）到 Mistral AI 节点。
    """
    api_key_gemini = os.environ.get("GEMINI_API_KEY")
    api_key_mistral = os.environ.get("MISTRAL_API_KEY")

    # 🔍 1. 第一优先级：Gemini 2.5 Flash
    if api_key_gemini:
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key_gemini}"
            headers = {'Content-Type': 'application/json'}
            payload = {"contents": [{"parts": [{"text": prompt}]}]}
            
            res = requests.post(url, headers=headers, json=payload, timeout=20)
            if res.status_code == 200:
                data = res.json()
                parts = data.get('candidates', [{}])[0].get('content', {}).get('parts', [])
                if parts:
                    text = parts[0].get('text', '').strip()
                    if text:
                        return text
            print(f"   ⚠️ Gemini 接口返回异常 (状态码: {res.status_code})，尝试降级至 Mistral...")
        except Exception as e:
            print(f"   ⚠️ Gemini 调用超时或异常: {e}，尝试降级至 Mistral...")

    # 🛡️ 2. 第二优先级：Mistral AI (Fallback)
    if api_key_mistral:
        try:
            url = "https://api.mistral.ai/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {api_key_mistral}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "mistral-small-latest",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7
            }
            
            res = requests.post(url, headers=headers, json=payload, timeout=30)
            if res.status_code == 200:
                data = res.json()
                choices = data.get('choices', [])
                if choices:
                    text = choices[0].get('message', {}).get('content', '').strip()
                    if text:
                        print("   ✅ 成功通过 Mistral AI 发起降级续航响应！")
                        return text
            print(f"   ❌ Mistral 降级接口也异常 (状态码: {res.status_code})")
        except Exception as e:
            print(f"   ❌ Mistral 降级调用失败: {e}")

    # 🔗 3. 第三优先级：Perplexity AI (Research/Fallback)
    api_key_perplexity = os.environ.get("PERPLEXITY_API_KEY")
    if api_key_perplexity and 'pplx-' in api_key_perplexity:
        try:
            url = "https://api.perplexity.ai/chat/completions"
            headers = {
                "Authorization": f"Bearer {api_key_perplexity}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "sonar", # 高级联网搜索节点
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 1000
            }
            res = requests.post(url, headers=headers, json=payload, timeout=30)
            if res.status_code == 200:
                data = res.json()
                choices = data.get('choices', [])
                if choices:
                    print("   ✅ 成功通过 Perplexity AI 发起降级续航响应！")
                    return choices[0].get('message', {}).get('content', '').strip()
        except Exception:
            pass

    print("   🚨 所有 AI 推理通道全部耗尽/超时，未能获取摘要。")
    return ""
