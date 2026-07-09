# helpers/make_qr.py
"""Generate QR PNGs for exercise URLs: uv run python helpers/make_qr.py"""
from pathlib import Path

import segno

BASE = "https://beyondsimulations.github.io/Introduction-to-Python/notebooks"
OUT = Path(__file__).resolve().parent.parent / "lectures" / "assets" / "qr"
EXERCISES = ["ex_01_a", "ex_01_b", "ex_01_c"]  # extend in later plans

OUT.mkdir(parents=True, exist_ok=True)
for ex in EXERCISES:
    segno.make(f"{BASE}/{ex}/").save(str(OUT / f"{ex}.png"), scale=8)
    print(f"wrote {OUT / (ex + '.png')}")
