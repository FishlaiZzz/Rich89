import sys

sys.stdout.reconfigure(encoding='utf-8')

try:
    with open("scratch/excel_rows.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    print(f"Total lines in excel_rows.txt: {len(lines)}")
    for idx, line in enumerate(lines):
        if "佩" in line or "婷" in line or "明星" in line:
            print(f"Line {idx+1}: {line.strip()}")
except Exception as e:
    print("Error:", e)
