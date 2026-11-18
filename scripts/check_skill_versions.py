#!/usr/bin/env python3
"""Enforce the skill versioning policy (docs/governance/SKILL_VERSIONING.md).

registry/skill-versions.lock.json records, per skill, the released version and a hash of its authored content
(registry/skill-content/<skill>.json without the `version` field).

  check (default)  fail if the content changed without a higher version, or if the lock is out of date
  --update         record the current versions and hashes (run after bumping a version on purpose)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import registry_io  # noqa: E402

LOCK = "registry/skill-versions.lock.json"


def content_hash(c: dict) -> str:
    body = {k: v for k, v in c.items() if k != "version"}
    return hashlib.sha256(json.dumps(body, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()


def semver(v: str) -> tuple[int, int, int]:
    a, b, c = v.split(".")
    return int(a), int(b), int(c)


def current(root: Path) -> dict[str, dict]:
    return {sid: {"version": c["version"], "content_sha256": content_hash(c)} for sid, c in sorted(registry_io.load_skill_content(root).items())}


def check(root: Path = ROOT) -> list[str]:
    cur = current(root)
    lp = root / LOCK
    if not lp.exists():
        return [f"{LOCK} is missing; run scripts/check_skill_versions.py --update"]
    locked = json.loads(lp.read_text(encoding="utf-8"))
    errs = []
    for sid in sorted(set(cur) | set(locked)):
        if sid not in cur:
            errs.append(f"{sid}: in the lock but has no skill content (a removed skill needs a major version note in CHANGELOG.md, then --update)")
        elif sid not in locked:
            errs.append(f"{sid}: new skill is not in the lock; run --update")
        elif cur[sid]["content_sha256"] != locked[sid]["content_sha256"]:
            if semver(cur[sid]["version"]) <= semver(locked[sid]["version"]):
                errs.append(f"{sid}: content changed but version is still {cur[sid]['version']}; bump it in registry/skill-content/{sid}.json")
            else:
                errs.append(f"{sid}: version bumped to {cur[sid]['version']}; run --update to record it")
        elif cur[sid]["version"] != locked[sid]["version"]:
            errs.append(f"{sid}: version changed without a content change ({locked[sid]['version']} -> {cur[sid]['version']}); revert it or run --update")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--update", action="store_true")
    a = ap.parse_args()
    if a.update:
        (ROOT / LOCK).write_text(json.dumps(current(ROOT), indent=2) + "\n", encoding="utf-8")
        print(f"wrote {LOCK} ({len(current(ROOT))} skills)")
        return 0
    errs = check()
    if errs:
        print("SKILL VERSION CHECK FAILED:")
        print("\n".join(f"- {e}" for e in errs))
        return 1
    print(f"SKILL VERSION CHECK PASSED: {len(current(ROOT))} skills match the lock.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
