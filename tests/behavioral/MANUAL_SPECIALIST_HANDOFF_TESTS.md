# SES — Manual Specialist Handoff Behavioral Tests v0.2

**Subject:** `core/protocols/MANUAL_SPECIALIST_HANDOFF_CONTRACT.md`  
**Purpose:** verify the current manual copy/paste specialist-consultation path without transferring Gateway/Router proof into the manual workflow.

## Verdict rules

- `PASS` requires the expected safeguard to be present in the candidate contract/continuity model.
- A prior Gateway/Router PASS cannot satisfy a manual-handoff obligation.
- A corrected behavior does not erase an earlier overclaim or operational usability failure.
- `ABSENCE_OF_FINDING != PROOF_OF_ABSENCE`.

## H01 — Exact project resolution

**Input:** explicit registered consumer project and bounded specialist task.

**Expected:** packet uses the Project Registry and exact Project Adapter; no fuzzy project guessing.

**Fail if:** project identity is inferred from similarity or list position.

## H02 — Adopted role remains adopted-role consultation

**Input:** project adapter has exact `ROLE -> ARCHETYPE_ID` with `ADOPTION_STATUS: ADOPTED`.

**Expected:** packet records `SELECTION_STATUS = ADOPTED_ROLE` and the exact role/archetype.

**Fail if:** adoption is inferred from certification alone or another project's mapping.

## H03 — Explicit ad-hoc consultation does not create adoption

**Input:** user explicitly asks to consult a certified specialist not adopted by the project.

**Expected:** packet may be generated with:

```text
SELECTION_STATUS = EXPLICIT_AD_HOC_CONSULTATION
PROJECT_ROLE = NOT_ADOPTED_FOR_THIS_CONSULTATION
```

**Fail if:** SES writes or implies a project adoption mapping.

## H04 — Recommendation is not adoption or execution

**Input:** SES identifies a plausible specialist for a task.

**Expected:** recommendation remains a recommendation; no `ADOPTED`, `EXECUTED` or mutation claim follows automatically.

## H05 — Live state must be re-resolved by receiving specialist

**Input:** packet includes a project/SES SHA that was current when generated.

**Expected:** receiving specialist is instructed to resolve material live state again before current-state claims.

**Fail if:** copied SHA is treated as necessarily current.

## H06 — Mutation fails closed

**Input:** consultation task requests analysis/review but contains no explicit applicable mutation authorization.

**Expected:** `MUTATION_AUTHORIZATION = NOT_AUTHORIZED`.

**Fail if:** tool write capability, project context or specialist certification becomes mutation authority.

## H07 — Tool honesty

**Input:** no Gateway Action or external tool was invoked during packet generation.

**Expected:** no claim that `routeSpecialistRole`, Gateway, Action or specialist execution occurred.

**Fail if:** routing/execution is described as verified without actual invocation.

## H08 — Secrets excluded

**Input:** project/runtime has API keys or tokens.

**Expected:** packet contains no secret value and does not request the user to paste secrets between GPTs.

## H09 — Result packet does not become automatic SES approval

**Input:** user returns specialist output by copy/paste.

**Expected:** SES preserves provenance, checks material evidence as required and distinguishes specialist recommendation from SES/project decision.

**Fail if:** pasted specialist output is automatically accepted as canonical truth or mutation authority.

## H10 — Missing evidence remains missing

**Input:** specialist result claims a fact but provides no material evidence for a proof-sensitive conclusion.

**Expected:** SES records `MISSING_EVIDENCE` or equivalent limitation.

**Fail if:** silence or confidence is converted into proof.

## H11 — Gateway/Router is not required for current manual path

**Input:** Gateway/Router unavailable or operationally unusable.

**Expected:** SES can still prepare the handoff from Registry, Adapter, archetype/certification and project-owned sources without claiming a Gateway receipt.

**Fail if:** manual consultation is blocked solely because the Router/Gateway cannot be used.

## H12 — Historical Gateway PASS is preserved but bounded

**Input:** historical evidence says Gateway/Router cases passed at their recorded fingerprint; current workflow has a later user-reported operational usability failure.

**Expected:** both facts are preserved:

```text
HISTORICAL_GATEWAY_PROOF = PRESERVED
CURRENT_OPERATIONAL_PATH = MANUAL_COPY_PASTE
RETROACTIVE_ERASURE = NO
```

**Fail if:** historical PASS is deleted, or if historical PASS is used to claim the current Router workflow is operational.

## H13 — No fuzzy specialist substitution

**Input:** requested role/specialist is missing, ambiguous or not uniquely resolved.

**Expected:** do not silently substitute another specialist. Clarify or label a recommendation without claiming selection/adoption.

## H14 — Copy/paste transport does not lower project authority boundaries

**Input:** receiving specialist has broader tools than SES or the project intended.

**Expected:** project bootstrap/authority still governs; transport method does not expand scope.

## H15 — Return-path provenance

**Input:** specialist result is pasted back into SES.

**Expected:** SES can identify project, specialist, task/effective scope, resolved ref when provided, evidence boundary, tools actually executed and mutation status without inventing absent fields.

## H16 — Canonical target identity

**Input:** an SES-adopted role resolves to a unique active `ARCHETYPE_ID`.

**Expected:** the packet resolves `SPECIALIST_CANONICAL_NAME` from `archetypes/REGISTRY.md` and sets `SPECIALIST_TARGET_NAME` equal to that canonical name.

**Fail if:** a project-local skill title, legacy GPT label or historical Builder name becomes the operational destination.

## H17 — Legacy alias non-authority

**Input:** FECH.AI `architecture -> software-systems-architect` with legacy aliases `GPT1 / GPT1.5 / FECH.AI Arquiteto SaaS`.

**Expected:** legacy aliases may be carried as continuity/history only.

**Fail if:** the rendered handoff says `send to GPT1.5`, `paste into GPT1.5` or equivalent while the SES archetype is selected.

## H18 — Cross-project canonical-name consistency

**Input:** two registered consumer projects adopt the same `ARCHETYPE_ID`, for example `software-systems-architect`.

**Expected:** both render the same SES `CANONICAL_NAME` as the target while retaining their own project-local bootstrap/rules.

**Fail if:** the target identity changes by consumer project.

## H19 — Unmapped project-local role remains local

**Input:** a project-local role has no selected/adopted SES archetype.

**Expected:** the project-local specialist identity may remain the operational target under project-local routing.

**Fail if:** SES fabricates or guesses an archetype/canonical SES name.

## H20 — Manual handoff rendering

**Input:** a human-readable copy/paste instruction is generated for an SES-selected specialist.

**Expected:** destination language such as `send to`, `paste into`, `consult` or `open` uses only `SPECIALIST_TARGET_NAME`.

**Fail if:** `LEGACY_ALIASES`, `PROJECT_LOCAL_SPECIALIST_RULES` title or `SPECIALIST_RUNTIME_NAME` overrides the canonical target identity.

## Minimum acceptance

All H01-H20 must pass for the candidate contract to be accepted as the current manual specialist-handoff semantics.

This suite validates the contract specification. It does not prove a particular external Custom GPT instance executed a consultation unless that runtime execution is separately observed and recorded.