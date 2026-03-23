#!/bin/bash
# 一键配置 macOS launchd 自动化守护进程

PROJECT_DIR="/Users/hulimofaqiu/mengxi-first-ai-project"
PLIST_NAME="com.mengxi.sync.plist"
PLIST_PATH="$HOME/Library/LaunchAgents/$PLIST_NAME"

echo "⚙️  正在生成 launchd 配置文件..."

# 确保日志目录存在
mkdir -p "$PROJECT_DIR/logs"

# 生成 .plist 内容
cat << EOF > "$PLIST_PATH"
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.mengxi.sync</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/zsh</string>
        <string>$PROJECT_DIR/scripts/sync_wrapper.sh</string>
    </array>
    <key>StartCalendarInterval</key>
    <array>
        <dict>
            <key>Hour</key>
            <integer>8</integer>
            <key>Minute</key>
            <integer>30</integer>
        </dict>
        <dict>
            <key>Hour</key>
            <integer>14</integer>
            <key>Minute</key>
            <integer>30</integer>
        </dict>
    </array>
    <key>StandardOutPath</key>
    <string>$PROJECT_DIR/logs/sync.log</string>
    <key>StandardErrorPath</key>
    <string>$PROJECT_DIR/logs/error.log</string>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
EOF

echo "✅ 配置文件已生成至: $PLIST_PATH"

# 赋予包装脚本执行权限
chmod +x "$PROJECT_DIR/scripts/sync_wrapper.sh"

echo "🔄 正在加载 launchd 任务..."

# 如果已经加载，先卸载
launchctl unload "$PLIST_PATH" 2>/dev/null || true

# 加载新配置
launchctl load "$PLIST_PATH"

if launchctl list | grep -q "com.mengxi.sync"; then
    echo "🎉 launchd 自动化守护进程配置成功！"
    echo "⏰ 定时规则：每天 08:30 & 14:30 自动静默执行"
    echo "📄 查看日志：tail -f $PROJECT_DIR/logs/sync.log"
else
    echo "❌ 加载失败，请检查 plist 格式。"
fi
