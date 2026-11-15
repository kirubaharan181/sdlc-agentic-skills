# Evals

Cases follow the structure recommended in Anthropic's [skill authoring guide](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices#build-evaluations-first):
a query, the skills in play and the behaviors a good answer shows.

```
python3 evals/run_evals.py     # offline: checks every case against the registries
```

## Status
- 6 cases in `evals/cases/`. Their structure is checked in CI by `tests/test_evals.py`.
- **No model has been run against them yet.** `model_results` is `"not run"` in every case, and this repository
  publishes no score. Do not cite one.

## Running them for real
1. For each case, run the same query with and without the named skill loaded (a baseline), in a fresh session.
2. Judge each `expected_behavior` line yes or no; keep the transcripts.
3. Save a dated record to `evals/results/<date>-<model>-<eval_id>.json` with the model name, per-behavior verdicts and
   who judged. Only then may a README or release note mention a result, and it must link the record.
