
import re
import os

target_file = "/Users/hulimofaqiu/Documents/obisidian笔记文件/math magic.md"
TARGET_WIDTH = "360"

def resize_images_in_url(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to find markdown images: ![alt](url)
        # Group 1: alt
        # Group 2: url
        image_pattern = r'(!\[[^\]]*\])\(([^)]+)\)'
        
        def resize_url(match):
            alt_part = match.group(1) # ![Math Diagram]
            url = match.group(2)      # https://...?width=600
            
            # Check if width param exists
            if "width=" in url:
                # Replace existing width
                new_url = re.sub(r'width=\d+', f'width={TARGET_WIDTH}', url)
            else:
                # Append width
                separator = "&" if "?" in url else "?"
                new_url = f"{url}{separator}width={TARGET_WIDTH}"
            
            return f"{alt_part}({new_url})"
            
        new_content = re.sub(image_pattern, resize_url, content)
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"✅ RESIZED IMAGES in {file_path}")
        print(f"   - Standardized all image URLs to width={TARGET_WIDTH}")

    except Exception as e:
        print(f"❌ Error processing file: {e}")

if __name__ == "__main__":
    resize_images_in_url(target_file)
