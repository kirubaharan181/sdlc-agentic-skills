#!/usr/bin/env python3
"""Skill selection engine: rank skills for a request using the authored keywords, tags and stage names.

  python3 scripts/select_skill.py "plan a safe production rollout with rollback"
  python3 scripts/select_skill.py --json "..."

It is a deterministic word matcher. It does not understand meaning, so treat the output as a suggestion and read the
chosen skill's "When NOT to Use" section. When two or more skills score close together, or the request spans stages,
it recommends `master-orchestration` to route and order the work.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import registry_io  # noqa: E402

CLOSE = 0.6          # a second skill within this share of the top score means "several skills"
INCIDENT = ("incident", "outage", "sev1", "sev2", "service down", "war room", "incident commander",
            "production is down", "production down", "site is down", "site down", "is down in production")


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def _terms(root: Path) -> dict[str, dict[str, float]]:
    content = registry_io.load_skill_content(root)
    stages = registry_io.load_stage_doc(root)["stages"]
    out: dict[str, dict[str, float]] = {}
    for sid, c in content.items():
        t: dict[str, float] = {}
        for k in c["keywords"]:
            t[_norm(k)] = 3.0
        for k in c["tags"]:
            t.setdefault(_norm(k), 1.5)
        for s in stages:
            if sid in s["skills"]:
                t.setdefault(_norm(s["stage_name"]), 2.0)
        out[sid] = t
    return out


def rank(request: str, root: Path = ROOT) -> dict:
    q = " " + _norm(request) + " "
    scores: dict[str, float] = {}
    why: dict[str, list[str]] = {}
    for sid, terms in _terms(root).items():
        for term, w in terms.items():
            if term and f" {term} " in q:
                scores[sid] = scores.get(sid, 0.0) + w
                why.setdefault(sid, []).append(term)
    ranked = sorted(scores, key=lambda s: (-scores[s], s))
    top = scores[ranked[0]] if ranked else 0.0
    close = [s for s in ranked if top and scores[s] >= CLOSE * top]
    advice = "no_match"
    if any(f" {_norm(w)} " in q for w in INCIDENT):
        advice = "incident_first"
    elif len(close) > 1:
        advice = "orchestrate"
    elif ranked:
        advice = "single_skill"
    return {"request": request, "advice": advice,
            "ranked": [{"skill": s, "score": scores[s], "matched": sorted(why[s])} for s in ranked[:5]],
            "use": ("incident-command" if advice == "incident_first" else "master-orchestration" if advice == "orchestrate" else ranked[0] if ranked else None)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("request")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    r = rank(a.request)
    if a.json:
        print(json.dumps(r, indent=2))
    elif r["advice"] != "incident_first" and not r["ranked"]:
        print("No skill matched. Ask for more detail, or start with master-orchestration.")
    else:
        print(f"Advice: {r['advice']} -> {r['use']}")
        for x in r["ranked"]:
            print(f"  {x['score']:>5.1f}  {x['skill']}  (matched: {', '.join(x['matched'])})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
