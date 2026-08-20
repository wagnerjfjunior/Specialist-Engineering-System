from __future__ import annotations

import base64
import json
import os
import re
from dataclasses import dataclass
from typing import Dict, Iterable, Mapping, Optional, Tuple
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from .controller import (
    ArchetypeRecord,
    CertificationRecord,
    ProjectAdapter,
    ProjectRecord,
    RoleMapping,
    RuntimeEnforcementGateway,
)

DEFAULT_REPOSITORY = "wagnerjfjunior/Specialist-Engineering-System"
DEFAULT_BRANCH = "main"


class CanonicalLoadError(RuntimeError):
    pass


@dataclass(frozen=True)
class CanonicalSnapshot:
    ses_ref: str
    gateway: RuntimeEnforcementGateway


class GitHubContentsClient:
    """Minimal read-only GitHub client used by the operational Gateway."""

    def __init__(self, token: Optional[str] = None, repository: str = DEFAULT_REPOSITORY, timeout: float = 10.0):
        self.token = token or os.getenv("SES_GITHUB_TOKEN") or os.getenv("GITHUB_TOKEN")
        self.repository = repository
        self.timeout = timeout

    def _request_json(self, path: str) -> Mapping[str, object]:
        url = f"https://api.github.com/repos/{self.repository}/{path.lstrip('/')}"
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "ses-runtime-enforcement-gateway/0.1",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        request = Request(url, headers=headers)
        try:
            with urlopen(request, timeout=self.timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as exc:
            raise CanonicalLoadError(f"GitHub read failed for {path}: {exc}") from exc

    def resolve_ref(self, branch: str = DEFAULT_BRANCH) -> str:
        payload = self._request_json(f"branches/{branch}")
        try:
            return str(payload["commit"]["sha"])  # type: ignore[index]
        except (KeyError, TypeError) as exc:
            raise CanonicalLoadError("GitHub branch response did not contain commit.sha") from exc

    def read_text(self, path: str, ref: str) -> str:
        payload = self._request_json(f"contents/{path}?ref={ref}")
        try:
            if payload.get("encoding") != "base64":
                raise CanonicalLoadError(f"Unsupported GitHub content encoding for {path}")
            encoded = str(payload["content"])
            return base64.b64decode(encoded).decode("utf-8")
        except (KeyError, ValueError, UnicodeDecodeError) as exc:
            raise CanonicalLoadError(f"Unable to decode GitHub content for {path}") from exc


def _fenced_blocks(text: str) -> Iterable[str]:
    return re.findall(r"```(?:text)?\s*\n(.*?)```", text, flags=re.DOTALL | re.IGNORECASE)


def _parse_scalar_block(block: str) -> Dict[str, str]:
    result: Dict[str, str] = {}
    for line in block.splitlines():
        match = re.match(r"^([A-Z][A-Z0-9_]*):\s*(.+?)\s*$", line)
        if match:
            result[match.group(1)] = match.group(2)
    return result


def _parse_list_after(block: str, key: str) -> Tuple[str, ...]:
    lines = block.splitlines()
    values = []
    active = False
    for line in lines:
        if line.strip() == f"{key}:":
            active = True
            continue
        if active:
            if re.match(r"^[A-Z][A-Z0-9_]*:", line.strip()):
                break
            item = re.match(r"^\s*-\s*(.+?)\s*$", line)
            if item:
                values.append(item.group(1))
    return tuple(values)


def parse_project_registry(text: str) -> Tuple[ProjectRecord, ...]:
    records = []
    for block in _fenced_blocks(text):
        fields = _parse_scalar_block(block)
        if not {"PROJECT_ID", "CANONICAL_NAME", "ADAPTER_PATH", "STATUS"}.issubset(fields):
            continue
        records.append(
            ProjectRecord(
                fields["PROJECT_ID"],
                fields["CANONICAL_NAME"],
                _parse_list_after(block, "ALIASES"),
                fields["ADAPTER_PATH"],
                fields["STATUS"],
            )
        )
    if not records:
        raise CanonicalLoadError("Project Registry contained no parseable project records")
    return tuple(records)


def parse_archetype_registry(text: str) -> Dict[str, ArchetypeRecord]:
    records: Dict[str, ArchetypeRecord] = {}
    for block in _fenced_blocks(text):
        fields = _parse_scalar_block(block)
        if not {"ARCHETYPE_ID", "CONTRACT_PATH", "RESOLUTION_STATUS"}.issubset(fields):
            continue
        archetype_id = fields["ARCHETYPE_ID"]
        records[archetype_id] = ArchetypeRecord(archetype_id, fields["CONTRACT_PATH"], fields["RESOLUTION_STATUS"])
    if not records:
        raise CanonicalLoadError("Archetype Registry contained no parseable archetype records")
    return records


def parse_certification_ledger(text: str) -> Dict[str, CertificationRecord]:
    records: Dict[str, CertificationRecord] = {}
    row_pattern = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*`(YES|NO)`\s*\|", re.MULTILINE)
    for archetype_id, certification in row_pattern.findall(text):
        records[archetype_id] = CertificationRecord(
            archetype_id=archetype_id,
            certification=certification,
            certified_subject=_certified_subject(text, archetype_id),
            fingerprint_status="CURRENT" if certification == "YES" else "UNSUPPORTED",
        )
    if not records:
        raise CanonicalLoadError("Certification ledger contained no parseable certification rows")
    return records


def _certified_subject(text: str, archetype_id: str) -> str:
    section_match = re.search(
        rf"ARCHETYPE_ID\s*=\s*{re.escape(archetype_id)}(?P<body>.*?)(?:\n##\s|\Z)",
        text,
        flags=re.DOTALL,
    )
    if not section_match:
        return f"{archetype_id}:LEDGER_CURRENT"
    body = section_match.group("body")
    for key in ("CURRENT_KERNEL_BLOB", "CURRENT_CANDIDATE", "CURRENT_RUNTIME_FINGERPRINT"):
        match = re.search(rf"^{key}\s*=\s*(.+?)\s*$", body, flags=re.MULTILINE)
        if match:
            return f"{key}={match.group(1)}"
    return f"{archetype_id}:LEDGER_CURRENT"


def parse_project_adapter(text: str, adapter_path: str) -> ProjectAdapter:
    base_fields: Dict[str, str] = {}
    for block in _fenced_blocks(text):
        fields = _parse_scalar_block(block)
        if "PROJECT_ID" in fields and "BOOTSTRAP_ENTRYPOINT" in fields:
            base_fields = fields
            break
    if not base_fields:
        raise CanonicalLoadError(f"Adapter {adapter_path} did not contain required locator fields")

    role_map = []
    role_section = re.search(r"SPECIALIST_ROLE_MAP:\s*(.*?)(?:```|\Z)", text, flags=re.DOTALL)
    if role_section:
        chunks = re.split(r"(?=^- ROLE:\s*)", role_section.group(1), flags=re.MULTILINE)
        for chunk in chunks:
            role_match = re.search(r"^- ROLE:\s*(.+?)\s*$", chunk, flags=re.MULTILINE)
            archetype_match = re.search(r"^\s*ARCHETYPE_ID:\s*(.+?)\s*$", chunk, flags=re.MULTILINE)
            adoption_match = re.search(r"^\s*ADOPTION_STATUS:\s*(.+?)\s*$", chunk, flags=re.MULTILINE)
            if not (role_match and archetype_match and adoption_match):
                continue
            local_match = re.search(r"^\s*PROJECT_LOCAL_RULES:\s*(.+?)\s*$", chunk, flags=re.MULTILINE)
            aliases_match = re.search(r"^\s*LEGACY_ALIASES:\s*(.+?)\s*$", chunk, flags=re.MULTILINE)
            aliases = ()
            if aliases_match and aliases_match.group(1).strip().lower() != "none":
                aliases = tuple(part.strip() for part in aliases_match.group(1).split("/") if part.strip())
            role_map.append(
                RoleMapping(
                    role=role_match.group(1).strip(),
                    archetype_id=archetype_match.group(1).strip(),
                    adoption_status=adoption_match.group(1).strip(),
                    project_local_rules=local_match.group(1).strip() if local_match else "NOT_APPLICABLE",
                    legacy_aliases=aliases,
                )
            )

    return ProjectAdapter(
        project_id=base_fields["PROJECT_ID"],
        adapter_path=adapter_path,
        canonical_source=base_fields.get("CANONICAL_SOURCE", "NOT_RESOLVED"),
        bootstrap_entrypoint=base_fields.get("BOOTSTRAP_ENTRYPOINT", "NOT_RESOLVED"),
        role_map=tuple(role_map),
        resolved=True,
    )


def load_canonical_snapshot(client: Optional[GitHubContentsClient] = None, branch: str = DEFAULT_BRANCH) -> CanonicalSnapshot:
    client = client or GitHubContentsClient()
    ses_ref = client.resolve_ref(branch)
    projects_text = client.read_text("projects/REGISTRY.md", ses_ref)
    archetypes_text = client.read_text("archetypes/REGISTRY.md", ses_ref)
    certifications_text = client.read_text("docs/SPECIALIST_CERTIFICATION_STATUS.md", ses_ref)

    projects = parse_project_registry(projects_text)
    archetypes = parse_archetype_registry(archetypes_text)
    certifications = parse_certification_ledger(certifications_text)

    adapters: Dict[str, ProjectAdapter] = {}
    for project in projects:
        adapter_text = client.read_text(project.adapter_path, ses_ref)
        adapters[project.adapter_path] = parse_project_adapter(adapter_text, project.adapter_path)

    gateway = RuntimeEnforcementGateway(
        ses_ref=ses_ref,
        projects=projects,
        adapters=adapters,
        archetypes=archetypes,
        certifications=certifications,
    )
    return CanonicalSnapshot(ses_ref=ses_ref, gateway=gateway)
