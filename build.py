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

def render_simanim():
    """בונה את רצועת סימני ראש השנה מתוך src/simanim.py."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("simanim", ROOT / "src" / "simanim.py")
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    cells = "\n".join(
        f'          <li class="siman">'
        f'<svg viewBox="0 0 48 48" aria-hidden="true">{path}</svg>'
        f'<span>{name}</span></li>'
        for name, path in mod.SIMANIM)
    return (
        '      <section class="simanim">\n'
        '        <h2 class="simanim__head">סימני ראש השנה <em>· לשנה טובה ומתוקה</em></h2>\n'
        '        <ul class="simanim__row">\n' + cells + '\n        </ul>\n'
        '      </section>')


FONT_DIR = ROOT / "assets" / "fonts"
# משקל -> מילת המפתח שמזהה את הקובץ בשם שעומר צופי מספק
WEIGHT_KEYS = {
    "Light": ("light",),
    "Regular": ("regular", "book"),
    "Medium": ("medium",),
    "Bold": ("bold",),
    "Black": ("black", "heavy"),
}
FONT_EXT = (".woff2", ".woff", ".ttf", ".otf")
MIME = {".woff2": "font/woff2", ".woff": "font/woff", ".ttf": "font/ttf", ".otf": "font/otf"}
FMT = {".woff2": "woff2", ".woff": "woff", ".ttf": "truetype", ".otf": "opentype"}


def _to_woff2(path):
    """ממיר ttf/otf ל-woff2 אם fonttools זמין. מחזיר (bytes, סיומת)."""
    if path.suffix.lower() == ".woff2":
        return path.read_bytes(), ".woff2"
    try:
        from fontTools.ttLib import TTFont
        import io
        f = TTFont(str(path))
        f.flavor = "woff2"
        buf = io.BytesIO()
        f.save(buf)
        return buf.getvalue(), ".woff2"
    except Exception as e:
        print(f"  ! לא הומר ל-woff2 ({path.name}): {e}")
        return path.read_bytes(), path.suffix.lower()


def find_font(weight_name):
    """מאתר את קובץ הפונט למשקל נתון, ללא תלות בשם המדויק שהגיע מהמעצב."""
    if not FONT_DIR.is_dir():
        return None
    keys = WEIGHT_KEYS[weight_name]
    cands = [f for f in FONT_DIR.iterdir()
             if f.suffix.lower() in FONT_EXT and any(k in f.stem.lower() for k in keys)]
    if not cands:
        return None
    # woff2 עדיף, ואחריו הקובץ הקטן ביותר
    cands.sort(key=lambda f: (f.suffix.lower() != ".woff2", f.stat().st_size))
    return cands[0]


def embed_fonts(html):
    """מטמיע את קבצי ברזיה כ-base64, או מסיר את בלוק ה-@font-face אם אין קבצים."""
    found = 0
    for weight in WEIGHT_KEYS:
        src = find_font(weight)
        placeholder = f'url("assets/fonts/Birzia-{weight}.woff2") format("woff2")'
        if src is None:
            continue
        data, ext = _to_woff2(src)
        uri = f"data:{MIME[ext]};base64," + base64.b64encode(data).decode()
        html = html.replace(placeholder, f'url("{uri}") format("{FMT[ext]}")')
        print(f"  ✓ {weight:<8} {src.name}  ({len(data)//1024} KB)")
        found += 1
    if found == 0:
        start = html.find('<style id="birzia-faces">')
        end = html.find("</style>", start)
        if start != -1 and end != -1:
            html = html[:start] + html[end + len("</style>") :].lstrip("\n")
        print("  – ברזיה לא נמצא ב-assets/fonts/ — נופל חזרה ל-Rubik/Assistant")
    return html


fragment = SRC.read_text(encoding="utf-8")
inlined = fragment.replace('src="assets/alegria-logo-web.png"', f'src="{LOGO_URI}"')
inlined = inlined.replace("<!--SIMANIM-->", render_simanim())
print("פונטים:")
inlined = embed_fonts(inlined)

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
        for fmt, out in (("A3", pdf_out), ("A4", pdf_out.with_name(pdf_out.stem + "-a4.pdf"))):
            pg.pdf(path=str(out), format=fmt, print_background=True,
                   margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
                   prefer_css_page_size=(fmt == "A3"))
            print("  rendered", out.name)
        pg.close()
        # PNG — הגיליון בלבד, ברזולוציה גבוהה
        pg = b.new_page(viewport={"width": 1123, "height": 1587}, device_scale_factor=2)
        pg.goto(url, wait_until="networkidle")
        pg.locator(".sheet").screenshot(path=str(png_out))
        pg.close()
        b.close()
    print("rendered", pdf_out.name, "+", png_out.name)
