#!/usr/bin/env python3
"""
בונה את תפריט ראש השנה של מסעדת אלגריה משלושה נכסים:
  src/menu.html            — מקור העיצוב (פרגמנט: title + style + markup)
  assets/alegria-logo*.png — הלוגו שחולץ ממדריך המותג

תוצרים:
  index.html               — עמוד עצמאי לצפייה/שיתוף
  dist/artifact.html       — פרגמנט עם לוגו מוטמע (לפרסום כ-Artifact)
  dist/alegria-rosh-hashana-menu.pdf — A4 מוכן להדפסה
  dist/alegria-rosh-hashana-menu.png — תמונה לוואטסאפ/סושיאל
"""
import base64, pathlib, sys

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src" / "menu.html"
DIST = ROOT / "dist"
DIST.mkdir(exist_ok=True)

LOGO = ROOT / "assets" / "alegria-logo-web.png"
LOGO_URI = "data:image/png;base64," + base64.b64encode(LOGO.read_bytes()).decode()

fragment = SRC.read_text(encoding="utf-8")
inlined = fragment.replace('src="assets/alegria-logo-web.png"', f'src="{LOGO_URI}"')

# 1. פרגמנט ל-Artifact (לוגו מוטמע, ללא עטיפת html/head/body)
(DIST / "artifact.html").write_text(inlined, encoding="utf-8")

# 2. עמוד עצמאי
standalone = (
    '<!doctype html>\n<html lang="he" dir="rtl">\n<head>\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
    '<meta name="description" content="תפריט ראש השנה של מסעדת אלגריה, קרית גת — בשרים, דגים, תוספות וסלטים. להזמנות: 054-543-7528">\n'
    + inlined +
    '\n</body>\n</html>\n'
).replace("<title>", "<title>", 1)
# סוגרים את ה-head לפני ה-markup: ה-title/link/style באים ראשונים בפרגמנט
standalone = standalone.replace('<div class="stage">', '</head>\n<body>\n<div class="stage">', 1)
(ROOT / "index.html").write_text(standalone, encoding="utf-8")
print("built index.html + dist/artifact.html")

# 3. רינדור ל-PDF ו-PNG
if "--render" in sys.argv:
    from playwright.sync_api import sync_playwright
    url = (ROOT / "index.html").as_uri()
    pdf_out = DIST / "alegria-rosh-hashana-menu.pdf"
    png_out = DIST / "alegria-rosh-hashana-menu.png"
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
        # PDF — A4 מדויק
        pg = b.new_page()
        pg.goto(url, wait_until="networkidle")
        pg.emulate_media(media="print")
        pg.pdf(path=str(pdf_out), format="A4", print_background=True,
               margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
        pg.close()
        # PNG — הגיליון בלבד, ברזולוציה גבוהה
        pg = b.new_page(viewport={"width": 794, "height": 1123}, device_scale_factor=3)
        pg.goto(url, wait_until="networkidle")
        pg.locator(".sheet").screenshot(path=str(png_out))
        pg.close()
        b.close()
    print("rendered", pdf_out.name, "+", png_out.name)
