
import re
import os

target_file = "/Users/hulimofaqiu/Documents/obisidian笔记文件/math magic.md"

def standardize_images(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Regex to find standard markdown images: ![alt](url)
        # We replace any alt text with '260'
        # Pattern: ! [ anything ] ( url )
        # We capture the url in group 2.
        
        # Note: We must be careful not to capture nested parenthesis in URL if any, 
        # but standard markdown usually handles balanced ones or simple urls.
        # This regex assumes simple URLs.
        
        new_content = re.sub(r'!\[(.*?)\]\((.*?)\)', r'![260](\2)', content)
        
        # Also handle Obsidian wikilinks if requested? 
        # User prompt said "Markdown syntax", and example is standard. 
        # I'll mostly focus on standard markdown as seen in the cat output.
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"✅ Successfully standardized images in {file_path}")
        
    except Exception as e:
        print(f"❌ Error processing file: {e}")

if __name__ == "__main__":
    standardize_images(target_file)
