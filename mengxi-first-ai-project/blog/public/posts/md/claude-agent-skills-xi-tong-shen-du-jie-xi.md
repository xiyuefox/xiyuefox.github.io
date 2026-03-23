---
title: "Claude Agent Skills 系统深度解析"
date: 2026-03-02
tags: []
category: "obsidian"
badge: "obsidian"
---

Claude Agent Skills 系统深度解析

**📋 目录**

• [概述](#%E6%A6%82%E8%BF%B0)

• [核心概念](#%E6%A0%B8%E5%BF%83%E6%A6%82%E5%BF%B5)

• [Skills 构建指南](#skills-%E6%9E%84%E5%BB%BA%E6%8C%87%E5%8D%97)

• [SKILL.md 编写规范](#skillmd-%E7%BC%96%E5%86%99%E8%A7%84%E8%8C%83)

• [常见设计模式](#%E5%B8%B8%E8%A7%81%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F)

• [内部架构](#%E5%86%85%E9%83%A8%E6%9E%B6%E6%9E%84)

• [完整执行生命周期](#%E5%AE%8C%E6%95%B4%E6%89%A7%E8%A1%8C%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F)

• [参考资源](#%E5%8F%82%E8%80%83%E8%B5%84%E6%BA%90)

**概述**

Claude 的 Agent Skills 系统是一个**基于提示词的元工具架构**，通过专门的指令注入来扩展 LLM 能力。与传统的函数调用或代码执行不同，skills 通过**提示词扩展**和**上下文修改**来改变 Claude 处理后续请求的方式，而不需要编写可执行代码。

**关键特性**

• **非代码执行**：Skills 不运行 Python/JavaScript，没有 HTTP 服务器或函数调用

• **提示词模板**：专门的提示词模板，向对话上下文注入领域特定指令

• **动态上下文修改**：修改对话上下文（注入指令）和执行上下文（更改工具权限和模型）

• **声明式发现**：基于文本描述的技能发现和调用，由 Claude 的语言理解决定

**核心概念**

**Tools vs Skills 对比**

方面

传统工具 (Tools)

技能 (Skills)

**执行模型**

同步、直接执行

提示词扩展

**目的**

执行特定操作

指导复杂工作流

**返回值**

立即结果

对话上下文 + 执行上下文变更

**示例**

Read, Write, Bash

internal-comms, skill-creator

**并发性**

通常安全

非并发安全

**类型**

多种

始终为 "prompt"

**工作流程图**

  

  

用户请求 → Claude 接收

    ├─ 用户消息

    ├─ 可用工具 (Read, Write, Bash...)

    └─ Skill 元工具

        └─ 包含所有可用 skills 的描述列表

  

Claude 推理 → 匹配用户意图与 skill 描述

  

调用 Skill 工具 → 注入上下文

    ├─ 对话上下文注入（指令提示词）

    ├─ 执行上下文修改（工具权限、模型切换）

    └─ 继续对话处理任务

  

**术语说明**

• Skill **工具**（大写 S）= 管理所有 skills 的元工具，出现在 Claude 的 tools 数组中

• **skills**（小写 s）= 单个技能，如 pdf、skill-creator、internal-comms

**Skills 构建指南**

**文件结构**

每个 Skill 是一个包含指令、脚本和资源的文件夹：

  

  

my-skill/

├── SKILL.md              # 核心提示词和指令（必需）

├── LICENSE.txt           # 许可证（可选）

├── scripts/              # 可执行的 Python/Bash 脚本

├── references/           # 加载到上下文的文档

└── assets/               # 模板和二进制文件

  

**渐进式披露原则**

**关键概念**：只显示足够的信息帮助 agent 决定下一步，然后根据需要逐步透露更多细节

1. **披露 Frontmatter**：最小化（名称、描述、许可证）

2. **如果选择了 skill**：加载 SKILL.md（全面但聚焦）

3. **执行时加载**：辅助资源、引用文档、脚本

**SKILL.md 编写规范**

**文件结构**

  

  

┌─────────────────────────────────────┐

│ 1. YAML Frontmatter (元数据)        │ ← 配置

│    ---                              │

│    name: skill-name                 │

│    description: 简要概述            │

│    allowed-tools: "Bash, Read"      │

│    version: 1.0.0                   │

│    ---                              │

├─────────────────────────────────────┤

│ 2. Markdown Content (指令)          │ ← Claude 的提示词

│                                     │

│    目的说明                         │

│    详细指令                         │

│    示例和指南                       │

│    分步骤流程                       │

└─────────────────────────────────────┘

  

**Frontmatter 字段详解**

name **(必需)**

技能名称，用作 Skill Tool 中的 command

description **(必需)**

简要描述技能功能。这是 Claude 判断何时调用技能的**主要信号**。

  

  

# ✅ 好的描述

description: Guide for creating effective skills. This skill should be used when users want to create a new skill...

  

# ❌ 不够清晰

description: A skill for stuff

  

allowed-tools **(可选)**

定义技能可以使用的工具，无需用户批准。

  

  

# ✅ 具体的 git 命令

allowed-tools: "Bash(git status:*),Bash(git diff:*),Read,Grep"

  

# ✅ 文件操作

allowed-tools: "Read,Write,Edit,Glob,Grep"

  

# ❌ 不必要的权限范围

allowed-tools: "Bash,Read,Write,Edit,Glob,Grep,WebSearch,Task,Agent"

  

model **(可选)**

指定技能使用的模型。

  

  

model: "claude-opus-4-20250514"  # 使用特定模型

model: "inherit"                 # 继承会话当前模型（默认）

  

**其他可选字段**

• license: 许可证信息

• version: 版本号（如 "1.0.0"）

• disable-model-invocation: 禁止 Claude 自动调用（需手动触发）

• mode: 标记为"模式命令"，显示在技能列表顶部

**Markdown 内容结构**

  

  

---

# Frontmatter 配置

---

  

# [简要目的陈述 - 1-2 句]

  

## 概述

[这个技能做什么，何时使用，提供什么]

  

## 前置要求

[所需工具、文件或上下文]

  

## 指令

  

### 步骤 1: [第一个动作]

[命令式指令]

[必要时添加示例]

  

### 步骤 2: [下一个动作]

[命令式指令]

  

### 步骤 3: [最终动作]

[命令式指令]

  

## 输出格式

[如何构造结果]

  

## 错误处理

[失败时如何处理]

  

## 示例

[具体使用示例]

  

## 资源

[引用 scripts/, references/, assets/]

  

**最佳实践**

• 保持在 5,000 词（约 800 行）以内

• 使用命令式语言（"分析代码..."）而非第二人称（"你应该分析..."）

• 使用 {baseDir} 引用路径，永远不要硬编码绝对路径

  

  

❌ Read /home/user/project/config.json

✅ Read {baseDir}/config.json

  

**常见设计模式**

**模式 1: 脚本自动化**

**使用场景**：需要多个命令或确定性逻辑的复杂操作

  

  

运行 scripts/analyzer.py 分析目标目录：

`python {baseDir}/scripts/analyzer.py --path "$USER_PATH" --output report.json`

  

解析生成的 `report.json` 并呈现结果。

  

  

  

  

allowed-tools: "Bash(python {baseDir}/scripts/*:*), Read, Write"

  

**模式 2: 读取-处理-写入**

**使用场景**：文件转换和数据处理

  

  

## 处理工作流

1. 使用 Read 工具读取输入文件

2. 根据格式解析内容

3. 按规范转换数据

4. 使用 Write 工具写入输出

5. 报告完成并提供摘要

  

  

  

  

allowed-tools: "Read, Write"

  

**模式 3: 搜索-分析-报告**

**使用场景**：代码库分析和模式检测

  

  

## 分析流程

1. 使用 Grep 查找相关代码模式

2. 读取每个匹配的文件

3. 分析漏洞

4. 生成结构化报告

  

  

  

  

allowed-tools: "Grep, Read"

  

**模式 4: 命令链执行**

**使用场景**：具有依赖关系的多步骤操作

  

  

执行分析管道：

npm install && npm run lint && npm test

  

报告每个阶段的结果。

  

  

  

  

allowed-tools: "Bash(npm install:*), Bash(npm run:*), Read"

  

**高级模式**

**向导式多步骤工作流**

在每个阶段等待用户确认的复杂流程

**基于模板的生成**

从 assets/ 加载模板，填充占位符

**迭代优化**

先进行广泛扫描，然后逐步深入分析

**上下文聚合**

从多个来源收集信息，综合成连贯的理解

**内部架构**

**Skill 对象设计**

  

  

Pd = {

  name: "Skill",  // 工具名称常量

  inputSchema: {

    command: string  // 例如 "pdf", "skill-creator"

  },

  outputSchema: {

    success: boolean,

    commandName: string

  },

  // 🔑 关键字段：动态生成技能列表

  prompt: async () => fN2(),

  // 验证和执行

  validateInput: async (input, context) => { /* 5 种错误码 */ },

  checkPermissions: async (input, context) => { /* allow/deny/ask */ },

  call: async *(input, context) => { /* yields messages + context modifier */ }

}

  

**API 请求结构**

Skills **不在系统提示词中**，它们存在于 tools 数组中：

  

  

{

  "model": "claude-sonnet-4-5-20250929",

  "system": "You are Claude Code...",

  "messages": [

    {"role": "user", "content": "Help me create a new skill"}

  ],

  "tools": [

    {

      "name": "Skill",

      "description": "Execute a skill...\n\n<available_skills>...",

      "input_schema": {

        "properties": {

          "command": {"type": "string"}

        }

      }

    },

    {"name": "Bash"},

    {"name": "Read"}

  ]

}

  

**对话和执行上下文注入**

Skills 通过两条独立的用户消息注入上下文：

消息

isMeta

可见性

目的

长度

**元数据消息**

false

用户可见

状态/透明度

~50-200 字符

**技能提示词**

true

隐藏

指令/指导

~500-5,000 词

  

  

// 消息 1: 用户可见

{

  content: "<command-message>The \"pdf\" skill is loading</command-message>",

  // isMeta: false (默认)

}

  

// 消息 2: 发送到 API 但在 UI 中隐藏

{

  content: "You are a PDF processing specialist...",

  isMeta: true

}

  

**完整执行生命周期**

**阶段 1: 发现和加载（启动时）**

扫描多个来源的技能：

• ~/.config/claude/skills/ (用户设置)

• .claude/skills/ (项目设置)

• 插件提供的技能

• 内置技能

**阶段 2: 回合 1 - 用户请求和技能选择**

**用户**："Extract text from report.pdf"

**Claude 推理**：

  

  

- 用户想要"从 report.pdf 提取文本"

- 这是 PDF 处理任务

- 查看可用技能...

- "pdf": 从 PDF 文档提取文本 - 当用户想要从 PDF 文件提取或处理文本时

- 匹配！决定：调用 Skill 工具，command="pdf"

  

**Claude 返回**：

  

  

{

  "type": "tool_use",

  "name": "Skill",

  "input": {"command": "pdf"}

}

  

**阶段 3: Skill 工具执行**

1. **验证**：检查技能是否存在、是否启用

2. **权限检查**：检查拒绝/允许规则，或询问用户

3. **加载文件**：读取 SKILL.md 内容

4. **生成消息**：

▪ 元数据消息（可见）

▪ 技能提示词（隐藏）

▪ 权限消息

5. **返回上下文修改器**：

  

  

{

  newMessages: [...],

  contextModifier(context) {

    // 注入允许的工具

    // 覆盖模型

    return modifiedContext;

  }

}

  

**阶段 4: 发送到 API（回合 1 完成）**

  

  

{

  "messages": [

    {"role": "user", "content": "Extract text from report.pdf"},

    {"role": "assistant", "content": [{"type": "tool_use", "name": "Skill", ...}]},

    {"role": "user", "content": "<command-message>..."},

    {"role": "user", "content": "You are a PDF specialist...", "isMeta": true},

    {"role": "user", "content": {"type": "command_permissions", ...}}

  ]

}

  

**阶段 5: 使用技能上下文执行工具**

Claude 接收注入的上下文：

• 专门的 PDF 处理指令（对话上下文）

• 预批准访问 Bash(pdftotext:*)、Read、Write（执行上下文）

• 清晰的工作流程（对话上下文）

Claude 执行：

  

  

{

  "type": "tool_use",

  "name": "Bash",

  "input": {

    "command": "pdftotext report.pdf output.txt"

  }

}

  

执行成功，读取输出，呈现给用户 ✅

**核心要点总结**

1. **Skills 是提示词模板**，不是可执行代码

2. **Skill 工具（大写 S）** 是管理所有 skills 的元工具，在 tools 数组中

3. Skills **修改对话上下文**（通过 isMeta: true 消息注入指令）

4. Skills **修改执行上下文**（通过更改工具权限和模型选择）

5. 选择通过 **LLM 推理**，而非算法匹配

6. 工具权限**作用域限定在技能执行**期间

7. 每次调用注入**两条用户消息**：一条用于用户可见的元数据，一条用于发送到 API 的隐藏指令

**优雅的设计**

通过将专门知识视为**修改对话上下文的提示词**和**修改执行上下文的权限**，而不是**执行的代码**，Claude Code 实现了传统函数调用难以达到的灵活性、安全性和可组合性。

**参考资源**

• [Introducing Agent Skills](https://www.anthropic.com/news/skills)

• [Equipping Agents for the Real World with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

• [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code/overview)

• [Anthropic API Reference](https://docs.anthropic.com/en/api/messages)

• [Skill Creator Skill](https://github.com/anthropics/skills/tree/main/skill-creator)

• [Internal Comms Skill](https://github.com/anthropics/skills/tree/main/internal-comms)

**引用格式**：

  

  

@article{

    leehanchung_claude_skills,

    author = {Lee, Hanchung},

    title = {Claude Agent Skills: A First Principles Deep Dive},

    year = {2025},

    month = {10},

    day = {26},

    url = {https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/}

}

































