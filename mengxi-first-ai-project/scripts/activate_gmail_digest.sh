#!/bin/bash
# 📧 Gmail 一键激活脚本 (Zero-Touch Helper)
# 运行此脚本后，只需粘贴 App Password 即可完成全链路激活

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
ENV_FILE="$PROJECT_DIR/.env"

echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║  📧 Gmail 私人主编·一键激活向导                        ║"
echo "╠══════════════════════════════════════════════════════════╣"
echo "║                                                          ║"
echo "║  Chrome 已自动打开 App Password 页面。                   ║"
echo "║  请在页面中:                                             ║"
echo "║    1. 输入名称: mengxi-digest                            ║"
echo "║    2. 点击「创建」                                       ║"
echo "║    3. 复制16位密码                                       ║"
echo "║                                                          ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# 检查是否已有 Gmail 配置
if grep -q "GMAIL_ADDRESS" "$ENV_FILE" 2>/dev/null; then
    echo "✅ .env 中已有 GMAIL 配置"
    grep "GMAIL" "$ENV_FILE"
    echo ""
    echo "如需更新，请手动编辑 $ENV_FILE"
    exit 0
fi

# 获取 Gmail 地址
read -p "📧 请输入你的 Gmail 地址: " gmail_addr
if [ -z "$gmail_addr" ]; then
    echo "❌ Gmail 地址不能为空"
    exit 1
fi

# 获取 App Password  
read -p "🔑 请粘贴 App Password (16位): " app_pwd
if [ -z "$app_pwd" ]; then
    echo "❌ App Password 不能为空"
    exit 1
fi

# 写入 .env
echo "" >> "$ENV_FILE"
echo "# Gmail Private Editor (auto_gmail_digest.py)" >> "$ENV_FILE"
echo "GMAIL_ADDRESS=$gmail_addr" >> "$ENV_FILE"
echo "GMAIL_APP_PASSWORD=$app_pwd" >> "$ENV_FILE"

echo ""
echo "✅ Gmail 配置已写入 $ENV_FILE"
echo ""

# 立即测试
echo "🧪 正在测试连接..."
python3 "$SCRIPT_DIR/auto_gmail_digest.py"

echo ""
echo "🎉 全链路激活完成！系统已进入永久自动驾驶状态！"
echo "   每 30 分钟自动运行，绝不再打扰你。"
echo "   安心去生宝宝吧！🍼"
