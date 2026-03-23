---
description: How to automatically sync and deploy Obsidian articles to the mengxi.space blog
---

# Obsidian 博客自动化同步部署指南

这个工作流用于将在本地 Obsidian Vault 中撰写的笔记和文章，自动化地同步到 `mengxi.space` 博客项目，并直接部署到 Cloudflare Pages 上。

## 适用场景
当你（USER）写完了新的 Obsidian 笔记，或者修改了旧的笔记，想把这些内容更新到线上博客时，你可以呼叫我（AI）执行这个工作流，或者你自己直接运行脚本。

## 自动化方案设计
这个方案是由一个中心调度 Bash 脚本 (`sync.sh`) 配合一个执行具体清洗和转化逻辑的 Python 脚本 (`scripts/sync_obsidian.py`) 共同实现的。

- **源路径**: `/Users/hulimofaqiu/Documents/obisidian笔记文件/`
- **目标路径**: 
  - 文章：`/Users/hulimofaqiu/mengxi-first-ai-project/posts/md/` (并复制至 `public/posts/md/`)
  - 首图和插图：`/Users/hulimofaqiu/mengxi-first-ai-project/public/images/obsidian/`
  - 缩略卡片：将 HTML 动态注入到首页 `index.html` 的 `<!-- ARTICLES_LIST_START -->` 和 `<!-- ARTICLES_LIST_END -->` 之间。

### 智能过滤机制
Python 脚本会自动过滤掉零碎的、不成熟的草稿，提取高质量长文。过滤规则如下：
1. **系统排除**: `00`, `01`, `Untitled`, `未命名`, `Drawing`, `!Pasted`, `Excalidraw` 命名的文件自动被排除。
2. **私密屏蔽**: 如果笔记内容中包含 `#draft` 或 `#private` 标签，则绝对不会被发布。
3. **内容长度**: 只有笔记正文字符数超过 **1200字** 的文章会被视为「成熟文章」进行收录同步。
4. **强制开绿灯**: 即使文章不到 1200 字，只要在文章的任何地方加上了 `#publish` 标签，仍会强制同步。

## 运行方式 (The `sync.sh` script)

要执行全自动同步部署，只需要在项目根目录下执行 `sync.sh` 脚本。这通常只需要几秒钟的时间，然后它会调用 wrangler CLI 将构建好的网页推送上线。

// turbo-all
1. 运行部署脚本
```bash
cd /Users/hulimofaqiu/mengxi-first-ai-project
./sync.sh
```

## 维护者须知
- 如果你想调整「什么样的文章才算合格能被同步」，请修改 `scripts/sync_obsidian.py` 文件中的 `is_valid_article` 函数。
- 所有的中文文件名会在同步时被解析成不含特殊字符的纯小写拼音（通过 `pypinyin` 组件）。这种短拼音 URL 是 SEO 友好并且不容易发生乱码 404 错误的。
- 不论在 Obsidian 中重构多少次，只要你的文件名发生变动，拼音 Slug 也将随之生成全新的链接。
- 我们会在首页保留原有的手动录入的卡片。只要确保将生成内容严格写进定好的注释标记即可，也就是保证 `index.html` 的结构不被误删。
