# Good first issues (drafts)

Drafts only: not yet opened on GitHub. Each is one stub stage to turn into real content.

Shared recipe: copy `registry/stage-content/099.json`, rewrite every field for the stage, run `make all`. Rules: at least 4 ordered steps,
at least 2 failure modes, a worked example starting with `ILLUSTRATIVE`, and no commands that point at scripts that do not exist.

## 1. Write stage 102: Container Security
Create `registry/stage-content/102.json` with `"status": "complete"`. Done when `make all` passes and the stage shows `complete` in `python3 scripts/demo.py` for a workflow that includes it.

## 2. Write stage 72: Dependency Review
Create `registry/stage-content/072.json` with `"status": "complete"`. Done when `make all` passes and the stage shows `complete` in `python3 scripts/demo.py` for a workflow that includes it.

## 3. Write stage 90: Accessibility Testing
Create `registry/stage-content/090.json` with `"status": "complete"`. Done when `make all` passes and the stage shows `complete` in `python3 scripts/demo.py` for a workflow that includes it.

## 4. Write stage 112: Automated Test Pipeline
Create `registry/stage-content/112.json` with `"status": "complete"`. Done when `make all` passes and the stage shows `complete` in `python3 scripts/demo.py` for a workflow that includes it.

## 5. Write stage 120: Environment Provisioning
Create `registry/stage-content/120.json` with `"status": "complete"`. Done when `make all` passes and the stage shows `complete` in `python3 scripts/demo.py` for a workflow that includes it.

## 6. Write stage 130: Staging Deployment
Create `registry/stage-content/130.json` with `"status": "complete"`. Done when `make all` passes and the stage shows `complete` in `python3 scripts/demo.py` for a workflow that includes it.

## 7. Write stage 150: Auto Scaling
Create `registry/stage-content/150.json` with `"status": "complete"`. Done when `make all` passes and the stage shows `complete` in `python3 scripts/demo.py` for a workflow that includes it.

## 8. Write stage 166: Reliability Improvement
Create `registry/stage-content/166.json` with `"status": "complete"`. Done when `make all` passes and the stage shows `complete` in `python3 scripts/demo.py` for a workflow that includes it.

## 9. Write stage 170: Bug Fixing
Create `registry/stage-content/170.json` with `"status": "complete"`. Done when `make all` passes and the stage shows `complete` in `python3 scripts/demo.py` for a workflow that includes it.

## 10. Write stage 185: Compliance Auditing
Create `registry/stage-content/185.json` with `"status": "complete"`. Done when `make all` passes and the stage shows `complete` in `python3 scripts/demo.py` for a workflow that includes it.

## 11. Write stage 34: Architecture Review
Create `registry/stage-content/034.json` with `"status": "complete"`. Done when `make all` passes and the stage shows `complete` in `python3 scripts/demo.py` for a workflow that includes it.

## 12. Write stage 16: User Journey Mapping
Create `registry/stage-content/016.json` with `"status": "complete"`. Done when `make all` passes and the stage shows `complete` in `python3 scripts/demo.py` for a workflow that includes it.

## 13. Run one eval against a model
Follow `evals/README.md`, save a dated result in `evals/results/`, and open a pull request. Do not edit the case files to make a model pass.

## 14. Add a scenario
Add a JSON file in `tests/scenarios/` for a workflow not yet covered (for example `feature-development`). `make test` must pass.

## 15. Test one adapter and log it
Install the library into one agent tool listed in `adapters/COMPATIBILITY.md`, run a real task, and attach a dated log. Only then may its status change from "documented".
