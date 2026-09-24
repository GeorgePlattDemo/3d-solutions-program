# Migration findings and work queue

Snapshot: September 24, 2026. No source repository has been deleted, archived, or made public by this pass.

## What has been examined

The complete default-branch file trees of Grok, Staging and Governed Reference were compared by Git blob identity with System. All listed branches of those three donors were inventoried; non-main branch trees were also compared. Readmes and the selected Review research document were read for their role and scope. This is not a claim that all source bodies have been read or semantically adjudicated.

| Donor main | Files | Exact copies found in System | Branches listed |
| --- | ---: | ---: | ---: |
| grok-file | 13 | 5 | 9 |
| scan-to-build-transfer-staging | 239 | 12 | 1 |
| scan-to-build-governed-reference | 233 | 39 | 4 |

Staging also contains 45 file entries whose blobs occur in Governed Reference. These counts overlap; they are not totals of unique migration savings. A missing blob match can mean revised content, not necessarily missing content.

The [machine-readable inventory](source-inventory.json) records 485 default-branch file entries and 186 non-main-branch entries with content not present in that donor's main. It records source identities and exact System matches. Proposed owner buckets are triage suggestions, not accepted migrations. Source bodies and conversation transcripts are not copied into this ledger.

## First admitted research document

The current public Review bounded-cell trial document is staged at [research/bounded-cell-trial.md](../research/bounded-cell-trial.md). Its substantive text is preserved, including the added economic acceptance section. Only the companion-document link is adjusted to work from its new location. Source identity is in [admissions.json](admissions.json).

Review's existing copy remains in place during this transition. A follow-up relocation change should preserve its old address with a concise pointer once the Program destination is accepted. Do not leave two independently edited authoritative copies.

## Grok reconciliation candidate

The [Grok report](grok-reconciliation.md) and [per-item register](grok-reconciliation.json) now reconcile all nine observed branch heads. Four selected research topics are staged in [Program research](../research/grok-machine-research.md). This replaces Grok triage for the recorded versions, pending PR acceptance; it is not retirement clearance.

The [current-validity follow-up](grok-validity-review.md) records which unresolved Grok proposals are already implemented, superseded or still technically relevant. No additional source bodies were imported.

## Post-freeze ordered mining

The September 24 ownership freeze supersedes the earlier semantic-owner assumption used during the first donor pass:

- **Program** — research, experiments, evidence, machine-development questions/findings, reviewed decisions/adoption records, partnerships/economic/business work, migration/retirement record.
- **System** — application, canonical shared operational definitions, application/Store semantic boundary, project-definition classes, records/custody, customer → Store → Yard journey, adapters/integration, application tests.
- **Store** — Store-local vocabulary, catalog/SKUs, material resolution, stock, admitted capability, modeled operations/time, economics, Store answers/refusals/deferrals, Store tests.

Because donor mining was performed before that ownership correction, the next phase reclassifies **already-admitted material** against these frozen buckets before reopening any donor source.

### Ordered reclassification queue

| Order | Subject | Current disposition |
| --- | --- | --- |
| 1 | Common Entry Architecture | **COMPLETED.** Rehomed to System; Program retains provenance/relocation only. |
| 2 | Information custody / external processing | **COMPLETED.** System owns implemented project/evidence/record custody and any future operational disclosure interface; Program retains broader secondary-use, aggregation, participant, provider-policy, and commercial-sensitivity questions. No consent machinery was invented. |
| 3 | Governed Reference enduring rulings | **COMPLETED.** Program keeps the ADR/ruling decision-provenance record. Current owner review found no additional operational rule body requiring migration solely to preserve those historical rulings. |
| 4 | Machine/cell research still housed in System | **IN PROGRESS.** First slice relocated: Machine Build Program, Next Engineering Step, and research-cell planning/staging now live under Program `research/machine-development/`; old System paths are compatibility pointers. Deeper dimensional/sheet staging and engineering remain for separate classification. |
| 5 | Review-owned research duplication | Preserve Review navigation/presentation while ending independently editable duplicate research authority. |
| 6 | Final pointer/dependency audit and donor retirement proposals | Archive only after active trees no longer depend on retired donors as current authority. |

Implementation kinks such as unknown-class fallback, Store economics, project behavior, or machine execution are **not mining work** and remain deferred until the ownership/migration cleanup is complete.

## Earlier pre-freeze queue — historical context

The table below records the first-pass queue and is retained for provenance. It no longer controls execution where the post-freeze ordered-mining queue above differs.

| Order | Work | Destination / decision |
| --- | --- | --- |
| 1 | Review Program organization and research admission; verify the existing public links | Program; then Review relocation notice |
| 2 | Review Grok reconciliation candidate and selected research | Program PR; no merge in this pass |
| 3 | Complete browser comparison for recovered Sarah interactions before retirement | Ownership resolved; browser execution unavailable in this pass; no source transplant |
| 4 | Review unknown-class fallback in current System; do not rebuild the existing shadow contract | System owner: dedicated regression and scoped decision; select research experiments separately |
| 5 | Staging candidate versus Governed Reference accepted/recovery code and tests | Establish successor coverage; retain useful test cases and historical proof, not the entire candidate package in System |
| 6 | Governed Reference semantics and open PR #4 (Store S1/machine-site boundary proposals) | Reconcile accepted semantics into System and experimental engineering into Program; close or transfer open work deliberately |
| 7 | Review research/ontology/roadmap supporting material | Route research to Program and governing contracts to System, while preserving full demonstration pages |
| 8 | Dependency and link audit, archive proposals | Grok, Staging and Governed Reference only after their retirement gates pass |

At inventory time Grok and Staging had no open PRs. Governed Reference had open PR #4. Open issues, tags/releases, unreachable history, deployment dependencies and external incoming links have not yet been exhaustively audited. These are retirement blockers, not reasons to import everything.

## Specific source contradictions to reconcile

- Resolved at System `5c07833f4547e68a80770488a47f86154e091e74`: its README now says “Public working repository.” This pass made no System or visibility change.
- Grok's README still describes a historical inability to access Governed Reference; current access works. That statement is historical, not a present blocker.
- Older branch instructions prohibit work outside their workshop. They describe that earlier task boundary; they do not override the owner's current consolidation instruction.
- System currently houses machine research. The new Program ownership direction does not make those files disappear or invalidate their references. Each relocation needs a destination and a checked pointer.

## Retirement acceptance

Every worthwhile item has a destination; every excluded item has a reason; source-only behavior has been evaluated; unresolved PRs/issues have a disposition; consumer pins and public links still work; a recoverable historical checkpoint exists. Only then is a retirement action ready for approval/execution.
