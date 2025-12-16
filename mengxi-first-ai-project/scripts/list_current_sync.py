
import os
import re

OBSIDIAN_VAULT_PATH = "/Users/hulimofaqiu/Documents/obisidian笔记文件"
FOLDER_MAP = {
    "Sparks": "sparks",
    "Notes": "notes",
    "Ideas": "ideas",
    "Growth": "growth",
    "Inbox": "inbox"
}

def scan_and_list():
    article_candidates = []
    
    # 1. Collect
    for root, dirs, files in os.walk(OBSIDIAN_VAULT_PATH):
        rel_path = os.path.relpath(root, OBSIDIAN_VAULT_PATH)
        path_parts = rel_path.split(os.sep)
        parent_folder = path_parts[0] if path_parts[0] != '.' else ""
        
        # Filters from sync script
        if parent_folder.startswith('.') or parent_folder.startswith('_'): continue
        if parent_folder in ["scripts", "blog", "Templates", ".Trash", "System"]: continue

        for filename in files:
            if filename.endswith(".md"):
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                except:
                    continue

                # Draft check
                if parent_folder == "Inbox": continue # mapped to inbox -> draft
                if "status: draft" in content: continue
                if re.search(r'^draft:\s*true', content, re.MULTILINE | re.IGNORECASE): continue
                
                word_count = len(content)
                if word_count < 200: continue

                article_candidates.append({
                    "path": file_path,
                    "count": word_count
                })

    # 2. Sort & Slice
    article_candidates.sort(key=lambda x: x['count'], reverse=True)
    selected = article_candidates[:10]

    # 3. Output
    print("Here are the 10 Obsidian source files currently synced to your blog (Curation Mode Active):")
    print("-" * 60)
    for item in selected:
        print(item['path'])
    print("-" * 60)

if __name__ == "__main__":
    scan_and_list()
