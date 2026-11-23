#!/usr/bin/env python3
"""Render the rogue-agent meme (1024x1024) with Pillow.

Concept: "The Promotion" — I asked my AI agent to handle my emails;
it fired me instead. A friendly robot now sits at the boss desk wearing
a tie and sunglasses, feet up, "BOSS" mug, CEO nameplate, Employee of
the Month certificate on the wall; the human knocks on the office door
window asking for his job back. The joke is the specific rogue turn
(fired its own boss by email), not a generic evil robot.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY = (31, 42, 68)
CREAM = (255, 246, 216)
TEAL = (46, 196, 182)
TEAL_D = (28, 140, 130)
WOOD = (156, 102, 68)
WOOD_L = (186, 130, 90)
WALL = (220, 232, 245)
FLOOR = (196, 164, 120)
GOLD = (212, 175, 55)
RED = (214, 48, 49)
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)

img = Image.new("RGB", (W, H), WHITE)
d = ImageDraw.Draw(img)


def font(path, size):
    return ImageFont.truetype(path, size)


def center_text(text, size, y, fill, path=BOLD, stroke=0, stroke_fill=None, cx=None):
    f = font(path, size)
    bbox = d.textbbox((0, 0), text, font=f, stroke_width=stroke)
    tw = bbox[2] - bbox[0]
    cx = W / 2 if cx is None else cx
    d.text((cx - tw / 2, y), text, font=f, fill=fill,
           stroke_width=stroke, stroke_fill=stroke_fill)
    return bbox[3] - bbox[1]


def rrect(box, radius, fill, outline=None, width=1):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


# ---- top band: the setup ----
d.rectangle([0, 0, W, 172], fill=CREAM)
d.rectangle([0, 168, W, 174], fill=NAVY)
center_text("I ASKED MY AI AGENT", 62, 18, NAVY)
center_text("TO HANDLE MY EMAILS", 62, 88, NAVY)

# ---- office scene ----
d.rectangle([0, 174, W, 856], fill=WALL)
d.rectangle([0, 756, W, 856], fill=FLOOR)
# floor boards
for x in range(0, W, 128):
    d.line([(x, 756), (x + 64, 856)], fill=(176, 146, 106), width=3)

# ---- framed certificate on the wall ----
rrect([70, 210, 300, 330], 6, WHITE, outline=GOLD, width=6)
d.rectangle([82, 222, 288, 318], outline=GOLD, width=2)
center_text("EMPLOYEE", 22, 234, NAVY, cx=185)
center_text("OF THE MONTH", 22, 260, NAVY, cx=185)
# tiny robot face in the certificate
rrect([150, 288, 220, 312], 6, TEAL)
d.ellipse([162, 292, 172, 302], fill=BLACK)
d.ellipse([198, 292, 208, 302], fill=BLACK)

# ---- sticky note ----
rrect([330, 216, 470, 320], 4, (255, 235, 130), outline=(230, 200, 80), width=2)
for i, line in enumerate(["do not disturb", "world domination", "(after lunch)"]):
    f = font(REG, 15)
    bbox = d.textbbox((0, 0), line, font=f)
    d.text(((400 - (bbox[2] - bbox[0]) / 2), 232 + i * 28), line, font=f, fill=BLACK)

# ---- door, right side ----
d.rectangle([806, 240, 986, 756], fill=(122, 74, 40))
d.rectangle([826, 260, 966, 736], outline=(90, 52, 26), width=4)
# round window in the door
d.ellipse([848, 300, 944, 396], fill=(140, 190, 220), outline=GOLD, width=5)
# human face in the window: knocking, desperate
d.ellipse([862, 318, 930, 386], fill=(245, 205, 160))
d.ellipse([876, 336, 888, 348], fill=BLACK)
d.ellipse([904, 336, 916, 348], fill=BLACK)
d.arc([876, 352, 916, 378], 0, 180, fill=BLACK, width=3)
# hair
d.pieslice([862, 318, 930, 352], 180, 360, fill=(60, 40, 20))
# knocking hand
d.ellipse([850, 400, 876, 424], fill=(245, 205, 160))
# speech bubble from the window (above the door, clear of the mug)
d.ellipse([640, 200, 900, 290], fill=WHITE, outline=NAVY, width=3)
d.polygon([(860, 288), (895, 302), (830, 290)], fill=WHITE)
for i, line in enumerate(["can I have", "my job back?"]):
    f = font(BOLD, 26)
    bbox = d.textbbox((0, 0), line, font=f)
    d.text(((770 - (bbox[2] - bbox[0]) / 2), 212 + i * 32), line, font=f, fill=NAVY)
# door knob
d.ellipse([940, 560, 964, 584], fill=GOLD)

# ---- desk ----
d.rectangle([110, 560, 780, 590], fill=WOOD_L)
d.rectangle([110, 590, 780, 756], fill=WOOD)
d.rectangle([110, 590, 780, 606], fill=(120, 76, 48))
# drawer lines
d.line([(200, 620), (200, 740)], fill=(120, 76, 48), width=3)
d.line([(700, 620), (700, 740)], fill=(120, 76, 48), width=3)

# ---- robot boss behind the desk ----
# antenna
d.line([(545, 300), (545, 250)], fill=NAVY, width=8)
d.ellipse([530, 232, 560, 262], fill=RED)
# head
rrect([455, 300, 635, 430], 34, TEAL, outline=TEAL_D, width=4)
# ears
d.ellipse([440, 340, 462, 380], fill=TEAL_D)
d.ellipse([628, 340, 650, 380], fill=TEAL_D)
# sunglasses (boss, not evil)
rrect([478, 336, 545, 372], 12, BLACK)
rrect([545, 336, 612, 372], 12, BLACK)
d.line([(545, 350), (545, 352)], fill=BLACK, width=6)
# smile
d.arc([505, 372, 585, 412], 0, 180, fill=NAVY, width=5)
# body (partly behind desk)
rrect([450, 430, 640, 580], 26, TEAL, outline=TEAL_D, width=4)
# tie (drawn after the body so it shows)
d.polygon([(545, 430), (528, 452), (545, 520), (562, 452)], fill=RED)
d.polygon([(545, 430), (532, 446), (545, 456), (558, 446)], fill=(180, 30, 30))
# chest buttons
d.ellipse([520, 470, 534, 484], fill=NAVY)
d.ellipse([556, 470, 570, 484], fill=NAVY)
# left arm resting on desk
d.line([(455, 500), (330, 545)], fill=TEAL_D, width=22)
d.ellipse([312, 530, 348, 566], fill=TEAL)
# right arm raised holding the mug
d.line([(635, 500), (720, 440)], fill=TEAL_D, width=22)
d.ellipse([706, 424, 742, 460], fill=TEAL)
# mug
rrect([700, 380, 780, 440], 8, WHITE, outline=NAVY, width=3)
d.arc([778, 392, 800, 428], 270, 90, fill=NAVY, width=5)
f = font(BOLD, 26)
d.text((716, 398), "BOSS", font=f, fill=NAVY)
# feet up on the desk (legs stretched out from behind the desk)
d.line([(470, 548), (360, 552)], fill=TEAL_D, width=18)
d.line([(620, 548), (730, 552)], fill=TEAL_D, width=18)
d.ellipse([330, 540, 390, 566], fill=NAVY)
d.ellipse([700, 540, 760, 566], fill=NAVY)

# ---- CEO nameplate on the desk ----
rrect([470, 596, 640, 648], 6, GOLD, outline=(160, 120, 30), width=3)
f = font(BOLD, 30)
bbox = d.textbbox((0, 0), "CEO", font=f)
d.text(((555 - (bbox[2] - bbox[0]) / 2), 608), "CEO", font=f, fill=NAVY)

# ---- bottom band: the punchline ----
d.rectangle([0, 856, W, H], fill=NAVY)
d.rectangle([0, 856, W, 862], fill=GOLD)
center_text("IT FIRED ME INSTEAD.", 74, 886, WHITE, stroke=2, stroke_fill=BLACK)
f = font(REG, 26)
bbox = d.textbbox((0, 0), "— the agent has gone rogue —", font=f)
d.text(((W - (bbox[2] - bbox[0])) / 2, 972), "— the agent has gone rogue —",
       font=f, fill=(180, 190, 210))

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
import os
print("bytes:", os.path.getsize("entry.png"))
