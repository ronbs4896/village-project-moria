#!/usr/bin/env python3
"""באנר המכירה של אלגריה — קריאייטיב למטא בשלושה יחסי מסך."""
import base64, pathlib, sys, importlib.util

ARGV = list(sys.argv)          # נשמר לפני שמייבאים את build.py

ROOT = pathlib.Path(__file__).parent
DIST = ROOT / "dist"; DIST.mkdir(exist_ok=True)

# מטמיע לוגו ופונטים דרך אותה לוגיקה של build.py
spec = importlib.util.spec_from_file_location("mb", ROOT / "build.py")
sys.argv = [sys.argv[0]]                       # build.py לא ירנדר בייבוא
mb = importlib.util.module_from_spec(spec); spec.loader.exec_module(mb)

LOGO = "data:image/png;base64," + base64.b64encode((ROOT/"assets"/"alegria-logo-web.png").read_bytes()).decode()
html = (ROOT/"src"/"banner.html").read_text(encoding="utf-8")
html = html.replace('src="assets/alegria-logo-web.png"', f'src="{LOGO}"')
print("פונטים:"); html = mb.embed_fonts(html)

(DIST/"banner-artifact.html").write_text(html, encoding="utf-8")
page = ('<!doctype html>\n<html lang="he" dir="rtl">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n' + html)
page = page.replace('<div class="stage">', '</head>\n<body>\n<div class="stage">', 1) + '\n</body>\n</html>\n'
(ROOT/"banner.html").write_text(page, encoding="utf-8")
print("built banner.html + dist/banner-artifact.html")

# --- יחסי המסך של מטא ---
# 1:1 לא נכלל: ב-1080x1080 המנות יורדות ל-13px, שזה ~5px על מסך טלפון.
FORMATS = [("4x5",  1080, 1350, "פיד — הפורמט הראשי", ""),
           ("9x16", 1080, 1920, "סטורי / ריל", """.top{padding:calc(var(--s)*26) calc(var(--s)*44)}
.top img{width:calc(var(--s)*152)}
.top__name{font-size:calc(var(--s)*52)}
.top__sub{font-size:calc(var(--s)*31)}
.hero{padding:calc(var(--s)*30) calc(var(--s)*40) calc(var(--s)*34)}
.hero__eyebrow{font-size:calc(var(--s)*42)}
.hero__title{font-size:calc(var(--s)*112)}
.hero__when{font-size:calc(var(--s)*34);padding:calc(var(--s)*14) calc(var(--s)*34)}
.goods{padding:calc(var(--s)*30);gap:calc(var(--s)*22);align-content:space-between}
.cat{padding:calc(var(--s)*22) calc(var(--s)*24)}
.cat__h{font-size:calc(var(--s)*46);margin-bottom:calc(var(--s)*16);padding-bottom:calc(var(--s)*12)}
.cat li{padding-block:calc(var(--s)*4)}
.cta{padding:calc(var(--s)*24) calc(var(--s)*40) calc(var(--s)*30)}
.cta__label{font-size:calc(var(--s)*36)}
.cta__phone a{font-size:calc(var(--s)*104)}
.cta__phone svg{width:calc(var(--s)*70);height:calc(var(--s)*70)}
.cta__addr{font-size:calc(var(--s)*32)}""")]

def render():
    from playwright.sync_api import sync_playwright
    url = (ROOT/"banner.html").as_uri()
    out = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
        for tag, w, h, label, extra in FORMATS:
            pg = b.new_page(viewport={"width": w + 80, "height": h + 200}, device_scale_factor=1)
            pg.goto(url, wait_until="networkidle")
            pg.add_style_tag(content=(
                f".stage{{padding:0;gap:0}} .frame{{width:{w}px}} "
                f".banner{{aspect-ratio:{w}/{h}}} " + extra))
            pg.wait_for_timeout(250)
            def measure():
                return pg.evaluate("""()=>{
                  const bad=[]; let total=0;
                  document.querySelectorAll('.cat').forEach(c=>{
                    const ul=c.querySelector('ul'), box=c.getBoundingClientRect();
                    const items=[...ul.children]; total+=items.length;
                    const vis=items.filter(li=>{const r=li.getBoundingClientRect();
                      return r.bottom<=box.bottom+1.5 && r.right<=box.right+1.5 && r.left>=box.left-1.5;});
                    if(vis.length<items.length)
                      bad.push(c.querySelector('.cat__h').textContent+' '+vis.length+'/'+items.length);
                  });
                  return {total, bad};}""")

            # מוצא את הגודל הגדול ביותר שבו כל המנות נכנסות
            chosen, fit = None, None
            for size in range(40, 15, -1):
                tag_handle = pg.add_style_tag(content=f".cat li{{font-size:calc(var(--s)*{size})}}")
                fit = measure()
                if not fit["bad"]:
                    chosen = size
                    break
                pg.evaluate("el=>el.remove()", tag_handle)
            if chosen is None:
                raise SystemExit(f"{tag}: אין גודל שבו כל המנות נכנסות")
            f = DIST / f"alegria-sale-banner-{tag}.png"
            pg.locator(".banner").screenshot(path=str(f))
            out.append((f.name, w, h, label, fit, chosen))
            pg.close()
        b.close()
    for name, w, h, label, fit, size in out:
        print(f"  {name:<32} {w}×{h}  {label:<20} ✓ כל {fit['total']} המנות · פריט {size}px")

if "--render" in ARGV:
    render()
