# Grok reconciliation

Candidate against Program main `ca3565a38fee5a067634590f3116afd5dac5d420`, September 24, 2026. Grok remains private; Program remains public. No donor content or settings are changed. No repository is cleared for retirement.

## Scope and evidence

The [register](grok-reconciliation.json) covers all nine observed branch heads: 257 file occurrences, 126 distinct path/blob records. Branch names, commits, tree identities and per-branch file counts are recorded. This supersedes the earlier Grok triage dispositions in [source-inventory.json](source-inventory.json) for these exact source versions; it does not revise Staging or Governed Reference triage.

All branch trees were compared. Documentary status, research sections, meaningful conflicting variants and System transfer records were examined. Code and test ownership is established by exact copies or documented ancestry, not by executing historical applications or claiming a line-by-line behavioral audit. Per-record reviewBasis states this limit. Tags, unreachable history, incoming links and source-only UI behavior remain outside retirement clearance.

| Branch | Files | Commit |
| --- | ---: | --- |
| build/app-foundation-0.1 | 116 | `4595b4785a2686486e477ce2e70fb3f476285a8d` |
| build/app-front-door-0.1 | 24 | `c85487d7285e044f024934132cc1dddc30c0b7dc` |
| main | 13 | `f704f0da3f34b58506791890691cbf4ceb315b8a` |
| plan/app-entry-intake-contract-0.1 | 25 | `2d80b5a7b0e7687c425e100bfa0ff3a833166d42` |
| plan/app-master-roadmap-0.1 | 24 | `985db87a707bd454d7c58419e2cf4d884f00cded` |
| prototype/sarah-alcove-tour | 11 | `b52570fe48db3af09825b826b739aca72db32c22` |
| wip/app-build-0.1-stabilization | 23 | `bec2da322d7f4e63d549f1b21f079d346c0b4086` |
| wip/atlas-0.1 | 10 | `843fc1878a544efc9d42145ccfecfbb87f87afbe` |
| wip/cell-spine-0.1 | 11 | `f0c3e08682810d7a3c03c211dc76f8ece756313e` |

The branch named `wip/atlas-0.1` does not itself contain the Atlas documents. Those research files were recovered on the stabilization and foundation branches. The cell-spine branch contains an earlier wording variant that must not be mistaken for commissioned capability.

## Dispositions by subject

| Subject | Disposition and destination |
| --- | --- |
| Atlas 04–07 selected research questions | ACCEPTED / migrate to Program: [curated questions](../research/grok-machine-research.md), with exact original and existing public source identities |
| Application foundation, tests, build and intake planning | SYSTEM-owned / leave or point to System where not identical; no old code imported |
| Identical journeys, architecture, Atlas background and corrected cell source | DUPLICATE / no new authority; register names the exact System copies |
| Old cell live-capability wording, old fulfillment wording, partial roadmap | SUPERSEDED / retain as history, do not promote; explicit corrections below |
| Workshop manifests, upload status and superseded navigation | SUPERSEDED / retain as history, do not promote; current ownership records govern |
| Compiler/minimum-contract proposals and two UI prototypes | UNRESOLVED / needs owner decision; no design or behavior adopted |
| Material, admitted capability, travel/time and economics | STORE-owned / leave or point to Store as a subject boundary; no standalone Grok item in this batch qualifies for Store migration |

Counts: 4 accepted, 38 System-owned, 0 Store-owned, 9 superseded, 71 duplicate, 4 unresolved. Acceptance applies only to the selected questions, not every claim in the source document.

## Why older variants are excluded

- Cell blob `e1864c2d3b7ad92293144e0fcacab4025d842878` calls synthetic operations live. Successor `73282ee4a7bdada9b1cd261f5fbae5bb5d7092a5` explicitly corrects this to synthetic, not installed or commissioned. The compared changes correct status and source references; they do not supply missing measured capability.
- Handoff blob `f75e3783623c68605fd747922b13d68276152b0a` uses simulated fulfillment status. Successor `73a6ffb981611190036dcbeabfe6069a9b5ec631` uses reference-node evaluation disposition. System contains that explicit correction.
- Partial roadmap `58de02e9906866a87f3a83fc4a9e54f87c1dd0ae` explicitly says not to build from the checkpoint. Completed roadmap `615dc7dc6faa13eeab2b16b6ee85a1fc5ba78f3b` supplies subsequent milestones; it remains System planning ancestry, not a fresh build order.
- The minimum-contract proposal explicitly narrows the compiler proposal and rejects owner names as status values. That conflict is recorded; neither proposal is adopted merely because one was written later.

These decisions use explicit correction, scope and transfer evidence—not timestamp precedence.

## Existing authority evidence

At System commit `3c6dfb27d798842286f4209ba14f47796256b8e3`:

- [Application transfer record](https://github.com/GeorgePlattDemo/scan-to-build-system/blob/3c6dfb27d798842286f4209ba14f47796256b8e3/apps/README.md) and [PR genealogy](https://github.com/GeorgePlattDemo/scan-to-build-system/blob/3c6dfb27d798842286f4209ba14f47796256b8e3/docs/project/BRANCH-PR-GENEALOGY.md) identify the Grok foundation transfer and accepted descendants.
- [Intake reconciliation](https://github.com/GeorgePlattDemo/scan-to-build-system/blob/3c6dfb27d798842286f4209ba14f47796256b8e3/docs/application/INTAKE-SOURCE-RECONCILIATION.md) admits the earlier intake contract only after rewrite. Historical Store pins are not repinned by this migration.
- [Definition ownership](https://github.com/GeorgePlattDemo/scan-to-build-system/blob/3c6dfb27d798842286f4209ba14f47796256b8e3/docs/definitions/README.md) keeps definitions separate from donor prototype behavior.

## Remaining owner decisions

1. System owner: do the compiler/minimum-contract proposals address a demonstrated gap in the current implementation? Record a scoped decision against current behavior before adopting anything; do not create another compiler from this migration.
2. System owner: do the front-door and Sarah prototype contain any useful interaction absent from the accepted application? Compare the actual interactions before retirement. Their local simulated answers and execution implications are not transferable authority.
3. Program owner: select whether any recovered research question merits an experiment. No controller/BOM, envelope increment, budget or commissioning commitment is made here.

**Proposed design → experimental evidence → reviewed decision → versioned Store/System adoption.** Research selection is only the first step.

## Gates and preservation

Program main was reported protected by current branch metadata. Required rules/check settings were not independently established by that flag. This candidate still requires review and is not merged. Existing public/private posture and all donor files remain intact. Only Program navigation points to this reconciliation; donor relocation notices are unnecessary because nothing was removed. Documentary checks validate coverage, identities and links, not machine performance or proposal merit.
