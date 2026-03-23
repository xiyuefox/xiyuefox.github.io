#!/usr/bin/env python3
import os
import requests
import re
import time

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_PATH = os.path.join(PROJECT_DIR, "posts", "md", "fen-mian-jue-ce-yu-lin-chan-ji-zhen-jian-ce-36-zhou-zhuan-shu.md")

# Load environment variables from .env if it exists
env_path = os.path.join(PROJECT_DIR, ".env")
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                try:
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value.replace('"', '').replace("'", "")
                except ValueError:
                    pass

def summarize_with_gemini(title, summary_text):
    """使用 Gemini 提炼分娩决策与临产触发监测 S.O.P。"""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
         print("   ⚠️ No API Key found.")
         return ""
         
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
        headers = {'Content-Type': 'application/json'}
        prompt = f"""你现在是上海红房子医院急诊科的资深分娩导乐。请对资讯进行极简提炼。
文章标题: {title}
文章内容: {summary_text}

提取要求：
1. 分辨【顺产/剖宫产选择】：提取具体的医学指征（如胎位、头盆关系、既往手术史等）。
2. 构建【入院决策树】：清晰标注 36 周后的‘必入指征’（如：511 宫缩原则、高位破水、胎动减少）。
3. 生成【急诊 S.O.P】：罗列入院那一刻所需的证件（身份证、医保卡、小卡等）。
4. 语言风格：冷峻、量化、排除干扰项，直接输出结论性清单。使用短划线 - 开头。不要感叹号和废话。
"""
        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        res = requests.post(url, headers=headers, json=payload, timeout=20)
        if res.status_code == 200:
             data = res.json()
             parts = data.get('candidates', [{}])[0].get('content', {}).get('parts', [])
             if parts:
                  return parts[0].get('text', '').strip()
        else:
            print(f"       Gemini Error: {res.status_code} - {res.text}")
    except Exception as e:
         print(f"   ⚠️ Gemini 摘要异常: {e}")
    return ""

def main():
    if not os.path.exists(MD_PATH):
        print(f"File not found: {MD_PATH}")
        return

    print(f"Reading file: {MD_PATH}")
    with open(MD_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    blocks = content.split('---')
    if len(blocks) < 3:
        print("Invalid file structure.")
        return

    frontmatter = blocks[1]
    body = '---'.join(blocks[2:])

    cards_count = 0
    
    def process_card_match(match):
        nonlocal cards_count
        full_match = match.group(0)
        title_section = match.group(1)
        raw_content = match.group(2)
        
        # Extract title text without markdown link padding if needed
        # #### [Title](Link)
        title_text = title_section
        title_link_match = re.search(r'\[(.*?)\]', title_section)
        if title_link_match:
            title_text = title_link_match.group(1)
            
        print(f"👉 Processing item: {title_text[:30]}")
        summary = summarize_with_gemini(title_text, raw_content)
        time.sleep(1)
        
        if summary:
            cards_count += 1
            # Reconstruct card with new summary
            new_card = f"""
#### {title_section}
> **⚕️ 分娩决策 S.O.P：**
{summary.strip()}

<details>
<summary>📂 查看原始卷宗 (Raw Data)</summary>

{raw_content.strip()}

</details>
"""
            return new_card
        else:
            print("   ⚠️ Summary update skipped.")
            return full_match

    # Pattern to match the item card
    # #### title_link
    # > **⚕️ 分娩决策 S.O.P：**
    # （总结未生成...）
    # \n\n<details>\n<summary>📂 查看原始卷宗 (Raw Data)</summary>\n\nraw_content\n\n</details>
    pattern = r'#### (.*?)\r?\n> \*\*⚕️ 分娩决策 S.O.P：\*\*\r?\n（总结未生成，具体请查阅原帖）\r?\n\r?\n<details>\r?\n<summary>.*?\r?\n\r?\n(.*?)\r?\n\r?\n</details>'
    
    updated_body = re.sub(pattern, process_card_match, body, flags=re.DOTALL)
    
    if cards_count == 0:
        print("No matches to backfill or updates found.")
        return

    final_output = f"---{frontmatter}---" + updated_body
    
    with open(MD_PATH, 'w', encoding='utf-8') as f:
        f.write(final_output)

    print(f"✅ Backfilled summaries for {cards_count} items in {MD_PATH}")

if __name__ == "__main__":
    main()
