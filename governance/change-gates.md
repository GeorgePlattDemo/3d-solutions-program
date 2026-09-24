# Ordered change gates

Use one bounded branch/PR per owning change. Link dependent PRs. A commit is a recoverable checkpoint; acceptance, deployment and physical commissioning are separate events.

| Gate | Required result |
| --- | --- |
| 0 — Scope and owner | State the problem, intended result, owning home and preserved behavior. Identify exact before-state. |
| 1 — Source and disposition | Read the source. Record source commit/path, current status and the reason to retain, migrate, supersede or exclude it. Check branch-only work and incoming references. |
| 2 — Candidate | Make the smallest coherent change on a branch. Keep documentation relocation separate from behavior changes. Preserve working demonstrations and source attribution. |
| 3 — Verification | Check links and content for documents. For behavior, exercise actual producer/consumer paths, negative cases and preservation regressions. Record failures and coverage limits. |
| 4 — Review and acceptance | Review the exact candidate diff and evidence. Resolve discrepancies. Merge only the identified candidate; do not describe local checks as hosted CI or branch protection. |
| 5 — Publication/adoption | Publish the accepted document or deploy the compatible application/Store versions. Record exact versions and verify the entry links or actual user path. |
| 6 — Retirement | Reconcile unique content, branches, open issues/PRs, references and deployment dependencies. Retain necessary provenance outside the active workspace. Archive before considering permanent deletion. |

## Migration dispositions

- **Retain here:** belongs to its existing owner and remains useful.
- **Migrate:** selected useful content has an identified destination and checked transformation.
- **Exact duplicate:** identical Git blob exists at a recorded destination; authority still requires review.
- **Superseded/exclude from active record:** record the reason and replacement, if any. Do not import the discarded body merely to preserve every thought.
- **Review required:** insufficient evidence for the decision; not deletion clearance.

## Dependencies

A documentation-only organization change does not require unrelated software rewrites. A change to Store capability is tested in Store, then against the consuming System adapter, then through the visible Review application before any visible-completion claim. Existing pins are not bulk-replaced during housekeeping.

The same rule applies to temporary repositories: moving a README is not migration of a runtime dependency.

## Enforcement status

The Program check validates local documentary links and structural evidence in the migration record. Its workflow runs on pushes and pull requests. It does not determine whether a research conclusion is correct or whether a public disclosure is appropriate.

Repository branch protection/rulesets have not been established or verified in this pass. Thus the check is automated validation, not yet a technically mandatory merge gate. Human review remains necessary. Do not advertise organization-wide enforcement until the corresponding repository settings and checks have been verified.

Bootstrap exception: the empty Program repository requires an initial main-branch commit. Subsequent organizational content is presented as a branch and pull request under these gates.
