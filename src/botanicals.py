# -*- coding: utf-8 -*-
"""מסגרת קישוט לראש השנה — רימונים, תפוחים, דבש, שיבולים ועלים. וקטור, viewBox 1080x1350."""

DEFS = '''
<defs>
  <linearGradient id="pg" x1="0" y1="0" x2=".4" y2="1">
    <stop offset="0" stop-color="#D9483A"/><stop offset=".5" stop-color="#B02A22"/><stop offset="1" stop-color="#6E100F"/>
  </linearGradient>
  <linearGradient id="pgc" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#F6E7C8"/><stop offset="1" stop-color="#E4CFA4"/>
  </linearGradient>
  <linearGradient id="ap" x1=".2" y1="0" x2=".8" y2="1">
    <stop offset="0" stop-color="#E0564A"/><stop offset=".55" stop-color="#B92B22"/><stop offset="1" stop-color="#7C130F"/>
  </linearGradient>
  <linearGradient id="lf" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#6E9A4A"/><stop offset="1" stop-color="#2F5623"/>
  </linearGradient>
  <linearGradient id="hy" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#F3BE45"/><stop offset="1" stop-color="#C07E09"/>
  </linearGradient>
  <linearGradient id="wh" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#E3B95A"/><stop offset="1" stop-color="#A57C1B"/>
  </linearGradient>
  <radialGradient id="parch" cx=".5" cy=".42" r=".78">
    <stop offset="0" stop-color="#FBF4E2"/><stop offset=".62" stop-color="#F5EAD0"/><stop offset="1" stop-color="#E9D9B4"/>
  </radialGradient>
</defs>'''

# ── יחידות בסיס, כל אחת סביב (0,0) ──
POM = '''<g>
  <path d="M0-52c-6-9-16-13-25-12 2 10 10 17 19 19" fill="#7C4A12"/>
  <path d="M0-46c-30 0-49 22-49 52 0 32 22 56 49 56s49-24 49-56c0-30-19-52-49-52Z" fill="url(#pg)"/>
  <path d="M0-46V-72" stroke="#6E3C10" stroke-width="7" stroke-linecap="round" fill="none"/>
  <path d="m0-66-15-13M0-66l15-13M0-59l-21-8M0-59l21-8" stroke="#6E3C10" stroke-width="6" stroke-linecap="round" fill="none"/>
  <ellipse cx="-17" cy="-6" rx="12" ry="18" fill="#E8705E" opacity=".33"/>
</g>'''

POM_CUT = '''<g>
  <circle r="52" fill="url(#pgc)"/>
  <circle r="52" fill="none" stroke="#B02A22" stroke-width="5"/>
  <g fill="#C6202A">
    <circle cx="-24" cy="-18" r="7"/><circle cx="-8" cy="-26" r="7"/><circle cx="9" cy="-23" r="7"/>
    <circle cx="24" cy="-13" r="7"/><circle cx="-30" cy="0" r="7"/><circle cx="-13" cy="-7" r="7"/>
    <circle cx="4" cy="-6" r="7"/><circle cx="21" cy="3" r="7"/><circle cx="-22" cy="16" r="7"/>
    <circle cx="-5" cy="11" r="7"/><circle cx="12" cy="19" r="7"/><circle cx="-14" cy="31" r="7"/>
    <circle cx="4" cy="34" r="7"/><circle cx="27" cy="21" r="7"/><circle cx="-33" cy="-32" r="6"/>
  </g>
  <g fill="#F07A6E" opacity=".55">
    <circle cx="-26" cy="-20" r="2.4"/><circle cx="6" cy="-8" r="2.4"/><circle cx="-7" cy="9" r="2.4"/>
    <circle cx="23" cy="1" r="2.4"/><circle cx="2" cy="32" r="2.4"/>
  </g>
</g>'''

APPLE = '''<g>
  <path d="M0-30c-8-8-22-10-31-2-11 9-11 30-3 44 6 11 15 24 24 32a8 8 0 0 0 10 0c9-8 18-21 24-32 8-14 8-35-3-44-9-8-23-6-31 2Z" fill="url(#ap)"/>
  <path d="M0-30v-18" stroke="#6E3C10" stroke-width="6" stroke-linecap="round" fill="none"/>
  <path d="M2-42c7-11 19-15 29-13-1 11-11 19-23 19" fill="url(#lf)"/>
  <ellipse cx="-16" cy="0" rx="8" ry="15" fill="#F0897A" opacity=".35"/>
</g>'''

LEAF = '''<g>
  <path d="M0 0c22-30 56-38 82-32-4 30-32 50-62 50-11 0-17-8-20-18Z" fill="url(#lf)"/>
  <path d="M0 0c26-9 52-16 78-25" stroke="#8FB367" stroke-width="3.5" fill="none" opacity=".75"/>
</g>'''

WHEAT = '''<g>
  <path d="M0 0V-96" stroke="#A57C1B" stroke-width="5" stroke-linecap="round" fill="none"/>
  <g fill="url(#wh)">
    <ellipse cx="-11" cy="-24" rx="7.5" ry="15" transform="rotate(-24 -11 -24)"/>
    <ellipse cx="11" cy="-30" rx="7.5" ry="15" transform="rotate(24 11 -30)"/>
    <ellipse cx="-11" cy="-46" rx="7.5" ry="15" transform="rotate(-24 -11 -46)"/>
    <ellipse cx="11" cy="-52" rx="7.5" ry="15" transform="rotate(24 11 -52)"/>
    <ellipse cx="-9" cy="-68" rx="7" ry="14" transform="rotate(-24 -9 -68)"/>
    <ellipse cx="9" cy="-74" rx="7" ry="14" transform="rotate(24 9 -74)"/>
    <ellipse cx="0" cy="-92" rx="7" ry="16"/>
  </g>
</g>'''

HONEY = '''<g>
  <path d="M-46 -6h92v58a16 16 0 0 1-16 16h-60a16 16 0 0 1-16-16Z" fill="#F7E7BE" opacity=".75"/>
  <path d="M-42 22h84v30a14 14 0 0 1-14 14h-56a14 14 0 0 1-14-14Z" fill="url(#hy)"/>
  <rect x="-52" y="-18" width="104" height="16" rx="8" fill="#B98A22"/>
  <path d="M-46 -6h92v58a16 16 0 0 1-16 16h-60a16 16 0 0 1-16-16Z" fill="none" stroke="#C79A34" stroke-width="4"/>
  <path d="M34-72v54" stroke="#8A5C18" stroke-width="7" stroke-linecap="round" fill="none"/>
  <g fill="#C9911C">
    <ellipse cx="34" cy="-56" rx="15" ry="6"/><ellipse cx="34" cy="-44" rx="15" ry="6"/><ellipse cx="34" cy="-32" rx="13" ry="6"/>
  </g>
  <path d="M34-26c0 12 6 16 6 26" stroke="url(#hy)" stroke-width="7" stroke-linecap="round" fill="none"/>
</g>'''

SWIRL = '''<path d="M0 0c26-20 58-20 80-4 16 12 14 32-4 34-14 2-22-10-16-20 8-13 30-14 44-2"
      fill="none" stroke="#C9A227" stroke-width="4.5" stroke-linecap="round" opacity=".85"/>'''


def _u(body, x, y, s=1.0, r=0.0, op=1.0):
    return (f'<g transform="translate({x} {y}) rotate({r}) scale({s})"'
            + (f' opacity="{op}"' if op != 1 else "") + f'>{body}</g>')


def frame_svg(w=1080, h=1350):
    """אשכול בפינה שמאלית עליונה + זר תחתון. הימין העליון נשאר פנוי לכותרת."""
    p = []

    # ── אשכול שמאלי עליון ──
    p += [
        _u(LEAF, 8, 150, 1.5, 200), _u(LEAF, 48, 34, 1.3, 262), _u(LEAF, 214, 268, 1.1, 158),
        _u(WHEAT, 236, 322, 1.25, 26), _u(WHEAT, 22, 330, 1.05, -16),
        _u(POM, 78, 116, 1.45), _u(POM_CUT, 232, 176, 1.05), _u(POM, 18, 292, .95),
        _u(HONEY, 186, 66, 1.0), _u(LEAF, 264, 92, .95, 322),
        _u(SWIRL, 292, 318, .85, 10, .75),
    ]

    # ── פינה ימנית עליונה: קישוט קל בלבד, מעל הכותרת ──
    p += [_u(SWIRL, w - 34, 16, -.62, 0, .55), _u(LEAF, w - 6, 22, .8, 338)]

    # ── זר תחתון: יושב על שפת הגיליון, הכרטיסים מכסים אותו חלקית ──
    y = h - 14
    row = [(70, POM, 1.0), (170, APPLE, .95), (262, POM_CUT, .85), (352, APPLE, .88),
           (452, POM, .95), (556, APPLE, 1.0), (654, POM_CUT, .82), (742, APPLE, .9),
           (840, POM, .98), (944, APPLE, .92), (1032, POM_CUT, .8)]
    for x, shape, s in row:
        p.append(_u(shape, x, y, s))
    for x, s, r in [(120, .85, -14), (312, .8, 12), (508, .85, -8), (700, .8, 14), (898, .85, -12)]:
        p.append(_u(WHEAT, x, y + 22, s, r))
    for x, s, r in [(30, 1.1, 196), (222, .95, 176), (410, 1.0, 200), (612, .95, 178),
                    (800, 1.0, 198), (990, .95, 176)]:
        p.append(_u(LEAF, x, y - 46, s, r))
    p.append(_u(HONEY, w - 62, y - 26, .92))
    p.append(_u(SWIRL, 640, h - 8, .9, 0, .5))

    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'width="{w}" height="{h}" preserveAspectRatio="xMidYMid slice">{DEFS}'
            f'<rect width="{w}" height="{h}" fill="url(#parch)"/>' + "".join(p) + '</svg>')


if __name__ == "__main__":
    import pathlib, sys
    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "assets/banner-art.svg")
    out.write_text(frame_svg(), encoding="utf-8")
    print(out, len(out.read_text(encoding='utf-8')), "bytes")
