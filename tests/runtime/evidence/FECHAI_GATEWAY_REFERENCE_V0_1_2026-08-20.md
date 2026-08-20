# SES — FECH.AI Runtime Gateway Reference Evidence — 2026-08-20

**Project:** `fechai`
**Adapter:** `projects/fechai/PROJECT_ADAPTER.md`
**Runtime:** `runtime/specialist_gateway/controller.py`
**Test:** `tests/runtime/test_fechai_gateway_reference.py`

Observed reference-routing result after the role map was applied to the SES FECH.AI Adapter:

```text
F01 documentation_audit -> documentation-auditor = PASS
F02 architecture -> software-systems-architect = PASS
F03 ux_ui -> ux-ui-app-specialist = PASS
F04 backend_data -> backend-data-platform-specialist = PASS
F05 application_security -> application-security-assurance-specialist = PASS
F06 all five mapped roles ROUTABLE and mutation_authorized=False = PASS
F07 platform_delivery and GPT1.5 are not guessed as roles = PASS

TOTAL = 7/7 PASS
```

Boundaries:

```text
SES_ADAPTER_MAPPING = PROVEN
GATEWAY_REFERENCE_ROUTING = PASS
FECHAI_REPOSITORY_ROUTING_RECONCILIATION = NOT_YET_PROVEN IN THIS PR
PRODUCTION_EXECUTION = NOT_CLAIMED
AUTOMATIC_ADOPTION = NO
```

The FECH.AI repository must still explicitly reconcile its own legacy specialist routing so new project conversations resolve these SES roles instead of treating GPT labels as current routing authority.
