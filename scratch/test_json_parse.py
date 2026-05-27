import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

js_path = r"D:\Antigravity\Rich\index.js"
with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

# Extract groupData block
start_marker = "  const groupData = "
end_marker = "};"

start_idx = js_content.find(start_marker)
if start_idx == -1:
    print("Could not find start of groupData")
    sys.exit(1)

start_json_idx = start_idx + len(start_marker)

# Find the matching closing brace before the semicolon
# We can find the end_marker "};"
end_idx = js_content.find(end_marker, start_json_idx)
if end_idx == -1:
    print("Could not find end of groupData")
    sys.exit(1)

json_str = js_content[start_json_idx:end_idx+1].strip()

print("Extracted JSON sample:")
print(json_str[:200])
print("...")
print(json_str[-200:])

try:
    group_data = json.loads(json_str)
    print("\n🎉 SUCCESS! Extracted block is valid JSON!")
except Exception as e:
    print("\n❌ Failed to parse as JSON:", e)
