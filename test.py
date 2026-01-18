# ===============================================
#       QUOTIVE 2025 — Professional Edition
#       Smart layout • Gradient • Branding
# ===============================================

from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import textwrap
import os
import random

# ================== CONFIG ==================
OUTPUT_FOLDER = r"E:\git-workstation\Quotive\Daily Quotes"
FONT_PATH = r"E:\git-workstation\Quotive\Fonts\Agbalumo-Regular.ttf"
IMAGE_SIZE = (1080, 720)

# ============= BACKGROUND COLORS ============
COLORS = [
    (30, 30, 30), (40, 60, 120), (60, 100, 60), (100, 50, 80),
    (200, 100, 40), (20, 100, 150), (45, 80, 150), (60, 179, 113),
    (123, 104, 238), (205, 92, 92), (72, 61, 139), (100, 149, 237),
    (139, 0, 139), (255, 105, 180), (70, 130, 180), (34, 139, 34)
]

# ============ VISUAL HELPERS ============

def vertical_gradient(size, top_color, bottom_color):
    base = Image.new("RGB", size, top_color)
    top = Image.new("RGB", size, bottom_color)
    mask = Image.linear_gradient("L").resize(size)
    return Image.composite(top, base, mask)

# =============== WELCOME ===================
print("\nQUOTIVE — Code Your Daily Motivation\n")
quote = input("Enter your quote: ").strip()
author = input("Author (optional): ").strip()

if not quote:
    print("Quote toh daalo bhai!")
    exit()

# ============= CREATE BACKGROUND ===========
bg_color_1 = random.choice(COLORS)
bg_color_2 = random.choice(COLORS)
img = vertical_gradient(IMAGE_SIZE, bg_color_1, bg_color_2)
draw = ImageDraw.Draw(img)

# ============== LOAD SMALL FONT ============
try:
    small_font = ImageFont.truetype(FONT_PATH, 32)
except:
    small_font = ImageFont.load_default()

# ========= SAFE AREA & PADDING ============
PADDING_H = 120
PADDING_V = 140

usable_w = IMAGE_SIZE[0] - 2 * PADDING_H
usable_h = IMAGE_SIZE[1] - 2 * PADDING_V

# ========= SMART AUTO-FIT FONT SIZE =========
for size in range(72, 44, -2):
    try:
        test_font = ImageFont.truetype(FONT_PATH, size)
    except:
        test_font = ImageFont.load_default()

    approx_char_width = size * 0.55
    WRAP_WIDTH = int(usable_w // approx_char_width)
    WRAP_WIDTH = max(25, min(WRAP_WIDTH, 70))

    wrapped_quote = textwrap.fill(quote, width=WRAP_WIDTH)
    bbox = draw.multiline_textbbox((0, 0), wrapped_quote, font=test_font)
    text_h = bbox[3] - bbox[1]

    if text_h <= usable_h:
        font = test_font
        main_font_size = size
        break

# ========= SMART LINE SPACING =========
LINE_SPACING = int(main_font_size * 0.35)

# ========= CALCULATE FINAL TEXT SIZE =========
bbox = draw.multiline_textbbox((0, 0), wrapped_quote, font=font, spacing=LINE_SPACING)
text_w = bbox[2] - bbox[0]
text_h = bbox[3] - bbox[1]

# ========= CENTER IN SAFE AREA =========
x = PADDING_H + (usable_w - text_w) // 2
y = PADDING_V + (usable_h - text_h) // 2 - 30

# ============= DRAW QUOTE =============
draw.multiline_text(
    (x, y),
    wrapped_quote,
    fill=(255, 255, 255),
    font=font,
    align="center",
    spacing=LINE_SPACING
)

# ============= DRAW AUTHOR ============
if author:
    author_text = f"— {author}"
    auth_bbox = draw.textbbox((0, 0), author_text, font=small_font)
    draw.text(
        (IMAGE_SIZE[0] // 2 - auth_bbox[2] // 2, y + text_h + 30),
        author_text,
        fill=(230, 230, 230),
        font=small_font
    )

# ============= DATE (Top Left) ==========
today_str = datetime.now().strftime("%d %b %Y")
draw.text((PADDING_H - 20, 50), today_str, fill=(200, 200, 200), font=small_font)

# ========= BRAND WATERMARK =========
brand_text = "Quotive • 2025"
brand_bbox = draw.textbbox((0, 0), brand_text, font=small_font)
draw.text(
    (IMAGE_SIZE[0] - brand_bbox[2] - 40, IMAGE_SIZE[1] - 60),
    brand_text,
    fill=(180, 180, 180),
    font=small_font
)

# ============ SAVE LOGIC ===============
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
today_date = datetime.now().strftime("%Y-%m-%d")
today_file = os.path.join(OUTPUT_FOLDER, f"{today_date}.png")
latest_file = os.path.join(OUTPUT_FOLDER, "latest.png")

# Remove old versions
for f in os.listdir(OUTPUT_FOLDER):
    if f.startswith(today_date) and "_v" in f:
        os.remove(os.path.join(OUTPUT_FOLDER, f))

# Rename previous latest
if os.path.exists(latest_file):
    mtime = os.path.getmtime(latest_file)
    old_date = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
    old_file = os.path.join(OUTPUT_FOLDER, f"{old_date}.png")
    if os.path.exists(old_file):
        os.remove(old_file)
    os.rename(latest_file, old_file)

# Save new images
img.save(latest_file)
img.save(today_file)

print("\nDone! Quote bilkul perfect bani hai!")
print(f"   → latest.png (updated)")
print(f"   → {today_date}.png (today's file)")
print(f"\nFolder: {OUTPUT_FOLDER}")
print("\nDo commit & push — Have a great day! 🚀")
