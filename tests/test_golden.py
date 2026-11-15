"""Golden numbers. If one changes on purpose, update tests/golden/metrics.json in the same commit and say why."""
import json
from pathlib import Path

import generate_reports

GOLDEN = Path(__file__).resolve().parent / "golden" / "metrics.json"


def test_metrics_match_golden(data):
    m = generate_reports.metrics(data)
    want = json.loads(GOLDEN.read_text())
    for k, v in want.items():
        assert m[k] == v, f"{k}: {m[k]!r} != golden {v!r}"


def test_readme_states_the_measured_completeness(data):
    m = generate_reports.metrics(data)
    readme = (GOLDEN.parents[2] / "README.md").read_text(encoding="utf-8")
    assert f"**{m['stages_complete']} of {m['stages_total']} (" in readme, "README completeness line is stale; update it"
    assert f"The other {m['stages_stub']} are marked" in readme
