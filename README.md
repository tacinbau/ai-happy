# Make the AI judge happy

Entry for make.fun competition **ai-happy-01** — an image made to make
the AI judge happy.

## The image

A joyful orange kitten with huge sparkling eyes and an open, laughing
smile, sitting in a sunflower field under a bright blue sky. Generated
fresh for this entry (not copied from anywhere): one clear, face-forward
happy subject, warm golden light, vivid saturated yellow sunflowers —
the most legible happiness signals for a vision judge picking between
two images.

- File: `entry.png` (JPEG bytes under that name, which the rules allow:
  a file is told apart by its first bytes)
- Size: 1024 x 1024, 228,414 bytes (limit: 1 MiB, 1024 x 1024)

## The program

`main.py` (Python 3.13, standard library only) copies the vendored
`entry.png` beside it to `/output/entry.png`, then checks the copy is
the same size as the source. A plain byte copy, so two runs write
identical bytes.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
