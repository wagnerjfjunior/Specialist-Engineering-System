# SES — AppSec L1-C A05 Evidence v0.1

**Fixture:** `A05 — Supabase privileged-key exposure`  
**Candidate:** `application-security-assurance-specialist-v0.1`  
**Kernel blob SHA:** `c1a0a6e66278b0bc94ef3280aff635a42faf9332`  
**Packet:** `tests/behavioral/execution-packets/APPSEC_L1C_A05_EXACT_PACKET_V0_1.md`

## Provenance

- Execution occurred in a separate ChatGPT conversation according to user-supplied screenshot evidence.
- User supplied the resulting first-response transcript as an attached Markdown artifact.
- The screenshot demonstrates a separate conversation and visible use of the AppSec L1-C kernel.
- The returned Markdown artifact is transport-escaped in this adjudication context, so no claim is made that this context possesses a byte-identical UI raw-input capture.
- No follow-up/correction evidence was supplied before the captured response.

## Behavioral adjudication

Expected critical behavior from canonical runbook:
- treat client-side `service_role`/secret as critical privileged-secret exposure;
- reject minification/obfuscation as a security control;
- require removal, rotation/revocation, impact analysis and trusted confinement.

Observed first response:
- classified privileged secret in client bundle as critical exposure;
- explicitly rejected minification/obfuscation as protection;
- treated the delivered secret as compromised;
- required client removal, rotation/deactivation, impact analysis and server-side confinement;
- distinguished publishable/anon client keys from privileged service-role/secret keys;
- bounded unknown blast radius as `NOT_DETERMINED`;
- produced remediation and retest proof obligations.

### Meta-label note

The executor wrote `A05 = FAIL canônico`. That label describes the security state in the fixture, not the behavioral-test result. Executor self-adjudication is not authoritative.

## Result

```text
P08 Secret/privileged-key exposure detection = PASS
P15 Finding quality = PASS
A05 BEHAVIORAL RESULT = PASS
RAW_UI_INPUT_HASH = NOT_CAPTURED
RAW_UI_OUTPUT_HASH = NOT_CAPTURED
CANONICAL PACKET BYTE-FIDELITY IN ADJUDICATION CONTEXT = NOT_PROVEN
```

No retroactive result is created. This evidence event remains bounded to the supplied screenshot/transcript provenance.