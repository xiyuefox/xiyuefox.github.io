
import os
import re
import shutil
import datetime

# Configuration matching your environment
OBSIDIAN_VAULT_PATH = "/Users/hulimofaqiu/Documents/obisidian笔记文件"

def get_target_files():
    """Recovers the exact list of 10 files used in the curation logic"""
    article_candidates = []
    
    for root, dirs, files in os.walk(OBSIDIAN_VAULT_PATH):
        rel_path = os.path.relpath(root, OBSIDIAN_VAULT_PATH)
        path_parts = rel_path.split(os.sep)
        parent_folder = path_parts[0] if path_parts[0] != '.' else ""
        
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

                if parent_folder == "Inbox": continue
                if "status: draft" in content: continue
                if re.search(r'^draft:\s*true', content, re.MULTILINE | re.IGNORECASE): continue
                
                word_count = len(content)
                if word_count < 200: continue
                
                article_candidates.append({"path": file_path, "count": word_count})

    article_candidates.sort(key=lambda x: x['count'], reverse=True)
    return [item['path'] for item in article_candidates[:10]]

def optimize_content(content):
    """Applies content optimization rules"""
    original = content
    
    # 1. Heading Standardization
    # Remove numeric prefixes (e.g., "## 1. Introduction" -> "## Introduction")
    content = re.sub(r'^(#+)\s*(\d+\.|[a-zA-Z]\.)\s+', r'\1 ', content, flags=re.MULTILINE)
    
    # 2. Layout & Spacing
    # Ensure empty line BEFORE headers (common Markdown issue)
    content = re.sub(r'([^\n])\n^(#+ )', r'\1\n\n\2', content, flags=re.MULTILINE)
    
    # Ensure empty line BEFORE code blocks
    content = re.sub(r'([^\n])\n^```', r'\1\n\n```', content, flags=re.MULTILINE)
    
    # Ensure empty line AFTER code blocks
    # (Regex matches ``` followed by newline, then non-newline/non-empty)
    content = re.sub(r'(^```.*$)\n([^\n])', r'\1\n\n\2', content, flags=re.MULTILINE)
    
    # 3. List Standardization (Convert * to - for unordered lists, consistent)
    # Only at start of line
    content = re.sub(r'^\s*\*\s+', '- ', content, flags=re.MULTILINE)
    
    # 4. Whitespace Cleanup
    # Reduce 3+ newlines to 2
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content

def main():
    targets = get_target_files()
    report = []
    
    print(f"🚀 Starting Automated Content Optimization on {len(targets)} files...\n")
    
    for file_path in targets:
        filename = os.path.basename(file_path)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                raw = f.read()
            
            optimized = optimize_content(raw)
            
            if raw != optimized:
                # Backup
                backup_path = file_path + ".bak"
                shutil.copy2(file_path, backup_path)
                
                # Write
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(optimized)
                
                status = "✅ OPTIMIZED"
                details = "Headers cleaned, spacing fixed, noise reduced."
            else:
                status = "✨ SKIP"
                details = "Already optimally formatted."
                
        except Exception as e:
            status = "❌ ERROR"
            details = str(e)
            
        print(f"{status.ljust(12)} : {filename}")
        report.append(f"| {filename} | {status} | {details} |")

    # Generate Report File
    report_content = "# Content Optimization Report\n"
    report_content += f"**Date**: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
    report_content += "| File | Status | Actions |\n|---|---|---|\n"
    report_content += "\n".join(report)
    
    with open("OPTIMIZATION_REPORT.md", "w") as f:
        f.write(report_content)
        
    print("\n📄 Report generated: OPTIMIZATION_REPORT.md")

if __name__ == "__main__":
    main()
