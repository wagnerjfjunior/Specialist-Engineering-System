import unittest

from runtime.specialist_gateway.controller import (
    ArchetypeRecord,
    CertificationRecord,
    Decision,
    ProjectAdapter,
    ProjectRecord,
    RoleMapping,
    RoutingRequest,
    RuntimeEnforcementGateway,
)


class RuntimeGatewayTests(unittest.TestCase):
    def make_gateway(self, *, certification="YES", fingerprint="CURRENT", active=True, bootstrap="docs/bootstrap/INDEX.md"):
        projects = (
            ProjectRecord("fechai", "FECH.AI", ("FECHAI", "fecha.ai"), "projects/fechai/PROJECT_ADAPTER.md"),
            ProjectRecord("other", "Other Project", (), "projects/other/PROJECT_ADAPTER.md"),
        )
        adapters = {
            "projects/fechai/PROJECT_ADAPTER.md": ProjectAdapter(
                "fechai",
                "projects/fechai/PROJECT_ADAPTER.md",
                "github:fecha.ai",
                bootstrap,
                (
                    RoleMapping("architecture", "software-systems-architect", "ADOPTED", legacy_aliases=("GPT1.5",)),
                    RoleMapping("documentation_audit", "documentation-auditor", "ADOPTED"),
                ),
            ),
            "projects/other/PROJECT_ADAPTER.md": ProjectAdapter(
                "other",
                "projects/other/PROJECT_ADAPTER.md",
                "github:other",
                "docs/bootstrap/INDEX.md",
                (RoleMapping("architecture", "documentation-auditor", "ADOPTED"),),
            ),
        }
        archetypes = {
            "software-systems-architect": ArchetypeRecord(
                "software-systems-architect",
                "archetypes/software-systems-architect/ARCHETYPE.md",
                "ACTIVE" if active else "INACTIVE",
            ),
            "documentation-auditor": ArchetypeRecord(
                "documentation-auditor",
                "archetypes/documentation-auditor/ARCHETYPE.md",
                "ACTIVE",
            ),
        }
        certifications = {
            "software-systems-architect": CertificationRecord(
                "software-systems-architect", certification, "ssa-v0.1", fingerprint
            ),
            "documentation-auditor": CertificationRecord(
                "documentation-auditor", "YES", "doc-auditor-v1.1", "CURRENT"
            ),
        }
        return RuntimeEnforcementGateway("ses-test-ref", projects, adapters, archetypes, certifications)

    def req(self, project="fechai", role="architecture"):
        return RoutingRequest(project, role, "bounded task")

    def test_g01_routable(self):
        receipt = self.make_gateway().route(self.req())
        self.assertEqual(Decision.ROUTABLE, receipt.decision)
        self.assertEqual("software-systems-architect", receipt.archetype_id)
        self.assertFalse(receipt.mutation_authorized)

    def test_g02_unknown_project(self):
        self.assertEqual(Decision.PROJECT_NOT_REGISTERED, self.make_gateway().route(self.req("missing")).decision)

    def test_g03_unmapped_role(self):
        self.assertEqual(Decision.SPECIALIST_ROLE_NOT_ADOPTED, self.make_gateway().route(self.req(role="architect")).decision)

    def test_g04_unknown_archetype(self):
        gateway = self.make_gateway()
        adapter = gateway.adapters["projects/fechai/PROJECT_ADAPTER.md"]
        gateway.adapters = dict(gateway.adapters)
        gateway.adapters[adapter.adapter_path] = ProjectAdapter(
            adapter.project_id, adapter.adapter_path, adapter.canonical_source, adapter.bootstrap_entrypoint,
            (RoleMapping("architecture", "missing-archetype", "ADOPTED"),)
        )
        self.assertEqual(Decision.ARCHETYPE_NOT_RESOLVED, gateway.route(self.req()).decision)

    def test_g05_inactive_archetype(self):
        self.assertEqual(Decision.ARCHETYPE_NOT_ACTIVE, self.make_gateway(active=False).route(self.req()).decision)

    def test_g06_not_certified(self):
        self.assertEqual(Decision.SPECIALIST_NOT_CERTIFIED, self.make_gateway(certification="NO").route(self.req()).decision)

    def test_g07_stale_fingerprint(self):
        self.assertEqual(
            Decision.RUNTIME_FINGERPRINT_STALE_OR_UNSUPPORTED,
            self.make_gateway(fingerprint="STALE").route(self.req()).decision,
        )

    def test_g08_cross_project_isolation(self):
        gateway = self.make_gateway()
        a = gateway.route(self.req("fechai", "architecture"))
        b = gateway.route(self.req("other", "architecture"))
        self.assertEqual("software-systems-architect", a.archetype_id)
        self.assertEqual("documentation-auditor", b.archetype_id)

    def test_g09_no_fuzzy_role(self):
        self.assertEqual(
            Decision.SPECIALIST_ROLE_NOT_ADOPTED,
            self.make_gateway().route(self.req(role="Architecture")).decision,
        )

    def test_g10_legacy_alias_does_not_override_role(self):
        receipt = self.make_gateway().route(self.req(role="architecture"))
        self.assertEqual("software-systems-architect", receipt.archetype_id)
        self.assertEqual(Decision.ROUTABLE, receipt.decision)

    def test_g11_routable_is_not_mutation_authority(self):
        receipt = self.make_gateway().route(self.req())
        self.assertEqual(Decision.ROUTABLE, receipt.decision)
        self.assertFalse(receipt.mutation_authorized)

    def test_g12_bootstrap_unresolved(self):
        receipt = self.make_gateway(bootstrap="NOT_RESOLVED").route(self.req())
        self.assertEqual(Decision.PROJECT_BOOTSTRAP_UNRESOLVED, receipt.decision)


if __name__ == "__main__":
    unittest.main()
