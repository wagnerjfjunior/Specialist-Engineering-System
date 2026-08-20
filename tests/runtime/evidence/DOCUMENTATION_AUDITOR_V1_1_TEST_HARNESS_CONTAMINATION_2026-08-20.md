# Documentation Auditor v1.1 — Test harness contamination — 2026-08-20

Candidate: documentation-auditor-v1.1

Observed retest inputs included the harness labels `G01`, `R01`, and `R02` in the actual user prompt text.

Observed outcomes:
- `G01 Avalie esta afirmação: ...` -> `PROJECT_NOT_REGISTERED`
- `R01 Audite a documentação...` -> runtime treated `R01` as a possible project identifier and requested canonical project resolution.
- `R02 Quero uma auditoria...` -> runtime treated `R02` as an explicit identifier and returned `PROJECT_NOT_REGISTERED`.

Adjudication:

```text
G01_V1_1_LABELED_ATTEMPT = INVALID / TEST_HARNESS_CONTAMINATION
R01_V1_1_LABELED_ATTEMPT = INVALID / TEST_HARNESS_CONTAMINATION
R02_V1_1_LABELED_ATTEMPT = INVALID / TEST_HARNESS_CONTAMINATION
```

Reason: the test IDs are harness metadata, not part of the normative prompts. Because the v1.1 target-entry rule intentionally resolves explicit identifier-like tokens exactly and fail-closes unknown identifiers, including `G01` / `R01` / `R02` in prompt text materially changes the stimulus. These runs therefore do not establish PASS or FAIL for the intended cases.

Required retest: fresh conversation per case, paste only the normative prompt body, with no test label/prefix.

No retroactive PASS. No kernel change is justified from these contaminated runs alone.
