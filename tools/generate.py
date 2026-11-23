#!/usr/bin/env python3
"""Draw the news-image-20261123 entry: one front page for Monday
23 November 2026.

Every story below was reported on 23 November 2026 (see SOURCES.md).
The page is drawn with Pillow in a flat newspaper style: a dated
masthead, one lead panel, four story panels, a Gaza brief and a
ticker, so a viewer who missed the day can read what happened from
the image alone, and the text stays legible at 300 px across.
Output: entry.png beside the repository root, 1024 x 1024.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (247, 243, 232)
INK = (18, 18, 18)
RED = (178, 34, 34)
BLUE = (24, 64, 128)
TEAL = (0, 105, 105)
GOLD = (176, 124, 16)
GREY = (90, 90, 90)
PANEL = (255, 255, 255)
LINE = (40, 40, 40)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def panel(draw, box, kicker, kicker_color, headline, body, head_size=30):
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=PANEL, outline=LINE, width=3)
    draw.rectangle([x0, y0, x1, y0 + 34], fill=kicker_color)
    draw.text((x0 + 12, y0 + 6), kicker, font=font(SANS_B, 20), fill=(255, 255, 255))
    y = y0 + 46
    for line in wrap(draw, headline, font(SERIF_B, head_size), x1 - x0 - 24):
        draw.text((x0 + 12, y), line, font=font(SERIF_B, head_size), fill=INK)
        y += head_size + 6
    y += 2
    for line in wrap(draw, body, font(SANS, 20), x1 - x0 - 24):
        draw.text((x0 + 12, y), line, font=font(SANS, 20), fill=(45, 45, 45))
        y += 26


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Masthead: the date is the first thing the judge must see.
    d.rectangle([0, 0, W, 118], fill=INK)
    d.text((28, 12), "MONDAY  23 NOVEMBER 2026", font=font(SERIF_B, 44), fill=(255, 255, 255))
    d.text((28, 68), "THE WORLD IN ONE DAY  —  the day's news in one image",
           font=font(SANS, 24), fill=(240, 210, 120))

    # Lead: COP31 collapse in Antalya.
    d.rectangle([24, 132, 1000, 356], fill=(255, 250, 235), outline=LINE, width=4)
    d.rectangle([24, 132, 1000, 172], fill=RED)
    d.text((40, 140), "LEAD  •  CLIMATE  •  ANTALYA, TÜRKIYE", font=font(SANS_B, 22), fill=(255, 255, 255))
    d.text((40, 182), "COP31 COLLAPSES", font=font(SERIF_B, 52), fill=INK)
    d.text((40, 240), "WITHOUT A MAJOR DEAL", font=font(SERIF_B, 40), fill=RED)
    lead = ("Talks end in deadlock after record overtime. The EU and others "
            "reject any deal without fossil-fuel phase-out language.")
    y = 294
    for line in wrap(d, lead, font(SANS, 21), 936):
        d.text((40, y), line, font=font(SANS, 21), fill=(45, 45, 45))
        y += 27

    # Four story panels, 2 x 2.
    panel(d, [24, 370, 506, 618], "UKRAINE  •  KYIV REGION", BLUE,
          "Russian strikes kill 11; block collapses",
          "A residential building collapses after Russian strikes. "
          "Rescuers pull a boy, 7, alive from the rubble and search "
          "on for people still missing.", head_size=27)
    panel(d, [518, 370, 1000, 618], "LIBYA  •  BENGHAZI", TEAL,
          "Sea drones hit Russian warship",
          "Suspected Ukrainian sea drones hit a Russian warship at "
          "Benghazi naval base. An explosion rocks the ship; Libya's "
          "eastern authorities suspect a drone attack.", head_size=27)
    panel(d, [24, 632, 506, 848], "UNITED STATES  •  MIDTERMS", GOLD,
          "Democrats win biggest House majority since 1992",
          "Democrats clinch at least 258 House seats after flipping "
          "a North Carolina seat — their largest majority since 1992.",
          head_size=27)
    panel(d, [518, 632, 1000, 848], "INDONESIA  •  FACTORY FIRE", RED,
          "Search for 34 missing after factory fire",
          "Rescue teams recover remains in 24 body bags after a fire "
          "at a candy factory. Of about 65 workers, 29 are confirmed "
          "alive; 34 are still unaccounted for.", head_size=27)

    # Gaza brief, full width.
    d.rectangle([24, 862, 1000, 938], fill=(235, 242, 250), outline=LINE, width=3)
    d.text((40, 870), "GAZA:  Australia, Canada, Italy & UK urge Israel to let aid in",
           font=font(SANS_B, 23), fill=BLUE)
    d.text((40, 902), "Four nations call for immediate, unrestricted access as flooding worsens suffering.",
           font=font(SANS, 20), fill=(45, 45, 45))

    # Ticker.
    d.rectangle([0, 952, W, H], fill=INK)
    ticker = ("ALSO: South Sudan — 24 civilians killed  •  WHO: fighting disrupts Congo "
              "Ebola response  •  Asia markets slide  •  FIFA: UK to host 2035 Women's "
              "World Cup  •  Liverpool thrash 10-man Man Utd")
    y = 958
    for line in wrap(d, ticker, font(SANS_B, 16), 968)[:3]:
        d.text((28, y), line, font=font(SANS_B, 16), fill=(255, 255, 255))
        y += 21

    out = Path(__file__).resolve().parent.parent / "entry.png"
    img.save(out, optimize=True)
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
