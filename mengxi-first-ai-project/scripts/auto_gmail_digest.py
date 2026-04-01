#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📥 私人主编·收件箱降噪引擎 v2.0 (Zero-Touch Edition)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
使用 Gmail IMAP + App Password 方案，彻底绕开 OAuth2 浏览器授权卡点。
无需任何手动操作：只要 .env 中配置了 GMAIL_ADDRESS 和 GMAIL_APP_PASSWORD 即可。

如何获取 App Password (一次性):
  1. 前往 https://myaccount.google.com/apppasswords
  2. 创建一个 App Password (选择"邮件"和"Mac")
  3. 将16位密码添加到 .env: GMAIL_APP_PASSWORD=xxxx xxxx xxxx xxxx

Pipeline Position: sync.sh Phase 1.5
Privacy: private-briefing 标签 → sync_obsidian.py 硬性跳过 → 不部署到 Cloudflare
"""
import os
import sys
import re
import json
import imaplib
import email
from email.header import decode_header
import datetime
import urllib.request

# ── 路径与环境 ────────────────────────────────────────────
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OBSIDIAN_VAULT = "/Users/hulimofaqiu/Documents/obisidian笔记文件/"
OUTPUT_DIR = os.path.join(OBSIDIAN_VAULT, "daily_brief")

# 加载 .env
ENV_PATH = os.path.join(PROJECT_DIR, ".env")
if os.path.exists(ENV_PATH):
    with open(ENV_PATH) as f:
        for line in f:
            if '=' in line and not line.startswith('#'):
                k, v = line.strip().split('=', 1)
                os.environ[k.strip()] = v.strip().strip('"')

GMAIL_ADDRESS = os.environ.get("GMAIL_ADDRESS", "")
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD", "")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY", "")

# ── Newsletter 智能过滤 ────────────────────────────────────
NEWSLETTER_KEYWORDS = [
    "newsletter", "digest", "weekly", "daily", "update",
    "noreply", "no-reply", "info@", "hello@",
    "substack", "mailchimp", "convertkit", "revue",
    "medium", "producthunt", "hackernewsletter",
    "tldrnewsletter", "morningbrew", "theinformation",
    "platformer", "stratechery", "lenny", "rundown",
    "techcrunch", "oreilly", "smashingmagazine",
    "arxiv", "deeplearning", "huggingface",
    "developer", "github", "vercel",
]

EXCLUDE_KEYWORDS = [
    "receipt", "invoice", "order", "shipping", "tracking",
    "password reset", "verification code", "security alert",
    "your payment", "transaction",
]


def decode_mime_header(header_value):
    """安全解码 MIME header"""
    if not header_value:
        return ""
    decoded_parts = decode_header(header_value)
    result = ""
    for part, charset in decoded_parts:
        if isinstance(part, bytes):
            charset = charset or 'utf-8'
            try:
                result += part.decode(charset, errors='ignore')
            except (UnicodeDecodeError, LookupError):
                result += part.decode('utf-8', errors='ignore')
        else:
            result += part
    return result


def extract_text_body(msg):
    """递归提取邮件纯文本正文"""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == 'text/plain':
                charset = part.get_content_charset() or 'utf-8'
                try:
                    return part.get_payload(decode=True).decode(charset, errors='ignore')
                except (UnicodeDecodeError, LookupError):
                    return part.get_payload(decode=True).decode('utf-8', errors='ignore')
            elif content_type == 'text/html':
                charset = part.get_content_charset() or 'utf-8'
                try:
                    html = part.get_payload(decode=True).decode(charset, errors='ignore')
                except (UnicodeDecodeError, LookupError):
                    html = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                # 粗暴去 HTML 标签
                return re.sub(r'<[^>]+>', ' ', html)
    else:
        charset = msg.get_content_charset() or 'utf-8'
        try:
            payload = msg.get_payload(decode=True)
            if payload:
                text = payload.decode(charset, errors='ignore')
                if msg.get_content_type() == 'text/html':
                    text = re.sub(r'<[^>]+>', ' ', text)
                return text
        except Exception:
            pass
    return ""


def is_newsletter(sender, subject, body_snippet):
    """智能判断是否为 Newsletter"""
    combined = f"{sender} {subject} {body_snippet}".lower()
    # 排除交易类
    for kw in EXCLUDE_KEYWORDS:
        if kw in combined:
            return False
    # 匹配白名单
    for kw in NEWSLETTER_KEYWORDS:
        if kw in combined:
            return True
    return False


def fetch_newsletters_via_imap(hours=24, max_count=30):
    """通过 IMAP 拉取过去 N 小时的 Newsletter 邮件"""
    if not GMAIL_ADDRESS or not GMAIL_APP_PASSWORD:
        print("⚠️  未配置 GMAIL_ADDRESS 或 GMAIL_APP_PASSWORD")
        print("   → 请在 .env 中添加:")
        print("     GMAIL_ADDRESS=your.email@gmail.com")
        print("     GMAIL_APP_PASSWORD=xxxx xxxx xxxx xxxx")
        print("   → App Password 获取: https://myaccount.google.com/apppasswords")
        return []

    since_date = (datetime.datetime.now() - datetime.timedelta(hours=hours)).strftime('%d-%b-%Y')

    try:
        print(f"📧 连接 Gmail IMAP (imap.gmail.com:993)...")
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        print(f"✅ 登录成功: {GMAIL_ADDRESS}")
    except imaplib.IMAP4.error as e:
        print(f"❌ IMAP 登录失败: {e}")
        print("   → 请确认 App Password 是否正确")
        print("   → 请确认已在 Gmail 设置中启用 IMAP")
        return []

    newsletters = []

    # 扫描多个文件夹：收件箱 + Updates + Promotions
    folders = ['INBOX', '[Gmail]/Updates', '[Gmail]/Promotions', 'CATEGORY_PROMOTIONS', 'CATEGORY_UPDATES']

    for folder in folders:
        try:
            status, _ = mail.select(folder, readonly=True)
            if status != 'OK':
                continue

            _, msg_ids = mail.search(None, f'(SINCE "{since_date}")')
            ids = msg_ids[0].split()

            if not ids:
                continue

            # 只取最近 max_count 封
            ids = ids[-max_count:]
            print(f"   📂 {folder}: 发现 {len(ids)} 封候选邮件")

            for msg_id in ids:
                try:
                    _, msg_data = mail.fetch(msg_id, '(RFC822)')
                    raw_email = msg_data[0][1]
                    msg = email.message_from_bytes(raw_email)

                    sender = decode_mime_header(msg.get('From', ''))
                    subject = decode_mime_header(msg.get('Subject', ''))
                    body = extract_text_body(msg)

                    if not is_newsletter(sender, subject, body[:500]):
                        continue

                    newsletters.append({
                        'from': sender,
                        'subject': subject,
                        'body': body[:3000],  # 截断防 token 爆炸
                        'date': msg.get('Date', ''),
                    })
                except Exception:
                    continue
        except Exception:
            continue

    mail.logout()

    # 去重（按 subject）
    seen_subjects = set()
    unique = []
    for nl in newsletters:
        key = nl['subject'].strip().lower()[:80]
        if key not in seen_subjects:
            seen_subjects.add(key)
            unique.append(nl)

    print(f"✉️  筛选并去重后: {len(unique)} 封高质量 Newsletter")
    return unique


def generate_digest_with_gemini(newsletters):
    """Gemini 主力提炼"""
    if not GEMINI_API_KEY:
        return generate_digest_with_mistral(newsletters)

    today = datetime.datetime.now().strftime('%Y-%m-%d')
    emails_text = ""
    for idx, nl in enumerate(newsletters[:15], 1):  # 最多15封防超 token
        emails_text += f"\n--- 邮件 #{idx} ---\n发件人: {nl['from']}\n标题: {nl['subject']}\n内容: {nl['body'][:1200]}\n"

    prompt = f"""你是一位品味极高、极度挑剔的"私人首席主编"（Chief Personal Editor）。你为一位身兼创客工程师与新晋母亲双重身份的读者服务。

今天是 {today}，你收到了她邮箱中过去 24 小时的 {len(newsletters)} 封 Newsletter 和订阅邮件：

{emails_text}

【核心任务 — 收件箱降噪】
1. 严格筛选 3-5 条真正最有价值、最硬核、或最好玩的洞察/资讯。
2. 无情过滤广告废话、客套、低营养内容。
3. 每条洞察 2-3 句极简阐述，注明来源。

【输出格式】直接输出纯 Markdown + YAML Frontmatter：
---
title: "📥 私人简报 | {{概括今日最重要发现}}"
date: "{today}"
type: "private-briefing"
tags: [private-briefing, inbox-digest, automated]
publish: true
private: true
---

> 🎯 一句金句式主编寄语

## 📌 今日核心洞察

### 1. {{洞察标题}}
{{2-3句}} —— 来源：{{Newsletter名}}

### 2. {{洞察标题}}
...

## 📊 主编快评
{{50字犀利总评}}

---
*AI 私人主编自动生成，仅供内部阅读。*

直接输出 Markdown，不要额外解释。"""

    proxy_handler = urllib.request.ProxyHandler({
        'http': 'http://127.0.0.1:7897', 'https': 'http://127.0.0.1:7897'
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
            if text.startswith("```markdown"): text = text[len("```markdown"):].strip()
            if text.startswith("```"): text = text[3:].strip()
            if text.endswith("```"): text = text[:-3].strip()
            return text
    except Exception as e:
        print(f"❌ Gemini 失败: {e}，切换 Mistral...")
        return generate_digest_with_mistral(newsletters)


def generate_digest_with_mistral(newsletters):
    """Mistral 备用"""
    if not MISTRAL_API_KEY:
        print("❌ 所有 LLM API 均不可用")
        return None

    today = datetime.datetime.now().strftime('%Y-%m-%d')
    emails_text = "\n".join([f"#{i+1} [{nl['subject']}] from {nl['from']}: {nl['body'][:600]}"
                             for i, nl in enumerate(newsletters[:10])])

    prompt = f"""私人主编任务：从以下{len(newsletters)}封邮件提炼3-5条最有价值洞察。
输出 Markdown + YAML (type:"private-briefing", tags:[private-briefing], private:true)。日期:{today}

{emails_text}

直接输出Markdown。"""

    proxy_handler = urllib.request.ProxyHandler({
        'http': 'http://127.0.0.1:7897', 'https': 'http://127.0.0.1:7897'
    })
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)

    try:
        req = urllib.request.Request("https://api.mistral.ai/v1/chat/completions",
            data=json.dumps({
                "model": "mistral-large-latest",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7
            }).encode('utf-8'),
            headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {MISTRAL_API_KEY}'})
        with urllib.request.urlopen(req, timeout=120) as res:
            data = json.loads(res.read().decode('utf-8'))
            text = data['choices'][0]['message']['content']
            if text.startswith("```markdown"): text = text[len("```markdown"):].strip()
            if text.endswith("```"): text = text[:-3].strip()
            return text
    except Exception as e:
        print(f"❌ Mistral 也失败: {e}")
        return None


def main():
    print("📥 启动『私人主编·收件箱降噪引擎 v2.0 (Zero-Touch)』...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 幂等性：每日最多一份
    today_str = datetime.datetime.now().strftime('%Y-%m-%d')
    for f in os.listdir(OUTPUT_DIR):
        if f.startswith(today_str) and 'Inbox-Digest' in f and f.endswith('.md'):
            print(f"✅ 今日私人简报已存在 ({f})，跳过。")
            return

    # IMAP 拉取
    newsletters = fetch_newsletters_via_imap(hours=24)
    if not newsletters:
        print("📭 今日无高价值 Newsletter，主编休息。")
        return

    # LLM 提炼
    print(f"🧠 调动 LLM 主编提炼 {len(newsletters)} 封邮件精华...")
    digest = generate_digest_with_gemini(newsletters)

    if digest:
        filename = f"{today_str}-Inbox-Digest.md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(digest)
        print(f"📥 私人简报已生成: {filepath}")
        print(f"   🔒 隐私级别: private-briefing (绝不公开)")
    else:
        print("⚠️  LLM 未返回有效内容。")


if __name__ == "__main__":
    main()
