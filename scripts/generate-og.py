#!/usr/bin/env python3
"""Generate OG images for the cache-bust experiment.

Produces images/og-v1.png and images/og-v2.png at 1200x630px with clearly
distinguishable visuals (different background color + bold "V1"/"V2" text).
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent.parent / "images"
OUT.mkdir(parents=True, exist_ok=True)


def find_font(size: int) -> ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNS.ttf",
        "/Library/Fonts/Arial Bold.ttf",
    ]
    for p in candidates:
        if Path(p).exists():
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()


def draw_card(version: str, bg: tuple, fg: tuple, title: str, out_path: Path) -> None:
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)

    big = find_font(420)
    sub = find_font(64)
    foot = find_font(36)

    bbox = d.textbbox((0, 0), version, font=big)
    bw, bh = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text(((W - bw) / 2 - bbox[0], (H - bh) / 2 - bbox[1] - 60), version, fill=fg, font=big)

    sbbox = d.textbbox((0, 0), title, font=sub)
    sw = sbbox[2] - sbbox[0]
    d.text(((W - sw) / 2 - sbbox[0], 50), title, fill=fg, font=sub)

    foot_text = "Kakao OG cache-bust experiment"
    fbbox = d.textbbox((0, 0), foot_text, font=foot)
    fw = fbbox[2] - fbbox[0]
    d.text(((W - fw) / 2 - fbbox[0], H - 90), foot_text, fill=fg, font=foot)

    img.save(out_path, format="PNG", optimize=True)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    draw_card("V1", bg=(30, 90, 220), fg=(255, 255, 255), title="Cache Test V1", out_path=OUT / "og-v1.png")
    draw_card("V2", bg=(220, 60, 80), fg=(255, 255, 255), title="Cache Test V2", out_path=OUT / "og-v2.png")
