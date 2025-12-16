
import os

target_file = "/Users/hulimofaqiu/Documents/obisidian笔记文件/数学思维设计研发资料整理.md"

if not os.path.exists(target_file):
    print(f"Error: File not found: {target_file}")
    exit(1)

with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Check if frontmatter exists
if content.startswith("---"):
    # Insert draft: true into existing frontmatter
    # Find the end of frontmatter
    end_idx = content.find("---", 3)
    if end_idx != -1:
        # Check if draft is already there
        if "draft:" in content[:end_idx]:
             print("Draft status already present.")
        else:
             new_content = content[:3] + "\ndraft: true" + content[3:]
             with open(target_file, 'w', encoding='utf-8') as f:
                 f.write(new_content)
             print("✅ Added 'draft: true' to existing frontmatter.")
else:
    # Prepend new frontmatter
    new_content = "---\ndraft: true\n---\n\n" + content
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("✅ Created frontmatter with 'draft: true'.")
