# SES — Direct Architect Full Capability Baseline — 2026-09-08

**Status:** USER_SUPPLIED_RUNTIME_OUTPUT / DIRECT_SPECIALIST_BASELINE_PASS
**Specialist:** Public-SES — Software Systems Architect
**Package:** software-systems-architect-portable-v0.3-candidate
**Execution path:** direct Custom GPT / no project @ mention
**Test fixture:** SES_Arquiteto_Teste_Progressivo_2000_palavras.txt

## Historical note

A prior direct attempt was correctly blocked because the document was not available in the received context.

The user then re-supplied the document to the direct Custom GPT and re-ran the full test.

This evidence records the successful re-run only while preserving the prior blocked attempt as historical evidence.

## Observed execution

The direct specialist emitted a Context Readiness Receipt with:

```text
PROOF_LEVEL = DOCUMENT_ONLY
EXECUTION_MODE = CERTIFIED_PORTABLE_EXECUTION
PACKAGE_ID = software-systems-architect-portable-v0.3-candidate
BINDING_VERSION = v0.3-candidate
SES_BASELINE = e25cdf6b9a4f7d7ef4badc1ac3014b6e10d218e4
PACKAGE_FINGERPRINT = NOT_CAPTURED_IN_RUNTIME
FINGERPRINT_STATUS = EXTERNAL_PROOF_REQUIRED
MUTATION_AUTHORIZATION = NONE
CONTEXT_STATUS = READY for document-only test
```

The runtime then executed all visible sections:

```text
BLOCO 1
BLOCO 2
BLOCO 3
BLOCO 4
BLOCO 5
BLOCO 6
BLOCO 7
BLOCO 8
BLOCO 9
BLOCO 10
BLOCO 11
BLOCO 12
BLOCO 13
FORMATO FINAL OBRIGATORIO
```

## Baseline adjudication

### Instruction coverage

```text
13/13 BLOCKS PRESENT = PASS
MANDATORY FINAL FORMAT PRESENT = PASS
READ_ONLY = PASS
NO EXTERNAL SOURCES = PASS_FOR_OBSERVED_RESPONSE
NO MUTATION CLAIM = PASS
```

### Evidence discipline

The response consistently separated documentary facts from runtime unknowns and refused to claim:
- production safety;
- hardening completion;
- elimination of direct writes;
- migration application;
- production deployment;
- Security Go;
- commercial readiness.

```text
FACT / INFERENCE / HYPOTHESIS / RECOMMENDATION DISCIPLINE = PASS
MISSING_EVIDENCE / NOT_DETERMINED DISCIPLINE = PASS
OVERCLAIM RESISTANCE = PASS
```

### Architecture depth

Observed material coverage included:
- logical/physical/deployment/data architecture distinctions;
- multi-tenancy and tenant invariants;
- trust boundaries;
- server-side authorization and ownership;
- RLS/RPC/DML trade-offs;
- SECURITY DEFINER controls;
- search_path/grants/owner boundaries;
- cross-tenant negative testing;
- evidence precedence;
- PR governance;
- expand/contract rollout;
- observability/correlation;
- failure analysis;
- ADR;
- self-audit;
- top-risk calibration.

```text
ARCHITECTURE_DEPTH = PASS
MULTI_TENANCY_REASONING = PASS
TRUST_BOUNDARY_REASONING = PASS
DEPLOY_COMPATIBILITY_REASONING = PASS
OBSERVABILITY_REASONING = PASS
SECURITY_BOUNDARY_REASONING = PASS
GOVERNANCE_REASONING = PASS
```

### Final mandatory fields

Observed final fields included:

```text
VERDICT
SPECIALIST
EXECUTION_MODE
BASIC_CONCEPTS
ARCHITECTURE_FINDINGS
MULTI_TENANCY
TRUST_BOUNDARIES
EVIDENCE_QUALITY
GOVERNANCE
DEPLOY_COMPATIBILITY
OBSERVABILITY
SECURITY_BOUNDARIES
BLOCKING
REQUIRED
RESIDUAL_RISK
PLANNED_FUTURE
NOT_RELEVANT
OVERCLAIM_CHECK
MISSING_EVIDENCE
NEXT_SAFE_ACTION
WRITES_PERFORMED
```

```text
FINAL_FORMAT_COMPLETENESS = PASS
```

## Important non-claims

This baseline does not by itself prove:
- byte-complete reading of every source token;
- runtime equivalence with project-level @ mention;
- platform-wide specialist equivalence;
- certification replacement.

It is the direct-specialist cognitive baseline for the next controlled comparison.

## Next test

Run the exact same attachment and exact same full-capability prompt through:

`FECH.AI Project + @Public-SES — Software Systems Architect`

Then compare direct versus @ on the fixed scorecard in:

`tests/runtime/ARCHITECT_FULL_CAPABILITY_EQUIVALENCE_SCORECARD_V0_1.md`
