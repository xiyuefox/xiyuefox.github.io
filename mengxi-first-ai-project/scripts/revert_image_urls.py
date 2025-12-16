
import re

target_file = "/Users/hulimofaqiu/Documents/obisidian笔记文件/如何给孩子早教（0-5岁）.md"

def revert_urls(content):
    # Regex to find markdown images with http urls
    # ![alt](http.../filename.png) -> ![[filename.png]]
    
    def replacer(match):
        url = match.group(2)
        filename = url.split('/')[-1]
        return f"![[{filename}]]"

    # Match ![alt](http...)
    new_content = re.sub(r'!\[(.*?)\]\((https?://.*?)\)', replacer, content)
    return new_content

try:
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = revert_urls(content)
    
    if content != new_content:
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated image links to wikilinks.")
    else:
        print("No changes needed.")

except Exception as e:
    print(f"Error: {e}")
