# Transfer Staging retirement review

**Donor:** `GeorgePlattDemo/scan-to-build-transfer-staging`  
**Donor main:** `4e9a50218679e05801e84f34eea99830db0779a0`  
**Review date:** 2026-09-24  
**Status:** retirement candidate; no archive or deletion performed by this review.

## Purpose

Decide whether the transfer repository contains current authority that must be migrated, or whether it can leave the active workspace after its useful evidence and lessons have durable destinations.

This is a disposition record, not an implementation import.

## Inventory result

The donor contains 239 tracked files and one branch.

After stripping the nested `m1.4-candidate.2/` transport prefix:

- 156 donor paths also exist in Governed Reference main `18949f163718a937f072f4be3a654bb303e53160`;
- 45 of those are exact Git blobs;
- 111 same-path files were changed in the later governed lineage;
- 83 donor paths are absent from the later Governed Reference tree.

The 83 absent paths are concentrated in the Candidate.2 reference-node/store prototype, synthetic fixtures, candidate-only schemas/tests, spec fragments, transfer-part reconstruction files, and transport/status documents. Exact absence does not make them current requirements.

## Controlling recovery evidence

Governed Reference contains the later recovery audit:

`docs/audits/phase-1-recovery-audit-2026-09-06.md`

That audit examined the transferred Candidate.2 against the authoritative governed baseline and concluded:

- recoverable concepts existed;
- the transferred package was incomplete and unsuitable for direct import;
- multiple critical/high defects remained in authority, unresolved-condition persistence, freshness/content binding, schema/fixture consistency, quantity/geometry checks, event claims, and routing;
- the accompanying validation/closure claims were not suitable as acceptance evidence;
- stale current-main replacements, shortened core/schema/test files, altered fixtures, moving-tag workflow, truncated specification fragments, and transfer packaging should not be imported;
- exact recovery artifacts and useful negative-test intent should be retained as historical/recovery evidence rather than promoted as the implementation baseline;
- final disposition was **NO-GO — candidate should not be imported**.

The later Governed Reference main contains a corrected bounded reference-node implementation and fixtures. That successor is itself historical relative to the present Program/System/Store organization; its existence is evidence that Candidate.2 was not left as the accepted implementation.

## Disposition by subject

| Subject | Disposition | Reason / destination |
| --- | --- | --- |
| Candidate.2 runtime/core replacements | **SUPERSEDED / reject from active record** | Later audit identified stale/incomplete replacements and blocking defects. Do not migrate them into System or Store. |
| Candidate validation/closure reports | **HISTORICAL CLAIM / do not use as acceptance evidence** | Later independent recovery audit found the claims not reproducible from the observed package. |
| Transfer parts, assembly metadata, recovered evaluator, exact hardening test | **HISTORICAL RECOVERY EVIDENCE** | Preserve provenance to donor commit/path or archived donor; do not make active implementation files merely to keep the bytes visible. |
| Stock-form sheet/dimensional separation | **VALID PRINCIPLE, successor exists** | Later Governed Reference and current architecture preserve the separation. Program shared definitions also preserve capability/material/authority distinctions. |
| Capability vs availability; availability vs reservation; evaluation vs GateResult; authorization vs execution | **VALID SHARED SEMANTICS** | Belongs in Program canonical definitions; not a reason to keep Staging active. |
| Explicit negative cases: unavailable/stale stock, missing quantity, machine/form mismatch, datum/authority failures | **VALID TEST INTENT** | Preserve the risks/requirements through successor tests or migration evidence; do not require the obsolete Candidate.2 fixture bodies. |
| Synthetic Meadows species/width bands | **HISTORICAL FIXTURE FACTS** | Not industry facts, current Store facts, or machine capability. |
| Candidate-only Store/service/project-class schemas | **NOT ACTIVATED / superseded** | Later governed audit/current architecture did not activate these as current contracts. |
| Candidate spec fragments | **REJECT from active record** | Full controlling specification existed elsewhere; fragments were identified as unsuitable substitutions. |
| Root README, `TRANSFER-STATUS.md`, `CANDIDATE-2-PRESENT.txt` | **TRANSPORT HISTORY** | No continuing authority after this disposition is recorded. |

## Current dependency check

Searches of the present working/public repositories — Program, System, Store, Review, and the short Scan-to-Build introduction — found no current reference to:

- `scan-to-build-transfer-staging`;
- `m1.4-candidate.2`;
- `TRANSFER-STATUS.md`;
- the transfer-part filenames.

System retains one historical mention of “Candidate.2” in its copied governed reference-node explanation, solely to state that unused Candidate.2 contracts were **not activated**. That is not a dependency on the donor repository.

No open pull request or additional branch exists in Transfer Staging.

This search is a current-tree dependency check, not a proof about external bookmarks, old conversations, unreachable Git history, or third-party links.

## Retirement requirement

Transfer Staging has no identified continuing owner function.

Before repository retirement:

1. retain this disposition record;
2. preserve the donor repository identity and final main SHA;
3. preserve the later Governed Reference recovery audit identity as the substantive technical disposition;
4. ensure any desired exact recovery bytes remain recoverable through an archived repository or another deliberate historical mechanism;
5. do not transplant rejected Candidate.2 bodies merely to justify retirement.

After those conditions are satisfied, the repository should leave the active working set. Archive is preferable as the first retirement action because it preserves exact Git provenance while removing the repository from normal development. Permanent deletion, if ever desired, should occur only after the owner intentionally decides that archive-level recovery is no longer needed.

## Result

**RETIREMENT CANDIDATE — no current implementation migration required.**

The useful result of Transfer Staging is the recovery evidence and the lessons that survived it, not the transferred candidate as an active codebase.
