import json
import re

js_path = r"d:\Antigravity\Rich\index.js"
tags_json_path = r"d:\Antigravity\Rich\scratch\new_tags.json"

# Load new tags
with open(tags_json_path, "r", encoding="utf-8") as f:
    new_tags = json.load(f)

# Read index.js
with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

# We want to replace the tags for each parent.
# A profile block in index.js looks like:
#         {
#           "name": "王慈惠",
#           "talent": "支持者",
#           "role": "家長",
#           "image": "reference/photo/支持者-王慈惠.jpg",
#           "tags": [
#             "＃資深平面設計師",
#             "＃加入Rich二年多還清百萬",
#             "＃從負到富的樂天派女孩"
#           ]
#         }

# Let's write a robust parser/regex to replace the tags list for each member.
# Specifically, we can find:
# "name": "NAME",
# followed by other fields, up to
# "tags": [ ... ]
# and replace the content inside "tags": [ ... ]

log_lines = []

for name, tags in new_tags.items():
    # If the tags value in excel is ["0"] or empty, keep original tags
    if not tags or tags == ["0"] or tags == [""]:
        log_lines.append(f"Keeping original tags for {name} (value is 0 or empty)")
        continue
    
    # We construct the new tags array string in JS format
    # Indentation should match the style in index.js:
    #             "tag1",
    #             "tag2",
    #             "tag3"
    js_tags_str = '[\n            ' + ',\n            '.join([f'"{t}"' for t in tags]) + '\n          ]'
    
    # Let's construct a pattern to match this specific member's tags block
    # We find the member object that has "name": "NAME"
    # We can match from `"name": "NAME"` to the next `"tags": \[[^\]]+\]`
    # We use re.DOTALL and match non-greedy.
    pattern = rf'("name":\s*"{name}",.*?"tags":\s*)\[[^\]]+\]'
    
    # Test if pattern matches
    match = re.search(pattern, js_content, re.DOTALL)
    if match:
        # Perform the replacement
        js_content = re.sub(
            pattern,
            rf'\1{js_tags_str}',
            js_content,
            count=1,
            flags=re.DOTALL
        )
        log_lines.append(f"Successfully updated tags for {name} to: {tags}")
    else:
        log_lines.append(f"WARNING: Could not find block for {name} in index.js")

# Save the updated index.js
with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_content)

# Save log
with open(r"d:\Antigravity\Rich\scratch\update_tags_log.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(log_lines))

print("Successfully updated tags in index.js!")
