# Donor mining closeout — Grok, Transfer Staging, Governed Reference

**Date:** 2026-09-24  
**Scope:** content mining only.  
**Donors:** `grok-file`, `scan-to-build-transfer-staging`, `scan-to-build-governed-reference`.  
**Result:** content mining complete. Remaining work is adoption, pointer cleanup, dependency verification, and retirement mechanics.

## End-state rule

The active working set is intended to have three authorities:

- **Program** — research, experiments, evidence, machine-development questions/findings, reviewed decisions/adoption records, partnerships/economic/business work, migration/retirement record.
- **System** — application, canonical shared operational definitions, application architecture, shared contracts, project-definition classes, records/custody, adapters/integration, tests.
- **Store** — Store-local vocabulary, material/stock/catalog facts, admitted capability, modeled work/time, economics/fulfillment facts, Store answers/refusals/deferrals, tests.

The public Review and short Scan-to-Build repositories remain review/demo surfaces.

Donor repositories do not remain active simply because useful thinking happened there.

## Grok

Program candidate: PR #2, `organize/grok-reconciliation`.

Observed source coverage:

- 9 branch heads;
- 257 file occurrences;
- 126 distinct path/blob records.

Final documentary classifications:

| Classification | Records |
| --- | ---: |
| ACCEPTED / migrate to Program | 4 |
| SYSTEM-owned / leave or point to System | 40 |
| DUPLICATE / no new authority | 71 |
| SUPERSEDED / retain as history, do not promote | 11 |
| Unresolved documentary classification | **0** |

Accepted Program value is curated research/question material, not old runtime code.

The minimum definition contract is already System-owned. The broad compiler proposal is superseded. Old front-door/prototype implementations are not new app authorities. Historical cell wording that implied live capability is not adopted.

One bounded System follow-up remains: a nonempty unknown class identifier must not silently acquire Board meaning. That is an implementation issue, not unmined Grok content.

**Mining status: COMPLETE.**

## Transfer Staging

Program candidate: PR #5, `organize/transfer-staging-retirement-0.1`.

Source main:

`4e9a50218679e05801e84f34eea99830db0779a0`

Tracked files: **239**.

After removing the transport prefix:

- 156 paths have a later path successor in Governed Reference;
- 83 paths are Candidate.2-only/transport-era material.

The later Governed Reference recovery audit examined Candidate.2 and concluded **NO-GO — do not import Candidate.2**.

Useful results were separated from the failed candidate:

- valid semantic/safety principles → current System operational definitions or Program research/decision record according to ownership;
- useful negative-test intent → current requirements/evidence where applicable;
- exact recovery artifacts → historical provenance;
- stale/incomplete runtime replacements → reject from current implementation;
- synthetic fixture facts → history, not Store truth;
- transfer manifests/status/reconstruction parts → transport history.

No current Program/System/Store/Review/short-demo tree reference to the Transfer Staging repository was found in the bounded dependency search already recorded in PR #5.

**Mining status: COMPLETE.**

## Governed Reference

Program candidate: PR #6, `organize/governed-reference-reconciliation-0.1`.

Source main:

`18949f163718a937f072f4be3a654bb303e53160`

Main files: **233**.

Final file coverage:

| Disposition class | Files |
| --- | ---: |
| Program-mined current meaning/research | 33 |
| System or historical executable evidence | 154 |
| Frozen source/archive only | 23 |
| Repository-local/provenance only | 23 |
| Unclassified | **0** |

Branch-only dispositions:

- `fix/m1-reference-node-recovery` — corrected work incorporated into donor main; no separate current body;
- `chore/review-readiness` — historical pre-recovery runtime/infrastructure versions;
- `docs/store-s1-boundaries` — two old Store/S1 plans superseded by current owner separation; machine-site convergence retained as Program research.

Program admissions from the Governed Reference mining include:

- enduring governance/ADR rulings;
- shared-definition source material;
- common-entry architecture (post-freeze rehomed to System; Program retains relocation/provenance);
- information custody/disclosure/external-processing source material (post-freeze split: System operational custody; Program broader research/policy);
- machine-site convergence research;
- Demand-as-Architecture research record;
- unresolved ownership/source questions.

The full private Demand-as-Architecture working paper remains private at its exact source/hash; Program contains the admitted current research propositions, not an accidental public copy of the full source.

The full historical M1 runtime, schemas, fixtures, tests, STB-REF/STB-PLAN versions, audits, and repository infrastructure remain archive/provenance unless a current implementation owner later demonstrates a specific need.

**Mining status: COMPLETE.**

## Canonical definitions dependency — resolved by ownership freeze

The September 24 ownership freeze superseded the earlier plan to make Program the continuing operational semantic authority. System now owns canonical shared operational definitions; Program retains research/decision vocabulary and semantic provenance.

The first-pass consolidation captured shared terminology from Governed Reference, Grok, Store, and System. Under the ownership freeze, operational meaning is now maintained by System while Program retains research/decision vocabulary and provenance for:

- high-risk common words such as project, model, stock, available, fixture, state, release, execution, production, and build;
- entry/actor/opening context;
- core governed objects;
- definition-contract responsibility/status/owner terms;
- Store/commercial distinctions;
- material/manufacturing/machine distinctions;
- explicit “never equate” boundaries.

Old semantic pointers are removed or retained strictly as provenance only after the current System/Store owner is identified.

## What “mining complete” means

No remaining donor file is waiting for someone to decide whether it contains useful current meaning.

Future retrieval from an archived donor is allowed only for one of these reasons:

1. exact historical provenance;
2. a current owner identifies a specific missing behavior/test and traces it to history;
3. legal/source verification requires the original;
4. a research question intentionally reopens an earlier source.

“Maybe there is something good in there” is no longer a reason to keep a donor active.

## Current pointer audit

A bounded search of Program, System, Store, Review, and the short public Scan-to-Build repository found **no current reference to Transfer Staging**.

Grok and Governed Reference references in System fall into two classes.

### Provenance references that may remain

These record historical source identity and should not be erased merely because the source is archived:

- `provenance/APP-TRANSFER.md`
- historical source rows in `provenance/SOURCE-PINS.md`
- accepted-lineage references in the current baseline/state records, when clearly labeled provenance/history
- source-library provenance headers for retained historical copies

Archived repositories remain valid provenance targets.

### Current/controlling-source references that must be reconciled before retirement

Examples found in current System include:

- `docs/application/README.md` — still says application code has not yet been transferred and points to Grok as accepted implementation;
- `docs/application/CONTROLLING-SOURCE-POINTERS.md` — still points to Grok as controlling source;
- `docs/project/SOURCE-AUTHORITY.md` — still names Grok/Governed Reference as current authorities;
- `docs/cell/CURRENT-CELL-SOURCE-POINTER.md` — still treats Grok Cell material as externally pinned current source;
- `docs/application/SEMANTIC-GUARDRAILS.md` and historical semantic copies — still point to Grok for meaning that is now owned by System operational definitions;
- `docs/governance/README.md` and `docs/governance/CONTROLLING-SOURCE-POINTERS.md` — still call Governed Reference the current documentary/semantic source and promise exact-copy transfer into System;
- `work/capability-bridge/GOLD-INDEX.md` and related source maps — include current-role labels that need to be separated from historical provenance;
- `apps/stb/shared/contracts.mjs` — contains a `GR_SOURCE` constant and therefore needs owner-specific review before any donor retirement claim;
- some capability/project bridge documents still say “current governed source” when the intended future authority is Program.

These references are not evidence of unmined donor content. They are stale or transitional ownership/pointer debt.

The retirement cleanup must preserve historical pins while changing current authority language to the frozen Program/System/Store ownership map.

## What remains before retirement

These are not mining tasks:

1. review/adopt or revise Program PR #2 (Grok);
2. keep System canonical operational definitions and Program research/decision vocabulary separated under the ownership freeze;
3. review/adopt or revise Program PR #5 (Transfer Staging disposition);
4. review/adopt or revise Program PR #6 (Governed Reference reconciliation);
5. close/disposition Governed Reference PR #4 after its selected research is secured;
6. repoint/remove System documents that still name Grok or Governed Reference as current semantic/governance sources rather than provenance;
7. run final incoming-link/dependency searches against the post-adoption trees;
8. record final donor branch-head checkpoints;
9. archive donors before any consideration of permanent deletion.

## Dead-wood rule after retirement

Once the donor migrations are adopted and pointers are corrected:

- do not keep duplicate governance in System;
- do not keep donor source libraries merely because they are already copied;
- do not keep old planning documents as current instructions;
- do not use branch forests as filing cabinets;
- keep exact history in Git/archive and current truth in the three owner repositories.

The next cleanup phase should therefore trim active-repository dead wood **before** broad branch deletion.

**NO BLOOD ON WOOD.**
