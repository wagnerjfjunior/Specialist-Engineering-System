# SES — Next Safe Action

> Este é o registro atual autoritativo da única próxima ação segura do SES.

**Next action ID:** `reconcile-standardized-project-entry-runtime-targets-v1`
**Primary target:** `SES — Documentation Auditor` v0.3
**Affected target:** `SES — SaaS Architect` v0.2
**Canonical source:** `wagnerjfjunior/Specialist-Engineering-System` / `main` resolved live

## Why this action supersedes the prior one

The standardized hybrid project-entry change materially changes the runtime targets for both current hybrid specialists:

- Documentation Auditor target moves from Builder profile/kernel v0.2 to v0.3;
- SaaS Architect target moves from the historically certified v0.1 baseline to a new v0.2 target;
- both targets standardize `# CLIQUE PARA INICIAR` and the shared P01–P08 project-entry proof obligations;
- the historical SaaS Architect v0.1 `RUNTIME_BEHAVIORAL_PROOF = PASS` remains preserved, but it must not be reused as v0.2 proof.

The previous action `reconcile-documentation-auditor-runtime-candidate-v1` is therefore materially superseded rather than silently completed.

## Action

After the standardized project-entry change is canonical on SES `main`, reconcile the actually configured external Builders against the exact canonical runtime targets, in this order:

1. `SES — Documentation Auditor` v0.3;
2. `SES — SaaS Architect` v0.2.

For each target:

1. resolve SES `main` live;
2. read `docs/bootstrap/INDEX.md`;
3. resolve the applicable archetype through `archetypes/REGISTRY.md`;
4. read the exact Builder profile and compact kernel on the same canonical ref;
5. read the applicable runtime runbook and shared hybrid behavioral spec;
6. compare the actually observed Builder configuration with the target profile;
7. capture only non-secret fingerprint evidence;
8. classify the target as `READY_FOR_RUNTIME_PROOF_PRECONDITIONS`, `LIMITED` with explicit gaps, or `BLOCKED` with explicit blockers.

For SaaS Architect, preserve separately:

```text
V0_1_RUNTIME_BEHAVIORAL_PROOF: PASS / HISTORICAL / PRESERVED
V0_2_RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED until separately proven
```

## Done condition

This semantic action is complete when both affected external Builders have a current target-bound reconciliation record and no historical proof has been rewritten or silently promoted across versions.

A reconciliation result does not itself establish runtime behavioral PASS.

## Limits

This action authorizes observation, reconciliation and evidence classification only.

It does **not** by itself authorize:

- changing either external Builder;
- publication or sharing changes;
- consumer-project mutation;
- write-capable production Actions;
- runtime behavioral certification;
- project-local equivalence promotion;
- legacy specialist retirement.

Any external Builder mutation requires separate explicit Product Authority authorization applicable to the exact change.

## Anti-loop

Do not reopen or downgrade the certified SaaS Architect v0.1 proof. Revalidate only the new v0.2 target and evidence invalidated by its material runtime changes.

Do not replay unrelated gates merely because a new profile version exists.

Replace this record only after this semantic action is completed, materially invalidated or explicitly superseded by a new authorized objective.
