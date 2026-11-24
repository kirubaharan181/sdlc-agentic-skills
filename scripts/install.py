#!/usr/bin/env python3
"""Install the standalone skills into the folder a coding agent reads (static copy or symlink; no network, no dependencies).

Targets and folders were taken from each tool's public documentation on 2026-11-23; check the current documentation, because
tools change. Installing does not prove that an agent loads or follows a skill (see adapters/COMPATIBILITY.md).

  python3 scripts/install.py --list
  python3 scripts/install.py --target codex --dest /path/to/project            # copies into <project>/.agents/skills
  python3 scripts/install.py --target opencode --scope user --dry-run
  python3 scripts/install.py --target claude --dest . --skill code-review-quality --skill incident-command
  python3 scripts/install.py --target codex --dest . --check                    # verify installed copies match this library
"""
from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# target -> (project-relative folder, user-relative folder under $HOME)
TARGETS = {
    "codex": (".agents/skills", ".agents/skills"),
    "opencode": (".opencode/skills", ".config/opencode/skills"),
    "claude": (".claude/skills", ".claude/skills"),
    "agents": (".agents/skills", ".agents/skills"),  # shared folder that Codex and OpenCode both scan
}


def library() -> dict[str, Path]:
    found = {p.parent.name: p.parent for p in sorted((ROOT / "skills").glob("*/*/SKILL.md"))}
    if not found:
        sys.exit("No skills found under skills/<group>/<skill>/SKILL.md")
    return found


def destination(target: str, scope: str, dest: str | None) -> Path:
    project, user = TARGETS[target]
    base = Path.home() / user if scope == "user" else Path(dest or ".").resolve() / project
    return base


def same_tree(a: Path, b: Path) -> bool:
    cmp = filecmp.dircmp(a, b)
    if cmp.left_only or cmp.right_only or cmp.funny_files or filecmp.cmpfiles(a, b, cmp.common_files, shallow=False)[1:] != ([], []):
        return False
    return all(same_tree(a / d, b / d) for d in cmp.common_dirs)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--target", choices=sorted(TARGETS))
    ap.add_argument("--scope", choices=["project", "user"], default="project")
    ap.add_argument("--dest", help="project folder for --scope project (default: current directory)")
    ap.add_argument("--skill", action="append", default=[], help="install only this skill id (repeatable)")
    ap.add_argument("--symlink", action="store_true", help="symlink instead of copy (stays in sync with this checkout)")
    ap.add_argument("--force", action="store_true", help="replace skills that already exist at the destination")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--check", action="store_true", help="verify installed skills match this library; installs nothing")
    ap.add_argument("--list", action="store_true", help="list skills and target folders")
    a = ap.parse_args(argv)

    lib = library()
    if a.list:
        print(f"{len(lib)} skills: " + ", ".join(lib))
        for t, (p, u) in TARGETS.items():
            print(f"  {t:9} project: <project>/{p}   user: ~/{u}")
        return 0
    if not a.target:
        ap.error("--target is required")
    unknown = [s for s in a.skill if s not in lib]
    if unknown:
        ap.error("unknown skill(s): " + ", ".join(unknown))
    chosen = {k: v for k, v in lib.items() if not a.skill or k in a.skill}
    base = destination(a.target, a.scope, a.dest)

    if a.check:
        bad = [k for k, v in chosen.items() if not (base / k).exists() or not same_tree(v, (base / k).resolve())]
        print(f"CHECK {'FAILED' if bad else 'PASSED'}: {len(chosen) - len(bad)}/{len(chosen)} skills match in {base}")
        for k in bad:
            print(f"  differs or missing: {k}")
        return 1 if bad else 0

    print(f"{'Would install' if a.dry_run else 'Installing'} {len(chosen)} skill(s) into {base} ({'symlink' if a.symlink else 'copy'})")
    skipped = 0
    for k, src in chosen.items():
        dst = base / k
        if dst.exists() or dst.is_symlink():
            if not a.force:
                skipped += 1
                print(f"  skip (exists, use --force): {k}")
                continue
            if not a.dry_run:
                shutil.rmtree(dst) if dst.is_dir() and not dst.is_symlink() else dst.unlink()
        if a.dry_run:
            continue
        base.mkdir(parents=True, exist_ok=True)
        if a.symlink:
            dst.symlink_to(src, target_is_directory=True)
        else:
            shutil.copytree(src, dst)
    if not a.dry_run:
        print(f"Done: {len(chosen) - skipped} installed, {skipped} skipped. Restart the agent so it rescans its skill folders.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
