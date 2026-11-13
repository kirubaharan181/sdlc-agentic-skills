import subprocess
import sys


def test_registry_validator_passes():
    result = subprocess.run([sys.executable, "scripts/validate.py"], text=True, capture_output=True)
    assert result.returncode == 0, result.stdout + result.stderr
