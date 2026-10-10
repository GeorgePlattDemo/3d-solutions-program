# Dimensional Machine Development

**Build the physical capability required by the trial.**

The Scan-to-Build application and reference Store evaluation path already exist. Project 1 carries one identified requirement through a reproduced Store answer into generated virtual commands. The next physical increment is one bounded dimensional-stock machine.

Machine Development establishes whether known tools and controlled stock movement can turn that requirement into inspected components. It supplies the engineering evidence needed before the Bounded-Cell Trial can test an operating service.

## Current candidate machine

The candidate arrangement uses:

- Two servo-controlled manipulating rollers.
- Two fixed-location, miter-capable downstroke saw stations.
- Up to three registered router stations.
- Two registered spot-drill stations.
- A fixed fence and support plane.
- A controlled first-cut workpiece-reference method.
- A local controller, motion hardware, I/O, and risk-derived protective system.
- A bounded machine-specific lowering/compiler.

**The board moves. The stations remain known.** Fixed-location stations may still pivot, plunge, or position their tools within declared travel.

The intended operations are reference establishment, indexing, cutting, bounded face miters, spotting, and routing functions justified by supported work. The full layout is not required for the first specimen. Each additional station or function must earn its place.

Use commercially available industrial components wherever practical. Check compatibility, condition, geometry, modifications, and protective requirements before reusing equipment. Select for performance, diagnostics, maintainability, replacement availability, safety integration, and local technical support.

The [Project 1 review](https://github.com/GeorgePlattDemo/store-zero/blob/main/docs/project-1-digital-trail/D001_Project1_Review.md) identifies the present reference specimen, candidate controller path, and unresolved physical conditions. It is starting material for selection and sizing, not an adopted machine BOM.

## Connect job facts to machine facts

The job carries part identity, material requirements, finished dimensions, feature locations, required operations, orientation, and dependencies. Store supplies its identified material and capability answer.

The validated machine configuration supplies station locations, tool geometry, blade and retained-face relationships, reference transforms, axis directions, travel and motion limits, process parameters, controller mappings, and operating prerequisites.

**Identified job requirements + validated machine configuration → controller-specific instructions.**

The compiler must preserve the required result, reject unsupported or inconsistent inputs, and retain the job and configuration identities. It does not redesign the component, choose Store inventory, or issue physical release. The machine-neutral interface remains a development target to implement and validate against the actual machine.

Specialist work belongs in design, registration, commissioning, validation, and maintenance, so supported jobs can reuse an identified configuration. Changes to tooling, geometry, calibration, mappings, or capability require the applicable updates and checks.

## Establish and validate the reference chain

The fence supplies the lateral reference; the support plane supplies the vertical reference. A controlled cleanup cut is proposed to establish the longitudinal workpiece reference.

That cut becomes usable only after engineering defines the retained face, cleanup allowance, blade and kerf relationship, restraint, and transform to machine coordinates. The rollers must move and hold the board while maintaining a checked relationship between commanded travel and actual stock position.

Drive feedback alone does not establish board position. Address slip, lift, contact loss, stock variation, cutting loads, separation, and interruption. Determine when the workpiece reference remains valid and when it must be re-established.

The chain to validate is:

**Machine references → workpiece reference → controlled stock position → registered tool action → independently inspected component.**

The preserved Project 1 specimen is the first target: two 18-inch parts with parallel face miters and a centered spot on each. Its digital review does not resolve physical stock control, blade-face registration, saw stroke, spot depth, controller execution, recovery, or part conformance. Resolve the identified one-roller states, retained-face/kerf relationship, and saw geometry before using nominal commands physically. The supplied controller source remains uncompiled.

## Development sequence

Each powered test requires an appropriate risk assessment, protective setup, test limits, and responsible authorization.

1. **Establish references and stock control.** Verify fence and support geometry, restraint, roller contact, actual board travel, and reference retention across the sequence.
2. **Validate the saw process.** Establish blade location, miter geometry, stroke, clearance, kerf, reference-cut behavior, and inspected dimensions. Install the saw capability required for the target sequence.
3. **Validate the Project 1 spot operation.** Register the 3/16-inch tool and establish point geometry, position, penetration depth, restraint, and inspection. The reference depth is **3/16 inch of full-diameter penetration beyond the drill point**.
4. **Connect lowering to the controller runtime.** Test the generator and target controller against the configuration, including readiness, admission, interruption, faults, and reference invalidation.
5. **Produce and inspect the components.** Use predetermined acceptance criteria, suitable instruments, repeated specimens, and recorded conditions. Include relevant stock variation; retain discrepancies and failed attempts.
6. **Add capability where needed.** Further spotting, routing, sensing, or automation must answer a demonstrated requirement and pass its own validation.

Controller coordinates are not inspection. Encoder resolution is not finished-part tolerance. Keep measured results separate from commanded or modeled values.

## Handoff to the service trial

Before service testing, responsible parties must accept an identified configuration and capability envelope, validate its protective and operating requirements, establish inspection criteria, and demonstrate the admitted work under authorized conditions.

The handoff records the configuration, admitted material and operations, observed performance, operating and inspection responsibilities, support needs, and remaining restrictions. Store decides what it will offer; System retains job meaning.

Faults, rework, maintenance, and observations from the trial may require further development. A capability change receives a new identified evaluation rather than silently widening the trial.

Machine Development establishes whether the machine can do the admitted work. The [Bounded-Cell Trial](../bounded-cell-trial.md) determines whether doing it this way justifies the service.

*Information before atoms. NO BLOOD ON WOOD.*
