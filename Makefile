.PHONY: build check validate test refs audit all
PY ?= python3

build:      ## regenerate everything derived (registries' derived fields, agent/workflow/skill md, dist/, dashboard data)
	$(PY) scripts/build.py
check:      ## fail if committed generated files are stale or the build is non-deterministic
	$(PY) scripts/build.py --check
validate:   ## structural, schema and content validation
	$(PY) scripts/validate.py
refs:       ## cross-reference resolution
	$(PY) scripts/check_references.py
audit:      ## duplication report
	$(PY) scripts/audit_duplication.py
test:       ## unit and regression tests
	$(PY) scripts/run_tests.py
all: build validate refs test check
