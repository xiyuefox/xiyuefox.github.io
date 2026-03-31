#!/bin/bash
# ═══════════════════════════════════════════════════════════════════
# 🛡️ sync.sh v2.0 — 自愈守护模式 (Watchdog-Powered Sync Pipeline)
# ═══════════════════════════════════════════════════════════════════
# 升级说明：
#   - 所有 Python 脚本现通过 auto_watchdog.py 执行，自动拦截异常
#   - 单个脚本失败不再中断整个流水线（故障隔离）
#   - 异常自动调用 LLM 生成修复补丁并沙盒验证
#   - 事件报告、Git 历史、macOS 通知自动归档
#
# 原始调用方式（已保留为注释可回退）:
#   python3 -u scripts/fetch_hn_feed.py
# 新调用方式:
#   python3 scripts/auto_watchdog.py --script scripts/fetch_hn_feed.py
# ═══════════════════════════════════════════════════════════════════

echo "🚀 开始自愈模式智能同步流程 (v2.0 Watchdog-Powered)..."

# ── 加载环境变量 ──────────────────────────────────────────────
if [ -f "/Users/hulimofaqiu/mengxi-first-ai-project/.env" ]; then
    echo "🔑 加载本地 .env 环境变量"
    export $(cat "/Users/hulimofaqiu/mengxi-first-ai-project/.env" | grep -v '^#' | xargs)
fi

cd "/Users/hulimofaqiu/mengxi-first-ai-project"

# ── 检查依赖 ────────────────────────────────────────────────
echo "📦 检查所需依赖..."
if ! python3 -c "import pypinyin" &> /dev/null; then
    echo "⚠️ 缺少 pypinyin 模块，正在安装..."
    pip3 install --user pypinyin
fi

if ! python3 -c "import yaml" &> /dev/null; then
    echo "⚠️ 缺少 PyYAML 模块，正在安装..."
    pip3 install --user pyyaml
fi

# ── 定义 Watchdog 安全执行函数 ────────────────────────────────
# 如果 auto_watchdog.py 可用则使用自愈模式，否则回退普通模式
WATCHDOG="scripts/auto_watchdog.py"

run_safe() {
    local script="$1"
    local label="$2"

    echo ""
    echo "🔄 ${label}..."

    if [ -f "$WATCHDOG" ]; then
        # 🛡️ 自愈模式：通过 watchdog 执行，自动拦截异常
        python3 "$WATCHDOG" --script "$script" --no-notify 2>&1
    else
        # 🔧 回退模式：裸执行（兼容旧逻辑）
        python3 -u "$script" 2>&1
    fi
}

# ═══════════════════════════════════════════════════════════════
# 🛡️ Phase 1: 全系统健康预检 (Pre-flight Health Scan)
# ═══════════════════════════════════════════════════════════════
echo ""
echo "🔍 ═══ Phase 1: 全系统健康预检 ═══"
if [ -f "$WATCHDOG" ]; then
    python3 "$WATCHDOG" --scan --no-notify 2>&1
fi

# ═══════════════════════════════════════════════════════════════
# 🔄 Phase 2: 数据抓取 (Data Fetching)
# ═══════════════════════════════════════════════════════════════
echo ""
echo "🔄 ═══ Phase 2: 数据抓取 ═══"

run_safe "scripts/fetch_hn_feed.py" \
    "正在自动化拉取 Hacker News 最新育儿与女性职场讨论"

run_safe "scripts/fetch_dxy_mom.py" \
    "正在拉取 丁香妈妈 最新孕育科普指南"

run_safe "scripts/fetch_xhs_avoid_pits.py" \
    "正在联动本地小红书 MCP 自动化抓取 待产包/避坑指南"

run_safe "scripts/fetch_newborn_care_rss.py" \
    "正在通过 RSS 拉取新生儿科学护理与循证医学指南"

run_safe "scripts/fetch_newborn_care.py" \
    "正在拉取医疗级新生儿护理 S.O.P (52天周期)"

run_safe "scripts/fetch_labor_delivery.py" \
    "正在拉取分娩决策与 36周+ 临产指标监控"

run_safe "scripts/fetch_montessori.py" \
    "正在同步蒙氏 0-1岁 Nido 家庭方案"

# echo "🔄 正在同步小红书母婴博主干货..."
# run_safe "scripts/sync_xhs_maternity.py" "小红书母婴"

# echo "🔄 正在同步小红书教育频道内容..."
# run_safe "scripts/sync_xhs_education.py" "小红书教育"

run_safe "scripts/fetch_math_puzzles.py" \
    "正在同步数学解谜与逻辑思维看板"

run_safe "scripts/fetch_logic_puzzles.py" \
    "正在解析数学逻辑与 Smart Games 矩阵"

run_safe "scripts/fetch_podcast.py" \
    "正在抓取全球蒙氏与极客育儿高分播客 (Podcasts)"

run_safe "scripts/fetch_poche_feed.py" \
    "正在同步 poche.app 精神母舰看板"

run_safe "scripts/fetch_news_feed.py" \
    "正在自动挂载全局 RSS 资讯源并降噪清洗"

# ═══════════════════════════════════════════════════════════════
# 🌱 Phase 3: 内容组装 (Content Assembly)
# ═══════════════════════════════════════════════════════════════
echo ""
echo "🌱 ═══ Phase 3: 内容组装 ═══"

run_safe "scripts/sync_early_learning_hub.py" \
    "正在组装 Early Learning Hub (0-1岁) 每日硬核 AI 榜单"

run_safe "scripts/sync_xiaoxi_channel.py" \
    "正在重组 小溪的极客成长板 (Product/Tech)"

echo ""
echo "📂 正在同步自动化情报看板离线缓存至 Obsidian 库..."
cp posts/md/*.md "/Users/hulimofaqiu/Documents/obisidian笔记文件/育儿/" 2>/dev/null

run_safe "scripts/generate_daily_quote.py" \
    "正在织入《男孩、鼹鼠、狐狸和马》治愈一言看板"

run_safe "scripts/generate_schedule.py" \
    "正在织入孕晚期 35周+ 科学作息时间看板"

# ═══════════════════════════════════════════════════════════════
# 🔗 Phase 4: 核心同步 (Core Sync — Critical Path)
# ═══════════════════════════════════════════════════════════════
echo ""
echo "🔗 ═══ Phase 4: 核心同步 (Critical Path) ═══"

run_safe "scripts/sync_obsidian.py" \
    "正在扫描并智能筛选 Obsidian 笔记（自动过滤草稿与碎片）"

run_safe "scripts/generate_matrix.py" \
    "正在生成 AI 内容矩阵宣发物料（小红书/Twitter/朋友圈/Newsletter/SEO）"

# 核心同步失败的判定：检查 index.html 是否正常更新
if [ ! -f "public/index.html" ] || [ ! -s "public/index.html" ]; then
    echo "❌ 核心同步后 public/index.html 异常，部署中断！"
    if [ -f "$WATCHDOG" ]; then
        python3 "$WATCHDOG" --scan-log logs/error.log --no-notify 2>&1
    fi
    exit 1
fi

# ═══════════════════════════════════════════════════════════════
# 🎵 Phase 5: 资产同步 (Asset Sync)
# ═══════════════════════════════════════════════════════════════
echo ""
echo "🎵 ═══ Phase 5: 资产同步 ═══"

echo "🎵 正在同步治愈音声音乐资产到部署目录..."
mkdir -p public/images/music
cp -rf images/music/* public/images/music/ 2>/dev/null

# ═══════════════════════════════════════════════════════════════
# 🌐 Phase 6: 部署 (Deploy to Cloudflare)
# ═══════════════════════════════════════════════════════════════
echo ""
echo "🌐 ═══ Phase 6: 部署到 Cloudflare Pages ═══"
npx wrangler pages deploy public --project-name="mengxi-blog"

DEPLOY_EXIT=$?

# ═══════════════════════════════════════════════════════════════
# 📊 Phase 7: 执行摘要 (Final Report)
# ═══════════════════════════════════════════════════════════════
echo ""
echo "═══════════════════════════════════════════════════════"
if [ $DEPLOY_EXIT -eq 0 ]; then
    echo "✅ 自愈模式同步 + 部署完成！🎉"
    echo "   📋 事件日志: logs/watchdog/incident_history.jsonl"
    echo "   📁 补丁归档: logs/watchdog/patches/"
    echo "   📊 运行日志: logs/watchdog/watchdog.log"
else
    echo "⚠️ 部署过程中出现警告或错误，请检查日志。"
    echo "   📋 错误日志: logs/watchdog/watchdog.log"
fi
echo "═══════════════════════════════════════════════════════"
