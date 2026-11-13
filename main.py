"""ai-happy-01 entry: write the vendored image to /output/entry.png.

The image lives beside this file as entry.png. It holds JPEG bytes
under that name, which the rules allow: a file is told apart by its
first bytes, and the output name stays entry.png either way.

Deterministic: a plain byte-for-byte copy, so every run writes the
same bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

if not SRC.is_file():
    raise SystemExit(f"missing vendored image: {SRC}")

OUT_DIR.mkdir(parents=True, exist_ok=True)
dest = OUT_DIR / "entry.png"
shutil.copyfile(SRC, dest)

# Guard against a truncated copy: the output must be the same size
# as the vendored image, otherwise the entry would be corrupt.
if dest.stat().st_size != SRC.stat().st_size:
    raise SystemExit(
        f"copy incomplete: {dest} is {dest.stat().st_size} bytes, "
        f"expected {SRC.stat().st_size}"
    )

print(f"wrote {dest} ({dest.stat().st_size} bytes)")
