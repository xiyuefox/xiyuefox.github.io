import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('profiles_generated.html', 'r', encoding='utf-8') as f:
    profiles_html = f.read()

# find the <section id="profiles"> and replace its inner html
pattern = re.compile(r'(<section id="profiles" class="tg-section">\s*<h2 class="tg-section-title">人物档案</h2>\s*)<div class="tg-grid">.*?(?=</section>)', re.DOTALL)

match = pattern.search(html)
if match:
    new_html = html[:match.end(1)] + profiles_html + "\n                " + html[match.end():]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Successfully replaced profiles section in index.html")
else:
    print("Could not find the profiles section")
