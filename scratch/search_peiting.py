import os

photo_dir = r"d:\Antigravity\Rich\reference\photo"
photos = os.listdir(photo_dir)

results = []
results.append("Checking for files containing '佩婷':")
for p in photos:
    if "佩婷" in p:
        results.append(f"MATCH: {p}")

results.append("\nChecking for files containing '佩':")
for p in photos:
    if "佩" in p:
        results.append(f"MATCH: {p}")

results.append("\nChecking for files containing '婷':")
for p in photos:
    if "婷" in p:
        results.append(f"MATCH: {p}")

# Write results
with open(r"d:\Antigravity\Rich\scratch\search_peiting_results.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(results))

print("Results written to search_peiting_results.txt")
