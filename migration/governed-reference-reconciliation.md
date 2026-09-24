# Governed Reference reconciliation

**Donor:** `GeorgePlattDemo/scan-to-build-governed-reference`  
**Main:** `18949f163718a937f072f4be3a654bb303e53160`  
**Review date:** 2026-09-24  
**Status:** migration/retirement candidate; no donor archive, deletion, runtime change, or Store change performed here.

## Purpose

Separate the durable governance and research created in Governed Reference from the historical M1 implementation that produced it.

The repository was necessary to establish a disciplined simulation-only reference slice. It no longer needs to remain a fourth working authority if its enduring content has clear destinations.

## Repository shape

Current main contains 233 files.

An exact-blob comparison against current working repositories found 39 Governed Reference files already copied exactly into System. Those include the root governance/review documents and all 13 ADRs. Blob equality is duplication evidence, not proof that System is their correct permanent owner.

The remaining tree is dominated by:

- M1/reference-node application code;
- schemas;
- fixtures;
- scripts;
- tests;
- package/build infrastructure;
- frozen documentary baseline copies;
- the full historical STB-REF/STB-PLAN documents;
- architecture/audit/supporting documents.

Those bodies should not all be copied into Program.

## Destination rule

### Program

Program owns research questions, experiment evidence, reviewed decisions/adoption records, machine-development questions/findings, and migration/retirement record. System owns canonical shared operational definitions and application architecture; Store owns Store-local facts and capability/economic answers.

Selected Governed Reference content belongs in Program only where it is research, evidence, reviewed decision/provenance, or migration record; operational material belongs with System or Store:

- enduring ADR/governance lessons as decision/provenance records;
- shared object/status source material only as provenance for System operational definitions;
- demand/information-custody research that remains current;
- safety/authority separation;
- negative lessons from recovery/security audits;
- unresolved machine-development questions;
- source provenance and retirement record.

Candidate result in this branch:

- `governance/governed-reference-rulings.md`
- `research/machine-site-convergence.md`

Canonical shared operational terminology is now owned by System. Program retains vocabulary only for research/decision context and provenance.

### System

System owns current application behavior, canonical shared operational definitions, application architecture, contracts/adapters, records, integration behavior, and tests.

Historical Governed Reference code should enter System only when a present System requirement specifically needs that executable behavior and it survives current acceptance tests. The old M1 packages/schemas/fixtures are not imported merely because they once demonstrated governance.

System's historical Governed Reference mirror remains provenance. Current operational rules should be explicit System contracts/docs; Program decision/research records may be referenced for rationale without becoming a second operational authority.

### Store

Store owns current material/offering/stock resolution, capability, machine/cell declaration, modeled work/time, economics, fulfillment, and Store answers.

Historical reference-node/store concepts enter Store only when they match the current Store contract. An old synthetic yard fixture is not current Store stock or capability.

### Historical source

The complete M1 runtime, schemas, fixtures, package infrastructure, frozen STB-REF/STB-PLAN bodies, historical validation reports, and repository-local workflow files are valuable provenance but do not need active copies in Program.

Archive preserves those exact bytes and their Git history without making them part of daily authority.

## Root governance and ADRs

The source root said STB-REF controlled domain semantics, STB-PLAN controlled activation, and STB-BUILD-M1 controlled that implementation slice.

That hierarchy was appropriate for the historical repository. The current organization changes the destination:

- shared operational meaning → System definitions;
- application architecture / record-custody rule → System where operational;
- research/evidence/decision rationale → Program;
- Store-local fact/capability/economic contract → Store;
- historical milestone/build rule → source archive/history.

The 13 source ADRs were reviewed. Their disposition is recorded in `governance/governed-reference-rulings.md`.

Not every historical “accepted” ADR remains present Program law. For example, the donor's private-repository policy is repository history, and its “do not store patent PDFs” choice is inconsistent with later current practice. M1-specific capability limits remain historical limits unless separately adopted today.

## Full STB-REF / STB-PLAN

The source contains large frozen `STB-REF-0.2.5` and `STB-PLAN-0.2.5` documents plus duplicate documentary-baseline copies and DOCX counterparts.

Do not create another active full-copy set in Program solely because the donor is retiring.

The correct extraction is:

- canonical still-valid shared operational definitions → System;
- application architecture / operational custody requirements → System;
- research propositions and reviewed decision/provenance records → Program;
- Store-local requirements → Store;
- the exact historical full documents → archived source provenance.

This preserves citeability without making old versioned specifications compete with current authority.

## Historical implementation disposition

| Source area | Disposition |
| --- | --- |
| `packages/`, `src/`, `capture-adapters/`, inspectors | Historical executable reference. Do not bulk-import. Extract a current requirement/test only when a present owner demonstrates need. |
| `schemas/` | Historical contracts for the M1/reference-node slice. Keep in archive; do not make schema presence equal current activation. |
| `fixtures/` | Historical conformance/adversarial evidence. Preserve through archive and selected risk lessons; do not treat synthetic material/stock as current facts. |
| `tests/` | Valuable evidence of risks and boundaries. Port only tests that protect a current System/Store contract; otherwise retain as historical proof. |
| `scripts/`, package files, CI | Repository-specific implementation infrastructure; retire with donor unless an owning repository independently needs equivalent tooling. |
| validation/freeze/change reports | Historical evidence; keep provenance, do not make current acceptance claims. |
| documentary baseline duplicate tree | Archive/history; do not copy duplicate bodies into Program. |
| STB-REF/STB-PLAN full bodies | Historical controlling sources for their version; cite through archived donor, while selected still-valid material is admitted to the current System, Store, or Program owner according to subject. |

## Branch reconciliation

The donor has four observed branches.

### `fix/m1-reference-node-recovery`

Head recorded in the Program inventory: `d3ad2a55fc118a5ab802d68a6d34e9fed0d4cca5`.

The branch contains no recorded file blob absent from both donor main and System. Its corrected work was squash-merged into donor main at `18949f163718a937f072f4be3a654bb303e53160`.

**Disposition:** superseded branch history; no separate migration body.

### `chore/review-readiness`

Head: `00147688c7039e70db7e51e13940d5a0313832b2`.

The prior inventory identified 10 branch-only file versions, all repository/runtime infrastructure (workflow, package metadata, core package versions, fixture verifier, root export). Main later diverged through reviewed recovery work.

**Disposition:** historical pre-recovery implementation versions. No Program migration. Preserve only through Git history unless a current owner can identify a specific still-missing behavior.

### `docs/store-s1-boundaries` / donor PR #4

Head: `f3a7ba4f35bd3abf0669e3aa15ce5a4af4455ec7`.

It adds exactly three proposed documents:

1. `store-reference-node-0.1.md`
2. `store-s1-build-plan-0.1.md`
3. `machine-site-convergence-0.1.md`

Disposition:

- **Store reference-node contract:** superseded as a build authority by the later independent Store/System ownership model. Durable semantic separations are covered by current System operational definitions and Store-local definitions. Do not migrate the full body.
- **S1 build plan:** superseded implementation plan. It explicitly assumes S1 code belongs in Governed Reference/Grok, which is no longer the current owner structure. Do not migrate as backlog.
- **Machine-site convergence:** retain as **Program research**, stripped of fixture-specific/unactivated pseudo-contract claims. The unresolved frames, kinematics, tool/stock binding, lowering, controller-dialect, release/acceptance/execution separation, and commissioning questions remain useful.

The open donor PR should be closed with its disposition recorded after the Program reconciliation is accepted; it should not be merged into a repository intended for retirement merely to preserve one useful research document.

## Governed Reference audit value

The Phase-1 recovery audit is one of the donor's most useful historical artifacts because it demonstrates that “green” package claims did not equal safe or correct authority behavior.

Retain the lessons:

- caller-constructible authority is not authority;
- unresolved conditions cannot disappear at a handoff;
- stale/changed content requires fresh binding;
- schemas and fixtures must agree;
- acceptance must validate relational ownership and finite/positive quantities;
- event names/status must not overstate execution;
- review/CI controls are part of the claimed evidence;
- synthetic fixture facts are not industry or current Store facts.

The full 73k audit can remain in the archived source. Program needs the decision lessons and exact source identity, not a second full copy.

## Final mining coverage

The final content pass classified all 233 files on donor main with no unclassified paths:

| Disposition class | Files | Meaning |
| --- | ---: | --- |
| First-pass Program admissions | 33 | Research, governance/ADR lessons, definitions/source vocabulary, common-entry/custody material, and Demand-as-Architecture source material were compacted rather than bulk-copied. Post-freeze reclassification now moves operational material to System/Store while Program retains research/decision/provenance. |
| System or historical executable evidence | 154 | M1/reference-node code, schemas, fixtures, tests, scripts, inspectors, current-simulation notes, audits and related executable evidence. Current implementation enters System only when a present System requirement specifically needs it; otherwise it remains source history. |
| Frozen source/archive only | 23 | Full STB-REF/STB-PLAN versions, documentary-baseline copies, source manifests and historical frozen material. Preserve exact source identity; do not make old versioned specs a competing current authority. |
| Repository-local/provenance only | 23 | Repository plumbing, package-era dependency record, root reports/manifests, setup/history and other donor-local administration/provenance. |

**Unclassified main paths: 0.**

Branch-only content is also dispositioned:

- `fix/m1-reference-node-recovery` — corrected work incorporated into donor main; no separate current body.
- `chore/review-readiness` — branch-only runtime/infrastructure versions are historical pre-recovery implementation evidence.
- `docs/store-s1-boundaries` — two Store/S1 planning documents are superseded by current System/Store ownership; machine-site convergence was retained as Program research.

Additional Program admissions from the final pass:

- `governance/common-entry-architecture.md` — now a relocation/provenance notice; current rule is System `docs/application/COMMON-ENTRY-ARCHITECTURE.md`
- `governance/information-custody-and-processing.md` — broader research/policy record; current application custody boundary is System `docs/application/INFORMATION-CUSTODY-BOUNDARY.md`
- `research/demand-as-architecture.md`
- `governance/ownership-and-source-questions.md`

The full private Demand-as-Architecture working paper remains private at its exact donor source/hash. Program records the admitted research propositions without accidentally publishing the full private source.

## Current blockers before retirement

**Content mining is complete.** Governed Reference is not yet archive-ready only because the current working repositories still contain documentary dependencies and the migration candidates have not yet been adopted.

Remaining retirement work is mechanical/governance work:

1. preserve the post-freeze System/Program/Store ownership map and finish reclassifying first-pass admissions;
2. keep this Governed Reference reconciliation aligned with those current owners;
3. close or otherwise disposition donor PR #4 without losing the selected machine-site research;
4. repoint/remove current System documentary pointers that still call Governed Reference the controlling semantic/governance source;
5. reduce System's copied governance mirror after Program ownership is established, while retaining implementation-specific contracts/tests that System actually needs;
6. run the final incoming-link/dependency search across the current working/public trees;
7. record the final donor main SHA and branch-head checkpoint;
8. archive the donor before considering any permanent deletion.

No further source-body mining is required unless a later owner identifies a specific current behavior that is missing and traces it back to the archived donor.

## Expected retirement result

The donor should ultimately become an **archived historical source**, not a fourth active authority.

Program should tell a future reader what the rules and research conclusions are now.  
System should tell them what the application executes now.  
Store should tell them what the Store resolves/models now.  
The archived Governed Reference should answer only: **how did this governance and the bounded M1 proof get established?**
