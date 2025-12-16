
import os

VAULT_PATH = "/Users/hulimofaqiu/Documents/obisidian笔记文件"

def list_structure(startpath):
    print(f"📂 Analyzing Vault: {startpath}")
    if not os.path.exists(startpath):
        print("❌ Path not found!")
        return

    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}📁 {os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        # Limit file listing to first 5 per folder to avoid spam
        for i, f in enumerate(files):
            if i < 3:
                print(f"{subindent}📄 {f}")
            elif i == 3:
                print(f"{subindent}... (and {len(files)-3} more)")

if __name__ == "__main__":
    list_structure(VAULT_PATH)
