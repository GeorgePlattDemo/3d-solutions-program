# Machine-site convergence — retained research questions

**Source:** `GeorgePlattDemo/scan-to-build-governed-reference`, branch `docs/store-s1-boundaries`, commit `f3a7ba4f35bd3abf0669e3aa15ce5a4af4455ec7`, original path `docs/planned/machine-site-convergence-0.1.md`.  
**Status:** Program research. Not Store capability, not System behavior, not a machine program, and not production authority.

## Why this material is retained

The historical PR contained three proposed documents. The Store-reference-node contract and S1 build plan were written for an ownership model that has since changed: current Store and System repositories now own those implementation concerns. They should not become a second current Store plan.

The machine-site convergence note is different. It identifies still-open engineering questions at the boundary between a resolved definition and a future commissioned machine. Those questions are not answered merely by the current application or Store implementation.

This page retains the research problem while stripping historical fixture-specific claims and unactivated pseudo-contract language.

## Research proposition

A resolved part definition does not become physical work merely by reaching a Store answer.

A future machine-site implementation must reconcile at least:

- the exact identified project/WorkPacket version;
- material and physical-stock identity at an explicitly chosen granularity;
- the actual machine/cell identity and family;
- the admitted operation set and its physical meaning;
- machine envelope and reachability;
- installed tooling and tool geometry;
- fixture/workholding identity;
- datums and current zeroing evidence;
- tool, fixture, wear, and kerf offsets where applicable;
- controller dialect/revision;
- one registered machine-specific lowering/postprocessor path;
- current calibration, readiness, interlock, workholding, and operator-authority evidence;
- the authority applicable to the particular stage.

Missing required evidence must stop the applicable stage. It must not be invented because upstream information is otherwise complete.

## State separation to preserve

A future machine path should keep these states distinct:

1. process/time estimate;
2. non-executable machine-site candidate;
3. candidate validation against identified machine/site bindings;
4. release for controller loading;
5. controller acceptance;
6. authorized physical execution;
7. recorded physical outcome.

No earlier state implies a later one.

In particular:

- candidate generation is not loading release;
- loading release is not controller acceptance;
- controller acceptance is not production authorization;
- production authorization is not proof of successful execution;
- recorded outcome cannot retroactively manufacture prior authority.

## Frames and references

The original note correctly identifies coordinate binding as a core engineering problem. A later bounded machine definition should make explicit which frames exist and how they relate, for example:

- project/opening;
- part;
- stock;
- workpiece;
- fixture;
- machine;
- tool;
- actuator/joint.

Important retained distinction:

**A data origin is not physical zeroing evidence.**

A machine-side transform must be supported by the applicable physical reference, fixture, tool, offset, calibration, and current-state evidence. Patent letters or drawing labels are informative aliases, not runtime datums.

## Kerf, finished size, and physical operations

Finished geometry requires tool geometry to be part of the machine-side calculation. Kerf, tool diameter/profile, approach/retract space, and applicable allowance cannot be treated as convenient constants when they materially affect the finished part.

A simulation-operation identifier is not automatically a physical cutting act. Before controller-specific lowering exists, a bounded machine definition must assign physical semantics to the accepted neutral operation.

This prevents a dangerous shortcut:

`operation name → guessed cut count → controller command`

The intended chain is closer to:

`identified part requirement → neutral bounded operation → commissioned machine definition + current bindings → validated machine-specific candidate → separately released/authorized execution`

## Work-to-tool versus tool-to-work

Different machine families can realize the same finished requirement using different kinematics.

A dimensional cell may bring stock to known fixed tool locations. A sheet machine may move a tool over registered stock. Those are not interchangeable assumptions.

A future machine definition therefore needs an explicit kinematic model. Store capability or a neutral operation name cannot silently select the kinematic.

## Envelope as a predicate

Part dimensions fitting inside a nominal work area are not sufficient evidence of physical reachability.

Future machine validation should consider, at minimum, whether the complete required motion is valid for:

- approach;
- workholding/clamp state;
- cutting/tool occupation;
- retract/clearance;
- applicable tool and fixture geometry;
- applicable interlocks and stopping conditions.

The exact predicate and evidence are unresolved research subjects. This page does not declare a commissioned envelope.

## One lowering path

Retain the architectural rule that:

- the application does not generate controller-specific instructions;
- the Store does not generate controller-specific instructions;
- machine-specific lowering occurs at the machine-development/site boundary;
- a controller dialect/revision and postprocessor identity/version are explicit bindings.

“Two generators cross-check each other” is not independent validation if both embody the same transformation assumptions. Regeneration creates a new candidate version; it is not proof.

## Safety and live motion

Remote live motion from the customer application or Store remains outside the intended architecture.

Machine-site placement alone does not create authority. Local candidate generation, loading, Cycle Start, execution, and outcome evidence remain separately controlled.

**NO BLOOD ON WOOD.**

## Open research questions

The original note leaves several questions that still merit explicit experimental resolution:

- What neutral machine-side IR, if any, is needed between accepted operations and controller-specific lowering?
- What is the source of truth for kerf/tool geometry by station and tool state?
- At what granularity is physical stock identified: lot, bundle, board/sheet, or individual blank?
- What evidence proves that the physical stock corresponds to the digital material/stock record?
- What constitutes current zeroing evidence for hard-stop, switch, probe, or other reference methods?
- What is the commissioning and compatibility process for controller dialect/revision?
- Who owns and signs/version-controls the registered postprocessor?
- What evidence is required for current tooling, offsets, calibration, workholding, interlocks, and operator authority?
- How are path reachability, frame transforms, concurrency, safe stopping, and fault recovery validated?
- Which checks belong to candidate validation, loading release, controller acceptance, and production authorization respectively?
- What outcome evidence is needed to compare intended geometry, machine execution, inspection, and staged/pickup result?
- How does a commissioned cell improve its models from measured outcomes without silently changing an accepted capability contract?

## What was deliberately not retained as current authority

The source note included synthetic Sarah fixture values, historical M1/S1 milestone language, current-node identifiers, and illustrative path classes/sequences.

Those may remain useful evidence in the source repository, but they are not promoted here as:

- current Store capability;
- commissioned machine geometry;
- a controller program;
- physical work instructions;
- a production authorization scheme;
- proof of patent practice;
- a requirement to activate any particular machine design.

The Program should turn these research questions into bounded experiments. Only reviewed experimental evidence should later change Store capability or machine-development contracts.
