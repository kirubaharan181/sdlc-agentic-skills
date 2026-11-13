# Testing Standard

Use a risk-based test strategy. Each acceptance criterion maps to one or more deterministic tests or an explicit justified manual verification. Unit tests verify local behavior, integration tests verify boundaries, contract/API tests verify compatibility, E2E tests verify critical journeys, and performance/security tests verify non-functional risks.

Reports must state command, environment, revision, duration, totals, failures/skips, known limitations, and artifact path. Do not narrow a suite, delete tests, or mark flaky behavior passed merely to obtain green CI.
