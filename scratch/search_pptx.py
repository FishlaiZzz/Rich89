import zipfile
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

pptx_path = r"D:\Antigravity\Rich\reference\天賦家長介紹範本.pptx"

if not os.path.exists(pptx_path):
    print("PPTX file does not exist.")
    sys.exit(0)

try:
    with zipfile.ZipFile(pptx_path, 'r') as z:
        print(f"Opened {pptx_path} successfully.")
        slide_files = [name for name in z.namelist() if name.startswith('ppt/slides/slide')]
        print(f"Found {len(slide_files)} slide files.")
        
        for sfile in slide_files:
            xml_content = z.read(sfile).decode('utf-8', errors='ignore')
            if '佩婷' in xml_content or '王佩婷' in xml_content:
                print(f"  FOUND IN {sfile}:")
                # print some surrounding text using regex
                matches = re.findall(r'<a:t>[^<]*佩婷[^<]*</a:t>', xml_content)
                for m in matches:
                    print(f"    Text: {m}")
except Exception as e:
    print("Error scanning PPTX:", e)
