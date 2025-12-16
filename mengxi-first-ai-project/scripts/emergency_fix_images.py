
import re
import os

target_file = "/Users/hulimofaqiu/Documents/obisidian笔记文件/math magic.md"

def emergency_fix(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Pattern 1: Remove centering div and change 280 to Math Diagram
        # Matches: <div align="center"> whitespace ![280](url) whitespace </div>
        # Group 1: url
        pattern_div = r'<div align="center">\s*!\[280\]\((.*?)\)\s*</div>'
        content = re.sub(pattern_div, r'![Math Diagram](\1)', content)

        # Pattern 2: Change any remaining ![280](url) to ![Math Diagram](url)
        # Group 1: url
        pattern_raw = r'!\[280\]\((.*?)\)'
        content = re.sub(pattern_raw, r'![Math Diagram](\1)', content)
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"✅ EMERGENCY FIX APPLIED to {file_path}")
        print("   - Reverted to standard markdown: ![Math Diagram](url)")
        print("   - Removed HTML centering")

    except Exception as e:
        print(f"❌ Error processing file: {e}")

if __name__ == "__main__":
    emergency_fix(target_file)
