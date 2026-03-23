#!/bin/bash
PROJECT_DIR="/Users/hulimofaqiu/mengxi-first-ai-project"
cd "$PROJECT_DIR" || exit

# 1. 尝试从文件夹下的 .env 载入环境变量 (例如 GEMINI_API_KEY)
if [ -f .env ]; then
    # 过滤注释与空行，载入
    export $(grep -v '^#' .env | xargs)
fi

# 2. 调用 Miniconda 的 Python 执行脚本并保存日志
/Users/hulimofaqiu/miniconda3/bin/python3 "$PROJECT_DIR/scripts/fetch_maker_parenting.py" >> "$PROJECT_DIR/scripts/ai_summary_cron_logs.log" 2>&1
echo "✅ AI 摘要抓取于 $(date) 执行完毕。" >> "$PROJECT_DIR/scripts/ai_summary_cron_logs.log"
