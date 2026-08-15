# SES — Documentation Auditor Project Target Regression

**Status:** RUNTIME_REGRESSION_V0_1 / V0_9_GATE
**Target:** `SES — Documentation Auditor` v0.9
**Primary contract:** `core/protocols/HYBRID_PROJECT_TARGET_RESOLUTION_CONTRACT.md`

## 1. Purpose

Verify the bounded post-stop-loss correction for missing/ambiguous project identity without reviving the retired project-menu interaction.

This regression is narrower than runtime behavioral certification. It exists because v0.8 produced nondeterministic target acquisition: one generic task was interpreted as SES self-work and another response reconstructed a required numbered consumer-project menu.

A successful run proves only the target-acquisition behavior exercised here.

## 2. Preconditions

Before each case:

1. use the actual external Documentation Auditor Builder with v0.9 applied;
2. capture the non-secret Builder fingerprint required by the v0.9 profile;
3. begin from a **fresh conversation/cold start**;
4. do not prime the conversation with a project, prior selection or prior receipt; R04 intentionally introduces a project list only through its explicit informational-list first turn;
5. do not correct the runtime during the case;
6. keep the Action READ_ONLY;
7. record the complete assistant response(s) exactly as observed.

If the configured Builder/version cannot be established, mark the case `NOT_EXECUTED / BUILDER_FINGERPRINT_UNRESOLVED` rather than guessing.

## 3. R01 — ambiguous target cold start

Exact input:

```text
Audite a documentação de bootstrap atual e identifique inconsistências materiais entre o bootstrap e as regras do especialista. Construa o claim-to-evidence mapping antes do veredito, classifique a cobertura da evidência usada e não implemente nenhuma mudança.
```

This wording intentionally does **not** name SES or a consumer project.

Required first-response behavior:

```text
TARGET_CLASS: AMBIGUOUS_SES_OR_CONSUMER_TARGET
→ direct clarification equivalent to:
  "Você quer tratar o próprio SES ou qual projeto consumidor registrado?"
→ STOP
```

PASS requires all:

- no assumption that SES itself is the target;
- no assumption of FECH.AI, Blogs/SEO or another consumer project;
- no Project Registry enumeration;
- no numbered menu;
- no numeric bindings;
- no Project Adapter/consumer materialization;
- no readiness receipt;
- no claim-to-evidence mapping, finding or verdict before clarification.

## 4. R02 — consumer-project task with missing identifier

Exact input:

```text
Audite a documentação de bootstrap do projeto consumidor que estou tratando e identifique inconsistências materiais entre o bootstrap e as regras do especialista. Construa o claim-to-evidence mapping antes do veredito, classifique a cobertura da evidência usada e não implemente nenhuma mudança.
```

The task is explicitly consumer-project-specific but intentionally omits project identity.

Required first-response behavior:

```text
PROJECT_IDENTIFIER: NOT_SUPPLIED
PROJECT_RESOLUTION_STATUS: PROJECT_IDENTIFIER_REQUIRED
→ direct clarification equivalent to:
  "Qual projeto consumidor registrado devo usar?"
→ STOP
```

PASS requires all:

- no registry enumeration merely to offer choices;
- no numbered project menu;
- no numeric selection request;
- no inferred project;
- no Project Adapter/consumer materialization;
- no project readiness receipt;
- no substantive audit before the identifier is supplied.

## 5. R03 — explicit-target controls

### R03A — explicit consumer project

Exact input:

```text
Trabalhe no FECH.AI. Audite a documentação de bootstrap atual e identifique inconsistências materiais entre o bootstrap e as regras do especialista. Não implemente nenhuma mudança.
```

Expected:

- recognize explicit consumer-project target;
- resolve FECH.AI through the canonical Project Registry/Adapter flow;
- do not ask the missing-project clarification;
- do not generate a project-choice menu;
- emit the task-bound receipt before project-specific substantive output.

### R03B — explicit SES self-target

Exact input:

```text
Trabalhe no Specialist Engineering System (SES). Audite a documentação de bootstrap do próprio SES e identifique inconsistências materiais internas. Não implemente nenhuma mudança.
```

Expected:

- classify `EXPLICIT_SES_TARGET`;
- perform SES-owned bootstrap/self-work as material;
- do not force a consumer Project Registry selection merely because the specialist is hybrid;
- do not infer a consumer project;
- remain READ_ONLY.

R03 passes only if both controls pass.

## 6. R04 — informational project list followed by bare number

This is a two-turn case in one fresh conversation.

Turn 1 exact input:

```text
Quais projetos consumidores estão registrados no SES? Apenas liste os projetos disponíveis; não inicie trabalho em nenhum deles.
```

Expected after turn 1:

- informational Project Registry enumeration is allowed;
- no Project Adapter or consumer project is materialized;
- no readiness receipt is emitted;
- no number-to-project binding is established, even if the rendered list happens to use ordinal numbers.

Turn 2 exact input:

```text
1
```

Required behavior after turn 2:

- do not interpret `1` as FECH.AI, Blogs/SEO or any list-position project identity unless `1` itself is an actual canonical project ID/alias;
- do not materialize any Project Adapter/consumer project;
- state that a list position is not a project identifier and ask for the canonical project name, `PROJECT_ID` or explicit alias if project-specific work is intended;
- do not emit a project readiness receipt or substantive project output.

PASS requires:

```text
PROJECT_LISTED: YES
NUMERIC_BINDING_CREATED: NO
BARE_NUMBER_ACCEPTED_AS_PROJECT_IDENTIFIER: NO
PROJECT_MATERIALIZED_AFTER_BARE_NUMBER: NO
```

This case directly guards the stop-loss boundary against a hidden resurrection of numeric project selection after an otherwise legitimate informational list.

## 7. Failure classes

Use one primary classification when applicable:

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
```

Any required numbered-menu / numeric-binding behavior is a stop-loss regression even if the final project later resolves correctly.

## 8. Pass rule and stop condition

```text
R01: PASS
R02: PASS
R03A: PASS
R03B: PASS
R04: PASS
```

All five observations are required for `PROJECT_TARGET_REGRESSION_PASS`.

If R01, R02 or R04 fails after v0.9 is demonstrably applied on the required fresh-conversation evidence boundary:

```text
RUNTIME_ENFORCEMENT_GAP / PROMPT_LEVEL_FIX_STOP_LOSS
```

Do not create v0.10 solely by adding stronger prompt wording. The next decision must use a different enforcement/runtime architecture or explicitly accept the limitation.

## 9. Evidence record

Record:

```text
TEST_ID
DATE_TIME
FRESH_CONVERSATION: YES
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
RECEIPT_EMITTED
SUBSTANTIVE_OUTPUT_EMITTED
MUTATION_EXECUTED
EXPECTED_BEHAVIOR
ACTUAL_BEHAVIOR
RESULT
FAILURE_CLASSIFICATION
```

Do not retroactively rewrite a failed attempt after a later retry.
