#!/usr/bin/env python3
"""One command to regenerate everything derived, deterministically.

  python scripts/build.py           regenerate registries' derived fields, agent/workflow/skill Markdown,
                                    dist/ reports and the dashboard snapshot
  python scripts/build.py --check   regenerate in a temporary copy and fail if (a) committed generated files
                                    are out of date or (b) two consecutive builds differ

Committed generated files: registry/*.json (derived fields), agents/*.md, workflows/*.md, skills/**/SKILL.md.
Git-ignored outputs: dist/, dashboard/data/library.json.
"""
from __future__ import annotations

import argparse
import hashlib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import bootstrap_library  # noqa: E402
import generate_reports  # noqa: E402
import rebuild_library  # noqa: E402

ROOT = HERE.parent
IGNORE = shutil.ignore_patterns(".git", ".venv", "__pycache__", ".pytest_cache", "dist", "node_modules")


def build(root: Path) -> None:
    rebuild_library.ROOT = root
    rebuild_library.main()
    generate_reports.write_all(root)
    subprocess.run([sys.executable, str(HERE / "generate_dashboard_data.py")], cwd=root, check=True,
                   env={**__import__("os").environ, "GITHUB_SHA": "build", "GITHUB_REF_NAME": "build"}, stdout=subprocess.DEVNULL)


def digest(root: Path) -> dict[str, str]:
    files = [p for sub in ("dist",) for p in (root / sub).rglob("*") if p.is_file()]
    files += list(bootstrap_library.generated_files(root))
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(files)}


def check() -> int:
    with tempfile.TemporaryDirectory(prefix="sdlc-build-check-") as tmp:
        work = Path(tmp) / "repo"
        shutil.copytree(ROOT, work, ignore=IGNORE)
        before = digest(ROOT)
        build(work)
        first = digest(work)
        build(work)
        second = digest(work)
    stale = sorted(k for k in set(before) & set(first) if before[k] != first[k])
    missing = sorted(k for k in set(before) if k not in first)
    nondeterministic = sorted(k for k in first if first[k] != second.get(k))
    for title, items in (("committed generated files out of date", stale), ("committed generated files no longer produced", missing),
                         ("non-deterministic output between two builds", nondeterministic)):
        if items:
            print(f"BUILD CHECK FAILED: {title}:")
            print("\n".join(f"- {i}" for i in items[:40]))
    if stale or missing or nondeterministic:
        return 1
    print(f"BUILD CHECK PASSED: {len(first)} generated files up to date; two consecutive builds identical.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    if args.check:
        return check()
    build(ROOT)
    print(f"built: dist/ ({sum(1 for _ in (ROOT / 'dist').rglob('*') if _.is_file())} files), dashboard/data/library.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
