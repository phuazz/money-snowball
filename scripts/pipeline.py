#!/usr/bin/env python3
"""Money Snowball build pipeline.

This dashboard carries NO external data (it is pure in-browser maths), so the
"build" is simply: copy template.html -> docs/index.html and stamp a build date.
Kept as scripts/pipeline.py for consistency with the vault dashboard convention.

Usage:
    python scripts/pipeline.py
"""

from __future__ import annotations

from datetime import date  # Python months are 1-indexed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "template.html"
OUT = ROOT / "docs" / "index.html"

# Build stamp: ISO date, formatted via the date library (never computed by hand).
BUILD_DATE = date.today().isoformat()  # e.g. 2026-07-11


def main() -> None:
    html = TEMPLATE.read_text(encoding="utf-8")

    # Replace the build-date placeholder if present; harmless if absent.
    html = html.replace("<!-- BUILD_DATE -->", BUILD_DATE)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")

    size_kb = len(html.encode("utf-8")) / 1024
    print(f"Built {OUT.relative_to(ROOT)}  ({size_kb:.0f} KB, build {BUILD_DATE})")


if __name__ == "__main__":
    main()
