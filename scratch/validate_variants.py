import re
import os
import sys

ref_dir = r"D:\Antigravity\Rich\reference"
txt_89_path = r"D:\Antigravity\Rich\reference\第89期組別正副家長名單.txt"

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

js_files = ["index.js", "index2.js", "index3.js"]
results = []

for js_file in js_files:
    js_path = os.path.join(r"D:\Antigravity\Rich", js_file)
    results.append(f"\n================ VALIDATING: {js_file} ================")
    
    with open(js_path, "r", encoding="utf-8") as f:
        js_content = f.read()

    js_members = re.findall(r'"?name"?:\s*"([^"]+)"[^{}]+"?talent"?:\s*"([^"]+)"[^{}]+"?role"?:\s*"([^"]+)"[^{}]+"?image"?:\s*"([^"]+)"[^{}]+"?tags"?:\s*\[([^\]]+)\]', js_content)
    results.append(f"Parsed {len(js_members)} profiles inside {js_file} data model.")

    errors = []
    
    if len(expected_names) != 26:
        errors.append(f"89th batch text file should contain exactly 26 names, but found {len(expected_names)}")
    if len(js_members) != 26:
        errors.append(f"{js_file} data model should contain exactly 26 profiles, but found {len(js_members)}")

    for exp_name in expected_names:
        js_match = None
        for js_m in js_members:
            js_name = js_m[0].strip()
            if exp_name == js_name or exp_name in js_name or js_name in exp_name:
                js_match = js_m
                break
                
        if not js_match:
            errors.append(f"Could not find matching profile in {js_file} for 89th batch name '{exp_name}'")
        else:
            js_tags_raw = js_match[4]
            js_tags = [t.replace('"', '').replace("'", "").replace("#", "").replace("＃", "").replace(" ", "").strip() for t in js_tags_raw.split(",")]
            
            if len(js_tags) != 3:
                errors.append(f"Parent '{js_match[0]}' in {js_file} does not have exactly 3 tags (found {len(js_tags)}).")
            
            js_image = js_match[3].strip()
            relative_path = js_image.replace("reference/", "")
            image_full_path = os.path.join(ref_dir, relative_path)
            if not os.path.exists(image_full_path):
                errors.append(f"Referenced image path does not exist on disk: '{image_full_path}' for parent '{js_match[0]}'.")

    if errors:
        results.append(f"ERROR: Validation failed for {js_file} with {len(errors)} errors:")
        for err in errors:
            results.append(f"  - {err}")
    else:
        results.append(f"SUCCESS: {js_file} is 100% valid and correct.")

# Save log
with open(r"d:\Antigravity\Rich\scratch\validate_variants_results.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(results))

print("Validation results written to scratch/validate_variants_results.txt")
if any("ERROR" in line for line in results):
    sys.exit(1)
