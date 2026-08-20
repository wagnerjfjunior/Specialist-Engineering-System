import unittest

from runtime.specialist_gateway.controller import (
    Decision,
    RoutingReceipt,
)
from runtime.specialist_gateway.github_loader import CanonicalLoadError, CanonicalSnapshot
from runtime.specialist_gateway.http_api import health_check, route_request


class FakeGateway:
    def __init__(self, decision=Decision.ROUTABLE):
        self.decision = decision

    def route(self, request):
        return RoutingReceipt(
            ses_ref="abc123",
            project_identifier_supplied=request.project_identifier,
            project_id="fechai",
            project_adapter_path="projects/fechai/PROJECT_ADAPTER.md",
            role=request.role,
            adoption_status="ADOPTED",
            archetype_id="documentation-auditor",
            archetype_contract_path="archetypes/documentation-auditor/ARCHETYPE.md",
            archetype_resolution_status="ACTIVE",
            certification_status="YES",
            certified_subject="CURRENT_KERNEL_BLOB=example",
            project_bootstrap_entrypoint="docs/bootstrap/INDEX.md",
            decision=self.decision,
            blocker="NONE" if self.decision == Decision.ROUTABLE else self.decision.value,
            mutation_authorized=False,
        )


def snapshot(decision=Decision.ROUTABLE):
    return CanonicalSnapshot("abc123", FakeGateway(decision))


class HttpGatewayTests(unittest.TestCase):
    def test_h01_health_ready_without_exposing_ref(self):
        result = health_check(api_key="secret", snapshot_loader=lambda: snapshot())
        self.assertEqual(200, result.status_code)
        self.assertEqual("ok", result.body["status"])
        self.assertNotIn("ses_ref", result.body)

    def test_h02_health_requires_runtime_auth_configuration(self):
        result = health_check(api_key="", snapshot_loader=lambda: snapshot())
        self.assertEqual(503, result.status_code)
        self.assertEqual("GATEWAY_AUTH_NOT_CONFIGURED", result.body["error"])

    def test_h03_route_requires_api_key(self):
        result = route_request(
            {"project_identifier": "fechai", "role": "documentation_audit", "task_scope": "audit"},
            None,
            api_key="secret",
            snapshot_loader=lambda: snapshot(),
        )
        self.assertEqual(401, result.status_code)
        self.assertEqual("UNAUTHORIZED", result.body["error"])

    def test_h04_route_serializes_receipt(self):
        result = route_request(
            {"project_identifier": "fechai", "role": "documentation_audit", "task_scope": "audit"},
            "secret",
            api_key="secret",
            snapshot_loader=lambda: snapshot(),
        )
        self.assertEqual(200, result.status_code)
        receipt = result.body["receipt"]
        self.assertEqual("ROUTABLE", receipt["decision"])
        self.assertEqual("abc123", receipt["ses_ref"])
        self.assertFalse(receipt["mutation_authorized"])

    def test_h05_invalid_or_extra_payload_is_rejected(self):
        result = route_request(
            {
                "project_identifier": "fechai",
                "role": "documentation_audit",
                "task_scope": "audit",
                "extra": "not allowed",
            },
            "secret",
            api_key="secret",
            snapshot_loader=lambda: snapshot(),
        )
        self.assertEqual(400, result.status_code)
        self.assertEqual("INVALID_REQUEST", result.body["error"])

    def test_h06_canonical_loader_failure_is_generic_503(self):
        def fail():
            raise CanonicalLoadError("private internal dependency detail")

        result = route_request(
            {"project_identifier": "fechai", "role": "documentation_audit", "task_scope": "audit"},
            "secret",
            api_key="secret",
            snapshot_loader=fail,
        )
        self.assertEqual(503, result.status_code)
        self.assertEqual("CANONICAL_SOURCE_UNAVAILABLE", result.body["error"])
        self.assertNotIn("private", str(result.body))

    def test_h07_domain_block_is_http_success_with_bounded_decision(self):
        result = route_request(
            {"project_identifier": "fechai", "role": "documentation_audit", "task_scope": "audit"},
            "secret",
            api_key="secret",
            snapshot_loader=lambda: snapshot(Decision.SPECIALIST_NOT_CERTIFIED),
        )
        self.assertEqual(200, result.status_code)
        self.assertEqual("SPECIALIST_NOT_CERTIFIED", result.body["receipt"]["decision"])
        self.assertFalse(result.body["receipt"]["mutation_authorized"])

    def test_h08_secret_is_never_echoed(self):
        secret = "do-not-echo-this"
        result = route_request(
            {"project_identifier": "fechai", "role": "documentation_audit", "task_scope": "audit"},
            "wrong",
            api_key=secret,
            snapshot_loader=lambda: snapshot(),
        )
        self.assertNotIn(secret, str(result.body))


if __name__ == "__main__":
    unittest.main()
