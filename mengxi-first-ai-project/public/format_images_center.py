
import re
import os

target_file = "/Users/hulimofaqiu/Documents/obisidian笔记文件/math magic.md"

def center_and_resize_images(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to match markdown images: ![alt](url)
        # matches ! [ anything ] ( anything )
        # We capture the URL in group 2
        pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
        
        # Function to ensure we don't wrap already wrapped images if possible,
        # but simpler approach is usually requested. 
        # However, looking at the previous step, we had ![260](url). 
        # We will replace ANY markdown image found.
        
        # Replacement pattern:
        # <div align="center">
        # ![280](url)
        # </div>
        
        def replacement(match):
            url = match.group(2)
            # check if it's strictly a standard image link we want to touch
            return f'<div align="center">\n![280]({url})\n</div>'

        # We need to be careful not to match images inside the HTML tags we just added if we run this multiple times? 
        # But for this task, we assume a single pass or we regex check for existing divs.
        # A simple way is to find images that are NOT preceded by <div align="center">.
        # But a standard re.sub is sufficient for the user's specific request "Perform...".
        
        new_content = re.sub(pattern, replacement, content)
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"✅ Successfully processed {file_path}")
        print("   - Wrapped images in <div align='center'>")
        print("   - Updated alt text to '280'")

    except Exception as e:
        print(f"❌ Error processing file: {e}")

if __name__ == "__main__":
    center_and_resize_images(target_file)
