#!/bin/bash
# 一键智能同步并部署 Obsidian 博客文章
# 无需手动添加 #publish 标签，脚本自动过滤草稿和短片段，保留高质量长文。

echo "🚀 开始一键智能同步流程..."

# 强制加载本地环境变量，确保后台 Launchd 进程能读到 API Key
if [ -f "/Users/hulimofaqiu/mengxi-first-ai-project/.env" ]; then
    echo "🔑 加载本地 .env 环境变量"
    export $(cat "/Users/hulimofaqiu/mengxi-first-ai-project/.env" | grep -v '^#' | xargs)
fi

# 检查环境变量和依赖
cd "/Users/hulimofaqiu/mengxi-first-ai-project"

echo "📦 检查所需依赖..."
if ! python3 -c "import pypinyin" &> /dev/null; then
    echo "⚠️ 缺少 pypinyin 模块，正在安装..."
    pip3 install --user pypinyin
fi

if ! python3 -c "import yaml" &> /dev/null; then
    echo "⚠️ 缺少 PyYAML 模块，正在安装..."
    pip3 install --user pyyaml
fi

echo "🔄 正在自动化拉取 Hacker News 最新育儿与女性职场讨论..."
python3 -u scripts/fetch_hn_feed.py

echo "🔄 正在拉取 丁香妈妈 最新孕育科普指南..."
python3 -u scripts/fetch_dxy_mom.py

echo "🔄 正在联动本地小红书 MCP 自动化抓取 待产包/避坑指南 (轻量降噪版)..."
python3 -u scripts/fetch_xhs_avoid_pits.py

echo "🔄 正在通过 RSS 拉取新生儿科学护理与循证医学指南..."
python3 -u scripts/fetch_newborn_care_rss.py

echo "🔄 正在拉取医疗级新生儿护理 S.O.P (52天周期)..."
python3 -u scripts/fetch_newborn_care.py

echo "🔄 正在拉取分娩决策与 36周+ 临产指标监控..."
python3 -u scripts/fetch_labor_delivery.py

echo "🔄 正在同步蒙氏 0-1岁 Nido 家庭方案..."
python3 -u scripts/fetch_montessori.py

# echo "🔄 正在同步小红书母婴博主干货..."
# python3 -u scripts/sync_xhs_maternity.py

# echo "🔄 正在同步小红书教育频道内容..."
# python3 -u scripts/sync_xhs_education.py

echo "🔄 正在同步数学解谜与逻辑思维看板..."
python3 -u scripts/fetch_math_puzzles.py

echo "🔄 正在解析数学逻辑与 Smart Games 矩阵..."
python3 -u scripts/fetch_logic_puzzles.py

echo "🔄 正在抓取全球蒙氏与极客育儿高分播客 (Podcasts)..."
python3 -u scripts/fetch_podcast.py

echo "🔄 正在同步 poche.app 精神母舰看板..."
python3 -u scripts/fetch_poche_feed.py

echo "🌱 正在组装 Early Learning Hub (0-1岁) 每日硬核 AI 榜单..."
python3 -u scripts/sync_early_learning_hub.py

echo "🧠 正在重组 小溪的极客成长板 (Product/Tech)..."
python3 -u scripts/sync_xiaoxi_channel.py

echo "📂 正在同步自动化情报看板离线缓存至 Obsidian 库..."
cp posts/md/*.md "/Users/hulimofaqiu/Documents/obisidian笔记文件/育儿/"

echo "💖 正在织入《男孩、鼹鼠、狐狸和马》治愈一言看板..."
python3 -u scripts/generate_daily_quote.py

echo "📅 正在织入孕晚期 35周+ 科学作息时间看板..."
python3 -u scripts/generate_schedule.py

echo "🔄 正在扫描并智能筛选 Obsidian 笔记（自动过滤草稿与碎片）..."
python3 -u scripts/sync_obsidian.py

if [ $? -ne 0 ]; then
    echo "❌ 同步脚本执行失败，部署中断！"
    exit 1
fi

echo "🎵 正在同步治愈音声音乐资产到部署目录..."
mkdir -p public/images/music
cp -rf images/music/* public/images/music/

echo "🌐 开始部署到 Cloudflare Pages..."
npx wrangler pages deploy public --project-name="mengxi-blog"

if [ $? -eq 0 ]; then
    echo "✅ 一步到位部署完成！您的最新随笔已上线。"
else
    echo "⚠️ 部署过程中出现警告或错误，请检查日志。"
fi
