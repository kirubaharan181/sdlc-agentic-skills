"""Unit tests for the registry loader, reference checker, duplication audit and renderers."""
import json
from pathlib import Path

import audit_duplication
import check_references
import registry_io
import render_skills


def test_counts(data):
    assert (len(data["stages"]), len(data["skills"]), len(data["agents"]), len(data["workflows"])) == (190, 20, 74, 23)


def test_stage_ids_are_1_to_190_in_order(data):
    assert [s["stage_id"] for s in data["stages"]] == list(range(1, 191))


def test_agents_derived_from_raci(data):
    for s in data["stages"]:
        assert s["agents"][0] == s["raci"]["accountable"]
        assert set(s["agents"]) == {s["raci"]["accountable"], *s["raci"]["responsible"]}


def test_no_unresolved_references_or_orphans(data):
    r = check_references.check(data)
    assert r["unresolved"] == [] and r["inconsistent"] == []
    assert r["orphans"]["agents_not_in_any_stage_or_workflow"] == []
    assert r["orphans"]["skills_unused"] == []


def test_workflow_levels_follow_needs():
    steps = [{"stage": 1, "needs": []}, {"stage": 2, "needs": [1]}, {"stage": 3, "needs": [1]}, {"stage": 4, "needs": [2, 3]}]
    assert registry_io._levels(steps) == {1: 1, 2: 2, 3: 2, 4: 3}


def test_new_product_development_has_all_stages(data):
    w = next(w for w in data["workflows"] if w["workflow_id"] == "new-product-development")
    assert sorted(w["stages"]) == list(range(1, 191))


def test_no_two_workflows_share_a_stage_list(data):
    lists = [tuple(sorted(w["stages"])) for w in data["workflows"]]
    assert len(lists) == len(set(lists))


def test_approvers_are_humans_not_agents(data):
    agent_ids = {a["agent_id"] for a in data["agents"]}
    for s in data["stages"]:
        if s["approval_required"]:
            assert s["approver"] not in agent_ids and s.get("approval_rationale")


def test_complete_stages_have_full_content(data):
    complete = [s for s in data["stages"] if s["status"] == "complete"]
    assert len(complete) == json.loads((Path(__file__).parent / 'golden' / 'metrics.json').read_text())['stages_complete']
    for s in complete:
        assert len(s["execution_instructions"]) >= 4 and s["failure_modes"] and s["entry_criteria"]
        assert s["worked_example"].startswith("ILLUSTRATIVE")


def test_description_is_third_person_and_bounded(data):
    stages = data["stages"]
    d = render_skills.description("Reduce risk.", stages[:20])
    assert len(d) <= 1024 and d.startswith("Provides") and "Use when" in d


def test_evidence_example_is_never_pass(data):
    st = [s for s in data["stages"] if s["status"] == "complete"][:1]
    rec = json.loads(render_skills.render_evidence_example("x", st))
    assert rec["example"] is True and rec["status"] == "ILLUSTRATIVE_ONLY"


def test_normalise_strips_own_name(tmp_path):
    p = tmp_path / "foo-bar.md"
    assert "foo" not in audit_duplication.normalise("# Foo Bar\nFoo Bar does things " * 3, p)


def test_exact_duplicates_found(tmp_path):
    (tmp_path / "a.txt").write_text("same")
    (tmp_path / "b.txt").write_text("same")
    (tmp_path / "c.txt").write_text("other")
    assert audit_duplication.exact_duplicates(tmp_path) == [["a.txt", "b.txt"]]


def test_repo_has_no_exact_duplicate_files():
    assert audit_duplication.exact_duplicates(Path(__file__).resolve().parents[1]) == []
