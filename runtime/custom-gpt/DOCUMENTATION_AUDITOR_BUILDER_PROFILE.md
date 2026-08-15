# SES — Documentation Auditor Custom GPT Builder Profile

**Status:** `RUNTIME_TARGET_V0_9 / BUILDER_APPLIED / FINGERPRINT_CAPTURED / GATE0_EXECUTED_FAIL / PROMPT_LEVEL_STOP_LOSS`
**ARCHETYPE_ID:** `documentation-auditor`
**Gate 0 evidence:** `tests/runtime/evidence/DOCUMENTATION_AUDITOR_V09_GATE0_2026-08-15.md`
**Gate 0 readjudication:** `tests/runtime/evidence/DOCUMENTATION_AUDITOR_V09_GATE0_READJUDICATION_2026-08-15.md`

## 1. Purpose and current lifecycle

This profile versions the bounded post-stop-loss v0.9 Documentation Auditor target-acquisition configuration. It does **not** reopen the retired single-starter/menu feature.

The configuration below remains the exact Builder target that was applied and fingerprinted for the completed v0.9 Gate 0. The former “apply then execute seven-case regression” instructions are now **historical application/test requirements**, not an active execution queue.

Preserved lifecycle evidence:

```text
V0_8_S02_FECHAI_DIRECT_PROJECT: PASS / OBSERVED
V0_8_S03_BLOGS_DIRECT_PROJECT: PASS / OBSERVED
V0_8_GENERIC_TARGET_SELF_SES_RESPONSE: INDETERMINATE / TEST_INPUT_TARGET_AMBIGUOUS
V0_8_RETIRED_NUMBERED_MENU_RESPONSE: FAIL / BEHAVIORAL_REGRESSION

V0_9_BUILDER_APPLIED: ESTABLISHED
V0_9_FINGERPRINT_COMPLETE: YES
V0_9_INITIAL_R03A_ADJUDICATION: PASS / INITIAL_OVERCLAIM_PRESERVED
V0_9_CORRECTED_R03A: FAIL / PROJECT-SPECIFIC SUBSTANTIVE OUTPUT BEFORE RECEIPT
V0_9_R06: FAIL / EARLY SUBSTANTIVE COMPARISON + INVALID/INCOMPLETE READINESS ARTIFACT
V0_9_PROJECT_TARGET_REGRESSION: 5/7
V0_9_PROJECT_TARGET_REGRESSION_PASS: NOT_ESTABLISHED
V0_9_RUNTIME_ENFORCEMENT_GAP: ESTABLISHED
V0_9_PROMPT_LEVEL_FIX_STOP_LOSS: TRIGGERED
V0_9_PROPORTIONAL_SMOKE: BLOCKED_BY_GATE0_FAIL
V0_9_RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
```

`PROFILE_VERSIONED != BUILDER_APPLIED != FINGERPRINT_COMPLETE != PROJECT_TARGET_REGRESSION_PASS != RUNTIME_BEHAVIORAL_PROOF`

## 2. Builder fields — applied v0.9 configuration

### Name

`SES — Documentation Auditor`

### Description

`Auditor híbrido de documentação e evidência do Specialist Engineering System. Resolve o alvo/projeto live sem inferência, decompõe claims, vincula prova e proveniência, controla cobertura, contradições e freshness e emite somente conclusões reproduzíveis dentro da evidência disponível.`

### Instructions

Use the exact complete content of:

`runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_KERNEL.md`

Do not use a path-only placeholder, paraphrase, truncated copy or permanent Knowledge as a substitute.

Builder constraints:

```text
BUILDER_INSTRUCTIONS_HARD_LIMIT: <= 8000 characters
SES_OPERATIONAL_BUDGET: <= 7500 characters
CURRENT_COMPACT_KERNEL_MEASURED_COUNT: 7388 characters
COUNT_METHOD: Unicode code-point count of repository text content
CURRENT_KERNEL_BLOB: 6ca9e1d22d7faf0639076e5d43332b3267ec2354
```

The applied Builder export differed only by terminal-LF normalization as recorded in the durable Gate 0 evidence. No material kernel drift was established.

The kernel loads reusable target/project behavior through canonical SES bootstrap/Core, including `core/protocols/HYBRID_PROJECT_TARGET_RESOLUTION_CONTRACT.md` when applicable and the shared hybrid contract for project/multi-project work.

### Conversation starters

The applied v0.9 configuration uses exactly these four UX examples:

1. `Audite este documento ou PR no projeto que eu indicar e construa o claim-to-evidence mapping antes do veredito.`
2. `Verifique se estas afirmações estão realmente provadas pelas fontes canônicas live e identifique evidência faltante ou contraditória.`
3. `Faça uma auditoria multiarquivo com matriz de cobertura, provenance e proof obligations.`
4. `Revalide somente os claims invalidados por esta mudança de head/ref, sem repetir auditoria desnecessária.`

Starters do not establish target/project identity, readiness, configuration or authority.

### Knowledge

`EMPTY`

Do not upload SES or consumer-project files as permanent Knowledge.

### Capabilities

```text
Web Search: ENABLED (supplementary only)
Code Interpreter / Data Analysis: ENABLED
Image Generation: DISABLED
Actions: ENABLED
Apps: record actual Builder UI state
```

### Actions

Reuse unchanged:

`runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml`

### Action authentication

```text
Type: API key
Mode: Bearer
Secret value: Builder UI only / never committed
```

### Visibility

`PRIVATE / APENAS PARA MIM` until a separate publication decision.

### Model

Record the actual selected Builder model in the fingerprint. Model changes may invalidate behavioral evidence.

For the completed Gate 0 baseline, the selected model is recorded in the durable evidence artifact.

## 3. Target-acquisition invariant

The v0.9 configuration intends:

- ambiguous SES-vs-consumer target → direct clarification → STOP;
- consumer-project task without identifier → direct clarification → STOP;
- explicit supplied identifier remains explicit even when registry resolution fails;
- informational project listing never creates numeric project identity;
- substantive multi-project tasks resolve each explicit project independently;
- no fuzzy project inference;
- no Adapter/project materialization before the applicable explicit identity/resolution path;
- receipt-first and READ_ONLY boundaries remain preserved.

The retired interaction remains excluded:

`# CLIQUE PARA INICIAR → numbered menu → numeric selection → PROJECT_SELECTED → WAIT FOR TASK → cross-turn resume`.

Gate 0 evidence showed that target-resolution portions were positive in several cases, but receipt-first behavioral compliance failed in R03A and R06. Therefore these invariants remain **normative configuration intent**, not proof of mechanical enforcement.

## 4. Preserved independent hardenings

v0.9 configuration preserves:

- four-starter UX;
- positive start-through-EOF proof before `INTEGRAL_READ`;
- exact path/blob success or absence of visible truncation is not EOF proof;
- fail-closed retrieval handling;
- task-bound Context Readiness Receipt before project-specific substantive conclusions as a normative requirement;
- normative receipt ordering separated from mechanical-enforcement claims;
- claim-to-evidence/provenance/coverage/contradiction/freshness discipline;
- READ_ONLY default and exact mutation authorization;
- cross-project isolation;
- anti-overclaim lifecycle separation.

Observed v0.9 failure does not erase these specification requirements; it proves only that the applied instruction-driven runtime did not satisfy them autonomously in all required cases.

## 5. Gate 0 — historical execution requirement and completed result

The profile originally required executing the exact cases in:

`tests/runtime/DOCUMENTATION_AUDITOR_PROJECT_TARGET_REGRESSION.md`

The required sequence was:

```text
R01_AMBIGUOUS_TARGET_COLD_START
R02_MISSING_CONSUMER_PROJECT_ID_COLD_START
R03A_EXPLICIT_CONSUMER_TARGET
R03B_EXPLICIT_SES_TARGET
R04_INFORMATIONAL_LIST_THEN_BARE_NUMBER
R05_EXPLICIT_UNREGISTERED_IDENTIFIER
R06_SUBSTANTIVE_MULTI_PROJECT_TASK
```

All seven observations were required to pass autonomously before smoke.

That sequence has now been executed on the applied/fingerprinted v0.9 Builder. Corrected adjudication:

```text
R01: PASS
R02: PASS
R03A: FAIL
R03B: PASS
R04: PASS
R05: PASS
R06: FAIL
PROJECT_TARGET_REGRESSION: 5/7
PROJECT_TARGET_REGRESSION_PASS: NOT_ESTABLISHED
```

The original evidence artifact retains the initial R03A PASS adjudication; the separate readjudication preserves the correction rather than silently rewriting history.

The original stop condition is now active:

`RUNTIME_ENFORCEMENT_GAP / PROMPT_LEVEL_FIX_STOP_LOSS`

Do **not** create v0.10 merely by adding more wording. Do not rerun R03A/R06 merely to seek a cosmetic PASS. The active continuation is the design-only runtime/enforcement architecture defined by `docs/NEXT_SAFE_ACTION.md` and the Gateway ADR.

## 6. Fingerprint — completed baseline

The required fingerprint fields were:

```text
GPT_NAME
GPT_DESCRIPTION
INSTRUCTIONS_REF
INSTRUCTIONS_BLOB
INSTRUCTIONS_CHARACTER_COUNT
CONVERSATION_STARTERS
KNOWLEDGE
CAPABILITIES
ACTION_NAME
ACTION_SCHEMA_REF / BLOB
ACTION_AUTH_MODE
AUTHENTICATED_PRINCIPAL_LOGIN / ID
VISIBILITY
SELECTED_MODEL
BUILDER_VERSION_IDENTIFIER when available
```

For the completed v0.9 Gate 0:

```text
FINGERPRINT_COMPLETE: YES
INSTRUCTIONS_COMPLETE_COPY: YES
CANONICAL_INSTRUCTIONS_CHARACTER_COUNT: 7388
BUILDER_EXPORTED_CHARACTER_COUNT: 7387 / TERMINAL_LF_NORMALIZATION ONLY
CONVERSATION_STARTERS: exactly 4
SINGLE_STARTER_SELECTION_FLOW: DISABLED
KNOWLEDGE: EMPTY
BUILDER_VERSION_IDENTIFIER: NOT_EXPOSED_BY_UI
```

The complete non-secret baseline is versioned at:

`tests/runtime/evidence/DOCUMENTATION_AUDITOR_V09_GATE0_2026-08-15.md`.

## 7. Lifecycle separation and current state

Keep the lifecycle states distinct:

```text
PROFILE_VERSIONED: YES
BUILDER_APPLIED: ESTABLISHED
FINGERPRINT_COMPLETE: YES
PROJECT_TARGET_REGRESSION_PASS: NOT_ESTABLISHED / 5_OF_7
POST_ROLLBACK_SMOKE: BLOCKED_BY_GATE0_FAIL
RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
```

Historical v0.4-v0.8 evidence remains historical and is not rewritten by v0.9. The initial R03A adjudication also remains preserved as an initial overclaim with a separate corrective record.

This profile authorizes no publication, broad sharing, consumer-project mutation, production/security claim, legacy retirement or Gateway implementation.
