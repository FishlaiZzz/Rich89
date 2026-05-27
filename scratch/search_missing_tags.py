import sys

sys.stdout.reconfigure(encoding='utf-8')

# Let's search for tags of missing parents in excel_rows.txt
missing_tags = {
    "楊琬琳": ["#咖啡師斜槓房仲", "#崇尚自由的靈魂", "#自帶貴人幸運星"],
    "王佩婷": ["#溫慢熱情支持者", "#財務規劃教練", "#順流人生實踐者"],
    "楊媛媛": ["#細水長流積蓄者", "#天賦諮詢師", "#專業財務規劃師"],
    "王宥鈞": ["#溫暖陪伴輔導員", "#天賦指引師", "#能量學實踐者"],
    "謝彥馨": ["#能量學高階輔導長", "#天賦順流指引師", "#雙北地區財富流教練"]
}

with open("scratch/excel_rows.txt", "r", encoding="utf-8") as f:
    rows = f.readlines()

for name, tags in missing_tags.items():
    print(f"\nSearching for '{name}' tags:")
    for tag in tags:
        found_tag = False
        for row in rows:
            if tag in row or tag[1:] in row:
                print(f"  Tag '{tag}' found in Row: {row.strip()}")
                found_tag = True
        if not found_tag:
            print(f"  Tag '{tag}' not found.")
