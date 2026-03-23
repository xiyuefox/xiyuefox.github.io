
import os
import shutil
import re
import unicodedata
import datetime
import subprocess
import hashlib
import json
import sys
from pathlib import Path

# ==============================================================================
# CONFIGURATION
# ==============================================================================
# Use environment variable if provided, else fallback to a default path
OBSIDIAN_VAULT_PATH = os.getenv("OBSIDIAN_VAULT_PATH", "/Users/hulimofaqiu/Documents/obisidian笔记文件")
BLOG_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HUGO_CONTENT_PATH = os.path.join(BLOG_ROOT, "blog/content/posts")
CACHE_FILE = os.path.join(BLOG_ROOT, "scripts/upload_cache.json")

# R2 Configuration
# R2 Configuration
R2_BUCKET = "xixi-image-bed"
R2_DOMAIN = "https://xixi-image-bed.jinxiyue07.workers.dev"
ENABLE_R2_UPLOAD = False # Enable R2 upload for images
STRIP_IMAGES = False # ENABLE IMAGES
CURATION_MODE = False # AUTO-CURATION: If True, only publishes top N articles
SMART_LIMIT = 1000 # Number of articles to publish in curation mode

# Smart Folders Mapping
FOLDER_MAP = {
    "Sparks": "sparks",   # 灵感
    "Notes": "notes",     # 笔记
    "Ideas": "ideas",     # 想法
    "Growth": "growth",   # 成长
    "Inbox": "inbox"      # Initial capture
}

# Try imports
try:
    from pypinyin import lazy_pinyin
except ImportError:
    lazy_pinyin = None

# ==============================================================================
# UTILITIES
# ==============================================================================

def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_cache(cache):
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=2)

def calculate_file_hash(filepath):
    """MD5 hash of file to check for changes."""
    hash_md5 = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def sanitize_title(title):
    """
    Sanitizes blog titles based on strict patterns:
    1. Number prefix: ^[\d\-_]+\s*
    2. Special chars: [\\/<>|"*?:]+
    3. Extra spaces: \s{2,}
    4. Trim edges: ^\s+|\s+$
    """
    if not title: return ""
    
    # 0. Normalize unicode
    title = unicodedata.normalize('NFKC', title)
    
    # 1. Number prefix (including U, V, -, _)
    title = re.sub(r'^[0-9UV\-_]+[\s.]*', '', title)
    
    # 2. Special chars
    title = re.sub(r'[\\/<>|"*?:]+', '', title)
    
    # 3. Extra spaces
    title = re.sub(r'\s{2,}', ' ', title)
    
    # 4. Trim edges
    return title.strip()

def sanitize_filename(filename):
    """Converts filename to URL-friendly string, applying title cleanup first."""
    name_without_ext = os.path.splitext(filename)[0]
    ext = os.path.splitext(filename)[1]
    
    # Apply strict title cleanup to filename source
    clean_base = sanitize_title(name_without_ext)
    if not clean_base: clean_base = name_without_ext # Fallback
    
    if lazy_pinyin:
        chars = lazy_pinyin(clean_base)
        clean_name = "-".join(chars)
    else:
        clean_name = clean_base

    clean_name = clean_name.lower()
    clean_name = re.sub(r'[^a-z0-9]+', '-', clean_name)
    clean_name = clean_name.strip('-')
    
    return f"{clean_name}{ext}"

# ==============================================================================
# R2 UPLOAD
# ==============================================================================

def upload_to_r2(local_path, remote_filename):
    """Uploads file to R2 using Wrangler CLI."""
    if not ENABLE_R2_UPLOAD:
        return True # Skip upload but pretend success so links are generated (or maybe False to keep local?)
        # User said "ignore images", so let's just return False so links aren't rewritten to broken URLs?
        # Or return True to generate the link even if not uploaded? 
        # "Sync and publish TEXT ONLY (ignore images for now)" -> likely means don't care about images.
        # Let's return False so it enters the "else" block in process_image_links if logic existed, 
        # but the current logic is: if upload_to_r2(..): cache[..] return link.
        # If I return False, it won't rewrite the link?
        # Let's check process_image_links logic.
    
    print(f"☁️ Uploading {remote_filename} to R2...")
    try:
        # Construct command: npx wrangler r2 object put <bucket>/<key> --file <path>
        key = f"{R2_BUCKET}/{remote_filename}"
        subprocess.run(
            ["npx", "wrangler", "r2", "object", "put", key, "--file", local_path],
            check=True,
            stdout=subprocess.DEVNULL, # Silence output
            stderr=subprocess.PIPE     # Capture errors
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Upload Failed: {e.stderr.decode()}")
        return False

# ==============================================================================
# SYNC LOGIC
# ==============================================================================

def process_image_links(content, file_dir_path, uploaded_cache, removal_log):
    """
    Finds ![[img]] or ![alt](img)
    If STRIP_IMAGES is True:
        Checks if file exists (validation)
        Removes the markdown syntax
        Logs the removal
    Else:
        Uploads to R2 and replaces link
    """
    
    # Regex for standard markdown images ![alt](path)
    # and Obsidian wikilink images ![[path]]
    
    def replacer(match):
        is_wikilink = match.group(0).startswith("![[")
        
        if is_wikilink:
            link_path = match.group(1).split('|')[0] # Handle ![[image.png|100]]
            alt_text = match.group(1).split('|')[-1] if '|' in match.group(1) else ""
        else:
            alt_text = match.group(1)
            link_path = match.group(2)
            
        # If already a URL
        if link_path.startswith("http"):
            if STRIP_IMAGES:
                removal_log.append(f"Removed External: {link_path}")
                return ""
            return match.group(0)

        # Resolve local path
        image_name = os.path.basename(link_path)
        
        # Look for image in 'Attachments' folder or relative
        # 1. Try relative to current file
        local_image_path = os.path.join(file_dir_path, link_path)
        
        # 2. Try default Attachments folder in Vault Root
        if not os.path.exists(local_image_path):
             local_image_path = os.path.join(OBSIDIAN_VAULT_PATH, "Attachments", image_name)
             
        # 3. Try same folder
        if not os.path.exists(local_image_path):
             local_image_path = os.path.join(file_dir_path, image_name)

        exists = os.path.exists(local_image_path)
        
        if STRIP_IMAGES:
            status = "Verified" if exists else "Missing"
            removal_log.append(f"Removed ({status}): {image_name}")
            return ""

        if exists:
            if ENABLE_R2_UPLOAD:
                # Calculate Hash
                img_hash = calculate_file_hash(local_image_path)
                
                # Check Cache
                if image_name in uploaded_cache and uploaded_cache[image_name]['hash'] == img_hash:
                    # Already uploaded
                    pass
                else:
                    # Need Upload
                    if upload_to_r2(local_image_path, image_name):
                        uploaded_cache[image_name] = {'hash': img_hash, 'date': str(datetime.datetime.now())}
                
                return f"![{alt_text}]({R2_DOMAIN}/{image_name})"
            else:
                # Copy to local static/images
                dest_dir = os.path.join(BLOG_ROOT, "blog/static/images")
                os.makedirs(dest_dir, exist_ok=True)
                shutil.copy2(local_image_path, os.path.join(dest_dir, image_name))
                return f"![{alt_text}](/images/{image_name})"
        else:
            print(f"⚠️ Image not found: {link_path}")
            return match.group(0) # Keep original if not found

    # Replace Wikilinks ![[...]]
    content = re.sub(r'!\[\[(.*?)\]\]', replacer, content)
    # Replace Md Links ![...](...)
    content = re.sub(r'!\[(.*?)\]\((.*?)\)', replacer, content)
    
    return content

def sync_vault():
    uploaded_cache = load_cache()
    synced_count = 0
    removal_log = []
    
    # Collection list for curation
    article_candidates = []

    # Step 1: Collect Candidates
    print("🔍 Scanning Vault for Smart Curation...")
    for root, dirs, files in os.walk(OBSIDIAN_VAULT_PATH):
        # Determine Category based on Folder name relative to Vault
        rel_path = os.path.relpath(root, OBSIDIAN_VAULT_PATH)
        path_parts = rel_path.split(os.sep)
        
        parent_folder = path_parts[0] if path_parts[0] != '.' else ""
        
        # Map to Hugo Category
        if parent_folder in FOLDER_MAP:
            hugo_category = FOLDER_MAP[parent_folder]
        else:
            hugo_category = "misc" # Default
            
        # Skip hidden folders, scripts, blog, templates, trash
        if parent_folder.startswith('.') or parent_folder.startswith('_'): continue
        if parent_folder in ["scripts", "blog", "Templates", ".Trash", "System"]: continue

        for filename in files:
            if filename.endswith(".md"):
                file_path = os.path.join(root, filename)
                
                # Fast read to determine eligibility before expensive processing
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                except Exception as e:
                    print(f"⚠️ Error reading {filename}: {e}")
                    continue

                # Override category for specific files
                current_category = hugo_category
                if filename == "如何给孩子早教（0-5岁）.md":
                    current_category = "notes"
                if filename == "CogniPlay匈牙利智力游戏Mondrian Blocks.md":
                    current_category = "notes"

                # Filter: Drafts
                is_draft = False
                if current_category == "inbox": is_draft = True
                if "status: draft" in content: is_draft = True
                # Check YAML draft (regex is robust enough for basic True/true)
                if re.search(r'^\s*draft:\s*true', content, re.MULTILINE | re.IGNORECASE): is_draft = True
                
                if is_draft:
                    # Double check if it's our target just to be sure, but we want to SKIP it if it is draft
                    # print(f"Skipping draft: {filename}")
                    continue # Skip drafts in curation mode

                # Filter: Length (Exclude very short notes)
                word_count = len(content)
                if CURATION_MODE and word_count < 200: continue 

                # Prepare candidate object
                candidate = {
                    "file_path": file_path,
                    "filename": filename,
                    "content": content,
                    "hugo_category": current_category,
                    "word_count": word_count,
                    "root": root
                }
                article_candidates.append(candidate)

    # Step 2: Smart Curation (Sort & Slice)
    if CURATION_MODE:
        print(f"🧠 Analyzing {len(article_candidates)} candidates based on length and quality...")
        # Sort by length descending
    # 3. Sort candidates
    article_candidates.sort(key=lambda x: x['word_count'], reverse=True) # Keep 'word_count' as it's defined above

    # 4. Selection Logic
    final_list = []
    
    # Blacklist filter (Quality Control)
    blacklist = ["外高桥", "租房", "看房"]
    
    # Force include specific targets
    target_filenames = [
        "零成本搭建个人图床！Cloudflare R2 完整实战教程.md",
        "如何给孩子早教（0-5岁）.md",
        "CogniPlay匈牙利智力游戏Mondrian Blocks.md",
        "蒙氏0-1岁Nido家庭方案自动化同步.md"
    ]
    
    for item in article_candidates:
        filename = os.path.basename(item['file_path'])
        
        # Check Blacklist
        if any(keyword in filename for keyword in blacklist):
            # print(f"🚫 Example excluded: {filename}")
            continue

        if filename in target_filenames:
            if item not in final_list:
                final_list.append(item)
                print(f"   --> Included specific target: {filename}")
            
    # Fill rest with top 9 longest
    current_count = len(final_list)
    for item in article_candidates:
        filename = os.path.basename(item['file_path'])
        
        if current_count >= 10: break
        
        # Check Blacklist again for main loop
        if any(keyword in filename for keyword in blacklist):
            continue
            
        if item not in final_list:
            final_list.append(item)
            current_count += 1

    print(f"✅ Selected {len(final_list)} articles for publication.")


    # 5. Clean & Copy
    # Clean target directory
    print(f"🧹 Use 'shutil.rmtree' to clean {HUGO_CONTENT_PATH}")
    if os.path.exists(HUGO_CONTENT_PATH):
        shutil.rmtree(HUGO_CONTENT_PATH)
    os.makedirs(HUGO_CONTENT_PATH, exist_ok=True)

    # Copy files
    for item in final_list:
        file_path = item['file_path'] # Use 'file_path'
        file_name = os.path.basename(file_path)
        
        # --- TITLE CLEANING & STANDARDIZATION ---
        # 1. Clean Title (remove extension first)
        clean_title = os.path.splitext(file_name)[0]
        # Remove leading numbers/dots (e.g. "01. Title" -> "Title")
        clean_title = re.sub(r'^[\d\s\.\-_]+', '', clean_title)
        # Remove Browser-Export Prefixes (e.g., "(从Canary打开)-", "e000-")
        clean_title = re.sub(r'^\(.*?\)-?', '', clean_title) # Remove leading (Content)
        clean_title = re.sub(r'^[eE]\d+-?', '', clean_title) # Remove e000- prefixes
        clean_title = re.sub(r'(从.*?打开)-?', '', clean_title) # Catch specific Chinese export patterns
        
        if "零成本搭建个人图床" in clean_title:
             clean_title = "零成本搭建个人图床：Cloudflare R2完整实战教程"
        
        # Determine Output Path
        
        # Determine Output Path
        hugo_category = item['hugo_category']
        out_dir = os.path.join(HUGO_CONTENT_PATH, hugo_category)
        os.makedirs(out_dir, exist_ok=True)
        
        # Sanitize Output Filename (using the existing function)
        new_filename = sanitize_filename(file_name)
        out_path = os.path.join(out_dir, new_filename)

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update Frontmatter
        # We inject the clean title and standard tags
        # Extract existing Frontmatter data
        existing_tags = []
        try:
            fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            if fm_match:
                fm_text = fm_match.group(1)
                for line in fm_text.split('\n'):
                    if line.strip().startswith('tags:'):
                        val = line.split(':', 1)[1].strip()
                        if val.startswith('['):
                            # Basic list parsing
                            existing_tags = [t.strip().strip("'\"") for t in val.strip("[]").split(",") if t.strip()]
                        else:
                            existing_tags = [t.strip() for t in val.split(",") if t.strip()]
        except Exception:
            pass
            
        final_tags = existing_tags if existing_tags else ["tech", "tutorial"]
        final_category = hugo_category
        
        # Special Case for Ralph Ammer
        if "ralph-ammer" in new_filename:
             final_category = "Inspiration"
             if not existing_tags: final_tags = ["drawing", "philosophy", "thinking"]

        frontmatter_update = f"""---
title: "{clean_title}"
date: {datetime.datetime.now().strftime('%Y-%m-%d')}
tags: {json.dumps(final_tags, ensure_ascii=False)}
categories: ["{final_category}"]
layout: "single" 
---
"""
        # Strip existing frontmatter for simplicity in this drastic overhaul
        content = re.sub(r'^---.*?---', '', content, flags=re.DOTALL).strip()
        final_content = frontmatter_update + "\n\n" + content

        # (Old logic removed for streamlined HN-style processing)
            
        # 2. Images (R2 or Strip)
        final_content = process_image_links(final_content, os.path.dirname(file_path), uploaded_cache, removal_log)
        
        # Write to Hugo
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        # Update cache occasionally
        if synced_count % 10 == 0:
            save_cache(uploaded_cache)
        
        print(f"✅ [{hugo_category}] {new_filename}")
        synced_count += 1

    save_cache(uploaded_cache)
    print(f"🎉 Sync Complete: {synced_count} files processed.")
    
    if removal_log:
        print("\n🗑️  Image Removal Report:")
        print(f"Total Removed: {len(removal_log)}")
        if len(removal_log) > 10:
            for item in removal_log[:5]: print(f"  - {item}")
            print(f"  ... and {len(removal_log)-10} more ...")
            for item in removal_log[-5:]: print(f"  - {item}")
        else:
            for item in removal_log: print(f"  - {item}")

if __name__ == "__main__":
    if lazy_pinyin is None:
        print("⚠️ Warning: 'pypinyin' not installed. Chinese filenames will not be romanized.")
    sync_vault()
