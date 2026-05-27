import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
file_path = r"D:\Antigravity\定課\一鍵更新到GitHub.bat"

lines = []
if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    lines.append("Content:")
    lines.append(content)
else:
    # Try different encoding like cp950
    try:
        with open(file_path, "r", encoding="cp950", errors="ignore") as f:
            content = f.read()
        lines.append("Content (cp950):")
        lines.append(content)
    except Exception as e:
        lines.append(f"Error: {e}")

with open("bat_content.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("Saved to bat_content.txt")
