import re

with open('designer-showcase/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Basic regex or string parsing to get the cards
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')
cards = soup.select('.designer-card')

featured = []
others = []

count = 0
for card in cards:
    href = card.get('href')
    link = f"designer-showcase/{href}"
    label = card.select_one('.card-label').text if card.select_one('.card-label') else ""
    name = card.select_one('.designer-name').text if card.select_one('.designer-name') else ""
    role = card.select_one('.designer-role').text if card.select_one('.designer-role') else ""
    
    icon = "👤"
    if "PIONEER" in label: icon = "⚙️"
    elif "THINKER" in label: icon = "🧠"
    elif "LEADER" in label: icon = "👑"
    elif "CREATOR" in label: icon = "✨"
    else: icon = "💡"
    
    tags = [tag.text for tag in card.select('.designer-tag')]
    tags_str = " · ".join(tags)
    
    # We want a few featured cards that are always visible
    grid_attr = ' style="grid-column: 1 / -1;"' if count < 2 else ''
    
    card_html = f'''                        <a href="{link}" class="tg-card tg-fade-in"{grid_attr}>
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
    if count < 6:
        featured.append(card_html)
    else:
        others.append(card_html)
    count += 1

output_html = "                    <div class=\"tg-grid\">\n"
output_html += "\n".join(featured)
output_html += "\n                    </div>\n"

output_html += '''
                    <details class="tg-profiles-details" style="margin-top: 2rem; border-top: 1px solid var(--tg-border-color); padding-top: 1rem;">
                        <summary style="cursor: pointer; font-family: var(--tg-font-mono); font-size: 0.8rem; color: var(--tg-text-muted); text-transform: uppercase; letter-spacing: 0.1em; display: inline-flex; align-items: center; gap: 0.5rem; user-select: none;">
                            <span class="tg-details-chev">▼</span> 查看全部存档档案 (Show All Profiles)
                        </summary>
                        <div class="tg-grid" style="margin-top: 1.5rem;">
'''

output_html += "\n".join(others)
output_html += "\n                        </div>\n                    </details>"

with open('profiles_generated.html', 'w', encoding='utf-8') as f:
    f.write(output_html)
