# ===============================================
#       QUOTIVE 2025 — Professional Edition
#       No more text touching edges! 
# ===============================================

from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import textwrap
import os
import random

# ================== CONFIG ==================
OUTPUT_FOLDER = r"E:\git-workstation\Quotive\Daily Quotes"   # Apna folder yahan daalo
FONT_PATH = r"E:\git-workstation\Quotive\Fonts\Agbalumo-Regular.ttf"  # Apna font
IMAGE_SIZE = (1080, 720)

# ============= BACKGROUND COLORS ============
COLORS = [
    (30, 30, 30), (40, 60, 120), (60, 100, 60), (100, 50, 80),
    (200, 100, 40), (20, 100, 150), (45, 80, 150), (60, 179, 113),
    (123, 104, 238), (205, 92, 92), (72, 61, 139), (100, 149, 237),
    (139, 0, 139), (255, 105, 180), (70, 130, 180), (34, 139, 34)
]

# =============== WELCOME ===================
print("\nQUOTIVE — Code Your Daily Motivation\n")
quote = input("Enter your quote: ").strip()
author = input("Author (optional): ").strip()

if not quote:
    print("Quote toh daalo bhai!")
    exit()

# ============= CREATE IMAGE ================
bg_color = random.choice(COLORS)
img = Image.new("RGB", IMAGE_SIZE, color=bg_color)
draw = ImageDraw.Draw(img)

# ============== LOAD FONTS ================
try:
    main_font_size = 68
    font = ImageFont.truetype(FONT_PATH, main_font_size)
    small_font = ImageFont.truetype(FONT_PATH, 32)
except:
    print("Font nahi mila, default use kar raha hoon...")
    font = ImageFont.load_default()
    small_font = ImageFont.load_default()

# ========= SAFE AREA & PADDING ============
PADDING_H = 120      # Left & Right safe margin
PADDING_V = 140      # Top & Bottom safe margin (date + github ke liye)

usable_w = IMAGE_SIZE[0] - 2 * PADDING_H
usable_h = IMAGE_SIZE[1] - 2 * PADDING_V

# ====== DYNAMIC FONT SIZE (Optional Pro Touch) ======
quote_len = len(quote)
if quote_len > 300:
    main_font_size = 48
elif quote_len > 200:
    main_font_size = 56
elif quote_len > 120:
    main_font_size = 62

try:
    font = ImageFont.truetype(FONT_PATH, main_font_size)
except:
    pass

# ========= DYNAMIC WRAP WIDTH =========
approx_char_width = main_font_size * 0.55
WRAP_WIDTH = int(usable_w // approx_char_width)
WRAP_WIDTH = max(25, min(WRAP_WIDTH, 70))  # Safe limits

wrapped_quote = textwrap.fill(quote, width=WRAP_WIDTH)

# ========= CALCULATE TEXT SIZE =========
bbox = draw.multiline_textbbox((0, 0), wrapped_quote, font=font)
text_w = bbox[2] - bbox[0]
text_h = bbox[3] - bbox[1]

# ========= CENTER IN SAFE AREA =========
x = PADDING_H + (usable_w - text_w) // 2
y = PADDING_V + (usable_h - text_h) // 2 - 40  # Thoda upar author ke liye jagah

# ============= DRAW QUOTE =============
draw.multiline_text(
    (x, y),
    wrapped_quote,
    fill=(255, 255, 255),
    font=font,
    align="center"
)

# ============= DRAW AUTHOR ============
if author:
    author_text = f"— {author}"
    auth_bbox = draw.textbbox((0, 0), author_text, font=small_font)
    auth_w = auth_bbox[2] - auth_bbox[0]
    draw.text(
        (IMAGE_SIZE[0]//2 - auth_w//2, y + text_h + 30),
        author_text,
        fill=(230, 230, 230),
        font=small_font
    )

# ============= DATE (Top-Left) ==========
today_str = datetime.now().strftime("%d %b %Y")
draw.text((PADDING_H - 20, 50), today_str, fill=(200, 200, 200), font=small_font)

# ========= GITHUB LINK (Bottom) =========
github = "https://github.com/theusmandev"
link_bbox = draw.textbbox((0, 0), github, font=small_font)
link_w = link_bbox[2] - link_bbox[0]
draw.text(
    (IMAGE_SIZE[0]//2 - link_w//2, IMAGE_SIZE[1] - 90),
    github,
    fill=(200, 200, 200),
    font=small_font
)

# ============ SAVE LOGIC ===============
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
today_date = datetime.now().strftime("%Y-%m-%d")
today_file = os.path.join(OUTPUT_FOLDER, f"{today_date}.png")
latest_file = os.path.join(OUTPUT_FOLDER, "latest.png")

# Remove old versions like 2025-11-26_v2.png
for f in os.listdir(OUTPUT_FOLDER):
    if f.startswith(today_date) and "_v" in f:
        os.remove(os.path.join(OUTPUT_FOLDER, f))

# Rename previous latest.png to its date
if os.path.exists(latest_file):
    mtime = os.path.getmtime(latest_file)
    old_date = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
    old_file = os.path.join(OUTPUT_FOLDER, f"{old_date}.png")
    if os.path.exists(old_file):
        os.remove(old_file)
    os.rename(latest_file, old_file)

# Save new files
img.save(latest_file)
img.save(today_file)

print("\nDone! Quote bilkul perfect bani hai!")
print(f"   → latest.png (updated)")
print(f"   → {today_date}.png (today's file)")
print(f"\nFolder: {OUTPUT_FOLDER}")
print("\nDo commit&push - Have a Good Day!")













