import openpyxl

wb = openpyxl.load_workbook(r"reference\RAY哥-實戰班PPT2.xlsx", data_only=True)
sheet = wb["Rich89"]

print("Printing rows 110 to 125 of RAY哥-實戰班PPT2.xlsx:")
results = []
for r in range(105, 130):
    row_vals = [sheet.cell(row=r, column=c).value for c in range(1, 5)]
    results.append(f"Row {r}: {row_vals}")

with open(r"scratch\excel_rows_110_125.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(results))

print("Done. Saved to scratch/excel_rows_110_125.txt")
