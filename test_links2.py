import os
import re

html_files = ["index2.html"]
for root, dirs, files in os.walk("ui2"):
    for f in files:
        if f.endswith(".html"):
            html_files.append(os.path.join(root, f).replace("\\", "/"))

print(f"Checking {len(html_files)} HTML files for link integrity...\n")

total_links = 0
dead_hashes = 0
missing_files = []

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Check for '#' dead links
    hashes = re.findall(r'href=["\']#["\']', html)
    if hashes:
        print(f"ERROR in {file_path}: Found {len(hashes)} href=\"#\"")
        dead_hashes += len(hashes)

    # 2. Extract all href links
    links = re.findall(r'href=["\']([^"\']+)["\']', html)
    base_dir = os.path.dirname(file_path)

    for link in links:
        total_links += 1
        if link.startswith("http://") or link.startswith("https://") or link.startswith("mailto:") or link.startswith("tel:"):
            continue

        target = link.split("#")[0].split("?")[0]
        if not target:
            continue

        if target.endswith("/"):
            target_file = os.path.join(base_dir, target, "index.html")
        else:
            target_file = os.path.join(base_dir, target)

        target_file = os.path.normpath(target_file)

        if not os.path.exists(target_file):
            missing_files.append((file_path, link, target_file))

print(f"Total links audited: {total_links}")
print(f"Dead '#' links: {dead_hashes}")
if missing_files:
    print(f"BROKEN LINKS ({len(missing_files)}):")
    for source, link, resolved in missing_files:
        print(f"  In {source} -> '{link}' (Resolved to: {resolved})")
else:
    print("ALL INTERNAL LINKS RESOLVE TO EXISTING FILES! ZERO 404s!")
