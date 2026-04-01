#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📥 私人主编·收件箱降噪引擎 (Private Inbox Editor — Gmail Digest Engine)

每日定时拉取 Gmail 中过去 24 小时的 Newsletter / 资讯订阅邮件，
由 LLM 扮演品味极高的"主编"，提炼 3-5 条真正有价值的硬核洞察，
输出为 Obsidian Markdown 文件（tags: [private-briefing]），
并确保不会出现在网站的公共时间线中。

Pipeline Position: sync.sh Phase 1.5
Privacy: private-briefing 标签 → sync_obsidian.py 硬性跳过 → 不部署到 Cloudflare
"""
import os
import sys
import re
import json
import base64
import datetime
import urllib.request
from email.utils import parsedate_to_datetime

# ── 路径与环境 ────────────────────────────────────────────
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OBSIDIAN_VAULT = "/Users/hulimofaqiu/Documents/obisidian笔记文件/"
OUTPUT_DIR = os.path.join(OBSIDIAN_VAULT, "daily_brief")
TOKEN_PATH = os.path.join(PROJECT_DIR, "token.json")
CREDS_PATH = os.path.join(PROJECT_DIR, "credentials.json")

# 加载 .env
ENV_PATH = os.path.join(PROJECT_DIR, ".env")
if os.path.exists(ENV_PATH):
    with open(ENV_PATH) as f:
        for line in f:
            if '=' in line and not line.startswith('#'):
                k, v = line.strip().split('=', 1)
                os.environ[k.strip()] = v.strip().strip('"')

# LLM API Keys (Gemini 主力, Mistral 备用)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY", "")

# ── Newsletter 发件人/关键词白名单 ────────────────────────
# 只有匹配这些模式的邮件才会被拉取，避免私人对话泄露
NEWSLETTER_PATTERNS = [
    "newsletter", "digest", "weekly", "daily", "update",
    "noreply", "no-reply", "notification", "info@", "hello@",
    "substack.com", "mailchimp", "convertkit", "revue",
    "medium.com", "producthunt", "hackernewsletter",
    "tldrnewsletter", "morningbrew", "theinformation",
    "platformer", "stratechery", "lenny", "rundown",
    "therundown", "waigenie", "aibreakfast", "superhuman",
    "techcrunch", "oreilly", "smashingmagazine",
    "alistapart", "css-tricks", "react", "vercel",
    "arxiv", "deeplearning.ai", "huggingface",
    "swiftui", "apple", "google", "developer",
]

# 排除列表：纯广告 / 交易类
EXCLUDE_PATTERNS = [
    "receipt", "invoice", "order", "shipping", "tracking",
    "password", "verification", "security alert",
    "unsubscribe only", "promotional",
]


def get_gmail_service():
    """获取已授权的 Gmail API 服务实例"""
    try:
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from googleapiclient.discovery import build
    except ImportError:
        print("⚠️  缺少 Google API 依赖。请先运行: python3 scripts/setup_gmail_auth.py")
        return None

    if not os.path.exists(TOKEN_PATH):
        print("⚠️  未找到 token.json。请先运行: python3 scripts/setup_gmail_auth.py")
        return None

    creds = Credentials.from_authorized_user_file(TOKEN_PATH,
                                                   ['https://www.googleapis.com/auth/gmail.readonly'])
    if creds.expired and creds.refresh_token:
        try:
            creds.refresh(Request())
            with open(TOKEN_PATH, 'w') as token:
                token.write(creds.to_json())
            print("🔄 Gmail token 已自动刷新")
        except Exception as e:
            print(f"❌ Token 刷新失败: {e}。请重新运行 setup_gmail_auth.py")
            return None

    return build('gmail', 'v1', credentials=creds)


def is_newsletter(headers_dict, snippet):
    """智能判断邮件是否为 Newsletter / 资讯类"""
    sender = headers_dict.get('From', '').lower()
    subject = headers_dict.get('Subject', '').lower()
    list_id = headers_dict.get('List-Unsubscribe', '')
    combined = f"{sender} {subject} {snippet}".lower()

    # 有 List-Unsubscribe 头 = 大概率是 Newsletter
    if list_id:
        return True

    # 匹配白名单关键词
    for pattern in NEWSLETTER_PATTERNS:
        if pattern in combined:
            return True

    # 排除明确的交易类
    for pattern in EXCLUDE_PATTERNS:
        if pattern in combined:
            return False

    return False


def fetch_recent_emails(service, hours=24, max_results=50):
    """拉取过去 N 小时内的 Newsletter 类邮件"""
    after_epoch = int((datetime.datetime.now() - datetime.timedelta(hours=hours)).timestamp())
    query = f"after:{after_epoch} category:updates OR category:promotions OR category:forums"

    try:
        results = service.users().messages().list(
            userId='me', q=query, maxResults=max_results
        ).execute()
    except Exception as e:
        print(f"❌ Gmail API 查询失败: {e}")
        return []

    messages = results.get('messages', [])
    if not messages:
        print("📭 过去 24 小时无新邮件")
        return []

    print(f"📬 发现 {len(messages)} 封候选邮件，正在智能过滤...")

    newsletters = []
    for msg_meta in messages:
        try:
            msg = service.users().messages().get(
                userId='me', id=msg_meta['id'], format='full'
            ).execute()

            headers = {h['name']: h['value'] for h in msg['payload'].get('headers', [])}
            snippet = msg.get('snippet', '')

            if not is_newsletter(headers, snippet):
                continue

            # 提取正文
            body_text = extract_body(msg['payload'])
            if not body_text or len(body_text.strip()) < 100:
                body_text = snippet

            newsletters.append({
                'from': headers.get('From', 'Unknown'),
                'subject': headers.get('Subject', '(无标题)'),
                'date': headers.get('Date', ''),
                'body': body_text[:3000],  # 截断防 token 爆炸
                'snippet': snippet,
            })
        except Exception as e:
            continue

    print(f"✉️  筛选出 {len(newsletters)} 封高质量 Newsletter")
    return newsletters


def extract_body(payload):
    """递归提取邮件纯文本正文"""
    if payload.get('mimeType') == 'text/plain' and payload.get('body', {}).get('data'):
        return base64.urlsafe_b64decode(payload['body']['data']).decode('utf-8', errors='ignore')

    if payload.get('mimeType') == 'text/html' and payload.get('body', {}).get('data'):
        html = base64.urlsafe_b64decode(payload['body']['data']).decode('utf-8', errors='ignore')
        # 粗暴去 HTML 标签
        return re.sub(r'<[^>]+>', ' ', html)

    # 遍历 multipart
    for part in payload.get('parts', []):
        result = extract_body(part)
        if result:
            return result
    return ''


def generate_digest_with_gemini(newsletters):
    """使用 Gemini API 生成高浓度提炼报告"""
    if not GEMINI_API_KEY:
        print("⚠️  未找到 GEMINI_API_KEY，尝试 Mistral 备用通道...")
        return generate_digest_with_mistral(newsletters)

    today = datetime.datetime.now().strftime('%Y-%m-%d')
    emails_text = ""
    for idx, nl in enumerate(newsletters, 1):
        emails_text += f"""
--- 邮件 #{idx} ---
发件人: {nl['from']}
标题: {nl['subject']}
内容摘要: {nl['body'][:1500]}

"""

    prompt = f"""你是一位品味极高、极度挑剔的"私人首席主编"（Chief Personal Editor）。你为一位身兼创客工程师与新晋母亲双重身份的读者服务。

今天是 {today}，你刚刚收到了她邮箱中过去 24 小时积压的 {len(newsletters)} 封 Newsletter 和资讯订阅邮件：

{emails_text}

【你的核心任务 — 收件箱降噪提炼】
1. 从这堆繁杂的邮件中，像一位经验丰富的报刊主编一样，严格筛选出 3-5 条真正有价值、最硬核、或最好玩的洞察 / 资讯。
2. 无情地过滤掉所有重复信息、广告废话、客套寒暄和低营养内容。
3. 每条洞察用 2-3 句话极简阐述核心价值，并注明来源邮件。

【输出格式】请直接输出纯 Markdown，带 YAML Frontmatter：
---
title: "📥 私人简报 | {{一句概括今日最重要发现的标题}}"
date: "{today}"
type: "private-briefing"
tags: [private-briefing, inbox-digest, automated]
publish: true
private: true
---

> 🎯 一句金句式的今日主编寄语

## 📌 今日核心洞察

### 1. {{洞察标题}}
{{2-3句极简阐述}} —— 来源：{{发件人/Newsletter 名称}}

### 2. {{洞察标题}}
...

### 3. {{洞察标题}}
...

## 📊 主编快评
{{一段 50 字以内的犀利总评，用"懒散但透彻"的语气}}

---
*本报告由 AI 私人主编自动生成，仅供内部阅读。*

注意：直接输出 Markdown，不要有任何外部解释。"""

    # 强制代理
    proxy_handler = urllib.request.ProxyHandler({
        'http': 'http://127.0.0.1:7897',
        'https': 'http://127.0.0.1:7897'
    })
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.7, "maxOutputTokens": 4096}
    }

    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'),
                                     headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req, timeout=120) as res:
            data = json.loads(res.read().decode('utf-8'))
            text = data['candidates'][0]['content']['parts'][0]['text']
            # 清理 markdown 代码块包裹
            if text.startswith("```markdown"):
                text = text[len("```markdown"):].strip()
            if text.startswith("```"):
                text = text[3:].strip()
            if text.endswith("```"):
                text = text[:-3].strip()
            return text
    except Exception as e:
        print(f"❌ Gemini API 调用失败: {e}")
        return generate_digest_with_mistral(newsletters)


def generate_digest_with_mistral(newsletters):
    """Mistral 备用通道"""
    if not MISTRAL_API_KEY:
        print("❌ 主力和备用 LLM 均无可用 key，跳过今日提炼。")
        return None

    today = datetime.datetime.now().strftime('%Y-%m-%d')
    emails_text = ""
    for idx, nl in enumerate(newsletters, 1):
        emails_text += f"#{idx} [{nl['subject']}] from {nl['from']}: {nl['body'][:800]}\n\n"

    prompt = f"""你是品味极高的私人主编。从以下 {len(newsletters)} 封邮件中提炼 3-5 条最有价值的洞察。
输出纯 Markdown + YAML frontmatter (type: "private-briefing", tags: [private-briefing, inbox-digest, automated], private: true)。
今日日期: {today}

邮件内容:
{emails_text}

直接输出 Markdown，不要额外解释。"""

    proxy_handler = urllib.request.ProxyHandler({
        'http': 'http://127.0.0.1:7897',
        'https': 'http://127.0.0.1:7897'
    })
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)

    url = "https://api.mistral.ai/v1/chat/completions"
    payload = {
        "model": "mistral-large-latest",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {MISTRAL_API_KEY}'
        })
        with urllib.request.urlopen(req, timeout=120) as res:
            data = json.loads(res.read().decode('utf-8'))
            text = data['choices'][0]['message']['content']
            if text.startswith("```markdown"):
                text = text[len("```markdown"):].strip()
            if text.endswith("```"):
                text = text[:-3].strip()
            return text
    except Exception as e:
        print(f"❌ Mistral API 备用通道也失败: {e}")
        return None


def main():
    print("📥 启动『私人主编·收件箱降噪引擎』...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 幂等性检查：每日最多一份简报
    today_str = datetime.datetime.now().strftime('%Y-%m-%d')
    for f in os.listdir(OUTPUT_DIR):
        if f.startswith(today_str) and 'Inbox-Digest' in f and f.endswith('.md'):
            print(f"✅ 今日私人简报已存在 ({f})，跳过重复生成。")
            return

    # 初始化 Gmail 服务
    service = get_gmail_service()
    if not service:
        print("⚠️  Gmail API 未就绪，跳过今日邮箱提炼。")
        print("   → 请运行: python3 scripts/setup_gmail_auth.py 完成首次授权")
        return

    # 拉取 Newsletter
    newsletters = fetch_recent_emails(service, hours=24)
    if not newsletters:
        print("📭 今日无高价值 Newsletter，主编休息。")
        return

    # LLM 提炼
    print(f"🧠 正在调动 LLM 主编提炼 {len(newsletters)} 封邮件中的精华...")
    digest_content = generate_digest_with_gemini(newsletters)

    if digest_content:
        # 提取标题用于文件名
        title_match = re.search(r'title:\s*["\']([^"\']+)["\']', digest_content)
        if not title_match:
            title_match = re.search(r'title:\s*(.+)', digest_content)
        display_title = title_match.group(1).strip() if title_match else "Inbox Digest"
        safe_title = re.sub(r'[\\/*?:"<>|#\n]', "", display_title).strip()[:50]

        filename = f"{today_str}-Inbox-Digest.md"
        filepath = os.path.join(OUTPUT_DIR, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(digest_content)

        print(f"📥 私人简报已生成: {filepath}")
        print(f"   标题: {display_title}")
        print(f"   隐私级别: private-briefing (不会出现在公共网站)")
    else:
        print("⚠️  LLM 主编未能返回有效内容，今日简报生成失败。")


if __name__ == "__main__":
    main()
