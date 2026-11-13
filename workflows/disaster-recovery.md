# Workflow: Disaster Recovery

## Trigger
Approved request for disaster recovery.

## Inputs
- request
- risk classification
- applicable artifacts

## Stages and dependencies
Stage IDs: 45, 53, 67, 68, 69, 79, 85, 110, 130, 131, 133, 138, 163, 164, 165. Stage order and gates are enforced by registry; independent work may run in parallel after prerequisites.

## Roles and skills
Agents: project-manager, full-stack-engineer, qa-lead, application-security-engineer, release-manager. Skills: master-orchestration, evidence-quality-gates, secure-change-control.

## Parallel tasks
- documentation and test planning after requirements approval

## Approval gates
- business
- requirements
- architecture
- qa
- security
- production-human-approval

## Outputs, failure handling, completion
Outputs: versioned artifacts, evidence bundle, final workflow report. Stop unsafe work; mark failed gate; create remediation/rollback path. Completion: Every included stage has PASS evidence or an approved, non-expired waiver.
