# Program work instructions

Read README.md, governance/authority.md, governance/change-gates.md and migration/README.md before making organizational changes.

Program, System and Store stand on their own. Do not link to `scan-to-build-review` or the original `Scan-to-Build`; cite them only as plain-text provenance (repo@commit). They are frozen history. System owns application behavior and canonical shared operational definitions; Store owns its actual Store facts/evaluation/economics; Program owns research, experiments, evidence, reviewed decisions/adoption records, partnership/economic/business work, and migration/retirement records.

Do not bulk-import donor repositories, transcripts or rejected proposals. Use the inventory to find existing copies, then inspect meaningful differences. Record what is retained, migrated, superseded or excluded and why. A matching blob is not deletion authorization. Read branch-only work before clearing a repository for retirement.

This repository is public. No new private folders are requested. Review source content before publishing it; preserve licenses and attribution. Do not infer a new software license from publication.

Use a bounded branch/PR after bootstrap. Run python3 tools/check_program.py. Report exact commits and distinguish local verification, hosted CI, acceptance and deployment. Do not claim branch protection or mandatory CI without verified settings. Never promote candidate engineering into admitted Store capability through a documentation move.

**Protected path — do not touch.** The live app in `scan-to-build-system` reaches the hosted Store on Railway at the exact Store commit owned by System's `STORE_PIN` in `scan-to-build-system/apps/stb/shared/contracts.mjs`. Program does not restate or change that pin, the Railway endpoint, or any Railway setting. See the "Protected path" section of System's `AGENTS.md`. If a task seems to require it, stop and ask.

**Definitions.** Shared terms are defined once, in System `docs/definitions/README.md`. Program may propose a change in meaning; it does not define shared terms here.