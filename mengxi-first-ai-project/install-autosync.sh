#!/bin/bash
# ============================================================
# install-autosync.sh — 安装 Mengxi Blog 定时同步任务
# 用法：bash install-autosync.sh
# ============================================================

PLIST_NAME="com.mengxi.blog-autosync"
PLIST_SRC="$(cd "$(dirname "$0")" && pwd)/${PLIST_NAME}.plist"
PLIST_DST="$HOME/Library/LaunchAgents/${PLIST_NAME}.plist"

echo "📦 安装 Mengxi Blog 定时同步任务..."

# 1. 复制 plist 到 LaunchAgents
cp "$PLIST_SRC" "$PLIST_DST"
echo "  ✅ plist 已复制到 ~/Library/LaunchAgents/"

# 2. 卸载旧版本（如存在）
launchctl unload "$PLIST_DST" 2>/dev/null

# 3. 加载新任务
launchctl load "$PLIST_DST"
echo "  ✅ 任务已加载"

# 4. 验证
if launchctl list | grep -q "$PLIST_NAME"; then
  echo ""
  echo "🎉 安装成功！定时任务已启动。"
  echo "   · 频率：每 30 分钟自动同步并部署一次"
  echo "   · 日志：~/mengxi-first-ai-project/autosync.log"
  echo "   · 错误：~/mengxi-first-ai-project/autosync-error.log"
  echo ""
  echo "📌 常用命令："
  echo "   立即触发一次：launchctl start $PLIST_NAME"
  echo "   暂停任务：    launchctl unload $PLIST_DST"
  echo "   查看状态：    launchctl list | grep mengxi"
  echo "   卸载任务：    bash uninstall-autosync.sh"
else
  echo "❌ 安装失败，请检查 plist 路径或权限。"
  exit 1
fi
