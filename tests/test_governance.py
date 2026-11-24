"""Tests for the skill-intelligence and governance layer: selection, graph, risk tiers, versions, score history, policy files."""
import csv
import json
import re
from pathlib import Path

import check_quality_regression
import check_skill_versions
import registry_io
import select_skill
import skill_graph

ROOT = Path(__file__).resolve().parents[1]


def _content():
    return registry_io.load_skill_content(ROOT)


# --- selection engine -------------------------------------------------------------------------------------------------

def test_selection_incident_goes_first():
    r = select_skill.rank("production is down and customers cannot pay", ROOT)
    assert r["advice"] == "incident_first" and r["use"] == "incident-command"


def test_selection_single_skill_for_code_review():
    r = select_skill.rank("review this pull request", ROOT)
    assert r["advice"] == "single_skill" and r["use"] == "code-review-quality"


def test_selection_overlap_goes_to_orchestration():
    r = select_skill.rank("we need a release approval and rollback plan", ROOT)
    assert r["advice"] == "orchestrate" and r["use"] == "master-orchestration"


def test_selection_no_match_is_honest():
    r = select_skill.rank("bake a chocolate cake", ROOT)
    assert r["advice"] == "no_match" and r["use"] is None and r["ranked"] == []


# --- dependency graph and responsibilities ---------------------------------------------------------------------------

def _c(handoffs, owns=()):
    return {"handoffs": handoffs, "owns": list(owns)}


def test_forward_cycle_is_detected():
    c = {"a": _c([{"skill": "b", "artifact": "x"}]), "b": _c([{"skill": "a", "artifact": "y"}])}
    cycle = skill_graph.forward_cycle(c)
    assert cycle and cycle[0] == cycle[-1]


def test_feedback_edge_is_not_a_cycle():
    c = {"a": _c([{"skill": "b", "artifact": "x"}]), "b": _c([{"skill": "a", "artifact": "y", "feedback": True}])}
    assert skill_graph.forward_cycle(c) is None


def test_duplicate_responsibility_is_reported():
    c = {"a": _c([], ["deploy approval"]), "b": _c([], ["deploy approval"]), "c": _c([], ["triage"])}
    dup = skill_graph.duplicate_responsibilities(c)
    assert dup == {"deploy approval": ["a", "b"]}


def test_real_skill_graph_is_acyclic_with_unique_owners():
    c = _content()
    assert len(c) == 20
    assert skill_graph.forward_cycle(c) is None
    assert skill_graph.duplicate_responsibilities(c) == {}
    for sid, x in c.items():
        for h in x["handoffs"]:
            assert h["skill"] in c and h["skill"] != sid


# --- skill documentation rules ---------------------------------------------------------------------------------------

def test_descriptions_follow_rules():
    for sid, c in _content().items():
        d = c["description"]
        assert 50 <= len(d) <= 150, sid
        assert "use when" in d.lower() and "do not use" in d.lower(), sid


def test_rendered_skills_have_required_sections_and_metadata():
    sections = ["## Purpose", "## When to Use", "## When NOT to Use", "## Prerequisites and Requirements", "## Inputs and Outputs",
                "## Decision Rules", "## Quality Gates", "## Examples", "## Limitations", "## Troubleshooting"]
    files = sorted(ROOT.glob("skills/*/*/SKILL.md"))
    assert len(files) == 20
    for f in files:
        t = f.read_text(encoding="utf-8")
        assert t.startswith("---\nname: " + f.parent.name + "\n"), f
        assert "author: kirubaharan181" in t and "tags:" in t and "version:" in t, f
        for s in sections:
            assert s in t, (f, s)


# --- risk tiers and approvals ----------------------------------------------------------------------------------------

def test_every_approval_gated_stage_has_a_risk_tier(data):
    tiers = json.loads((ROOT / "registry/risk-tiers.json").read_text(encoding="utf-8"))
    gated = {str(s["stage_id"]) for s in data["stages"] if s["approval_required"]}
    assert gated <= set(tiers["stage_tiers"])
    assert set(tiers["stage_tiers"].values()) <= {t["id"] for t in tiers["tiers"]}


def test_approver_table_matches_registry(data):
    doc = (ROOT / "docs/governance/APPROVAL_ESCALATION_MATRIX.md").read_text(encoding="utf-8")
    expected: dict[str, set[int]] = {}
    for s in data["stages"]:
        if s["approval_required"]:
            expected.setdefault(s["approver"], set()).add(s["stage_id"])
    documented: dict[str, set[int]] = {}
    for m in re.finditer(r"^\| ([a-z-]+) \| ([0-9, ]+) \|$", doc, re.M):
        documented[m.group(1)] = {int(x) for x in m.group(2).split(",")}
    assert documented == expected


# --- skill versions and score history --------------------------------------------------------------------------------

def test_skill_versions_match_lock():
    assert check_skill_versions.check(ROOT) == []


def test_content_change_without_version_bump_fails(repo_copy):
    p = repo_copy / "registry/skill-content/code-review-quality.json"
    obj = json.loads(p.read_text(encoding="utf-8"))
    obj["limitations"].append("An extra limitation added without a version bump.")
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    errs = check_skill_versions.check(repo_copy)
    assert any("code-review-quality" in e and "version" in e for e in errs)


def test_score_history_has_baseline_and_no_regression():
    assert check_quality_regression.problems(ROOT) == []
    rows = list(csv.DictReader((ROOT / "reports/skill-quality/SCORE_HISTORY.csv").open(encoding="utf-8")))
    assert len(rows) >= 20 and all(r["source"].strip() for r in rows)


def test_score_drop_is_flagged(repo_copy):
    path = repo_copy / "reports/skill-quality/SCORE_HISTORY.csv"
    rows = list(csv.DictReader(path.open(encoding="utf-8", newline="")))
    base = next(r for r in rows if r["skill"] == "code-review-quality")
    worse = dict(base, date="2026-12-01", score=str(float(base["score"]) - 5), findings=str(int(base["findings"]) + 3))
    with path.open("a", encoding="utf-8", newline="") as f:
        csv.DictWriter(f, fieldnames=list(base)).writerow(worse)
    errs = check_quality_regression.problems(repo_copy)
    assert any("code-review-quality" in e and "score fell" in e for e in errs)
    assert any("findings rose" in e for e in errs)


# --- policy files ----------------------------------------------------------------------------------------------------

def test_license_is_full_mit_text():
    t = (ROOT / "LICENSE").read_text(encoding="utf-8")
    assert t.startswith("MIT License") and "Copyright (c) 2026" in t
    assert "WARRANTIES OF MERCHANTABILITY" in t and "NONINFRINGEMENT" in t


def test_security_policy_has_no_personal_email_and_no_certification_claim():
    t = (ROOT / "SECURITY.md").read_text(encoding="utf-8")
    assert not re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", t)
    assert "Report a vulnerability" in t and "not been" in t and "certified" in t


def test_contributing_covers_skill_workflow():
    t = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
    for needle in ("registry/skill-content", "check_skill_versions.py", "check_quality_regression.py", "MIT License"):
        assert needle in t


# --- standalone skill layout and valid frontmatter -------------------------------------------------------------------

def test_frontmatter_description_is_a_quoted_string_equal_to_the_source():
    content = _content()
    for f in sorted(ROOT.glob("skills/*/*/SKILL.md")):
        fm = f.read_text(encoding="utf-8").split("---\n")[1]
        line = next(x for x in fm.splitlines() if x.startswith("description: "))
        assert json.loads(line[len("description: "):]) == content[f.parent.name]["description"], f


def test_every_skill_is_standalone():
    """SKILL.md may link only to files inside its own folder, and those files must exist."""
    for f in sorted(ROOT.glob("skills/*/*/SKILL.md")):
        text = f.read_text(encoding="utf-8")
        for link in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", text):
            if link.startswith("http"):
                continue
            assert not link.startswith(".."), (f, link)
            assert (f.parent / link).exists(), (f, link)
        assert (f.parent / "references/CORE_PROCEDURE.md").exists(), f
        assert (f.parent / "references/HANDOFF_CONTRACT.md").exists(), f
        assert not (f.parent / "reference").exists() and not (f.parent / "examples").exists(), f


def test_descriptions_lead_with_the_trigger():
    for sid, c in _content().items():
        assert c["description"].startswith("Use when"), sid
        assert c["description"].lower().find("use when") < 60, sid


def test_score_history_rows_are_traceable():
    rows = list(csv.DictReader((ROOT / "reports/skill-quality/SCORE_HISTORY.csv").open(encoding="utf-8")))
    for r in rows:
        assert r["skill_version"] and r["source_commit"] and r["evaluator_version"], r


# --- Atelier dashboard (static snapshot) ----------------------------------------------------------------------------------

def _dashboard_data():
    import subprocess, sys
    path = ROOT / "dashboard/data/library.json"
    if not path.exists():
        subprocess.run([sys.executable, str(ROOT / "scripts/generate_dashboard_data.py")], check=True, cwd=ROOT)
    return json.loads(path.read_text(encoding="utf-8"))


def test_dashboard_snapshot_data_is_enriched_and_honest():
    d = _dashboard_data()
    assert d["skills"] and all(s.get("version") and "handoffs" in s and "quality" in s for s in d["skills"])
    assert sum(1 for s in d["stages"] if s.get("risk_tier")) == 19
    q = d["governance"]["qualitySummary"]
    assert q["skillsRecorded"] == len(d["skills"]) and q["note"]
    assert d["meta"]["sourceCommit"] and d["meta"]["sourceCommit"] != "local"
    assert d["meta"].get("notice")


def test_dashboard_page_is_accessible_static_snapshot():
    html = (ROOT / "dashboard/index.html").read_text(encoding="utf-8")
    assert 'class="skip"' in html and "Static snapshot" in html and 'tabindex="-1"' in html
    assert html.count('role="dialog"') >= 2 and 'role="status"' in html
    js = (ROOT / "dashboard/assets/app.js").read_text(encoding="utf-8")
    assert "Not publication approval" in js and "#sr tr[data-stage]" in js


# --- agent installer -------------------------------------------------------------------------------------------------------

def test_installer_copies_checks_and_detects_drift(tmp_path):
    import subprocess, sys
    run = lambda *a: subprocess.run([sys.executable, str(ROOT / "scripts/install.py"), *a], capture_output=True, text=True)
    r = run("--target", "opencode", "--dest", str(tmp_path), "--skill", "incident-command", "--skill", "code-review-quality")
    assert r.returncode == 0, r.stderr
    skill = tmp_path / ".opencode/skills/incident-command/SKILL.md"
    assert skill.exists() and (tmp_path / ".opencode/skills/code-review-quality").is_dir()
    assert run("--target", "opencode", "--dest", str(tmp_path), "--skill", "incident-command", "--check").returncode == 0
    assert "skip" in run("--target", "opencode", "--dest", str(tmp_path), "--skill", "incident-command").stdout
    skill.write_text(skill.read_text(encoding="utf-8") + "\nx", encoding="utf-8")
    assert run("--target", "opencode", "--dest", str(tmp_path), "--skill", "incident-command", "--check").returncode == 1
    assert run("--target", "codex", "--dest", str(tmp_path), "--skill", "nope").returncode != 0
    assert (tmp_path / ".agents").exists() is False  # dry-run and failures write nothing
    assert run("--target", "codex", "--dest", str(tmp_path), "--dry-run").returncode == 0
    assert (tmp_path / ".agents").exists() is False


def test_agent_guides_cover_codex_and_opencode():
    for name, token in (("CODEX_USAGE.md", ".agents/skills"), ("OPENCODE_USAGE.md", ".opencode/skills")):
        t = (ROOT / "docs/agent-guide" / name).read_text(encoding="utf-8")
        assert token in t and "scripts/install.py" in t and "not tested" in t.lower()


def test_dashboard_finder_matches_select_skill():
    import shutil, subprocess, sys
    node = shutil.which("node")
    if not node:
        import pytest
        pytest.skip("node not installed")
    sys.path.insert(0, str(ROOT / "scripts"))
    import select_skill
    subprocess.run([sys.executable, str(ROOT / "scripts/generate_dashboard_data.py")], check=True, cwd=ROOT, capture_output=True)
    js = (ROOT / "dashboard/assets/app.js").read_text(encoding="utf-8")
    start = js.index("function normQ"); end = js.index("function finder")
    reqs = ["plan a safe production rollout with rollback", "production is down", "zzzz qqq", "write a threat model and review the code",
            "define requirements and acceptance criteria", "set up monitoring and alerting with slo"]
    script = ("const S={d:JSON.parse(require('fs').readFileSync(process.argv[1],'utf8'))};" + js[start:end] +
              f"console.log(JSON.stringify({json.dumps(reqs)}.map(rankRequest)))")
    out = subprocess.run([node, "-e", script, str(ROOT / "dashboard/data/library.json")], capture_output=True, text=True, check=True)
    for req, got in zip(reqs, json.loads(out.stdout)):
        want = select_skill.rank(req)
        assert got["advice"] == want["advice"] and got["use"] == want["use"], req
        assert [(x["skill"], x["score"]) for x in got["ranked"]] == [(x["skill"], x["score"]) for x in want["ranked"]], req
