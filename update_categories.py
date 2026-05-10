#!/usr/bin/env python3
"""Update hero banner, description and filter dropdowns for all 10 category pages."""

import re, os

BASE = os.path.dirname(os.path.abspath(__file__))

CATEGORIES = {
    "pc-components": {
        "title": "PC Components",
        "image": "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=3840&q=85",
        "alt": "PC Components — CPUs, GPUs, Motherboards",
        "description": (
            "<strong>PC Components</strong> for building and upgrading your dream setup. "
            "From processors and motherboards to GPUs, RAM, coolers, power supplies, and cases — "
            "we bring together top brands like Intel, AMD, ASUS, Corsair, NZXT, and more. "
            "Whether you are building a gaming rig or a workstation, find everything you need for performance and reliability."
        ),
        "filters": [
            ("Availability", "⚙", ["In Stock", "Pre-Order", "Out of Stock"]),
            ("Brand", "🏷", ["AMD", "Intel", "ASUS", "Corsair", "NZXT", "Gigabyte", "MSI", "Seasonic"]),
            ("Component Type", "🔧", ["CPU / Processor", "GPU / Graphics Card", "Motherboard", "RAM", "PSU", "Cooler", "PC Case", "SSD"]),
            ("Socket Type", "🔩", ["LGA1700", "LGA1851", "AM4", "AM5", "TR4"]),
            ("Price Range", "💰", ["Under AED 200", "AED 200–500", "AED 500–1000", "AED 1000–2000", "Above AED 2000"]),
        ],
    },
    "desktop-and-laptop": {
        "title": "Desktop & Laptop",
        "image": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=3840&q=85",
        "alt": "Desktops and Laptops",
        "description": (
            "<strong>Desktops &amp; Laptops</strong> for every need — from business ultrabooks to high-performance "
            "all-in-ones and workstation towers. Explore top brands like HP, Dell, Lenovo, Apple, and ASUS. "
            "Whether you need a portable powerhouse or a desktop workstation, find the right machine for work and play."
        ),
        "filters": [
            ("Availability", "⚙", ["In Stock", "Pre-Order", "Out of Stock"]),
            ("Brand", "🏷", ["HP", "Dell", "Lenovo", "Apple", "ASUS", "Acer", "Microsoft"]),
            ("Type", "💻", ["Business Laptop", "Gaming Laptop", "Desktop AIO", "Tower Desktop", "Workstation"]),
            ("Processor", "🔧", ["Intel Core i5", "Intel Core i7", "Intel Core i9", "AMD Ryzen 5", "AMD Ryzen 7", "Apple M-Series"]),
            ("RAM", "📦", ["8 GB", "16 GB", "32 GB", "64 GB"]),
            ("Price Range", "💰", ["Under AED 1000", "AED 1000–3000", "AED 3000–6000", "Above AED 6000"]),
        ],
    },
    "computer-accessories": {
        "title": "Computer Accessories",
        "image": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=3840&q=85",
        "alt": "Computer Accessories — Keyboards, Mice, Headsets",
        "description": (
            "<strong>Computer Accessories</strong> to complete your workstation or gaming setup. "
            "Discover keyboards, mice, webcams, headsets, USB hubs, docking stations, laptop stands, and more. "
            "Featuring top brands like Logitech, Razer, HP, Dell, and Belkin — the perfect complement to any system."
        ),
        "filters": [
            ("Availability", "⚙", ["In Stock", "Pre-Order", "Out of Stock"]),
            ("Brand", "🏷", ["Logitech", "Razer", "HP", "Dell", "Belkin", "Anker", "Kingston"]),
            ("Category", "🖱", ["Keyboard", "Mouse", "Headset & Mic", "Webcam", "USB Hub", "Docking Station", "Laptop Stand", "Cable & Adapter"]),
            ("Connectivity", "📡", ["Wired", "Wireless", "Bluetooth", "USB-C", "USB-A"]),
            ("Price Range", "💰", ["Under AED 100", "AED 100–300", "AED 300–700", "Above AED 700"]),
        ],
    },
    "monitors-and-projectors": {
        "title": "Monitors & Projectors",
        "image": "https://images.unsplash.com/photo-1593640408182-31c70c8268f5?w=3840&q=85",
        "alt": "Monitors and Projectors",
        "description": (
            "<strong>Monitors &amp; Projectors</strong> for crisp, vibrant displays in any environment. "
            "From ultra-wide business monitors to 4K gaming screens and compact portable projectors — "
            "find the right display from top brands like LG, Samsung, Dell, BenQ, Acer, and Epson."
        ),
        "filters": [
            ("Availability", "⚙", ["In Stock", "Pre-Order", "Out of Stock"]),
            ("Brand", "🏷", ["LG", "Samsung", "Dell", "BenQ", "Acer", "AOC", "Epson", "ViewSonic"]),
            ("Type", "🖥", ["IPS Monitor", "VA Monitor", "OLED Monitor", "Curved Monitor", "4K Monitor", "Projector"]),
            ("Screen Size", "📐", ['24"', '27"', '32"', '34" Ultrawide', '40"+']),
            ("Resolution", "🔍", ["Full HD (1080p)", "QHD (1440p)", "4K UHD", "8K"]),
            ("Refresh Rate", "⚡", ["60 Hz", "75 Hz", "144 Hz", "165 Hz", "240 Hz+"]),
        ],
    },
    "gaming": {
        "title": "Gaming",
        "image": "https://images.unsplash.com/photo-1593642632559-0c6d3fc62b89?w=3840&q=85",
        "alt": "Gaming — PCs, Consoles, Peripherals",
        "description": (
            "<strong>Gaming</strong> gear for every level of player. Explore gaming PCs, consoles, "
            "controllers, gaming chairs, RGB peripherals, and more. "
            "From casual setups to full esports rigs — featuring ASUS ROG, Razer, SteelSeries, MSI, and PlayStation."
        ),
        "filters": [
            ("Availability", "⚙", ["In Stock", "Pre-Order", "Out of Stock"]),
            ("Brand", "🏷", ["ASUS ROG", "Razer", "MSI", "SteelSeries", "HyperX", "Corsair", "PlayStation", "Xbox"]),
            ("Category", "🎮", ["Gaming PC", "Gaming Laptop", "Console", "Controller", "Gaming Headset", "Gaming Chair", "RGB Keyboard", "Gaming Mouse"]),
            ("Platform", "🕹", ["PC", "PlayStation 5", "Xbox Series X", "Nintendo Switch"]),
            ("Price Range", "💰", ["Under AED 200", "AED 200–500", "AED 500–1500", "Above AED 1500"]),
        ],
    },
    "printers-and-scanners": {
        "title": "Printers & Scanners",
        "image": "https://images.unsplash.com/photo-1612815154858-60aa4c59eaa6?w=3840&q=85",
        "alt": "Printers and Scanners",
        "description": (
            "<strong>Printers &amp; Scanners</strong> for home, office, and professional use. "
            "From compact inkjet printers to high-speed laser MFPs, plotters, and document scanners — "
            "we carry Canon, HP, Epson, Brother, Kyocera, and more. "
            "Find the right print solution for any volume and workflow."
        ),
        "filters": [
            ("Availability", "⚙", ["In Stock", "Pre-Order", "Out of Stock"]),
            ("Brand", "🏷", ["Canon", "HP", "Epson", "Brother", "Kyocera", "Xerox", "Ricoh"]),
            ("Printer Type", "🖨", ["Inkjet Printer", "Laser Printer", "Laser MFP", "Large Format / Plotter", "Label Printer", "Dot Matrix", "3D Printer"]),
            ("Print Function", "📄", ["Print Only", "Print + Scan + Copy", "Print + Fax + Scan + Copy"]),
            ("Print Technology", "⚙", ["Inkjet", "Laser", "Thermal", "Sublimation"]),
            ("Monthly Pages Vol.", "📊", ["Up to 1,000", "1,000–5,000", "5,000–15,000", "15,000+"]),
            ("Paper Size", "📐", ["A4", "A3", "A3+", "A2 / Large Format"]),
            ("Connection Type", "📡", ["USB", "Wi-Fi", "Wi-Fi + Ethernet", "Ethernet Only"]),
        ],
    },
    "games-and-softwares": {
        "title": "Games & Software",
        "image": "https://images.unsplash.com/photo-1556438064-2d7646166914?w=3840&q=85",
        "alt": "Games and Software",
        "description": (
            "<strong>Games &amp; Software</strong> for work and play. "
            "Discover the latest PC and console game titles, productivity suites, creative software, antivirus solutions, "
            "and operating systems. Featuring Microsoft, Adobe, Norton, Kaspersky, EA, and more."
        ),
        "filters": [
            ("Availability", "⚙", ["In Stock", "Pre-Order", "Out of Stock"]),
            ("Brand / Publisher", "🏷", ["Microsoft", "Adobe", "Norton", "Kaspersky", "EA", "Ubisoft", "Activision"]),
            ("Category", "💿", ["PC Game", "Console Game", "Productivity Suite", "Creative Software", "Antivirus", "Operating System", "ID Card Software"]),
            ("Platform", "🕹", ["PC / Windows", "PlayStation 5", "Xbox Series X", "Nintendo Switch"]),
            ("License Type", "🔑", ["Single User", "Multi-User", "Subscription", "Perpetual"]),
        ],
    },
    "servers-and-workstations": {
        "title": "Servers & Workstations",
        "image": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=3840&q=85",
        "alt": "Servers and Workstations",
        "description": (
            "<strong>Servers &amp; Workstations</strong> built for demanding enterprise and professional environments. "
            "From tower and rack-mount servers to mobile and desktop workstations — "
            "we carry HPE, Dell, Lenovo ThinkStation, Fujitsu, and more. "
            "Scalable, reliable, and engineered for performance-critical workloads."
        ),
        "filters": [
            ("Availability", "⚙", ["In Stock", "Pre-Order", "Out of Stock"]),
            ("Brand", "🏷", ["HPE", "Dell", "Lenovo", "Fujitsu", "Supermicro", "IBM"]),
            ("Type", "🖥", ["Tower Server", "Rack Server", "Blade Server", "Desktop Workstation", "Mobile Workstation"]),
            ("Processor", "🔧", ["Intel Xeon", "AMD EPYC", "Intel Core i9", "AMD Ryzen Threadripper"]),
            ("RAM Capacity", "📦", ["16 GB", "32 GB", "64 GB", "128 GB", "256 GB+"]),
            ("Form Factor", "📐", ["1U Rack", "2U Rack", "4U Rack", "Tower", "Mini Tower"]),
        ],
    },
    "storage-and-devices": {
        "title": "Storage & Devices",
        "image": "https://images.unsplash.com/photo-1597852074816-d933c7d2b988?w=3840&q=85",
        "alt": "Storage and Devices — SSDs, HDDs, NAS",
        "description": (
            "<strong>Storage &amp; Devices</strong> for every capacity and use case. "
            "Explore internal and external SSDs, hard drives, NAS systems, USB flash drives, SD cards, and data tapes. "
            "Featuring Western Digital, Seagate, Samsung, Kingston, Synology, and more — "
            "from portable everyday storage to enterprise-grade backup solutions."
        ),
        "filters": [
            ("Availability", "⚙", ["In Stock", "Pre-Order", "Out of Stock"]),
            ("Brand", "🏷", ["Western Digital", "Seagate", "Samsung", "Kingston", "Synology", "QNAP", "SanDisk"]),
            ("Type", "💾", ["Internal SSD", "External SSD", "Internal HDD", "External HDD", "NAS", "USB Flash Drive", "SD Card", "LTO Tape"]),
            ("Interface", "🔌", ["SATA", "NVMe (M.2)", "USB 3.0", "USB-C", "Thunderbolt"]),
            ("Capacity", "📦", ["Up to 256 GB", "256 GB–1 TB", "1 TB–4 TB", "4 TB–10 TB", "10 TB+"]),
        ],
    },
    "networking": {
        "title": "Networking",
        "image": "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=3840&q=85",
        "alt": "Networking — Routers, Switches, Access Points",
        "description": (
            "<strong>Networking</strong> solutions for homes, offices, and enterprise environments. "
            "From Wi-Fi routers and managed switches to access points, firewalls, and powerline adapters — "
            "we carry TP-Link, Cisco, Ubiquiti, Netgear, D-Link, and more. "
            "Build fast, reliable, and secure networks of any scale."
        ),
        "filters": [
            ("Availability", "⚙", ["In Stock", "Pre-Order", "Out of Stock"]),
            ("Brand", "🏷", ["TP-Link", "Cisco", "Ubiquiti", "Netgear", "D-Link", "Juniper", "Aruba"]),
            ("Device Type", "📡", ["Wi-Fi Router", "Managed Switch", "Unmanaged Switch", "Access Point", "Firewall", "Powerline Adapter", "KVM Switch", "Range Extender"]),
            ("Wi-Fi Standard", "📶", ["Wi-Fi 5 (802.11ac)", "Wi-Fi 6 (802.11ax)", "Wi-Fi 6E", "Wi-Fi 7"]),
            ("Port Speed", "⚡", ["Fast Ethernet (100 Mbps)", "Gigabit (1 Gbps)", "Multi-Gig (2.5/5 Gbps)", "10 Gbps"]),
            ("Port Count", "🔌", ["4–8 Ports", "12–16 Ports", "24 Ports", "48 Ports"]),
        ],
    },
}

SVG_ICONS = {
    "⚙": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>',
    "🏷": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg>',
    "default": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>',
    "arrow": '<svg class="ai-smart-filter__dropdown-arrow-auxbybef0vkjmuctzbaigenblockd1d2c04ezpth7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>',
}

def make_filter_html(filters):
    groups_html = ""
    for label, icon, options in filters:
        icon_svg = SVG_ICONS.get(icon, SVG_ICONS["default"])
        options_html = "\n".join(
            f'              <a class="ai-smart-filter__option-auxbybef0vkjmuctzbaigenblockd1d2c04ezpth7" href="#">'
            f'{opt}</a>'
            for opt in options
        )
        groups_html += f"""
            <div class="ai-smart-filter__group-auxbybef0vkjmuctzbaigenblockd1d2c04ezpth7">
              <div class="ai-smart-filter__dropdown-auxbybef0vkjmuctzbaigenblockd1d2c04ezpth7">
                <button class="ai-smart-filter__dropdown-button-auxbybef0vkjmuctzbaigenblockd1d2c04ezpth7" type="button" onclick="this.closest('.ai-smart-filter__dropdown-auxbybef0vkjmuctzbaigenblockd1d2c04ezpth7').classList.toggle('open')">
                  <span class="ai-smart-filter__dropdown-label-auxbybef0vkjmuctzbaigenblockd1d2c04ezpth7">
                    <span class="ai-smart-filter__dropdown-icon-auxbybef0vkjmuctzbaigenblockd1d2c04ezpth7">{icon_svg}</span>
                    <span class="ai-smart-filter__dropdown-text-auxbybef0vkjmuctzbaigenblockd1d2c04ezpth7">{label}</span>
                  </span>
                  {SVG_ICONS["arrow"]}
                </button>
                <div class="ai-smart-filter__dropdown-menu-auxbybef0vkjmuctzbaigenblockd1d2c04ezpth7">
{options_html}
                </div>
              </div>
            </div>"""
    return groups_html


def build_filter_block(cat_key, cat):
    title = cat["title"]
    groups_html = make_filter_html(cat["filters"])
    return f"""
          <div class="ai-smart-filter-container-auxbybef0vkjmuctzbaigenblockd1d2c04ezpth7">
            <div class="ai-smart-filter-auxbybef0vkjmuctzbaigenblockd1d2c04ezpth7">
              <div class="ai-smart-filter__header-auxbybef0vkjmuctzbaigenblockd1d2c04ezpth7">
                <p class="ai-smart-filter__title-auxbybef0vkjmuctzbaigenblockd1d2c04ezpth7">{title}</p>
                <p class="ai-smart-filter__subtitle-auxbybef0vkjmuctzbaigenblockd1d2c04ezpth7">Find your perfect match — Select categories to refine your search</p>
              </div>
              <button class="ai-smart-filter__all-button-auxbybef0vkjmuctzbaigenblockd1d2c04ezpth7" type="button">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
                All Products
              </button>
              <div class="ai-smart-filter__groups-auxbybef0vkjmuctzbaigenblockd1d2c04ezpth7">
{groups_html}
              </div>
            </div>
          </div>"""


HERO_PATTERN = re.compile(
    r'(<div class="collection-hero__image image-animate media media--400px media-mobile--250px">)'
    r'.*?'
    r'(</div>\s*</use-animate>)',
    re.DOTALL
)

TITLE_PATTERN = re.compile(
    r'(<h1 class="collection-hero__title h0">\s*<span class="visually-hidden">Collection:</span>\s*).*?(\s*</h1>)',
    re.DOTALL
)

DESC_PATTERN = re.compile(
    r'(<div class="collection-hero__description rte">\s*<p>).*?(</p>\s*</div>)',
    re.DOTALL
)

FILTER_SECTION_PATTERN = re.compile(
    r'(<div class="ai-smart-filter-container-auxbybef0vkjmuctzbaigenblockd1d2c04ezpth7">)'
    r'.*?'
    r'(</div>\s*<!--\s*end\s*filter|</div>\s*</div>\s*</div>\s*(?=\s*</div>\s*(?:<!--|\s*<div id="shopify)))',
    re.DOTALL
)


def update_page(filepath, cat_key):
    cat = CATEGORIES[cat_key]
    print(f"  Processing {filepath}...")

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update hero image
    new_img = (
        f'<img src="{cat["image"]}"\n'
        f'                      alt="{cat["alt"]}"\n'
        f'                      width="3840" height="2160" loading="eager" sizes="100vw" is="lazy-image">'
    )
    new_hero_inner = (
        f'\\1\n                    {new_img}\n                  \\2'
    )
    content, n = re.subn(HERO_PATTERN, lambda m: m.group(1) + "\n                    " + new_img + "\n                  " + m.group(2), content, count=1)
    if n == 0:
        print(f"    WARNING: hero image pattern not found in {filepath}")

    # 2. Update h1 title
    content, n = re.subn(
        TITLE_PATTERN,
        lambda m: m.group(1) + cat["title"] + m.group(2),
        content, count=1
    )

    # 3. Update description
    content, n = re.subn(
        DESC_PATTERN,
        lambda m: m.group(1) + cat["description"] + m.group(2),
        content, count=1
    )
    if n == 0:
        print(f"    WARNING: description pattern not found in {filepath}")

    # 4. Update filter block — replace between the container divs
    new_filter = build_filter_block(cat_key, cat)

    # Find the filter wrapper start and replace up to the end of it
    filter_start = content.find('<div class="ai-smart-filter-container-auxbybef0vkjmuctzbaigenblockd1d2c04ezpth7">')
    if filter_start == -1:
        print(f"    WARNING: filter container not found in {filepath}")
    else:
        # Find the matching close: we need to count divs
        pos = filter_start
        depth = 0
        end_pos = -1
        while pos < len(content):
            open_match = content.find("<div", pos)
            close_match = content.find("</div>", pos)
            if open_match == -1 and close_match == -1:
                break
            if open_match != -1 and (close_match == -1 or open_match < close_match):
                depth += 1
                pos = open_match + 4
            else:
                depth -= 1
                pos = close_match + 6
                if depth == 0:
                    end_pos = pos
                    break
        if end_pos != -1:
            content = content[:filter_start] + new_filter + content[end_pos:]
        else:
            print(f"    WARNING: could not find end of filter container in {filepath}")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"    Done.")


# ── Main ──────────────────────────────────────────────────────────────────────
collections_dir = os.path.join(BASE, "collections")
for cat_key in CATEGORIES:
    filepath = os.path.join(collections_dir, f"{cat_key}.html")
    if os.path.exists(filepath):
        update_page(filepath, cat_key)
    else:
        print(f"  SKIP (not found): {filepath}")

print("\nAll done!")
