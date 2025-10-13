# Quotive — Code Your Daily Motivation

“Consistency isn’t about doing big things. It’s about doing small things every day — without fail.”

##  What is Quotive?

Quotive is not just a Python script. It’s a **habit machine** for coders.

Every day, it transforms your favorite quote into a beautifully styled image — **automatically**. You simply enter a quote and (optionally) an author, and Quotive handles the rest. It designs the image, saves it with the current date, and waits for you to push it to GitHub — keeping your commit streak alive while keeping your mind inspired. ⚡

##  Why I Built It

There was a time I struggled with consistency. Some days I’d code for hours, other days I’d skip entirely. So I asked myself:

*“What if I made something simple that keeps me showing up every single day?”*

That’s how Quotive was born. It’s my way of blending **motivation**, **design**, and **discipline** into a small daily ritual. One quote. One commit. Every day. 🔁

##  Features That Keep You Going

-  **Random Backgrounds** – Each quote gets a fresh color palette.
-  **Smart Font Sizing** – Auto-adjusts based on quote length.
-  **Date + Author Display** – Feels like a personal journal.
-  **Auto File Save** – Every image is timestamped by date.
-  **Your GitHub Link** – Because your code deserves a signature.

##  Project Structure

```
Quotive/
│
├── main.py               # The heart of the project 
│
├── Fonts/                # Your font files (e.g., Roboto_Condensed-Black.ttf)
│
└── Daily Quotes/         # Generated images (auto-created every day)
```

##  How to Use

1. **Clone this repo**

   ```bash
   git clone https://github.com/theusmandev/Quotive.git
   ```

2. **Install Pillow**

   ```bash
   pip install pillow
   ```

3. **Run the script**

   ```bash
   python main.py
   ```

4. **Enter your daily quote**

   Quotive will create a clean, centered image with your quote and save it in the `Daily Quotes` folder.

5. **Commit & Push**

   ```bash
   git add .
   git commit -m " Added today's quote"
   git push
   ```

6. ** Congratulations** — your GitHub streak just got stronger, and your mind just got inspired!

##  Example Output

![Daily Quote Example](Daily%20Quotes/2025-10-13.png)

##  My Philosophy

*“If you can’t make big moves every day, take small steps — but never stop moving forward.”*

Quotive is more than code. It’s a reminder that **progress is built one commit at a time**. Each quote you post is proof that you showed up. And sometimes, that’s all that matters. 

##  Author

Created by: **@theusmandev**

Made with , ☕, and a love for simple ideas that spark consistency.

##  If you like Quotive...

Leave a ⭐ on the repo — not for me, but to remind *yourself* that you showed up today.
