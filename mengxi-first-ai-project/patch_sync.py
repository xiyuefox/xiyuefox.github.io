import re

with open('scripts/sync_obsidian.py', 'r') as f:
    content = f.read()

# Add import yaml if not there
if 'import yaml' not in content:
    content = content.replace('import re', 'import re\nimport yaml')

new_func = '''def process_vault_article(filepath):
    """Process a new article from the Obsidian vault."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(filepath)
    if not is_valid_article(filename, content):
        return None

    # Parse YAML frontmatter
    match = re.match(r'^---\\n(.*?)\\n---\\n(.*)', content, re.DOTALL)
    existing_frontmatter = {}
    body_content = content
    
    if match:
        yaml_str = match.group(1)
        body_content = match.group(2)
        try:
            parsed = yaml.safe_load(yaml_str)
            if isinstance(parsed, dict):
                existing_frontmatter = parsed
        except Exception:
            pass

    title = existing_frontmatter.get('title')
    if not title:
        title = os.path.splitext(filename)[0]

    slug = sanitize_slug(title)
    if not slug:
        slug = sanitize_slug(filename)
        
    mtime = os.path.getmtime(filepath)
    date_str = str(existing_frontmatter.get('date', ''))
    if not date_str or date_str == 'None':
        date_obj = datetime.datetime.fromtimestamp(mtime)
        date_str = date_obj.strftime("%Y-%m-%d")
        
    month_str = date_str[:7] if len(date_str) >= 7 else "2026-03"
    
    # Extract tags
    fm_tags = existing_frontmatter.get('tags', [])
    if isinstance(fm_tags, str):
        fm_tags = [t.strip() for t in fm_tags.split(',')]
    if fm_tags is None: fm_tags = []
    
    tags = [str(t) for t in fm_tags if str(t).lower() not in ['publish', 'draft']]
    main_tag = tags[0] if tags else "obsidian"
    
    desc = "A note from Obsidian."
    paragraphs = body_content.split('\\n\\n')
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith('#') and not p.startswith('!') and not p.startswith('['):
            clean_p = re.sub(r'[*_`~]+', '', p)
            desc = clean_p[:80] + '...' if len(clean_p) > 80 else clean_p
            break

    images = re.findall(r'!\[\[(.*?)\]\]', body_content)
    for img in images:
        img_name = img.split('|')[0]
        img_source = None
        for root, _, files in os.walk(OBSIDIAN_VAULT):
            if img_name in files:
                img_source = os.path.join(root, img_name)
                break
        
        if img_source:
            safe_img_name = urllib.parse.quote(img_name)
            dest_path = os.path.join(IMAGES_DIR, img_name)
            import shutil
            shutil.copy2(img_source, dest_path)
            body_content = body_content.replace(f'![[{img}]]', f'![{img_name}](/images/obsidian/{safe_img_name})')
            
    final_content = f"""---
title: "{title.replace('"', '')}"
date: {date_str}
tags: [{', '.join(tags)}]
category: "obsidian"
badge: "{main_tag}"
---

{body_content.lstrip()}
"""
    return {'''

pattern = re.compile(r'def process_vault_article\(filepath\):.*?return \{', re.DOTALL)
content = re.sub(pattern, new_func, content)

with open('scripts/sync_obsidian.py', 'w') as f:
    f.write(content)

