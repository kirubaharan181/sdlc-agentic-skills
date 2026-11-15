# Quickstart (about five minutes)

```
git clone https://github.com/kirubaharan181/sdlc-agentic-skills && cd sdlc-agentic-skills
pip install jsonschema pytest
make all                      # build, validate, check references and links, run tests, check generated files
make demo                     # plan for the production-release workflow
python3 scripts/demo.py --list
python3 scripts/demo.py bug-fix
cat dist/COVERAGE_REPORT.md   # honest completeness numbers
```

What `make demo` shows: ordered steps, which can run in parallel, who owns each, which need a named human approval,
decisions and failure paths, and how many steps have real content versus stub. A recorded run is in
[docs/examples/DEMO_production-release.txt](../examples/DEMO_production-release.txt) and a test keeps it current.

Using it with an agent: point the agent at `skills/` and `agents/`, and give it a workflow from `workflows/`.
Platform adapters are documented but not tested; see [adapters/COMPATIBILITY.md](../../adapters/COMPATIBILITY.md).
