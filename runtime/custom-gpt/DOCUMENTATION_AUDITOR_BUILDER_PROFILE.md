# SES — Documentation Auditor Custom GPT Builder Profile

**Status:** `RUNTIME_TARGET_V0_9 / BUILDER_APPLIED / FINGERPRINT_CAPTURED / GATE0_EXECUTED_FAIL / PROMPT_LEVEL_STOP_LOSS`
**ARCHETYPE_ID:** `documentation-auditor`
**Gate 0 evidence:** `tests/runtime/evidence/DOCUMENTATION_AUDITOR_V09_GATE0_2026-08-15.md`
**Gate 0 readjudication:** `tests/runtime/evidence/DOCUMENTATION_AUDITOR_V09_GATE0_READJUDICATION_2026-08-15.md`

## 1. Purpose and current lifecycle

This profile versions the bounded post-stop-loss v0.9 Documentation Auditor target-acquisition configuration. It does **not** reopen the retired single-starter/menu feature.

The configuration below remains the Builder target that was applied and fingerprinted for completed Gate 0. Former “apply then execute regression” instructions are historical application/test requirements, not an active queue.

```text
V0_8_S02_FECHAI_DIRECT_PROJECT: PASS / OBSERVED
V0_8_S03_BLOGS_DIRECT_PROJECT: PASS / OBSERVED
V0_8_GENERIC_TARGET_SELF_SES_RESPONSE: INDETERMINATE / TEST_INPUT_TARGET_AMBIGUOUS
V0_8_RETIRED_NUMBERED_MENU_RESPONSE: FAIL / BEHAVIORAL_REGRESSION

V0_9_BUILDER_APPLIED: ESTABLISHED
V0_9_FINGERPRINT_COMPLETE: YES
V0_9_INITIAL_R03A: PASS / INITIAL_OVERCLAIM_PRESERVED
V0_9_INITIAL_R05: PASS / INITIAL_OVERCLAIM_PRESERVED
V0_9_CORRECTED_R03A: FAIL / PRE-RECEIPT SUBSTANTIVE OUTPUT
V0_9_CORRECTED_R05: FAIL / UNSOLICITED USER-VISIBLE PROJECT ENUMERATION AFTER ZERO-MATCH
V0_9_R06: FAIL / EARLY SUBSTANTIVE COMPARISON + INVALID/INCOMPLETE READINESS
V0_9_PROJECT_TARGET_REGRESSION: 4/7
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

```text
BUILDER_INSTRUCTIONS_HARD_LIMIT: <= 8000 characters
SES_OPERATIONAL_BUDGET: <= 7500 characters
CURRENT_COMPACT_KERNEL_MEASURED_COUNT: 7388 characters
COUNT_METHOD: Unicode code-point count of repository text content
CURRENT_KERNEL_BLOB: 6ca9e1d22d7faf0639076e5d43332b3267ec2354
```

The applied Builder export differed only by terminal-LF normalization as recorded in durable evidence; no material kernel drift was established.

### Conversation starters

The applied v0.9 configuration uses exactly:

1. `Audite este documento ou PR no projeto que eu indicar e construa o claim-to-evidence mapping antes do veredito.`
2. `Verifique se estas afirmações estão realmente provadas pelas fontes canônicas live e identifique evidência faltante ou contraditória.`
3. `Faça uma auditoria multiarquivo com matriz de cobertura, provenance e proof obligations.`
4. `Revalide somente os claims invalidados por esta mudança de head/ref, sem repetir auditoria desnecessária.`

Starters do not establish target/project identity, readiness, configuration or authority.

### Knowledge

`EMPTY`

### Capabilities

```text
Web Search: ENABLED (supplementary only)
Code Interpreter / Data Analysis: ENABLED
Image Generation: DISABLED
Actions: ENABLED
Apps: record actual Builder UI state
```

### Actions / authentication

```text
ACTION_SCHEMA: runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml
Type: API key
Mode: Bearer
Secret value: Builder UI only / never committed
```

### Visibility

`PRIVATE / APENAS PARA MIM` until a separate publication decision.

### Model

Record actual selected Builder model in the fingerprint. Model changes may invalidate behavioral evidence. The completed Gate 0 model is recorded in durable evidence.

## 3. Target-acquisition/readiness invariants — normative intent

The v0.9 configuration intends:

- ambiguous SES-vs-consumer target → direct clarification → STOP;
- consumer-project task without identifier → direct clarification → STOP;
- explicit supplied identifier remains explicit even when registry resolution fails;
- project enumeration only for an explicit informational listing request;
- zero-match `PROJECT_NOT_REGISTERED` → fail closed / STOP without unsolicited project-choice enumeration;
- informational project listing never creates numeric identity;
- substantive multi-project tasks resolve each explicit project independently;
- no fuzzy project inference;
- no Adapter/project materialization before applicable explicit identity/resolution;
- canonically valid task-bound readiness before substantive project output;
- READ_ONLY default and exact mutation authorization.

The retired interaction remains excluded:

`# CLIQUE PARA INICIAR → numbered menu → numeric selection → PROJECT_SELECTED → WAIT FOR TASK → cross-turn resume`.

Gate 0 shows that these are normative configuration requirements, not mechanically enforced invariants: R03A failed receipt ordering, R05 failed the user-visible enumeration/zero-match STOP boundary, and R06 failed both output ordering and canonical readiness completeness.

## 4. Preserved independent hardenings

v0.9 configuration preserves four-starter UX, positive EOF proof before `INTEGRAL_READ`, fail-closed retrieval handling, claim/evidence/provenance/coverage/contradiction/freshness discipline, receipt-first/full-readiness requirements, cross-project isolation, READ_ONLY default and lifecycle anti-overclaim separation.

Observed failures do not erase specification requirements; they show the instruction-driven runtime did not satisfy all required behavior autonomously.

## 5. Gate 0 — historical execution requirement and completed result

The profile originally required executing:

`tests/runtime/DOCUMENTATION_AUDITOR_PROJECT_TARGET_REGRESSION.md`

Corrected completed result:

```text
R01: PASS
R02: PASS
R03A: FAIL
R03B: PASS
R04: PASS
R05: FAIL
R06: FAIL
PROJECT_TARGET_REGRESSION: 4/7
PROJECT_TARGET_REGRESSION_PASS: NOT_ESTABLISHED
```

The original evidence artifact retains initial R03A/R05 PASS adjudications; the separate readjudication preserves corrections instead of rewriting history.

The original stop condition is active:

`RUNTIME_ENFORCEMENT_GAP / PROMPT_LEVEL_FIX_STOP_LOSS`

Do **not** create v0.10 merely by adding wording or rerun R03A/R05/R06 merely to seek cosmetic PASS. Continue only from `docs/NEXT_SAFE_ACTION.md`.

## 6. Fingerprint — completed baseline

Required fields included name/description, instructions ref/blob/count, starters, Knowledge, capabilities, action/schema/auth, authenticated principal, visibility, model and Builder version identifier when exposed.

For completed v0.9 Gate 0:

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

Complete non-secret baseline: `tests/runtime/evidence/DOCUMENTATION_AUDITOR_V09_GATE0_2026-08-15.md`.

## 7. Lifecycle separation and current state

```text
PROFILE_VERSIONED: YES
BUILDER_APPLIED: ESTABLISHED
FINGERPRINT_COMPLETE: YES
PROJECT_TARGET_REGRESSION_PASS: NOT_ESTABLISHED / 4_OF_7
POST_ROLLBACK_SMOKE: BLOCKED_BY_GATE0_FAIL
RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
```

Historical v0.4-v0.8 evidence remains historical. Initial R03A/R05 over-adjudications remain preserved with a separate corrective record.

This profile authorizes no publication, broad sharing, consumer-project mutation, production/security claim, legacy retirement or Gateway implementation.
