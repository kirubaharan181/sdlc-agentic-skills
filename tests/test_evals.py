import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_eval_cases_are_structurally_valid():
    r = subprocess.run([sys.executable, "evals/run_evals.py"], cwd=ROOT, text=True, capture_output=True)
    assert r.returncode == 0, r.stdout


def test_no_eval_claims_a_model_result():
    import json

    for p in (ROOT / "evals" / "cases").glob("*.json"):
        assert json.loads(p.read_text())["model_results"] == "not run"
