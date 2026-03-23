
import re
import os

target_file = "/Users/hulimofaqiu/Documents/obisidian笔记文件/math magic.md"

def simplify_images(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Step 1: Unwrap images from div tags
        # Pattern: <div align="center">\s*(!\[.*?\]\(.*?\))\s*</div>
        # We capture the full image markdown in group 1
        unwrap_pattern = r'<div align="center">\s*(!\[.*?\]\([^)]+\))\s*</div>'
        content = re.sub(unwrap_pattern, r'\1', content, flags=re.DOTALL)

        # Step 2: Ensure proper Alt Text
        # Find any remaining images (unwrapped or originally distinct) and force Alt Text to "Math Diagram"
        
        # Regex: !\[([^\]]*)\]\(([^)]+)\)
        # Group 1: Old Alt Text
        # Group 2: URL
        image_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
        
        def normalize_alt(match):
            url = match.group(2)
            return f'![Math Diagram]({url})'
            
        content = re.sub(image_pattern, normalize_alt, content)
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"✅ SIMPLIFIED FIX APPLIED to {file_path}")
        print("   - Removed all HTML centering divs")
        print("   - Standardized to pure Markdown: ![Math Diagram](url)")

    except Exception as e:
        print(f"❌ Error processing file: {e}")

if __name__ == "__main__":
    simplify_images(target_file)
