#!/usr/bin/env python3
"""Check eval cases against the registries (offline), and print a result template for model runs.

What this verifies: each case names a real workflow, skill and stages that belong together.
What it does NOT do: call a model. `model_results` stays "not run" until a person runs the cases against a model
and records dated results in evals/results/ (see evals/README.md). No score is reported by this script.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import registry_io  # noqa: E402


def main() -> int:
    data = registry_io.load_all(ROOT)
    wfs = {w["workflow_id"]: w for w in data["workflows"]}
    skills = {s["skill_id"] for s in data["skills"]}
    bad = []
    cases = sorted((ROOT / "evals" / "cases").glob("*.json"))
    for p in cases:
        c = json.loads(p.read_text(encoding="utf-8"))
        if c["workflow"] not in wfs:
            bad.append(f"{p.name}: unknown workflow {c['workflow']}")
            continue
        for s in c["skills"]:
            if s not in skills:
                bad.append(f"{p.name}: unknown skill {s}")
        for sid in c["stage_ids"]:
            if sid not in wfs[c["workflow"]]["stages"]:
                bad.append(f"{p.name}: stage {sid} is not in workflow {c['workflow']}")
        if len(c["expected_behavior"]) < 2:
            bad.append(f"{p.name}: needs at least two expected behaviors")
    print(f"eval cases: {len(cases)}; structural problems: {len(bad)}; model runs recorded: "
          f"{len(list((ROOT / 'evals' / 'results').glob('*.json'))) if (ROOT / 'evals' / 'results').is_dir() else 0}")
    for b in bad:
        print("  PROBLEM", b)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
