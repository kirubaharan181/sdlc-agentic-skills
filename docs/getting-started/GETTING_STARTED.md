# Getting Started

1. Clone the repository and run `python scripts/validate.py`.
2. Select a workflow from `registry/WORKFLOW_REGISTRY.yaml`.
3. Resolve stages in `SDLC_STAGE_REGISTRY.yaml`; load only the relevant category skill.
4. Create evidence records for each completed gate.
5. Obtain human approval before any sensitive operation.

The registry uses JSON syntax inside `.yaml` files, which is valid YAML 1.2 and supports dependency-free validation.
