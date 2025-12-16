
import re
import os

target_file = "/Users/hulimofaqiu/Documents/obisidian笔记文件/math magic.md"

def standardize_and_center(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Step 1: Normalize - Remove existing centering divs to ensure clean state
        # Detect: <div align="center">\s*![...](...)\s*</div>
        # Replace with: ![...](...)
        
        # This regex matches the div wrapper and captures the image part
        # Group 1: The full image markdown ![alt](url)
        unwrap_pattern = r'<div align="center">\s*(!\[.*?\]\([^)]+\))\s*</div>'
        content = re.sub(unwrap_pattern, r'\1', content, flags=re.DOTALL)

        # Step 2: Apply Formatting
        # Find all images: ![alt](url)
        # Replace with: <div align="center">\n![Math Diagram](url)\n</div>
        
        # Regex to find image: !\[([^\]]*)\]\(([^)]+)\)
        # Group 1: Current Alt Text (ignored in replacement, replaced by 'Math Diagram')
        # Group 2: URL (preserved)
        
        image_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
        
        def wrapper(match):
            url = match.group(2)
            # Construct the new block
            return f'<div align="center">\n![Math Diagram]({url})\n</div>'
        
        new_content = re.sub(image_pattern, wrapper, content)
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"✅ Successfully processed {file_path}")
        print("   - Unwrapped existing divs (if any)")
        print("   - Updated Alt Text to 'Math Diagram'")
        print("   - Wrapped images in <div align='center'>")

    except Exception as e:
        print(f"❌ Error processing file: {e}")

if __name__ == "__main__":
    standardize_and_center(target_file)
