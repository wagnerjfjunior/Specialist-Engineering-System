from __future__ import annotations

import hmac
import os
from dataclasses import asdict, dataclass
from typing import Callable, Mapping, Optional

from .controller import RoutingRequest
from .github_loader import CanonicalLoadError, CanonicalSnapshot, load_canonical_snapshot

GATEWAY_NAME = "ses-runtime-enforcement-gateway"
GATEWAY_VERSION = "0.1"
API_KEY_ENV = "SES_GATEWAY_API_KEY"
MAX_PROJECT_IDENTIFIER = 256
MAX_ROLE = 128
MAX_TASK_SCOPE = 4096

SnapshotLoader = Callable[[], CanonicalSnapshot]


@dataclass(frozen=True)
class ApiResult:
    status_code: int
    body: Mapping[str, object]


def _configured_api_key(explicit_api_key: Optional[str] = None) -> Optional[str]:
    value = explicit_api_key if explicit_api_key is not None else os.getenv(API_KEY_ENV)
    if value is None or not value.strip():
        return None
    return value


def _authorized(provided: Optional[str], expected: str) -> bool:
    if provided is None:
        return False
    return hmac.compare_digest(provided, expected)


def _error(status_code: int, code: str) -> ApiResult:
    return ApiResult(status_code, {"status": "error", "error": code})


def health_check(
    *,
    api_key: Optional[str] = None,
    snapshot_loader: SnapshotLoader = load_canonical_snapshot,
) -> ApiResult:
    if _configured_api_key(api_key) is None:
        return _error(503, "GATEWAY_AUTH_NOT_CONFIGURED")

    try:
        snapshot_loader()
    except CanonicalLoadError:
        return _error(503, "CANONICAL_SOURCE_UNAVAILABLE")
    except Exception:
        return _error(500, "INTERNAL_ERROR")

    return ApiResult(
        200,
        {
            "status": "ok",
            "gateway": GATEWAY_NAME,
            "version": GATEWAY_VERSION,
        },
    )


def _validated_request(payload: object) -> Optional[RoutingRequest]:
    if not isinstance(payload, Mapping):
        return None

    required = {"project_identifier", "role", "task_scope"}
    if set(payload.keys()) != required:
        return None

    project_identifier = payload.get("project_identifier")
    role = payload.get("role")
    task_scope = payload.get("task_scope")
    if not all(isinstance(value, str) for value in (project_identifier, role, task_scope)):
        return None

    assert isinstance(project_identifier, str)
    assert isinstance(role, str)
    assert isinstance(task_scope, str)
    if not project_identifier.strip() or not role.strip() or not task_scope.strip():
        return None
    if len(project_identifier) > MAX_PROJECT_IDENTIFIER or len(role) > MAX_ROLE or len(task_scope) > MAX_TASK_SCOPE:
        return None

    return RoutingRequest(project_identifier, role, task_scope)


def route_request(
    payload: object,
    provided_api_key: Optional[str],
    *,
    api_key: Optional[str] = None,
    snapshot_loader: SnapshotLoader = load_canonical_snapshot,
) -> ApiResult:
    expected_api_key = _configured_api_key(api_key)
    if expected_api_key is None:
        return _error(503, "GATEWAY_AUTH_NOT_CONFIGURED")
    if not _authorized(provided_api_key, expected_api_key):
        return _error(401, "UNAUTHORIZED")

    request = _validated_request(payload)
    if request is None:
        return _error(400, "INVALID_REQUEST")

    try:
        snapshot = snapshot_loader()
        receipt = snapshot.gateway.route(request)
    except CanonicalLoadError:
        return _error(503, "CANONICAL_SOURCE_UNAVAILABLE")
    except Exception:
        return _error(500, "INTERNAL_ERROR")

    serialized = asdict(receipt)
    serialized["decision"] = receipt.decision.value
    return ApiResult(200, {"status": "ok", "receipt": serialized})
