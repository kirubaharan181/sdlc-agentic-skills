"""Machine-readable scenarios: each states what a workflow must contain, in what order, and who approves."""
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = sorted((ROOT / "tests" / "scenarios").glob("*.json"))


@pytest.mark.parametrize("path", SCENARIOS, ids=[p.stem for p in SCENARIOS])
def test_scenario(path, data):
    sc = json.loads(path.read_text(encoding="utf-8"))
    wf = next(w for w in data["workflows"] if w["workflow_id"] == sc["workflow"])
    order = [s["stage"] for s in wf["steps"]]
    for sid in sc["stage_ids"]:
        assert sid in order, f"{sc['scenario_id']}: stage {sid} missing from workflow {wf['workflow_id']}"
    stages = {s["stage_id"]: s for s in data["stages"]}
    for sid, approver in sc["expected_approvers"].items():
        assert stages[int(sid)]["approver"] == approver
        assert int(sid) in [a["stage"] for a in wf["approval_points"]]
    for a, b in sc["expected_order"]:
        assert order.index(a) < order.index(b), f"{a} must come before {b}"

