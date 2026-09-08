# SES — Specialist Consultation Transport Contract v0.1

**Contract ID:** specialist-consultation-transport-contract-v0.1
**Status:** CANONICAL_V0_1 / DUAL_TRANSPORT

## Decision

SES supports two valid specialist consultation transports in ChatGPT:

- PREFERRED_CHATGPT_SPECIALIST_TRANSPORT = PROJECT_LEVEL_@
- SUPPORTED_FALLBACK_TRANSPORT = MANUAL_COPY_PASTE

PREFERRED != EXCLUSIVE.
FALLBACK != DEPRECATED.
NEW_TRANSPORT_ADOPTED != OLD_TRANSPORT_INVALIDATED.

## Project-level @

When the intended SES specialist is visibly available in the ChatGPT Project mention UI, project-level @ is the preferred path.

Operationally:
PROJECT CHAT -> explicit @ target specialist -> bounded specialist work -> result remains in project chat.

Current evidence supports this path for Software Systems Architect portable v0.3 and Documentation Auditor portable v1.3. This is operational evidence for the observed runtime, not a universal platform guarantee.

## Action-dependent turns

For Action-dependent work:
ACTION-DEPENDENT SPECIALIST TURN -> EXPLICIT @ MENTION IN THAT TURN.

Do not assume Action availability persists from a prior turn. If the Action is not exposed after re-mention, do not invent execution; use the supported manual fallback when appropriate.

## Manual copy/paste

The existing Manual Specialist Handoff Contract remains fully supported and canonical as fallback/portability/recovery transport.

Manual transport is appropriate when @ is unavailable, unstable, not preferred by the user, unsupported by the target runtime, or when an evidence-preserving fallback is needed.

## Authority

Transport does not change authority:
@ MENTION != PROJECT ADOPTION
MANUAL HANDOFF != PROJECT ADOPTION
CONSULTED != ADOPTED
ADOPTED != EXECUTED
EXECUTED != AUTHORIZED_TO_MUTATE
TOOL CAPABILITY != AUTHORIZATION
SPECIALIST OUTPUT != SES APPROVAL

## Identity

For @ transport, the exact intended specialist must be visibly selected. If identity/package differs materially from the intended specialist, classify the turn as invalid for that specialist rather than as a specialist failure.

## Evidence boundary

Two independent specialists currently support these probable shared principle candidates:
1. ACTION-DEPENDENT TURN -> EXPLICIT @ MENTION IN THAT TURN.
2. PROJECT-LEVEL @ can transport specialist cognition without material degradation for the observed specialists/runtime.

These are not UNIVERSAL PRINCIPLES.

## Failure and fallback

TRANSPORT FAILURE != SPECIALIST CERTIFICATION FAILURE.

Preserve failed/invalid transport evidence. A successful manual fallback must not rewrite the failed transport turn as PASS.

## Certification

Dual-transport adoption changes no specialist kernel, Builder Instructions or certified fingerprint.

TRANSPORT CONTRACT CHANGE + NO SPECIALIST FINGERPRINT CHANGE -> NO SPECIALIST RECERTIFICATION.

## Current operational state

CURRENT_SPECIALIST_TRANSPORT_MODE = DUAL
PREFERRED_CHATGPT_SPECIALIST_TRANSPORT = PROJECT_LEVEL_@
SUPPORTED_FALLBACK_TRANSPORT = MANUAL_COPY_PASTE
SPECIALIST_ROUTER_CURRENT_STATUS = NOT_CURRENT_OPERATIONAL_PATH
RUNTIME_ENFORCEMENT_GATEWAY_CURRENT_STATUS = NOT_CURRENT_OPERATIONAL_PATH_FOR_SPECIALIST_CONSULTATION

## Adoption boundary

This decision changes SES operational guidance only. It does not automatically mutate consumer projects, Project Adapters, specialist adoption mappings, Builders, Actions, certification ledgers or production.

## Invalidation

Revisit this contract if @ behavior, Action exposure, specialist composition, runtime boundaries or superior transport capabilities change materially.

PREFERRED TRANSPORT != ONLY TRANSPORT.
CENTRAL EVOLUTION != AUTOMATIC PROJECT MUTATION.