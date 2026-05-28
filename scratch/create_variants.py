import os

workspace = r"d:\Antigravity\Rich"
html_path = os.path.join(workspace, "index.html")
js_path = os.path.join(workspace, "index.js")

# 1. Read original index.html and index.js
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

# ==================== VERSION 2: index2.html & index2.js ====================
# HTML: Point to index2.js, update titles
html2 = html_content.replace(
    '<title>輕易豐盛學苑 | 天賦實戰班第89期黃金家長團隊</title>',
    '<title>輕易豐盛學苑 | 天賦實戰班第89期黃金家長團隊 (完整收納版)</title>'
).replace(
    '<h1 id="mainTitle">天賦實戰班第89期黃金陣容</h1>',
    '<h1 id="mainTitle">天賦實戰班第89期黃金陣容 (完整收納版)</h1>'
).replace(
    '<script src="index.js"></script>',
    '<script src="index2.js"></script>'
)

# JS: Set all images to contain and top-position
js2 = js_content.replace(
    '<img class="profile-image" src="${member.image}" alt="${member.name} - ${member.talent}" loading="lazy"${member.name === "江勁霖" ? \' style="object-fit: contain; object-position: top;"\' : \'\'}>',
    '<img class="profile-image" src="${member.image}" alt="${member.name} - ${member.talent}" loading="lazy" style="object-fit: contain; object-position: top;">'
)

# ==================== VERSION 3: index3.html & index3.js ====================
# HTML: Point to index3.js, update titles
html3 = html_content.replace(
    '<title>輕易豐盛學苑 | 天賦實戰班第89期黃金家長團隊</title>',
    '<title>輕易豐盛學苑 | 天賦實戰班第89期黃金家長團隊 (頭部半身版)</title>'
).replace(
    '<h1 id="mainTitle">天賦實戰班第89期黃金陣容</h1>',
    '<h1 id="mainTitle">天賦實戰班第89期黃金陣容 (頭部半身版)</h1>'
).replace(
    '<script src="index.js"></script>',
    '<script src="index3.js"></script>'
)

# JS: Set all images to cover and top-position
js3 = js_content.replace(
    '<img class="profile-image" src="${member.image}" alt="${member.name} - ${member.talent}" loading="lazy"${member.name === "江勁霖" ? \' style="object-fit: contain; object-position: top;"\' : \'\'}>',
    '<img class="profile-image" src="${member.image}" alt="${member.name} - ${member.talent}" loading="lazy" style="object-fit: cover; object-position: top;">'
)

# Write index2 files
with open(os.path.join(workspace, "index2.html"), "w", encoding="utf-8") as f:
    f.write(html2)
with open(os.path.join(workspace, "index2.js"), "w", encoding="utf-8") as f:
    f.write(js2)

# Write index3 files
with open(os.path.join(workspace, "index3.html"), "w", encoding="utf-8") as f:
    f.write(html3)
with open(os.path.join(workspace, "index3.js"), "w", encoding="utf-8") as f:
    f.write(js3)

print("index2.html, index2.js, index3.html, index3.js created successfully!")
