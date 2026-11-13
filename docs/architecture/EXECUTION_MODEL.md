# Execution Model

The orchestrator classifies a request, selects a workflow, resolves stage dependencies, assigns a role and skills, and requires structured evidence before advancing a gate. It may parallelize only independent tasks; it never replaces a specialist approval or authorizes itself for sensitive work. Gate statuses are `NOT_STARTED`, `IN_PROGRESS`, `PASS`, `FAIL`, `BLOCKED`, `INCONCLUSIVE`, `NEEDS_HUMAN_APPROVAL`, and `WAIVED`. A waiver has a reason, risk, approver, date, and expiry/review condition.

```text
request -> classify -> workflow -> prerequisite checks -> stage execution
        -> evidence -> independent verification -> gate -> handoff -> report
```
