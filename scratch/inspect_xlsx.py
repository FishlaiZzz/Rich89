import openpyxl
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

xlsx_path = r"D:\Antigravity\Rich\reference\RAY哥-實戰班PPT2.xlsx"
wb = openpyxl.load_workbook(xlsx_path)
sheet = wb['Rich89']

print("Dimensions:", sheet.dimensions)
for row_idx in range(1, 40):
    row_vals = [sheet.cell(row=row_idx, column=col_idx).value for col_idx in range(1, 6)]
    print(f"Row {row_idx}: {row_vals}")
