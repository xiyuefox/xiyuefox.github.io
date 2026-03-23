
import re
import os

target_file = "/Users/hulimofaqiu/Documents/obisidian笔记文件/math magic.md"

def process_file(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            # 1. Deletion Rules
            # Remove lines containing "Explanation 解释" or "为什么"
            if "Explanation 解释" in line:
                continue
            if "为什么" in line:
                continue
            
            # 2. Formatting Rules
            # Highlight "why" (case-insensitive) with bold, preserving case
            # Using function in re.sub to check case of match? 
            # OR just re.sub with ignorecase and using capture group.
            
            # Pattern: word boundary 'why' word boundary
            # Replacement: **match**
            
            def bold_replacer(match):
                return f"**{match.group(0)}**"
            
            # Apply regex
            processed_line = re.sub(r'\bwhy\b', bold_replacer, line, flags=re.IGNORECASE)
            new_lines.append(processed_line)

        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
            
        print(f"✅ Successfully processed {file_path}")
        print("   - Removed lines with 'Explanation 解释' and '为什么'")
        print("   - Bolded all instances of 'why'")

    except Exception as e:
        print(f"❌ Error processing file: {e}")

if __name__ == "__main__":
    process_file(target_file)
