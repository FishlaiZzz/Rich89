from PIL import Image

img_path = r"d:\Antigravity\Rich\reference\photo\支持者-江勁霖.jpg"
try:
    img = Image.open(img_path)
    print(f"Format: {img.format}, Size: {img.size}, Mode: {img.mode}")
except Exception as e:
    print("Error:", e)
