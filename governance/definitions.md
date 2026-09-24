# Canonical definitions and semantic boundaries

**Status:** Program authority for cross-repository terminology.  
**Owner:** `3d-solutions-program`.  
**Applies to:** Scan-to-Build Program, System, Store, and material admitted from retired donor repositories.

This page is the common vocabulary contract for the working program. It exists so the application, Store, research record, and later machine-development work cannot use the same word to mean materially different things without an explicit qualified term.

It is not a runtime schema, a machine controller, a Store capability declaration, a commercial contract, or an authorization issuer. A documentation change here does not silently alter deployed behavior. When a current implementation conflicts with this page, the conflict is a reconciliation defect to be resolved in the owning repository.

## 1. Precedence and ownership

For **shared cross-repository terms**, this page controls meaning.

System and Store may define implementation-specific or owner-specific terms that are not defined here. They may add narrower qualifiers, but they shall not silently change a shared meaning.

If a durable wire identifier or existing type name cannot be renamed without breaking compatibility, preserve the identifier and document its qualified meaning. Compatibility is not permission to collapse semantic boundaries.

Implementation ownership remains separate:

- **Program** owns shared definitions, governance, research questions, evidence, and reviewed program decisions.
- **System** owns application behavior, project journeys, application records, adapters, shared implementation contracts, and application tests.
- **Store** owns material/offering resolution, stock facts, admitted capability, modeled work/time, economics, fulfillment facts, Store answers, and Store tests.
- A future commissioned machine/controller implementation owns local machine configuration, controller-specific lowering, physical readiness, and execution evidence within its accepted boundary.

A Program definition cannot manufacture Store capability, application implementation, inventory, price, machine readiness, commercial assent, or physical authority.

## 2. Source reconciliation basis

This page consolidates still-valid semantic material from these sources:

- Governed Reference `18949f163718a937f072f4be3a654bb303e53160`, especially `specs/STB-REF-0.2.5.md` status and object contracts.
- Grok semantic-boundary source `4595b4785a2686486e477ce2e70fb3f476285a8d`, `docs/architecture/STB-SEMANTIC-BOUNDARIES-0.1.md`.
- Store `1f9f1a217d91686ef21848508b20e605e7cc6bc1`, `DEFINITIONS.md`.
- System `5c07833f4547e68a80770488a47f86154e091e74`, including `apps/stb/shared/definition-contract.mjs` and `docs/application/SEMANTIC-GUARDRAILS.md`.

Those repositories remain evidence/provenance for their exact historical versions. This page is the intended continuing semantic home for the shared meanings selected here.

## 3. Foundational words

**Need** — Something a person wants changed, supplied, repaired, made, learned, or resolved. A need does not require a known product or SKU.

**Intent** — What the person is trying to make true in a particular situation.

**Requirement** — A condition that must be satisfied for the applicable result.

**Constraint** — A condition that limits possible solutions.

**Preference** — A desired condition that is not automatically mandatory.

**Definition** — An attributable description of what is being required, selected, derived, or resolved. Always qualify the kind of definition when ambiguity would matter.

**Project definition** — Plain-language umbrella for the information describing what is wanted and what it must satisfy. It is not, by itself, a new canonical runtime object.

**Selection** — A choice deliberately made by an actor entitled to make it. Selection is not verification.

**Confirmation** — Explicit acknowledgment of information or a choice. Confirmation does not automatically establish physical truth, commercial assent, Store acceptance, payment, fabrication authority, or machine readiness.

**Unresolved** — Information or a determination required for the applicable boundary remains unknown, unverified, disputed, stale, unavailable, refused, or otherwise incomplete.

**Defer** — Stop the present decision because something required is not yet sufficient.

**Refuse** — Explicit negative result because a request exceeds an applicable rule, material, capability, authority, or safety boundary. A correct refusal is a complete system outcome.

## 4. Evidence, observation, and truth state

**Capture** — Acquisition of project or site evidence using an identified method.

**Scan** — A capture method. A scan is not automatically a verified measurement or fabrication definition.

**Measurement** — A value produced by a stated measurement process. Numerical form does not make it exact truth.

**Observation** — A measured or document-derived result with provenance and status. An observation is not automatically verified.

**Verified** — Established through an applicable verification act by an actor or process with the required authority and method.

**Accuracy** — Closeness to the applicable reference or accepted value.

**Precision / repeatability** — Closeness of repeated results to one another. Precision is not accuracy.

**Uncertainty** — Doubt associated with a measurement result. It is not a generic confidence score.

**Evidence** — Attributable information used to support or limit a claim. Evidence must retain what it established and, when material, what it did not establish.

**Inference** — A derived proposition. Inference is not observation or verification.

**Calculated** — Produced through an identified rule or procedure from stated inputs. Calculation does not confer verification or authority.

### Assertion status dimensions

Consequential assertions may require separate dimensions for source, derivation, environment, verification, certification, selection, authorization, execution, lifecycle, dispute, and knowledge state. These dimensions are not one interchangeable status.

In particular:

- source/basis is not verification;
- verification is not certification;
- selection is not authorization;
- authorization is not execution;
- execution is not proof that the underlying definition was correct;
- lifecycle is not authority;
- simulation environment is not production environment.

The historical Governed Reference `AssertionStatus` model remains the source basis for this separation until a reviewed successor is adopted.

## 5. Core governed objects

These are semantic meanings. Current schemas and implementation details remain owned by their implementing repository.

**DeclaredRecord** — Preserves a person's declared interest or intent without replacing the original language with system interpretation.

**ClassHypothesis** — Proposed project classification. It does not replace the declaration, and acceptance of a class is not verification.

**ProjectInstance** — Governed project record binding the applicable project information and lifecycle. A project does not require that every fact already be resolved.

**ObservationSet** — Structured result of a capture method containing observations, coverage, unresolved conditions, and status.

**MaterialClass** — Material identity layer describing what the material is independently of a merchant SKU.

**MaterialSpec** — Material specified for a particular use and form. It is not a merchant SKU.

**OfferingRecord** — Merchant/location/channel representation of an offered material or product.

**InventoryAssertion** — Time-bounded assertion about quantity or availability. Stale inventory is not current fulfillment truth.

**CapabilityCard** — Holder-declared capability, limits, prerequisites, and refusals. It is not availability, quotation, readiness, certification, or execution authorization.

**MachineEnvelope** — Versioned representation of allowed/refused machine operations and limits for an identified machine, cell, or fixture context. It is not proof of commissioning or readiness.

**GateResult** — Structured result of a named rule evaluation. Governed outcomes remain distinct from Store dispositions and commercial decisions.

**RefusalRecord** — Preserved structured refusal, basis, affected scope, and next act.

**WorkPacket** — Versioned governed description of the work definition that may travel downstream. A WorkPacket is not a machine program and does not authorize machine motion.

**SimulationAuthorization** — Authorization for a specified simulation context only.

**ProductionExecutionAuthorization** — Production authority type. It is not issued merely because a packet, Store answer, simulation, or machine program exists.

**SimulatedExecutionEvent** — Record that simulated execution occurred. It does not establish physical fabrication, commissioned capability, dimensional accuracy, operator competence, or production readiness.

**ResolutionRecord** — Record of how an inquiry or project resolved.

**OutcomeRecord** — Preserved result including what changed and what remains unresolved.

## 6. Definition-contract vocabulary

The current System minimum definition contract uses a small closed vocabulary. Program controls the shared meaning; System owns the executable module and tests.

### Responsibility status

**CANDIDATE** — Proposed value or answer not yet established at the applicable boundary.

**CONFIRMED** — Value affirmatively established by the responsible actor for the applicable definition context. It is not a universal verification, Store acceptance, or physical authorization.

**DERIVED** — Value produced by an identified rule from stated inputs.

**UNRESOLVED** — Required value remains unresolved.

**DEFERRED** — Responsibility intentionally held for a later boundary or qualified resolver.

**NOT_REQUIRED** — Responsibility does not apply to the identified definition/boundary.

Status and owner are orthogonal. `STORE_OWNED` is not a status.

### Responsibility owner

**USER** — Holder/user supplies or confirms the responsibility.

**PROJECT** — Project definition itself supplies the value through its identified facts.

**RULE** — Identified deterministic rule derives the value.

**STORE** — Store owns the answer.

**QUALIFIED_PERSON** — A qualified human authority owns the determination.

**GOVERNED** — A governed rule/authority owns the determination.

Ownership does not make an unresolved value resolved.

### Boundaries

**DEFINITION** — Minimum boundary at which the project definition is sufficiently accounted for under the applicable project rules.

**STORE_SUBMISSION** — Boundary at which the identified project/revision can truthfully ask the Store the bounded question it owns.

**PHYSICAL_RELEASE** — Boundary for any later physical release/production authority. It is not currently satisfied merely by reaching Store-submission readiness.

Store-owned unresolved information can be the reason to ask Store; it does not automatically block Store submission unless that unresolved fact is also required to complete the project definition itself.

## 7. Application review terminology

**DefinitionReviewRecorded** — Application record that the user reviewed an exact definition and acknowledged the displayed Store information, disclosures, and unresolved conditions applicable to that review.

It is not:

- commercial submission;
- purchase;
- Store acceptance;
- payment;
- reservation;
- governed authorization;
- production authorization;
- machine readiness;
- Cycle Start.

**UnresolvedDefinitionAcknowledged** — Record that the user acknowledged an incomplete, refused, unavailable, or otherwise unresolved disclosed state. It is not a finding that the condition has been resolved or supported.

A prior review becomes historical when the consequential definition, revision, Store basis, disclosures, replacement state, or import context changes.

## 8. Store and commerce terminology

**Store inquiry** — Bounded question asking what a Store can truthfully report about material, offering, stock, supply route, fulfillment, capability, modeled work, or economics.

**Store response** — Attributable Store answer containing its applicable facts, limits, freshness, provenance, and unresolved conditions.

**Store evaluation** — Comparison of a bounded project requirement against applicable Store facts.

**SUPPORTABLE** — Favorable Store result under the exact implemented Store checks and supplied scope. It is not comprehensive physical approval, governed acceptance, machine authorization, commercial acceptance, or proof that every possible limit has been checked.

**UNRESOLVED / REFUSED / UNAVAILABLE** — Distinct Store dispositions. Do not collapse them into one generic failure state.

**Store accept** — If retained as a Store-local term, means only that represented Store facts support the applicable next governed step. It is not governed authorization or commercial assent.

**Store defer** — Store-side result indicating required Store information or capability is insufficient at present.

**Store refusal** — Store-side result indicating the request lies outside a declared Store boundary.

**BudgetaryEstimate / Q** — Store-issued budgetary result under the identified model and inputs. It is not automatically a legal quotation, payable total, reservation, or proof of support.

**Price observation** — Price reported or observed from an identified source and time. Not automatically a binding quote.

**Estimate** — Calculated or informed expectation. Not automatically binding.

**Quote** — Commercial offer under stated scope, price, validity, terms, and responsible seller. Legal effect depends on applicable terms and law; an application event does not decide contract formation by vocabulary alone.

**Reservation / allocation** — Commercial commitment holding specified stock or capacity for an identified purpose. Not authorization to manufacture.

**Current Store answer** — Store answer applicable to the exact candidate/revision/request/attempt under the consuming System's correlation rules. It does not automatically mean live inventory, newly queried information, continuing commercial commitment, or binding price.

Application receipt time does not renew Store source time.

## 9. Material and supply distinctions

**MaterialClass** is not **SKU**.

**MaterialSpec** is not **SKU**.

**Catalog item** is not **offering**.

**Offering** is not **stock**.

**Stock** is not **reservation**.

**On hand** is not automatically **available for this project**.

**Special-order listing** is not **confirmed supplier availability**.

**Nominal size** is not **actual size**.

**Hardwood** is not a species and does not mean physically hard wood.

**Grade** has meaning only under an identified grading or commercial system.

**Board foot (bf)** is a volume measure; **linear foot (lf)** is a length measure; neither is a piece count.

## 10. Manufacturing and machine distinctions

**Stock material** — Input material from which a part or component is produced.

**Workpiece** — Material currently being positioned or worked on for manufacturing.

**Part** — Defined manufactured item with requirements attributable to it.

**Component** — Part or supplied item participating in a larger assembly or deliverable.

**Operation** — Bounded manufacturing act such as crosscut, bore, trim, rout, mill, or dado.

**Process plan** — Structured description of operations and resources required to produce the intended result.

**Machine program / controller instructions** — Machine-runtime representation produced for a specific machine/controller context. Downstream from project definition and process definition.

**Postprocessor / lowering** — Transformation from a neutral/process representation into machine- or controller-specific instructions.

**Readiness** — Present ability to perform work given current material, tooling, machine, operator, and safety conditions.

**Authorization** — Permission from a defined authority for a defined act.

**Cycle Start** — Local act initiating an allowed machine cycle after the applicable local prerequisites are satisfied.

**Datum** — Formal engineering reference with a specific defined role. Do not use it as a synonym for every edge, stop, zero, or convenient reference.

**Machine reference** — Fixed machine-side geometric reference.

**Origin** — Defined zero point of a coordinate system. It is not automatically a formal datum.

**Capability** — Ability within a stated envelope. Capability is not availability, readiness, acceptance, or authorization.

**Modeled cycle / modeled occupied-cell time** — Calculated reference duration under an identified model. Not measured production time or a promised completion time.

## 11. Program doctrines with defined meaning

**Scan-to-Build** — Governed path intended to let a sufficiently resolved requirement reach relevant material and bounded productive capability, receive an attributable result or refusal, and preserve the consequential record.

**Demand as Architecture** — Proposition that incomplete human or commercial demand can become an earlier system input before it has necessarily become a SKU, RFQ, or fully specified order.

**Data before atoms / information before atoms** — Resolve consequential information before unnecessarily moving or transforming physical material.

**Smallest useful increment** — Add only the information, process, or machine capability needed beyond what the existing holder already provides.

**Refusal is an outcome** — Correct refusal is successful system behavior when the request lies outside the applicable boundary.

**No silent promotion** — A weaker information state does not become a stronger one merely because continuation would be convenient.

**Owner declaration remains owner declaration** — System interpretation may structure or classify a person's words but does not rewrite the interpretation as though it were the person's original declaration.

**Capability is not authority** — Ability to perform work does not confer permission to perform it.

**Machine does not infer the project** — Physical execution receives sufficiently resolved instructions; the machine/controller does not decide what the person meant.

**Store does not rewrite governance** — Store facts and Store convenience do not create or modify shared governance or project truth.

**NO BLOOD ON WOOD** — Human safety and valid refusal boundaries outrank convenience, throughput, demonstration success, cost, or software completion.

## 12. Never equate

The following substitutions are prohibited unless a separately defined transformation explicitly establishes the stronger proposition:

- user declaration ≠ system interpretation
- declared ≠ observed
- observed ≠ verified
- measurement ≠ exact truth
- confidence ≠ verification
- precision ≠ accuracy
- selection ≠ verification
- confirmation ≠ commercial assent
- confirmation ≠ physical truth
- estimate ≠ quote
- quote ≠ reservation
- price observation ≠ quote
- MaterialSpec ≠ SKU
- offering ≠ stock
- stock ≠ reservation
- availability ≠ capability
- capability ≠ readiness
- readiness ≠ authorization
- Store SUPPORTABLE ≠ governed authorization
- Store accept ≠ governed authorization
- WorkPacket ≠ process plan
- WorkPacket ≠ machine program
- process plan ≠ G-code/controller instructions
- machine program ≠ authorization
- G-code/controller instructions ≠ authorization
- schema-valid ≠ physically true
- deterministic ≠ correct
- hash ≠ digital signature
- authentication ≠ authorization
- simulation ≠ production
- simulated execution ≠ physical fabrication
- Git commit ≠ architectural approval
- defined ≠ activated
- fixture fact ≠ industry fact
- modeled cycle ≠ measured cycle
- current answer ≠ live source
- historical success ≠ commissioned capability

## 13. Change rule

Add or change a shared term only when the difference can materially affect project meaning, evidence, material, Store answers, economics, authority, safety, execution, or the durable record.

A shared-definition change should identify:

1. the term;
2. prior meaning/source;
3. proposed meaning;
4. affected System/Store interfaces;
5. compatibility consequences;
6. tests or documentary checks required;
7. whether any durable identifier remains unchanged.

System and Store should link to this page for shared terminology and maintain only their genuinely local terms. Donor repositories may retain historical wording as provenance, but they cease to be semantic authorities once their selected material is admitted here.
