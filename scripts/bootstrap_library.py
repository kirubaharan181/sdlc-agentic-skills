"""Safe entry point for canonical library regeneration and verification.

Normal mode writes generated artifacts. Check mode regenerates inside a temporary
copy and compares expected bytes with the working tree; it never mutates the checkout.
"""
import argparse
import shutil
import tempfile
from pathlib import Path

import rebuild_library


def generated_files(root: Path):
    files = [
        root / "registry/SDLC_STAGE_REGISTRY.yaml",
        root / "registry/AGENT_REGISTRY.yaml",
        root / "registry/WORKFLOW_REGISTRY.yaml",
    ]
    files += list((root / "agents").glob("*.md"))
    files += list((root / "workflows").glob("*.md"))
    files += list((root / "skills").rglob("SKILL.md"))
    files += list((root / "skills").rglob("STAGE_PLAYBOOK.md"))
    return sorted(p for p in files if p.exists())


def main():
    parser = argparse.ArgumentParser(description="Regenerate canonical specialist library artifacts.")
    parser.add_argument("--check", action="store_true", help="Compare deterministic output without modifying the checkout.")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]

    if not args.check:
        rebuild_library.main()
        return 0

    with tempfile.TemporaryDirectory(prefix="sdlc-library-check-") as temp:
        temp_root = Path(temp) / "repository"
        shutil.copytree(
            root,
            temp_root,
            ignore=shutil.ignore_patterns(".git", ".venv", "__pycache__", ".pytest_cache"),
        )
        rebuild_library.ROOT = temp_root
        rebuild_library.main()

        actual = {p.relative_to(root): p.read_bytes() for p in generated_files(root)}
        expected = {p.relative_to(temp_root): p.read_bytes() for p in generated_files(temp_root)}
        changed = sorted(
            str(path)
            for path in set(actual) | set(expected)
            if actual.get(Path(path)) != expected.get(Path(path))
        )

    if changed:
        print("GENERATOR CHECK FAILED: generated content differs:")
        print("\n".join(f"- {path}" for path in changed[:40]))
        return 1

    print("GENERATOR CHECK PASSED: deterministic output matches; checkout was not modified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
