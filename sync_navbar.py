#!/usr/bin/env python3
"""
Navbar Sync Script
==================
Syncs the navbar component from components/navbar.html into all HTML pages.

Usage: python3 sync_navbar.py

The script looks for these markers in each HTML file:
  <!-- NAVBAR_COMPONENT_START -->
  <!-- NAVBAR_COMPONENT_END -->

Everything between these markers is replaced with the content of components/navbar.html.
For pages in subdirectories, relative paths (cdn/..., collections/..., etc.) are
automatically adjusted with the correct prefix (../).
"""

import os
import re
import glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
COMPONENT_FILE = os.path.join(SCRIPT_DIR, 'components', 'navbar.html')

# Markers used to identify the navbar section in each page
START_MARKER = '<!-- NAVBAR_COMPONENT_START -->'
END_MARKER = '<!-- NAVBAR_COMPONENT_END -->'

# HTML files to sync (add new pages here as they are created)
# Use glob patterns relative to the script directory
PAGE_PATTERNS = [
    '*.html',
    'collections/*.html',
    'pages/*.html',
    'checkouts/*.html',
]


def get_navbar_html():
    """Read the navbar component HTML."""
    with open(COMPONENT_FILE, 'r', encoding='utf-8') as f:
        return f.read()


def adjust_paths_for_depth(html, depth):
    """Adjust relative paths for pages in subdirectories."""
    if depth == 0:
        return html
    
    prefix = '../' * depth
    
    # Fix asset paths: href="cdn/... and src="cdn/...
    html = re.sub(r'(href|src)="cdn/', rf'\1="{prefix}cdn/', html)
    
    # Fix srcset paths: cdn/ at the start of srcset entries
    html = re.sub(r'(srcset=")cdn/', rf'\1{prefix}cdn/', html)
    html = re.sub(r'(\s)cdn/shop/', rf'\1{prefix}cdn/shop/', html)
    
    # Fix page links
    html = re.sub(r'href="collections\.html"', f'href="{prefix}collections.html"', html)
    html = re.sub(r'href="collections/', f'href="{prefix}collections/', html)
    html = re.sub(r'href="index\.html"', f'href="{prefix}index.html"', html)
    html = re.sub(r'href="pages/', f'href="{prefix}pages/', html)
    
    return html


def get_depth(filepath):
    """Calculate directory depth relative to the site root."""
    rel_path = os.path.relpath(filepath, SCRIPT_DIR)
    parts = rel_path.split(os.sep)
    return len(parts) - 1  # -1 for the filename itself


def sync_page(filepath, navbar_html):
    """Replace the navbar section in a single HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if markers exist
    if START_MARKER not in content:
        return False, 'No start marker found'
    if END_MARKER not in content:
        return False, 'No end marker found'
    
    # Calculate path depth and adjust navbar HTML
    depth = get_depth(filepath)
    adjusted_html = adjust_paths_for_depth(navbar_html, depth)
    
    # Replace everything between markers using string operations (not regex,
    # because the navbar HTML contains \u escape sequences that break re.sub)
    start_idx = content.index(START_MARKER)
    end_idx = content.index(END_MARKER) + len(END_MARKER)
    
    # Find the indentation of the start marker
    line_start = content.rfind('\n', 0, start_idx) + 1
    indent = content[line_start:start_idx]
    
    new_content = (
        content[:start_idx]
        + START_MARKER + '\n'
        + adjusted_html + '\n'
        + indent + END_MARKER
        + content[end_idx:]
    )
    
    if new_content == content:
        return True, 'Already up to date'
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True, f'Updated (depth={depth})'


def main():
    print('Navbar Sync Script')
    print('=' * 40)
    
    # Read the component
    navbar_html = get_navbar_html()
    print(f'Read navbar component: {len(navbar_html)} bytes')
    print()
    
    # Find all HTML files
    synced = 0
    skipped = 0
    errors = 0
    
    for pattern in PAGE_PATTERNS:
        full_pattern = os.path.join(SCRIPT_DIR, pattern)
        for filepath in sorted(glob.glob(full_pattern)):
            rel_path = os.path.relpath(filepath, SCRIPT_DIR)
            
            # Skip backup files
            if filepath.endswith('.bak'):
                continue
            
            success, message = sync_page(filepath, navbar_html)
            if success:
                if 'Updated' in message:
                    print(f'  ✅ {rel_path}: {message}')
                    synced += 1
                else:
                    print(f'  ⏭  {rel_path}: {message}')
                    skipped += 1
            else:
                print(f'  ⚠️  {rel_path}: {message}')
                errors += 1
    
    print()
    print(f'Summary: {synced} updated, {skipped} skipped, {errors} without markers')
    print()
    if errors > 0:
        print('To add navbar support to a page, add these markers where the navbar should go:')
        print(f'  {START_MARKER}')
        print(f'  {END_MARKER}')


if __name__ == '__main__':
    main()
