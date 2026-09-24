# Donor Pointer Audit

**Step:** 4 — donor-pointer audit only  
**Program base:** `34fd6e7d1290d3234e3a5492c1720bdf64b37f03`  
**System base:** `57d22530ce095df902228a49989d28d25a40c819`  
**Store base:** `ead5fb182eb05e7081e89c103ff74458654502ae`  
**Review base:** `3d22e9cae852d9612bce96b99420c0208d4778e5`  
**Scan-to-Build base:** `ea17feeac299fc359c6776f85019b242ffffc085`

Donors audited:

- `GeorgePlattDemo/grok-file`
- `GeorgePlattDemo/scan-to-build-governed-reference`
- `GeorgePlattDemo/scan-to-build-transfer-staging`

The audit searched the five current repositories for donor names, common donor path fragments, and known historical donor SHAs. System was also checked for `GR_SOURCE`, `CURRENT-CELL-SOURCE-POINTER`, `source-library`, and `governed-reference`. Search-index hits were checked against exact current-main files where material. Program was scanned directly at the pinned base because its code-search index was unavailable.

Historical pins, source-library copies, ancestry and reconciliation records are `PROVENANCE — KEEP`. A current operational/current-reading dependency on a donor is `CURRENT POINTER — REPOINT`. A copied body is `DEAD DUPLICATE — REMOVE` only when the current owner has already replaced that body with a pointer and duplicate status is unambiguous. Uncertainty is KEEP.

## Result

- `PROVENANCE — KEEP`: **93**
- `CURRENT POINTER — REPOINT`: **2**
- `DEAD DUPLICATE — REMOVE`: **0**

No donor-name or known-donor-SHA hits were found on the audited current mains of `scan-to-build-store`, `scan-to-build-review`, or `Scan-to-Build`.

## Current pointers still blocking donor archive

1. `scan-to-build-system/work/user-intake/CURRENT-FACTS.md` — current implementation facts are still anchored to `grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d`; repoint current identity to the existing System current baseline and retain the donor pin only as historical provenance.
2. `scan-to-build-system/work/user-intake/README.md` — the current work surface still places Grok donor material under **Primary current sources**; repoint current readers to the existing System current baseline/source pointers and keep Grok pins only as historical source history.

No repoint is made in this audit because both blocking rows are in System and this Step 4 change is intentionally one Program branch / one Program ledger file. The next session should fix these rows before any donor archive action.

## Ledger

| repo | path | identity/SHA if present | classification | one-line reason |
| --- | --- | --- | --- | --- |
| 3d-solutions-program | governance/authority.md | grok-file; donor name | PROVENANCE — KEEP | Retirement/ownership register; donor history only. |
| 3d-solutions-program | governance/authority.md | scan-to-build-governed-reference; donor name | PROVENANCE — KEEP | Retirement/ownership register; donor history only. |
| 3d-solutions-program | governance/authority.md | scan-to-build-transfer-staging; donor name | PROVENANCE — KEEP | Retirement/ownership register; donor history only. |
| 3d-solutions-program | governance/common-entry-architecture.md | 18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Explicit source-lineage pin for reconciled Program record. |
| 3d-solutions-program | governance/governed-reference-rulings.md | scan-to-build-governed-reference@18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Program reconciliation provenance. |
| 3d-solutions-program | governance/ownership-and-source-questions.md | 18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Source-lineage note for Program research. |
| 3d-solutions-program | governance/semantic-provenance.md | 18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Intentional historical Governed Reference provenance. |
| 3d-solutions-program | governance/semantic-provenance.md | 4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | Intentional historical Grok provenance. |
| 3d-solutions-program | migration/README.md | grok-file; inventory counts | PROVENANCE — KEEP | Migration inventory record. |
| 3d-solutions-program | migration/README.md | scan-to-build-governed-reference; inventory counts | PROVENANCE — KEEP | Migration inventory record. |
| 3d-solutions-program | migration/README.md | scan-to-build-transfer-staging; inventory counts | PROVENANCE — KEEP | Migration inventory record. |
| 3d-solutions-program | migration/donor-mining-closeout.md | grok-file; donor set | PROVENANCE — KEEP | Donor-mining closeout record. |
| 3d-solutions-program | migration/donor-mining-closeout.md | scan-to-build-governed-reference@18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Donor-mining closeout provenance. |
| 3d-solutions-program | migration/donor-mining-closeout.md | scan-to-build-transfer-staging@4e9a50218679e05801e84f34eea99830db0779a0 | PROVENANCE — KEEP | Donor-mining closeout provenance. |
| 3d-solutions-program | migration/governed-reference-reconciliation.md | scan-to-build-governed-reference@18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Detailed reconciliation ledger. |
| 3d-solutions-program | migration/grok-reconciliation.json | grok-file; multiple branch commits incl. 4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | Machine-readable reconciliation provenance. |
| 3d-solutions-program | migration/grok-reconciliation.md | grok-file; includes 4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | Human-readable reconciliation provenance. |
| 3d-solutions-program | migration/grok-validity-review.md | grok-file@f704f0da3f34b58506791890691cbf4ceb315b8a | PROVENANCE — KEEP | Proposal-review provenance. |
| 3d-solutions-program | migration/source-inventory.json | grok-file; multiple historical source commits | PROVENANCE — KEEP | Migration source inventory. |
| 3d-solutions-program | migration/source-inventory.json | scan-to-build-governed-reference; multiple historical commits incl. 18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Migration source inventory. |
| 3d-solutions-program | migration/source-inventory.json | scan-to-build-transfer-staging@4e9a50218679e05801e84f34eea99830db0779a0 | PROVENANCE — KEEP | Migration source inventory. |
| 3d-solutions-program | migration/transfer-staging-retirement-review.md | scan-to-build-transfer-staging@4e9a50218679e05801e84f34eea99830db0779a0 | PROVENANCE — KEEP | Retirement history; not a current dependency. |
| 3d-solutions-program | migration/transfer-staging-retirement-review.md | scan-to-build-governed-reference@18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Historical cross-donor comparison. |
| 3d-solutions-program | research/demand-as-architecture.md | Governed Reference@18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Research source citation. |
| 3d-solutions-program | research/grok-machine-research.md | grok-file@bec2da322d7f4e63d549f1b21f079d346c0b4086 | PROVENANCE — KEEP | Research provenance; identical System copies are cited. |
| 3d-solutions-program | research/machine-development/engineering/README.md | grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | Program research reading source; not operational law. |
| 3d-solutions-program | research/machine-site-convergence.md | scan-to-build-governed-reference@f3a7ba4f35bd3abf0669e3aa15ce5a4af4455ec7 | PROVENANCE — KEEP | Source-lineage citation for Program research copy. |
| scan-to-build-system | START-HERE.md | grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | Transferred-source lineage; also says not to start in Grok. |
| scan-to-build-system | STB-CURRENT-BASELINE.md | grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | Historical transfer baseline; current System identity is separate. |
| scan-to-build-system | STB-PROJECT-STATE-AND-SOURCE-INDEX.md | grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | Accepted-app provenance row. |
| scan-to-build-system | STB-PROJECT-STATE-AND-SOURCE-INDEX.md | scan-to-build-governed-reference@18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Explicit historical governance provenance. |
| scan-to-build-system | apps/README.md | grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | Transferred lineage record. |
| scan-to-build-system | apps/stb/README.md | grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | Transfer ancestry comment. |
| scan-to-build-system | apps/stb/README.md | Governed Reference@18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Explicit inert candidate/reference; non-executable and non-authoritative. |
| scan-to-build-system | apps/stb/browser/ui/narrative.mjs | Governed Reference@18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Story/source citation, not current authority. |
| scan-to-build-system | apps/stb/shared/contracts.mjs | GR_SOURCE = scan-to-build-governed-reference@18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Hard-coded provenance only; mapped source is executable=false and authority=false; no donor import. |
| scan-to-build-system | apps/stb/test/unit/entry.test.mjs | GR_SOURCE (inherits 18949f163718a937f072f4be3a654bb303e53160) | PROVENANCE — KEEP | Test preserves inert provenance; no donor read. |
| scan-to-build-system | apps/stb/test/browser/project-identity.spec.mjs | GR_SOURCE (inherits 18949f163718a937f072f4be3a654bb303e53160) | PROVENANCE — KEEP | Test preserves inert provenance; no donor read. |
| scan-to-build-system | docs/application/COMMON-ENTRY-ARCHITECTURE.md | Governed Reference@18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Source lineage after rehoming current rule to System. |
| scan-to-build-system | docs/application/CONTROLLING-SOURCE-POINTERS.md | Governed Reference@18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Historical lineage; current System destinations stated in same file. |
| scan-to-build-system | docs/application/CONTROLLING-SOURCE-POINTERS.md | grok-file@2d80b5a7b0e7687c425e100bfa0ff3a833166d42; @4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | Explicit historical/provenance entries after current destinations. |
| scan-to-build-system | docs/application/CURRENT-APP-SUMMARY.md | grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | Original donor pin labeled historical provenance. |
| scan-to-build-system | docs/application/INTAKE-SOURCE-RECONCILIATION.md | grok-file@2d80b5a7b0e7687c425e100bfa0ff3a833166d42; @4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | Reconciliation note records donors and in-System destination. |
| scan-to-build-system | docs/application/README.md | grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | Explicit provenance, not current authority. |
| scan-to-build-system | docs/application/SEMANTIC-GUARDRAILS.md | grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | Earlier semantic-boundary provenance. |
| scan-to-build-system | docs/cell/CURRENT-CELL-SOURCE-POINTER.md | grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | Explicit historical source; current homes listed separately. |
| scan-to-build-system | docs/governance/CONTROLLING-SOURCE-POINTERS.md | scan-to-build-governed-reference@18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Compatibility/historical pointer with current destinations. |
| scan-to-build-system | docs/governance/README.md | scan-to-build-governed-reference@18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Historical copied evidence expressly non-authoritative. |
| scan-to-build-system | docs/governance/source/GOVERNANCE.md | scan-to-build-governed-reference; source copy | PROVENANCE — KEEP | Historical governed-source evidence; current System definitions control operationally. |
| scan-to-build-system | docs/governance/source/STB-BUILD-M1.md | scan-to-build-governed-reference; M1 source copy | PROVENANCE — KEEP | Historical executable/reference evidence. |
| scan-to-build-system | docs/machine/POST-APP-MECHANICAL-SOURCE-MAP.md | grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | KEEP-REFERENCE/KEEP-DONOR research map; current research routes through Program. |
| scan-to-build-system | docs/project/BRANCH-PR-GENEALOGY.md | grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | Ancestry record. |
| scan-to-build-system | docs/project/CURRENT-STATE.md | grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | Transferred-app provenance; current System tree separate. |
| scan-to-build-system | docs/project/SOURCE-AUTHORITY.md | grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | Explicit historical Grok provenance. |
| scan-to-build-system | docs/project/SOURCE-AUTHORITY.md | scan-to-build-governed-reference@18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Explicit historical Governed Reference provenance. |
| scan-to-build-system | docs/project/VERIFICATION-REGISTER.md | 4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | Proof row for historical transferred baseline. |
| scan-to-build-system | provenance/ADMISSION-REGISTER.md | grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | Admission history; current System owner stated. |
| scan-to-build-system | provenance/ADMISSION-REGISTER.md | scan-to-build-governed-reference@18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Historical admission/provenance record. |
| scan-to-build-system | provenance/ADMISSION-REGISTER.md | Transfer Staging; rejected-candidate history | PROVENANCE — KEEP | Explicit archive/provenance candidate; not current baseline. |
| scan-to-build-system | provenance/APP-TRANSFER.md | grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | Exact transfer ancestry. |
| scan-to-build-system | provenance/SOURCE-PINS.md | grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d; @985db87a707bd454d7c58419e2cf4d884f00cded; @2d80b5a7b0e7687c425e100bfa0ff3a833166d42 | PROVENANCE — KEEP | Pinned source/roadmap/intake provenance. |
| scan-to-build-system | provenance/SOURCE-PINS.md | scan-to-build-governed-reference@18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Pinned governed-reference provenance. |
| scan-to-build-system | source-library/README.md | grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | Source-library index; KEEP by rule. |
| scan-to-build-system | source-library/README.md | scan-to-build-governed-reference@18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Source-library index; KEEP by rule. |
| scan-to-build-system | source-library/application-current/README.md | grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | Source-library transfer snapshot. |
| scan-to-build-system | source-library/application-current/STB-APP-BUILD-0.1.md | grok-file; historical copied build document | PROVENANCE — KEEP | Source-library copy; KEEP by rule. |
| scan-to-build-system | source-library/application-current/STB-APP-BUILD-0.1.md | scan-to-build-governed-reference@18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Source-library copy; KEEP by rule. |
| scan-to-build-system | source-library/application-current/STB-APP-SOURCE-MAP-0.1.md | grok-file@f0c3e08682810d7a3c03c211dc76f8ece756313e; @261f643ea27994a8367e971e78c763875f4b524e; @b52570fe48db3af09825b826b739aca72db32c22 | PROVENANCE — KEEP | Source-library source map. |
| scan-to-build-system | source-library/application-current/STB-APP-SOURCE-MAP-0.1.md | scan-to-build-governed-reference@18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Source-library source map. |
| scan-to-build-system | source-library/application-current/STB-APP-STABILIZATION-0.1.md | grok-file@f0c3e08682810d7a3c03c211dc76f8ece756313e; @261f643ea27994a8367e971e78c763875f4b524e; @b52570fe48db3af09825b826b739aca72db32c22 | PROVENANCE — KEEP | Source-library preserved stabilization document. |
| scan-to-build-system | source-library/application-current/STB-APP-STABILIZATION-0.1.md | scan-to-build-governed-reference@18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Source-library preserved stabilization document. |
| scan-to-build-system | source-library/application-current/STB-APP-STRUCTURE-0.1.md | grok-file; preserved source document | PROVENANCE — KEEP | Source-library copy; KEEP by rule. |
| scan-to-build-system | source-library/application-current/STB-SEMANTIC-BOUNDARIES-0.1.md | grok-file@b663d242daa8385ef16af29b89ade6df71971596 | PROVENANCE — KEEP | Source-library semantic snapshot. |
| scan-to-build-system | source-library/application-current/STB-SEMANTIC-BOUNDARIES-0.1.md | scan-to-build-governed-reference@18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Source-library semantic snapshot. |
| scan-to-build-system | source-library/atlas-research/README.md | grok-file / wip/app-build-0.1-stabilization | PROVENANCE — KEEP | Source-library Atlas research; explicitly not adopted. |
| scan-to-build-system | source-library/atlas-research/STB-ATLAS-01-CAPTURE-0.1.md | grok-file / wip/app-build-0.1-stabilization | PROVENANCE — KEEP | Source-library Atlas research; explicitly not adopted. |
| scan-to-build-system | source-library/atlas-research/STB-ATLAS-02-EASY-HARD-IN-0.1.md | grok-file / wip/app-build-0.1-stabilization | PROVENANCE — KEEP | Source-library Atlas research; explicitly not adopted. |
| scan-to-build-system | source-library/atlas-research/STB-ATLAS-03-ORDER-MEMBRANE-0.1.md | grok-file / wip/app-build-0.1-stabilization | PROVENANCE — KEEP | Source-library Atlas research; explicitly not adopted. |
| scan-to-build-system | source-library/atlas-research/STB-ATLAS-04-NEUTRAL-OPS-TO-MACHINE-0.1.md | grok-file / wip/app-build-0.1-stabilization | PROVENANCE — KEEP | Source-library Atlas research; explicitly not adopted. |
| scan-to-build-system | source-library/atlas-research/STB-ATLAS-05-ENVELOPE-LADDER-0.1.md | grok-file / wip/app-build-0.1-stabilization | PROVENANCE — KEEP | Source-library Atlas research; explicitly not adopted. |
| scan-to-build-system | source-library/atlas-research/STB-ATLAS-06-IRON-0.1.md | grok-file / wip/app-build-0.1-stabilization | PROVENANCE — KEEP | Source-library Atlas research; explicitly not adopted. |
| scan-to-build-system | source-library/atlas-research/STB-ATLAS-07-ATOMS-VS-BITS-0.1.md | grok-file / wip/app-build-0.1-stabilization | PROVENANCE — KEEP | Source-library Atlas research; explicitly not adopted. |
| scan-to-build-system | source-library/journey-donors/README.md | grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | Source-library donor bucket; DONOR / REFERENCE. |
| scan-to-build-system | source-library/machine-cell/README.md | grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d; blob 73282ee4a7bdada9b1cd261f5fbae5bb5d7092a5 | PROVENANCE — KEEP | Source-library machine/cell copy. |
| scan-to-build-system | source-library/machine-cell/STB-CELL-0.1.md | grok-file@6137832a79f135933a03b4c4931bd284755b1ee7 | PROVENANCE — KEEP | Exact pre-decision source-library artifact. |
| scan-to-build-system | work/capability-bridge/DIMENSIONAL-MODEL-0.1.md | 4595b478 (Grok accepted-board baseline) | PROVENANCE — KEEP | Historical demand-window evidence for a reference model. |
| scan-to-build-system | work/capability-bridge/GOLD-INDEX.md | grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d; @985db87a707bd454d7c58419e2cf4d884f00cded; @2d80b5a7b0e7687c425e100bfa0ff3a833166d42 | PROVENANCE — KEEP | Explicit Historical donor identities table. |
| scan-to-build-system | work/capability-bridge/GOLD-INDEX.md | scan-to-build-governed-reference@18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Explicit historical donor identity. |
| scan-to-build-system | work/capability-bridge/GOLD-INDEX.md | scan-to-build-transfer-staging@4e9a50218679e05801e84f34eea99830db0779a0 | PROVENANCE — KEEP | Failed-candidate history; do not build from. |
| scan-to-build-system | work/capability-bridge/STORE-SURFACE-0.1.md | 4595b478 (Grok accepted-app notes) | PROVENANCE — KEEP | Historical protocol-note source; no donor checkout or authority. |
| scan-to-build-system | work/capability-bridge/TRIAL-LOG.md | 4595b478 (Grok accepted transfer baseline) | PROVENANCE — KEEP | Historical trial-log row. |
| scan-to-build-system | work/capability-bridge/TRIAL-PROTOCOL.md | grok-file@4595b478… | PROVENANCE — KEEP | Explicitly says donor identity is provenance, not current System identity. |
| scan-to-build-system | work/capability-bridge/WINDOW-SEAT-EDGE-CASE-JOURNEY-0.1.md | scan-to-build-governed-reference@18949f163718a937f072f4be3a654bb303e53160 | PROVENANCE — KEEP | Explicitly labeled historical governed source. |
| scan-to-build-system | work/user-intake/CURRENT-FACTS.md | grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d | PROVENANCE — KEEP | System merge `8fe959a48c7c97f69367920741932dc075c4adec` makes current identity System and retains the Grok pin as transferred-app provenance only. |
| scan-to-build-system | work/user-intake/README.md | grok-file@4595b4785a2686486e477ce2e70fb3f476285a8d; @985db87a707bd454d7c58419e2cf4d884f00cded; @2d80b5a7b0e7687c425e100bfa0ff3a833166d42 | PROVENANCE — KEEP | System merge `8fe959a48c7c97f69367920741932dc075c4adec` sends current readers to System sources and leaves Grok/roadmap/intake pins as historical provenance. |
