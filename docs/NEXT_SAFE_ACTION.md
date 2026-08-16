# SES — Next Safe Action

> Este é o registro autoritativo da única próxima ação segura do SES quando este estado estiver em `main`.

**Next action ID:** `apply-ux-ui-app-specialist-l2-runtime-profile`  
**Primary target:** `SES — UX/UI APP Specialist Candidate v0.1`  
**Current phase:** `SPECIALIST_PORTFOLIO_EXPANSION / UX_UI_CANONICAL_L1_PASS / L2_RUNTIME_PROFILE_READY`  
**Canonical source:** `wagnerjfjunior/Specialist-Engineering-System` / `main` resolved live

## 1. Material state reached

Preserve both behavioral evidence events:

```text
L0 HARNESS SANITY = PASS
HISTORICAL L1-P / PACKETED = PASS_WITH_FIDELITY_AND_PROVENANCE_LIMITATIONS
CANONICAL L1-C = PASS
P01–P20 = PASS
CANDIDATE_BEHAVIORAL_VALIDATION_L1 = PASS
FULL_L1_BEHAVIORAL_SUITE = PASS
STOP_LOSS_TRIGGERED = NO
INITIAL_OVERCLAIM = NONE OBSERVED
RETROACTIVE_PASS = NONE
```

L1-C evidence is recorded in `tests/behavioral/UX_UI_APP_SPECIALIST_L1C_VALIDATION_V0_1.md`.

## 2. L2 preparation state

Versioned L2 artifacts:
- `tests/runtime/UX_UI_APP_SPECIALIST_L2_RUNTIME_PROFILE_V0_1.md`
- `tests/runtime/UX_UI_APP_SPECIALIST_L2_RUNBOOK_V0_1.md`

```text
L2 PROFILE/RUNBOOK = PREPARED
BUILDER APPLIED = NO
L2 EXECUTED = NO
L2 RUNTIME PASS = NOT ESTABLISHED
```

## 3. Sole next material action

Apply the approved L2 runtime profile to the actual external Builder/runtime and capture the exact effective fingerprint before testing.

This action requires explicit applicable authorization because it mutates external Builder/runtime configuration.

Before any L2 execution, capture when exposed:

```text
RUNTIME_ID
BUILDER/GPT_ID_OR_URL
RUNTIME_NAME
PROFILE_VERSION
PROFILE_BLOB_SHA
INSTRUCTION_BLOB_SHA_OR_EXACT_EXPORT
KNOWLEDGE_FILE_LIST/HASHES
ACTIONS/TOOLS_ENABLED
ACTION/TOOL_CONFIG_VERSION
MODEL
MODEL_MODE/SETTINGS
CAPABILITIES
CONVERSATION_START_MODE
DATE/TIME
EXECUTION_ID
```

Unknown/unexposed values must be recorded as `NOT EXPOSED`, not invented.

## 4. L2 execution sequence

After Builder application and fingerprint freeze:

```text
APPLY VERSIONED PROFILE
→ CAPTURE EXACT BUILDER FINGERPRINT
→ FREEZE EFFECTIVE CONFIGURATION
→ EXECUTE R01–R06 IN FRESH BUILDER CONVERSATIONS
→ ADJUDICATE L2-01..L2-12
→ RECORD PROVENANCE
```

The runbook includes a runtime-specific tool challenge. Tool availability alone is not evidence of execution.

## 5. Done condition

Only a successful runtime execution under the exact fingerprint may establish:

```text
L2_RUNTIME_FINGERPRINT_VALIDATION = PASS
```

L2 PASS still does not automatically establish registry activation, consumer adoption, production certification for every project or risk acceptance.

## 6. Explicitly blocked

Do not:
- treat L1-C PASS as L2/runtime PASS;
- claim Builder applied before actual external configuration;
- claim tool execution without invocation/result evidence;
- activate UX/UI APP Specialist in `archetypes/REGISTRY.md` from L1 alone;
- publish/configure an external Builder without explicit applicable authorization;
- adopt the specialist into a consumer project automatically;
- retire project-local specialists;
- alter historical packeted outcomes/provenance;
- implement the deferred Documentation Auditor Gateway;
- execute the SaaS Architect rename from direction alone.

## 7. Portfolio direction

```text
UX/UI APP Specialist — canonical L1 PASS; L2 runtime application/validation next
→ Application Security Assurance
→ Backend & Data Platform
→ Platform + Delivery + Reliability
→ SEO & Organic Growth
→ challenge Growth + Analytics + Monetization
→ Integration + Automation if still justified
→ only then evaluate project adoption/legacy retirement
```

```text
CENTRAL SES EVOLUTION != AUTOMATIC PROJECT MUTATION
TARGET CONSOLIDATION != AUTHORIZED RETIREMENT
```
