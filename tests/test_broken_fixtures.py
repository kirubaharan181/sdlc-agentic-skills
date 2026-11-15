"""Break a copy of the repository on purpose; the validator or checker must fail with a specific message."""
import json

from conftest import edit_json, run_script


def test_clean_copy_passes(repo_copy):
    r = run_script(repo_copy, "validate.py")
    assert r.returncode == 0, r.stdout + r.stderr


def test_unknown_skill_reference_fails(repo_copy):
    edit_json(repo_copy / "registry/SDLC_STAGE_REGISTRY.json", lambda d: d["stages"][0].__setitem__("skills", ["no-such-skill"]))
    r = run_script(repo_copy, "check_references.py")
    assert r.returncode == 1 and "no-such-skill" in r.stdout


def test_identical_workflow_stage_lists_fail(repo_copy):
    src = json.loads((repo_copy / "registry/workflows/rollback.json").read_text())
    def clone(d):
        d["steps"] = src["steps"]; d["decisions"] = []; d["failure_paths"] = []; d["approval_points"] = []
    edit_json(repo_copy / "registry/workflows/bug-fix.json", clone)
    r = run_script(repo_copy, "validate.py")
    assert r.returncode == 1 and "identical stage list" in r.stdout


def test_workflow_cycle_fails(repo_copy):
    def cyc(d):
        d["steps"][0]["needs"] = [d["steps"][-1]["stage"]]
    edit_json(repo_copy / "registry/workflows/bug-fix.json", cyc)
    r = run_script(repo_copy, "validate.py")
    assert r.returncode != 0


def test_complete_without_content_fails(repo_copy):
    (repo_copy / "registry/stage-content/099.json").unlink()
    r = run_script(repo_copy, "validate.py")
    assert r.returncode != 0


def test_example_evidence_saying_pass_fails(repo_copy):
    p = next((repo_copy / "skills").rglob("examples/evidence-example.json"))
    edit_json(p, lambda d: d.update(status="PASS"))
    r = run_script(repo_copy, "validate.py")
    assert r.returncode == 1 and "must not say PASS" in r.stdout


def test_stale_generated_file_fails_build_check(repo_copy):
    p = repo_copy / "agents" / "sre.md"
    p.write_text(p.read_text() + "\nhand edit\n")
    r = run_script(repo_copy, "build.py", "--check")
    assert r.returncode != 0
