# PROJECT 1 / D-001 — Reference Implementation, Controller Lowering, and Q Derivation 0.1

**Owner:** `GeorgePlattDemo/3d-solutions-program`  
**Status:** `CANDIDATE ENGINEERING / REFERENCE IMPLEMENTATION`  
**Investigation date:** 2026-10-03  
**Physical status:** not built, not commissioned, not safety-validated, not measured in production  
**Rule:** this document does not change System meaning, Store capability/economics, `STORE_PIN`, or physical authority.

> **NO COMMERCIAL CONTROL STACK WAS PREVIOUSLY FROZEN. THE BECKHOFF/TWINCAT STACK BELOW IS A NEW REFERENCE IMPLEMENTATION SELECTION.**

---

## 0. Executive statement

This document closes one bounded information-to-machine chain for the current 16 in endpoint of Project 1 (`SYO-USER1-XBRACE`, configuration `0.1`) without claiming that the reference machine exists physically.

The chain is:

`confirmed Project 1 definition → physical demand → pinned Store material/capability answer → machine-neutral operations → D-001 station transforms → TwinCAT NC targets → IEC 61131-3 Structured Text → servo/tool handshakes → deterministic reference trace → machine-time comparison → Q reconciliation`.

The current authoritative Store answer remains **$8.54**. That answer is produced by the System-pinned Store revision `9c62d9d6f7775deef83d47196d32c9b5174a352c`, not by this document. The pinned Store model gives `T_MACHINE = 85.3620 s = 1.4227 min`, material `$2.61`, machine service `$5.93`, and `Q = $8.54`.

The independently specified reference hardware/control trace developed here gives **83.7759 s = 1.3963 min** when the current Store handling assumptions are retained for an apples-to-apples comparison. At the Store's existing `$250/h` machine-service rate that timing would yield `$5.82` machine service and `$8.43` material-plus-service. That **$8.43 is not a Store answer**. It is a `REFERENCE_IMPLEMENTATION_TIMING_CHECK`. The timing delta is `-1.5861 s`; the resulting comparison delta is `-$0.11`.

The remaining empirical gap is physical construction, risk assessment and safety validation, machine commissioning, traction/slip measurement, positional accuracy, miter/spot conformance, actual cycle time, and inspection of produced parts. It is not necessary to rediscover whether ordinary industrial servos, deterministic PLC motion blocks, pneumatic saw cycles, or digital I/O exist.

---

## 1. Evidence identities

### 1.1 Repository identities frozen for this investigation

| Owner | Revision used | Role |
| --- | --- | --- |
| Program | `641c0149909568abc3872c4b7c2fb45592006a68` | research / candidate engineering |
| System | `b6c7fbcb9d618e600eca0e46dc10374db6d2ecfc` | current job meaning |
| Store main | `0b73941ba1cd4cf90c532c6c09f501681a5ab01d` | repository head only; **not** the runtime authority used for this calculation |
| Store runtime pin | `9c62d9d6f7775deef83d47196d32c9b5174a352c` | exact Store source consumed by current System runtime for this path |

`CURRENT SOURCE RULE`: Store main is not substituted for the System-owned runtime pin.

### 1.2 Exact current Project 1 calculation identity

Current System regression evidence for the 16 in endpoint records:

- `configurationId = SYO-USER1-XBRACE`
- `configurationVersion = 0.1`
- Store input hash `bea3c0b3841d013b463277ebaa02121bef79b65abe5e46b05a40f337afa3b868`
- Store result hash `0fd6b7d19ef8f64d133486c9d2ccf72256b2993bb60aa14c77b3c3e8004973bc`
- pinned Store `9c62d9d6f7775deef83d47196d32c9b5174a352c`
- material `$2.61`
- machine service `$5.93`
- combined value `$8.54`
- modeled job time `1.4227 min`
- final remainder `27.625 in`.

Primary current files:

- System Project 1 rule: `apps/stb/shared/user1-xbrace-rule.mjs`
- System regression: `apps/stb/public-build/tests/user1-travel-standard.test.mjs`
- Store envelope: `d001-stage2-envelope.mjs`
- Store travel/economics: `d001-travel-standard.mjs`
- Store catalog: `store-zero-catalog.json`

### 1.3 Patent primary sources

- U.S. Patent 9,720,401 B2, issued 2017-08-01.
- U.S. Patent 10,768,609 B2, issued 2020-09-08.

This is engineering correspondence only. No statement below is a legal conclusion regarding claim scope, infringement, validity, enforceability, or claim construction.

---

## 2. Authority / ownership boundaries

| Layer | Owns | Does not own here |
| --- | --- | --- |
| Program | why this reference design was selected; candidate hardware/control engineering; evidence and unresolved questions | current job meaning or Store authority |
| System | Project 1 identity, dimensions, part/features, revision semantics, physical-demand meaning | Store price/capability; controller coordinates |
| Store | current material mapping, declared D-001 Stage-2 capability/model, Store timing/economics, Store answer/refusal | customer definition; machine-local servo/controller implementation |
| Machine-local reference implementation | axes, encoder scaling, station offsets, tool identities, I/O, PLC source, drive parameters, state machine | permission to rewrite System or Store |

A coherent controller program in this document does not become commissioned capability. A catalog page does not become an installed fact. A patent feature does not become a safety requirement merely because it is disclosed.

---

## 3. Current facts register

### 3.1 System / Project facts

| Fact | Value | Evidence class |
| --- | --- | --- |
| Configuration | `SYO-USER1-XBRACE` / `0.1` | `CURRENT SOURCE RULE` |
| Part quantity | 2 | `CURRENT SOURCE RULE` |
| Part length | 16.000 in each | `CURRENT SOURCE RULE` |
| Parent workpiece demand | 60.000 in | `CURRENT SOURCE RULE` |
| Fixed horizontal span | 8.000 in | `CURRENT SOURCE RULE` |
| Derived face-miter angle | 30.000° | `DERIVED ENGINEERING VALUE` from System rule, `asin(8/16)` |
| Achieved rise | 13.856406 in | `DERIVED ENGINEERING VALUE`, `sqrt(16^2-8^2)` |
| End relation | parallel | `CURRENT SOURCE RULE` |
| Length datum | long-long outer edge | `CURRENT SOURCE RULE` |
| Cut plane | miter-face | `CURRENT SOURCE RULE` |
| Saw cuts | 3 total | `CURRENT SOURCE RULE` |
| Spot features | one per part, part-relative X = 8.000 in | `CURRENT SOURCE RULE` |
| Spot across width | centered on wide face | `CURRENT SOURCE RULE` |
| Required ops | `MITER_LIMITED`, `SPOT_ON_LOCATION` | `CURRENT SOURCE RULE` |
| Datum C method | `REFERENCE_CUT` | `CURRENT SOURCE RULE` |
| Unresolved Project conditions | none | `CURRENT SOURCE RULE` |
| Material source | Store Zero | `CURRENT SOURCE RULE` |

### 3.2 Current pinned Store facts

| Fact | Value | Evidence class |
| --- | ---: | --- |
| Material offering | `STB-ZERO-SPF-2X4-60-001` | `CURRENT_STORE_DECLARATION` |
| Actual section | 1.5 × 3.5 in | `CURRENT_STORE_DECLARATION` |
| Selling amount | $2.61 | `CURRENT_STORE_DECLARATION` |
| Store selection | shortest complete Store offering | `CURRENT_STORE_DECLARATION` |
| D-001 envelope | `D001-STAGE2-ENVELOPE-0.3` | `CURRENT_STORE_DECLARATION` |
| Travel standard | `STB-D001-DIMENSIONAL-TRAVEL-0.1` v0.2.0 | `CURRENT_STORE_DECLARATION` |
| Economics | `STB-D001-STORE-ECONOMICS-S2-0.1` v0.1.0 | `CURRENT_STORE_DECLARATION` |
| X loaded max | 480 in/min | `MODELED ASSUMPTION`, Store-owned |
| X acceleration | 32 in/s² | `MODELED ASSUMPTION`, Store-owned |
| Y max | 240 in/min | `MODELED ASSUMPTION`, Store-owned |
| Y acceleration | 16 in/s² | `MODELED ASSUMPTION`, Store-owned |
| Kerf | 0.125 in | `MODELED ASSUMPTION`, Store-owned |
| Minimum retained control | 24 in | `CURRENT_STORE_DECLARATION` |
| Load/seat | 36 s | `MODELED ASSUMPTION`, Store-owned |
| Release/label | 24 s | `MODELED ASSUMPTION`, Store-owned |
| Store annual cost pool | $120,000 | `MODELED ASSUMPTION`, Store-owned |
| Forecast productive hours | 600 h/year | `MODELED ASSUMPTION`, Store-owned |
| Target gross margin | 20% | `MODELED ASSUMPTION`, Store-owned |
| Break-even rate | $200/h | `DERIVED ENGINEERING VALUE` from Store model |
| Machine sell rate | $250/h | `DERIVED ENGINEERING VALUE` from Store model |

### 3.3 Current D-001 declared geometry

`CURRENT_STORE_DECLARATION`, measured = false, commissioned = false:

| Element | X (in) | Role |
| --- | ---: | --- |
| `MILL_END` | -6 | end-mill reference station |
| `SAW-L` | 0 | infeed downstroke / single-plane face-miter 0–45° |
| `R1` | 24 | manipulating roller |
| `MILL_LONG` / `SPOT-FACE-REF` | 36 | longitudinal mill / spot tooling center |
| `R2` | 48 | manipulating roller |
| `SAW-R` | 72 | outfeed square downstroke station |

Axes: X is along the fence/feed, Y is perpendicular to the fence/across width, Z is tool engagement/depth. Datum A is the fixed fence at Y=0. Datum B is the support/table at Z=0. Datum C is the dynamic longitudinal workpiece origin.

### 3.4 Explicit current D-001 unresolved items preserved

The pinned Store source itself names unresolved items including: patent FIG. 5 has three manipulating rollers while Stage 2 names two; saw-type details; an additional router/drill way; generic drill capability beyond the fixed 3/16 in spot; unsupported overhang geometry; and whether short material may run under one-roller control. This document does not erase those items.

---

## 4. Patent claim trail

The table is correspondence, not claim construction.

| Patent / claim | Relevant limitation | Engineering meaning for this investigation | Correspondence |
| --- | --- | --- | --- |
| 9,720,401 claim 1 | customer interface; final selection; tandem sheet/dimensional machines; generated instructions controlling fabrication | definition remains upstream of machine; instructions exist downstream | `CLAIM CORRESPONDENCE` |
| 9,720,401 claim 2 | manual control panel or automated computer control | local manual/recovery plus automated run is compatible with the disclosed architecture | `CLAIM CORRESPONDENCE` |
| 9,720,401 claim 4 | dimensional support surface/frame; fence; clamping roller; servo-controlled manipulating roller; circular-saw station | D-001 fence/table/roller/saw architecture derives directly from this disclosed relationship | `CLAIM CORRESPONDENCE` |
| 9,720,401 claim 5 | fixed rigid vertical/horizontal ways positioning tool heads under servo control | Y/Z tooling carriages are one narrower implementation | `CLAIM CORRESPONDENCE` + `BOUNDED IMPLEMENTATION CHOICE` |
| 9,720,401 claim 6 | rigid metal base with mounting provisions | one common datum-bearing machine structure is retained | `CLAIM CORRESPONDENCE` |
| 9,720,401 claim 9 | component label and assembly instructions | result/label signal remains downstream | `CLAIM CORRESPONDENCE` |
| 9,720,401 claims 10–13 | customer variation, estimated price, acceptance, materials/machining instructions, transmission | current architecture separates definition, Store answer and machine-local lowering while retaining explicit handoffs | `CLAIM CORRESPONDENCE` with current architecture separation |
| 9,720,401 claims 14–18 | labels, packaging/secondary ops, machine-readable instructions, Store pricing database | label/result and Store-derived Q retain the lineage | `CLAIM CORRESPONDENCE` |
| 10,768,609 claim 1 | estimated price; final selection; dimensional machine moving stock fore/aft along its longitudinal axis | Project 1 feed axis and Q are directly relevant | `CLAIM CORRESPONDENCE` |
| 10,768,609 claim 4 | accepted order → materials list and machining instructions | current demonstration stops before commercial order; instruction derivation is still modeled | `CLAIM CORRESPONDENCE`; no commerce claim |
| 10,768,609 claim 5 | transmit instructions; operator load instruction; machining operations specific to component | local cached job package + local Cycle Start implement the information relationship without remote real-time motion | `CLAIM CORRESPONDENCE` + `BOUNDED IMPLEMENTATION CHOICE` |
| 10,768,609 claims 6–15 | labels, CAD/CAM, sequential loading, storage media, Store pricing, retail location | current System/Store/Machine separation preserves the relevant information path | `CLAIM CORRESPONDENCE` |

---

## 5. Patent specification / figure correspondence

Patent FIG. 5 and its dimensional-machine specification disclose a support/table, fixed fence used as a datum, commonly controlled manipulating rollers, idler rollers, end saw stations, pneumatic clamping rollers, fixed tooling ways, lead-screw/tool plunging arrangements, controller-derived servo signals, local Cycle Start, and sequential operations while stock moves along the fence.

The reference implementation intentionally differs in three important ways:

1. **Two manipulating rollers are retained because current Store Stage 2 names R1 and R2.** The patent exemplary embodiment describes three. This is a `BOUNDED IMPLEMENTATION CHOICE`, not an assertion that the patent requires two.
2. **The selected Cantek PCM508 saw cycles pneumatically.** This is a practical reference selection for the downstroke station; it is not represented as literal servo actuation of the saw stroke. Its approved machine-builder interface remains a commissioning dependency.
3. **Controller-specific lowering is machine-local.** The current architecture does not deny instruction generation/transmission; it moves controller coordinates, postprocessing, I/O and drive details downstream from System/Store authority.

Patent correspondence establishes lineage. It establishes neither guarding adequacy nor commissioned capability.

---

## 6. Exact Project 1 definition

Canonical demand used for the 16 in endpoint:

```json
{
  "configurationId": "SYO-USER1-XBRACE",
  "configurationVersion": "0.1",
  "definedWorkpieceLengthIn": 60,
  "sawAngleDeg": 30,
  "cutPlane": "miter-face",
  "endIdentity": "both",
  "endRelation": "parallel",
  "lengthDatum": "long-long-outer-edge",
  "datumCMethod": "REFERENCE_CUT",
  "requiredOps": ["MITER_LIMITED", "SPOT_ON_LOCATION"],
  "declaredSawCuts": 3,
  "declaredSpotCount": 2,
  "parts": [
    {"partId":"PART-1","lengthIn":16,"features":[{"featureId":"SPOT-1","kind":"SPOT_ON_LOCATION","xIn":8,"locationRule":"CENTERED_ON_PART","acrossWidthRule":"CENTERED_ON_WIDE_FACE"}]},
    {"partId":"PART-2","lengthIn":16,"features":[{"featureId":"SPOT-2","kind":"SPOT_ON_LOCATION","xIn":8,"locationRule":"CENTERED_ON_PART","acrossWidthRule":"CENTERED_ON_WIDE_FACE"}]}
  ]
}
```

No servo coordinate, station location, kerf compensation or controller instruction is part of this definition.

---

## 7. Physical-demand derivation

| Project requirement | Physical demand | Machine-neutral operation |
| --- | --- | --- |
| 60 in Store-origin parent | load and retain material identity | `LOAD_MATERIAL` |
| fixed fence/table relationship | establish A/B contact | `SEAT_AND_CLAMP` |
| dynamic longitudinal origin | create a known fresh face | `REFERENCE_CUT` |
| SPOT-1 at part-relative 8 in | place fixed 3/16 in point feature at center wide face | `SPOT_ON_LOCATION` |
| SPOT-2 at part-relative 8 in | same operation on second part | `SPOT_ON_LOCATION` |
| PART-1 length 16, 30° face | establish retained cutoff face | `MITER_CUTOFF` |
| fresh cut becomes next origin | update dynamic C only after successful cut | `REBASE_DATUM_C` |
| PART-2 length 16, 30° face | second retained cutoff | `MITER_CUTOFF` |
| remaining stock | retain remnant if control rule passes | `RETURN_REMNANT` |
| completion identity | emit result / label-ready record | `COMPLETE_AND_SIGNAL_LABEL` |

The resulting machine-neutral sequence is:

```text
LOAD_MATERIAL STB-ZERO-SPF-2X4-60-001
SEAT_AND_CLAMP DATUM_A DATUM_B
REFERENCE_CUT angle=30deg datumEffect=ESTABLISH_DATUM_C
SPOT_ON_LOCATION part=PART-1 x=8in across=CENTERED_ON_WIDE_FACE tool=3/16in
SPOT_ON_LOCATION part=PART-2 x=8in across=CENTERED_ON_WIDE_FACE tool=3/16in
MITER_CUTOFF part=PART-1 length=16in angle=30deg keptFaceRule=LONG_LONG_OUTER_EDGE
REBASE_DATUM_C method=FRESH_CUT_FACE
MITER_CUTOFF part=PART-2 length=16in angle=30deg keptFaceRule=LONG_LONG_OUTER_EDGE
REBASE_DATUM_C method=FRESH_CUT_FACE
RETURN_REMNANT expected=27.625in minControlled=24in
COMPLETE_AND_SIGNAL_LABEL
```

---

## 8. Current Store answer and derivation

The pinned Store economics formula is:

`Q = stock/sourced selling price + (T_MACHINE_hr × STORE_MACHINE_SELL_RATE)`.

Store rate:

- break-even = `$120,000 / 600 h = $200/h`
- sell rate = `$200 / (1 - 0.20) = $250/h`.

### 8.1 Pinned Store X timing

Store motion: `V = 480 in/min = 8 in/s`, `A = 32 in/s²`. Transition distance is `V²/A = 2 in`; all Project 1 X moves are trapezoidal.

For `D ≥ 2 in`:

`t = 2V/A + (D - V²/A)/V = 0.5 + (D - 2)/8`.

| Move | Distance (in) | Time (s) |
| --- | ---: | ---: |
| C 0 → P1 spot target 28 | 28.000 | 3.750000 |
| P1 target 28 → P2 target 11.875 | 16.125 | 2.265625 |
| P2 target 11.875 → cutoff target -16 | 27.875 | 3.734375 |
| rebased C 0 → second cutoff -16 | 16.000 | 2.250000 |
| **Total** | | **12.000000** |

### 8.2 Pinned Store saw timing

Store model: 20 in blade, 1,800 rpm, 80 teeth, 0.003 in/tooth, finish factor 0.5, 1 s deploy, 1 s retract.

- modeled feed = `0.003 × 80 × 1800 × 0.5 = 216 in/min`
- 30° traverse = `3.5 / cos(30°) = 4.041451884 in`
- cutting traverse time = `4.041451884 / 216 × 60 = 1.122625523 s`
- one modeled saw cycle = `3.122625523 s`
- three saw cycles = `9.367876570 s`.

### 8.3 Pinned Store spot timing

- wide-face center Y = `3.5 / 2 = 1.75 in`
- Store Y speed = 4 in/s; A = 16 in/s²; Y time = `0.6875 s`
- drill point length = `(0.1875/2) / tan(118°/2) = 0.056330683 in`
- plunge = `0.056330683 + 0.1875 = 0.243830683 in`
- feed = `3000 rpm × 0.008 in/rev = 24 in/min = 0.4 in/s`
- plunge time = `0.609576708 s`
- one Store spot = `0.6875 + 0.35 + 0.609576708 + 0.35 = 1.997076708 s`
- two = `3.994153415 s`.

### 8.4 Current pinned Store total

```text
T_LOAD_SEAT       36.000000 s
T_REFERENCE        3.122626 s
T_INDEX           12.000000 s
T_SAW              6.245251 s
T_SPOT             3.994153 s
T_MILL             0.000000 s
T_RELEASE_LABEL   24.000000 s
--------------------------------
T_MACHINE         85.362030 s = 1.4227005 min
```

Machine service = `85.362030 / 3600 × $250 = $5.93` after Store rounding.  
Material = `$2.61`.  
**CURRENT PINNED STORE Q = $8.54.**

Final remnant: `60 - 0.125 reference kerf - (16 + 0.125) - (16 + 0.125) = 27.625 in`, which remains above the 24 in Store minimum-control rule.

---

## 9. Coordinate model and actual Project 1 transforms

### 9.1 Workpiece coordinates

Let the fresh Datum C face be `x_w = 0`. Kerf is process geometry, not customer finished length.

For part `i`:

`partStart_i = sum(previous part length + kerf)`.

Thus:

- PART-1 start = `0`
- SPOT-1 workpiece X = `0 + 8 = 8`
- PART-2 start = `16 + 0.125 = 16.125`
- SPOT-2 workpiece X = `16.125 + 8 = 24.125`.

### 9.2 Station transform

For a fixed station at machine coordinate `X_station`, Store's dynamic C target is:

`C_target = X_station - x_w_feature`.

At `SPOT-FACE-REF`, `X_station = 36`:

- SPOT-1 C = `36 - 8 = 28`
- SPOT-2 C = `36 - 24.125 = 11.875`.

At `SAW-L`, `X_station = 0`. After each successful fresh-face rebase, a 16 in cutoff target is:

`C_target = 0 - 16 = -16`.

### 9.3 Controller coordinate realization

`NEW_REFERENCE_SELECTION`: configure the X NC axis in inches with positive sign matching increasing Store C. The feed servo is rotary, so there is no linear stage hard-stroke corresponding to these coordinates. The work coordinate is an NC/software coordinate over roller rotation.

- Before the first cut, encoder motion may be calibrated for controller use, but `POSITION_VALID = FALSE` at the Scan-to-Build machine semantic layer.
- After the successful reference cut, `MC_SetPosition(Position := 0, Mode := FALSE)` establishes the current X NC work coordinate as Datum C = 0.
- After each successful cutoff, the same operation rebases the fresh face to C = 0 without a physical move.
- Any slip detection, loss of clamp pressure, encoder fault, guard event requiring position re-establishment, manual jog outside controlled recovery, or rejected saw completion invalidates `POSITION_VALID`.

Y is measured from Datum A/fence. For a 3.5 in wide board, center is `Y=1.75 in`.

Z is defined as **tool-tip height above Datum B/table**, not motor turns. Store material thickness supplies the 1.5 in board top. Reference tool positions are:

- safe `Z = 2.000 in`
- approach `Z = 1.550 in`
- final spot tip `Z = 1.500 - 0.243830683 = 1.256169317 in`.

Tool length calibration is machine-local and must be measured before physical commissioning.

---

## 10. Industrial control-family comparison

| Family | Motion / network / safety | Finding |
| --- | --- | --- |
| Beckhoff CX / TwinCAT 3 / AX8000 / EtherCAT / TwinSAFE | PC-based PLC/NC; EtherCAT; PLCopen-style `Tc2_MC2`; OCT servo feedback; integrated Safe Motion options | **selected reference**: coherent controller/drive/I/O/safety stack and directly documented motion blocks |
| Siemens S7-1500T / SINAMICS S210 / PROFINET / PROFIsafe | mature technology CPU, servo and safety ecosystem | credible alternate; not used for calculations |
| Rockwell Compact GuardLogix 5380 / Kinetix / EtherNet/IP CIP Motion/Safety | mature North American PLC/motion/safety ecosystem | credible alternate; not used for calculations |

This is not a ranking of industrial vendors. It is one bounded selection so the rest of the derivation uses one consistent controller family.

---

## 11. Reference implementation selection

### 11.1 Control and feed axis

`NEW_REFERENCE_SELECTION`:

- Beckhoff `CX5340-0195` embedded PC, Windows 10 IoT Enterprise 2021 LTSC 64-bit with TwinCAT 3 Runtime XAR preinstalled; licenses ordered separately.
- Beckhoff AX8000 drive family: `AX8620-0000-0000` supply, `AX8206-0200-0000` dual Safe Motion axis module and `AX8108-0200-0000` single Safe Motion axis module for Project 1 X/Y/Z. Additional axes for end-mill tooling require another axis module before adoption.
- Beckhoff `AM8022` D-winding motors; reference feedback selection is 24-bit multi-turn OCT. Final full motor ordering string is **quote/configuration dependent** and must be frozen by the machine builder; the functional motor family is not presented as installed hardware.
- Beckhoff `AG2250-+PLE40-M02-40` 40:1 planetary gearbox for X: 18 Nm nominal output, 29 Nm max acceleration torque. Beckhoff identifies the clamping-hub letter automatically from the motor; final suffix is therefore `UNRESOLVED_ORDERING_SUFFIX`, not invented here.
- two Sunray `450X350SK` 4.50 × 3.50 in polyurethane drive wheels at R1/R2.
- two Festo `DSBC-50-50-PPVA-N3` cylinders for controlled roller normal force.
- SKF `SY 30 TF` class pillow-block supports for the common-drive shaft where the final shaft drawing uses 30 mm journals.
- Lovejoy L099 class jaw coupling where a flexible shaft coupling is required; final bores/keyways follow the issued shaft drawing.

### 11.2 Saw stations

`NEW_REFERENCE_SELECTION`: two Cantek `PCM508` 20 in pneumatic miter cut-off saws provide common spares and cover the Store's downstroke miter/square station concept. SAW-L is mechanically set/verified at 30° for Project 1; SAW-R is locked/verified at 0° for the square role. Manufacturer/dealer data report 20 in blade, 3,100 rpm, 7.5 hp, ±60° capability and 30–45 cycles/min.

For Project 1 the reference timing uses the slow end of the published cycle range: `60/30 = 2.0 s/cycle`. This is a manufacturer-rate-derived reference interval, **not measured integrated-cell cycle time**.

The machine builder must provide an approved remote cycle/complete/retracted interface. This document does not bypass or redesign the OEM saw safety circuit.

### 11.3 Spot station

`NEW_REFERENCE_SELECTION`:

- Nakanishi `EMS-3060K`, code 7862, 30 mm motor spindle, max 60,000 rpm, 350 W, CHK collet range 0.5–6.35 mm.
- Nakanishi `E3000` controller, 200 V code 8422, 1,000–80,000 rpm, external motor start/stop and speed control/monitoring.
- 3/16 in, 118° drill point matching the Store geometric rule; final tool manufacturer/lot is a tooling-consumable selection to freeze before commissioning.
- HIWIN KK-series Y ballscrew stage, functional selection `KK8610P0640` class; the final cover/sensor/motor-adapter ordering suffix must be confirmed through HIWIN configuration.
- HIWIN KK-series Z stage, functional selection `KK6005P0150` class; final ordering suffix similarly requires configuration.

### 11.4 Broader D-001 mill functions not used by Project 1

The Store also declares milling. A concrete candidate spindle is Teknomotor `5160-A-DB-P-ER25-PR-RH`, order code `COM51600424`: ER25, 2.2 kW S1, 1.75 Nm, 12,000 rpm nominal, 18,000 rpm max, 220/380 V, manufacturer-described for wood/aluminum/PVC machinery.

For the x=36 tooling center, the reference mechanical concept uses a machine-builder-designed exchangeable spot/router head interface with tool identity sensing. `MILL_END` at x=-6 requires a separate or duplicated Y/Z tooling carriage. Because Project 1 does not use `MILL_LONG` or `MILL_END`, the **exact end-mill carriage part-number stack remains UNRESOLVED and cannot be promoted as a completed full-D-001 installed BOM**. This is an explicit adoption blocker for Store-wide D-001 replacement, not a hidden omission in the Project 1 execution.

---

## 12. Reference BOM / component shopping register

Observed public prices are research observations dated 2026-10-03, not purchase orders or quotes. `QUOTE_REQUIRED` means no defensible public price was found and no number is invented.

| Function | Manufacturer / exact reference | Qty | Key fact | Price / availability | Evidence class |
| --- | --- | ---: | --- | --- | --- |
| Embedded controller | Beckhoff `CX5340-0195` | 1 | TwinCAT 3 XAR, Windows 10 IoT LTSC | `QUOTE_REQUIRED` | manufacturer specification |
| AX8000 supply | Beckhoff `AX8620-0000-0000` | 1 | 3ph 200–480 VAC supply module | `QUOTE_REQUIRED` | manufacturer specification |
| X/Y drive | Beckhoff `AX8206-0200-0000` | 1 | 2 × 6 A, Safe Motion, OCT | `QUOTE_REQUIRED` | manufacturer specification |
| Z drive | Beckhoff `AX8108-0200-0000` | 1 | 8 A, Safe Motion, OCT | `QUOTE_REQUIRED` | manufacturer specification |
| X/Y/Z motors | Beckhoff AM8022 D-winding, 24-bit multi-turn OCT configured variant | 3 | 0.70 Nm rated, 4.18 Nm peak, 8,000 rpm | `QUOTE_REQUIRED`; final full order code unresolved | manufacturer specification |
| X gearbox | Beckhoff `AG2250-+PLE40-M02-40` + AM802x F2 adapter | 1 | ratio 40, 18 Nm nominal, 29 Nm accel | `QUOTE_REQUIRED`; hub suffix auto-selected | manufacturer specification |
| Drive wheels | Sunray `450X350SK`, 4.50 × 3.50 | 2 | polyurethane drive wheel; shaft/keyway configured to drawing | **$108.71 ea** public listing | distributor/manufacturer listing |
| Roller cylinders | Festo `DSBC-50-50-PPVA-N3`, 1366950 | 2 | 50 mm bore/stroke; 1178 N advance at 6 bar | `QUOTE_REQUIRED` | manufacturer specification |
| Safe pneumatic exhaust | Festo `MS6-SV-1/2-E-10V24-AD1`, 562580 | 1 | safe exhausting / unexpected-start prevention component | `QUOTE_REQUIRED` | manufacturer specification |
| Saw-L | Cantek `PCM508` | 1 | 20 in, 3100 rpm, 30–45 cycles/min, pneumatic miter | public market observation about **$18.7k–$18.9k**; verify quote | manufacturer/dealer specification |
| Saw-R | Cantek `PCM508` | 1 | same unit locked/verified square for reference | same | manufacturer/dealer specification |
| Spot spindle | Nakanishi `EMS-3060K`, 7862 | 1 | 350 W, max 60k rpm | `QUOTE_REQUIRED` | manufacturer specification |
| Spot controller | Nakanishi `E3000`, 200 V code 8422 | 1 | 1k–80k rpm, external I/O control | `QUOTE_REQUIRED` | manufacturer specification |
| Y stage | HIWIN KK86 10-mm-lead 640-mm-rail configured stage | 1 | >14 in required travel | `QUOTE_REQUIRED`; final suffix unresolved | manufacturer family/catalog |
| Z stage | HIWIN KK60 5-mm-lead 150-mm-rail configured stage | 1 | sufficient reference plunge stroke | `QUOTE_REQUIRED`; final suffix unresolved | manufacturer family/catalog |
| Router spindle | Teknomotor `COM51600424` | 1 | ER25, 2.2 kW, 12k nominal / 18k max | `QUOTE_REQUIRED` | manufacturer specification |
| Safety logic | Beckhoff `EL6910` | 1 | TwinSAFE Logic / FSoE | `QUOTE_REQUIRED` | manufacturer specification |
| Safe inputs | Beckhoff `EL1904` | 2 | 4 safe inputs each | public secondary listings vary; quote preferred | manufacturer + distributor observation |
| Safe outputs | Beckhoff `EL2904` | 1 | 4 safe outputs | public secondary listing about **$174**; quote preferred | manufacturer + distributor observation |
| Guard locks | Schmersal `AZM300Z-ST-1P2P`, 103001435 | 2 | RFID, monitored guard lock, power-to-unlock | public listing **$788 ea**, 6 shown in stock; recheck before order | manufacturer + distributor observation |
| E-stops | Schneider `XB5AS8445` | 2 | 40 mm red latching turn-release 1NO+1NC | normally stocked; price by distributor | manufacturer specification |
| 24 VDC supply | Phoenix Contact `QUINT4-PS/3AC/24DC/20`, 2904622 | 1 | 3ph input, 24 VDC/20 A | `QUOTE_REQUIRED` | manufacturer specification |
| Main disconnect | Eaton `DH362URK` | 1 | 60 A, 600 V, 3-pole non-fused switch | distributor quote | manufacturer specification |
| Control enclosure | nVent Hoffman `A60H4812SSLPQT` | 1 | 60 × 48 × 12 in Type 4X stainless | `QUOTE_REQUIRED` | manufacturer specification |
| Idler/support rollers | Ultimation `RS19G-24-ROLLER` | as drawing | 1.9 in galvanized, 24 in BF, 267 lb/roller | **$19.50 ea** public listing | manufacturer/distributor listing |
| Feed shaft | machine-builder drawing | 1 | keyed 30 mm bearing journals; wheel hubs to drawing | fabricated | candidate engineering |
| Guarding/frame/fence/table | machine-builder drawings | 1 lot | common rigid datum structure; guarding based on risk assessment | fabricated / quote | candidate engineering |
| Dust collection interfaces | machine-builder ducting per saw/spindle requirements | 1 lot | no dust-system capacity claimed here | unresolved design | unresolved |

Critical alternates: Siemens S7-1500T/SINAMICS and Rockwell Compact GuardLogix/Kinetix remain controller-family alternates; Cantek PCM610 is a larger related miter-saw family alternate. They are not mixed into the calculations.

---

## 13. Feed-axis engineering

### 13.1 Kinematics

Selected drive-wheel OD = `4.5 in`.

- circumference = `π × 4.5 = 14.137166941 in/rev`
- at 480 in/min, roller speed = `480 / 14.137166941 = 33.953055 rpm`
- with 40:1 gearbox, motor speed = `1,358.122 rpm`
- AM8022 rated speed = `8,000 rpm`
- selected operating point uses about 17% of rated speed.

The Store's 480 in/min is therefore kinematically achievable by the selected motor/gear/wheel combination. This does **not** prove lumber traction or positional accuracy.

### 13.2 Encoder quantization

With a 24-bit encoder and 40:1 gearbox, ideal mathematical wheel-surface quantization is:

`14.137166941 / (40 × 2^24) = 0.000000021066 in/count`.

This number is **not machine accuracy**. Gear backlash, wheel compliance, wood compression, shaft torsion, mounting, roller eccentricity and slip will dominate long before that quantization limit.

### 13.3 Conservative force / torque check

`MODELED ENGINEERING ASSUMPTIONS`, not measured values:

- moving equivalent mass: 100 lbm
- parasitic resistance: 20 lbf
- acceleration: 32 in/s²
- minimum traction coefficient used only for this check: 0.25
- gearbox efficiency: 0.90
- normal-force command: 100 lbf per driven roller.

Derived:

- inertial force ≈ `8.288 lbf`
- total demanded longitudinal force ≈ `28.288 lbf`
- required roller torque at 2.25 in radius ≈ `7.191 Nm`
- required motor torque through 40:1 at 90% efficiency ≈ `0.200 Nm`
- AM8022 rated torque = `0.70 Nm`
- gearbox nominal output rating = `18 Nm`
- 200 lbf total normal × μ0.25 gives 50 lbf modeled traction ceiling, about `12.711 Nm` at the rollers.

The ordinary component ratings therefore exceed this modeled requirement. **The coefficient of friction and actual clamp/traction behavior remain commissioning tests.**

---

## 14. Tool/station engineering

### 14.1 Saw

For the independent reference trace, one PCM508 automatic pneumatic cycle is conservatively set to **2.0 s**, derived from the manufacturer's/dealer's low published rate of 30 cycles/min. The published faster end, 45/min, would be 1.333 s, but is not used.

The Store model's 3.1226 s saw cycle and the reference saw's 2.0 s cycle are different models. Neither is silently rewritten.

### 14.2 Spot Z cycle

`NEW_REFERENCE_SELECTION` motion caps:

- Z rapid velocity = 1.5 in/s
- Z rapid acceleration = 20 in/s²
- cutting feed = Store-equivalent 24 in/min = 0.4 in/s
- safe = 2.000 in
- approach = 1.550 in
- final tool-tip = 1.256169317 in.

Using the same trapezoidal/triangular calculation:

- safe → approach, 0.450 in = `0.375000 s`
- approach → target, 0.293830683 in at cutting feed = `0.754576708 s`
- target → safe, 0.743830683 in = `0.570887122 s`
- one Z spot cycle = `1.700463830 s`
- two = `3.400927659 s`.

Y goes 0 → 1.75 once before SPOT-1 and remains at 1.75 while X repositions for SPOT-2; after SPOT-2 it returns 1.75 → 0. Total Y motion = `2 × 0.6875 = 1.375 s`.

Nakanishi documentation provides a speed-achieved/monitoring interface but not a universal guaranteed spin-up interval for this assembled cell. The reference trace therefore includes a visible **1.0 s MODELED ENGINEERING ASSUMPTION** to reach/confirm the configured 3,000 rpm speed before Z cutting motion. Physical software must wait on the real speed-confirmed signal with a timeout; it must not use a blind one-second delay as proof of speed.

---

## 15. Electrical and network architecture

Reference block architecture:

```text
480 VAC 3φ source
  → lockable Eaton DH362URK disconnect
  → engineered branch protection / distribution
      → Cantek SAW-L OEM electrical interface
      → Cantek SAW-R OEM electrical interface
      → Beckhoff AX8620 DC-link supply
           → AX8206 Safe Motion → X feed AM8022
           → AX8206 Safe Motion → Y tool AM8022
           → AX8108 Safe Motion → Z tool AM8022
      → appropriate branch/transformer for Nakanishi E3000
      → router/VFD branch when milling head installed
      → Phoenix QUINT 24 VDC control supply
           → CX5340
           → EtherCAT I/O
           → sensors / interposing devices

EtherCAT:
CX5340 → AX8000 → EtherCAT terminals
          ↘ FSoE / TwinSAFE safety telegrams

Application/network side:
System/Store may deliver an identified job package before Cycle Start.
Network communication is never the real-time servo loop.
```

Any actual North American panel requires conductor, overcurrent, SCCR, grounding/bonding, enclosure, motor-circuit and local-code engineering by qualified personnel. This document does not declare an assembled-panel listing.

---

## 16. Safety architecture — component capability, not validation

Reference safety functions to be engineered and validated:

- emergency stop;
- access/guard locking;
- drive Safe Torque Off and other selected Safe Motion functions as justified by risk assessment;
- pneumatic safe exhaust / unexpected-start prevention;
- restart prevention;
- local mode selection;
- local Cycle Start;
- fault reset separated from start;
- safe state for loss of guard, E-stop, pressure, drive safety or safety-controller health;
- lockout/tagout points for electrical and pneumatic energy.

Selected EL6910/EL1904/EL2904, AX8000 Safe Motion variants, Schmersal AZM300 and Festo MS6-SV-E have manufacturer-stated safety capabilities. **The assembled D-001 machine is not thereby Cat 4, PL e, SIL 3 or otherwise validated.** Required risk assessment, architecture selection, calculations, wiring review and validation remain professional work before energization.

---

## 17. Axis list

| Axis | Physical function | Drive / motor | Units | Reference |
| --- | --- | --- | --- | --- |
| X_FEED | common rotation of R1/R2 to translate board along fence | AX8206 ch1 / AM8022 / AG2250 40:1 | inches of board travel | controller calibrated; **Datum C only earned by reference cut** |
| Y_TOOL | move x=36 tooling carriage across board width | AX8206 ch2 / AM8022 / HIWIN KK | in from fence A | home/reference switch at Y0 |
| Z_TOOL | move spot/router tool tip toward/away from board | AX8108 / AM8022 / HIWIN KK | tool-tip in above table B | home/reference plus calibrated tool length |
| Y_END | future x=-6 end-tool carriage | not frozen in this Project 1 pass | in | `UNRESOLVED` |
| Z_END | future x=-6 end-tool plunge | not frozen in this Project 1 pass | in | `UNRESOLVED` |

Project 1 requires only X/Y_TOOL/Z_TOOL.

---

## 18. I/O map

Exact EtherCAT channel assignment is a machine-build deliverable; semantic I/O is frozen here so the controller program has no anonymous bits.

| Tag | Type | Meaning | Required for automatic motion? |
| --- | --- | --- | --- |
| `siSafetyOk` | safe derived | TwinSAFE permissive summary for standard sequence | yes; safety action itself remains in TwinSAFE |
| `diAutoMode` | DI | local AUTO selected | yes |
| `diCycleStart` | DI | local momentary Cycle Start | yes |
| `diReset` | DI | local fault reset | recovery only |
| `diJobLinkHealthy` | DI/software | upstream job transport healthy before start | yes before start; not real-time loop |
| `diStockPresent` | DI | expected board present | yes |
| `diFenceSeated` | DI | board seated against Datum A | yes |
| `diClampPressureOk` | DI | commanded roller/clamp pressure achieved | yes |
| `diSawAngle30Ok` | DI | SAW-L setup verified at 30° | yes for Project 1 |
| `diSawRetracted` | DI | SAW-L clear/retracted | yes |
| `diSawCycleDone` | DI | approved OEM cycle completion handshake | yes |
| `diSpotSpeedOk` | DI | E3000 speed-achieved/ready condition | yes before plunge |
| `diToolIdentitySpot` | DI | 3/16 spot head/tool identity confirmed | yes |
| `diYHome` | DI | Y reference cam | reference |
| `diZHome` | DI | Z reference cam | reference |
| `doClampDown` | DO | command pneumatic roller pressure | yes |
| `doSawCycleRequest` | DO | request approved PCM508 automatic cycle interface | yes |
| `doSpotRun` | DO | E3000 motor run request | spot only |
| `doSpotSpeedSelect` | DO/field | select configured 3000 rpm preset | spot only |
| `doLabelReady` | DO/software | result record says label may be produced | completion |

No remote application bit maps directly to `MC_MoveAbsolute`, a saw valve, or an axis jog.

---

## 19. Machine state model

Primary states:

`POWER_OFF → BOOT → NOT_READY ↔ MANUAL → REFERENCE_REQUIRED → READY → LOAD_REQUIRED → REFERENCE_ESTABLISHING → POSITION_VALID → AUTO_READY → RUNNING → COMPLETE`.

Fault branches: `FAULT`, `SAFETY_STOP`, `RECOVERY`.

Rules:

- Safety loss has priority over normal sequence.
- Job identity mismatch refuses AUTO_READY.
- Position validity is separate from NC encoder calibration.
- Datum C becomes valid only after a successful reference cut and `MC_SetPosition` completion.
- Any loss of clamp/fence/traction assumptions requiring re-reference invalidates C.
- Network loss before local Cycle Start blocks start.
- Network loss during RUNNING does not become a remote real-time motion event: the already validated local job can complete under local controller/safety authority unless another local fault occurs. No new job may start until communication/identity is restored.
- Local Cycle Start is mandatory. Remote software cannot assert it.

---

## 20. Lowering / compiler architecture

| Stage | Representation | Owner | Failure behavior |
| --- | --- | --- | --- |
| 1 | `SYO-USER1-XBRACE/0.1` confirmed definition | System | no definition → no demand |
| 2 | physical demand with parts/features/ops | System semantic contract | unresolved meaning → no Store-ready job |
| 3 | Store evaluation / material + envelope + Q | Store | unsupported/unavailable/unresolved → refuse/no Q |
| 4 | `D001-LOCAL-JOB-0.1` machine-neutral accepted job package | machine-local importer | pin/hash/config mismatch → no load |
| 5 | station transform table + tool identities | machine configuration | missing station/tool → lowering failure |
| 6 | `D001-MOTION-IR-0.1` ordered targets/handshakes | deterministic local lowering | bounds/identity failure → no program |
| 7 | TwinCAT PLC/NC source + project config | machine implementation | build error → no deployable artifact |
| 8 | TwinCAT XAE build / activation | machine implementation | compiler/config error → no run |
| 9 | local runtime + TwinSAFE + Cycle Start | commissioned machine only | safety/readiness failure → no motion |

No AI interpretation is allowed between accepted local job identity and Cycle Start.

### 20.1 Project 1 `D001-MOTION-IR-0.1`

```text
CHECK JOB=SYO-USER1-XBRACE VERSION=0.1 STORE_PIN=9c62d9d...
CHECK TOOL=SPOT_3_16_118DEG
CHECK SAW_L_ANGLE=30deg
LOAD_SEAT_CLAMP
SAW_CYCLE SAW-L                     ; establishes fresh reference face
SET_C 0
START_SPOT_SPINDLE preset=3000rpm; WAIT_SPEED_OK
MOVE_X C=28.000000 V=8 A=32
MOVE_Y Y=1.750000 V=4 A=16
MOVE_Z 1.550000 rapid
MOVE_Z 1.256169317 feed=0.4
MOVE_Z 2.000000 rapid
MOVE_X C=11.875000 V=8 A=32         ; Y stays at 1.75
MOVE_Z 1.550000 rapid
MOVE_Z 1.256169317 feed=0.4
MOVE_Z 2.000000 rapid
MOVE_Y Y=0
STOP_SPOT_SPINDLE
MOVE_X C=-16.000000 V=8 A=32
SAW_CYCLE SAW-L
SET_C 0                              ; fresh cutoff face
MOVE_X C=-16.000000 V=8 A=32
SAW_CYCLE SAW-L
SET_C 0
CHECK_REMAINDER expected=27.625 min=24
RELEASE
SIGNAL_LABEL_READY
COMPLETE
```

---

## 21. Actual controller environment

Reference engineering target:

- controller: Beckhoff `CX5340-0195`
- runtime: TwinCAT 3 XAR on the CX5340 option selected above
- engineering: TwinCAT 3.1 Build 4026 family, XAE / XAE Shell on Windows
- PLC language: IEC 61131-3 Structured Text
- motion library: `Tc2_MC2`
- axis interface: TwinCAT NC `AXIS_REF`
- fieldbus: EtherCAT / CoE to AX8000
- safety engineering: TwinCAT 3 Safety Editor / FSoE / TwinSAFE
- motion FBs used below: `MC_Power`, `MC_Reset`, `MC_Home`, `MC_SetPosition`, `MC_MoveAbsolute`, `MC_Stop`.

Beckhoff documents that `MC_MoveAbsolute` takes absolute position, velocity, acceleration, deceleration and jerk; `MC_Power` provides software enable but does not replace hardware enable; `MC_SetPosition` can set the current NC position; and MC blocks must be called cyclically while busy.

**Compiler status for this investigation: NOT COMPILED.** No licensed/installed TwinCAT XAE compiler/runtime was available in the investigation environment. Therefore this document does not say “compiled successfully.” The source below is a reference source body reviewed against current Beckhoff function-block signatures, followed by a deterministic independent trace. Before deployment it must be imported into an actual TwinCAT 4026 XAE project, bound to real axes/I/O, built without error, activated against the exact runtime and then commissioned.

---

## 22. Actual Project 1 TwinCAT Structured Text reference source

The following is controller source, not G-code and not a remote application command. Hardware I/O symbols are linked to EtherCAT channels in the TwinCAT project; safety outputs are owned by TwinSAFE, not this standard PLC program.

```iecst
{attribute 'qualified_only'}
TYPE E_D001State :
(
    POWER_OFF,
    BOOT,
    NOT_READY,
    REFERENCE_REQUIRED,
    READY,
    LOAD_REQUIRED,
    REFERENCE_ESTABLISHING,
    POSITION_VALID,
    AUTO_READY,
    RUN_SPINDLE_START,
    RUN_X_SPOT1,
    RUN_Y_SPOT,
    RUN_Z1_APPROACH,
    RUN_Z1_CUT,
    RUN_Z1_RETRACT,
    RUN_X_SPOT2,
    RUN_Z2_APPROACH,
    RUN_Z2_CUT,
    RUN_Z2_RETRACT,
    RUN_Y_RETRACT,
    RUN_X_CUT1,
    RUN_SAW_CUT1,
    RUN_REBASE1,
    RUN_X_CUT2,
    RUN_SAW_CUT2,
    RUN_REBASE2,
    RUN_RELEASE,
    COMPLETE,
    FAULT,
    SAFETY_STOP,
    RECOVERY
);
END_TYPE

TYPE ST_D001Project1Identity :
STRUCT
    JobId               : STRING(32);
    ConfigurationId     : STRING(32);
    ConfigurationVer    : STRING(16);
    SystemRevision      : STRING(40);
    StorePin            : STRING(40);
    StoreInputHash      : STRING(64);
    StoreResultHash     : STRING(64);
END_STRUCT
END_TYPE

VAR_GLOBAL
    AxisX : AXIS_REF;
    AxisY : AXIS_REF;
    AxisZ : AXIS_REF;

    (* Standard/control inputs. Safety logic is evaluated independently in TwinSAFE. *)
    siSafetyOk          : BOOL;
    diAutoMode          : BOOL;
    diCycleStart        : BOOL;
    diReset             : BOOL;
    diJobLinkHealthy    : BOOL;
    diStockPresent      : BOOL;
    diFenceSeated       : BOOL;
    diClampPressureOk   : BOOL;
    diSawAngle30Ok      : BOOL;
    diSawRetracted      : BOOL;
    diSawCycleDone      : BOOL;
    diSpotSpeedOk       : BOOL;
    diToolIdentitySpot  : BOOL;
    diYHome             : BOOL;
    diZHome             : BOOL;

    doClampDown         : BOOL;
    doSawCycleRequest   : BOOL;
    doSpotRun           : BOOL;
    doSpotSpeedSelect   : BOOL;
    doLabelReady        : BOOL;
END_VAR

PROGRAM MAIN
VAR CONSTANT
    cXVel       : LREAL := 8.0;        (* 480 in/min *)
    cXAcc       : LREAL := 32.0;
    cYVel       : LREAL := 4.0;        (* 240 in/min *)
    cYAcc       : LREAL := 16.0;
    cZRapidVel  : LREAL := 1.5;
    cZRapidAcc  : LREAL := 20.0;
    cZFeedVel   : LREAL := 0.4;        (* 24 in/min *)
    cZFeedAcc   : LREAL := 20.0;
    cXSpot1     : LREAL := 28.0;
    cXSpot2     : LREAL := 11.875;
    cXCut       : LREAL := -16.0;
    cYSpot      : LREAL := 1.75;
    cZSafe      : LREAL := 2.0;
    cZApproach  : LREAL := 1.55;
    cZSpot      : LREAL := 1.256169317;
    cRemainder  : LREAL := 27.625;
    cMinRemain  : LREAL := 24.0;
END_VAR
VAR
    st                  : E_D001State := E_D001State.BOOT;
    ident               : ST_D001Project1Identity := (
        JobId := 'PROJECT1-16',
        ConfigurationId := 'SYO-USER1-XBRACE',
        ConfigurationVer := '0.1',
        SystemRevision := 'b6c7fbcb9d618e600eca0e46dc10374db6d2ecfc',
        StorePin := '9c62d9d6f7775deef83d47196d32c9b5174a352c',
        StoreInputHash := 'bea3c0b3841d013b463277ebaa02121bef79b65abe5e46b05a40f337afa3b868',
        StoreResultHash := '0fd6b7d19ef8f64d133486c9d2ccf72256b2993bb60aa14c77b3c3e8004973bc');

    bAxisEnable         : BOOL;
    bMoveX              : BOOL;
    bMoveY              : BOOL;
    bMoveZ              : BOOL;
    bSetX               : BOOL;
    bHomeY              : BOOL;
    bHomeZ              : BOOL;
    bForceCalX          : BOOL;
    bResetAxes          : BOOL;
    bStopAxes           : BOOL;
    bSawIssued          : BOOL;
    bCycleStartLatched  : BOOL;
    bPositionValid      : BOOL;
    bJobIdentityValid   : BOOL := TRUE; (* importer sets FALSE on any identity/hash mismatch *)

    xTarget             : LREAL;
    xVel                : LREAL;
    xAcc                : LREAL;
    yTarget             : LREAL;
    yVel                : LREAL;
    yAcc                : LREAL;
    zTarget             : LREAL;
    zVel                : LREAL;
    zAcc                : LREAL;

    fbPowerX            : MC_Power;
    fbPowerY            : MC_Power;
    fbPowerZ            : MC_Power;
    fbResetX            : MC_Reset;
    fbResetY            : MC_Reset;
    fbResetZ            : MC_Reset;
    fbHomeX             : MC_Home;
    fbHomeY             : MC_Home;
    fbHomeZ             : MC_Home;
    fbSetX              : MC_SetPosition;
    fbMoveX             : MC_MoveAbsolute;
    fbMoveY             : MC_MoveAbsolute;
    fbMoveZ             : MC_MoveAbsolute;
    fbStopX             : MC_Stop;
    fbStopY             : MC_Stop;
    fbStopZ             : MC_Stop;
END_VAR

(* Default commands: individual states assert only what they own. *)
bMoveX := FALSE;
bMoveY := FALSE;
bMoveZ := FALSE;
bSetX := FALSE;
bHomeY := FALSE;
bHomeZ := FALSE;
bForceCalX := FALSE;
bResetAxes := FALSE;
bStopAxes := FALSE;
doSawCycleRequest := FALSE;
doLabelReady := FALSE;

IF NOT siSafetyOk THEN
    bPositionValid := FALSE;
    st := E_D001State.SAFETY_STOP;
END_IF;

bAxisEnable := siSafetyOk AND diAutoMode AND
               (st <> E_D001State.FAULT) AND
               (st <> E_D001State.SAFETY_STOP);

CASE st OF

E_D001State.BOOT:
    doClampDown := FALSE;
    doSpotRun := FALSE;
    doSpotSpeedSelect := FALSE;
    bPositionValid := FALSE;
    IF siSafetyOk THEN st := E_D001State.REFERENCE_REQUIRED; END_IF;

E_D001State.REFERENCE_REQUIRED:
    (* X receives controller calibration without granting workpiece Datum C validity. *)
    bForceCalX := NOT fbHomeX.Busy AND NOT fbHomeX.Done;
    bHomeY := NOT fbHomeY.Busy AND NOT fbHomeY.Done;
    bHomeZ := NOT fbHomeZ.Busy AND NOT fbHomeZ.Done;
    IF fbHomeX.Done AND fbHomeY.Done AND fbHomeZ.Done THEN
        st := E_D001State.READY;
    END_IF;

E_D001State.READY:
    IF diAutoMode AND bJobIdentityValid AND diJobLinkHealthy THEN
        st := E_D001State.LOAD_REQUIRED;
    END_IF;

E_D001State.LOAD_REQUIRED:
    doClampDown := TRUE;
    IF diStockPresent AND diFenceSeated AND diClampPressureOk AND
       diSawAngle30Ok AND diSawRetracted AND diToolIdentitySpot THEN
        IF diCycleStart THEN
            bCycleStartLatched := TRUE;
            bSawIssued := FALSE;
            st := E_D001State.REFERENCE_ESTABLISHING;
        END_IF;
    END_IF;

E_D001State.REFERENCE_ESTABLISHING:
    doClampDown := TRUE;
    IF NOT bSawIssued THEN
        doSawCycleRequest := TRUE;
        bSawIssued := TRUE;
    END_IF;
    IF bSawIssued AND diSawCycleDone AND diSawRetracted THEN
        bSawIssued := FALSE;
        bSetX := NOT fbSetX.Busy AND NOT fbSetX.Done;
        IF fbSetX.Done THEN
            bPositionValid := TRUE;
            st := E_D001State.POSITION_VALID;
        END_IF;
    END_IF;

E_D001State.POSITION_VALID:
    IF bPositionValid AND bCycleStartLatched THEN
        st := E_D001State.AUTO_READY;
    ELSE
        st := E_D001State.FAULT;
    END_IF;

E_D001State.AUTO_READY:
    IF bPositionValid AND diClampPressureOk AND diFenceSeated THEN
        doSpotSpeedSelect := TRUE;
        doSpotRun := TRUE;
        st := E_D001State.RUN_SPINDLE_START;
    END_IF;

E_D001State.RUN_SPINDLE_START:
    doClampDown := TRUE;
    doSpotSpeedSelect := TRUE;
    doSpotRun := TRUE;
    IF diSpotSpeedOk THEN
        xTarget := cXSpot1; xVel := cXVel; xAcc := cXAcc;
        st := E_D001State.RUN_X_SPOT1;
    END_IF;

E_D001State.RUN_X_SPOT1:
    doClampDown := TRUE; doSpotSpeedSelect := TRUE; doSpotRun := TRUE;
    bMoveX := NOT fbMoveX.Busy AND NOT fbMoveX.Done;
    IF fbMoveX.Done THEN
        yTarget := cYSpot; yVel := cYVel; yAcc := cYAcc;
        st := E_D001State.RUN_Y_SPOT;
    END_IF;

E_D001State.RUN_Y_SPOT:
    doClampDown := TRUE; doSpotSpeedSelect := TRUE; doSpotRun := TRUE;
    bMoveY := NOT fbMoveY.Busy AND NOT fbMoveY.Done;
    IF fbMoveY.Done THEN
        zTarget := cZApproach; zVel := cZRapidVel; zAcc := cZRapidAcc;
        st := E_D001State.RUN_Z1_APPROACH;
    END_IF;

E_D001State.RUN_Z1_APPROACH:
    doClampDown := TRUE; doSpotSpeedSelect := TRUE; doSpotRun := TRUE;
    bMoveZ := NOT fbMoveZ.Busy AND NOT fbMoveZ.Done;
    IF fbMoveZ.Done THEN
        zTarget := cZSpot; zVel := cZFeedVel; zAcc := cZFeedAcc;
        st := E_D001State.RUN_Z1_CUT;
    END_IF;

E_D001State.RUN_Z1_CUT:
    doClampDown := TRUE; doSpotSpeedSelect := TRUE; doSpotRun := TRUE;
    bMoveZ := NOT fbMoveZ.Busy AND NOT fbMoveZ.Done;
    IF fbMoveZ.Done THEN
        zTarget := cZSafe; zVel := cZRapidVel; zAcc := cZRapidAcc;
        st := E_D001State.RUN_Z1_RETRACT;
    END_IF;

E_D001State.RUN_Z1_RETRACT:
    doClampDown := TRUE; doSpotSpeedSelect := TRUE; doSpotRun := TRUE;
    bMoveZ := NOT fbMoveZ.Busy AND NOT fbMoveZ.Done;
    IF fbMoveZ.Done THEN
        xTarget := cXSpot2; xVel := cXVel; xAcc := cXAcc;
        st := E_D001State.RUN_X_SPOT2;
    END_IF;

E_D001State.RUN_X_SPOT2:
    doClampDown := TRUE; doSpotSpeedSelect := TRUE; doSpotRun := TRUE;
    bMoveX := NOT fbMoveX.Busy AND NOT fbMoveX.Done;
    IF fbMoveX.Done THEN
        zTarget := cZApproach; zVel := cZRapidVel; zAcc := cZRapidAcc;
        st := E_D001State.RUN_Z2_APPROACH;
    END_IF;

E_D001State.RUN_Z2_APPROACH:
    doClampDown := TRUE; doSpotSpeedSelect := TRUE; doSpotRun := TRUE;
    bMoveZ := NOT fbMoveZ.Busy AND NOT fbMoveZ.Done;
    IF fbMoveZ.Done THEN
        zTarget := cZSpot; zVel := cZFeedVel; zAcc := cZFeedAcc;
        st := E_D001State.RUN_Z2_CUT;
    END_IF;

E_D001State.RUN_Z2_CUT:
    doClampDown := TRUE; doSpotSpeedSelect := TRUE; doSpotRun := TRUE;
    bMoveZ := NOT fbMoveZ.Busy AND NOT fbMoveZ.Done;
    IF fbMoveZ.Done THEN
        zTarget := cZSafe; zVel := cZRapidVel; zAcc := cZRapidAcc;
        st := E_D001State.RUN_Z2_RETRACT;
    END_IF;

E_D001State.RUN_Z2_RETRACT:
    doClampDown := TRUE; doSpotSpeedSelect := TRUE; doSpotRun := TRUE;
    bMoveZ := NOT fbMoveZ.Busy AND NOT fbMoveZ.Done;
    IF fbMoveZ.Done THEN
        yTarget := 0.0; yVel := cYVel; yAcc := cYAcc;
        st := E_D001State.RUN_Y_RETRACT;
    END_IF;

E_D001State.RUN_Y_RETRACT:
    doClampDown := TRUE; doSpotRun := FALSE; doSpotSpeedSelect := FALSE;
    bMoveY := NOT fbMoveY.Busy AND NOT fbMoveY.Done;
    IF fbMoveY.Done THEN
        xTarget := cXCut; xVel := cXVel; xAcc := cXAcc;
        st := E_D001State.RUN_X_CUT1;
    END_IF;

E_D001State.RUN_X_CUT1:
    doClampDown := TRUE;
    bMoveX := NOT fbMoveX.Busy AND NOT fbMoveX.Done;
    IF fbMoveX.Done THEN bSawIssued := FALSE; st := E_D001State.RUN_SAW_CUT1; END_IF;

E_D001State.RUN_SAW_CUT1:
    doClampDown := TRUE;
    IF NOT bSawIssued THEN doSawCycleRequest := TRUE; bSawIssued := TRUE; END_IF;
    IF bSawIssued AND diSawCycleDone AND diSawRetracted THEN
        bSawIssued := FALSE;
        st := E_D001State.RUN_REBASE1;
    END_IF;

E_D001State.RUN_REBASE1:
    doClampDown := TRUE;
    bSetX := NOT fbSetX.Busy AND NOT fbSetX.Done;
    IF fbSetX.Done THEN
        xTarget := cXCut; xVel := cXVel; xAcc := cXAcc;
        st := E_D001State.RUN_X_CUT2;
    END_IF;

E_D001State.RUN_X_CUT2:
    doClampDown := TRUE;
    bMoveX := NOT fbMoveX.Busy AND NOT fbMoveX.Done;
    IF fbMoveX.Done THEN bSawIssued := FALSE; st := E_D001State.RUN_SAW_CUT2; END_IF;

E_D001State.RUN_SAW_CUT2:
    doClampDown := TRUE;
    IF NOT bSawIssued THEN doSawCycleRequest := TRUE; bSawIssued := TRUE; END_IF;
    IF bSawIssued AND diSawCycleDone AND diSawRetracted THEN
        bSawIssued := FALSE;
        st := E_D001State.RUN_REBASE2;
    END_IF;

E_D001State.RUN_REBASE2:
    doClampDown := TRUE;
    bSetX := NOT fbSetX.Busy AND NOT fbSetX.Done;
    IF fbSetX.Done THEN
        IF cRemainder >= cMinRemain THEN
            st := E_D001State.RUN_RELEASE;
        ELSE
            st := E_D001State.FAULT;
        END_IF;
    END_IF;

E_D001State.RUN_RELEASE:
    doClampDown := FALSE;
    doSpotRun := FALSE;
    doSpotSpeedSelect := FALSE;
    doLabelReady := TRUE;
    bCycleStartLatched := FALSE;
    bPositionValid := FALSE;
    st := E_D001State.COMPLETE;

E_D001State.COMPLETE:
    doClampDown := FALSE;
    doLabelReady := TRUE;

E_D001State.SAFETY_STOP:
    (* TwinSAFE performs the safety function; standard PLC only removes normal requests. *)
    doClampDown := FALSE;
    doSpotRun := FALSE;
    doSpotSpeedSelect := FALSE;
    bStopAxes := TRUE;
    IF siSafetyOk AND diReset THEN st := E_D001State.RECOVERY; END_IF;

E_D001State.FAULT:
    bPositionValid := FALSE;
    doClampDown := FALSE;
    doSpotRun := FALSE;
    doSpotSpeedSelect := FALSE;
    bStopAxes := TRUE;
    IF diReset AND siSafetyOk THEN bResetAxes := TRUE; st := E_D001State.RECOVERY; END_IF;

E_D001State.RECOVERY:
    bPositionValid := FALSE;
    IF siSafetyOk THEN st := E_D001State.REFERENCE_REQUIRED; END_IF;

ELSE
    st := E_D001State.FAULT;
END_CASE;

(* Cyclic motion-function-block calls. *)
fbPowerX(Axis := AxisX, Enable := bAxisEnable, Enable_Positive := TRUE,
         Enable_Negative := TRUE, Override := 100.0, BufferMode := MC_Aborting);
fbPowerY(Axis := AxisY, Enable := bAxisEnable, Enable_Positive := TRUE,
         Enable_Negative := TRUE, Override := 100.0, BufferMode := MC_Aborting);
fbPowerZ(Axis := AxisZ, Enable := bAxisEnable, Enable_Positive := TRUE,
         Enable_Negative := TRUE, Override := 100.0, BufferMode := MC_Aborting);

fbResetX(Axis := AxisX, Execute := bResetAxes);
fbResetY(Axis := AxisY, Execute := bResetAxes);
fbResetZ(Axis := AxisZ, Execute := bResetAxes);

fbHomeX(Axis := AxisX, Execute := bForceCalX, Position := 0.0,
        HomingMode := MC_ForceCalibration, bCalibrationCam := FALSE);
fbHomeY(Axis := AxisY, Execute := bHomeY, Position := 0.0,
        HomingMode := MC_DefaultHoming, bCalibrationCam := diYHome);
fbHomeZ(Axis := AxisZ, Execute := bHomeZ, Position := cZSafe,
        HomingMode := MC_DefaultHoming, bCalibrationCam := diZHome);

fbSetX(Axis := AxisX, Execute := bSetX, Position := 0.0, Mode := FALSE);

fbMoveX(Axis := AxisX, Execute := bMoveX, Position := xTarget,
        Velocity := xVel, Acceleration := xAcc, Deceleration := xAcc,
        Jerk := 0.0, BufferMode := MC_Aborting);
fbMoveY(Axis := AxisY, Execute := bMoveY, Position := yTarget,
        Velocity := yVel, Acceleration := yAcc, Deceleration := yAcc,
        Jerk := 0.0, BufferMode := MC_Aborting);
fbMoveZ(Axis := AxisZ, Execute := bMoveZ, Position := zTarget,
        Velocity := zVel, Acceleration := zAcc, Deceleration := zAcc,
        Jerk := 0.0, BufferMode := MC_Aborting);

fbStopX(Axis := AxisX, Execute := bStopAxes, Deceleration := cXAcc, Jerk := 0.0);
fbStopY(Axis := AxisY, Execute := bStopAxes, Deceleration := cYAcc, Jerk := 0.0);
fbStopZ(Axis := AxisZ, Execute := bStopAxes, Deceleration := cZRapidAcc, Jerk := 0.0);

(* Any motion FB error is fail-closed in the standard state sequence. *)
IF fbMoveX.Error OR fbMoveY.Error OR fbMoveZ.Error OR
   fbHomeX.Error OR fbHomeY.Error OR fbHomeZ.Error OR fbSetX.Error THEN
    bPositionValid := FALSE;
    st := E_D001State.FAULT;
END_IF;
END_PROGRAM
```

### 22.1 Source caveat found during static review

The source above deliberately uses the documented `Tc2_MC2` signatures, but it has **not** been passed through a TwinCAT compiler. Final XAE work must resolve any project-version-specific requirement for optional `Options` structures or namespace qualification, then retain the exact compiled source and build identity. That is a compiler-admission step, not permission to rewrite the numerical targets.

---

## 23. Build / compiler result

| Item | Result |
| --- | --- |
| TwinCAT XAE installed in investigation environment | **No** |
| TwinCAT source compiled | **No** |
| PLC project activated against CX5340 | **No** |
| EtherCAT topology scanned against physical hardware | **No** |
| TwinSAFE project validated | **No** |
| Alternate validation performed | source-signature review + deterministic arithmetic/state trace |

A future build record must name the exact installed TwinCAT 3.1.4026 revision, `Tc2_MC2` version, target runtime revision, library resolution, build result, warnings/errors and resulting project/artifact hash.

---

## 24. Reference controller execution trace

This is a **DETERMINISTIC REFERENCE EXECUTION**, not a physical run and not a TwinCAT simulator run. Times use the selected reference models stated above. Store's 36 s load/seat and 24 s release/label are retained only to isolate machine-cycle differences.

| Seq | Model time end (s) | State/action | Target/result | Project source |
| ---: | ---: | --- | --- | --- |
| 1 | 36.0000 | load / seat / clamp | SPF 2×4 ×60 seated A/B | parent demand |
| 2 | 38.0000 | reference saw cycle | SAW-L 30° complete | datumC=`REFERENCE_CUT` |
| 3 | 39.0000 | spot spindle ready assumption | 3000 rpm confirmed in model | spot requirement |
| 4 | 42.7500 | X index | C=28.000 | SPOT-1 workpiece X=8 at station36 |
| 5 | 43.4375 | Y index | Y=1.750 | centered 3.5 in wide face |
| 6 | 45.1380 | Z spot 1 | tip 1.256169 then safe | SPOT-1 full-diameter depth rule |
| 7 | 47.4036 | X index | C=11.875 | SPOT-2 workpiece X=24.125 |
| 8 | 49.1041 | Z spot 2 | tip 1.256169 then safe | SPOT-2 |
| 9 | 49.7916 | Y retract | Y=0 | station clear |
| 10 | 53.5259 | X index | C=-16 | PART-1 length 16 |
| 11 | 55.5259 | saw cutoff 1 | 30° complete | PART-1 cutoff |
| 12 | 55.5259 | rebase C | C=0 at fresh face | `FRESH_CUT_FACE` |
| 13 | 57.7759 | X index | C=-16 | PART-2 length 16 |
| 14 | 59.7759 | saw cutoff 2 | 30° complete | PART-2 cutoff |
| 15 | 59.7759 | rebase C | C=0 | fresh remainder face |
| 16 | 83.7759 | release / label interval | remnant 27.625; label-ready | Store handling comparison assumption |

Feature trace is complete: the two 8 in spots and both 16 in finished parts have a unique definition → workpiece coordinate → station transform → NC target → motion/tool action path.

---

## 25. Reference cycle-time derivation

```text
T_HANDLING_LOAD       = 36.000000000 s   Store model retained for comparison
T_REFERENCE_SAW       =  2.000000000 s   30 cuts/min conservative PCM508 rate
T_SPINDLE_READY       =  1.000000000 s   modeled assumption; runtime waits real signal
T_X_INDEX             = 12.000000000 s   same Store velocity/acceleration, selected drivetrain supports it
T_Y_TOTAL             =  1.375000000 s   out once + back once
T_Z_SPOT_TOTAL        =  3.400927659 s   two derived Z cycles
T_CUTOFF_SAWS         =  4.000000000 s   two additional PCM508 cycles
T_HANDLING_RELEASE    = 24.000000000 s   Store model retained for comparison
-----------------------------------------------------------------
T_REFERENCE_MACHINE   = 83.775927659 s
                       = 1.396265461 min
```

Difference from current Store model:

`83.775927659 - 85.362029985 = -1.586102326 s`.

The near agreement is **not** treated as physical validation. The reference saw is faster than the Store saw model by about 3.368 s across three cuts, while the explicit Y/Z/spindle spot implementation is about 1.782 s slower than the Store's two spot intervals, producing the net difference above.

---

## 26. Q reconciliation

### 26.1 Current authority

```text
CURRENT PINNED STORE Q
Material                         $2.61
Store modeled machine service   $5.93
Q                                $8.54
```

### 26.2 Timing-only reference check using the **existing** Store rate

```text
83.775927659 s / 3600 × $250/h = $5.81777 → $5.82
$2.61 + $5.82 = $8.43
```

`REFERENCE_IMPLEMENTATION_TIMING_CHECK = $8.43`  
Delta from Store Q = `-$0.11`.

This does not create a second pricing engine. It asks only: *if the Store retained its own sell rate but later adopted this reference timing, what arithmetic difference would result?*

---

## 27. Independent reference economic check

Because public prices are unavailable for many industrial components and machine-builder integration dominates a prototype, this is a sensitivity study, not a hidden replacement Store rate.

| Scenario | Installed-capital assumption | Life | Operator | Facility/admin | Maint/tooling | Energy/dust/IT | Productive h | Derived sell rate at 20% GM | Project1 Q using 83.7759 s |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Low | $120,000 | 10 y | $40k | $15k | $8k | $7k | 900 | $113.89/h | $5.26 |
| Base | $165,000 | 7 y | $50k | $20k | $12k | $10k | 600 | $240.77/h | $8.21 |
| High | $220,000 | 5 y | $70k | $30k | $20k | $15k | 400 | $559.38/h | $15.63 |

The current Store rate `$250/h` lies close to this deliberately transparent base scenario, but that is **not validation**. The range demonstrates that utilization, integration capital and labor assumptions dominate economics. Actual quotes and Store observations must replace these scenario inputs before adoption.

---

## 28. Assembly definition

Reference assembly sequence at engineering level:

1. Fabricate and inspect the common base/frame/table structure.
2. Establish Datum B support plane and Datum A fence from the same surveyed structure.
3. Install idler/support rollers so they support stock without redefining A/B.
4. Install R1 at X=24 and R2 at X=48 with common-drive shaft, bearings, wheels and pneumatic down-force assemblies.
5. Install X servo/gear transmission; guard all rotating drivetrain elements.
6. Mount SAW-L at X=0 and SAW-R at X=72; align blade planes to the common machine reference; install OEM-approved control interfaces and guarding.
7. Install x=36 Y/Z tooling carriage; establish machine-surveyed station X and calibrated Y/Z reference sensors.
8. Install spot spindle/tool interface and tool-ID sensing; commission router head only as a separate tool-configuration step.
9. Build the x=-6 end-tool carriage only after its exact axis/BOM is separately frozen; it is not required for Project 1.
10. Install electrical enclosure, disconnect, drives, controller, I/O and 24 VDC supply under qualified panel engineering.
11. Install pneumatic preparation, safe exhaust, regulators and pressure monitoring.
12. Install guarding/access devices and local operator station.
13. Route power, motor/OCT, EtherCAT, safety and sensor cables by separation classes defined by the electrical design.
14. Perform electrical inspection before powered commissioning.
15. Perform machine risk assessment and safety validation before hazardous powered testing.
16. Only then begin low-energy axis verification, dry-run sequencing, stock traction tests, saw/tool commissioning and part inspection.

A paper assembly sequence is not commissioning.

---

## 29. What does and does not require physical proof

| Proposition | Pre-construction evidence sufficient? | Status / evidence |
| --- | --- | --- |
| AM8022 rated torque/speed | yes | manufacturer specification |
| AG2250 40:1 nominal torque | yes | manufacturer specification |
| AX8000 supports EtherCAT/OCT/Safe Motion options | yes | manufacturer specification |
| TwinCAT provides `MC_MoveAbsolute`, `MC_SetPosition`, etc. | yes | vendor documentation |
| 4.5 in wheel + 40:1 gives 1358 rpm motor at 480 in/min | yes | calculation |
| Project1 workpiece coordinates lower deterministically | yes | source + equations + trace |
| current Store Q is $8.54 | yes, as current software/model fact | pinned Store/System regression |
| reference modeled cycle is 83.7759 s | yes, as model | transparent calculation |
| assembled rollers hold lumber without slip | **no** | physical commissioning |
| actual X accuracy/repeatability | **no** | calibrated measurement |
| actual saw cycle in integrated cell | **no** | physical observation |
| actual 30° miter conformance | **no** | inspection |
| actual full-diameter spot depth repeatability | **no** | inspection |
| guarding achieves required risk reduction | **no** | safety design/validation |
| assembled machine may be released for production | **no** | commissioning + safety + owner authority |

---

## 30. Commissioning delta

| Test | Method | Candidate acceptance criterion | Model fact it can replace | If failed |
| --- | --- | --- | --- | --- |
| X feed scale | traceable linear measurement over multiple travel lengths | criterion to be set by engineering before test | modeled wheel/gear scaling | recalibrate/redesign; no capability promotion |
| X repeatability | repeated bidirectional target tests under representative stock | criterion tied to part tolerance, not invented here | ideal encoder math | no production release |
| traction/slip | encoder vs independent board displacement under worst admitted stock | no lost-position event within accepted tolerance | modeled μ/normal-force assumptions | increase traction/control or reduce envelope |
| reference-face repeatability | repeated reference cut + measurement | criterion derived from part tolerance | Datum C modeled behavior | no position validity claim |
| saw cycle | controller timestamps and high-speed observation | stable bounded cycle within adopted Store model | 2.0 s reference / 3.1226 s Store model | change timing or hardware |
| miter angle | calibrated angle measurement on cut samples | project tolerance to be defined | 30° setup assumption | fix setup/sensing |
| spot X/Y | CMM/jig/caliper method suitable to tolerance | project tolerance to be defined | calculated X/Y targets | correct transform/slip/tooling |
| spot depth | depth-gauge/section sample | project tolerance to be defined around 3/16 full-diameter requirement | modeled Z/tool length | recalibrate Z/tool |
| E-stop/guard/STO/pneumatic dump | validated safety test plan | per approved risk-reduction design | none; cannot be inferred | no hazardous operation |
| network loss | controlled disconnect before/during cycle | no remote-loop dependency; no new cycle after loss | architecture rule | revise controller |

The acceptance tolerances themselves require a deliberate engineering requirement; this document does not invent them after the fact.

---

## 31. Traceability matrices

### 31.1 Definition → machine-neutral instruction → controller target

| Definition fact | Neutral op | D-001 transform | TwinCAT action |
| --- | --- | --- | --- |
| reference cut required | `REFERENCE_CUT` | SAW-L at X0 | saw handshake then `MC_SetPosition(X,0)` |
| SPOT-1 X8 | `SPOT_ON_LOCATION` | 36−8=28 | `MC_MoveAbsolute X=28` |
| spot wide-face center | `SPOT_ON_LOCATION` | 3.5/2=1.75 | `MC_MoveAbsolute Y=1.75` |
| fixed spot depth | `SPOT_ON_LOCATION` | top1.5−(point.056330683+.1875)=1.256169317 | Z approach/feed/retract moves |
| SPOT-2 X8 on second part | `SPOT_ON_LOCATION` | second part start16.125; 36−24.125=11.875 | `MC_MoveAbsolute X=11.875` |
| PART-1 16 in | `MITER_CUTOFF` | 0−16=−16 | `MC_MoveAbsolute X=-16`; saw handshake |
| fresh face | `REBASE_DATUM_C` | C:=0 | `MC_SetPosition(X,0)` |
| PART-2 16 in | `MITER_CUTOFF` | 0−16=−16 | same target after rebase |
| remnant | `RETURN_REMNANT` | 27.625≥24 | completion check |

### 31.2 Controller instruction → physical component

| Controller action | Physical component |
| --- | --- |
| X `MC_MoveAbsolute` | CX/TwinCAT → EtherCAT → AX8206 → AM8022 → AG2250 → common R1/R2 drive wheels |
| Y `MC_MoveAbsolute` | AX8206 → AM8022 → HIWIN Y stage |
| Z `MC_MoveAbsolute` | AX8108 → AM8022 → HIWIN Z stage / tool mount |
| spot run/speed I/O | E3000 → EMS-3060K / 3/16 tool |
| saw-cycle handshake | machine-builder-approved PCM508 control interface |
| clamp command | Festo pneumatic circuit / DSBC cylinders, subject to safety architecture |
| safe permissives | TwinSAFE logic, safe I/O, guard/E-stop/drive/pneumatic safety devices |

### 31.3 Physical action → timing → Q

| Action | Reference time contribution | Q path |
| --- | ---: | --- |
| load/seat | 36 s retained Store assumption | occupied-cell time |
| 4 X indexes | 12 s | occupied-cell time |
| three saws | 6 s | occupied-cell time |
| spindle-ready assumption | 1 s | occupied-cell time |
| Y out/back | 1.375 s | occupied-cell time |
| two Z spot cycles | 3.400927659 s | occupied-cell time |
| release/label | 24 s retained Store assumption | occupied-cell time |
| **reference total** | **83.775927659 s** | timing-only comparison at Store rate → `$5.82` service → `$8.43` comparison |
| **current Store authority** | **85.362029985 s** | Store calculation → `$5.93` service + `$2.61` → **`$8.54`** |

---

## 32. Claims made

1. The exact current Project 1 16 in definition can be lowered deterministically to the D-001 Stage-2 station model without inventing a customer dimension.
2. The current Store calculation reproduces `T_MACHINE=1.4227 min` and `Q=$8.54` from its declared inputs.
3. Mature commercial industrial components exist with published ratings sufficient to make a concrete candidate controller/feed/tool implementation.
4. The selected feed drivetrain has documented speed/torque ratings above the explicit modeled Project 1 demand used here.
5. Beckhoff documents the required PLC/NC motion primitives used by the reference Structured Text source.
6. A deterministic nonphysical reference trace produces 83.7759 s under the stated hardware/model assumptions.

## 33. Claims explicitly not made

This document does **not** claim:

- a D-001 machine has been built;
- the controller source has compiled;
- a TwinCAT runtime or simulator executed it;
- any machine has cut wood;
- any stated tolerance has been measured;
- traction coefficient or slip performance is known;
- the PCM508 has an already-approved remote interface for this integration;
- a complete x=-6 end-mill axis BOM has been frozen;
- the assembled safety system achieves a particular PL/SIL/category;
- the machine is compliant, commissioned or production-ready;
- `$8.43` is a Store quote or replacement Store Q;
- the patent correspondence is a legal conclusion.

---

## 34. Adoption delta

If the owner later chooses to pursue this reference implementation, the following must occur **outside this document** before it can become Store authority:

1. Freeze final motor, HIWIN-stage, shaft/bearing/coupling and enclosure order codes from vendor/machine-builder quotes.
2. Freeze a complete x=-6 end-mill carriage or explicitly narrow the adopted D-001 capability so Store does not claim it.
3. Complete mechanical drawings, tolerance stack, workholding/traction calculations, guarding design, dust design and OEM saw-interface approval.
4. Complete electrical schematics, branch/SCCR/grounding design and panel construction review.
5. Complete formal machine risk assessment and safety design/validation.
6. Build the TwinCAT project with exact 4026 revision, libraries, AX8000 configuration, encoder scaling, I/O mapping and TwinSAFE project; record build/artifact hashes.
7. Commission X/Y/Z and tool/saw handshakes; retain measured evidence.
8. Run the commissioning table above and record measured results.
9. Only then decide whether Store should adopt different machine configuration/timing facts. Any Store change belongs in Store with its own tests and a compatible consuming System verification.
10. Do not repin System merely because a candidate document exists. A later Store adoption and System pin change are separate governed changes.

No System or Store file is authorized for modification by this investigation.

---

## 35. Direct answers to the required questions

1. **What does Project 1 define?** Two 16 in parts from a 60 in Store-origin SPF 2×4 demand; 30° parallel face-miter ends; one center-wide-face 3/16 in spot per part at part-relative 8 in; three saw cuts; long-long outer-edge length datum.
2. **What does Store add?** Material/SKU resolution, represented stock/capability, D-001 station/model facts, timing/economics and the current `$8.54` answer.
3. **Machine-neutral operations?** Load/seat, reference cut, two spot operations, two 16 in miter cutoffs with C rebasing, remnant return, result/label signal.
4. **Required D-001 configuration?** A/B fixed references, dynamic C, SAW-L, R1/R2 feed, x=36 spot carriage and associated controls; Project 1 does not require milling.
5. **Pre-existing machine facts?** The pinned Store envelope/travel/station geometry and modeled motion/economics listed above.
6. **Newly selected facts?** Beckhoff/TwinCAT control family, specific candidate drive train, Cantek saws, Nakanishi spot spindle, HIWIN tool axes and named safety/control components.
7. **Commercial components?** Listed in the BOM; unresolved ordering suffixes are identified instead of invented.
8. **Industrial controller?** Beckhoff CX5340-0195.
9. **Programming environment?** TwinCAT 3.1 Build 4026 family / XAE; exact installed patch still required for the actual build record.
10. **Language?** IEC 61131-3 Structured Text using `Tc2_MC2` motion blocks.
11. **Controller instructions?** Full reference source is included above; principal motion primitives are `MC_Home`, `MC_SetPosition`, `MC_MoveAbsolute`, `MC_Stop`, `MC_Reset`, `MC_Power` plus deterministic tool/saw I/O handshakes.
12. **Actually compiled?** No. Proprietary/vendor environment was not available here; no false compile claim is made.
13. **Actually simulated in TwinCAT?** No. A deterministic independent reference execution trace was performed, not a vendor-runtime simulation.
14. **Complete modeled reference cycle?** 83.775927659 s under the stated assumptions.
15. **Current Store T_MACHINE?** 85.362029985 s = 1.4227005 min.
16. **Current Store Q?** `$8.54`.
17. **Derivation?** `$2.61 + round((85.362029985/3600)×$250,2) = $2.61+$5.93=$8.54`.
18. **Does reference implementation support Store timing assumptions?** It supports the order of magnitude and feed kinematics, but does not validate them physically. Its independent cycle is 1.5861 s shorter.
19. **Where do they differ?** Primarily saw-cycle model versus explicit Y/Z/spindle spot implementation.
20. **What would Store have to change?** Only after measured adoption: its declared machine configuration/timing/economic evidence as appropriate, with Store tests and compatible System consumption; nothing changes merely from this document.
21. **What remains unproven?** Physical fit, traction, accuracy, repeatability, cut/spot quality, actual cycle, OEM integration, safety and commissioning.
22. **What does not require reinvention?** The existence and documented ratings of industrial servo drives/motors, EtherCAT, safety I/O, PLCopen-style motion blocks, pneumatic cut-off saws, linear stages and machine spindles.

---

## 36. Sources

### Current repositories / patents

- https://github.com/GeorgePlattDemo/scan-to-build-system/blob/b6c7fbcb9d618e600eca0e46dc10374db6d2ecfc/apps/stb/shared/user1-xbrace-rule.mjs
- https://github.com/GeorgePlattDemo/scan-to-build-system/blob/b6c7fbcb9d618e600eca0e46dc10374db6d2ecfc/apps/stb/public-build/tests/user1-travel-standard.test.mjs
- https://github.com/GeorgePlattDemo/scan-to-build-store/blob/9c62d9d6f7775deef83d47196d32c9b5174a352c/d001-stage2-envelope.mjs
- https://github.com/GeorgePlattDemo/scan-to-build-store/blob/9c62d9d6f7775deef83d47196d32c9b5174a352c/d001-travel-standard.mjs
- https://github.com/GeorgePlattDemo/scan-to-build-store/blob/9c62d9d6f7775deef83d47196d32c9b5174a352c/store-zero-catalog.json
- https://github.com/GeorgePlattDemo/scan-to-build-system/blob/b6c7fbcb9d618e600eca0e46dc10374db6d2ecfc/docs/patents/PATENT-ALIGNMENT-GATE.md
- U.S. Patent 9,720,401 B2, repository source hash recorded by System.
- U.S. Patent 10,768,609 B2, repository source hash recorded by System.

### Beckhoff / controller / motion

- https://www.beckhoff.com/en-us/products/ipc/embedded-pcs/cx5300-intel-atom-r-x6/cx5340.html
- https://www.beckhoff.com/en-us/products/motion/servo-drives/ax8000-multi-axis-servo-system/ax8620.html
- https://www.beckhoff.com/en-en/products/motion/servo-drives/ax8000-multi-axis-servo-system/ax8206.html
- https://www.beckhoff.com/en-us/products/motion/servo-drives/ax8000-multi-axis-servo-system/ax8108-0200-0000.html
- https://www.beckhoff.com/en-us/products/motion/rotary-servomotors/am8000-servomotors/am8022-wdyz.html
- https://www.beckhoff.com/en-us/products/motion/planetary-gears/ag2250-planetary-gear-units-for-servo-and-stepper-motors/ag2250-ple40-m02-40.html
- https://www.beckhoff.com/en-us/products/i-o/ethercat-terminals/el-ed6xxx-communication/el6910.html
- https://www.beckhoff.com/en-us/products/automation/twinsafe/twinsafe-hardware/el2904.html
- https://infosys.beckhoff.com/content/1033/tcplclib_tc2_mc2/70049419.html (`MC_Power`)
- https://infosys.beckhoff.com/content/1033/tcplclib_tc2_mc2/70050955.html (`MC_Reset`)
- https://infosys.beckhoff.com/content/1033/tcplclib_tc2_mc2/70117515.html (`MC_Home`)
- https://infosys.beckhoff.com/content/1033/tcplclib_tc2_mc2/70052491.html (`MC_SetPosition`)
- https://infosys.beckhoff.com/content/1033/tcplclib_tc2_mc2/70094731.html (`MC_MoveAbsolute`)
- https://infosys.beckhoff.com/content/1033/tcplclib_tc2_mc2/70108555.html (`MC_Stop`)
- https://infosys.beckhoff.com/content/1033/tcplclib_tc2_mc2/70043531.html (general MC function-block rules)
- https://infosys.beckhoff.com/content/1033/tc3_plc_intro/13729845515.html (TwinCAT 3.1 Build 4026)

### Mechanical / tooling / safety components

- https://cantekamerica.com/saws/cut-off-saws/ (Cantek PCM508 family)
- https://www.awmachineryllc.com/products/20-miter-cutoff-saw/ (PCM508 detailed specifications)
- https://en.nakanishi-spindle.com/product/ems-3060k/
- https://en.nakanishi-spindle.com/product/e3000-controller/
- https://hiwin.com/products/single-axis-stages/
- https://hiwin.com/resources/catalogs/
- https://www.teknomotor.com/product/materials/spindles-for-aluminum-materials/5160-a-db-p-er25-pr-rh/
- https://www.sunray-inc.com/online-store/4-50-x-3-50-drive-wheel/
- https://ftp.festo.com/Public/PNEUMATIC/SOFTWARE_SERVICE/DataSheet/1366950.html
- https://ftp.festo.com/public/PNEUMATIC/SOFTWARE_SERVICE/DataSheet/EN_GB/562580.pdf
- https://products.schmersal.com/en_US/azm300z-st-1p2p-103001435
- https://www.se.com/us/en/product/XB5AS8445/
- https://www.phoenixcontact.com/en-us/products/power-supply-quint4-ps3ac24dc20-2904622
- https://www.eaton.com/us/en-us/skuPage.DH362URK.html
- https://www.nvent.com/en-us/hoffman/products/encA60H4812SSLPQT
- https://www.ultimationinc.com/replacement-parts/buy-rollers/24bf-19-conveyor-roller/
- https://www.lovejoy-inc.com/products/jaw-type-couplings/l-type-standard-jaw-coupling/

### Price / availability observations used only where expressly labeled

- Sunray public wheel listing above: `$108.71` observed 2026-10-03.
- Applied Automation Schmersal listing: https://www.appliedautomation.com/part/schmersal/azm300z-st-1p2p/2060086 (`$788`, 6 stock shown when researched).
- Secondary Cantek market observations were approximately `$18.7k–$18.9k`; obtain an actual vendor quote before budgeting.

---

## 37. Closing engineering finding

The current Project 1 chain no longer needs an unspecified “PLC,” “servo,” “CNC” or “machine language” placeholder to explain how the defined job could reach ordinary industrial controls. One concrete reference path now exists from the exact System definition through the exact pinned Store answer to named machine stations, coordinates, Beckhoff NC motion blocks, tool/saw handshakes, modeled timing and Q reconciliation.

What this document has **not** done is turn that reference path into a physical machine fact. That boundary remains load-bearing.

**Information before atoms. NO BLOOD ON WOOD.**
