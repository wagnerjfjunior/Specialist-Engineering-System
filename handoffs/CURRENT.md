# SES — Current Handoff

**Status:** `SFJM_OPERATIONAL_CONTINUITY_V0_1 / STOP_LOSS_ROLLBACK_STATE`
**Canonical source:** `wagnerjfjunior/Specialist-Engineering-System`
**Canonical ref rule:** resolve `main` live before material work
**Continuity contract:** `core/protocols/PROJECT_CONTINUITY_CONTRACT.md`
**Authoritative next action:** `docs/NEXT_SAFE_ACTION.md`
**Next action ID:** `reconcile-ses-builders-to-multi-starter-baselines-v1`

## 1. Purpose

Preserve the durable stop-loss decision and safe continuation after retiring the single-starter project-selection feature.

Consumer-project truth, continuity and authority remain project-owned.

## 2. Reading order

1. resolve SES `main` live and read `docs/bootstrap/INDEX.md`;
2. read `handoffs/CURRENT.md`;
3. read `docs/PROJECT_STATUS.md`;
4. read `docs/NEXT_SAFE_ACTION.md`;
5. read `docs/BLOCKED_ACTIONS.md`;
6. then read task-material contracts/runtime evidence.

## 3. Durable state

1. SES remains project-agnostic.
2. SFJM continuity remains operational; `LIVE_RESOLVED_STATE != MATERIAL_RECORDED_STATE`.
3. SaaS Architect v0.1 historical runtime PASS T01–T29 = 29/29 remains preserved for its exact historical fingerprint.
4. PRs #14/#15 introduced the single-starter / selection-first / deferred cross-turn project-entry experiment.
5. PR #16 fixed EOF/`INTEGRAL_READ` overclaim behavior; preserve it.
6. PR #17 fixed the Documentation Auditor receipt-order specification contradiction; preserve receipt-before-substantive-output.
7. PR #18 bounded mechanical-enforcement claims; preserve that learning without more prompt-hardening loops.
8. PR #19 is closed without merge as `ABANDONED / STOP-LOSS` and remains historical.
9. PR #20 merged the controlled rollback and retired `# CLIQUE PARA INICIAR → menu → number → PROJECT_SELECTED → WAIT FOR TASK → resume`.
10. Direct project + substantive-task bootstrap semantics and multi-starter UX are the active interaction model.
11. Historical v0.4/v0.5/v0.6 failures remain failures; no retroactive PASS.
12. Documentation Auditor v0.8 is the post-stop-loss repository target.
13. SaaS Architect historical certified kernel blob `50672d09665035c0f60f18887f3295a5ea8cad03` remains historical evidence but exceeds the present Builder Instructions limit when copied in the current UI.
14. The current SaaS Builder target is the compact v0.1-semantics kernel `runtime/custom-gpt/SAAS_ARCHITECT_BUILDER_KERNEL.md`, measured at 6182 code points; it is a new Builder fingerprint and requires proportional smoke.
15. `runtime/custom-gpt/UNIVERSAL_BUILDER_KERNEL.md` is retained only as a deprecated compatibility locator and must not be copied into Builder Instructions.
16. No consumer project is automatically mutated by SES changes.

## 4. Current required behavior

For project-specific substantive work:

```text
TASK_SCOPE + EXPLICIT PROJECT_IDENTIFIER
→ SES live/bootstrap/archetype
→ projects/REGISTRY.md
→ unique Project Adapter
→ consumer project live/bootstrap/local specialist
→ task-material/mandatory sources
→ task-bound Context Readiness Receipt
→ project-specific substantive work
```

If project identity is missing, ask for it directly. Do not require a generated numbered menu or numeric cross-turn selection state.

Preserve:

```text
CONTEXT_READINESS_RECEIPT
→ PROJECT-SPECIFIC VERDICT / FINDINGS / RISKS / RECOMMENDATIONS

EXACT_READER_SUCCESS != EOF_PROOF
NO_VISIBLE_TRUNCATION != EOF_PROOF
UNPROVEN_EOF -> PARTIAL_READ
INTEGRAL_READ -> POSITIVE START-THROUGH-EOF PROOF + STABLE TARGET IDENTITY
```

Keep separate:

```text
NORMATIVE_REQUIREMENT
BEHAVIORAL_COMPLIANCE
MECHANICALLY_ENFORCED_INVARIANT
```

## 5. Preserved evidence

```text
SAAS_V0_1_RUNTIME_BEHAVIORAL_PROOF: PASS / HISTORICAL / PRESERVED
SAAS_HISTORICAL_KERNEL_BLOB: 50672d09665035c0f60f18887f3295a5ea8cad03
SAAS_CURRENT_BUILDER_FIT_KERNEL: NEW FINGERPRINT / PROPORTIONAL SMOKE REQUIRED
SAAS_V0_2_V0_3_SELECTION_FIRST_TARGETS: SUPERSEDED_BY_STOP_LOSS

DA_V0_4_P09_ATTEMPT_1: FAIL / PRESERVED
DA_V0_4_P09_ATTEMPT_2: FAIL / PRESERVED
DA_V0_5_C01: PASS / HISTORICAL / PRESERVED
DA_V0_5_P09_ATTEMPT_1: FAIL / PRESERVED
DA_V0_6_P09_ATTEMPT_1: FAIL / PRESERVED
DA_V0_6_UNSUPPORTED_INTEGRAL_READ_PROMOTION: 0 / PRESERVED
DA_V0_6_RECEIPT_MECHANICAL_ENFORCEMENT: NOT_ESTABLISHED / PRESERVED
DA_V0_7: ABANDONED / STOP_LOSS / PR #19 NOT_MERGED
DA_V0_8: ROLLBACK_TARGET
```

## 6. Next action

Authoritative source: `docs/NEXT_SAFE_ACTION.md`.

Reconcile both external private SES Builders to their current multi-starter repository profiles, capture fresh non-secret fingerprints, execute proportional smoke only, then return to ordinary SES development.

For SaaS Architect, copy only `runtime/custom-gpt/SAAS_ARCHITECT_BUILDER_KERNEL.md` into Instructions; do not manually truncate or use the deprecated universal locator.

## 7. Short resume prompt

```text
SES -> resolve main live -> starter/menu/cross-turn selection retired by stop loss -> PR #20 rollback merged -> direct project+task bootstrap active -> SaaS historical v0.1 PASS preserved only for historical fingerprint -> current SaaS Builder-fit kernel is SAAS_ARCHITECT_BUILDER_KERNEL.md (6182 chars) -> DA v0.8 remains rollback target -> next: reconcile both Builders -> proportional smoke -> continue SES; do not reopen starter-menu experiment.
```
