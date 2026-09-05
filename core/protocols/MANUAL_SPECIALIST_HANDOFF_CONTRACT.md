# SES — Manual Specialist Handoff Contract v0.3

**Contract ID:** `manual-specialist-handoff-contract-v0.3`  
**Status:** `CANONICAL_V0_3 / CURRENT_OPERATIONAL_TRANSPORT / CANONICAL_TARGET_IDENTITY_ENFORCED / CONSUMER_RECERTIFICATION_DETOUR_FORBIDDEN`  
**Scope:** SES-mediated consultation of reusable specialists when direct Router/Gateway composition is not an accepted operational path.

## 1. Purpose

This contract defines how SES prepares, transfers and receives a specialist consultation without pretending that one Custom GPT executed another specialist.

The current accepted transport is human-mediated copy/paste:

```text
SES ORCHESTRATION
-> SPECIALIST CONSULTATION PACKET
-> HUMAN COPY
-> TARGET SPECIALIST CUSTOM GPT
-> HUMAN PASTE
-> SPECIALIST WORK
-> SPECIALIST RESULT PACKET
-> HUMAN COPY
-> SES
-> SES ADJUDICATION / NEXT DECISION
```

The transport is deliberately separated from the consultation semantics. A future transport may replace manual copy/paste only after its own operational evidence and explicit adoption.

```text
HANDOFF_CONTRACT != TRANSPORT_IMPLEMENTATION
TESTED_TRANSPORT != ACCEPTED_OPERATIONAL_TRANSPORT
```

## 2. Current operational status

As of the correction that introduced this contract:

```text
CURRENT_SPECIALIST_TRANSPORT = MANUAL_COPY_PASTE
SPECIALIST_ROUTER = NOT_CURRENT_OPERATIONAL_PATH
RUNTIME_ENFORCEMENT_GATEWAY = NOT_CURRENT_OPERATIONAL_PATH
```

Historical Gateway/Router tests remain historical evidence for the exact tested objects and fingerprints. They are not erased and are not retroactively converted to failures.

```text
HISTORICAL_PASS != CURRENT_OPERATIONAL_ACCEPTANCE
RETROACTIVE_PASS = NO
RETROACTIVE_ERASURE = NO
```

## 3. Boundary classification

### UNIVERSAL

The following are reusable SES rules:

- consultation must identify the intended project, specialist and task explicitly;
- for any SES archetype selected for consultation, the human-facing operational target name must be resolved from `archetypes/REGISTRY.md` `CANONICAL_NAME`; project-local or legacy aliases are continuity only and must not replace the canonical target identity;
- the handoff must preserve provenance and authority boundaries;
- the receiving specialist must resolve material live state itself before substantive current-state claims;
- a copied SHA or state snapshot is an anchor, not proof that it remains current;
- consultation does not imply project adoption;
- adoption does not imply execution;
- execution does not imply mutation authority;
- tool availability does not imply tool execution;
- the specialist result returns to SES for adjudication rather than becoming automatically authoritative;
- secrets must never be embedded in a handoff packet.

### PROJECT-LOCAL

The consumer project remains authoritative for:

- project truth and live state;
- canonical repository/source;
- bootstrap and continuity;
- authority and mutation permissions;
- environments;
- project-local specialist rules and overrides;
- explicit role adoption.

### SPECIALIST-SPECIFIC

The selected specialist/archetype remains authoritative for its domain method, specialist-specific proof obligations, failure modes and tool/evidence requirements, subject to project-local boundaries.

## 4. Consultation versus adoption

SES must keep these states separate:

```text
CONSULTED != ADOPTED
ADOPTED != EXECUTED
EXECUTED != AUTHORIZED_TO_MUTATE
CERTIFIED_FOR_ANY_PROJECT != CONSUMER_PROJECT_ADOPTED
```

A specialist may be consulted in either of two valid modes:

### A. Adopted-role consultation

The project adapter contains an exact adopted role mapping:

```text
ROLE -> ARCHETYPE_ID
ADOPTION_STATUS: ADOPTED
```

The handoff may identify that specialist as the canonical adopted specialist for that role, subject to current certification eligibility and project-local rules.

### B. Explicit ad-hoc consultation

A user may explicitly request consultation with a certified SES specialist that the project has not adopted. SES may generate the handoff, but must label it:

```text
SELECTION_STATUS = EXPLICIT_AD_HOC_CONSULTATION
PROJECT_ROLE_ADOPTION = NO
```

The consultation must not be described as the project's canonical role assignment and must not silently create an adoption mapping.

SES may recommend a specialist, but recommendation alone does not authorize adoption or execution. If a material ambiguity exists between plausible specialists, resolve it before claiming a selected specialist.

## 5. Preconditions

Before emitting a project-specific handoff packet, SES must resolve or explicitly classify:

1. `SES_EFFECTIVE_REF`;
2. explicit `PROJECT_IDENTIFIER`;
3. unique Project Registry record and Project Adapter;
4. canonical consumer-project source;
5. project bootstrap entrypoint;
6. task scope;
7. selected specialist/archetype and selection basis;
8. applicable project-local specialist mapping/rules when material;
9. authority sources when mutation, lifecycle or risk acceptance is material.

Fail closed when a required item is unresolved.

Do not use fuzzy project or role guessing for a material handoff.

Before rendering any instruction such as "send to", "paste into", "consult", "open the specialist" or equivalent, resolve the selected `ARCHETYPE_ID` in `archetypes/REGISTRY.md` and obtain its exact `CANONICAL_NAME`.

For an SES-selected specialist:

```text
SPECIALIST_TARGET_NAME = ARCHETYPE_REGISTRY.CANONICAL_NAME
LEGACY_ALIAS != SPECIALIST_TARGET_NAME
PROJECT_LOCAL_SKILL_TITLE != SPECIALIST_TARGET_NAME
BUILDER_HISTORY_LABEL != SPECIALIST_TARGET_NAME
```

A project-local identity may be the operational target only when no SES archetype is selected for that consultation, for example an unmapped project-local role or explicitly project-local specialist with no adopted/certified SES replacement. Do not fabricate an SES identity for such a case.


## 5.1 Consumer consultation admission versus SES release lifecycle

A consumer project must not hijack its own task/lifecycle to close an internal SES candidate-release certification gap unless the consumer task explicitly requires that exact candidate fingerprint as a certification precondition.

For ordinary manual consultation of an adopted SES role, admission is based on:

```text
PROJECT ROLE = ADOPTED
+ ARCHETYPE = ACTIVE
+ CURRENT SES LEDGER CERTIFICATION = YES
→ CONSULTATION ELIGIBLE
```

The consumer project must not scan unrelated SES candidate kernels/packages and convert their existence, application history or pending proportional certification into a project blocker.

```text
CERTIFIED ARCHETYPE EXISTS
+ UNPUBLISHED / NONCURRENT SES CANDIDATE EXISTS
!= CONSUMER PROJECT BLOCKED
```

If the external Custom GPT currently carries a runtime delta that is not the current certified SES release, its output may still be consumed as bounded specialist evidence under the normal result-packet/adjudication rules, provided the output truthfully records the evidence/tool boundary. That runtime delta must not be represented as universally certified merely because it was used.

```text
SPECIALIST_OUTPUT_USABLE_AS_BOUNDED_EVIDENCE
!= EXACT_RUNTIME_CERTIFIED_FOR_ANY_PROJECT
```

An exact runtime fingerprint becomes a consumer admission blocker only when at least one of these is true:

1. the consumer project's own authority explicitly requires a certified exact runtime/fingerprint for the task;
2. the task's proof obligation materially depends on a runtime capability whose use is allowed only by a certified exact-runtime contract;
3. the handoff explicitly selects a particular SES release/fingerprint rather than the archetype generally.

Otherwise, the consumer project continues its own lifecycle and SES release closure remains an SES lifecycle concern.

For project-local tool bindings, distinguish:

```text
PROJECT_LOCAL_TOOL_CONTRACT
+ ACTUAL TOOL INVOCATION / VERIFIED RESULT
→ PROJECT-LOCAL EVIDENCE CHANNEL

PROJECT_LOCAL_TOOL_PROOF
!= UNIVERSAL SES RUNTIME CERTIFICATION

UNIVERSAL RUNTIME CERTIFICATION GAP
!= PROJECT-LOCAL TOOL UNUSABLE
```

This rule does not weaken tool honesty, result provenance, project authority, risk acceptance or certification semantics. It only prevents consumer projects from inserting an unrelated SES release-certification workflow into their own next-safe-action chain.

## 6. Specialist Consultation Packet

The packet is the minimum transport object from SES to the receiving specialist.

Use this schema semantically; formatting may vary without removing required meaning.

```text
SES SPECIALIST CONSULTATION PACKET

PACKET_VERSION: manual-specialist-handoff-v0.3
PROJECT_IDENTIFIER: <explicit project id/name>
PROJECT_CANONICAL_NAME: <resolved canonical project name>
CANONICAL_SOURCE: <project-owned canonical source>
SES_EFFECTIVE_REF: <exact SES ref used to prepare packet>
PROJECT_REF_RULE: <how receiving specialist must resolve current project ref>

SPECIALIST_ARCHETYPE_ID: <resolved archetype id>
SPECIALIST_CANONICAL_NAME: <exact CANONICAL_NAME from archetypes/REGISTRY.md>
SPECIALIST_TARGET_NAME: <must equal SPECIALIST_CANONICAL_NAME for SES-selected specialist>
SES_CERTIFICATION_STATUS: <current ledger state for selected archetype>
SES_CERTIFIED_SUBJECT: <current certified subject/fingerprint when material>
CONSUMER_RUNTIME_VARIANT_STATUS: <NOT_REQUIRED | CURRENT_CERTIFIED_SUBJECT | NONCURRENT_VARIANT_BOUNDED_EVIDENCE>
LEGACY_ALIASES: <continuity/history aliases or NONE>
SPECIALIST_RUNTIME_NAME: <optional external Builder display name; informational only and never routing authority>
SELECTION_STATUS: <ADOPTED_ROLE | EXPLICIT_AD_HOC_CONSULTATION>
PROJECT_ROLE: <exact adopted role or NOT_ADOPTED_FOR_THIS_CONSULTATION>

TASK_SCOPE: <complete bounded request>
TARGET_REF_OR_OBJECT: <explicit target or NOT_REQUIRED_FOR_THIS_TASK>
ENVIRONMENT: <explicit environment or NOT_REQUIRED_FOR_THIS_TASK>

BOOTSTRAP_ENTRYPOINT: <project-owned path>
CONTINUITY_ENTRYPOINT: <project-owned path when applicable>
AUTHORITY_ENTRYPOINT: <project-owned path(s) when applicable>
PROJECT_LOCAL_SPECIALIST_RULES: <resolved pointer or NONE_DECLARED>

MUTATION_AUTHORIZATION: <AUTHORIZED_EXACT_SCOPE | NOT_AUTHORIZED>

REQUIRED_EXECUTION_RULES:
- resolve material live state before substantive current-state claims;
- follow project bootstrap and project-local authority;
- distinguish FACT / EVIDENCE / ASSUMPTION / INFERENCE / PREFERENCE / UNKNOWN / MISSING_EVIDENCE;
- do not claim a tool or Action was executed unless it was actually executed;
- do not treat packet state as a substitute for live verification when freshness is material;
- do not expand scope or mutation authority;
- return a Specialist Result Packet.
```

The packet may include task-specific evidence pointers, acceptance criteria or proof obligations, but must not include secrets.

### 6.1 Canonical target rendering rule

When the handoff is rendered for a human, all operational destination language must use `SPECIALIST_TARGET_NAME`.

Allowed example:

```text
Send this packet to: SES — Software Systems Architect
```

Disallowed when `software-systems-architect` is the selected SES archetype:

```text
Send this packet to: GPT1.5 — FECH.AI Arquiteto SaaS
```

A legacy or project-local label may appear only as explicitly labeled continuity/context, never as the destination identity.

```text
CANONICAL_TARGET_IDENTITY = UNIVERSAL
PROJECT_LOCAL_RULES = PROJECT_LOCAL
LEGACY_CONTINUITY = HISTORICAL / PROJECT_LOCAL
TRANSPORT = MANUAL_COPY_PASTE
```

## 7. Freshness and provenance

The receiving specialist must not treat the handoff packet as a frozen mirror of live project state.

If current state is material:

```text
PACKET_ANCHOR
-> RESOLVE LIVE SOURCE
-> RECORD RESOLVED REF
-> READ REQUIRED SOURCES
-> CONTEXT READINESS
-> SUBSTANTIVE WORK
```

If the specialist cannot access a required live source, it must declare the limitation rather than simulate verification.

```text
ABSENCE_OF_FINDING != PROOF_OF_ABSENCE
UNAVAILABLE_TOOL != EXECUTED_TOOL
COPIED_CONTEXT != LIVE_EVIDENCE
```

## 8. Mutation authority

Manual transport creates no authority.

Default:

```text
MUTATION_AUTHORIZATION = NOT_AUTHORIZED
```

A mutation may be included only when the consumer project's applicable authority explicitly authorizes the exact scope. The packet must state that authorization explicitly. A general request for analysis, review, design or consultation is not mutation authority.

The receiving specialist must preserve:

```text
TOOL_CAPABILITY != AUTHORIZATION
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
GENERATE != AUTHORIZE != PUBLISH
```

## 9. Specialist Result Packet

The specialist should return a bounded result suitable for SES adjudication:

```text
SES SPECIALIST RESULT PACKET

SPECIALIST_ARCHETYPE_ID: <id>
SELECTION_STATUS: <value from consultation packet>
PROJECT_IDENTIFIER: <project>
TASK_SCOPE: <effective task scope>
RESOLVED_PROJECT_REF: <exact ref or NOT_RESOLVED>
RESOLVED_SES_REF: <exact ref when actually resolved, otherwise NOT_RESOLVED>

CONTEXT_STATUS: <READY | LIMITED | BLOCKED>
EFFECTIVE_SCOPE: <scope actually completed>
GAPS: <material gaps>

FINDINGS: <bounded findings>
EVIDENCE: <provenance/pointers>
ASSUMPTIONS: <explicit assumptions>
INFERENCES: <explicit inferences>
UNKNOWNS: <unknowns / missing evidence>
BLOCKERS: <blockers>
RECOMMENDATIONS: <recommendations, not automatic decisions>

TOOLS_ACTUALLY_EXECUTED: <operations actually invoked>
MUTATIONS_EXECUTED: <none or exact authorized mutations>
AUTHORITY_STATUS: <what was and was not authorized>
```

A free-form specialist answer may still be consumed, but SES must not invent missing proof fields from silence.

## 10. Return and adjudication

When the result is copied back to SES:

1. identify the consultation packet/task it belongs to;
2. preserve the specialist's claimed evidence boundary;
3. distinguish specialist findings from SES adjudication;
4. verify material claims independently when the SES decision requires it and tools/evidence are available;
5. identify contradictions, missing evidence and authority gaps;
6. decide the next step without silently converting a recommendation into project authorization.

```text
SPECIALIST_OUTPUT != SES_APPROVAL
SPECIALIST_RECOMMENDATION != PROJECT_DECISION
SPECIALIST_RESULT != MUTATION_AUTHORIZATION
```

## 11. Router/Gateway relationship

The Runtime Enforcement Gateway and `SES — Specialist Router` remain versioned historical/runtime-candidate assets. They are not deleted by this contract.

While they are not the accepted operational path:

- SES must not require a live Gateway receipt to prepare a manual consultation packet;
- SES must not claim `routeSpecialistRole` was invoked when it was not;
- a historical `ROUTABLE` proof does not substitute for current project/specialist resolution;
- manual handoff must use Registry, Adapter, archetype/certification and project-owned sources directly;
- no fallback from an unavailable Gateway may silently alter role or specialist selection.

A future Router/Gateway re-adoption requires a material decision and new operational proof that the end-to-end workflow is usable in the intended ChatGPT project/runtime context.

## 12. Acceptance criteria

This contract is acceptable only if behavioral validation demonstrates at minimum:

- exact project resolution;
- adopted-role versus ad-hoc consultation distinction;
- no automatic adoption;
- live-state re-resolution requirement;
- mutation fail-closed behavior;
- tool-call honesty;
- secret exclusion;
- specialist result return/adjudication boundary;
- Gateway/Router not required for the current manual path;
- historical Gateway proof preserved without being presented as current operational acceptance;
- canonical target identity resolved from the Archetype Registry;
- legacy/project-local aliases never emitted as operational destinations for SES-selected specialists;
- same archetype renders the same canonical target name across consumer projects while project-local rules remain different;
- unmapped project-local roles remain project-local and are not forcibly renamed to SES.

## 13. Cross-project consistency

The canonical specialist identity is SES-wide, not consumer-project-specific.

For the same selected `ARCHETYPE_ID`, different projects may supply different bootstrap, authority and project-local rules, but the operational target name remains the same canonical SES identity.

```text
SAME ARCHETYPE_ID
+ DIFFERENT PROJECT_CONTEXT
→ SAME SPECIALIST_TARGET_NAME
→ DIFFERENT PROJECT_LOCAL_RULES MAY APPLY
```

This rule does not mean every certified specialist is automatically adopted by every project. Availability/certification, project adoption and ad-hoc consultation remain separate states.

```text
CERTIFIED_FOR_ANY_PROJECT != CONSUMER_PROJECT_ADOPTED
CANONICAL_IDENTITY != AUTOMATIC_ADOPTION
```

## 14. Invalidation

Revisit this contract when a material transport capability changes, including:

- reliable native specialist-to-specialist composition becomes available;
- Router/Gateway end-to-end usability is re-proven and explicitly re-adopted;
- project/adoption semantics change;
- specialist runtime boundaries change materially.

A new transport does not automatically supersede this one.

```text
CENTRAL_EVOLUTION != AUTOMATIC_PROJECT_MUTATION
NEW_TRANSPORT_AVAILABLE != NEW_TRANSPORT_ADOPTED
```