import unittest

from runtime.specialist_gateway.controller import Decision, RoutingRequest
from runtime.specialist_gateway.github_loader import (
    CanonicalLoadError,
    load_canonical_snapshot,
    parse_archetype_registry,
    parse_certification_ledger,
    parse_project_adapter,
    parse_project_registry,
)


PROJECTS = '''
```text
PROJECT_ID: fechai
CANONICAL_NAME: FECH.AI
ALIASES:
- FECHAI
- fecha.ai
ADAPTER_PATH: projects/fechai/PROJECT_ADAPTER.md
STATUS: ACTIVE
```
'''

ARCHETYPES = '''
```text
ARCHETYPE_ID: documentation-auditor
CANONICAL_NAME: SES — Documentation Auditor
CONTRACT_PATH: archetypes/documentation-auditor/ARCHETYPE.md
RESOLUTION_STATUS: ACTIVE
LIFECYCLE_STATUS: READY
```
'''

CERTIFICATIONS = '''
| ARCHETYPE_ID | Certification | Current reason |
|---|---|---|
| `documentation-auditor` | `YES` | current |

## Documentation Auditor
```text
ARCHETYPE_ID = documentation-auditor
CURRENT_CANDIDATE = documentation-auditor-v1.1
CERTIFIED_FOR_ANY_PROJECT = YES
```
'''

ADAPTER = '''
```text
PROJECT_ID: fechai
PROJECT_NAME: FECH.AI
CANONICAL_SOURCE: GitHub repository wagnerjfjunior/fecha.ai
BOOTSTRAP_ENTRYPOINT: docs/bootstrap/INDEX.md
```

```text
SPECIALIST_ROLE_MAP:
- ROLE: documentation_audit
  ARCHETYPE_ID: documentation-auditor
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: docs/skills/auditor.md
  LEGACY_ALIASES: GPT0 / Old Auditor
```
'''


class FakeClient:
    def resolve_ref(self, branch="main"):
        return "abc123"

    def read_text(self, path, ref):
        return {
            "projects/REGISTRY.md": PROJECTS,
            "archetypes/REGISTRY.md": ARCHETYPES,
            "docs/SPECIALIST_CERTIFICATION_STATUS.md": CERTIFICATIONS,
            "projects/fechai/PROJECT_ADAPTER.md": ADAPTER,
        }[path]


class LoaderTests(unittest.TestCase):
    def test_l01_project_registry(self):
        records = parse_project_registry(PROJECTS)
        self.assertEqual("fechai", records[0].project_id)
        self.assertEqual(("FECHAI", "fecha.ai"), records[0].aliases)

    def test_l02_archetype_registry(self):
        records = parse_archetype_registry(ARCHETYPES)
        self.assertEqual("ACTIVE", records["documentation-auditor"].resolution_status)

    def test_l03_certification_ledger(self):
        records = parse_certification_ledger(CERTIFICATIONS)
        self.assertEqual("YES", records["documentation-auditor"].certification)
        self.assertIn("documentation-auditor-v1.1", records["documentation-auditor"].certified_subject)

    def test_l04_adapter_role_map(self):
        adapter = parse_project_adapter(ADAPTER, "projects/fechai/PROJECT_ADAPTER.md")
        self.assertEqual("documentation_audit", adapter.role_map[0].role)
        self.assertEqual(("GPT0", "Old Auditor"), adapter.role_map[0].legacy_aliases)

    def test_l05_snapshot_routes_with_resolved_ref(self):
        snapshot = load_canonical_snapshot(FakeClient())
        receipt = snapshot.gateway.route(RoutingRequest("fechai", "documentation_audit", "audit docs"))
        self.assertEqual("abc123", receipt.ses_ref)
        self.assertEqual(Decision.ROUTABLE, receipt.decision)
        self.assertFalse(receipt.mutation_authorized)

    def test_l06_unmapped_role_fails_closed(self):
        snapshot = load_canonical_snapshot(FakeClient())
        receipt = snapshot.gateway.route(RoutingRequest("fechai", "GPT0", "audit docs"))
        self.assertEqual(Decision.SPECIALIST_ROLE_NOT_ADOPTED, receipt.decision)

    def test_l07_missing_registry_records_fail_closed(self):
        with self.assertRaises(CanonicalLoadError):
            parse_project_registry("no records")


if __name__ == "__main__":
    unittest.main()
