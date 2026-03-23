# ✍️ Obsidian 内容发布模版 (Mengxi Blog)

这个模版旨在最大化利用自动化脚本的"智能筛选"和"格式美化"功能。

## 📝 模版建议 (复制到 Obsidian)

```markdown
---
title: "这里写文章标题"
date: 2026-02-05
tags: ["tech", "life", "design"]
categories: ["notes"]
status: published  # published / draft / private
private: false     # true 则绝对不发布，无论其他设置
---

# 🌟 文章大标题

> 这里可以写一段简短的导语，或者引用。

### 1. 核心观点
在这里开始你的写作。

### 2. 设计美学 (配合 Retro 模式)
- **重点内容**：使用加粗。
- *感性描述*：使用斜体。

---
*Mengxi Archive - 记录思维的碰撞*
```

---

## 🔒 私密控制（三种方式任选）

> **重要**：以下三种方式都能阻止文章发布到 mengxi.space，满足其一即生效。

### 方式 1：Frontmatter `private: true`（推荐）
```markdown
---
title: "我的私人日记"
private: true
---
这篇不会出现在网站上。
```

### 方式 2：`status: private`
```markdown
---
title: "草稿中的想法"
status: private
---
同样不会发布。
```

### 方式 3：放入私密文件夹
将笔记文件放在以下任意文件夹名称下，整个文件夹内容都不会发布：

| 文件夹名 | 说明 |
|---------|------|
| `private` / `Private` | 英文私密文件夹 |
| `私密` | 中文私密文件夹 |
| `个人` | 个人内容 |
| `日记` / `diary` | 日记类内容 |
| `personal` | 个人事务 |

示例结构：
```
📁 obisidian笔记文件/
├── 📁 private/          ← 整个文件夹不发布
│   ├── 孕期日记.md
│   └── 私人感悟.md
├── 📁 Notes/            ← 正常发布
│   └── 学习笔记.md
└── 📁 Ideas/            ← 正常发布
    └── 设计灵感.md
```

---

## 🚀 发布状态速查表

| Frontmatter 设置 | 是否发布 |
|----------------|---------|
| 无特殊设置 | ✅ 发布 |
| `status: published` | ✅ 发布 |
| `draft: true` | ❌ 不发布 |
| `status: draft` | ❌ 不发布 |
| `private: true` | 🔒 不发布（私密）|
| `status: private` | 🔒 不发布（私密）|
| 位于私密文件夹 | 🔒 不发布（私密）|
| 文件名含"Untitled"/未命名 | ❌ 不发布 |

---



---

## 🏷️ 内容分类与专属渲染 (Type Routing)

为了降低主页混乱度，我们支持通过 YAML 的 `type` 字段对内容进行自动路由分发。

```markdown
---
title: "我的内容标题"
type: showcase  # 选填: article / showcase / podcast
---
```

### 🗂️ 分部机制
| 类型 (`type`) | 首页去向 | 专属单页渲染效果 (`post.html`) |
| :--- | :--- | :--- |
| `article` | 📝 创客日志 (Articles) | 标准经典排版 |
| `showcase` | ✨ 项目展示 (Showcases) | 标准经典排版 |
| `podcast` | 🎙️ 播客与对谈 (Podcasts) | **🔥 专属 Hero 播放器 + AI 摘要面板** |

---

## 🎙️ 播客专属免摩擦渲染 (`type: podcast`)

当 `type` 设定为 `podcast` 时，系统将触发智能提取流：
1. **自动音频 Hero 卡片**：自动抓取正文中**第一个** `.mp3`、`.m4a` 等音频链接，提炼到文章最顶部形成一个带有 Terminal Hard Shadow 的漂浮播放器。
2. **AI Takeaway 面板**：自动扫描正文中的 **Obsidian Callout**，只要其标题包含 `AI、总结、亮点、Takeaway`，就会自动克隆悬置于播放器下方，开启点阵背景发光样。

> **小贴士**：您正常书写 Markdown，系统将免配置、零摩擦抓取，正文中的冗余锚点会自动对齐并隐藏。


## 📋 其他书写建议

1. **字数要求**：脚本筛选 100+ 字的内容，短文会被自动过滤。
2. **标题规范**：脚本自动移除文件名中的数字前缀（如 `01. `）。
3. **分类映射**：
   - `Notes` 文件夹 → 网站 `notes` 分类
   - `Ideas` 文件夹 → 网站 `ideas` 分类
   - `Sparks` 文件夹 → 网站 `sparks` 分类
4. **快捷键**：
   - **'T'** 循环切换主题
   - **'R'** 进入 Vibrant Retro 模式
