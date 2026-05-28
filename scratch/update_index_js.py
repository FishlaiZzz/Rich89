import os
import json
import re

js_path = r"d:\Antigravity\Rich\index.js"
photo_dir = r"d:\Antigravity\Rich\reference\photo"

# Read current index.js
with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Get list of photos in directory
photos = os.listdir(photo_dir)

# Mapping of parent names to photo filenames and talents
parent_names = [
    "王慈惠", "蕭惠允", "許蓓瑾", "楊家瑜", "劉錦芳", "楊琬琳",
    "楊君慧", "周詩容", "黃雲嵩", "賴貞如", "王雅琳", "林苡姗",
    "陳瑩臻", "許淳皓", "林胤呈", "張庭熒", "楊振達", "王佩婷",
    "吳家怡", "徐瑩瑩", "江勁霖", "楊媛媛", "王宥鈞", "陳彥萍",
    "謝彥馨", "張家榮"
]

photo_mapping = {}
for name in parent_names:
    matched = [p for p in photos if name in p]
    if matched:
        filename = matched[0]
        talent = filename.split("-")[0]
        photo_mapping[name] = {
            "image": f"reference/photo/{filename}",
            "talent": talent
        }
    else:
        photo_mapping[name] = {
            "image": None,
            "talent": None
        }

log_lines = []
new_js_content = js_content

member_block_pattern = r'\{\s*"name":\s*"([^"]+)",\s*"talent":\s*"([^"]+)",\s*"role":\s*"([^"]+)",\s*"image":\s*"([^"]+)"'

def replace_member(match):
    name = match.group(1)
    old_talent = match.group(2)
    role = match.group(3)
    old_image = match.group(4)
    
    mapping = photo_mapping.get(name)
    if mapping and mapping["image"]:
        new_image = mapping["image"]
        new_talent = mapping["talent"]
        log_lines.append(f"Updating {name}: image '{old_image}' -> '{new_image}', talent '{old_talent}' -> '{new_talent}'")
        return f'{{\n          "name": "{name}",\n          "talent": "{new_talent}",\n          "role": "{role}",\n          "image": "{new_image}"'
    else:
        log_lines.append(f"Keeping default for {name} (no photo found)")
        return match.group(0)

# Replace all occurrences
new_js_content = re.sub(member_block_pattern, replace_member, js_content)

# Save the updated index.js
with open(js_path, 'w', encoding='utf-8') as f:
    f.write(new_js_content)

# Save log
with open(r"d:\Antigravity\Rich\scratch\update_index_js_log.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(log_lines))

print("Successfully updated index.js! Log written to scratch/update_index_js_log.txt")
