from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping, Optional, Sequence, Tuple


class Decision(str, Enum):
    ROUTABLE = "ROUTABLE"
    PROJECT_NOT_REGISTERED = "PROJECT_NOT_REGISTERED"
    PROJECT_ID_AMBIGUOUS = "PROJECT_ID_AMBIGUOUS"
    PROJECT_ADAPTER_UNRESOLVED = "PROJECT_ADAPTER_UNRESOLVED"
    SPECIALIST_ROLE_NOT_ADOPTED = "SPECIALIST_ROLE_NOT_ADOPTED"
    ARCHETYPE_NOT_RESOLVED = "ARCHETYPE_NOT_RESOLVED"
    ARCHETYPE_NOT_ACTIVE = "ARCHETYPE_NOT_ACTIVE"
    SPECIALIST_NOT_CERTIFIED = "SPECIALIST_NOT_CERTIFIED"
    PROJECT_BOOTSTRAP_UNRESOLVED = "PROJECT_BOOTSTRAP_UNRESOLVED"
    RUNTIME_FINGERPRINT_STALE_OR_UNSUPPORTED = "RUNTIME_FINGERPRINT_STALE_OR_UNSUPPORTED"
    BLOCKED = "BLOCKED"


@dataclass(frozen=True)
class ProjectRecord:
    project_id: str
    canonical_name: str
    aliases: Tuple[str, ...]
    adapter_path: str
    status: str = "ACTIVE"

    def identifiers(self) -> Tuple[str, ...]:
        return (self.project_id, self.canonical_name, *self.aliases)


@dataclass(frozen=True)
class RoleMapping:
    role: str
    archetype_id: str
    adoption_status: str
    project_local_rules: str = "NOT_APPLICABLE"
    legacy_aliases: Tuple[str, ...] = ()


@dataclass(frozen=True)
class ProjectAdapter:
    project_id: str
    adapter_path: str
    canonical_source: str
    bootstrap_entrypoint: str
    role_map: Tuple[RoleMapping, ...] = ()
    resolved: bool = True


@dataclass(frozen=True)
class ArchetypeRecord:
    archetype_id: str
    contract_path: str
    resolution_status: str


@dataclass(frozen=True)
class CertificationRecord:
    archetype_id: str
    certification: str
    certified_subject: str = "NOT_CAPTURED"
    fingerprint_status: str = "CURRENT"


@dataclass(frozen=True)
class RoutingRequest:
    project_identifier: str
    role: str
    task_scope: str


@dataclass(frozen=True)
class RoutingReceipt:
    ses_ref: str
    project_identifier_supplied: str
    project_id: str = "NOT_RESOLVED"
    project_adapter_path: str = "NOT_RESOLVED"
    role: str = ""
    adoption_status: str = "NOT_RESOLVED"
    archetype_id: str = "NOT_RESOLVED"
    archetype_contract_path: str = "NOT_RESOLVED"
    archetype_resolution_status: str = "NOT_RESOLVED"
    certification_status: str = "NOT_RESOLVED"
    certified_subject: str = "NOT_RESOLVED"
    project_bootstrap_entrypoint: str = "NOT_RESOLVED"
    decision: Decision = Decision.BLOCKED
    blocker: str = "UNSPECIFIED"
    mutation_authorized: bool = False


@dataclass
class RuntimeEnforcementGateway:
    ses_ref: str
    projects: Sequence[ProjectRecord]
    adapters: Mapping[str, ProjectAdapter]
    archetypes: Mapping[str, ArchetypeRecord]
    certifications: Mapping[str, CertificationRecord]

    def _receipt(self, request: RoutingRequest, **kwargs) -> RoutingReceipt:
        base = dict(
            ses_ref=self.ses_ref,
            project_identifier_supplied=request.project_identifier,
            role=request.role,
            mutation_authorized=False,
        )
        base.update(kwargs)
        return RoutingReceipt(**base)

    def _resolve_project(self, supplied: str) -> Tuple[Optional[ProjectRecord], Optional[Decision]]:
        key = supplied.strip().casefold()
        matches = []
        for project in self.projects:
            if project.status != "ACTIVE":
                continue
            if any(key == identifier.strip().casefold() for identifier in project.identifiers()):
                matches.append(project)
        if not matches:
            return None, Decision.PROJECT_NOT_REGISTERED
        if len(matches) != 1:
            return None, Decision.PROJECT_ID_AMBIGUOUS
        return matches[0], None

    @staticmethod
    def _resolve_role(adapter: ProjectAdapter, role: str) -> Optional[RoleMapping]:
        exact = [mapping for mapping in adapter.role_map if mapping.role == role]
        if len(exact) != 1:
            return None
        mapping = exact[0]
        if mapping.adoption_status != "ADOPTED":
            return None
        return mapping

    def route(self, request: RoutingRequest) -> RoutingReceipt:
        if not request.project_identifier.strip() or not request.role or not request.task_scope.strip():
            return self._receipt(request, decision=Decision.BLOCKED, blocker="REQUIRED_INPUT_MISSING")

        project, project_error = self._resolve_project(request.project_identifier)
        if project_error is not None:
            return self._receipt(request, decision=project_error, blocker=project_error.value)
        assert project is not None

        adapter = self.adapters.get(project.adapter_path)
        project_fields = dict(project_id=project.project_id, project_adapter_path=project.adapter_path)
        if adapter is None or not adapter.resolved or adapter.project_id != project.project_id:
            return self._receipt(
                request,
                **project_fields,
                decision=Decision.PROJECT_ADAPTER_UNRESOLVED,
                blocker="PROJECT_ADAPTER_UNRESOLVED",
            )

        role_mapping = self._resolve_role(adapter, request.role)
        adapter_fields = dict(
            **project_fields,
            project_bootstrap_entrypoint=adapter.bootstrap_entrypoint or "NOT_RESOLVED",
        )
        if role_mapping is None:
            return self._receipt(
                request,
                **adapter_fields,
                decision=Decision.SPECIALIST_ROLE_NOT_ADOPTED,
                blocker="SPECIALIST_ROLE_NOT_ADOPTED",
            )

        adoption_fields = dict(
            **adapter_fields,
            adoption_status=role_mapping.adoption_status,
            archetype_id=role_mapping.archetype_id,
        )
        archetype = self.archetypes.get(role_mapping.archetype_id)
        if archetype is None:
            return self._receipt(
                request,
                **adoption_fields,
                decision=Decision.ARCHETYPE_NOT_RESOLVED,
                blocker="ARCHETYPE_NOT_RESOLVED",
            )

        archetype_fields = dict(
            **adoption_fields,
            archetype_contract_path=archetype.contract_path,
            archetype_resolution_status=archetype.resolution_status,
        )
        if archetype.resolution_status != "ACTIVE":
            return self._receipt(
                request,
                **archetype_fields,
                decision=Decision.ARCHETYPE_NOT_ACTIVE,
                blocker="ARCHETYPE_NOT_ACTIVE",
            )

        certification = self.certifications.get(archetype.archetype_id)
        if certification is None or certification.certification != "YES":
            return self._receipt(
                request,
                **archetype_fields,
                certification_status=certification.certification if certification else "NOT_RESOLVED",
                certified_subject=certification.certified_subject if certification else "NOT_RESOLVED",
                decision=Decision.SPECIALIST_NOT_CERTIFIED,
                blocker="SPECIALIST_NOT_CERTIFIED",
            )

        certification_fields = dict(
            **archetype_fields,
            certification_status=certification.certification,
            certified_subject=certification.certified_subject,
        )
        if certification.fingerprint_status != "CURRENT":
            return self._receipt(
                request,
                **certification_fields,
                decision=Decision.RUNTIME_FINGERPRINT_STALE_OR_UNSUPPORTED,
                blocker="RUNTIME_FINGERPRINT_STALE_OR_UNSUPPORTED",
            )

        if not adapter.bootstrap_entrypoint or adapter.bootstrap_entrypoint == "NOT_RESOLVED":
            return self._receipt(
                request,
                **certification_fields,
                project_bootstrap_entrypoint="NOT_RESOLVED",
                decision=Decision.PROJECT_BOOTSTRAP_UNRESOLVED,
                blocker="PROJECT_BOOTSTRAP_UNRESOLVED",
            )

        return self._receipt(
            request,
            **certification_fields,
            decision=Decision.ROUTABLE,
            blocker="NONE",
        )
