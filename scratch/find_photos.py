import json
import re
import os

js_path = r"d:\Antigravity\Rich\index.js"
photo_dir = r"d:\Antigravity\Rich\reference\photo"

# Read index.js
with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Parse the JSON structure properly by finding the "const groupData = ..." pattern
# Let's extract the JS object by finding the matching braces
start_idx = js_content.find("const groupData =")
if start_idx == -1:
    print("Could not find groupData")
    exit(1)

# Find the first '{' after 'const groupData ='
brace_start = js_content.find("{", start_idx)
# Parse simple JS object as JSON by converting keys and removing trailing commas if any,
# or just do a robust regex since the format is very clean.
# Actually, let's just use regex to extract name, talent, role, and current image.
pattern = r'\{\s*"name":\s*"([^"]+)",\s*"talent":\s*"([^"]+)",\s*"role":\s*"([^"]+)",\s*"image":\s*"([^"]+)"'
matches = re.findall(pattern, js_content)

photos = os.listdir(photo_dir)

results = []
results.append(f"Found {len(matches)} members in index.js")
results.append(f"Found {len(photos)} photos in {photo_dir}\n")

mismatches = []
matches_found = []

for name, talent, role, curr_img in matches:
    # Find matching photo files
    matched_files = [p for p in photos if name in p]
    if matched_files:
        matches_found.append({
            "name": name,
            "talent": talent,
            "role": role,
            "curr_img": curr_img,
            "matched_files": matched_files
        })
    else:
        mismatches.append({
            "name": name,
            "talent": talent,
            "role": role,
            "curr_img": curr_img
        })

results.append("=== MATCHES FOUND ===")
for m in matches_found:
    results.append(f"Name: {m['name']} | Talent in JS: {m['talent']} | Role: {m['role']} | Current Img: {m['curr_img']}")
    for f in m['matched_files']:
        results.append(f"  -> Found Photo File: {f}")

results.append("\n=== WARNING: MISMATCHES / NO PHOTO FOUND ===")
for m in mismatches:
    results.append(f"Name: {m['name']} | Talent in JS: {m['talent']} | Role: {m['role']} | Current Img: {m['curr_img']}")

# Write to file in utf-8
output_path = r"d:\Antigravity\Rich\scratch\find_photos_results.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n".join(results))

print("Results written to find_photos_results.txt")
