#!/usr/bin/env python3
"""Track documentation quality scores over time and fail on a regression.

Source of truth: reports/skill-quality/SCORE_HISTORY.csv, one row per skill per evaluator run. Scores are written only from a
real SkillEvaluator run; this script never produces a score. See docs/quality/QUALITY_MANAGEMENT.md.

  python3 scripts/check_quality_regression.py            compare each skill's latest run with its previous run
  python3 scripts/check_quality_regression.py --summary  print the latest scores and the average
  python3 scripts/check_quality_regression.py --add SKILL SCORE GRADE C D R E FINDINGS --date YYYY-MM-DD \\
        --source "SkillEvaluator <version>" --run-by "<who ran it>" --library-version "<git sha or tag>"
"""
from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import registry_io  # noqa: E402

HISTORY = "reports/skill-quality/SCORE_HISTORY.csv"
FIELDS = ["date", "skill", "score", "grade", "correctness", "discoverability", "reliability", "efficiency", "findings", "source", "evaluator_run_by", "library_version"]
SCORE_TOLERANCE = 0.5        # an overall drop larger than this fails
DIMENSION_TOLERANCE = 5      # a single dimension drop larger than this fails


def load(root: Path = ROOT) -> dict[str, list[dict]]:
    by: dict[str, list[dict]] = defaultdict(list)
    with (root / HISTORY).open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            by[row["skill"]].append(row)
    for rows in by.values():
        rows.sort(key=lambda r: r["date"])
    return by


def problems(root: Path = ROOT, score_tol: float = SCORE_TOLERANCE, dim_tol: float = DIMENSION_TOLERANCE) -> list[str]:
    by = load(root)
    errs = []
    skills = {s["skill_id"] for s in registry_io.load_skill_doc(root)["skills"]}
    for sid in sorted(skills - set(by)):
        errs.append(f"{sid}: no row in {HISTORY}")
    for sid in sorted(set(by) - skills):
        errs.append(f"{sid}: history row for an unknown skill")
    for sid, rows in sorted(by.items()):
        for r in rows:
            for k in ("score", "correctness", "discoverability", "reliability", "efficiency", "findings"):
                try:
                    float(r[k])
                except ValueError:
                    errs.append(f"{sid} {r['date']}: {k} is not a number")
            if not r["source"].strip():
                errs.append(f"{sid} {r['date']}: source is empty (say which evaluator run produced the score)")
        if len(rows) < 2:
            continue
        prev, last = rows[-2], rows[-1]
        if float(prev["score"]) - float(last["score"]) > score_tol:
            errs.append(f"{sid}: score fell {prev['score']} -> {last['score']} ({prev['date']} -> {last['date']})")
        for k in ("correctness", "discoverability", "reliability", "efficiency"):
            if float(prev[k]) - float(last[k]) > dim_tol:
                errs.append(f"{sid}: {k} fell {prev[k]} -> {last[k]}")
        if float(last["findings"]) > float(prev["findings"]):
            errs.append(f"{sid}: findings rose {prev['findings']} -> {last['findings']}")
    return errs


def summary(root: Path = ROOT) -> str:
    by = load(root)
    latest = {s: r[-1] for s, r in by.items()}
    scores = [float(r["score"]) for r in latest.values()]
    lines = [f"{'skill':32} {'score':>6} {'grade':>5} {'findings':>8}  date"]
    for s in sorted(latest):
        r = latest[s]
        lines.append(f"{s:32} {float(r['score']):6.1f} {r['grade']:>5} {r['findings']:>8}  {r['date']}")
    lines.append(f"\nskills: {len(scores)}  average: {sum(scores) / len(scores):.2f}  lowest: {min(scores):.1f}  highest: {max(scores):.1f}  at or above 97: {sum(x >= 97 for x in scores)}")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--summary", action="store_true")
    ap.add_argument("--add", nargs=8, metavar=("SKILL", "SCORE", "GRADE", "C", "D", "R", "E", "FINDINGS"))
    ap.add_argument("--date")
    ap.add_argument("--source", default="")
    ap.add_argument("--run-by", default="")
    ap.add_argument("--library-version", default="")
    a = ap.parse_args()
    if a.add:
        if not (a.date and a.source and a.run_by and a.library_version):
            ap.error("--add needs --date, --source, --run-by and --library-version so every score is traceable to a real run")
        with (ROOT / HISTORY).open("a", encoding="utf-8", newline="") as f:
            csv.writer(f).writerow([a.date, a.add[0], *a.add[1:], a.source, a.run_by, a.library_version])
        print(f"appended {a.add[0]} to {HISTORY}")
        return 0
    if a.summary:
        print(summary())
        return 0
    errs = problems()
    if errs:
        print("QUALITY REGRESSION CHECK FAILED:")
        print("\n".join(f"- {e}" for e in errs))
        return 1
    print(f"QUALITY REGRESSION CHECK PASSED: {len(load())} skills, no regression between the last two recorded runs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
