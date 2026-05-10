#!/usr/bin/env python3
"""
sync_footer.py
--------------
Reads components/footer.html and injects it between
  <!-- FOOTER_COMPONENT_START -->
  <!-- FOOTER_COMPONENT_END -->
markers in every HTML page across the site.

Replaces placeholder tokens:
  __ASSET_BASE__   → relative path prefix to root  (e.g. "../../" for depth-2 pages)
  __CONTACT_URL__  → relative path to pages/contact-us.html
  __HOME_URL__     → relative path to index.html

Run from the project root:
    python3 sync_footer.py
"""

import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
FOOTER_FILE = os.path.join(BASE, "components", "footer.html")

# All HTML pages to update (path relative to BASE, plus depth from root)
# depth 0 = root (index.html, collections.html)
# depth 1 = pages/ or collections/
# depth 2 = checkouts/ sub-pages, etc.
PAGES = [
    # (relative path,  depth)
    ("index.html",                                   0),
    ("collections.html",                             0),
    ("laser-printers-uae copy.html",                 0),
    ("pages/contact-us.html",                        1),
    ("pages/information.html",                       1),
    ("collections/pc-components.html",               1),
    ("collections/desktop-and-laptop.html",          1),
    ("collections/computer-accessories.html",        1),
    ("collections/monitors-and-projectors.html",     1),
    ("collections/gaming.html",                      1),
    ("collections/printers-and-scanners.html",       1),
    ("collections/games-and-softwares.html",         1),
    ("collections/servers-and-workstations.html",    1),
    ("collections/storage-and-devices.html",         1),
    ("collections/networking.html",                  1),
]

START_MARKER = "<!-- FOOTER_COMPONENT_START -->"
END_MARKER   = "<!-- FOOTER_COMPONENT_END -->"


def depth_prefix(depth: int) -> str:
    """Return the relative path prefix to reach the root from this depth."""
    return "../" * depth if depth > 0 else ""


def build_footer_html(depth: int, raw_footer: str) -> str:
    """Substitute placeholder tokens for a page at the given depth."""
    prefix = depth_prefix(depth)

    # Contact Us is always pages/contact-us.html from root
    contact_url = f"{prefix}pages/contact-us.html"
    home_url    = f"{prefix}index.html"

    html = raw_footer
    html = html.replace("__ASSET_BASE__",  prefix)
    html = html.replace("__CONTACT_URL__", contact_url)
    html = html.replace("__HOME_URL__",    home_url)
    return html


def inject_footer(filepath: str, depth: int, footer_html: str) -> bool:
    """
    Replace everything between START_MARKER and END_MARKER (inclusive)
    with the footer block.

    If markers don't exist, append them before </body> (first-time setup).
    Returns True if the file was modified.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    built = f"{START_MARKER}\n{footer_html}\n{END_MARKER}"

    if START_MARKER in content and END_MARKER in content:
        # Replace between markers
        pattern = re.compile(
            re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
            re.DOTALL,
        )
        new_content, count = pattern.subn(built, content)
        if count == 0:
            print(f"  WARNING: pattern sub failed in {filepath}")
            return False
    else:
        # First run — insert markers just before </body>
        if "</body>" not in content:
            print(f"  SKIP (no </body>): {filepath}")
            return False
        new_content = content.replace("</body>", f"\n{built}\n</body>", 1)

    if new_content == content:
        print(f"  Unchanged: {filepath}")
        return False

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True


def main():
    # Read the component
    with open(FOOTER_FILE, "r", encoding="utf-8") as f:
        raw_footer = f.read().strip()

    # Strip the HTML comment header from the component file (first comment block)
    raw_footer = re.sub(r"^<!--.*?-->\s*", "", raw_footer, flags=re.DOTALL).strip()

    updated = 0
    skipped = 0

    for rel_path, depth in PAGES:
        filepath = os.path.join(BASE, rel_path)
        if not os.path.exists(filepath):
            print(f"  SKIP (not found): {rel_path}")
            skipped += 1
            continue

        footer_html = build_footer_html(depth, raw_footer)
        changed = inject_footer(filepath, depth, footer_html)
        if changed:
            print(f"  Updated (depth={depth}): {rel_path}")
            updated += 1
        else:
            skipped += 1

    print(f"\nDone — {updated} file(s) updated, {skipped} unchanged/skipped.")


if __name__ == "__main__":
    main()
