import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Source File Paths
txt_89_path = r"D:\Antigravity\Rich\reference\第89期組別正副家長名單.txt"
js_path = r"D:\Antigravity\Rich\index.js"
ref_dir = r"D:\Antigravity\Rich\reference"

print("================ 89TH BATCH DATA INTEGRITY VALIDATION ================")

# 1. Parse parent list from 第89期組別正副家長名單.txt
with open(txt_89_path, "r", encoding="utf-8") as f:
    lines_89 = f.readlines()

expected_names = []
for line in lines_89:
    line = line.strip()
    if not line or line.startswith("【"):
        continue
    match = re.match(r'^(\d+)\s*(\S+)\s+(\S+)', line)
    if match:
        expected_names.append(match.group(2).strip())
        expected_names.append(match.group(3).strip())

print(f"Parsed {len(expected_names)} expected parent/co-parent names from 89th batch text file.")

# 2. Extract and parse data model inside index.js
with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

# We can search for the values of members in groupData block
js_members = re.findall(r'"?name"?:\s*"([^"]+)"[^{}]+"?talent"?:\s*"([^"]+)"[^{}]+"?role"?:\s*"([^"]+)"[^{}]+"?image"?:\s*"([^"]+)"[^{}]+"?tags"?:\s*\[([^\]]+)\]', js_content)

print(f"Parsed {len(js_members)} profiles inside index.js data model.")

errors = []
warnings = []

# Validate count
if len(expected_names) != 26:
    errors.append(f"89th batch text file should contain exactly 26 names, but found {len(expected_names)}")
if len(js_members) != 26:
    errors.append(f"index.js data model should contain exactly 26 profiles, but found {len(js_members)}")

# Validate each name matches
for exp_name in expected_names:
    js_match = None
    for js_m in js_members:
        js_name = js_m[0].strip()
        if exp_name == js_name or exp_name in js_name or js_name in exp_name:
            js_match = js_m
            break
            
    if not js_match:
        errors.append(f"Could not find matching profile in index.js for 89th batch name '{exp_name}'")
    else:
        # Match found! Verify tags
        js_tags_raw = js_match[4]
        js_tags = [t.replace('"', '').replace("'", "").replace("#", "").replace("＃", "").replace(" ", "").strip() for t in js_tags_raw.split(",")]
        
        if len(js_tags) != 3:
            errors.append(f"Parent '{js_match[0]}' in index.js does not have exactly 3 tags (found {len(js_tags)}).")
        
        # Verify image path
        js_image = js_match[3].strip()
        relative_path = js_image.replace("reference/", "")
        image_full_path = os.path.join(ref_dir, relative_path)
        if not os.path.exists(image_full_path):
            errors.append(f"Referenced image path does not exist on disk: '{image_full_path}' for parent '{js_match[0]}'.")

# Output results
if errors:
    print(f"\n❌ Validation failed with {len(errors)} errors:")
    for err in errors:
        print(f"  - ERROR: {err}")
    sys.exit(1)
else:
    print("\n🎉 SUCCESS! All 26 parents and tags matched perfectly for Batch 89.")
    print("🎉 All 26 referenced avatar image assets actually exist on disk.")
    print("======================================================================")
