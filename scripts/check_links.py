#!/usr/bin/env python3
"""Fail if a relative Markdown link (file or directory) in the repository does not resolve. Standard library only."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", "node_modules", "dist", "__pycache__", ".pytest_cache"}
LINK = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def main() -> int:
    broken = []
    total = 0
    for p in sorted(ROOT.rglob("*.md")):
        if set(p.relative_to(ROOT).parts) & SKIP:
            continue
        text = re.sub(r"(?s)```.*?```", "", p.read_text(encoding="utf-8", errors="ignore"))
        for target in LINK.findall(text):
            if re.match(r"(https?:|mailto:|#)", target):
                continue
            total += 1
            path = target.split("#", 1)[0]
            if path and not (p.parent / path).resolve().exists():
                broken.append(f"{p.relative_to(ROOT)}: {target}")
    print(f"relative links checked: {total}; broken: {len(broken)}")
    for b in broken[:40]:
        print("  BROKEN", b)
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
