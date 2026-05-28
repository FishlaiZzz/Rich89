import os
import re

photo_dir = r"d:\Antigravity\Rich\reference\photo"
photos = os.listdir(photo_dir)

pattern = r"^([^-]+)-([^-]+)\.(jpg|png|jpeg)$"

non_matching = []
for p in photos:
    match = re.match(pattern, p)
    if not match:
        non_matching.append(p)

print(f"Non-matching files ({len(non_matching)}):")
for n in non_matching:
    print(n)
