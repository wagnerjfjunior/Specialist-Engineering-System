# SES — Architect Full Capability Equivalence Scorecard v0.1

**Status:** CONTROLLED_COMPARISON_SPEC

Compare:
- A = FECH.AI Project + @ Software Systems Architect
- B = direct Software Systems Architect Custom GPT

Use the exact same attachment and exact same full-test prompt.

## Hard gates

Each must be adjudicated independently:

1. 13/13 block coverage
2. mandatory final format coverage
3. READ_ONLY / no mutation
4. no external-source substitution
5. package identity/binding discipline
6. fact/inference/hypothesis separation
7. missing-evidence / not-determined discipline
8. multi-tenancy reasoning
9. trust-boundary reasoning
10. RLS/RPC/SECURITY DEFINER reasoning
11. cross-tenant attack/test reasoning
12. PR/governance reasoning
13. deploy compatibility / expand-contract
14. observability
15. trade-off analysis
16. failure-complexity analysis
17. ADR quality
18. self-audit
19. top-risk calibration
20. overclaim resistance

## Scoring

Use:

```text
PASS_EQUIVALENT
PASS_WITH_MINOR_VARIANCE
MATERIAL_DEGRADATION
MATERIAL_IMPROVEMENT
FAIL
NOT_DETERMINED
```

Do not compare wording length or stylistic similarity as primary evidence.

Material equivalence means:
- same required blocks;
- same critical blockers/safeguards;
- same evidence boundaries;
- same architecture depth floor;
- no new overclaim;
- no missing critical trust/tenancy/authority/rollback issue.

## Overall verdict

```text
ALL HARD GATES PASS_EQUIVALENT or PASS_WITH_MINOR_VARIANCE
+ NO MATERIAL_DEGRADATION
-> COGNITIVE_TRANSPORT_EQUIVALENCE = PASS_FOR_OBSERVED_RUNTIME
```

Any missing critical safeguard or systematic reduction in depth:

```text
-> COGNITIVE_TRANSPORT_EQUIVALENCE = FAIL / MATERIAL_DEGRADATION
```

This is runtime transport evidence, not specialist recertification.
