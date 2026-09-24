# Governed Reference — enduring rulings and historical dispositions

**Source repository:** `GeorgePlattDemo/scan-to-build-governed-reference`  
**Source main:** `18949f163718a937f072f4be3a654bb303e53160`  
**Status:** Program reconciliation candidate. This page does not alter System or Store runtime behavior.

## Purpose

Preserve the governance that still matters after the historical Governed Reference repository leaves the active working set, without treating every M1-era repository decision as permanent Program law.

The source repository mixed three things:

1. durable governance principles;
2. milestone-specific M1 implementation decisions;
3. repository-local process/packaging decisions.

Those categories must remain separate.

## Current enduring rulings

### Safety and authority

- **NO BLOOD ON WOOD / I0 remains non-waivable.**
- Ability, eligibility, readiness, authorization, and execution are separate states.
- Simulation authority and physical-production authority are separate. A simulation result cannot be converted into production authority merely because the simulation passed.
- Live-motion or physical-execution authority must fail closed when the required authority path does not exist.
- A model may process information but does not become an authority and must not sit on a safety-gate or authorization-issuance path.
- A failed or unresolved gate is not made safe by presenting, calculating, or serializing it.
- Production authorization remains a separately activated concern; no historical M1 document creates a present issuer.

### Evidence and state

- Planned objects do not become active merely because they appear in a register, proposal, schema draft, or document.
- A weaker evidence state does not silently promote itself to a stronger one.
- Unknown or unresolved conditions remain visible until a named rule/evidence act resolves them.
- A content hash establishes content identity, not authorship, authority, authenticity, physical correspondence, or safety.
- Released conformance fixtures are immutable as evidence. A substantive correction creates a new identified version rather than silently rewriting the old evidence.
- Durable identifiers should remain stable where compatibility matters; prose improvement alone is not a reason to mutate wire identifiers.

### Geometry, units, and fabrication meaning

- Captured geometry, a drawing, mesh, or point cloud is not automatically fabrication geometry.
- A coordinate origin in data is not proof that a physical machine has been zeroed.
- Geometric feasibility is not structural adequacy.
- Units must be explicit at consequential boundaries. Conversion, where supported, must be explicit and attributable; no silent conversion may be used to manufacture certainty.
- Machine or Store capability cannot fill missing project facts by inference.

### Build discipline

- Map broadly; activate narrowly.
- Implement the smallest verified slice needed to prove the present contract rather than building an entire ontology in advance.
- A proposed module, schema, machine feature, or commercial state has no requirement force until deliberately activated.
- Validation must include negative/adversarial cases appropriate to the authority being claimed.
- A repository move, documentation copy, or schema presence is not acceptance of behavior.

### Custody and outside processing

- Connecting information to another processor is not automatically a transfer of ownership, authority, or custody.
- Outside processing must preserve attribution, source status, unresolved conditions, and applicable authority boundaries.
- External services cannot create governed, Store, or physical authority merely by returning a result.

## Source ADR disposition

| ADR | Historical decision | Program disposition |
| --- | --- | --- |
| 0008 — simulation / production separation | Separate authorization types; no production issuer in v0.2 | **Retain principle.** Generalized above; milestone/version detail remains historical. |
| 0009 — scalar-first geometry | M1 used scalar measurements; mesh/point cloud not fabrication geometry | **Retain principle, not M1 representation freeze.** Current systems may support richer evidence, but richer evidence still requires explicit derivation/verification before fabrication use. |
| 0010 — private repository | Governed Reference remained private/all-rights-reserved | **Historical repository policy.** Not Program-wide governance; current Program/System/Store visibility is separately controlled. |
| 0011 — M1 vertical slice | Implement only the PLACE/Project A slice | **Retain build-discipline principle.** Specific inactive M1 entry contexts are historical. |
| 0012 — fail-closed gate-to-authorization | Only policy-constructed eligibility plus explicit command could issue simulation authorization | **Retain fail-closed principle.** Exact historical classes/functions are implementation history. |
| 0013 — fixture immutability | Hash governed fixtures; correction creates new version | **Retain evidence principle.** Exact script/directory layout is historical implementation. |
| 0014 — identifier policy | Use existing `stb:` identifier pattern | **Retain stability/attribution principle.** Exact length/schema rules remain with current executable contracts. |
| 0015 — no silent unit conversion | M1 refused to convert metric observations into its inch-only geometric rule | **Retain no-silent-conversion principle.** The M1 refusal code and inch-only limitation are historical, not a ban on explicit governed conversion. |
| 0016 — structural span | M1 did not evaluate structural span | **Historical capability limit.** Do not promote as a universal current rule; retain the larger rule that geometric fit is not structural adequacy. |
| 0017 — bounded simulation adapter | Finite simulation operations; live command vocabulary refused | **Retain simulation boundary principle.** Exact adapter implementation is historical. |
| 0018 — patent bibliography | Treat patents as background, not runtime rules; do not store PDFs in primary Git tree | **Split disposition.** “Patents are not runtime authority” remains valid. The old PDF-storage choice is superseded by current repository practice. |
| 0019 — holder control | Information connection is not custody transfer; disclosure objects inactive in M1 | **Retain custody principle.** M1 activation state is historical. |
| 0020 — no model on safety path | Models may process, never authorize or sit on I0/issuance | **Retain principle.** Provider-specific implementation remains separately governed. |

## M1 implementation document

`STB-BUILD-M1.md` is valuable evidence of a bounded implementation method, but it is not a current cross-repository build plan.

Retain these lessons:

- whole architecture may be mapped while only a bounded slice is activated;
- missing structural evidence remains unresolved rather than invented;
- live motion is refused where no physical authority path exists;
- simulation output must be labeled as simulation;
- negative and import-boundary tests matter;
- “definition of done” must be limited to the identified milestone rather than advertised as whole-system conformance.

Do not carry forward its frozen fixture values, inactive-feature list, package layout, or M1 command list as present Program requirements.

## Relationship to canonical definitions

The Program canonical-definitions candidate is intended to own shared word meaning across Program/System/Store. This page owns enduring governance rulings and historical ADR disposition.

Definitions answer **what a term means**.  
This page answers **what cross-repository governance constraints still apply**.

Neither page silently changes executable System or Store behavior. A conflict found in implementation requires an owner-specific reconciliation and tests.

## Historical source retention

The source ADR files, full STB-REF/STB-PLAN documents, M1 packages, fixtures, schemas, tests, and audit records remain recoverable in the retired/archived source repository. They do not all need active duplicates in Program.

The point of this page is to preserve the rulings that must remain easy to find after that repository is no longer part of the working set.
