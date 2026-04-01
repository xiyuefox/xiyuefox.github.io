#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gmail API 一键授权引导脚本 (One-Time Setup)
运行此脚本完成 OAuth2 授权，生成 token.json 供 auto_gmail_digest.py 使用。

前置步骤：
1. 前往 https://console.cloud.google.com/ 创建项目
2. 启用 Gmail API
3. 创建 OAuth 2.0 客户端 ID (桌面应用)
4. 下载 credentials.json 到项目根目录
"""
import os
import sys

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDS_PATH = os.path.join(PROJECT_DIR, "credentials.json")
TOKEN_PATH = os.path.join(PROJECT_DIR, "token.json")

def main():
    # 检查依赖
    try:
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
    except ImportError:
        print("⚠️  缺少 Google API 依赖，正在安装...")
        os.system(f"{sys.executable} -m pip install --user google-api-python-client google-auth-httplib2 google-auth-oauthlib")
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow

    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

    if not os.path.exists(CREDS_PATH):
        print(f"""
╔══════════════════════════════════════════════════════════╗
║  🔐 Gmail API 授权向导                                  ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  未找到 credentials.json!                                ║
║                                                          ║
║  请按以下步骤操作：                                      ║
║  1. 前往 https://console.cloud.google.com/               ║
║  2. 创建项目 → 启用 Gmail API                            ║
║  3. 凭据 → 创建 OAuth 2.0 客户端 ID (桌面应用)          ║
║  4. 下载 JSON 文件，重命名为 credentials.json             ║
║  5. 放置到: {PROJECT_DIR}/                               ║
║  6. 重新运行此脚本                                       ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
""")
        sys.exit(1)

    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("🔄 Token 已过期，正在自动刷新...")
            creds.refresh(Request())
        else:
            print("🌐 首次授权，将打开浏览器进行 OAuth2 认证...")
            flow = InstalledAppFlow.from_client_secrets_file(CREDS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(TOKEN_PATH, 'w') as token:
            token.write(creds.to_json())
        print(f"✅ Token 已保存至 {TOKEN_PATH}")
    else:
        print("✅ Token 有效，Gmail API 授权已就绪！")

    # 验证连接
    from googleapiclient.discovery import build
    service = build('gmail', 'v1', credentials=creds)
    profile = service.users().getProfile(userId='me').execute()
    print(f"📧 已连接邮箱: {profile.get('emailAddress')}")
    print(f"📊 总邮件数: {profile.get('messagesTotal')}")
    print("\n🎉 Gmail API 授权完成！auto_gmail_digest.py 现在可以正常工作了。")

if __name__ == "__main__":
    main()
