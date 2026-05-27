import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read parent list
txt_89_path = r"D:\Antigravity\Rich\reference\第89期組別正副家長名單.txt"
with open(txt_89_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

parents = []
for line in lines:
    line = line.strip()
    if not line or line.startswith("【"):
        continue
    parts = line.split()
    # E.g. "1王慈惠 蕭惠允"
    # Remove leading group number from first name
    match = re.match(r'^\d+(\S+)', parts[0])
    if match:
        p1 = match.group(1).strip()
    else:
        p1 = parts[0].strip()
    parents.append(p1)
    if len(parts) > 1:
        parents.append(parts[1].strip())

print("Parents (Total 26):", parents)

# Read tags file
tags_path = r"D:\Antigravity\Rich\reference\正副家長姓名標籤.txt"
with open(tags_path, "r", encoding="utf-8") as f:
    tags_raw = f.read()

# Parse tags file into blocks robustly
blocks = []
current_header = None
current_tags = []

lines = tags_raw.splitlines()
for line in lines:
    line = line.strip()
    if not line:
        continue
    if line.startswith("#") or line.startswith("＃"):
        if current_header:
            current_tags.append(line)
    else:
        if current_header and current_tags:
            blocks.append((current_header, current_tags))
        current_header = line
        current_tags = []

if current_header and current_tags:
    blocks.append((current_header, current_tags))

print("\n--- Parsed Tag Blocks (Robust) ---")
for idx, (header, tags) in enumerate(blocks):
    print(f"Block {idx+1}: Header='{header}', Tags={tags}")

# Let's map parent names to tag blocks
mapped = {}
for parent in parents:
    # Try to find a block where the header contains the parent name or parts of the parent name
    # e.g., "王雅琳" in "地)王雅琳_114光譜_新店"
    # "江勁霖" matches "勁霖"
    # "楊琬琳" matches "琬琳"
    # "蕭惠允" matches "蕭惠允"
    matched_blocks = []
    for header, tags in blocks:
        # Check direct substring
        if parent in header:
            matched_blocks.append((header, tags))
            continue
        
        # Check if parent is "林苡姗" and header is "玟姍（13）"
        if parent == "林苡姗" and ("玟姍" in header or "苡姗" in header or "13" in header):
            matched_blocks.append((header, tags))
            continue
            
        # Check if last 2 characters of parent name are in header (e.g. "勁霖" in "勁霖")
        if len(parent) >= 3:
            short_name = parent[1:]
            if short_name in header:
                matched_blocks.append((header, tags))
                continue
                
    if matched_blocks:
        mapped[parent] = matched_blocks

print("\n--- Mappings ---")
for parent, m_blocks in mapped.items():
    print(f"Parent '{parent}':")
    for h, t in m_blocks:
        print(f"  -> Match Header: '{h}' | Tags: {t}")

unmapped = [p for p in parents if p not in mapped]
print("\nUnmapped parents:", unmapped)
