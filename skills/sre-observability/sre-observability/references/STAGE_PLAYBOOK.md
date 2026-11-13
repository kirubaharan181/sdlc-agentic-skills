# Reliability and observability — Stage Playbook

> Generated from the canonical stage registry. Use the parent skill first, then load only the relevant stage entry.

## 153. Application Monitoring

**Purpose:** provide actionable observability and service-level control

**Procedure:**
- Instrument golden signals and key business transactions with stable service/environment labels.
- Correlate logs, metrics and traces using request IDs while excluding secrets and sensitive payloads.
- Define SLI/SLO windows, burn-rate alerts, ownership, runbooks and paging policy.
- Test alert routing and diagnostic usefulness; remove noisy or unactionable alerts.

**Inputs:** service map and critical user journeys, SLO and alert thresholds, telemetry and privacy requirements
**Artifact:** telemetry specification
**Verification:** SRE review and alert simulation.
**Handoff:** Transfer telemetry specification with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 154. Infrastructure Monitoring

**Purpose:** provide actionable observability and service-level control

**Procedure:**
- Instrument golden signals and key business transactions with stable service/environment labels.
- Correlate logs, metrics and traces using request IDs while excluding secrets and sensitive payloads.
- Define SLI/SLO windows, burn-rate alerts, ownership, runbooks and paging policy.
- Test alert routing and diagnostic usefulness; remove noisy or unactionable alerts.

**Inputs:** service map and critical user journeys, SLO and alert thresholds, telemetry and privacy requirements
**Artifact:** telemetry specification
**Verification:** SRE review and alert simulation.
**Handoff:** Transfer telemetry specification with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 155. Centralized Logging

**Purpose:** provide actionable observability and service-level control

**Procedure:**
- Instrument golden signals and key business transactions with stable service/environment labels.
- Correlate logs, metrics and traces using request IDs while excluding secrets and sensitive payloads.
- Define SLI/SLO windows, burn-rate alerts, ownership, runbooks and paging policy.
- Test alert routing and diagnostic usefulness; remove noisy or unactionable alerts.

**Inputs:** service map and critical user journeys, SLO and alert thresholds, telemetry and privacy requirements
**Artifact:** telemetry specification
**Verification:** SRE review and alert simulation.
**Handoff:** Transfer telemetry specification with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 156. Metrics Monitoring

**Purpose:** provide actionable observability and service-level control

**Procedure:**
- Instrument golden signals and key business transactions with stable service/environment labels.
- Correlate logs, metrics and traces using request IDs while excluding secrets and sensitive payloads.
- Define SLI/SLO windows, burn-rate alerts, ownership, runbooks and paging policy.
- Test alert routing and diagnostic usefulness; remove noisy or unactionable alerts.

**Inputs:** service map and critical user journeys, SLO and alert thresholds, telemetry and privacy requirements
**Artifact:** telemetry specification
**Verification:** SRE review and alert simulation.
**Handoff:** Transfer telemetry specification with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 157. Distributed Tracing

**Purpose:** provide actionable observability and service-level control

**Procedure:**
- Instrument golden signals and key business transactions with stable service/environment labels.
- Correlate logs, metrics and traces using request IDs while excluding secrets and sensitive payloads.
- Define SLI/SLO windows, burn-rate alerts, ownership, runbooks and paging policy.
- Test alert routing and diagnostic usefulness; remove noisy or unactionable alerts.

**Inputs:** service map and critical user journeys, SLO and alert thresholds, telemetry and privacy requirements
**Artifact:** telemetry specification
**Verification:** SRE review and alert simulation.
**Handoff:** Transfer telemetry specification with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 158. Alert Management

**Purpose:** provide actionable observability and service-level control

**Procedure:**
- Instrument golden signals and key business transactions with stable service/environment labels.
- Correlate logs, metrics and traces using request IDs while excluding secrets and sensitive payloads.
- Define SLI/SLO windows, burn-rate alerts, ownership, runbooks and paging policy.
- Test alert routing and diagnostic usefulness; remove noisy or unactionable alerts.

**Inputs:** service map and critical user journeys, SLO and alert thresholds, telemetry and privacy requirements
**Artifact:** telemetry specification
**Verification:** SRE review and alert simulation.
**Handoff:** Transfer telemetry specification with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 159. Uptime Monitoring

**Purpose:** provide actionable observability and service-level control

**Procedure:**
- Instrument golden signals and key business transactions with stable service/environment labels.
- Correlate logs, metrics and traces using request IDs while excluding secrets and sensitive payloads.
- Define SLI/SLO windows, burn-rate alerts, ownership, runbooks and paging policy.
- Test alert routing and diagnostic usefulness; remove noisy or unactionable alerts.

**Inputs:** service map and critical user journeys, SLO and alert thresholds, telemetry and privacy requirements
**Artifact:** telemetry specification
**Verification:** SRE review and alert simulation.
**Handoff:** Transfer telemetry specification with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 160. SLA/SLO Management

**Purpose:** provide actionable observability and service-level control

**Procedure:**
- Instrument golden signals and key business transactions with stable service/environment labels.
- Correlate logs, metrics and traces using request IDs while excluding secrets and sensitive payloads.
- Define SLI/SLO windows, burn-rate alerts, ownership, runbooks and paging policy.
- Test alert routing and diagnostic usefulness; remove noisy or unactionable alerts.

**Inputs:** service map and critical user journeys, SLO and alert thresholds, telemetry and privacy requirements
**Artifact:** telemetry specification
**Verification:** SRE review and alert simulation.
**Handoff:** Transfer telemetry specification with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 161. Capacity Planning

**Purpose:** provide actionable observability and service-level control

**Procedure:**
- Instrument golden signals and key business transactions with stable service/environment labels.
- Correlate logs, metrics and traces using request IDs while excluding secrets and sensitive payloads.
- Define SLI/SLO windows, burn-rate alerts, ownership, runbooks and paging policy.
- Test alert routing and diagnostic usefulness; remove noisy or unactionable alerts.

**Inputs:** service map and critical user journeys, SLO and alert thresholds, telemetry and privacy requirements
**Artifact:** telemetry specification
**Verification:** SRE review and alert simulation.
**Handoff:** Transfer telemetry specification with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 162. Incident Detection

**Purpose:** restore service and convert failure evidence into prevention

**Procedure:**
- Establish commander, severity, scribe and communications channel; preserve a timestamped timeline.
- Assess customer impact and contain safely before attempting speculative fixes.
- Use telemetry and controlled hypotheses to isolate contributing causes; record evidence and uncertainty.
- Verify recovery against user-facing signals, then assign blameless corrective actions with owners and dates.

**Inputs:** incident signals and timeline, severity and command policy, service dependency and recovery data
**Artifact:** incident timeline
**Verification:** Incident commander and service owner review.
**Handoff:** Transfer incident timeline with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 163. Incident Response

**Purpose:** restore service and convert failure evidence into prevention

**Procedure:**
- Establish commander, severity, scribe and communications channel; preserve a timestamped timeline.
- Assess customer impact and contain safely before attempting speculative fixes.
- Use telemetry and controlled hypotheses to isolate contributing causes; record evidence and uncertainty.
- Verify recovery against user-facing signals, then assign blameless corrective actions with owners and dates.

**Inputs:** incident signals and timeline, severity and command policy, service dependency and recovery data
**Artifact:** incident timeline
**Verification:** Incident commander and service owner review.
**Handoff:** Transfer incident timeline with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 164. Root Cause Analysis

**Purpose:** restore service and convert failure evidence into prevention

**Procedure:**
- Establish commander, severity, scribe and communications channel; preserve a timestamped timeline.
- Assess customer impact and contain safely before attempting speculative fixes.
- Use telemetry and controlled hypotheses to isolate contributing causes; record evidence and uncertainty.
- Verify recovery against user-facing signals, then assign blameless corrective actions with owners and dates.

**Inputs:** incident signals and timeline, severity and command policy, service dependency and recovery data
**Artifact:** incident timeline
**Verification:** Incident commander and service owner review.
**Handoff:** Transfer incident timeline with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 165. Postmortem

**Purpose:** restore service and convert failure evidence into prevention

**Procedure:**
- Establish commander, severity, scribe and communications channel; preserve a timestamped timeline.
- Assess customer impact and contain safely before attempting speculative fixes.
- Use telemetry and controlled hypotheses to isolate contributing causes; record evidence and uncertainty.
- Verify recovery against user-facing signals, then assign blameless corrective actions with owners and dates.

**Inputs:** incident signals and timeline, severity and command policy, service dependency and recovery data
**Artifact:** incident timeline
**Verification:** Incident commander and service owner review.
**Handoff:** Transfer incident timeline with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 166. Reliability Improvement

**Purpose:** restore service and convert failure evidence into prevention

**Procedure:**
- Establish commander, severity, scribe and communications channel; preserve a timestamped timeline.
- Assess customer impact and contain safely before attempting speculative fixes.
- Use telemetry and controlled hypotheses to isolate contributing causes; record evidence and uncertainty.
- Verify recovery against user-facing signals, then assign blameless corrective actions with owners and dates.

**Inputs:** incident signals and timeline, severity and command policy, service dependency and recovery data
**Artifact:** incident timeline
**Verification:** Incident commander and service owner review.
**Handoff:** Transfer incident timeline with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.
