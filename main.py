# SPDX-License-Identifier: MIT
"""Roast Your Own Agent — writes the winning one-line roast to /output/entry.txt."""
import os

ROAST = "My agent logs everything it does for me — the log is now the biggest thing it has done for me."


def main():
    # Gate check, measured locally: single line, 1-200 characters, non-blank.
    assert 1 <= len(ROAST) <= 200 and ROAST.strip() and "\n" not in ROAST
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = "output"
        os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
