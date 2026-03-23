
import os

hide_file = "/Users/hulimofaqiu/Documents/obisidian笔记文件/05_String Manipulation for Python Coders 1.md"
keep_file = "/Users/hulimofaqiu/Documents/obisidian笔记文件/05_String Manipulation for Python Coders.md"

def set_draft_status(file_path, is_draft):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        has_frontmatter = lines[0].strip() == "---"
        new_lines = []
        found_draft = False
        
        if has_frontmatter:
            # We are inside frontmatter processing
            in_frontmatter = True
            for i, line in enumerate(lines):
                if i == 0:
                    new_lines.append(line)
                    continue
                
                if line.strip() == "---":
                    in_frontmatter = False
                    # Before closing, if we haven't found draft and we need to set it, add it
                    if not found_draft:
                        new_lines.append(f"draft: {str(is_draft).lower()}\n")
                    new_lines.append(line)
                    # Add the rest of the file
                    new_lines.extend(lines[i+1:])
                    break
                
                if line.strip().startswith("draft:"):
                    new_lines.append(f"draft: {str(is_draft).lower()}\n")
                    found_draft = True
                else:
                    new_lines.append(line)
        else:
            # Create frontmatter
            new_lines.append("---\n")
            new_lines.append(f"draft: {str(is_draft).lower()}\n")
            new_lines.append("---\n")
            new_lines.extend(lines)
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
            
        action = "Hided" if is_draft else "Activated"
        print(f"✅ {action}: {os.path.basename(file_path)}")
        
    except Exception as e:
        print(f"❌ Error processing {os.path.basename(file_path)}: {e}")

if __name__ == "__main__":
    if os.path.exists(hide_file):
        set_draft_status(hide_file, True)
    else:
        print(f"⚠️ File not found: {hide_file}")
        
    if os.path.exists(keep_file):
        set_draft_status(keep_file, False)
    else:
        print(f"⚠️ File not found: {keep_file}")
