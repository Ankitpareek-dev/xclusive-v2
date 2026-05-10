#!/usr/bin/env python3
"""
fix_footer_duplicates.py
------------------------
Removes the OLD Shopify footer section that existed before the component
was introduced.  The new footer (wrapped in FOOTER_COMPONENT_START/END
markers) is kept.

The old footer sits inside:
  <!-- BEGIN sections: footer-group -->
  ...old scrolling-promotion section + old footer div...
  <!-- END sections: footer-group -->

We strip the OLD footer div (and its surrounding wrapper) but leave the
scrolling-promotion section intact if present.

Run once from the project root:
    python3 fix_footer_duplicates.py
"""

import os, re

BASE = os.path.dirname(os.path.abspath(__file__))

PAGES = [
    "index.html",
    "collections.html",
    "laser-printers-uae copy.html",
    "pages/contact-us.html",
    "pages/information.html",
    "collections/pc-components.html",
    "collections/desktop-and-laptop.html",
    "collections/computer-accessories.html",
    "collections/monitors-and-projectors.html",
    "collections/gaming.html",
    "collections/printers-and-scanners.html",
    "collections/games-and-softwares.html",
    "collections/servers-and-workstations.html",
    "collections/storage-and-devices.html",
    "collections/networking.html",
]

START_MARKER = "<!-- FOOTER_COMPONENT_START -->"

# In collection pages the old footer div has id BEFORE class; in index it's the opposite.
# Match either variant.
OLD_FOOTER_PATTERNS = [
    '<div id="shopify-section-sections--17981471883486__footer"',
    '<div class="shopify-section shopify-section-group-footer-group shopify-section-footer"',
]


def remove_old_footer(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    marker_pos = content.find(START_MARKER)
    if marker_pos == -1:
        print(f"  SKIP (no marker): {filepath}")
        return

    found = False
    for OLD_FOOTER_START in OLD_FOOTER_PATTERNS:
        idx = 0
        while True:
            pos = content.find(OLD_FOOTER_START, idx)
            if pos == -1:
                break
            # Recalculate marker position each iteration
            marker_pos = content.find(START_MARKER)
            if pos < marker_pos:
                # This is the OLD one — find its matching </div> by counting depth
                search_pos = pos
                depth = 0
                end_pos = -1
                while search_pos < len(content):
                    open_tag  = content.find("<div", search_pos)
                    close_tag = content.find("</div>", search_pos)
                    if open_tag == -1 and close_tag == -1:
                        break
                    if open_tag != -1 and (close_tag == -1 or open_tag < close_tag):
                        depth += 1
                        search_pos = open_tag + 4
                    else:
                        depth -= 1
                        search_pos = close_tag + 6
                        if depth == 0:
                            end_pos = search_pos
                            break

                if end_pos == -1:
                    print(f"  WARNING: could not find end of old footer in {filepath}")
                    break

                # Also eat an optional trailing </link> and newlines
                tail = content[end_pos:]
                tail_stripped = re.sub(r"^\s*</link>\s*", "", tail)
                end_pos += (len(tail) - len(tail_stripped))

                content = content[:pos] + content[end_pos:]
                found = True
                break  # restart outer loop with fresh content
            else:
                idx = pos + len(OLD_FOOTER_START)


    if not found:
        print(f"  Unchanged (no old footer before marker): {filepath}")
        return

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Fixed: {filepath}")


for rel_path in PAGES:
    filepath = os.path.join(BASE, rel_path)
    if not os.path.exists(filepath):
        print(f"  SKIP (not found): {rel_path}")
        continue
    remove_old_footer(filepath)

print("\nDone.")
