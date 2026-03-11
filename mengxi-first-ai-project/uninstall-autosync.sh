#!/bin/bash
# ============================================================
# uninstall-autosync.sh — 卸载 Mengxi Blog 定时同步任务
# 用法：bash uninstall-autosync.sh
# ============================================================

PLIST_NAME="com.mengxi.blog-autosync"
PLIST_DST="$HOME/Library/LaunchAgents/${PLIST_NAME}.plist"

echo "🗑️  卸载 Mengxi Blog 定时同步任务..."

launchctl unload "$PLIST_DST" 2>/dev/null
rm -f "$PLIST_DST"

if ! launchctl list | grep -q "$PLIST_NAME"; then
  echo "✅ 任务已停止并移除。"
else
  echo "⚠️  移除可能未完全生效，请重新登录后确认。"
fi
