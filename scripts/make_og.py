#!/usr/bin/env python3
"""Generate the social share card and touch icon for Money Snowball.

Link-preview crawlers (WhatsApp, Telegram, Facebook, iMessage) will not render an
SVG or a data URI, so og:image must be a real raster file at an absolute URL.
This script writes them into docs/ (the Pages root) so they publish alongside index.html.

Colours are taken from C:\\dev\\design.md; Georgia is the house serif fallback
('Instrument Serif', Georgia, serif) and is present on Windows.

Usage:
    python scripts/make_og.py
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

# --- design.md tokens ---
BG = (250, 250, 248)      # --bg
SKY = (234, 244, 255)     # kid layer --sky
T1 = (26, 26, 24)         # --t1
T3 = (138, 138, 130)      # --t3
BLUE = (59, 130, 246)     # --b2
JOY = (124, 58, 237)      # --joy
GREEN = (26, 135, 84)     # --g
BD2 = (213, 211, 202)     # --bd2

FONTS = Path("C:/Windows/Fonts")


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS / name), size)


def sky_gradient(w: int, h: int) -> Image.Image:
    """Vertical wash from sky-blue to page background, echoing the page header."""
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    stop = int(h * 0.62)
    for y in range(stop):
        t = y / stop
        d.line(
            [(0, y), (w, y)],
            fill=tuple(round(SKY[i] + (BG[i] - SKY[i]) * t) for i in range(3)),
        )
    return img


def snowball_trail(d: ImageDraw.ImageDraw, x0: int, y0: int, x1: int, y1: int, balls) -> None:
    """A slope with snowballs growing as they roll down it — the whole metaphor in one glance."""
    d.line([(x0, y0), (x1, y1)], fill=BD2, width=5)
    for t, r in balls:
        cx = x0 + (x1 - x0) * t
        cy = y0 + (y1 - y0) * t - r * 0.55
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255), outline=BLUE, width=4)
        # two speckles, as on the page's SVG ball
        if r > 14:
            d.ellipse([cx - r * .38 - 3, cy - r * .38 - 3, cx - r * .38 + 3, cy - r * .38 + 3], fill=SKY)
            d.ellipse([cx + r * .30 - 2, cy + r * .34 - 2, cx + r * .30 + 2, cy + r * .34 + 2], fill=SKY)


def build_og() -> None:
    W, H = 1200, 630
    img = sky_gradient(W, H)
    d = ImageDraw.Draw(img)

    f_title = font("georgia.ttf", 104)
    f_sub = font("georgiai.ttf", 40)
    f_hook = font("arialbd.ttf", 34)
    f_small = font("arial.ttf", 25)

    # Title, centred
    title = "Money Snowball"
    tw = d.textbbox((0, 0), title, font=f_title)[2]
    d.text(((W - tw) / 2, 74), title, font=f_title, fill=T1)

    sub = "watch small money grow into BIG money"
    sw = d.textbbox((0, 0), sub, font=f_sub)[2]
    d.text(((W - sw) / 2, 196), sub, font=f_sub, fill=T3)

    # The snowball rolling down its hill
    snowball_trail(d, 150, 300, 1050, 430, [(0.02, 9), (0.26, 18), (0.52, 32), (0.78, 52), (1.0, 76)])

    # The hook — the number that does the teaching
    hook = "1 cent, doubled for 30 days  =  $5,368,709"
    hw = d.textbbox((0, 0), hook, font=f_hook)[2]
    pad_x, pad_y, by = 30, 16, 496
    d.rounded_rectangle(
        [(W - hw) / 2 - pad_x, by - pad_y, (W + hw) / 2 + pad_x, by + 44 + pad_y],
        radius=34, fill=(255, 255, 255), outline=JOY, width=3,
    )
    d.text(((W - hw) / 2, by), hook, font=f_hook, fill=JOY)

    foot = "Teach your kids compounding — 7 steps, ages 7-12"
    fw = d.textbbox((0, 0), foot, font=f_small)[2]
    d.text(((W - fw) / 2, 582), foot, font=f_small, fill=T3)

    out = DOCS / "og.png"
    img.save(out, "PNG", optimize=True)
    print(f"  og.png          {out.stat().st_size/1024:6.1f} KB  (1200x630)")


def build_icon() -> None:
    """Apple touch icon — kids may add this to a home screen."""
    S = 180
    img = Image.new("RGB", (S, S), SKY)
    d = ImageDraw.Draw(img)
    d.ellipse([26, 26, 154, 154], fill=(255, 255, 255), outline=BLUE, width=7)
    d.ellipse([60, 60, 78, 78], fill=SKY)
    d.ellipse([104, 106, 116, 118], fill=SKY)
    out = DOCS / "icon-180.png"
    img.save(out, "PNG", optimize=True)
    print(f"  icon-180.png    {out.stat().st_size/1024:6.1f} KB  (180x180)")


if __name__ == "__main__":
    DOCS.mkdir(parents=True, exist_ok=True)
    print("Building share assets ->", DOCS)
    build_og()
    build_icon()
