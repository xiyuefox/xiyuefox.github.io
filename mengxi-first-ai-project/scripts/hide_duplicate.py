
import os

target_file = "/Users/hulimofaqiu/Documents/obisidian笔记文件/education- prompt.md"

def hide_file(file_path):
    # Obsidian frontmatter format:
    # ---
    # key: value
    # ---
    
    # We want to check if draft: true exists, if not add it.
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        has_frontmatter = lines[0].strip() == "---"
        new_lines = []
        
        if has_frontmatter:
            # Insert draft: true after the first ---
            new_lines.append(lines[0])
            new_lines.append("draft: true\n")
            new_lines.extend(lines[1:])
        else:
            # Create frontmatter
            new_lines.append("---\n")
            new_lines.append("draft: true\n")
            new_lines.append("---\n")
            new_lines.extend(lines)
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
            
        print(f"✅ Hided file: {file_path}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    hide_file(target_file)
