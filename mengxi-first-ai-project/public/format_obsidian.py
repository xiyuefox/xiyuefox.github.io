import os
import re
import yaml
import datetime

OBSIDIAN_VAULT = "/Users/hulimofaqiu/Documents/obisidian笔记文件/"

# Prefix filters for ignores
IGNORE_PREFIXES = ['00', '01', 'untitled', '未命名', 'drawing', '!pasted', 'ralph']

def is_mature_article(filename, content, existing_frontmatter):
    fname_lower = filename.lower()
    
    # Exclude system and draft names
    if any(fname_lower.startswith(prefix) for prefix in IGNORE_PREFIXES):
        return False
        
    if 'excalidraw' in fname_lower:
        return False
        
    # Exclude specific tags
    content_lower = content.lower()
    if '#draft' in content_lower or '#private' in content_lower:
        return False
        
    tags = existing_frontmatter.get('tags', [])
    if isinstance(tags, str):
        tags = [tags]
    if tags is None:
        tags = []
    
    tag_strs = [str(t).lower() for t in tags]
    if 'draft' in tag_strs or 'private' in tag_strs:
        return False

    # Automatic inclusion trigger
    if '#publish' in content_lower or str(existing_frontmatter.get('publish', '')).lower() == 'true':
        return True
        
    # Length filter: Must be substantial enough (e.g., > 1200 chars)
    if len(content) < 1200:
        return False
        
    return True

def process_file(filepath):
    filename = os.path.basename(filepath)
    if not filename.endswith('.md'):
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse existing frontmatter
    # YAML frontmatter is usually between --- and --- at the very top
    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    existing_frontmatter = {}
    body_content = content

    if match:
        yaml_str = match.group(1)
        body_content = match.group(2)
        try:
            parsed = yaml.safe_load(yaml_str)
            if isinstance(parsed, dict):
                existing_frontmatter = parsed
        except yaml.YAMLError:
            pass # fallback to empty if malformed

    # Determine mature
    mature = is_mature_article(filename, body_content, existing_frontmatter)
    
    # Process old tags (sometimes they are a string, sometimes a list)
    tags = existing_frontmatter.get('tags', [])
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(',') if t.strip()]
    if tags is None:
        tags = []
        
    # Build new frontmatter
    new_frontmatter = {}
    
    # title
    title = existing_frontmatter.get('title')
    if not title:
        title = filename[:-3] # remove .md
    new_frontmatter['title'] = title

    # author
    new_frontmatter['author'] = existing_frontmatter.get('author', 'Mengxi')

    # date
    date = existing_frontmatter.get('date')
    if not date:
        # File creation time (or modification time)
        stat = os.stat(filepath)
        dt = datetime.datetime.fromtimestamp(stat.st_mtime)
        date = dt.strftime('%Y-%m-%d')
    elif isinstance(date, datetime.date):
        date = date.strftime('%Y-%m-%d')
    new_frontmatter['date'] = str(date)
    
    # version
    new_frontmatter['version'] = existing_frontmatter.get('version', '1.0')
    
    # Determine publish / draft values
    publish_val = existing_frontmatter.get('publish')
    if publish_val is None:
        publish_val = mature
    else:
        publish_val = str(publish_val).lower() == 'true'

    draft_val = existing_frontmatter.get('draft')
    if draft_val is None:
        draft_val = not publish_val
    else:
        draft_val = str(draft_val).lower() == 'true'
        
    # Force consistency between draft and publish if they weren't explicitly over-ridden
    # To keep things clean, if it's considered mature, we ensure draft is false and publish is true unless overridden
    new_frontmatter['draft'] = draft_val
    new_frontmatter['publish'] = publish_val

    # tags
    if tags:
        new_frontmatter['tags'] = tags

    # Keep other existing properties to not lose data
    for k, v in existing_frontmatter.items():
        if k not in new_frontmatter and v is not None:
            new_frontmatter[k] = v

    # Write back
    new_yaml = yaml.dump(new_frontmatter, allow_unicode=True, default_flow_style=False, sort_keys=False)
    
    new_file_content = f"---\n{new_yaml}---\n{body_content.lstrip()}"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_file_content)

    return publish_val

def main():
    count = 0
    mature_count = 0
    for root, dirs, files in os.walk(OBSIDIAN_VAULT):
        # Optional: ignore some folders
        if '.obsidian' in root or '.git' in root or '.trash' in root:
            continue
            
        for f in files:
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                try:
                    is_published = process_file(filepath)
                    count += 1
                    if is_published:
                        mature_count += 1
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")
                            
    print(f"Processed {count} files. Identified {mature_count} mature articles for publishing.")

if __name__ == '__main__':
    main()
