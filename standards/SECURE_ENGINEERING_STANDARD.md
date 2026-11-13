# Secure Engineering Standard

## Baseline

Classify data, verify identity at every trust boundary, enforce authorization server-side, use parameterized queries, validate input by allowlist, encode output for its target context, and keep secrets out of code, logs, test evidence, and prompts. Threat-model meaningful changes before implementation.

## Evidence

Record SAST/SCA/secrets/container/IaC scan command, tool version, target revision, report location, finding disposition, owner, due date, and independent verification. A scan with unavailable rules, partial scope, or failed upload is `INCONCLUSIVE`, not PASS.

## Release block conditions

Block release for an unresolved critical finding, exploitable authentication/authorization defect, exposed credential, unsupported internet-facing component, unapproved data-processing change, or missing incident/rollback ownership.
