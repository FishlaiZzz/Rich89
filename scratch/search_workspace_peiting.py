import os

workspace = r"d:\Antigravity\Rich"
results = []

for root, dirs, files in os.walk(workspace):
    for f in files:
        if "佩婷" in f or "peiting" in f.lower():
            results.append(os.path.join(root, f))

print(f"Found {len(results)} files matching '佩婷' or 'peiting':")
for r in results:
    print(r)
