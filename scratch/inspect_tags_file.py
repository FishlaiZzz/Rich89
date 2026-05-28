import os

workspace = r"d:\Antigravity\Rich"
keywords = ["溫慢熱情支持者", "財務規劃教練", "順流人生實踐者"]

results = []
for root, dirs, files in os.walk(workspace):
    for f in files:
        if f.endswith(".txt") or f.endswith(".js") or f.endswith(".py") or f.endswith(".html"):
            fpath = os.path.join(root, f)
            try:
                with open(fpath, "r", encoding="utf-8") as file:
                    content = file.read()
                    for kw in keywords:
                        if kw in content:
                            results.append(f"Found '{kw}' in {fpath}")
            except Exception as e:
                pass

for r in results:
    print(r)
