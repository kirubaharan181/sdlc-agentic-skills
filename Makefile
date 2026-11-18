.PHONY: build check validate test refs audit links demo all governance select
PY ?= python3

build:      ## regenerate everything derived (registries' derived fields, agent/workflow/skill md, dist/, dashboard data)
	$(PY) scripts/build.py
check:      ## fail if committed generated files are stale or the build is non-deterministic
	$(PY) scripts/build.py --check
validate:   ## structural, schema and content validation
	$(PY) scripts/validate.py
refs:       ## cross-reference resolution
	$(PY) scripts/check_references.py
links:      ## relative Markdown links resolve
	$(PY) scripts/check_links.py
audit:      ## duplication report
	$(PY) scripts/audit_duplication.py
test:       ## pytest (unit, golden, scenario, broken-fixture) plus legacy fixtures
	$(PY) -m pytest -q
	$(PY) scripts/run_tests.py
governance: ## skill versions, quality regression, templates
	$(PY) scripts/check_skill_versions.py
	$(PY) scripts/check_quality_regression.py
	$(PY) scripts/trace_evidence.py --templates
select:     ## rank skills for a request (REQ="...")
	$(PY) scripts/select_skill.py "$(REQ)"
all: build validate refs links governance test check
demo:       ## print the execution plan for a workflow (WORKFLOW=bug-fix to change)
	$(PY) scripts/demo.py $(WORKFLOW)
