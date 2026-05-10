from bs4 import BeautifulSoup
import re

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Make Search and Cart unclickable
for sel in ['.header__icon--cart', '.header__icon--search', '#cart-icon-bubble', 'search-modal summary']:
    for el in soup.select(sel):
        if 'style' in el.attrs:
            if 'pointer-events: none' not in el['style']:
                el['style'] += ' pointer-events: none; cursor: default;'
        else:
            el['style'] = 'pointer-events: none; cursor: default;'

# Remove menu items
texts = ["SHOP BY BRAND", "DEAL & OFFERS", "DEALS AND OFFERS", "KNOWLEDGE HUB"]
for t in texts:
    for node in soup.find_all(string=re.compile(t, re.IGNORECASE)):
        li = node.find_parent('li')
        if li:
            li.decompose()

# Remove blog section
for node in soup.find_all(string=re.compile(r'Blog posts', re.IGNORECASE)):
    sec = node.find_parent('section')
    if sec:
        sec.decompose()

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Modified successfully")
