import os

filepath = "/Users/ankit/atomoffice-local/atomoffice-local/atomoffice.com/components/navbar.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Mobile menu replacements
content = content.replace(
    """<a class="menu-drawer__menu-item" href="#">DESKTOP
                                          &amp; LAPTOP</a>""",
    """<a class="menu-drawer__menu-item" href="collections/desktop-and-laptop.html">DESKTOP
                                          &amp; LAPTOP</a>"""
)

content = content.replace(
    """<a class="menu-drawer__menu-item" href="#">COMPUTER
                                          ACCESSORIES</a>""",
    """<a class="menu-drawer__menu-item" href="collections/computer-accessories.html">COMPUTER
                                          ACCESSORIES</a>"""
)

content = content.replace(
    """<a class="menu-drawer__menu-item" href="#">MONITORS
                                          &amp; PROJECTORS</a>""",
    """<a class="menu-drawer__menu-item" href="collections/monitors-and-projectors.html">MONITORS
                                          &amp; PROJECTORS</a>"""
)

content = content.replace(
    """<a class="menu-drawer__menu-item" href="#">GAMING</a>""",
    """<a class="menu-drawer__menu-item" href="collections/gaming.html">GAMING</a>"""
)

content = content.replace(
    """<a class="menu-drawer__menu-item" href="#">PRINTERS &amp; SCANNERS</a>""",
    """<a class="menu-drawer__menu-item" href="collections/printers-and-scanners.html">PRINTERS &amp; SCANNERS</a>"""
)

content = content.replace(
    """<a class="menu-drawer__menu-item" href="#">GAMES &amp; SOFTWARE</a>""",
    """<a class="menu-drawer__menu-item" href="collections/games-and-softwares.html">GAMES &amp; SOFTWARE</a>"""
)

content = content.replace(
    """<a class="menu-drawer__menu-item" href="#">SERVERS &amp; WORKSTATIONS</a>""",
    """<a class="menu-drawer__menu-item" href="collections/servers-and-workstations.html">SERVERS &amp; WORKSTATIONS</a>"""
)

content = content.replace(
    """<a class="menu-drawer__menu-item" href="#">STORAGE &amp; DEVICES</a>""",
    """<a class="menu-drawer__menu-item" href="collections/storage-and-devices.html">STORAGE &amp; DEVICES</a>"""
)

content = content.replace(
    """<a class="menu-drawer__menu-item" href="#">NETWORKING</a>""",
    """<a class="menu-drawer__menu-item" href="collections/networking.html">NETWORKING</a>"""
)

# Mega menu replacements
content = content.replace(
    """<a class="mega-menu__item-link list-menu__item focus-inset" href="#">
                        <div class="header__menu-item">
                          <span class="label">DESKTOP &amp; LAPTOP</span>""",
    """<a class="mega-menu__item-link list-menu__item focus-inset" href="collections/desktop-and-laptop.html">
                        <div class="header__menu-item">
                          <span class="label">DESKTOP &amp; LAPTOP</span>"""
)

content = content.replace(
    """<a class="mega-menu__item-link list-menu__item focus-inset" href="#">
                        <div class="header__menu-item">
                          <span class="label">COMPUTER ACCESSORIES</span>""",
    """<a class="mega-menu__item-link list-menu__item focus-inset" href="collections/computer-accessories.html">
                        <div class="header__menu-item">
                          <span class="label">COMPUTER ACCESSORIES</span>"""
)

content = content.replace(
    """<a class="mega-menu__item-link list-menu__item focus-inset" href="#">
                        <div class="header__menu-item">
                          <span class="label">MONITORS &amp; PROJECTORS</span>""",
    """<a class="mega-menu__item-link list-menu__item focus-inset" href="collections/monitors-and-projectors.html">
                        <div class="header__menu-item">
                          <span class="label">MONITORS &amp; PROJECTORS</span>"""
)

content = content.replace(
    """<a class="mega-menu__item-link list-menu__item focus-inset" href="#">
                        <div class="header__menu-item">
                          <span class="label">GAMING</span>""",
    """<a class="mega-menu__item-link list-menu__item focus-inset" href="collections/gaming.html">
                        <div class="header__menu-item">
                          <span class="label">GAMING</span>"""
)

content = content.replace(
    """<a class="mega-menu__item-link list-menu__item focus-inset" href="#">
                        <div class="header__menu-item">
                          <span class="label">PRINTERS &amp; SCANNERS</span>""",
    """<a class="mega-menu__item-link list-menu__item focus-inset" href="collections/printers-and-scanners.html">
                        <div class="header__menu-item">
                          <span class="label">PRINTERS &amp; SCANNERS</span>"""
)

content = content.replace(
    """<a class="mega-menu__item-link list-menu__item focus-inset" href="#">
                        <div class="header__menu-item">
                          <span class="label">GAMES &amp; SOFTWARE</span>""",
    """<a class="mega-menu__item-link list-menu__item focus-inset" href="collections/games-and-softwares.html">
                        <div class="header__menu-item">
                          <span class="label">GAMES &amp; SOFTWARE</span>"""
)

content = content.replace(
    """<a class="mega-menu__item-link list-menu__item focus-inset" href="#">
                        <div class="header__menu-item">
                          <span class="label">SERVERS &amp; WORKSTATIONS</span>""",
    """<a class="mega-menu__item-link list-menu__item focus-inset" href="collections/servers-and-workstations.html">
                        <div class="header__menu-item">
                          <span class="label">SERVERS &amp; WORKSTATIONS</span>"""
)

content = content.replace(
    """<a class="mega-menu__item-link list-menu__item focus-inset" href="#">
                        <div class="header__menu-item">
                          <span class="label">STORAGE &amp; DEVICES</span>""",
    """<a class="mega-menu__item-link list-menu__item focus-inset" href="collections/storage-and-devices.html">
                        <div class="header__menu-item">
                          <span class="label">STORAGE &amp; DEVICES</span>"""
)

content = content.replace(
    """<a class="mega-menu__item-link list-menu__item focus-inset" href="#">
                        <div class="header__menu-item">
                          <span class="label">NETWORKING</span>""",
    """<a class="mega-menu__item-link list-menu__item focus-inset" href="collections/networking.html">
                        <div class="header__menu-item">
                          <span class="label">NETWORKING</span>"""
)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
