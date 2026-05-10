import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

allowed_local_pages = [
    'pages/information.html',
    'pages/contact-us.html',
    'collections.html',
    'collections/laser-printers-uae.html',
    'index.html',
    '#'
]

# First, replace the contact link pointing to external site to local page
content = content.replace('href="https://atomoffice.com/pages/contact-us"', 'href="pages/contact-us.html"')
content = content.replace("href='https://atomoffice.com/pages/contact-us'", "href='pages/contact-us.html'")
content = content.replace('href="https://atomoffice.com/contact#ContactFooter"', 'href="pages/contact-us.html"')

# We also should protect links like #MainContent
# Function to process <a> tags
def repl_a_tag(match):
    full_tag = match.group(0)
    
    # Extract href
    href_match = re.search(r'href=[\'"]([^\'"]*)[\'"]', full_tag)
    if not href_match:
        return full_tag
        
    href_val = href_match.group(1)
    
    # If the href is an anchor link, keep it
    if href_val.startswith('#'):
        return full_tag
        
    # Check if the href matches one of the allowed pages
    # Or ends with them
    is_allowed = False
    for allowed in allowed_local_pages:
        if href_val.endswith(allowed) or allowed in href_val:
            is_allowed = True
            break
            
    if is_allowed:
        return full_tag
        
    # Otherwise, replace the href with #
    new_tag = re.sub(r'href=[\'"][^\'"]*[\'"]', 'href="#"', full_tag)
    return new_tag

new_content = re.sub(r'<a\s+[^>]*>', repl_a_tag, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating links in index.html")
