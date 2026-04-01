---
description: How to automatically sync and deploy Obsidian articles to the mengxi.space blog
---

# Obsidian 博客自动化同步部署指南

这个工作流用于将在本地 Obsidian Vault 中撰写的笔记和文章，自动化地同步到 `mengxi.space` 博客项目，并直接部署到 Cloudflare Pages 上。

## 适用场景
当你（USER）写完了新的 Obsidian 笔记，或者修改了旧的笔记，想把这些内容更新到线上博客时，你可以呼叫我（AI）执行这个工作流，或者你自己直接运行脚本。

## 自动化方案设计
这个方案由三层架构协同实现：

1. **中心调度**: `sync.sh` v2.0 (Watchdog-Powered)
2. **自愈守护**: `scripts/auto_watchdog.py` — 异常拦截 + LLM 诊断 + 沙盒验证
3. **核心同步**: `scripts/sync_obsidian.py` — 数据清洗和 HTML 注入

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

### 🛡️ 自愈守护机制 (v2.0 新增)
`auto_watchdog.py` 为每个脚本提供：
- **异常拦截**: 全局 try-except + 日志异常模式匹配
- **LLM 自动诊断**: 收集错误堆栈 → 注入架构规则 → 调用 Gemini/Mistral/Perplexity 生成修复补丁
- **沙盒验证**: 补丁代码先在隔离环境试运行，通过后自动 Git Commit
- **故障隔离**: 单个脚本失败不中断整条流水线

## 运行方式

// turbo-all
1. 运行完整部署流水线（自愈模式）
```bash
cd /Users/hulimofaqiu/mengxi-first-ai-project
./sync.sh
```

2. 仅执行健康扫描（不部署）
```bash
cd /Users/hulimofaqiu/mengxi-first-ai-project
python3 scripts/auto_watchdog.py --scan
```

3. 调试单个脚本
```bash
cd /Users/hulimofaqiu/mengxi-first-ai-project
python3 scripts/auto_watchdog.py --script scripts/fetch_hn_feed.py
```

## 日志与事件归档
- **运行日志**: `logs/watchdog/watchdog.log`
- **事件历史**: `logs/watchdog/incident_history.jsonl`
- **AI 补丁归档**: `logs/watchdog/patches/`
- **独立事件报告**: `logs/watchdog/incidents/`

## 维护者须知
- 如果你想调整「什么样的文章才算合格能被同步」，请修改 `scripts/sync_obsidian.py` 文件中的 `is_valid_article` 函数。
- 所有的中文文件名会在同步时被解析成不含特殊字符的纯小写拼音（通过 `pypinyin` 组件）。这种短拼音 URL 是 SEO 友好并且不容易发生乱码 404 错误的。
- 不论在 Obsidian 中重构多少次，只要你的文件名发生变动，拼音 Slug 也将随之生成全新的链接。
- 我们会在首页保留原有的手动录入的卡片。只要确保将生成内容严格写进定好的注释标记即可，也就是保证 `index.html` 的结构不被误删。
- 自愈守护的安全红线硬编码禁止补丁删除文件、修改 `.env`、绕过隐私过滤，详见 `auto_watchdog.py` 中的 `FORBIDDEN_PATTERNS`。
