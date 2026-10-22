"""Wrap Platane/snk SVGs in a framed panel that matches the header and footer.

Usage: python frame_snake.py dist/github-contribution-grid-snake.svg dist/github-contribution-grid-snake-dark.svg
Files whose name contains "dark" get the dark panel; the rest get the light one.
"""
import re
import sys

PAD = 24  # space between the contribution grid and the frame
CORNER = 18  # length of the gold corner brackets

THEMES = {
    "dark": {"bg_top": "#0D1117", "bg_bottom": "#0A1410", "inner": "#10B981", "inner_opacity": "0.16"},
    "light": {"bg_top": "#FFFFFF", "bg_bottom": "#F0FDF4", "inner": "#10B981", "inner_opacity": "0.28"},
}


def frame(svg: str, theme: dict) -> str:
    if 'id="snkFrameBorder"' in svg:
        return svg  # already framed

    open_tag = re.match(r"<svg[^>]*>", svg).group(0)
    x, y, w, h = (float(v) for v in re.search(r'viewBox="([^"]+)"', open_tag).group(1).split())
    x, y, w, h = x - PAD, y - PAD, w + 2 * PAD, h + 2 * PAD

    new_open = re.sub(r'viewBox="[^"]+"', f'viewBox="{x:g} {y:g} {w:g} {h:g}"', open_tag)
    new_open = re.sub(r'width="[^"]+"', f'width="{w:g}"', new_open, count=1)
    new_open = re.sub(r'height="[^"]+"', f'height="{h:g}"', new_open, count=1)

    # outer panel sits 2 units inside the edge so the stroke is not clipped
    ox, oy, ow, oh = x + 2, y + 2, w - 4, h - 4
    ix, iy, iw, ih = x + 9, y + 9, w - 18, h - 18
    c = CORNER
    corners = " ".join([
        f"M{ox + 6:g},{oy + 6 + c:g} V{oy + 6:g} H{ox + 6 + c:g}",
        f"M{ox + ow - 6 - c:g},{oy + 6:g} H{ox + ow - 6:g} V{oy + 6 + c:g}",
        f"M{ox + 6:g},{oy + oh - 6 - c:g} V{oy + oh - 6:g} H{ox + 6 + c:g}",
        f"M{ox + ow - 6 - c:g},{oy + oh - 6:g} H{ox + ow - 6:g} V{oy + oh - 6 - c:g}",
    ])

    background = (
        "<defs>"
        '<linearGradient id="snkFrameBg" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{theme["bg_top"]}"/><stop offset="1" stop-color="{theme["bg_bottom"]}"/>'
        "</linearGradient>"
        '<linearGradient id="snkFrameBorder" x1="0" y1="0" x2="1" y2="0">'
        '<stop offset="0" stop-color="#0F766E"/><stop offset="0.35" stop-color="#10B981"/>'
        '<stop offset="0.5" stop-color="#F59E0B"/><stop offset="0.65" stop-color="#10B981"/>'
        '<stop offset="1" stop-color="#0F766E"/>'
        "</linearGradient>"
        "</defs>"
        f'<rect x="{ox:g}" y="{oy:g}" width="{ow:g}" height="{oh:g}" rx="14" fill="url(#snkFrameBg)"/>'
    )
    border = (
        f'<rect x="{ix:g}" y="{iy:g}" width="{iw:g}" height="{ih:g}" rx="10" fill="none" '
        f'stroke="{theme["inner"]}" stroke-opacity="{theme["inner_opacity"]}" stroke-width="1"/>'
        f'<rect x="{ox:g}" y="{oy:g}" width="{ow:g}" height="{oh:g}" rx="14" fill="none" '
        'stroke="url(#snkFrameBorder)" stroke-width="1.6"/>'
        f'<path d="{corners}" fill="none" stroke="#F59E0B" stroke-width="1.6" stroke-opacity="0.85"/>'
    )

    body = svg[len(open_tag):]
    body = body[: body.rindex("</svg>")]
    return new_open + background + body + border + "</svg>"


for path in sys.argv[1:]:
    theme = THEMES["dark" if "dark" in path else "light"]
    with open(path, encoding="utf-8") as f:
        svg = f.read()
    with open(path, "w", encoding="utf-8") as f:
        f.write(frame(svg, theme))
    print(f"framed {path}")
