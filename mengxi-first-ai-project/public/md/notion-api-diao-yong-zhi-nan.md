---
title: "Notion API 调用指南"
date: 2026-03-09
tags: [api, notion, guide]
category: "obsidian"
badge: "api"
---

## Notion API 调用指南

### 1. 创建集成并获取 Token

1. 前往 [notion.so/profile/integrations](https://www.notion.so/profile/integrations)
2. 点击 **"新建集成"**，填写名称，选择关联的工作区
3. 创建后复制 **Internal Integration Token**（以 `ntn_` 开头）

### 2. 授权页面访问

在 Notion 中打开目标页面/数据库 → 点击右上角 `···` → **连接** → 选择你创建的集成。

> ⚠️ 不授权页面的话，API 会返回空结果。

### 3. 基本调用方式

所有请求需携带以下 Header：

```http
Authorization: Bearer ntn_your_token_here
Notion-Version: 2022-06-28
Content-Type: application/json
```

### 4. 常用 API 端点

| 功能 | 方法 | 端点 |
|---|---|---|
| 搜索 | POST | `https://api.notion.com/v1/search` |
| 获取页面 | GET | `https://api.notion.com/v1/pages/{page_id}` |
| 创建页面 | POST | `https://api.notion.com/v1/pages` |
| 更新页面属性 | PATCH | `https://api.notion.com/v1/pages/{page_id}` |
| 查询数据库 | POST | `https://api.notion.com/v1/databases/{database_id}/query` |
| 获取块内容 | GET | `https://api.notion.com/v1/blocks/{block_id}/children` |
| 追加块内容 | PATCH | `https://api.notion.com/v1/blocks/{block_id}/children` |

### 5. 示例

#### cURL — 搜索工作区

```bash
curl -X POST 'https://api.notion.com/v1/search' \
  -H 'Authorization: Bearer ntn_****' \
  -H 'Notion-Version: 2022-06-28' \
  -H 'Content-Type: application/json' \
  -d '{"query": "项目计划"}'
```

#### Python — 查询数据库

```python
import requests

NOTION_TOKEN = "ntn_****"
DATABASE_ID = "your_database_id"

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}

# 查询数据库
resp = requests.post(
    f"https://api.notion.com/v1/databases/{DATABASE_ID}/query",
    headers=headers,
    json={
        "filter": {
            "property": "Status",
            "select": {"equals": "进行中"}
        }
    }
)
data = resp.json()
for item in data["results"]:
    print(item["properties"])
```

#### Python — 创建页面

```python
resp = requests.post(
    "https://api.notion.com/v1/pages",
    headers=headers,
    json={
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Name": {
                "title": [{"text": {"content": "新任务"}}]
            },
            "Status": {
                "select": {"name": "待办"}
            }
        },
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"text": {"content": "这是页面正文内容"}}]
                }
            }
        ]
    }
)
```

### 6. 官方 SDK

也可以使用官方 JavaScript SDK 简化调用：

```bash
npm install @notionhq/client
```

```javascript
const { Client } = require("@notionhq/client");

const notion = new Client({ auth: "ntn_****" });

// 搜索
const results = await notion.search({ query: "会议记录" });

// 查询数据库
const db = await notion.databases.query({
  database_id: "your_database_id",
});
```

### 关键注意事项

* **page_id / database_id** 可从 Notion 页面 URL 中提取（32 位字符串）
* API 有 **速率限制**，平均 3 请求/秒
* 块内容（正文）需通过 `/blocks/{id}/children` 单独获取，`/pages/{id}` 只返回属性
* 官方文档：[developers.notion.com](https://developers.notion.com)

