#!/usr/bin/env python3
"""Build a reproducible release archive and SHA256SUMS from the files tracked by git (standard library only).

  python3 scripts/make_release.py --out dist-release          # writes sdlc-agentic-skills-<VERSION>.tar.gz and SHA256SUMS
  python3 scripts/make_release.py --notes                      # prints the CHANGELOG section for VERSION

The archive is deterministic for a given commit (sorted entries, fixed mtime/owner). Checksums prove the file you downloaded matches
what was built; they are not a signature and not a security certification.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import re
import subprocess
import sys
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def version() -> str:
    return (ROOT / "VERSION").read_text(encoding="utf-8").strip()


def tracked() -> list[str]:
    out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True).stdout
    return sorted(p for p in out.decode("utf-8").split("\0") if p)


def build(out: Path) -> tuple[Path, Path]:
    name = f"sdlc-agentic-skills-{version()}"
    out.mkdir(parents=True, exist_ok=True)
    archive = out / f"{name}.tar.gz"
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w") as tar:
        for rel in tracked():
            p = ROOT / rel
            if not p.is_file():
                continue
            info = tarfile.TarInfo(f"{name}/{rel}")
            data = p.read_bytes()
            info.size, info.mtime, info.uid, info.gid, info.uname, info.gname = len(data), 0, 0, 0, "", ""
            info.mode = 0o755 if p.stat().st_mode & 0o111 else 0o644
            tar.addfile(info, io.BytesIO(data))
    with archive.open("wb") as raw, gzip.GzipFile(fileobj=raw, mode="wb", mtime=0) as gz:
        gz.write(buf.getvalue())
    sums = out / "SHA256SUMS"
    sums.write_text(f"{hashlib.sha256(archive.read_bytes()).hexdigest()}  {archive.name}\n", encoding="utf-8")
    return archive, sums


def notes() -> str:
    text = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    m = re.search(rf"^## \[{re.escape(version())}\][^\n]*\n(.*?)(?=^## \[|\Z)", text, re.S | re.M)
    if not m:
        sys.exit(f"CHANGELOG.md has no section for {version()}")
    return m.group(1).strip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, default=ROOT / "dist-release")
    ap.add_argument("--notes", action="store_true")
    a = ap.parse_args()
    if a.notes:
        print(notes(), end="")
        return 0
    archive, sums = build(a.out)
    print(f"{archive}\n{sums.read_text(encoding='utf-8').strip()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
