# helpers/make_qr.py
"""Generate QR PNGs for exercise URLs: uv run python helpers/make_qr.py

Ad hoc (e.g. a checkpoint on the separate host):
    uv run python helpers/make_qr.py <url> <out.png>
"""
import sys
from pathlib import Path

import segno

BASE = "https://python.tobiasvlcek.com/notebooks"
OUT = Path(__file__).resolve().parent.parent / "lectures" / "assets" / "qr"
EXERCISES = [
    "ex_01_a", "ex_01_b", "ex_01_c",
    "ex_02_a", "ex_02_b", "ex_02_c",
    "ex_03_a", "ex_03_b",
    "ex_04_a", "ex_04_b", "ex_04_c",
    "ex_05_a", "ex_05_b",
    "ex_06_a", "ex_06_b",
    "ex_07_a", "ex_07_b", "ex_07_c",
    "ex_08_a", "ex_08_b",
    "ex_09_a", "ex_09_b", "ex_09_c",
]  # extend in later plans

if len(sys.argv) == 3:
    segno.make(sys.argv[1]).save(sys.argv[2], scale=8, light=None, dark="#363D45")
    print(f"wrote {sys.argv[2]} -> {sys.argv[1]}")
    raise SystemExit

OUT.mkdir(parents=True, exist_ok=True)
for ex in EXERCISES:
    segno.make(f"{BASE}/{ex}/").save(str(OUT / f"{ex}.png"), scale=8, light=None, dark="#363D45")
    print(f"wrote {OUT / (ex + '.png')}")
