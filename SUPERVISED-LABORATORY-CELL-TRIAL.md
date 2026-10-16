## Supervised Laboratory Dimensional Cell Trial

3D Solutions LLC | Proposed trial | 11 October 2026

### Where we are today

A working application shows several real-world wood projects, each customized through user controls. The definition travels over the web to Store Zero, a modeled test surface: a virtual lumberyard with declared stock, modestly automated machinery and its own economics.

Store evaluates the requested material against its declared SKUs, available stock, supported operations and machine capabilities. The resulting operation sequence accounts for stock handling, positioning, cutting, milling and drilling, with material consumption and modeled machine time forming the basis of budgetary Q.

Store Zero returns modeled time and budgetary Q for that exact definition, together with an ordered operation ledger containing nominal positioning and processing instructions.

Machine functions are registered before the customer arrives: stock envelopes, supported operations, tools, station geometry and motion conventions are identified in advance. The customer defines the required operations and values. System derives the part requirements; Store resolves material and the manufacturing plan; accepted-job lowering binds that verified plan to the registered model. This compilation chain absorbs the modeled job's programming burden: supported requirements determine the ledger without a second person redrawing parts or entering derived coordinates. A requirement Store cannot support receives a refusal or unresolved answer. Proving the genuine accepted-order handoff and reusable controller export remains part of digital completion.

Try it yourself, then examine the audit trail: each answer is tied to the definition revision it answers and to a fresh Store evaluation receipt. In Start Your Own, Accept & Pay records a simulated inbound order and queue entry tied to that revision and its fresh Store answer.

The next step joins digital completion with physical validation. A reusable controller-oriented export must extend the existing accepted-packet and lowering path. Machine development must then carry that same identified job into inspected parts. The central question is whether reusable registration eliminates enough per-order interpretation, programming and handling expense to make the complete service economically viable.

### Purpose of the supervised lab trial

For many small woodworking jobs, arranging the work can cost more than doing it, so the work goes undone. Industry research on distributed production names the same burden: human planning in quoting, and repeated engineering and process-development costs ([Helu et al., NIST, 2020](https://www.nist.gov/publications/industry-review-distributed-production-discrete-manufacturing)). Whether that burden is large enough to matter for a local yard is what this trial measures.

The underlying language and motion-control techniques are established engineering; their application to this bounded machine still requires integration and validation. The economic question is how much useful work a modest, pre-referenced cell can perform before additional capability and its maintenance cost outweigh avoided per-job preparation. Start with one dimensional-stock machine in a supervised laboratory and find the smallest cell that serves a significant share of the woodwork people now avoid.

Before moving a board across the state or country for a few prepared parts, let its definition reach suitable local wood first. Information before atoms.

Test capability against footprint and complete service cost. Add the sheet machine when demand warrants it.

### Why North Carolina

North Carolina is well placed to test whether this path grows local economic capability: it has the wood, the yards, the colleges and the research institutions to find out quickly and openly.

I offer this framework, its patented architecture and software foundation as a basis for institutional stewardship and public benefit. If the will and expertise exist locally, the foundation is here; willing institutions elsewhere can investigate it as well.

The objective is straightforward: determine whether networked preparation, local material and local fabrication provide measurable public value through evidence rather than assumption.

### Where the trial starts

The patents describe familiar tools, controlled stock movement and generated instructions. Project 1 generates virtual commands; its reference controller source remains uncompiled. The application authorizes no physical motion.

Current Store lowering verifies the accepted job and binds its exact stock plan, operation sequence and predicted occupancy to the declared configuration. The present virtual replay checks that modeled ledger; it is not a commissioned controller runtime. The historical Project 1 generator separately produced controller-oriented data. The trial must connect a reusable current-job export to a selected controller, then validate actual machine state and output under qualified technical supervision.

Guarding, stopping, isolation and restart control belong in the build and verification process rather than the current application. **NO BLOOD ON WOOD:** software success, simulated motion and commercial convenience do not resolve physical safety requirements.

The trial separates three activities. **Demand and baseline observation** records requests, customer decisions, existing alternatives and the effort needed to clarify and prepare comparable work; it can begin before a physical cell exists. **Engineering validation** establishes references, stock control, tool processes, controller behavior and inspected specimens for a declared capability. **Bounded service testing** observes actual requests beside real stock, using only capability released for the test.

Before testing, record the following. Undecided items stay marked unresolved, and no customer processing begins until the applicable conditions are met.

- Admitted stock classes, dimensions, conditions and operations.
- The machine configuration and the operating release that applies to it.
- Responsible operating, inspection and test-approval roles.
- Component acceptance criteria and inspection methods, set before testing.
- Stop conditions, and what happens to interrupted or nonconforming work.
- Budget and test duration, and the evidence that will justify proceeding, revising or stopping.
- Customer terms: whether the work is paid, subsidized or experimental.
- Record custody, participant permissions and what may be published.

Requests outside the boundary remain evidence. Refuse, redirect or record them; do not silently expand the machine to absorb them.

### Educational and research value

Participants can learn basic robotics through encoder counts, board movement, tool coordinates and sensed conditions. Qualified technical staff lead integration and powered testing.

The trial measures capability, preparation burden, occupied space and complete service cost. The goal is to create evidence useful to engineering, workforce development, manufacturing and public-interest evaluation.

### Build and verify the dimensional machine

**The board moves. The stations remain known.** Fixed-location stations may still pivot, plunge or position their tools within declared travel. The full layout is not required for the first specimen; each additional station or function must earn its place.

| Element            | Count   | Proposed arrangement                                                                                                                                                                                                      |
| ------------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Feed and restraint | 2       | Servo-driven manipulating rollers, with clamping rollers, a fixed fence and a firm support plane.                                                                                                                         |
| Saw stations       | 2       | Fixed-location, miter-capable downstroke saws with registered blade faces, angle range, stroke and clearance.                                                                                                             |
| Router stations    | Up to 3 | Heads with the stiffness and travel appropriate to their assigned work; qualify each separately.                                                                                                                          |
| Spot station       | 1       | The minimum trial configuration: a 3/16-inch tool with defined location and 3/16-inch full-diameter penetration beyond the point. A second station is added only if measured requirements justify its footprint and cost. |
| Base and supports  | 1       | Rigid base, idler rollers and infeed and outfeed support for the admitted stock lengths.                                                                                                                                  |
| Local controls     | 1       | Controller, drives, I/O, actual position feedback, tool and restraint sensing, a risk-derived protective system, guarding and extraction.                                                                                 |

Use commercially available industrial components wherever practical. [IEC 61131-3 Structured Text](https://webstore.iec.ch/en/publication/68533), [PLCopen motion function blocks and state models](https://www.plcopen.org/standards/motion-control/), and [TwinCAT PLC/NC point-to-point axis interfaces and EtherCAT](https://www.beckhoff.com/en-us/products/automation/twincat/tcxxxx-twincat-3-base/tc1250.html) provide established foundations consistent with Project 1's reference.

[FreeCAD CAM/postprocessing](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/CAM_Workbench.md), [LinuxCNC instruction/coordinate interpretation](https://linuxcnc.org/docs/html/gcode/coordinates.html), and [grblHAL hardware abstraction](https://github.com/grblHAL/core) are researched alternatives, not installed dependencies. [OPC UA machine-tool information](https://reference.opcfoundation.org/specs/OPC-40501-1/1.1) is a candidate for identified job/status exchange, not the motion loop. Select equipment for performance, diagnostics, maintainability, compatibility, protective requirements and local support. Project 1 remains selection and sizing evidence, not an adopted machine bill of materials.

**Establish the layout.** Treat 5 feet wide by 3 feet deep as the core-machine target. Check a dimensioned layout through every tool movement. Record the complete operating space, including stock travel, supports, guarding, extraction and access. The two feed servos are only part of the actuator count; saw and tool positioning also require the appropriate drives and feedback.

**Control the cost.** Use compatible laboratory equipment and donated or standard components where practical. Set a cash ceiling before procurement. Record purchased items, contributed equipment, fabrication, control licenses, protective equipment and integration hours. A low purchase bill and a low replacement or operating cost are separate results.

Include operator labor, maintenance, downtime, inspection and waste; value contributed equipment separately at replacement cost.

### Complete the registered path to inspected parts

**Translate the definition.** Extend the existing lowering architecture: **accepted job → verified Store plan → registered machine configuration → lowering layer → controller instructions**. System supplies the meaning, geometry, independent manifest and revision; Store has already selected stock and generated the priced plan. The exporter must consume that exact plan, retain packet/receipt/calculation, parent/SKU, component/feature and configuration identities, and add only registered local execution facts. It must not redesign components, select stock, reschedule the accepted plan or compute another time/Q. Missing station, tool, axis, units, datum or required controller parameters produce an identified unresolved condition or refusal.

Register each function's operands, tooling, geometry, units, references, capability limits, preconditions and allowed outcomes. A clamp allowance does not become sensed clamp confirmation; a nominal reference event does not become an inspected retained face. The current model's linear C coordinate must map explicitly to a continuous longitudinal axis and workpiece offset, not to a conventional rotary G-code C axis. Keep reference instruction data, compiled controller code and executed runtime evidence distinct. Exercise the selected controller's cyclic function calls, Execute transitions and terminal outcomes before powered cutting. Specialist work belongs in registration, qualification, commissioning and maintenance, so supported orders reuse the mappings.

Bind each test to its job revision, Store evaluation receipt and machine configuration, and preserve those identities, with the part and feature identities and the observed execution, through the entire sequence. Recheck the mapping after a change.

**Validate the physical state.** The fence establishes Datum A (lateral reference); the support plane establishes Datum B (vertical reference). A controlled cleanup cut is proposed to establish Datum C, the longitudinal origin of each workpiece; it becomes usable only after engineering defines the retained face, cleanup allowance, blade and kerf relationship, restraint, and transform to machine coordinates. Track actual longitudinal board movement against its reference: drive rotation or drive feedback alone cannot establish that a board has not slipped. Address slip, lift, contact loss, stock variation, cutting loads, separation and interruption. Verify contact and restraint at every working position and maintain a checked position relationship. A disturbance that can move the stock invalidates Datum C until the longitudinal reference is re-established.

The chain to validate: **machine references → workpiece reference → controlled stock position → registered tool action → independently inspected component.**

The Project 1 review identifies one-roller states, unresolved face and kerf registration, and unverified saw-stroke geometry. Resolve these specific gaps through layout, sensing and measured tests before nominal commands are used physically; the supplied controller source remains uncompiled.

**Prove useful output.** Use the current two-part SPF Job 1 default and its variation as paired specimens, each with the same eight-inch horizontal span:

| Requirement/result | 16-inch default | 18-inch variation |
| --- | ---: | ---: |
| Face-miter magnitude | 30° | 26.387799961243° |
| Centered spot X | 8 in | 9 in |
| Selected parent | 60 in | 72 in |
| Modeled manufacturing Q | $8.62 | $9.13 |

The [Store walkthrough](https://github.com/GeorgePlattDemo/store-zero/blob/main/STORE-ZERO-MASTER.md#82-start-your-own) supplies their complete identified ledger, kerf convention, positions and timing. The current Project 1 review and full reference proof regenerate both SPF settings, and required System browser checks carry their actual accepted records into Store lowering/replay. The original 18-inch treated-lumber publication retains its own $11.09 calculation and 45-command source reference as provenance.

Inspect length, angle, spot location and full-diameter depth against predetermined criteria using suitable instruments, repeated specimens and recorded stock conditions. Demonstrate that changing only the admitted customer value produces a new identified definition, fresh Store result and regenerated instructions without manual angle or coordinate re-entry. Compare actual dimensions and whole-job effort with modeled results. Controller targets and encoder counts are not component inspection.

Exercise changes and repeated specimens, then qualify routing and further dimensional jobs individually. Record actual versus modeled time, interruptions, rework and inspected results. Keep actual execution distinct from the application’s simulated fulfillment.

**Development sequence.** Each powered test requires an appropriate risk assessment, protective setup, test limits and responsible authorization.

1. **Establish references and stock control.** Verify fence and support geometry, restraint, roller contact, actual board travel and reference retention across the sequence.
2. **Validate the saw process.** Establish blade location, miter geometry, stroke, clearance, kerf, reference-cut behavior and inspected dimensions.
3. **Validate the spot operation.** Register the 3/16-inch tool and establish point geometry, position, penetration depth, restraint and inspection. The reference depth is 3/16 inch of full-diameter penetration beyond the drill point.
4. **Connect lowering to the controller runtime.** Test the generator and target controller against the configuration, including readiness, admission, interruption, faults and reference invalidation.
5. **Produce and inspect the components.** Use predetermined acceptance criteria, suitable instruments and repeated specimens, include relevant stock variation, and retain discrepancies and failed attempts.
6. **Add capability where needed.** Further spotting, routing, sensing or automation must answer a demonstrated requirement and pass its own validation. Preserve refused demand and compare separately registered hypothetical configurations through deterministic compilation/Store, including added feasible work and complete cost. A third or fourth machine extends capability registration and mappings without rebuilding the customer-definition compiler; capability-impact analysis is a core successor requirement.

**Handoff to the service trial.** Before service testing, responsible parties accept an identified configuration and capability envelope, validate its protective and operating requirements, set inspection criteria and demonstrate the admitted work under authorized conditions. The handoff records the configuration, admitted material and operations, observed performance, operating and inspection responsibilities, support needs and remaining restrictions. A capability change receives a new identified evaluation rather than silently widening the trial.

### Supervised laboratory service

After the admitted work is demonstrated, offer free preparation to participants through an approved operator and a bounded intake process. Participants may bring wood that passes the laboratory’s material inspection and capability limits. Record material identity, actual dimensions and material condition as supplied material; it is not a fictitious purchase from Store inventory. Include unsupported requests and customers who do not proceed.

Measure real-world usefulness: clarification effort, machine loading, processing effort, inspection burden, handoff effort, waste and customer support. Compare the same result against an existing manual or shop service.

Free uptake establishes interest and operating experience. Willingness to pay requires a separate test.

### Extension to one local yard

Bring one willing local yard into the next stage using its own stock, actual offered prices, measured labor and measured utilization. Test the laboratory process under real yard conditions. The laboratory tests supervised preparation, including qualified participant-supplied wood; the yard trial establishes economics with the yard’s own inventory, actual costs, offered prices and observed utilization. That is where the experiment becomes a test of a business proposition.

### Evidence and evaluation

Student studies should examine economics, stewardship and continuity with input from:

- **Forestry organizations:** local wood supply, resource use and retained value.
- **NC Commerce and workforce boards:** additional jobs, job quality and public spending outcomes.
- **Community college instructors:** robotics teaching, practical skills and supervised laboratory work.
- **UNC faculty and research teams:** validation, research methods and continuity between student teams.
- **NC State Extension and NCMEP:** engineering, service economics and practical business trials.
- **Lumberyards, operators and customers:** real requests, operating constraints and evidence of what people will pay.

Ask where public money goes, which costs remain subsidized, and what additional paid work or local income the trial produces compared with the existing service. Report refused, failed and abandoned requests alongside successful jobs.

**Observe the whole job.** Keep an identifiable record for each qualifying request: its definition revision, Store inquiry and answer, disposition and resulting work. Distinguish technical failures, customer decisions and Store refusals.

| Measure         | What to record                                                                                                 |
| --------------- | -------------------------------------------------------------------------------------------------------------- |
| Demand          | Request counts and types; supported, refused, redirected, deferred and abandoned outcomes; known reasons.      |
| Preparation     | Clarification, measurement, drawing, re-entry, estimating, programming, revision and customer communication.   |
| Material        | Parent stock, consumption, kerf, returned remnants, damage, scrap and replacement material.                    |
| Operations      | Loading, setup, handling, machine occupancy, inspection, labeling, staging and handoff.                        |
| Reliability     | Faults, interventions, interrupted work, recovery, rework, rejected parts and downtime.                        |
| Support         | Tooling, maintenance, cleaning, calibration, troubleshooting and required skills.                              |
| Economics       | Actual receipts and costs, operator occupancy, installed investment, space, software and observed utilization. |
| Customer result | Inspection disposition, receipt and response, price offered and whether the customer proceeded.                |

Separate observations from estimates and allocations, count failed and refused attempts as well as completed jobs, and record shared operating time consistently so costs are neither omitted nor counted twice. Compare realistic alternatives for the same required result: an existing saw service, manual preparation, a local shop, a standard product, another supplier, repair or refusal. Additional demand is different from improved service. A customer’s reason for starting or abandoning a project is not proof of what would otherwise have happened, and interest and modeled prices are not completed purchases.

**Decide from the evidence.** Before interpreting results, state the comparison and the economic go/no-go criteria: required component performance, acceptable service burden, the business’s margin or return requirement, and the evidence needed to continue. Record and explain any later change to those criteria. The trial should establish:

- Which requests fit, and how frequently they occur.
- Where reconstruction effort is removed, shifted or newly introduced.
- Whether inspected components satisfy the identified requirements.
- Whether customers value the result enough to proceed on the stated terms.
- Whether the complete service justifies material, labor, equipment, maintenance, space and operating burden at realistic utilization.
- Where another solution remains better.

A useful negative identifies the demand limit, cost, technical constraint or better alternative, and the trial must not expand merely to avoid that result. Evidence may justify continuing, narrowing, changing or stopping.

### Who owns what

**Program investigates and records why. System defines what the job means. Store determines what the identified Store can provide.** A document that discusses another owner’s work gains no authority over it. Shared terms are defined once in [System’s definitions](https://github.com/GeorgePlattDemo/new-system/blob/main/docs/DEFINITIONS.md).

| Owner                        | Owns                                                                                                                                                                 | Boundary                                                                                                 |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Program                      | Research questions, evidence, experiments, candidate engineering, machine development, economic and operating research, findings and development decisions.          | Proposals and findings do not change System behavior, Store capability or physical operating permission. |
| System                       | The application, project definitions, shared operational meaning, job records and revisions, custody, and the interfaces carrying the job to Store.                  | It preserves and presents Store answers without creating substitute facts, prices or capability.         |
| Store                        | Its material, catalog, represented stock, admitted capability, modeled work and time, economics, answers and refusals.                                               | It answers the definition without changing the requested component to make the job fit.                  |
| Local machine implementation | Commissioned geometry, tools, reference validity, controller/I/O mappings, physical adaptation of the existing lowering path, motion, interlocks, calibration and observed results. | Adds execution facts to the accepted Store plan; owns no second project compiler, stock planner or Q. |

The chain is **customer operations/values → System geometry/features/manifest → Store stock/capability/plan/time/Q → customer decision and accepted packet → registered configuration and verified lowering → virtual instructions and evidence → commissioned controller execution and inspected result**. The first stages are implemented digital functions; current machine evidence is modeled; reusable controller export and physical execution remain development and validation work. No later stage backfills missing authority. A changed definition requires a fresh Store evaluation, and a changed tool, station, datum or mapping requires a new identified configuration and corresponding checks.

Project 1 is the living end-to-end proof of the current System/Store. Code, specification, machine-model or catalog changes require corresponding current proof and operative-document reconciliation. Original sealed source records retain their identities and provenance; they cannot substitute for the current proof. Research use or publication of customer and business records requires permission for that purpose, and project participation does not itself authorize unrelated reuse.

### Institutional stewardship and continuity

Public benefit and institutional stewardship take priority; personal financial gain is secondary. If developed as a UNC project, agreed faculty guidance and a documented handover could support continuity beyond any single participant. The objective is durable institutional knowledge rather than dependence on any individual contributor.

### Findings and next steps

**In-network testing.** Make each commissioned cell approachable through the same application, first in the laboratory and then at one local yard. Verify that the identified request:

1. Reaches registered equipment without re-entry.
2. Executes through approved machine controls.
3. Produces inspected results.
4. Returns those results to its originating record.

The definition, evaluation and occupancy-evidence path exists. Required current System Chromium checks prove the actual published acceptance-to-packet/Store lowering handoff for both SPF settings and publish revision-bound evidence. Remaining digital validation requires provenance-complete controller export and target-runtime behavior. Local readiness, operator Cycle Start and inspected fulfillment then require separate physical evidence at each commissioned connection.

**Positive and negative findings.** A well-supported negative finding is as valuable as a positive one. Either outcome gives the state an empirical answer about local yards, retained income and public value. The objective is not to prove success, but to determine whether local preparation, local material and networked fabrication produce measurable value worth carrying forward.

**Source basis:** System definitions | current verification | Store specification | lowering code | Project 1 review sections 9 to 13 | US 9720401 B2 | US 10768609 B2 | Beckhoff motion block rules | OSHA woodworking guidance | [Program evidence record](https://github.com/GeorgePlattDemo/3d-solutions-program/blob/main/EVIDENCE.md)