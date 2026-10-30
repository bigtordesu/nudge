"""Draws Nudge's app icons: the little buddy on a violet gradient.

Usage: python tools/make_icons.py <output-folder>
"""
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

S = 2048  # draw large, then downsample for smooth edges
OUT = Path(sys.argv[1] if len(sys.argv) > 1 else ".")


def lerp(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(len(a)))


def background():
    top, bottom = (164, 150, 255), (86, 64, 220)
    n = int(S * 1.5)
    col = Image.new("RGB", (1, 512))
    for y in range(512):
        col.putpixel((0, y), lerp(top, bottom, y / 511))
    g = col.resize((n, n), Image.BILINEAR).rotate(28, resample=Image.BICUBIC)
    off = (n - S) // 2
    return g.crop((off, off, off + S, off + S)).convert("RGBA")


def ellipse(cx, cy, rx, ry):
    return (cx - rx, cy - ry, cx + rx, cy + ry)


def soft_layer(draw_fn, blur):
    layer = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    draw_fn(ImageDraw.Draw(layer))
    return layer.filter(ImageFilter.GaussianBlur(blur))


def star(cx, cy, r, inner=0.3):
    pts = []
    for i in range(8):
        rad = r if i % 2 == 0 else r * inner
        a = math.radians(-90 + i * 45)
        pts.append((cx + rad * math.cos(a), cy + rad * math.sin(a)))
    return pts


def draw_icon():
    img = background()
    cx, cy = S * 0.5, S * 0.53
    rx, ry = S * 0.30, S * 0.29

    # glow in the top-left corner
    img.alpha_composite(soft_layer(lambda d: d.ellipse(ellipse(S * 0.18, S * 0.12, S * 0.42, S * 0.32), fill=(255, 255, 255, 46)), S * 0.15))
    # shadow under the buddy
    img.alpha_composite(soft_layer(lambda d: d.ellipse(ellipse(cx, cy + S * 0.05, rx * 0.95, ry * 0.9), fill=(40, 20, 120, 110)), S * 0.035))

    # body with a gentle top-to-bottom shade
    body = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    shade = Image.new("RGBA", (1, 256))
    for y in range(256):
        shade.putpixel((0, y), lerp((255, 255, 255, 255), (232, 226, 255, 255), y / 255))
    body_fill = shade.resize((S, S), Image.BILINEAR)
    mask = Image.new("L", (S, S), 0)
    ImageDraw.Draw(mask).ellipse(ellipse(cx, cy, rx, ry), fill=255)
    body.paste(body_fill, (0, 0), mask)
    img.alpha_composite(body)

    d = ImageDraw.Draw(img)
    ink = (30, 27, 46, 255)
    # eyes + highlights
    for sx in (-1, 1):
        ex, ey = cx + sx * S * 0.105, cy - S * 0.03
        d.ellipse(ellipse(ex, ey, S * 0.042, S * 0.056), fill=ink)
        d.ellipse(ellipse(ex + S * 0.015, ey - S * 0.021, S * 0.015, S * 0.015), fill=(255, 255, 255, 255))
    # cheeks
    img.alpha_composite(soft_layer(lambda dd: [dd.ellipse(ellipse(cx + sx * S * 0.185, cy + S * 0.06, S * 0.046, S * 0.027), fill=(255, 140, 178, 170)) for sx in (-1, 1)], S * 0.006))
    d = ImageDraw.Draw(img)
    # smile: quadratic curve drawn as a thick round-capped polyline
    p0, p1, p2 = (cx - S * 0.062, cy + S * 0.065), (cx, cy + S * 0.125), (cx + S * 0.062, cy + S * 0.065)
    w = S * 0.03
    for i in range(61):
        t = i / 60
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        d.ellipse(ellipse(x, y, w / 2, w / 2), fill=ink)
    # sparkle (kept inside the maskable safe zone)
    d.polygon(star(cx + S * 0.245, cy - S * 0.245, S * 0.055), fill=(255, 209, 102, 255))
    d.polygon(star(cx - S * 0.27, cy - S * 0.2, S * 0.025), fill=(255, 255, 255, 200))
    return img.convert("RGB")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    icon = draw_icon()
    for name, size in [("icon-512.png", 512), ("icon-192.png", 192), ("icon-180.png", 180), ("icon-maskable-512.png", 512)]:
        icon.resize((size, size), Image.LANCZOS).save(OUT / name, optimize=True)
        print("wrote", OUT / name)


if __name__ == "__main__":
    main()
