# SES — Next Safe Action

> Este é o registro atual autoritativo da única próxima ação segura do SES.

**Next action ID:** `reconcile-documentation-auditor-runtime-candidate-v1`
**Target:** `SES — Documentation Auditor`
**Canonical source:** `wagnerjfjunior/Specialist-Engineering-System` / `main` resolved live

## Action

Reconcile the current Documentation Auditor runtime candidate with the versioned SES profile before claiming or executing runtime certification.

## Required sources

Read on the exact live SES ref:

1. `docs/bootstrap/INDEX.md`;
2. `archetypes/REGISTRY.md` and the resolved `documentation-auditor` archetype;
3. `runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_PROFILE.md`;
4. `runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_KERNEL.md`;
5. `tests/runtime/DOCUMENTATION_AUDITOR_RUNTIME_RUNBOOK.md`.

Then compare the actually observed runtime candidate with those canonical sources and record only what is established, missing or divergent.

## Done condition

The action is complete when the candidate is classified as one of:

- `READY_FOR_RUNTIME_PROOF_PRECONDITIONS`;
- `LIMITED` with explicit gaps;
- `BLOCKED` with explicit blockers.

No runtime PASS may be declared by this reconciliation alone.

## Limits

This action is observation and reconciliation only. It does not authorize configuration changes, publication, consumer-project changes, legacy retirement or runtime certification.

## Anti-loop

Do not reopen completed SaaS Architect proof states without a material invalidation event.

Do not replace this record for ordinary commits or conversation changes. Replace it only after this semantic action is completed, materially invalidated or explicitly superseded.
