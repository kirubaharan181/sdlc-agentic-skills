from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    result = subprocess.run([sys.executable, "scripts/validate.py"], cwd=ROOT, text=True)
    if result.returncode:
        return result.returncode
    semantic = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"], cwd=ROOT, text=True)
    if semantic.returncode:
        return semantic.returncode
    required = [
        "tests/fixtures/scenarios/new-inventory-web-app.md",
        "tests/fixtures/scenarios/production-bug-fix.md",
        "tests/fixtures/scenarios/security-vulnerability.md",
    ]
    missing = [p for p in required if not (ROOT / p).is_file()]
    if missing:
        print("TEST FAILED: missing scenario fixtures: " + ", ".join(missing))
        return 1
    print("TESTS PASSED: semantic clone fixtures, deterministic registry checks and 3 controlled scenario fixtures.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
