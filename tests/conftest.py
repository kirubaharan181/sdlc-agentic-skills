import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


@pytest.fixture(scope="session")
def data():
    import registry_io

    return registry_io.load_all(ROOT)


@pytest.fixture
def repo_copy(tmp_path):
    """A throwaway copy of the repository that a test may break on purpose."""
    dst = tmp_path / "repo"
    shutil.copytree(ROOT, dst, ignore=shutil.ignore_patterns(".git", "dist", "__pycache__", ".pytest_cache", "node_modules"))
    return dst


def run_script(repo: Path, script: str, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(repo / "scripts" / script), *args], cwd=repo, text=True, capture_output=True)


def edit_json(path: Path, fn) -> None:
    obj = json.loads(path.read_text(encoding="utf-8"))
    fn(obj)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
