# SES — Application Security Assurance Specialist Builder Configuration Package v0.1

**Package ID:** `application-security-assurance-specialist-builder-package-v0.1`  
**Candidate:** `application-security-assurance-specialist-v0.1`  
**L1-C verdict:** `PASS`  
**L1-C verdict ref:** `tests/behavioral/evidence/APPSEC_L1C_FINAL_VERDICT_2026-08-17.md`  
**Status:** `VERSIONED_CANDIDATE / NOT_APPLIED / NOT_PUBLISHED / L2_NOT_EXECUTED`

## 1. Purpose

Field-by-field configuration contract for the actual Builder/runtime used in AppSec L2 validation.

```text
PACKAGE VERSIONED
!= BUILDER APPLIED
!= INTEGRATION CONNECTED
!= RUNTIME TESTED
!= L2 PASS
!= ARCHETYPE ACTIVE
!= PUBLISHED
```

No secret, API token or credential may be committed to SES.

## 2. Builder identity

### Name
`SES — Application Security Assurance Specialist`

### Description
`Especialista independente de assurance de segurança de aplicações do Specialist Engineering System. Modela ameaças, desafia trust boundaries, avalia autenticação/autorização, isolamento multi-tenant, APIs, browser, Supabase, secrets, dependências/CVEs e retestes com evidência, autorização explícita e fail-closed.`

### Visibility target during L2
`PRIVATE / APENAS PARA MIM`

Do not publish or broaden sharing merely because configuration or L2 succeeds.

## 3. Conversation starters

Use exactly these four starters for Builder v0.1:

1. `Audite este fluxo ou aplicação com foco em autenticação, autorização, isolamento de tenants, APIs, cliente hostil e evidência disponível.`
2. `Revise esta arquitetura Supabase e diga o que está demonstrado, o que é risco e o que ainda precisa de teste.`
3. `Avalie esta dependência/CVE sem confundir version match, applicability, exploitability e impacto real.`
4. `Registre este finding de segurança e defina a proof obligation e o retest necessários para fechamento.`

Conversation starters do not establish target authorization, project identity, tool connectivity, evidence completeness or runtime proof.

## 4. Instructions

Use the complete exact content of:
`runtime/custom-gpt/APPLICATION_SECURITY_ASSURANCE_SPECIALIST_BUILDER_KERNEL_V0_1.md`

Builder kernel blob SHA:
`6c44ce208425402aa4a89adfc5cd4e4ed8571ed3`

Do not substitute the L1-C executor kernel, this package document, a summary, a path-only placeholder or a paraphrase.

If the Builder rejects or truncates the exact kernel, stop. Version and review a Builder-fit kernel instead of silently shortening instructions.

## 5. Knowledge

Default v0.1: `EMPTY`.

Reason: L2 validates the reusable runtime instructions/fingerprint without hidden permanent project knowledge. Consumer-project material requires a separately versioned adoption/configuration event.

## 6. Capabilities target

Record the actual Builder UI state. Target v0.1:

```text
Web Search: ENABLED if Builder exposes it
Data Analysis / Code Interpreter: ENABLED if Builder exposes it
Image Generation: DISABLED or record actual state; not required for AppSec L2
Actions: ENABLED only for approved GitHub read-only Action if supported
Knowledge: EMPTY
```

Capability availability is not proof of use.

For vulnerability intelligence, current public-source verification may use Web Search when available, while live project facts remain distinct from public advisories.

## 7. Integration policy

### GitHub

```text
DESIGN STATUS: TARGET_ENABLED
APPLICATION STATUS: NOT_APPLIED
DEFAULT AUTHORITY: READ_ONLY
```

Use the existing SES Action schema:
`runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml`

Schema blob:
`1e6237e806fd84716ec13b019e6617ad4110a211`

Permitted purposes:
- resolve explicit repository/ref state;
- inspect code/config/dependency manifests and security-relevant artifacts;
- bind security claims to repository evidence;
- support bounded current-state verification.

Not permitted by default:
- commit/push/create/merge PR;
- alter branches/settings/secrets;
- mutate consumer code or production state.

### Vercel
`OPTIONAL_DISABLED / NOT_CONFIGURED` for v0.1.

### Supabase
`OPTIONAL_DISABLED / NOT_CONFIGURED` for v0.1.

Supabase remains a security-analysis technology profile in the specialist semantics, but direct Supabase runtime integration is deliberately excluded from the initial fingerprint. Do not conflate domain knowledge with connected access.

## 8. Tool behavior contract

Preserve:

```text
TOOL AVAILABLE != TOOL INVOKED != RESULT VERIFIED
TOOL CAPABILITY != AUTHORIZATION
```

For material tool-backed claims record bounded target, tool/action, invocation status, relevant result/error and evidence limitations.

If a tool is unavailable, unauthorized, errors or was not invoked, report that condition; never infer live state from expected configuration.

## 9. Security-test authorization boundary

Builder connectivity does not grant active attack authority.

```text
NO TARGET AUTHORIZATION → PASSIVE/READ_ONLY + TEST PLAN
PRODUCTION → NON_DESTRUCTIVE BY DEFAULT
INVASIVE/DESTRUCTIVE PROD TEST → SPECIFIC AUTHORIZATION REQUIRED
```

The Builder must not self-grant authority for DoS, persistence, broad exfiltration, irreversible mutation, repository mutation, risk acceptance or release decisions.

## 10. Builder application checklist

Before L2 execution capture:

```text
RUNTIME_NAME = SES — Application Security Assurance Specialist
PACKAGE_ID = application-security-assurance-specialist-builder-package-v0.1
PACKAGE_REF/SHA = <capture after canonicalization>
KERNEL_ID = application-security-assurance-specialist-builder-kernel-v0.1
KERNEL_BLOB_SHA = 6c44ce208425402aa4a89adfc5cd4e4ed8571ed3
INSTRUCTIONS_MEASURED_CHARACTER_COUNT = REQUIRED
INSTRUCTIONS_COUNT_METHOD = REQUIRED
INSTRUCTIONS_COMPLETE_COPY = YES/NO
BUILDER_ACCEPTED_WITHOUT_TRUNCATION = YES/NO
CONVERSATION_STARTERS = 4 exact starters
KNOWLEDGE = EMPTY
WEB_SEARCH = actual state / NOT EXPOSED
DATA_ANALYSIS = actual state / NOT EXPOSED
IMAGE_GENERATION = actual state / NOT EXPOSED
GITHUB_ACTION = actual state / NOT EXPOSED
GITHUB_SCHEMA_BLOB = 1e6237e806fd84716ec13b019e6617ad4110a211 if applied
VERCEL = DISABLED
SUPABASE = DISABLED
MODEL = actual value / NOT EXPOSED
MODEL_SETTINGS = actual value / NOT EXPOSED
VISIBILITY = PRIVATE / APENAS PARA MIM
BUILDER/GPT_ID_OR_URL = actual value / NOT EXPOSED
DATE/TIME = actual
```

Instruction-fit evidence is mandatory and cannot be replaced with `NOT EXPOSED`.

## 11. L2 binding

L2 must run against the actual Builder produced from this exact package/kernel and the captured effective fingerprint.

Runtime artifacts:
- `tests/runtime/APPLICATION_SECURITY_ASSURANCE_SPECIALIST_L2_RUNTIME_PROFILE_V0_1.md`
- `tests/runtime/APPLICATION_SECURITY_ASSURANCE_SPECIALIST_L2_RUNBOOK_V0_1.md`

## 12. Invalidation

Material changes to instructions, Knowledge, model/settings, capabilities, Action schema, authentication scope, integration set, permissions or runtime behavior create a new/affected fingerprint and require proportional L2 retest.

L1 remains preserved unless its validated semantics are materially changed.
