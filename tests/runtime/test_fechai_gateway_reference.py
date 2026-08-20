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


class FechaiGatewayReferenceTests(unittest.TestCase):
    def setUp(self):
        project = ProjectRecord(
            "fechai",
            "FECH.AI",
            ("FECHAI", "fecha.ai", "FECH.AI — Projeto Principal / Master Project"),
            "projects/fechai/PROJECT_ADAPTER.md",
        )
        adapter = ProjectAdapter(
            "fechai",
            "projects/fechai/PROJECT_ADAPTER.md",
            "GitHub repository wagnerjfjunior/fecha.ai",
            "docs/bootstrap/INDEX.md",
            (
                RoleMapping("documentation_audit", "documentation-auditor", "ADOPTED", "docs/skills/fechai-gpt0-documentation-auditor.md"),
                RoleMapping("architecture", "software-systems-architect", "ADOPTED", "docs/skills/fechai-gpt1-architect-saas.md", ("GPT1", "GPT1.5")),
                RoleMapping("ux_ui", "ux-ui-app-specialist", "ADOPTED", "docs/skills/fechai-gpt2-ux-ui-app-specialist.md"),
                RoleMapping("backend_data", "backend-data-platform-specialist", "ADOPTED", "docs/skills/fechai-gpt3-supabase-security-specialist.md"),
                RoleMapping("application_security", "application-security-assurance-specialist", "ADOPTED"),
            ),
        )
        ids = (
            "documentation-auditor",
            "software-systems-architect",
            "ux-ui-app-specialist",
            "backend-data-platform-specialist",
            "application-security-assurance-specialist",
        )
        archetypes = {
            item: ArchetypeRecord(item, f"archetypes/{item}/ARCHETYPE.md", "ACTIVE") for item in ids
        }
        certifications = {
            item: CertificationRecord(item, "YES", f"{item}:CURRENT_CERTIFIED_SUBJECT", "CURRENT") for item in ids
        }
        self.gateway = RuntimeEnforcementGateway(
            "ses-reference-test-ref",
            (project,),
            {adapter.adapter_path: adapter},
            archetypes,
            certifications,
        )

    def route(self, role):
        return self.gateway.route(RoutingRequest("fechai", role, "reference routing test"))

    def test_f01_documentation(self):
        self.assertEqual("documentation-auditor", self.route("documentation_audit").archetype_id)

    def test_f02_architecture(self):
        self.assertEqual("software-systems-architect", self.route("architecture").archetype_id)

    def test_f03_ux_ui(self):
        self.assertEqual("ux-ui-app-specialist", self.route("ux_ui").archetype_id)

    def test_f04_backend_data(self):
        self.assertEqual("backend-data-platform-specialist", self.route("backend_data").archetype_id)

    def test_f05_application_security(self):
        self.assertEqual("application-security-assurance-specialist", self.route("application_security").archetype_id)

    def test_f06_all_current_roles_are_routable_without_mutation_authority(self):
        for role in ("documentation_audit", "architecture", "ux_ui", "backend_data", "application_security"):
            receipt = self.route(role)
            self.assertEqual(Decision.ROUTABLE, receipt.decision)
            self.assertFalse(receipt.mutation_authorized)

    def test_f07_unmapped_or_legacy_label_is_not_guessed(self):
        self.assertEqual(Decision.SPECIALIST_ROLE_NOT_ADOPTED, self.route("platform_delivery").decision)
        self.assertEqual(Decision.SPECIALIST_ROLE_NOT_ADOPTED, self.route("GPT1.5").decision)


if __name__ == "__main__":
    unittest.main()
