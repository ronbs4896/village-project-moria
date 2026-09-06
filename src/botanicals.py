# -*- coding: utf-8 -*-
"""מסגרת קישוט לראש השנה — רימונים, תפוחים, דבש, שיבולים ועלים. וקטור, viewBox 1080x1350."""

DEFS = '''
<defs>
  <filter id="drop" x="-30%" y="-30%" width="170%" height="170%">
    <feDropShadow dx="0" dy="5" stdDeviation="7" flood-color="#4A1A08" flood-opacity=".34"/>
  </filter>
  <filter id="blur6"><feGaussianBlur stdDeviation="6"/></filter>
  <filter id="grain" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="4" seed="7" result="n"/>
    <feColorMatrix in="n" type="saturate" values="0" result="g"/>
    <feComponentTransfer in="g"><feFuncA type="linear" slope=".5"/></feComponentTransfer>
  </filter>
  <filter id="stain" x="-20%" y="-20%" width="140%" height="140%">
    <feTurbulence type="fractalNoise" baseFrequency="0.007" numOctaves="3" seed="21" result="n"/>
    <feColorMatrix in="n" type="saturate" values="0"/>
    <feComponentTransfer><feFuncA type="linear" slope=".26"/></feComponentTransfer>
  </filter>

  <radialGradient id="pomB" cx=".33" cy=".26" r=".92">
    <stop offset="0"   stop-color="#F07660"/><stop offset=".22" stop-color="#D8412F"/>
    <stop offset=".58" stop-color="#A81E18"/><stop offset=".85" stop-color="#71100E"/>
    <stop offset="1"   stop-color="#4E0908"/>
  </radialGradient>
  <radialGradient id="pomRim" cx=".5" cy=".5" r=".5">
    <stop offset=".62" stop-color="#3A0605" stop-opacity="0"/>
    <stop offset="1"   stop-color="#3A0605" stop-opacity=".55"/>
  </radialGradient>
  <radialGradient id="pith" cx=".4" cy=".32" r=".8">
    <stop offset="0" stop-color="#FFF8E6"/><stop offset=".7" stop-color="#F0DCB2"/>
    <stop offset="1" stop-color="#D8BE8C"/>
  </radialGradient>
  <radialGradient id="seed" cx=".35" cy=".3" r=".8">
    <stop offset="0" stop-color="#F2635F"/><stop offset=".55" stop-color="#C81F28"/>
    <stop offset="1" stop-color="#8A0D16"/>
  </radialGradient>

  <radialGradient id="apB" cx=".32" cy=".26" r=".92">
    <stop offset="0"   stop-color="#F58070"/><stop offset=".24" stop-color="#DC4232"/>
    <stop offset=".62" stop-color="#AC2019"/><stop offset=".88" stop-color="#75110D"/>
    <stop offset="1"   stop-color="#530A08"/>
  </radialGradient>

  <linearGradient id="lfB" x1=".1" y1="0" x2=".9" y2="1">
    <stop offset="0" stop-color="#8FBA5E"/><stop offset=".45" stop-color="#54893A"/>
    <stop offset="1" stop-color="#264B1D"/>
  </linearGradient>

  <linearGradient id="glass" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#FFFDF4" stop-opacity=".92"/>
    <stop offset=".3" stop-color="#F4E9CE" stop-opacity=".55"/>
    <stop offset=".72" stop-color="#E9D8AE" stop-opacity=".6"/>
    <stop offset="1" stop-color="#FFFDF4" stop-opacity=".85"/>
  </linearGradient>
  <linearGradient id="honeyG" x1="0" y1="0" x2=".7" y2="1">
    <stop offset="0" stop-color="#FBD46B"/><stop offset=".4" stop-color="#E8A81F"/>
    <stop offset="1" stop-color="#A66B06"/>
  </linearGradient>
  <linearGradient id="woodG" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#B98246"/><stop offset=".5" stop-color="#8A5A24"/>
    <stop offset="1" stop-color="#6B4319"/>
  </linearGradient>
  <linearGradient id="whG" x1="0" y1="0" x2=".6" y2="1">
    <stop offset="0" stop-color="#F0D283"/><stop offset=".5" stop-color="#C89A2C"/>
    <stop offset="1" stop-color="#8E680F"/>
  </linearGradient>
  <linearGradient id="goldL" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#F7E4A6"/><stop offset=".4" stop-color="#C9A227"/>
    <stop offset=".6" stop-color="#F3DE9B"/><stop offset="1" stop-color="#9A7314"/>
  </linearGradient>
  <radialGradient id="parch" cx=".5" cy=".4" r=".8">
    <stop offset="0" stop-color="#FCF6E7"/><stop offset=".6" stop-color="#F6ECD5"/>
    <stop offset="1" stop-color="#EADBB9"/>
  </radialGradient>
</defs>'''

POM = '''<g filter="url(#drop)">
  <path d="M0-46c-31 0-50 22-50 53 0 33 22 57 50 57s50-24 50-57c0-31-19-53-50-53Z" fill="url(#pomB)"/>
  <path d="M0-46c-31 0-50 22-50 53 0 33 22 57 50 57s50-24 50-57c0-31-19-53-50-53Z" fill="url(#pomRim)"/>
  <path d="M0-44V-76" stroke="#5E2F0C" stroke-width="8" stroke-linecap="round" fill="none"/>
  <path d="m0-70-16-14M0-70l16-14M0-62l-23-9M0-62l23-9" stroke="#5E2F0C" stroke-width="6.5" stroke-linecap="round" fill="none"/>
  <ellipse cx="-19" cy="-9" rx="13" ry="21" fill="#FFF" opacity=".2" transform="rotate(-18 -19 -9)"/>
  <ellipse cx="-23" cy="-19" rx="6" ry="9" fill="#FFF" opacity=".42" transform="rotate(-18 -23 -19)"/>
</g>'''

POM_CUT = '''<g filter="url(#drop)">
  <circle r="52" fill="url(#pith)"/>
  <circle r="52" fill="none" stroke="url(#pomB)" stroke-width="7"/>
  <circle r="46" fill="none" stroke="#E6CDA0" stroke-width="2.5"/>
  <g fill="url(#seed)">
    <circle cx="-25" cy="-19" r="7.5"/><circle cx="-8" cy="-27" r="7.5"/><circle cx="10" cy="-24" r="7.5"/>
    <circle cx="25" cy="-13" r="7.5"/><circle cx="-31" cy="0" r="7.5"/><circle cx="-13" cy="-7" r="7.5"/>
    <circle cx="5" cy="-6" r="7.5"/><circle cx="22" cy="3" r="7.5"/><circle cx="-23" cy="17" r="7.5"/>
    <circle cx="-5" cy="12" r="7.5"/><circle cx="13" cy="20" r="7.5"/><circle cx="-14" cy="32" r="7"/>
    <circle cx="5" cy="35" r="7"/><circle cx="28" cy="22" r="7"/><circle cx="-34" cy="-32" r="6.5"/>
  </g>
  <g fill="#FFF" opacity=".5">
    <circle cx="-27" cy="-21" r="2.3"/><circle cx="7" cy="-8" r="2.3"/><circle cx="-7" cy="10" r="2.3"/>
    <circle cx="24" cy="1" r="2.3"/><circle cx="3" cy="33" r="2.3"/><circle cx="-10" cy="-29" r="2.3"/>
  </g>
</g>'''

APPLE = '''<g filter="url(#drop)">
  <path d="M0-28c-9-9-24-11-34-2-12 10-12 33-3 48 7 12 16 26 26 35a9 9 0 0 0 11 0c10-9 19-23 26-35 9-15 9-38-3-48-10-9-25-7-34 2Z" fill="url(#apB)"/>
  <path d="M0-28c-9-9-24-11-34-2-12 10-12 33-3 48 7 12 16 26 26 35a9 9 0 0 0 11 0c10-9 19-23 26-35 9-15 9-38-3-48-10-9-25-7-34 2Z" fill="url(#pomRim)" opacity=".8"/>
  <path d="M0-30v-20" stroke="#5E2F0C" stroke-width="6.5" stroke-linecap="round" fill="none"/>
  <path d="M3-44c8-12 21-16 32-14-2 12-13 21-25 21Z" fill="url(#lfB)"/>
  <path d="M5-42c8-6 17-10 26-11" stroke="#A9CE7C" stroke-width="2.5" fill="none" opacity=".7"/>
  <ellipse cx="-17" cy="-2" rx="9" ry="17" fill="#FFF" opacity=".22" transform="rotate(-14 -17 -2)"/>
  <ellipse cx="-20" cy="-12" rx="4.5" ry="7" fill="#FFF" opacity=".45"/>
</g>'''

LEAF = '''<g filter="url(#drop)">
  <path d="M0 0c24-33 60-41 88-34-4 32-34 54-66 54-12 0-19-9-22-20Z" fill="url(#lfB)"/>
  <path d="M2 0c28-10 56-18 84-27" stroke="#B7D897" stroke-width="3" fill="none" opacity=".6"/>
  <g stroke="#B7D897" stroke-width="1.8" fill="none" opacity=".45">
    <path d="M22-8c2-8 6-14 11-18"/><path d="M42-15c2-8 7-13 12-17"/><path d="M62-22c2-7 6-11 11-14"/>
  </g>
</g>'''

WHEAT = '''<g filter="url(#drop)">
  <path d="M0 0V-100" stroke="#9C7318" stroke-width="5.5" stroke-linecap="round" fill="none"/>
  <g fill="url(#whG)" stroke="#8A6410" stroke-width="1.2">
    <ellipse cx="-12" cy="-25" rx="8" ry="16" transform="rotate(-25 -12 -25)"/>
    <ellipse cx="12" cy="-31" rx="8" ry="16" transform="rotate(25 12 -31)"/>
    <ellipse cx="-12" cy="-48" rx="8" ry="16" transform="rotate(-25 -12 -48)"/>
    <ellipse cx="12" cy="-54" rx="8" ry="16" transform="rotate(25 12 -54)"/>
    <ellipse cx="-10" cy="-71" rx="7.5" ry="15" transform="rotate(-25 -10 -71)"/>
    <ellipse cx="10" cy="-77" rx="7.5" ry="15" transform="rotate(25 10 -77)"/>
    <ellipse cx="0" cy="-95" rx="7.5" ry="17"/>
  </g>
</g>'''

HONEY = '''<g filter="url(#drop)">
  <path d="M-44 20h88v32a16 16 0 0 1-16 16h-56a16 16 0 0 1-16-16Z" fill="url(#honeyG)"/>
  <path d="M-46-8h92v60a16 16 0 0 1-16 16h-60a16 16 0 0 1-16-16Z" fill="url(#glass)"/>
  <path d="M-46-8h92v60a16 16 0 0 1-16 16h-60a16 16 0 0 1-16-16Z" fill="none" stroke="#C79A34" stroke-width="3.5"/>
  <rect x="-53" y="-22" width="106" height="18" rx="9" fill="url(#goldL)"/>
  <rect x="-38" y="2" width="9" height="58" rx="4.5" fill="#FFF" opacity=".5"/>
  <path d="M36-78v58" stroke="url(#woodG)" stroke-width="8" stroke-linecap="round" fill="none"/>
  <g fill="url(#woodG)">
    <ellipse cx="36" cy="-60" rx="16" ry="6.5"/><ellipse cx="36" cy="-47" rx="16" ry="6.5"/><ellipse cx="36" cy="-34" rx="14" ry="6"/>
  </g>
  <path d="M36-28c0 14 7 18 7 30" stroke="url(#honeyG)" stroke-width="7.5" stroke-linecap="round" fill="none"/>
</g>'''

SWIRL = '''<g fill="none" stroke="url(#goldL)" stroke-linecap="round">
  <path d="M0 0c28-22 62-22 86-4 17 13 15 35-5 37-15 2-24-11-17-22 9-14 32-15 47-2" stroke-width="5"/>
  <path d="M14 14c22-14 46-13 63 0" stroke-width="3" opacity=".7"/>
</g>'''


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
            f'<rect width="{w}" height="{h}" fill="url(#parch)"/>'
            f'<rect width="{w}" height="{h}" filter="url(#stain)" opacity=".68" '
            f'style="mix-blend-mode:multiply"/>'
            f'<rect width="{w}" height="{h}" filter="url(#grain)" opacity=".2" '
            f'style="mix-blend-mode:multiply"/>'
            + "".join(p) + '</svg>')


if __name__ == "__main__":
    import pathlib, sys
    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "assets/banner-art.svg")
    out.write_text(frame_svg(), encoding="utf-8")
    print(out, len(out.read_text(encoding='utf-8')), "bytes")
