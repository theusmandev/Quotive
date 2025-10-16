from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import textwrap
import os
import random

# === CONFIG ===
OUTPUT_FOLDER = r"E:\git-workstation\Quotive\Daily Quotes"# ✅ Tumhara folder
FONT_PATH = r"E:\git-workstation\Quotive\Fonts\Roboto_Condensed-Black.ttf" # ✅ Tumhara font
IMAGE_SIZE = (1080, 720)

# === BACKGROUND COLORS ===
COLORS = [
    (30, 30, 30),
    (40, 60, 120),
    (60, 100, 60),
    (100, 50, 80),
    (200, 100, 40),
    (20, 100, 150),
    (45, 80, 150),
    (60, 179, 113),
    (123, 104, 238),
    (205, 92, 92),
    (72, 61, 139),
    (100, 149, 237),
]

# === STEP 1: Input ===
quote = input("Enter your quote of the day: ").strip()
author = input("Author (optional): ").strip()

if not quote:
    print("❌ Please enter a quote.")
    exit()

# === STEP 2: Auto font + wrap adjustment ===
quote_len = len(quote)

if quote_len < 120:
    FONT_SIZE = 64
    WRAP_WIDTH = 35
elif quote_len < 250:
    FONT_SIZE = 52
    WRAP_WIDTH = 45
elif quote_len < 400:
    FONT_SIZE = 44
    WRAP_WIDTH = 55
else:
    FONT_SIZE = 36
    WRAP_WIDTH = 65

# === STEP 3: Create image ===
bg_color = random.choice(COLORS)
img = Image.new("RGB", IMAGE_SIZE, color=bg_color)
draw = ImageDraw.Draw(img)

# === STEP 4: Load fonts ===
try:
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    small_font = ImageFont.truetype(FONT_PATH, 30)
except:
    print("⚠️ Font not found or invalid, using default font.")
    font = ImageFont.load_default()
    small_font = ImageFont.load_default()

# === STEP 5: Wrap text 
wrapped_text = textwrap.fill(quote, width=WRAP_WIDTH)
bbox = draw.multiline_textbbox((0, 0), wrapped_text, font=font)
text_w = bbox[2] - bbox[0]
text_h = bbox[3] - bbox[1]

# Center horizontally & vertically
x = (IMAGE_SIZE[0] - text_w) / 2
y = (IMAGE_SIZE[1] - text_h) / 2 - 20  # thoda upar shift for author space

# === STEP 6: Draw quote ===
draw.multiline_text((x, y), wrapped_text, fill=(255, 255, 255), font=font, align="center")

# === STEP 7: Author below quote ===
if author:
    author_text = f"– {author}"
    author_bbox = draw.textbbox((0, 0), author_text, font=small_font)
    author_w = author_bbox[2] - author_bbox[0]
    author_x = (IMAGE_SIZE[0] - author_w) / 2
    author_y = y + text_h + 30
    draw.text((author_x, author_y), author_text, fill=(220, 220, 220), font=small_font)

# === STEP 8: Date top-left ===
today = datetime.now().strftime("%d %b %Y")
draw.text((30, 30), today, fill=(200, 200, 200), font=small_font)

# === STEP 9: GitHub link bottom-center ===
github_link = "https://github.com/theusmandev"
link_bbox = draw.textbbox((0, 0), github_link, font=small_font)
link_w = link_bbox[2] - link_bbox[0]
link_x = (IMAGE_SIZE[0] - link_w) / 2
link_y = IMAGE_SIZE[1] - 60
draw.text((link_x, link_y), github_link, fill=(200, 200, 200), font=small_font)

# === STEP 10: Save image ===
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
filename = f"{datetime.now().strftime('%Y-%m-%d')}.png"
filepath = os.path.join(OUTPUT_FOLDER, filename)
img.save(filepath)

print(f"\n✅ Quote saved successfully as: {filepath}")
print("Now you can commit and push manually to GitHub.")
