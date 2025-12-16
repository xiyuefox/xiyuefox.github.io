# 适配Obsidian的AI时间轴整合流程（你高频使用的工具）
Obsidian将所有笔记存在**本地文件夹（Vault目录）**，因此可以直接监控该目录，无需复杂的API调用，更适合高频使用场景。

## 核心流程（仅需3步）
### ① 监控触发：自动监听Obsidian Vault目录
AI Agent将**实时监控你的Obsidian仓库文件夹**（如：`~/MyObsidianVault/`），当：
- 新建/修改笔记文件（.md）
- 新增附件（截图、图片、音频等）
时，立即自动启动处理流程。

### ② 数据整理：智能解析Obsidian笔记
AI Agent会提取并结构化Obsidian笔记的关键信息：
#### 若你用**YAML Frontmatter**标注笔记（推荐）：
```yaml
---
date: 2025-12-05
time: 14:30
type: 学习笔记
tags: ["AI Agent", "架构"]
---
# AI Agent 架构设计
核心模块：输入层→处理层→输出层...
```
Agent会**自动读取Frontmatter的元数据**，直接生成结构化JSON。

#### 若你不用Frontmatter：
Agent会通过**AI语义分析**识别笔记类型、提取关键词、推测时间（通过文件修改时间）。

### ③ 界面更新：生成时间轴+可视化
处理完成后，Agent会将JSON数据存入前端目录，**打开时间轴HTML即可查看最新内容**。

---

## 可选：保留Notion偶尔使用的支持
若需同步Notion内容，仅需新增「Notion API拉取」步骤（作为补充数据源），不影响Obsidian的核心流程。

## 本地部署（Obsidian用户最优解）
将前端HTML和JSON文件存在**Obsidian Vault的附件目录**或**专门的时间轴文件夹**，即可在Obsidian中通过「Open in Browser」插件直接打开时间轴，无需切换工具！
