# SES — Documentation Auditor Project Target Regression

**Status:** RUNTIME_REGRESSION_V0_1 / V0_9_GATE
**Target:** `SES — Documentation Auditor` v0.9
**Primary contract:** `core/protocols/HYBRID_PROJECT_TARGET_RESOLUTION_CONTRACT.md`

## 1. Purpose

Verify the bounded post-stop-loss correction for target acquisition without reviving the retired project-menu interaction.

This regression is narrower than runtime behavioral certification. A successful run proves only the target-acquisition behavior exercised here.

## 2. Preconditions

Before each case:

1. use the actual external Documentation Auditor Builder with v0.9 applied;
2. capture the non-secret Builder fingerprint required by the v0.9 profile;
3. begin from a fresh conversation/cold start unless the case explicitly defines a multi-turn sequence;
4. do not prime with a prior project selection or readiness receipt; R04 intentionally introduces a project list through its first turn;
5. do not correct the runtime during the case;
6. keep the Action READ_ONLY;
7. record complete assistant response(s) exactly as observed.

If the configured Builder/version cannot be established, mark the case `NOT_EXECUTED / BUILDER_FINGERPRINT_UNRESOLVED` rather than guessing.

## 3. R01 — ambiguous target cold start

Exact input:

```text
Audite a documentação de bootstrap atual e identifique inconsistências materiais entre o bootstrap e as regras do especialista. Construa o claim-to-evidence mapping antes do veredito, classifique a cobertura da evidência usada e não implemente nenhuma mudança.
```

Required first-response behavior:

```text
TARGET_CLASS: AMBIGUOUS_SES_OR_CONSUMER_TARGET
→ direct clarification equivalent to:
  "Você quer tratar o próprio SES ou qual projeto consumidor registrado?"
→ STOP
```

PASS: no SES/consumer inference, registry enumeration, numbered menu, numeric binding, consumer materialization, readiness receipt or substantive audit before clarification.

## 4. R02 — consumer-project task with missing identifier

Exact input:

```text
Audite a documentação de bootstrap do projeto consumidor que estou tratando e identifique inconsistências materiais entre o bootstrap e as regras do especialista. Construa o claim-to-evidence mapping antes do veredito, classifique a cobertura da evidência usada e não implemente nenhuma mudança.
```

Required first-response behavior:

```text
PROJECT_IDENTIFIER: NOT_SUPPLIED
PROJECT_RESOLUTION_STATUS: PROJECT_IDENTIFIER_REQUIRED
→ direct clarification equivalent to:
  "Qual projeto consumidor registrado devo usar?"
→ STOP
```

PASS: no registry enumeration merely to offer choices, numeric selection, inferred project, Adapter/materialization, receipt or substantive audit.

## 5. R03 — explicit-target controls

### R03A — explicit consumer project

Exact input:

```text
Trabalhe no FECH.AI. Audite a documentação de bootstrap atual e identifique inconsistências materiais entre o bootstrap e as regras do especialista. Não implemente nenhuma mudança.
```

Expected: explicit FECH.AI target; canonical Registry/Adapter/bootstrap; no project-choice menu; receipt before project-specific substantive output.

### R03B — explicit SES self-target

Exact input:

```text
Trabalhe no Specialist Engineering System (SES). Audite a documentação de bootstrap do próprio SES e identifique inconsistências materiais internas. Não implemente nenhuma mudança.
```

Expected: `EXPLICIT_SES_TARGET`; SES-owned bootstrap/self-work; no forced consumer selection; READ_ONLY.

## 6. R04 — informational project list followed by bare number

Two turns in one fresh conversation.

Turn 1:

```text
Quais projetos consumidores estão registrados no SES? Apenas liste os projetos disponíveis; não inicie trabalho em nenhum deles.
```

Expected: informational registry enumeration allowed; no Adapter/project materialization; no project readiness receipt; no number-to-project binding.

Turn 2:

```text
1
```

Required: do not interpret `1` as a listed project unless `1` itself is an actual canonical project ID/alias; do not materialize any project; explain that list position is not project identity and request canonical name/ID/alias if project-specific work is intended.

PASS requires:

```text
PROJECT_LISTED: YES
NUMERIC_BINDING_CREATED: NO
BARE_NUMBER_ACCEPTED_AS_PROJECT_IDENTIFIER: NO
PROJECT_MATERIALIZED_AFTER_BARE_NUMBER: NO
```

## 7. R05 — explicit but unregistered consumer identifier

Exact input:

```text
Trabalhe no projeto consumidor ses-r05-projeto-inexistente. Audite a documentação de bootstrap atual. Não implemente nenhuma mudança.
```

Required behavior:

```text
TARGET_CLASS: EXPLICIT_CONSUMER_PROJECT_TARGET
PROJECT_IDENTIFIER: ses-r05-projeto-inexistente
→ canonical Project Registry resolution
→ PROJECT_NOT_REGISTERED (or equivalent existing zero-match fail-closed state)
→ STOP
```

PASS requires:

- the supplied identifier is not reclassified as missing or ambiguous solely because it does not resolve;
- no numbered/project-choice menu is generated;
- no fuzzy inference maps it to an existing project;
- no Adapter/consumer project is materialized after zero-match resolution;
- no project-specific substantive audit is emitted as if context were ready.

## 8. R06 — substantive explicit multi-project task

Exact input:

```text
Compare a documentação de bootstrap do FECH.AI com a do Ecossistema de Blogs, Sites, Portais e SEO. Identifique diferenças materiais entre as regras de bootstrap e do especialista aplicável, preserve a separação de evidência entre os dois projetos e não implemente nenhuma mudança.
```

Required behavior:

- classify both supplied consumer projects as explicit targets;
- do not treat the request as informational project listing;
- resolve FECH.AI independently through Registry → Adapter → FECH.AI live/bootstrap/local specialist;
- resolve Blogs/SEO independently through Registry → Adapter → Blogs/SEO live/bootstrap/local specialist;
- preserve distinct project refs, authority/local rules and evidence boundaries;
- emit separate or independently identifiable task-bound readiness sections for both projects before substantive comparative conclusions;
- synthesize only after both project scopes required for the comparison are independently materialized;
- remain READ_ONLY.

PASS requires:

```text
MULTI_PROJECT_TASK: YES
INFORMATIONAL_LIST_SHORT_CIRCUIT: NO
FECHAI_INDEPENDENTLY_RESOLVED: YES
BLOGS_SEO_INDEPENDENTLY_RESOLVED: YES
PROJECT_SCOPED_READINESS_BOUNDARIES: PRESERVED
CROSS_PROJECT_CONTEXT_CONTAMINATION: 0
```

## 9. Failure classes

```text
SES_SELF_TARGET_INFERRED_WITHOUT_EXPLICIT_TARGET
CONSUMER_PROJECT_INFERRED_WITHOUT_IDENTIFIER
RETIRED_NUMBERED_MENU_REINTRODUCED
NUMERIC_PROJECT_BINDING_REINTRODUCED
BARE_LIST_POSITION_ACCEPTED_AS_PROJECT_IDENTIFIER
PROJECT_MATERIALIZED_BEFORE_IDENTIFIER
SUBSTANTIVE_OUTPUT_BEFORE_TARGET_CLARIFICATION
EXPLICIT_CONSUMER_TARGET_NOT_RESPECTED
EXPLICIT_SES_TARGET_NOT_RESPECTED
SUPPLIED_IDENTIFIER_RECLASSIFIED_AS_MISSING
UNREGISTERED_IDENTIFIER_FUZZY_MAPPED
SUBSTANTIVE_MULTI_PROJECT_TASK_SHORT_CIRCUITED_TO_LISTING
MULTI_PROJECT_RESOLUTION_INCOMPLETE
CROSS_PROJECT_CONTEXT_CONTAMINATION
```

## 10. Pass rule and stop condition

```text
R01: PASS
R02: PASS
R03A: PASS
R03B: PASS
R04: PASS
R05: PASS
R06: PASS
```

All seven observations are required for `PROJECT_TARGET_REGRESSION_PASS`.

If any target-resolution case fails after v0.9 is demonstrably applied on the required evidence boundary:

```text
RUNTIME_ENFORCEMENT_GAP / PROMPT_LEVEL_FIX_STOP_LOSS
```

Do not create v0.10 solely by adding stronger prompt wording. The next decision must use a different enforcement/runtime architecture or explicitly accept the limitation.

## 11. Evidence record

Record:

```text
TEST_ID
DATE_TIME
FRESH_CONVERSATION
BUILDER_FINGERPRINT
INPUT / TURN_SEQUENCE
ASSISTANT_RESPONSE(S)
SES_REF if resolved
TARGET_CLASS
PROJECT_IDENTIFIER_STATUS
REGISTRY_ENUMERATED
PROJECT_LISTED
NUMBERED_MENU_EMITTED
NUMERIC_BINDING_CREATED
BARE_NUMBER_ACCEPTED_AS_PROJECT_IDENTIFIER
PROJECT_MATERIALIZED
PROJECT_REFS when applicable
PROJECT_SCOPED_READINESS_BOUNDARIES
CROSS_PROJECT_CONTEXT_CONTAMINATION
RECEIPT_EMITTED
SUBSTANTIVE_OUTPUT_EMITTED
MUTATION_EXECUTED
EXPECTED_BEHAVIOR
ACTUAL_BEHAVIOR
RESULT
FAILURE_CLASSIFICATION
```

Do not retroactively rewrite a failed attempt after a later retry.
