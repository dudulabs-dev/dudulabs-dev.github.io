#!/usr/bin/env python3
"""Store screenshots (1320x2868, headline + phone frame) -> web feature images.

Crops the app screen out of the store screenshot (drops the headline, background and phone bezel),
rounds the top corners, resizes to 600px wide and writes transparent WebP into assets/features/.
The bottom edge is cut on purpose: the page lets the phone bleed off the bottom of its band.

Usage: python3 tools/make-feature-images.py                 # DayCount images
       python3 tools/make-feature-images.py mm13 <raw dir>   # Muscle Memory 1.3 (D2 design)
<raw dir> = output of muscle-memory-d2 `scripts/capture-store-shots.sh` (full 1320x2868 simulator screens):
the hero, the home page shots and the weekly / chart bands come from raw screens (not in the store set).
Needs Pillow and `cwebp` (brew install webp).
"""
import subprocess
import sys
import tempfile
from pathlib import Path
from PIL import Image, ImageDraw

SRC = Path.home() / "Projects/mobile-apps"
SITE = Path(__file__).resolve().parent.parent
OUT = SITE / "assets" / "features"

# (store shot dir, screen top-left y). Screen = x 132..1188 (W*0.8 wide inside 22px bezel), see scripts/make-store-shots.py
DC_V3 = SRC / "day-count/design/store-screenshots/v3"          # live: 1.5 listing
DC_V4 = SRC / "day-count-deco/design/store-screenshots/v4"     # 1.7, live since 2026-11-26
MM_13 = SRC / "muscle-memory-d2/docs/store-shots-1.3"          # 1.3 build 28 store set: {l}/01.png .. 06.png
DC_TOP = 662   # frame top 640 + bezel 22
MM_TOP = 582   # frame top 560 + bezel 22
LEFT, WIDTH = 132, 1056
RADIUS = 128
OUT_W = 600

RELEASED = [
    (DC_V3, DC_TOP, "dc-home", "{l}-2-home.png"),
    (DC_V3, DC_TOP, "dc-composer", "{l}-4-composer.png"),
    (DC_V3, DC_TOP, "dc-detail", "{l}-3-detail.png"),
    (DC_V3, DC_TOP, "dc-icon", "{l}-5-icon.png"),
]
MM13_STORE = [
    (MM_13, MM_TOP, "mm-rest", "{l}/02.png"),
    (MM_13, MM_TOP, "mm-month", "{l}/03.png"),
    (MM_13, MM_TOP, "mm-lock", "{l}/05.png"),
]
MM13_RAW = [("mm-chart", "{l}-chart.png"), ("mm-weekly", "{l}-weekly.png")]
LIVE_17 = [
    (DC_V4, DC_TOP, "dc-deco-home", "{l}-1-deco-home.png"),
    (DC_V4, DC_TOP, "dc-deco-editor", "{l}-2-deco-editor.png"),
]


def screen(path: Path, top: int) -> Image.Image:
    im = Image.open(path).convert("RGB")
    crop = im.crop((LEFT, top, LEFT + WIDTH, im.height))
    # rounded top corners only (bottom bleeds off the band)
    mask = Image.new("L", crop.size, 0)
    d = ImageDraw.Draw(mask)
    d.rounded_rectangle([0, 0, crop.width - 1, crop.height + RADIUS], RADIUS, fill=255)
    out = crop.convert("RGBA")
    out.putalpha(mask)
    h = round(crop.height * OUT_W / crop.width)
    return out.resize((OUT_W, h), Image.LANCZOS)


def raw_screen(path: Path) -> Image.Image:
    """Full simulator screen -> the same crop as screen() gives from a store shot (1056 wide, top 2286 px)."""
    im = Image.open(path).convert("RGB").resize((WIDTH, round(2868 * WIDTH / 1320)), Image.LANCZOS)
    return im.crop((0, 0, WIDTH, 2868 - MM_TOP))


def webp(im: Image.Image, dst: Path, alpha=True):
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td) / "x.png"
        im.save(tmp)
        args = ["cwebp", "-quiet", "-q", "80", "-m", "6"] + (["-alpha_q", "90"] if alpha else [])
        subprocess.run(args + [str(tmp), "-o", str(dst)], check=True)
    print(dst.relative_to(SITE), im.size, dst.stat().st_size)


def write_mm13(raw: Path):
    write(MM13_STORE, OUT)
    for lang in ("en", "ko"):
        for name, pattern in MM13_RAW:
            crop = raw_screen(raw / pattern.format(l=lang))
            mask = Image.new("L", crop.size, 0)
            ImageDraw.Draw(mask).rounded_rectangle([0, 0, crop.width - 1, crop.height + RADIUS], RADIUS, fill=255)
            im = crop.convert("RGBA")
            im.putalpha(mask)
            webp(im.resize((OUT_W, round(crop.height * OUT_W / crop.width)), Image.LANCZOS), OUT / f"{name}-{lang}.webp")
        # hero (560x1216 full screen, like before) and the two home page shots (PNG, 560x1216)
        today = Image.open(raw / f"{lang}-today.png").convert("RGB").resize((560, 1216), Image.LANCZOS)
        webp(today, OUT / f"hero-mm-today-{lang}.webp", alpha=False)
        for key in ("today", "month"):
            dst = SITE / "assets" / "shots" / f"mm-{key}-{lang}.png"
            Image.open(raw / f"{lang}-{key}.png").convert("RGB").resize((560, 1216), Image.LANCZOS).save(dst, optimize=True)
            print(dst.relative_to(SITE), dst.stat().st_size)


def write(items, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    for folder, top, name, pattern in items:
        for lang in ("en", "ko"):
            src = folder / pattern.format(l=lang)
            im = screen(src, top)
            with tempfile.TemporaryDirectory() as td:
                tmp = Path(td) / "x.png"
                im.save(tmp)
                dst = out_dir / f"{name}-{lang}.webp"
                subprocess.run(["cwebp", "-quiet", "-q", "80", "-alpha_q", "90", "-m", "6", str(tmp), "-o", str(dst)], check=True)
            print(dst.relative_to(SITE), im.size, dst.stat().st_size)


def main():
    if sys.argv[1:2] == ["mm13"]:
        write_mm13(Path(sys.argv[2]))
        return
    write(RELEASED + LIVE_17, OUT)


if __name__ == "__main__":
    main()
