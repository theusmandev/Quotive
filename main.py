
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, timedelta
import textwrap
import os
import random

# === CONFIG ===
OUTPUT_FOLDER = r"E:\git-workstation\Quotive\Daily Quotes" # Your folder path
FONT_PATH = r"E:\git-workstation\Quotive\Fonts\Agbalumo-Regular.ttf"# Your font
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

# === STEP 1: INPUT ===
print("\n🪶 Welcome to Quotive — Code Your Daily Motivation 🌤️\n")

quote = input("Enter your quote of the day: ").strip()
author = input("Author (optional): ").strip()

if not quote:
    print("Please enter a quote to continue.")
    exit()

# === STEP 2: AUTO FONT SIZE & WRAP WIDTH ===
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

# === STEP 3: CREATE IMAGE ===
bg_color = random.choice(COLORS)
img = Image.new("RGB", IMAGE_SIZE, color=bg_color)
draw = ImageDraw.Draw(img)

# === STEP 4: LOAD FONTS ===
try:
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    small_font = ImageFont.truetype(FONT_PATH, 30)
except:
    print("⚠️ Font not found or invalid, using default font.")
    font = ImageFont.load_default()
    small_font = ImageFont.load_default()

# === STEP 5: WRAP TEXT ===
wrapped_text = textwrap.fill(quote, width=WRAP_WIDTH)
bbox = draw.multiline_textbbox((0, 0), wrapped_text, font=font)
text_w = bbox[2] - bbox[0]
text_h = bbox[3] - bbox[1]

# Center horizontally & vertically
x = (IMAGE_SIZE[0] - text_w) / 2
y = (IMAGE_SIZE[1] - text_h) / 2 - 20  # a little upward for author space

# === STEP 6: DRAW QUOTE ===
draw.multiline_text((x, y), wrapped_text, fill=(255, 255, 255), font=font, align="center")

# === STEP 7: AUTHOR BELOW QUOTE ===
if author:
    author_text = f"– {author}"
    author_bbox = draw.textbbox((0, 0), author_text, font=small_font)
    author_w = author_bbox[2] - author_bbox[0]
    author_x = (IMAGE_SIZE[0] - author_w) / 2
    author_y = y + text_h + 30
    draw.text((author_x, author_y), author_text, fill=(220, 220, 220), font=small_font)

# === STEP 8: DATE TOP-LEFT ===
today_str = datetime.now().strftime("%d %b %Y")
draw.text((30, 30), today_str, fill=(200, 200, 200), font=small_font)

# === STEP 9: GITHUB LINK BOTTOM-CENTER ===
github_link = "https://github.com/theusmandev"
link_bbox = draw.textbbox((0, 0), github_link, font=small_font)
link_w = link_bbox[2] - link_bbox[0]
link_x = (IMAGE_SIZE[0] - link_w) / 2
link_y = IMAGE_SIZE[1] - 60
draw.text((link_x, link_y), github_link, fill=(200, 200, 200), font=small_font)

# === STEP 10: SAVE IMAGES ===
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# CLEAN UP OLD VERSION FILES FOR TODAY
today_date = datetime.now().strftime("%Y-%m-%d")
today_filename = f"{today_date}.png"
today_path = os.path.join(OUTPUT_FOLDER, today_filename)

# Delete any existing version files for today (2025-10-19_v2.png, etc.)
version_pattern = f"{today_date}_v*.png"
for file in os.listdir(OUTPUT_FOLDER):
    if file.startswith(today_date) and file.endswith('.png') and '_' in file and file != today_filename:
        try:
            os.remove(os.path.join(OUTPUT_FOLDER, file))
            print(f"Removed old version: {file}")
        except:
            pass

# 1️⃣ Handle old latest.png → rename to its date
latest_path = os.path.join(OUTPUT_FOLDER, "latest.png")
if os.path.exists(latest_path):
    # Get modification time to determine which date it belongs to
    mtime = os.path.getmtime(latest_path)
    old_date = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
    old_filename = f"{old_date}.png"
    old_path = os.path.join(OUTPUT_FOLDER, old_filename)

    # If file already exists for that date, delete it first
    if os.path.exists(old_path):
        os.remove(old_path)
        print(f" Removed existing {old_filename} to avoid duplicates")

    # Rename latest.png to its date
    os.rename(latest_path, old_path)
    print(f"Renamed previous latest.png → {old_filename}")

#  Save new latest.png
latest_path = os.path.join(OUTPUT_FOLDER, "latest.png")
img.save(latest_path)
print("Saved new latest.png")

#  Save today's date file (overwrite if exists)
# Remove existing today file if it exists
if os.path.exists(today_path):
    os.remove(today_path)
    print(f"Overwrote existing {today_filename}")

img.save(today_path)
print(f"Saved today's quote as: {today_filename}")

print("\nAll done! Images saved successfully.")
print("Only ONE file per date: YYYY-MM-DD.png")
print("latest.png is updated with today's quote")
print("Files are ready in:", OUTPUT_FOLDER)
print("Keep coding. Keep showing up.")