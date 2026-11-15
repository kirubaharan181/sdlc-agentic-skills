import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_demo_output_matches_documented_example():
    r = subprocess.run([sys.executable, "scripts/demo.py", "production-release"], cwd=ROOT, text=True, capture_output=True)
    assert r.returncode == 0
    assert r.stdout == (ROOT / "docs/examples/DEMO_production-release.txt").read_text(encoding="utf-8")
