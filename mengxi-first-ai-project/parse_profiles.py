from bs4 import BeautifulSoup
import re

with open('designer-showcase/index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

cards = soup.select('.designer-card')
html_output = []

for card in cards:
    href = card.get('href')
    link = f"designer-showcase/{href}"
    label = card.select_one('.card-label').text if card.select_one('.card-label') else ""
    name = card.select_one('.designer-name').text if card.select_one('.designer-name') else ""
    role = card.select_one('.designer-role').text if card.select_one('.designer-role') else ""
    # Use a generic icon or try to map based on label
    icon = "👤"
    if "PIONEER" in label: icon = "⚙️"
    elif "THINKER" in label: icon = "🧠"
    elif "LEADER" in label: icon = "👑"
    elif "CREATOR" in label: icon = "✨"
    else: icon = "💡"
    
    tags = [tag.text for tag in card.select('.designer-tag')]
    tags_str = " · ".join(tags)
    
    # We will format this into a tg-card. But instead of putting all 23, we can create a grid.
    
    card_html = f'''                        <a href="{link}" class="tg-card tg-fade-in">
                            <div class="tg-card-header">
                                <span class="tg-card-icon">{icon}</span>
                                <span class="tg-card-source">{label.lower()}</span>
                            </div>
                            <h3 class="tg-card-title">{name}</h3>
                            <p class="tg-card-desc">{role}</p>
                            <div class="tg-card-footer">
                                <span class="tg-card-meta">{tags_str}</span>
                            </div>
                        </a>'''
    html_output.append(card_html)

print("\n".join(html_output))
