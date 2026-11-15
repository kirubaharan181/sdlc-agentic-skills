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
