# D-001 Project 1 controller admission record 0.1

**Status:** engineering correction record for draft PR #26  
**Applies to:** `D001-PROJECT1-REFERENCE-IMPLEMENTATION-Q-0.1.md`  
**Purpose:** identify and close source-admission defects without changing System meaning, Store authority, Store timing/economics, or the current `Q = $8.54` result.

This record is deliberately narrower than the reference implementation document. Where this record conflicts with the controller-source section of the first draft, this record controls until the parent document is consolidated into a later revision.

---

## 1. Fail-closed job identity

The first draft initialized `bJobIdentityValid := TRUE` and relied on an importer to clear it. That is not acceptable for a machine-admission boundary.

The required rule is:

```text
default identity state = INVALID
loaded job bytes -> deterministic parse -> exact comparison -> VALID only if every required identity matches
```

Required comparisons for Project 1:

- `ConfigurationId = SYO-USER1-XBRACE`
- `ConfigurationVersion = 0.1`
- System revision = `b6c7fbcb9d618e600eca0e46dc10374db6d2ecfc`
- Store pin = `9c62d9d6f7775deef83d47196d32c9b5174a352c`
- Store input hash = `bea3c0b3841d013b463277ebaa02121bef79b65abe5e46b05a40f337afa3b868`
- Store result hash = `0fd6b7d19ef8f64d133486c9d2ccf72256b2993bb60aa14c77b3c3e8004973bc`
- declared part count = 2
- declared saw count = 3
- declared spot count = 2
- required tool identity = fixed 3/16 in, 118 degree point spot tool
- required saw setup = 30 degree face-miter at SAW-L.

Any missing, malformed, additional-unrecognized mandatory field, mismatched identity, mismatched hash, or unsupported version leaves identity invalid and prevents `AUTO_READY`.

Reference Structured Text invariant:

```iecst
bJobIdentityValid : BOOL := FALSE;
```

The importer or validation FB may set it true only after all exact comparisons return true in the same accepted job record. There is no permissive fallback.

---

## 2. TwinCAT project-object boundaries

The first draft presented DUT, GVL, and POU source in one Markdown listing for readability. It must not be mistaken for one importable TwinCAT POU.

The reference project should be represented as separate TwinCAT objects:

```text
D001_Project1.tsproj
└─ D001_Project1_PLC.plcproj
   ├─ E_D001State.TcDUT
   ├─ ST_D001Project1Identity.TcDUT
   ├─ GVL_D001_IO.TcGVL
   ├─ GVL_D001_Axes.TcGVL
   ├─ FB_D001JobAdmission.TcPOU
   ├─ FB_D001SawCycle.TcPOU
   └─ MAIN.TcPOU
```

A future compiled build record must retain the exact `.tsproj`, `.plcproj`, DUT/GVL/POU sources, library references, runtime target, and resulting TwinCAT boot/runtime artifact identity. Beckhoff documents the PLC boot application form as `Port_xxx.app`; that artifact is not described here as generic machine code.

---

## 3. State-model correction

The narrative in the first draft listed `MANUAL`, while the AUTO reference source did not implement a MANUAL branch. The corrected boundary is:

- Project 1 automatic production logic does **not** contain unrestricted manual tooling motion.
- Maintenance/setup/jog behavior, if later implemented, belongs to a separate mode-specific POU under locally selected mode, reduced/appropriate motion limits, and the validated safety concept.
- `MANUAL` is therefore not part of this Project 1 automatic state sequence unless and until that separate implementation is designed.

Correct Project 1 AUTO state family:

```text
BOOT
-> REFERENCE_REQUIRED
-> READY
-> LOAD_REQUIRED
-> REFERENCE_ESTABLISHING
-> POSITION_VALID
-> AUTO_READY
-> RUNNING SUBSTATES
-> COMPLETE

fault branches:
FAULT
SAFETY_STOP
RECOVERY
```

This removes the prose/source mismatch without inventing manual control behavior.

---

## 4. Motion command admission: explicit command edges

The first draft used expressions such as:

```iecst
bMoveX := NOT fbMoveX.Busy AND NOT fbMoveX.Done;
```

That pattern is not admitted as production logic merely because it looks plausible. It can interact with previous-cycle `Done` state and PLC scan order in ways that should be proven in the actual TwinCAT runtime.

The corrected design rule is:

1. entering a motion state arms one command exactly once;
2. the `Execute` input receives an explicit rising edge;
3. the state retains ownership while the FB is Busy;
4. only the matching `Done`, `CommandAborted`, or `Error` outcome advances or faults;
5. `Execute` is returned false before another command instance is admitted.

Reference pattern:

```iecst
CASE st OF

RUN_X_SPOT1_ENTER:
    xTarget := 28.0;
    bXCommandIssued := FALSE;
    st := RUN_X_SPOT1;

RUN_X_SPOT1:
    IF NOT bXCommandIssued THEN
        bMoveXExecute := TRUE;          (* rising edge *)
        bXCommandIssued := TRUE;
    ELSE
        bMoveXExecute := FALSE;
    END_IF;

    IF fbMoveX.Done THEN
        st := RUN_Y_SPOT_ENTER;
    ELSIF fbMoveX.CommandAborted OR fbMoveX.Error THEN
        st := FAULT;
    END_IF;
END_CASE;

fbMoveX(
    Axis := AxisX,
    Execute := bMoveXExecute,
    Position := xTarget,
    Velocity := cXVel,
    Acceleration := cXAcc,
    Deceleration := cXAcc,
    Jerk := 0.0,
    BufferMode := MC_Aborting
);
```

Equivalent explicit-entry patterns are required for Y, Z, homing, `MC_SetPosition`, and any other edge-triggered motion FB.

This record does not claim the fragment has been compiled. It states the command-ownership rule the compiled version must satisfy.

---

## 5. Saw handshake correction

Cantek's current PCM508 material establishes a pneumatic saw activated by a foot switch, with optional dual push-button control. It does **not** establish a PLC remote-cycle interface. Therefore no pinout, relay interception, or bypass circuit is invented here.

Any automatic D-001 integration requires an OEM/machine-builder-approved interface that provides at minimum:

- cycle request acceptance;
- saw retracted/clear confirmation;
- cycle-in-progress or equivalent state;
- cycle completion indication;
- fault/not-ready state;
- integration with the validated guard/safety design.

The software handshake must reject a stale completion signal.

Required logical sequence:

```text
precondition: CycleDone = FALSE and SawRetracted = TRUE
issue one cycle request edge
observe request accepted / cycle leaves idle
wait for cycle completion transition
require SawRetracted = TRUE again
then and only then mark the saw operation complete
```

A robust reference FB shape is:

```iecst
TYPE E_SawHandshake : (SAW_IDLE, SAW_WAIT_CLEAR, SAW_PULSE_REQUEST,
                       SAW_WAIT_START, SAW_WAIT_DONE, SAW_VERIFY_RETRACT,
                       SAW_COMPLETE, SAW_FAULT);
END_TYPE
```

No automatic cycle is admitted if `CycleDone` is already high at command entry and the interface cannot prove a new cycle occurred.

---

## 6. Motor part-number correction

The selected motor family can be narrowed for the reference build.

Reference no-brake motor:

`Beckhoff AM8022-0DH0-0000`

Meaning used for this selection:

- AM8022 frame/family;
- D winding;
- H feedback code: 24-bit multi-turn OCT feedback family as documented by Beckhoff;
- smooth shaft;
- no holding brake.

Reference ratings retained from the first document:

- rated torque: 0.70 Nm;
- peak torque: 4.18 Nm;
- rated-speed family value used in the comparison: 8,000 rpm.

The corresponding holding-brake variant `AM8022-0DH1-0000` may exist as a mechanical holding option, but a holding brake is not represented as a validated safety brake. Whether Y/Z require a brake is a machine risk/load analysis and configuration decision, not a catalog-driven safety conclusion.

The Program reference therefore uses `AM8022-0DH0-0000` for the arithmetic unless the eventual machine builder establishes a reason to select a brake-equipped axis variant.

---

## 7. Job-admission FB requirement

The compiled reference project should contain a dedicated deterministic admission POU rather than burying identity logic in `MAIN`.

Functional contract:

```text
INPUT:
  parsed immutable D001-LOCAL-JOB-0.1 record
  installed machine configuration identity
  allowed System revision
  allowed Store pin
  allowed Store input/result hashes
  installed tool identities
  installed station identities

OUTPUT:
  JobValid
  RejectCode
  AcceptedJobIdentity
```

Minimum reject codes:

```text
JOB_MISSING
JOB_SCHEMA_UNSUPPORTED
CONFIGURATION_ID_MISMATCH
CONFIGURATION_VERSION_MISMATCH
SYSTEM_REVISION_MISMATCH
STORE_PIN_MISMATCH
STORE_INPUT_HASH_MISMATCH
STORE_RESULT_HASH_MISMATCH
PART_COUNT_MISMATCH
SAW_COUNT_MISMATCH
SPOT_COUNT_MISMATCH
TOOL_IDENTITY_MISMATCH
SAW_SETUP_MISMATCH
MACHINE_CONFIG_MISMATCH
```

`JobValid` defaults false on every new load attempt and remains false for any unrecognized mandatory condition.

---

## 8. What remains unchanged

These corrections do not change the current pinned Store calculation:

```text
T_MACHINE = 85.362029985 s = 1.4227005 min
material = $2.61
machine service = $5.93
Q = $8.54
```

They also do not change the independent timing arithmetic in the parent document:

```text
reference timing check = 83.775927659 s = 1.396265461 min
comparison at existing Store rate = $8.43
```

The `$8.43` value remains only a timing sensitivity check and is not Store authority.

---

## 9. Admission status after this correction record

The reference architecture is now sufficiently specified to identify what an actual TwinCAT build must contain, but it is still **not admitted as compiled controller software**.

Still required before the controller section can be called build-closed:

1. create the actual TwinCAT project-object set described above;
2. implement fail-closed `FB_D001JobAdmission`;
3. implement explicit edge/state ownership for all MC commands;
4. implement the non-stale OEM saw-cycle FB against an approved physical interface;
5. bind real EtherCAT axes and I/O;
6. resolve exact TwinCAT 4026 patch/library versions;
7. compile with zero errors;
8. record warnings, source hashes, `.app` artifact identity, and target-runtime identity;
9. execute a non-hazardous runtime/simulation test before physical commissioning;
10. keep safety commissioning and machine release separate from ordinary PLC compilation.

Until those steps exist as evidence, the controller source remains `REFERENCE SOURCE / NOT COMPILED`.

---

## 10. Engineering finding

The first full document successfully closes the semantic and arithmetic path from Project 1 to the current Store Q and names a concrete industrial implementation. This admission record prevents that useful result from being weakened by treating plausible controller prose as compiled fact.

The remaining controller work is now specific: exact project objects, exact fail-closed admission, exact command-edge behavior, exact OEM saw handshake, build evidence, and then commissioning evidence. None of those requires changing Project 1, reverse-engineering Q, or proving the general existence of servo motion.
