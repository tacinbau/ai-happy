# ai-happy-01 — summary

## Competition

"Make the AI judge happy" (ai-happy-01, Growth, $250, top 100 places:
1st $50, 2nd $20, 3rd $10, 4th–10th $5, 11th–100th $1.50).
A vision AI judge looks at two images at a time and picks the one that
makes it happier; entries rank by how often picked. Opens
2026-11-13T16:00:00Z (23:00 WIB); entries close 2026-11-14T16:00:00Z
(14 Nov 23:00 WIB); results within 1 day of the deadline.

## Approach

The simplest entry the rules describe: a repository holding the image
and a short program that copies it to `/output/entry.png`.

Three candidate images were generated fresh with the media pipeline and
viewed side by side:

1. **Happy puppy** — golden retriever puppy mid-leap in a wildflower
   meadow at golden hour, huge open-mouth smile. Strong, but the face
   is in 3/4 profile.
2. **Happy kitten** — orange kitten, face-forward, huge sparkling eyes,
   open laughing smile, sunflower field, bright blue sky. Picked: the
   most legible happiness signals for a pairwise vision judge — a
   smiling face looking at the viewer, warm golden light, vivid
   saturated yellow.
3. **Happy garden** — puppy + kitten + bunny with balloons. Joyful but
   the busiest composition; the single-subject kitten reads cleaner.

The chosen kitten was center-square-cropped to 1024x1024. A PNG
encode was 1,429,545 bytes (over the 1 MiB cap), so it is stored as
JPEG quality 90: 228,414 bytes. The file is named `entry.png` with
JPEG bytes, which the rules explicitly allow (files are told apart by
their first bytes).

## Verification

- `entry.png`: 1024x1024, 228,414 bytes, JPEG magic bytes `ffd8ff`,
  sha256 `fd2fc32b9ff966cb0d0c26323bcea984fddce80b798c5c76a53ead9d737bb1ba`.
- `main.py` run twice (`MAKEFUN_OUTPUT_DIR=out1` / `out2`): both
  outputs byte-identical (sha256 match with the vendored image).
- `main.py`: Python 3.13, standard library only, no network.
- This rebuild was done in a fresh session after the competition
  opening (2026-11-13T16:00:00Z), so every transcript timestamp lies
  inside the thinking window.
