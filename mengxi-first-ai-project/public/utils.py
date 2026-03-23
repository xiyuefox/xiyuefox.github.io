#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import yaml

def append_frontmatter(file_path, metadata_dict):
    """
    Injects or merges YAML frontmatter into a Markdown file.
    If frontmatter exists, updates with metadata_dict.
    Otherwise creates new one.
    """
    if not os.path.exists(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        content = ""
    else:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
    # Match frontmatter using regex
    match = re.match(r'^---\s*\n(.*?)\n---(\s*\n|$)', content, re.DOTALL)
    if match:
        yaml_content = match.group(1)
        body = content[match.end():]
        try:
            existing_meta = yaml.safe_load(yaml_content) or {}
            existing_meta.update(metadata_dict)
            new_yaml = yaml.dump(existing_meta, allow_unicode=True, default_flow_style=False).strip()
            content = f"---\n{new_yaml}\n---\n{body}"
        except Exception as e:
            # Fallback for parsing errors
            print(f"⚠️ 解析 frontmatter 出错 ({file_path}): {e}")
            for k, v in metadata_dict.items():
                if f"{k}:" not in yaml_content:
                    yaml_content += f"\n{k}: {v}"
            content = f"---\n{yaml_content}\n---\n{body}"
    else:
        new_yaml = yaml.dump(metadata_dict, allow_unicode=True, default_flow_style=False).strip()
        content = f"---\n{new_yaml}\n---\n\n" + content

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ YAML frontmatter 已更新: {file_path}")
