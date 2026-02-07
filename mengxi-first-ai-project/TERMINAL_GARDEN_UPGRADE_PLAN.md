# 🌿 Mengxi.Space Terminal Garden 升级计划

> 参考灵感: [poche.app/fonter](https://poche.app/fonter) - Terminal-Chic 复古终端风格
> 
> 核心原则: **保持元内容不变 + 自动化发布不变 + 更好玩有趣**

---

## 📊 现状分析

### ✅ 工作正常的部分

| 组件 | 状态 | 说明 |
|------|------|------|
| GitHub Actions | ✅ | deploy.yml 配置完整，自动部署到 Cloudflare |
| Obsidian 同步 | ✅ | obsidian_to_hugo.py 功能完善 |
| Hugo 配置 | ✅ | hugo.toml 结构正确 |
| CSS 设计系统 | ✅ | unified-styles.css 统一风格 |
| 一键发布 | ✅ | sync-and-publish.sh 可用 |

### ⚠️ 需要整理的问题

| 问题 | 位置 | 建议 |
|------|------|------|
| 冗余目录 | blog/public_preview* (11个) | 删除所有预览目录 |
| 散落文件 | 根目录 20+ HTML 文件 | 移动到 /apps/ 目录 |
| 重复文档 | *_REPORT.md, *_ROADMAP.md | 合并到 /docs/ |
| 占位符 | hugo.toml github url | 更新为真实链接 |

### ❌ 潜在冲突

1. **designer-showcase 双重存在**: 根目录 + blog/static/，每次 sync 会重复复制
2. **环境变量不一致**: deploy.yml 中 `OBSIDIAN_VAULT_PATH='./obsidian-vault'` vs 本地实际路径
3. **入口分散**: index.html (FamilyHub) 和 blog/ (Hugo) 是独立入口

---

## 🎯 升级目标

### 参考 Poche.app/fonter 的设计精髓

```
┌─────────────────────────────────────────────────────────────────┐
│  🌙 TERMINAL-CHIC AESTHETIC                                    │
│                                                                 │
│  • 深蓝/深紫暗色背景 (#0E101F)                                   │
│  • 霓虹蓝/紫点缀色 (#2D3494, #6C5CE7)                            │
│  • 等宽字体 (JetBrains Mono, Fira Code)                         │
│  • CLI 命令按钮 (./launch, ./explore, ./read)                   │
│  • 可爱 ASCII 吉祥物                                            │
│  • 动态悬停效果 + 微动画                                         │
│                                                                 │
│  ᕱ⑅ᕱ  <-- 吉祥物示例 (小羊)                                     │
│  --Mengxi                                                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📋 实施计划

### Phase 1: 清理整理 (30 min) 🧹

```bash
# 1.1 删除冗余预览目录
rm -rf blog/public_preview*

# 1.2 创建 apps 目录并移动工具
mkdir -p apps
mv contraction-timer.html apps/
mv feeding-tracker.html apps/
mv diaper-counter.html apps/
mv sleep-tracker.html apps/
mv pregnancy_calculator.html apps/
mv pregnancy-food-game.html apps/
mv sugar-checker.html apps/
mv upload.html apps/
# ... 等等

# 1.3 合并文档到 docs/
mv *_REPORT.md docs/archive/
mv *_ROADMAP.md docs/archive/
```

**修复点**:
- [ ] 更新 hugo.toml 中的 github 占位符
- [ ] 统一 OBSIDIAN_VAULT_PATH 配置
- [ ] 更新 index.html 中的应用链接路径

---

### Phase 2: 设计系统升级 (1 hr) 🎨

创建 `css/terminal-garden.css`:

```css
/* Terminal Garden Design System */
:root {
  /* === Dark Mode (Default) === */
  --bg-primary: #0E101F;
  --bg-secondary: #161832;
  --bg-card: #1A1C36;
  
  --accent-blue: #48DBFB;
  --accent-purple: #6C5CE7;
  --accent-pink: #FD79A8;
  --accent-green: #00CEC9;
  
  --text-primary: #F5F6FA;
  --text-secondary: #A4B0BE;
  --text-muted: #636E72;
  
  --border-color: #2D3436;
  
  /* === Typography === */
  --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
  --font-display: 'Inter', sans-serif;
  
  /* === CLI Prefix === */
  --cli-prefix: './';
}

/* Light Mode Override */
[data-theme="light"] {
  --bg-primary: #FFF7ED;
  --bg-secondary: #F5F0E8;
  --bg-card: #FFFFFF;
  --text-primary: #2D3436;
  --text-secondary: #636E72;
}

/* CLI Style Buttons */
.btn-cli {
  font-family: var(--font-mono);
  background: transparent;
  border: 1px solid var(--accent-purple);
  color: var(--accent-purple);
  padding: 0.5rem 1rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-cli::before {
  content: var(--cli-prefix);
  opacity: 0.6;
}

.btn-cli:hover {
  background: var(--accent-purple);
  color: var(--bg-primary);
  transform: translateY(-2px);
}
```

---

### Phase 3: 首页改造 (1 hr) 🏠

将 `index.html` 改造为 Terminal Garden 风格:

**新布局结构**:
```
┌─────────────────────────────────────────────────────────────────┐
│  🌙 Terminal Garden                           [./theme] [./rss] │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ᕱ⑅ᕱ  Welcome to Mengxi's Digital Garden                       │
│  ---                                                            │
│  > A playful space for family tools, learning, and ideas.       │
│                                                                 │
├──────────────┬──────────────────────────────────────────────────┤
│              │                                                  │
│  [./explore] │  ┌────────────┐ ┌────────────┐ ┌────────────┐   │
│              │  │ 🤰 Labor   │ │ 🍼 Feeding │ │ 😴 Sleep   │   │
│  Categories  │  │ Timer      │ │ Tracker    │ │ Tracker    │   │
│  ───────────│  │ ./launch   │ │ ./launch   │ │ ./launch   │   │
│  Baby [6]    │  └────────────┘ └────────────┘ └────────────┘   │
│  Learn [4]   │                                                  │
│  Play [3]    │  ┌────────────┐ ┌────────────┐ ┌────────────┐   │
│  Dev [2]     │  │ 🌱 Early   │ │ 🧠 Know-   │ │ 🎨 Design  │   │
│              │  │ Learning   │ │ ledge      │ │ Showcase   │   │
│              │  │ ./enter    │ │ ./explore  │ │ ./view     │   │
│              │  └────────────┘ └────────────┘ └────────────┘   │
│              │                                                  │
└──────────────┴──────────────────────────────────────────────────┘
```

**特色元素**:
- 吉祥物: 可爱的 ASCII 艺术 (🦊 小狐狸 或 ᕱ⑅ᕱ 小羊)
- CLI 风格导航
- 卡片瀑布流
- 实时分类计数 `[6]`
- 主题切换按钮

---

### Phase 4: Hugo 主题升级 (2 hr) 📖

更新 `blog/themes/starter-theme/`:

1. **布局改进**:
   - 侧边栏分类导航
   - 文章卡片样式
   - 代码块语法高亮

2. **样式统一**:
   - 引入 Terminal Garden 设计系统
   - 等宽字体用于代码和日期
   - CLI 风格标签

3. **交互增强**:
   - 平滑滚动
   - 悬停动画
   - 加载过渡

---

### Phase 5: 验证自动化 (30 min) ✅

```bash
# 测试本地发布流程
./scripts/sync-and-publish.sh

# 验证 GitHub Actions
git add -A
git commit -m "feat: Terminal Garden upgrade"
git push origin main

# 检查 Cloudflare Pages 部署
open https://mengxi.space
```

---

## 🗂️ 文件结构调整

### 调整前:
```
mengxi-first-ai-project/
├── contraction-timer.html  ← 散落
├── feeding-tracker.html    ← 散落
├── BLOG_ANALYSIS_REPORT.md ← 重复文档
├── OPTIMIZATION_REPORT.md  ← 重复文档
├── blog/
│   ├── public_preview/     ← 冗余
│   ├── public_preview_final/ ← 冗余
│   └── ...
└── ...
```

### 调整后:
```
mengxi-first-ai-project/
├── index.html              ← Terminal Garden 首页
├── apps/                   ← 工具集中存放
│   ├── contraction-timer.html
│   ├── feeding-tracker.html
│   └── ...
├── css/
│   ├── unified-styles.css
│   └── terminal-garden.css ← 新主题
├── docs/
│   ├── OBSIDIAN_WORKFLOW_GUIDE.md
│   └── archive/            ← 旧文档归档
├── blog/
│   └── public/             ← 只保留最终构建
└── ...
```

---

## 🎭 吉祥物设计 - 小马驹 🐴

**确定选择**: 小马驹 (取名 "Mengxi" 或 "小骏")

```
    ,
   /|
  /_|    ⌐╦╦═─
 (o o)    
  \__/    --Mengxi
   ||
  _||_
 
  或简化版:
  
  ᐱᐱ
 (◕‿◕)🐴
  ──Mengxi
```

**寓意**: 
- 马驹象征活力、奔跑、成长
- "骏" 与 "Mengxi" 谐音呼应
- 体现家庭育儿的希望与活力

---

## ⏱️ 时间估算

| Phase | 任务 | 时间 |
|-------|------|------|
| 1 | 清理整理 | 30 min |
| 2 | 设计系统 | 1 hr |
| 3 | 首页改造 | 1 hr |
| 4 | Hugo 主题 | 2 hr |
| 5 | 验证部署 | 30 min |
| **总计** | | **~5 hr** |

---

## 🔒 保持不变

以下核心功能将保持不变:

1. ✅ **Obsidian 同步逻辑** - obsidian_to_hugo.py 不改动
2. ✅ **Cloudflare 部署** - deploy.yml 不改动
3. ✅ **内容分类结构** - sparks, notes, ideas, growth
4. ✅ **一键发布脚本** - sync-and-publish.sh 不改动
5. ✅ **R2 图床配置** - 保持不变

---

## 🚀 下一步行动

1. **确认计划**: 你是否满意这个升级方向？
2. **选择吉祥物**: 喜欢哪个小动物？
3. **开始执行**: 我将按 Phase 顺序逐步实施

---

*Made with ❤️ for Mengxi's Digital Garden*
