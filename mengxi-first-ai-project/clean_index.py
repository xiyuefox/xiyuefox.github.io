import re

index_path = "/Users/hulimofaqiu/mengxi-first-ai-project/index.html"

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 寻找 <div class="tg-welcome-text"> 到 节末 的连绵重复块
pattern = r'(<div class="tg-welcome-text">[\s\S]*?<p class="tg-welcome-sub">\./explore_around\.sh \| grep "curiosity"</p>)([\s\S]*?)(</div>\s*</div>\s*</section>)'

matches = re.search(pattern, content)
if matches:
    print("Found welcome text container. Cleaning up messy injections...")
    base_text = matches.group(1)
    end_tag = matches.group(3)
    
    # 组合为净版：加入注释标记方便将来正则安全替换
    cleaned_content = base_text + """
    <!-- HEALING_QUOTE_START -->
    <!-- HEALING_QUOTE_END -->
    <!-- SCHEDULE_START -->
    <!-- SCHEDULE_END -->
    """ + end_tag
    
    # 替换回全文
    content = content.replace(matches.group(0), cleaned_content)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ index.html 已被清理干净并添加了精准替换锚点。")
else:
    print("⚠️ 无法匹配到 welcome text 目标清除范围。")
