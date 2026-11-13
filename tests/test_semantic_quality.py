import unittest
from scripts.semantic_quality import find_near_duplicates, similarity


class SemanticQualityTests(unittest.TestCase):
    def test_name_only_clone_is_detected(self):
        first = """---
agent_id: api-architect
---
# API Architect

## Execution
Inspect the API contract, define resource schemas, verify compatibility and record migration decisions.
"""
        second = """---
agent_id: cloud-architect
---
# Cloud Architect

## Execution
Inspect the API contract, define resource schemas, verify compatibility and record migration decisions.
"""
        self.assertGreaterEqual(similarity(first, second), 0.88)
        self.assertEqual(len(find_near_duplicates({"api": first, "cloud": second})), 1)

    def test_distinct_domain_procedures_are_not_clones(self):
        api = "Define OpenAPI schemas, auth scopes, idempotency, versioning and consumer migration tests."
        audit = "Select risk-based control samples, inspect operating evidence, rate findings and verify corrective action."
        self.assertLess(similarity(api, audit), 0.70)
        self.assertEqual(find_near_duplicates({"api": api, "audit": audit}), [])

    def test_small_wording_change_does_not_hide_duplicate(self):
        first = "Review the API schema and test compatibility before approving the migration."
        second = "Review the API schema and verify compatibility before approving the migration."
        self.assertGreaterEqual(similarity(first, second), 0.88)


if __name__ == "__main__":
    unittest.main()
