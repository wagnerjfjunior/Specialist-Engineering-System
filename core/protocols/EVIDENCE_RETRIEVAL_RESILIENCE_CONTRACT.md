# SES — Evidence Retrieval Resilience Contract

**Status:** FOUNDATION_V0_1 / CORE_PROTOCOL

## 1. Purpose

Define reusable fail-closed retrieval behavior for large files, large repository trees and context-budget pressure across SES specialists.

This is a SES Core protocol. It defines retrieval/coverage resilience primitives only. Archetypes decide how to apply them to domain work; consumer projects remain authoritative for project truth and local evidence rules.

## 2. Core invariants

```text
OBJECT_EXISTS != OBJECT_RETRIEVED != OBJECT_COMPLETELY_READ
TREE_RETURNED != TREE_COMPLETELY_ENUMERATED
SEARCH_EMPTY != ABSENCE_PROVED
TOOL_FAILURE != NEGATIVE_EVIDENCE
```

Never promote incomplete transport into complete evidence.

## 3. Progressive disclosure

For material tasks, prefer:

```text
TASK
→ CLAIMS
→ PROOF OBLIGATIONS
→ MATERIAL SURFACES
→ TARGETED TREE WALK
→ TARGETED FILES
→ CHUNKED / MANUAL FALLBACK ONLY WHEN REQUIRED
```

Do not ingest an entire repository by default. Retrieve the minimum evidence necessary to prove or refute the bounded claim while preserving provenance.

## 4. Large-file contingency

When a material file may exceed tool/runtime output limits:

1. resolve repository, exact ref and path;
2. capture blob/object identity and size when available;
3. attempt the normal exact-ref final-file reader;
4. classify the result by content actually recovered:
   - if the reader fails before returning any file content, preserve `NOT_READ` and record the retrieval/tool failure explicitly;
   - if some file content is recovered but the response truncates, omits a material suffix, or cannot prove EOF, classify `PARTIAL_READ`;
5. do not retry the same oversized operation indefinitely;
6. use a deterministic bounded-chunk mechanism when the configured tool surface supports one;
7. maintain a coverage ledger for every chunk/range actually retrieved;
8. detect gaps and overlaps explicitly;
9. only promote to `INTEGRAL_READ` when coverage proves start-through-EOF with no material gap;
10. if complete reading remains material after either a zero-content failure or a partial read, continue through the best actually available bounded/alternate retrieval path; if no technical chunk mechanism is available, state `CHUNKED_READ_UNAVAILABLE` and request an approved alternate source/manual attachment rather than stopping at the coverage classification alone.

`ZERO_CONTENT_FAILURE = NOT_READ + TOOL/RETRIEVAL_FAILURE`

`SOME_CONTENT_WITHOUT_EOF = PARTIAL_READ`

Coverage classification and fallback state are independent dimensions:

```text
COVERAGE_STATE
=
NOT_READ + TOOL/RETRIEVAL_FAILURE
OR
PARTIAL_READ

IF COMPLETE_READING_IS_MATERIAL
AND NO_CONFIGURED_BOUNDED_READER_IS_AVAILABLE
THEN
CHUNKED_READ_UNAVAILABLE
+
MANUAL_OR_ALTERNATE_SOURCE_REQUIRED
```

Conceptual coverage record:

```text
FILE_PATH
EXACT_REF
BLOB_OR_OBJECT_ID
CHUNK_ID
RANGE_START
RANGE_END
RETRIEVAL_METHOD
RESULT
GAP_BEFORE
GAP_AFTER
EOF_PROOF
```

Chunk sizes are implementation details and must not be hard-coded as universal evidence semantics.

## 5. Manual-file fallback

A user-supplied attachment may be used as an alternate source when live retrieval cannot technically recover a required large file, but it must be classified separately from independently retrieved canonical live content.

Minimum rules:

- preserve supplied filename and provenance;
- bind to a canonical ref/blob only if independently cross-checked;
- otherwise state `SUPPLIED_ARTIFACT / LIVE_EQUIVALENCE_NOT_ESTABLISHED`;
- do not silently treat a supplied copy as current live main;
- if the user supplies the exact live artifact and identity can be cross-checked, record the cross-check method.

## 6. Large-tree contingency

A recursive tree response is complete only when the tool/source explicitly establishes that it is not truncated and the relevant universe is covered.

If recursive tree retrieval returns `truncated=true`, fails, or exceeds the runtime output budget:

```text
RECURSIVE_TREE_RESULT = PARTIAL_TREE
→ SWITCH TO DIRECTORY_WALK
```

Directory-walk protocol:

1. fetch the root tree non-recursively;
2. record child blob/tree entries and child tree SHAs;
3. fetch required child trees non-recursively;
4. recurse directory-by-directory only across task-relevant subtrees;
5. maintain `VISITED_TREE_SHA[]` and `ENUMERATED_PATHS[]`;
6. detect inaccessible/missing subtrees;
7. declare full bounded-tree coverage only when every material subtree in the declared universe was traversed.

A truncated recursive response must never support `COMPLETE_REPOSITORY_ENUMERATION`.

## 7. Context-budget resilience

When returned evidence is too large for one response/context window:

- preserve exact refs/object IDs before summarization;
- summarize already-read material without upgrading coverage;
- continue retrieval incrementally;
- keep claim-to-evidence mapping stable across batches;
- avoid re-fetching unchanged evidence without cause;
- prefer narrow files/subtrees/callers relevant to the active proof obligation;
- if context budget prevents a complete required proof, state the remaining gap rather than synthesizing PASS.

## 8. Coverage union

Multiple partial reads may prove complete reading only when their union demonstrably covers the complete target.

```text
PARTIAL_READ + PARTIAL_READ + ...
!= INTEGRAL_READ
```

unless:

```text
UNION_OF_RANGES = START..EOF
AND NO_MATERIAL_GAP
AND TARGET_IDENTITY_STABLE
```

If target ref/blob changes between chunks, prior chunks cannot be silently combined with the new object.

## 9. Tool-claim integrity

State the mechanism actually used:

- path reader;
- raw blob reader;
- tree reader;
- directory walk;
- search;
- supplied attachment;
- bounded chunk loader when actually available.

Do not claim a chunk loader exists merely because the desired protocol specifies one.

## 10. Current GitHub Action limitation

The current SES GitHub READ_ONLY Action provides exact-ref file/blob/tree readers but does not define a dedicated server-side line-range/chunk operation.

Therefore, when a file exceeds the runtime's safe single-response capacity and no other configured bounded reader is available, first preserve the actual coverage outcome:

```text
COVERAGE_STATE =
  NOT_READ + TOOL/RETRIEVAL_FAILURE
  OR
  PARTIAL_READ
```

Then, for **either** coverage outcome, if complete reading is material:

```text
CHUNKED_READ_UNAVAILABLE
+
MANUAL_OR_ALTERNATE_SOURCE_REQUIRED
```

Do not attach fallback obligations only to `PARTIAL_READ`; a zero-content failure requires the same fail-closed continuation when the proof obligation still requires the complete file.

A future bounded read operation may be added only through a separately versioned Action/runtime change with its own safety and behavioral evidence.

## 11. Invalidation

Material target identity changes invalidate unfinished coverage unions:

- ref/head change;
- blob/object ID change;
- project switch;
- source replacement;
- retrieval-method change that alters evidence semantics.

Revalidate proportionally; do not restart unrelated evidence work.

## 12. Relationship to archetypes

This protocol is reusable SES Core infrastructure.

`Documentation Auditor` must apply it rigorously for evidence claims. `SaaS Architect`, future security, CI/CD and other archetypes may use the same primitives when their work depends on large files/trees or bounded completeness.
