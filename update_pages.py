import os

mappings = [
    {
        "html": "desktop-and-laptop.html",
        "js": "desktop_laptop_data.js",
        "var": "DESKTOP_LAPTOP_PRODUCTS",
        "title": "Desktop and Laptop"
    },
    {
        "html": "computer-accessories.html",
        "js": "computer_accessories_data.js",
        "var": "COMPUTER_ACCESSORIES_PRODUCTS",
        "title": "Computer Accessories"
    },
    {
        "html": "monitors-and-projectors.html",
        "js": "monitors_projectors_data.js",
        "var": "MONITORS_PROJECTORS_PRODUCTS",
        "title": "Monitors and Projectors"
    },
    {
        "html": "gaming.html",
        "js": "gaming_data.js",
        "var": "GAMING_PRODUCTS",
        "title": "Gaming"
    },
    {
        "html": "printers-and-scanners.html",
        "js": "printers_scanners_data.js",
        "var": "PRINTERS_SCANNERS_PRODUCTS",
        "title": "Printers and Scanners"
    },
    {
        "html": "games-and-softwares.html",
        "js": "games_software_data.js",
        "var": "SOFTWARE_PRODUCTS",
        "title": "Games and Softwares"
    },
    {
        "html": "servers-and-workstations.html",
        "js": "servers_workstations_data.js",
        "var": "SERVERS_WORKSTATIONS_PRODUCTS",
        "title": "Servers and Workstations"
    },
    {
        "html": "storage-and-devices.html",
        "js": "storage_devices_data.js",
        "var": "STORAGE_DEVICES_PRODUCTS",
        "title": "Storage and Devices"
    },
    {
        "html": "networking.html",
        "js": "networking_data.js",
        "var": "NETWORKING_9ETOWRSQ_PRODUCTS",
        "title": "Networking"
    }
]

# Fix JS files first
for item in mappings:
    js_path = os.path.join("components", item["js"])
    if os.path.exists(js_path):
        with open(js_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace export const with window.
        content = content.replace("export const " + item["var"] + " = [", "window." + item["var"] + " = [")
        
        with open(js_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated JS: " + item["js"])

# Update HTML files
for item in mappings:
    html_path = os.path.join("collections", item["html"])
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replacements
        content = content.replace("<title>Buy PC Components", "<title>Buy " + item["title"])
        content = content.replace("alt=\"PC Components\"", "alt=\"" + item["title"] + "\"")
        content = content.replace(">PC Components<", ">" + item["title"] + "<")
        content = content.replace("                    PC Components", "                    " + item["title"])
        content = content.replace("<strong>PC Components</strong> for building and upgrading your dream setup. From processors and", "<strong>" + item["title"] + "</strong>")
        
        # Script tag
        content = content.replace("src=\"../components/pc_components_data.js\"", "src=\"../components/" + item["js"] + "\"")
        
        # JS variables
        content = content.replace("!window.PC_COMPONENTS_PRODUCTS", "!window." + item["var"])
        content = content.replace("= window.PC_COMPONENTS_PRODUCTS", "= window." + item["var"])
        
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated HTML: " + item["html"])
