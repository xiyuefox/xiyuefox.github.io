
import re
import os

target_file = "/Users/hulimofaqiu/Documents/obisidian笔记文件/math magic.md"

def optimize_images_robust(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Step 1: Normalize - Remove existing centering divs around images to avoid double wrapping
        # Matches: <div align="center"> whitespace? image whitespace? </div>
        # We replace with just the image.
        # Note: We capture text groups 2 (alt) and 3 (url) of the image to reconstruct it clean.
        
        # Regex explanation:
        # <div align="center">\s*  -> opening tag and optional whitespace
        # !\[(.*?)\]\((.*?)\)      -> The image markdown (Group 1: alt, Group 2: url)
        # \s*</div>                -> closing tag and optional whitespace
        
        clean_pattern = r'<div align="center">\s*!\[(.*?)\]\((.*?)\)\s*</div>'
        
        # We replace it with just ![alt](url) to strip the div
        # BUT we can just proceed to Step 2 if we handle the replacement logic well.
        
        # Actually, let's do a complete replacement pass.
        # We want to find ANY image, whether wrapped or not, and output a wrapped image with alt=280.
        
        # To do this safely, let's first "unwrap" any wrapped images.
        content = re.sub(clean_pattern, r'![\1](\2)', content, flags=re.DOTALL)
        
        # Step 2: Now all images are raw ![alt](url). 
        # We find them and wrap them with alt=280.
        
        image_pattern = r'!\[(.*?)\]\((.*?)\)'
        
        def wrap_replacement(match):
            url = match.group(2)
            # URL might need cleaning if it captured extra spaces? Usually strict regex is fine.
            return f'<div align="center">\n![280]({url})\n</div>'
            
        new_content = re.sub(image_pattern, wrap_replacement, content)
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"✅ Successfully robustly processed {file_path}")
        print("   - Normalized and re-wrapped images")
        print("   - Set width to 280")

    except Exception as e:
        print(f"❌ Error processing file: {e}")

if __name__ == "__main__":
    optimize_images_robust(target_file)
