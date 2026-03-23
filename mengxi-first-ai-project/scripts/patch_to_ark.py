import glob
import os
import re

scripts = glob.glob("/Users/hulimofaqiu/mengxi-first-ai-project/scripts/*.py")

patch_code = """def call_gemini_summarize(text_content):
    import sys
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    import ark_helper
"""

for script in scripts:
    if "ark_helper.py" in script or "sync_obsidian.py" in script:
        continue
        
    with open(script, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "call_gemini_summarize" in content:
        print(f"Patching: {script}")
        # Find the system_prompt block
        prompt_match = re.search(r'(system_prompt\s*=\s*""".*?""")', content, re.DOTALL)
        if prompt_match:
            sys_prompt = prompt_match.group(1)
            new_func = f"""def call_gemini_summarize(text_content):
    import sys
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    import ark_helper

    # 继承原稿 Prompt
    {sys_prompt}
    return ark_helper.call_ark_summarize(text_content, system_prompt=system_prompt)
"""
            # Replace the old function definition body
            # Matches def call_gemini_summarize(...) until return "⚠️ 生成超时崩溃" or equivalent end
            content = re.sub(
                r'def call_gemini_summarize\(text_content\):.*?(\n\s*return\s+["\'].*?["\']|\n\s*return\s+part_text|\n\s*return\s+summary|\n\s*return\s+"⚠️ 生成超时崩溃")',
                new_func,
                content,
                flags=re.DOTALL
            )
            
            with open(script, 'w', encoding='utf-8') as f:
                f.write(content)
                
    if "generate_summary" in content and "gemini_helper" not in script:
        print(f"Patching generate_summary in: {script}")
        content = re.sub(r'def generate_summary\(.*?\):.*?def ', 'def ', content, flags=re.DOTALL) # Placeholder or wrapper
        # For simplicity, if they use gemini_helper.generate_summary, we just make gemini_helper use Ark inside itself!

print("Updating gemini_helper.py to wrap Ark...")
with open("/Users/hulimofaqiu/mengxi-first-ai-project/scripts/gemini_helper.py", 'w', encoding='utf-8') as f:
    f.write("""#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import ark_helper

def generate_summary(text_content):
    system_prompt = \"\"\"
你是一个专业的育儿和教育AI助手。请针对以下拉取到的小红书贴子内容，提供一个**详细的要点总结**。
总结应当：
1. **提炼核心观点**（博主的核心建议、知识点）。
2. **整理热门讨论/避坑指南**（如果有提及实操经验、注意事项、避坑点）。
3. 结构清晰，使用 Markdown 符号分点表达，语言通俗易懂，带有亲和力。
\"\"\"
    return ark_helper.call_ark_summarize(text_content, system_prompt=system_prompt)
""")
