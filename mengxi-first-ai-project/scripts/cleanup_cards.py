import os
import re

filepath = "/Users/hulimofaqiu/mengxi-first-ai-project/index.html"

if not os.path.exists(filepath):
    print("File not found")
    exit(1)

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 使用正则表达式移除包含特定链接的整个 <a> 标签
patterns = [
    r'<a href="post\.html\?post=wen-zhang-biao-ti".*?</a>',
    r'<a href="post\.html\?post=notion-api-guide".*?</a>',
    r'<a href="post\.html\?post=auto-draw-for-pen".*?</a>',
    r'<a href="post\.html\?post=auto-layout".*?</a>'
]

new_content = content
for pattern in patterns:
    new_content = re.sub(pattern, '', new_content, flags=re.DOTALL)

if new_content != content:
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("✅ 成功移除 index.html 中占位/系统工具卡片")
else:
    print("⚠️ 未发现需要移除的内容，或可能匹配失败")
