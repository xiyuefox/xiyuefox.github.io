#!/bin/bash
# 一键智能同步并部署 Obsidian 博客文章
# 无需手动添加 #publish 标签，脚本自动过滤草稿和短片段，保留高质量长文。

echo "🚀 开始一键智能同步流程..."

# 检查环境变量和依赖
cd "/Users/hulimofaqiu/mengxi-first-ai-project"

echo "📦 检查所需依赖..."
if ! python3 -c "import pypinyin" &> /dev/null; then
    echo "⚠️ 缺少 pypinyin 模块，正在安装..."
    pip3 install --user pypinyin
fi

echo "🔄 正在扫描并智能筛选 Obsidian 笔记（自动过滤草稿与碎片）..."
python3 scripts/sync_obsidian.py

if [ $? -ne 0 ]; then
    echo "❌ 同步脚本执行失败，部署中断！"
    exit 1
fi

echo "🌐 开始部署到 Cloudflare Pages..."
npx wrangler pages deploy public --project-name="mengxi-blog"

if [ $? -eq 0 ]; then
    echo "✅ 一步到位部署完成！您的最新随笔已上线。"
else
    echo "⚠️ 部署过程中出现警告或错误，请检查日志。"
fi
