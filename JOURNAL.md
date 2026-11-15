---
title: "Automated Pharmacy Compounding System"
author: "microwave"
created_at: "2026-06-11"
---

# 2026-11-09: J33 Putting the build in perspective

**Total time spent: 2 hours**

*Milestone 5 | Retrospective build notes*

By the final milestone, the project had the feeder, agitator, carousel, lifted drive, scale feedback, and touchscreen brought together into a prototype. The notes had shifted toward pulse generation, fault reporting, mounting, and wiring. Those last integration details were a lot less simple than the original raise-rotate-lower description made them sound.

Looking back, the failures connect fairly clearly. Sharing motors created the engagement problem. Sugar needed to stay put while idle and stop being added before the scale caught up. Cornstarch needed help both inside the screw and out near the hopper walls. Recipes added another layer where position and completion messages mattered as much as the motion itself.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

The 5 g table is still the strongest numerical result: eight of eight listed runs inside 3%. The 55 mg table is the uncomfortable one: only three of eight. Both belong in the project. Leaving out the small-target failures would give a much cleaner ending and a much less useful picture of the machine.

There are gaps in the archive too. I don't have one confirmed final set matching every software file to the installed hardware, or the full per-ingredient data from an autonomous recipe run. That limits what I can conclude here. It doesn't erase the design work, but it does tell me what evidence to keep next.

## More views

![Current Main workspace SuperStructureAssem. Only one hopper is visible in this assembly view. CAD includes mate or linked-reference warnings; the image is not proof of a fully populated or validated mechanism.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_assembly.jpg)

Current Main workspace SuperStructureAssem. Only one hopper is visible in this assembly view. CAD includes mate or linked-reference warnings; the image is not proof of a fully populated or validated mechanism.

![Full frame, carousel, drive, and screen CAD from M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_4.jpg)

Full frame, carousel, drive, and screen CAD from M4.

## Code for this revision

Exact archived source excerpts. The file labels identify their revisions.

### controller_later.py · lines 107–108

Recovered later Library controller; its settings are distinct from both July snapshots.

```python
MAX_DISPENSE_TIME_S = 120.0
HEARTBEAT_INTERVAL_S = 0.50
```

### app_later.py · lines 1108–1112

Recovered full later Library app; contains automatic recipes, serial discovery, and switch-indexing wording.

```python
                     "limit switch is OPEN in its indent, then press SET CURRENT AS "
                     "SLOT 1. After that one-time setup, START "
                     "will move through the complete recipe automatically.")
        return
    if actuator_position == "UNKNOWN":
```

## Next

The next priority would be freezing one matched configuration and running it repeatedly, with the raw results kept alongside it. Especially at the small target. There's a real prototype and a lot of useful engineering behind it; the remaining job is to make the performance as clear as the mechanism.

<details>
<summary>Notes added while reconstructing this entry</summary>

The integrated system spans feeder and disk CAD, printed interfaces, motor and actuator hardware, driver settings, wiring, the touchscreen app, the mass controller, and separate motion firmware. The archive preserves several real revisions of those elements, but not a confirmed final manifest matching every file to the installed hardware.

Two version boundaries remain especially important. The app describes switch-based indexing while the recovered disk firmware uses counted steps, and the later controller's 120 s timeout is shorter than several recorded powder trials. Those mismatches don't erase the trials; they prevent attributing all earlier results to one assumed final code set.

The intended integrated flow covers reference setup, recipe entry, lift clearance, disk movement, engagement, mass-controlled feeding, and the transition to the next ingredient. The saved app implements that ordering with state and completion checks. The available evidence doesn't include an uncut run and corresponding ingredient-by-ingredient data that establish the complete sequence's measured performance.

Per-item CSV fields in the app can retain target, actual mass, error, remaining amount, and status. Those fields are part of the logging design; they aren't populated test results in this account. Recipe duration, manual interventions, and final mixture measurements are therefore not assigned values that the source doesn't provide.

The strongest numerical distinction remains the target size: eight of eight recorded 5 g trials met 3%, compared with three of eight at 0.055 g. These are single-powder results. The full assembly CAD shows one populated hopper, so its appearance doesn't independently establish the hopper count or success of a physical eight-ingredient demonstration.

My next priorities would be to freeze one matched hardware-and-code configuration, retain a complete integrated run, and repeat fixed-target measurements with controlled conditions. Those experiments would build directly on the documented mechanism and expose whether remaining error came from dispensing variability, feedback timing, positioning, or engagement. They are future work rather than additional completed tests.

</details>

## Sources

- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)
- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)
- [Existing Forge journals](https://forge.hackclub.com/projects/763)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R33_document_the_final_integrated_state_and_identify_exactly_what_was_demonstrated.md)



[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-11-08: J32 Writing down the steps I was already taking for granted

**Total time spent: 2 hours**

*Milestone 5 | Retrospective build notes*

I wrote an operating procedure for someone who hadn't spent all this time in the code. Select powder, load it, tare the scale, enter the mass, start, check the result. Stop if it jams or malfunctions. Then empty and disassemble the contact parts for cleaning.

Putting that into instructions exposed how much setup I could otherwise skip over in a quick explanation. A target number is only useful with the right baseline. An automatic recipe is only useful when the disk and actuator references mean something physically.

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

The later app also loses trust in position after force stop. That means recovery can't just be 'press start again' as though the interrupted move completed. The unknown state belongs in the operating explanation, even if it makes the process less effortless to describe.

The test materials were the eight household powders. A written procedure didn't turn the prototype into a clinically validated machine or establish that every surface was clean enough by a measured criterion. I wanted the instructions to describe what I had, not quietly expand the claims beyond the tests.

## Setup and recovery details

The later recipe app requires a known disk position and a meaningful actuator UP reference. UNKNOWN blocks a run. In the saved reference-based arrangement, physical alignment and SET CURRENT operations establish what the software will treat as its position; the app doesn't automatically sense an actuator top limit.

Force stop marks actuator and disk state unknown. That differs from normal completion and can require the operator to establish references again before continuing. Retaining an old slot number after interrupted motion would assume the disk finished a movement that may have stopped partway through.

Cleaning connects directly to the earlier interface decisions. The contact path includes the hopper interior, agitator, screw, outlet, and receiving area. Combining components removed a joint but left those surfaces to access and inspect. The source procedure calls for disassembly of the hopper and lid and lists an M3 wrench and screwdriver or Allen key among the tools.

## More views

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

This was useful work because it made the hidden assumptions harder to ignore. Setup, recovery, and cleaning were all connected to earlier design decisions. The procedure existed; independent usability and cleaning validation were still separate work.

<details>
<summary>Notes added while reconstructing this entry</summary>

The written SOP covers selecting powder, entering mass, dispensing, stopping, and cleaning. The original single-doser procedure and the later recipe app have different positioning requirements. I treated the documented procedure and later source behavior as distinct stages so a general START instruction didn't conceal the extra references required by the carousel.

The original procedure includes broad performance language and a capacity limit. The measured evidence in this account is narrower: individual household-powder results at 5 g and 0.055 g, including small-dose failures. I've kept that demonstrated range distinct from the hopper capacity target and from any clinical performance claim.

Writing the procedure didn't validate a cleaning chemistry or quantify residual powder. No compatibility study, contamination acceptance measurement, or independent usability trial is preserved in this record. The result of this stage was an operating document, with those additional questions left as future validation work.

</details>

## Sources

- [Standard Operating Procedure: Safely Utilizing and Operating PharmaTech Rx's Doser](https://docs.google.com/document/d/1p1OGP37uR5EISkR5pwSQ_23Vjzx4Qd3G_bUwq5q5h0U/edit)
- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)
- [Existing Forge journals](https://forge.hackclub.com/projects/763)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R32_write_an_operating_and_cleaning_procedure_consistent_with_the_actual_prototype.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-11-08: J31 The wiring needed somewhere to live

**Total time spent: 2 hours**

*Milestone 5 | Retrospective build notes*

Once the parts were on the frame, the wiring needed attention. I printed wire covers, an Arduino cover, and mounting pieces, then secured the connections along the side and concentrated the route around one extrusion.

It was tempting to treat this as the tidy-up at the end. But the motor moved with the lift, the disk rotated, and the cup still needed access. A wire route that looked fine with everything stationary could get in the way somewhere else in the sequence.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

The covers also had to fit actual connectors and leave the boards accessible. Covering a mess without being able to reach the next connection wouldn't make later debugging much nicer.

The notes establish the routing and printed parts, not an electrical-noise measurement or a full endpoint inspection. I can describe the organization change. I can't say a neater cable bundle proved every electrical issue was gone.

## Cable routes and clearance

The cable bundle and actual mounting surface constrained the covers. Internal space, wall thickness, connector exits, and attachment positions affected whether the parts could organize wiring without pinching it or blocking board access. The milestone record identifies the printed parts but doesn't provide all of their feature dimensions.

The lifted drive required a moving cable section, while most electronics stayed on the frame. The moving segment needed enough travel allowance at both UP and DOWN positions. A cable photographed with the actuator in only one position can't show whether it becomes taut or catches during the other part of the stroke.

Cable clearance has to be considered over the full index-and-lift sequence. A route could rub at the disk, pull at a driver or breadboard, obstruct coupling, or cross the cup access area. Those are relevant inspection conditions; a recorded full-travel result for each route isn't available here.

## More views

![Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_superstructure.jpg)

Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.

The wiring had a more deliberate place on the machine now. The moving section was still the part to judge through the whole stroke, not from one nice photo. Packaging only helps if it keeps access and movement workable.

<details>
<summary>Notes added while reconstructing this entry</summary>

M5 notes describe printed wire covers, an Arduino cover, and a breadboard mount, with wiring secured to the side and consolidated around one extrusion. This was a final integration task because the motor, lift, disk, scale, and screen positions determined where the cable routes could run.

The reported change was consolidation and physical support of wiring. The source doesn't establish final wire gauges, terminal specifications, a quantified strain-relief rating, or a measured noise reduction. Those outcomes can't be deduced from the cleaner layout alone.

The assembly views show the wider packaging context, while the notes supply the description of covers and consolidated routing. I retained the actual images without adding a substitute construction sequence for unrecovered channel and enclosure features.

</details>

## Sources

- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)
- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R31_design_protective_covers_and_consolidate_wiring_along_the_frame.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-11-08: J30 Back to a breadboard, but make it fit

**Total time spent: 2 hours**

*Milestone 5 | Retrospective build notes*

The PCB plan hadn't become a stable board, and the full-size breadboard was still awkward to put on the frame. I tried perfboard as a more permanent arrangement. That attempt didn't give me the working connections I needed.

So I went back to a breadboard. Not the most satisfying-looking end to the PCB idea, but I needed to keep changing and testing the circuit. The notes don't identify the exact perfboard fault, so I'm not going to retrofit a solder-bridge story onto it.

![IMG_8167.HEIC Drive preview: breadboard wiring beside an unsoldered perfboard. Supports the board-packaging discussion; does not show a completed failed perfboard circuit.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/photo_perfboard_comparison.jpg)

IMG_8167.HEIC Drive preview: breadboard wiring beside an unsoldered perfboard. Supports the board-packaging discussion; does not show a completed failed perfboard circuit.

I used a half-size breadboard and printed a custom mount to reduce the footprint. That dealt with the immediate physical problem while keeping the connection rows accessible. The circuit could still change without making another permanent board.

This was one of the less glamorous parts of getting the machine together. A working circuit spread across the bench wasn't the same thing as a circuit that could stay on the frame while the mechanisms moved around it.

## Mounting notes

The final mounting response was a half-size breadboard and a custom printed mount. The design task shifted from creating a permanent electrical circuit to constraining an interchangeable board mechanically. Relevant CAD details are the board footprint, retaining edges, access to connection rows, mounting-hole positions, standoff height, and clearance around the frame fasteners.

The mount had to hold the breadboard without covering useful connection rows or making routine changes awkward. Wire movement could pull at contacts, while excessive retention could distort the board. These were packaging constraints on the printed part, rather than evidence of a measured vibration or pullout rating.

## More views

![Electronics schematic proposal from M2. It is not evidence that a PCB was manufactured.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_1.jpg)

Electronics schematic proposal from M2. It is not evidence that a PCB was manufactured.

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

![Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_superstructure.jpg)

Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.

The half-size board and mount were the practical choice for this stage. I still wanted more permanent electronics eventually, but the circuit had to be ready for that. Forcing the PCB plan to look finished wouldn't have made the machine easier to debug.

<details>
<summary>Notes added while reconstructing this entry</summary>

The early PCB plan never reached a finalized design according to M5 notes. As motor control, timers, alarm lines, and the actuator changed, a fixed board layout would have needed repeated revision. The eventual prototype needed an adaptable arrangement that could support continued testing.

A perfboard was tried after the larger breadboard proved bulky and messy. The notes say the perfboard failed to connect, then record returning to a breadboard. That establishes a failed implementation attempt, but doesn't identify whether the failure came from a solder joint, a trace break, a wrong connection, or another electrical cause. The comparison photo shows both arrangements; it doesn't diagnose the failure.

The comparison imagery records the electrical arrangements, and the notes identify the custom mount. Its detailed retaining geometry and a diagnosed perfboard fault aren't preserved. I describe the reported transition and its practical purpose without adding a particular joint failure or an invented mount dimension.

The result was a prototype arrangement that kept the electronics accessible and modifiable. The decision explains why a breadboard remained in the assembled machine despite the earlier PCB proposal. A permanent board could become useful once the circuit stabilized, but it wasn't a prerequisite for completing this integration stage.

</details>

## Sources

- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)
- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R30_drop_the_fixed_board_plan_troubleshoot_perfboard_and_mount_a_half_size_breadboard.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-11-07: J29 Changing speed without uploading another sketch

**Total time spent: 2 hours**

*Milestone 5 | Retrospective build notes*

Recompiling and uploading for every new speed setting was an unnecessary part of the test cycle. I added an interactive speed-test workflow so I could type a rate, observe the response, and try another. The M5 notes describe recording the commanded speed associated with a driver fault too.

That made a stopped motor more informative. Instead of only noticing something had gone wrong, there was a requested operating point to connect to it. I don't have the standalone transcript, though, so there isn't a failure-speed number I can honestly recover from this account.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

The later production firmware has explicit alarm paths: stop motion, latch the fault, report it. Status and the communication watchdog do different jobs. I wanted to keep those distinctions because 'fault handling' can hide quite a few unrelated behaviors.

The alarm message itself stays generic. It doesn't tell me whether the cause was current, temperature, or position error without more information from the driver. I shouldn't turn a useful fault signal into a more detailed diagnosis than it actually provides.

## Alarm and watchdog behavior

The later production firmware does contain concrete fault paths. Auger alarm is pin 7 and disk alarm is pin 6. The auger alarm check reads LOW as a fault while the mechanism is running, stops auger motion, latches faulted state, and emits FAULT DRIVER ALARM. The source uses INPUT_PULLUP and notes that an unconnected alarm line reads HIGH, so an unused input doesn't establish functional driver fault detection.

RESET FAULT clears the latched fault states and stops the auger. STATUS reports the run mode, current frequency, target frequency, and OCR1A. The 2000 ms serial watchdog stops active auger motion if serial contact disappears. These are distinct mechanisms: driver alarm reports the driver signal, status describes configured motion, and watchdog detects lost controller communication.

FAULT DRIVER ALARM identifies the received fault signal, rather than a detailed cause. Without the installed driver's corresponding status information, it doesn't separately diagnose temperature, current, or position error. The active-LOW interpretation in the saved source is a wiring assumption tied to that revision.

Requested frequency, microsteps, acceleration, supply, and powder load all affect how a speed test is interpreted. An unloaded shaft test and an auger moving cornstarch are different operating conditions. I didn't infer a grams-per-second rate or universal speed ceiling from the presence of a regular timer output.

## More views

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

## Code for this revision

Exact archived source excerpts. The file labels identify their revisions.

### timer_controller_later.ino · lines 662–674

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
void checkAlarm() {
  if (augerMode == AUGER_STOPPED || faulted) {
    return;
  }

  // With nothing connected, INPUT_PULLUP reads HIGH and will not fault.
  // Confirm your driver's ALM polarity before wiring this input.
  if (digitalRead(AUGER_ALM_PIN) == LOW) {
    stopAugerImmediate(false);
    faulted = true;
    Serial.println(F("FAULT DRIVER ALARM"));
  }
}
```

### timer_controller_later.ino · lines 635–660

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
void printStatus() {
  Serial.print(F("STATUS MODE="));

  if (augerMode == AUGER_CONTINUOUS) {
    Serial.print(F("CONTINUOUS"));
  } else if (augerMode == AUGER_PULSE) {
    Serial.print(F("PULSE"));
  } else {
    Serial.print(F("STOPPED"));
  }

  Serial.print(F(" CURRENT_HZ="));
  if (augerMode == AUGER_CONTINUOUS) {
    Serial.print(currentContinuousHz);
  } else if (augerMode == AUGER_PULSE) {
    Serial.print(activePulseHz);
  } else {
    Serial.print(0);
  }

  Serial.print(F(" TARGET_HZ="));
  Serial.print(targetContinuousHz);

  Serial.print(F(" OCR1A="));
  Serial.println(OCR1A);
}
```

### timer_controller_later.ino · lines 676–685

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
void updateWatchdog() {
  if (augerMode == AUGER_STOPPED) {
    return;
  }

  if ((uint32_t)(millis() - lastSerialContactMs) > SERIAL_WATCHDOG_MS) {
    stopAugerImmediate(false);
    Serial.println(F("FAULT WATCHDOG"));
  }
}
```

The testing workflow became easier to adjust, and the controller had clearer ways to expose its state. The numerical speed limit is still missing from the archive. What I can keep is the method and the fault logic, without pretending a source-code setting was a measured ceiling.

<details>
<summary>Notes added while reconstructing this entry</summary>

The M5 speed-test workflow accepted a typed speed and recorded the requested rate associated with a driver fault. This reduced recompilation between experiments. The standalone test source and captured output aren't preserved in the available set, so no numerical fault-speed threshold is reconstructed from that description.

Alarm latching, fault reset, status output, and the watchdog are directly visible in the later firmware. The milestone notes separately describe the interactive test version. Together they document a more observable development process, while the missing raw speed trials limit quantitative conclusions.

</details>

## Sources

- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R29_add_driver_alarm_handling_and_an_interactive_motor_speed_test.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-11-06: J28 The pulse generator was another speed limit

**Total time spent: 2 hours**

After changing the drive hardware, I still had to look at what the Arduino was actually asking it to do. The early version toggled STEP in software. The main loop also had commands and timing work to handle, so pulse generation could become a bottleneck of its own.

I moved the later version to hardware timers. Timer1 handled the auger and Timer2 handled the disk. That let the hardware generate the repeated transitions while software still counted finite motions and reported when they ended.

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

The pin change was part of the work, not a footnote. OC1A means the auger STEP output is on pin 9 in this setup, and the disk uses pin 11. Keeping the earlier wiring while loading this firmware would defeat the whole change.

I kept the timer calculation with the configured rates below. It tells me the intended electrical waveform. It doesn't prove the loaded motor can follow every pulse at 20 kHz. Getting the timing source out of the busy loop was one problem; getting the mechanism through resistant powder was still another.

## Timers, pins, and rates

The M5 notes distinguish a basic pulse-generation version from a hardware-timer version. The early July firmware calculates halfPeriodMicros as 500000 divided by the current step rate and toggles STEP in software. That arrangement depends on how often the main loop returns to the timing check. Serial handling, acceleration updates, and other work compete with pulse timing.

The later firmware assigns auger STEP to pin 9, the AVR OC1A output, and uses Timer1 in CTC mode with prescaler 1. The output toggles on each compare match. The source's conversion is frequency = F_CPU divided by twice (OCR1A + 1). On a 16 MHz configuration, 20,000 pulses per second corresponds to OCR1A = 399. This is a calculated timer setting, not a measured maximum loaded motor speed.

Continuous auger motion starts at 2000 Hz and changes by 500 Hz on nominal 10 ms ramp updates. The timer-based settings use 20,000 Hz TURBO for both families, 2400 Hz FREE NORMAL, and 9000 Hz NONFREE NORMAL. These are later parameters and differ from the early July rates; they aren't one speed configuration carried unchanged through the project.

Finite auger pulses enable the Timer1 compare interrupt and count two compare matches per requested step. When the count reaches zero, the interrupt disconnects the timer output and sets a completion flag. The main loop reports completion separately. Hardware creates the waveform while software retains a defined end to the motion and command reporting.

The disk uses Timer2 and pin 11, OC2A, with a prescaler of 64 and its own compare-match count. Timer selection therefore changes the wiring: auger STEP moves from the early pin 2 to pin 9, and disk STEP uses pin 11. The later integrated drive also uses HIGH for enable and LOW for disable. These pin and polarity changes must accompany the firmware change.

## More views

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

## Code for this revision

Exact archived source excerpts. The file labels identify their revisions.

### timer_controller_later.ino · lines 175–192

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
uint16_t frequencyToOcr(uint32_t frequencyHz) {
  if (frequencyHz < 123) {
    frequencyHz = 123;
  }

  // Timer1 CTC, prescaler = 1, OC1A toggles on every compare match.
  // STEP frequency = F_CPU / (2 * (OCR1A + 1)).
  uint32_t ocr = (F_CPU / (2UL * frequencyHz)) - 1UL;

  if (ocr > 65535UL) {
    ocr = 65535UL;
  }
  if (ocr < 1UL) {
    ocr = 1UL;
  }

  return (uint16_t)ocr;
}
```

### timer_controller_later.ino · lines 303–315

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
ISR(TIMER1_COMPA_vect) {
  if (augerMode != AUGER_PULSE || pulseCompareMatchesRemaining == 0) {
    return;
  }

  pulseCompareMatchesRemaining--;

  if (pulseCompareMatchesRemaining == 0) {
    TCCR1A &= ~_BV(COM1A0);
    TIMSK1 &= ~_BV(OCIE1A);
    pulseFinishedFlag = true;
  }
}
```

### timer_controller_later.ino · lines 317–354

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
void updateContinuousRamp() {
  if (augerMode != AUGER_CONTINUOUS) {
    return;
  }

  uint32_t now = millis();
  if ((uint32_t)(now - lastRampUpdateMs) < RAMP_UPDATE_MS) {
    return;
  }
  lastRampUpdateMs = now;

  if (currentContinuousHz == targetContinuousHz) {
    return;
  }

  if (currentContinuousHz < targetContinuousHz) {
    uint32_t next = currentContinuousHz + RAMP_STEP_HZ;
    if (next > targetContinuousHz) {
      next = targetContinuousHz;
    }
    currentContinuousHz = next;
  } else {
    if (currentContinuousHz > RAMP_STEP_HZ) {
      uint32_t next = currentContinuousHz - RAMP_STEP_HZ;
      if (next < targetContinuousHz) {
        next = targetContinuousHz;
      }
      currentContinuousHz = next;
    } else {
      currentContinuousHz = targetContinuousHz;
    }
  }

  noInterrupts();
  setTimerFrequency(currentContinuousHz);
  TCNT1 = 0;
  interrupts();
}
```

This was a more concrete improvement than just raising the requested speed again. I had changed how the waveform was produced. A measured pulse trace paired with a loaded run would be the next way to check both halves of that change; that paired measurement isn't in the saved record.

<details>
<summary>Notes added while reconstructing this entry</summary>

Timer configuration establishes the intended electrical timing, while the motor and powder load determine whether the shaft follows it. The record contains no preserved waveform measurement paired with a loaded-speed series. The configured 20 kHz rate is therefore reported as a command setting, without assigning it the meaning of a demonstrated reliable mechanical limit.

</details>

## Sources

- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)
- [steppermotortest.ino](https://github.com/aaravs-s/pharmatech/blob/main/firmware/steppermotortest.ino)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R28_move_step_generation_from_the_software_loop_to_hardware_timers.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-11-05: J27 Getting the recipe to wait for the mechanisms

**Total time spent: 2 hours**

*Milestone 4 | Retrospective build notes*

Moving from one powder to a recipe made the application more demanding. It had to know the contents of each slot, the requested amount, and where the mechanisms were before it could even start the next dispense.

I used the same basic sequence I had been building mechanically: raise, index, lower, feed. The app waits at the boundaries instead of firing all the commands and assuming the hardware keeps up. If the actuator position is unknown, it doesn't go on with an invented position.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

Cancellation was another awkward edge. The actuator has its own controller, so STOP ALL on the Uno isn't a stop for the whole machine. The app has to reach both devices and stop trusting position after interruption.

For the mass, each ingredient needs a new starting reference. Otherwise powder already in the cup could be mistaken for part of the next addition. The app also has CSV fields for per-item results. I don't have a complete measured recipe tied to one matched final software set here, so those fields are a logging feature rather than a result table I can populate from the single-powder trials.

## The preparation sequence

The later app builds active_run_items from slots with a positive requested amount, preserving each slot's powder name and target. It initializes per-item dispensed, remaining, and status values, computes the total recipe target, clears cancellation events, and begins preparing the first item. That is the data model behind the multi-powder workflow.

The preparation worker first checks cancellation and actuator state. If the actuator is UNKNOWN, it refuses to continue. If it isn't UP, it sends ACTUATOR UP and waits for a motion response with a 70 s timeout. If it is already UP, it checks status and handles the source's declared reference procedure. Only then does it request DISK GOTO for the next item.

Disk motion has a 12 s timeout in the recipe worker. The returned line must contain DONE DISK SLOT with the requested slot number. Once that is confirmed, the app records the slot, checks cancellation again, sends ACTUATOR DOWN, waits for completion, and queues a ready result. The main UI then launches mass dispensing for the item. This is an explicit raise/index/lower/feed chain with completion checks between actions.

The actuator has a separate controller, so Uno STOP ALL doesn't stop every moving mechanism by itself. The app's force-stop route also sends an actuator stop and marks actuator and disk state unknown. Cancellation checks between stages prevent a canceled preparation sequence from proceeding through the remaining actions on its old assumptions.

After all recipe items have dispensed, preparation is called with no next item; the worker raises the actuator and queues completion. The app exports per-item results to CSV, including target, actual mass, error, remaining amount, and status. Those fields can document a real integrated trial, but their presence in source code doesn't prove that such a trial occurred successfully.

## More views

![Current Main workspace SuperStructureAssem. Only one hopper is visible in this assembly view. CAD includes mate or linked-reference warnings; the image is not proof of a fully populated or validated mechanism.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_assembly.jpg)

Current Main workspace SuperStructureAssem. Only one hopper is visible in this assembly view. CAD includes mate or linked-reference warnings; the image is not proof of a fully populated or validated mechanism.

![Full frame, carousel, drive, and screen CAD from M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_4.jpg)

Full frame, carousel, drive, and screen CAD from M4.

## Code for this revision

Exact archived source excerpts. The file labels identify their revisions.

### app_later.py · lines 959–997

Recovered full later Library app; contains automatic recipes, serial discovery, and switch-indexing wording.

```python
def _prepare_recipe_item_worker(item):
    global actuator_position, disk_current_slot, disk_position_known
    try:
        _check_recipe_cancelled()
        if actuator_position == "UNKNOWN":
            raise RuntimeError("Linear actuator position is UNKNOWN. Return it to the top "
                               "and use SET CURRENT AS UP before restarting the recipe.")
        if actuator_position != "UP":
            _recipe_status("Raising the linear actuator 69,000 steps before disk movement...")
            _perform_actuator_command("ACTUATOR UP", response_type="motion", timeout=70.0)
            actuator_position = "UP"
        else:
            status = _perform_actuator_command("ACTUATOR STATUS", response_type="status", timeout=3.0)
            if "POSITION=UNKNOWN" in status:
                _perform_actuator_command("SET ACTUATOR UP", response_type="ok", timeout=2.0)
            elif "POSITION=UP" not in status:
                raise RuntimeError(f"XIAO did not confirm the actuator is UP: {status}")
        _check_recipe_cancelled()
        if item is None:
            recipe_result_queue.put(("complete", None))
            return
        target_slot = item["slot"]
        _recipe_status(f"Actuator is UP. Moving disk to slot {target_slot}: {item['name']}...")
        disk_response = _perform_disk_command(f"DISK GOTO {target_slot}", response_type="motion", timeout=12.0)
        match = re.search(r"DONE DISK SLOT\s+(\d+)", disk_response)
        if not match or int(match.group(1)) != target_slot:
            raise RuntimeError(f"Disk did not confirm slot {target_slot}: {disk_response}")
        disk_current_slot = target_slot
        disk_position_known = True
        _check_recipe_cancelled()
        _recipe_status(f"Disk is at slot {target_slot}. Lowering the actuator 69,000 steps before dispensing...")
        _perform_actuator_command("ACTUATOR DOWN", response_type="motion", timeout=70.0)
        actuator_position = "DOWN"
        _check_recipe_cancelled()
        recipe_result_queue.put(("ready", item))
    except RecipeSequenceCancelled as exc:
        recipe_result_queue.put(("cancelled", str(exc)))
    except Exception as exc:
        recipe_result_queue.put(("error", str(exc)))
```

### app_later.py · lines 1035–1047

Recovered full later Library app; contains automatic recipes, serial discovery, and switch-indexing wording.

```python
def start_recipe_preparation():
    if not recipe_run_active or recipe_cancel_event.is_set():
        return
    if recipe_run_index < len(active_run_items):
        item = active_run_items[recipe_run_index]
        message = (f"Preparing item {recipe_run_index + 1} of {len(active_run_items)}: "
                   f"Slot {item['slot']} — {item['name']}")
    else:
        item = None
        message = "All powders are dispensed. Returning the actuator to UP..."
    recipe_motion_screen(message)
    threading.Thread(target=_prepare_recipe_item_worker, args=(item,), daemon=True).start()
    root.after(100, process_recipe_result_queue)
```

The recipe logic was mostly about making each stage earn the next one: known position, completed movement, then feeding. That is much more than adding eight quantities to the screen. The remaining gap in this record is the matched firmware and full run data needed to check the whole sequence together.

<details>
<summary>Notes added while reconstructing this entry</summary>

The final paired actuator firmware, disk firmware, and measured recipe transcript aren't identified in the available archive. In particular, switch-based app wording differs from the recovered step-count disk code. The state and command flow above describe the saved implementation without asserting that an arbitrary combination of those files is a validated final build.

</details>

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)
- [Existing Forge journals](https://forge.hackclub.com/projects/763)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R27_sequence_lift_indexing_engagement_and_mass_feedback_for_a_multi_powder_recipe.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-11-04: J26 One slot backward instead of seven forward

**Total time spent: 2 hours**

*Milestone 4 | Retrospective build notes*

Always rotating in one direction wastes a lot of movement near the numbering boundary. From slot 1 to slot 8, I only need one station in reverse, not seven forward. I added the shorter-route calculation to the step-count version.

The four-station case needed a tie rule, so the code chooses forward when both distances are equal. Requesting the current slot doesn't need a move at all. These are simple cases, but they're exactly the sort of details that get lost if I just write 'shortest path added.'

![Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_rotary.jpg)

Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.

The more consequential part was waiting. An OK response says the command started; it doesn't mean the disk has stopped at the target. The Pi needed the destination in DONE DISK SLOT before lowering the drive.

The timer counts the move, then the main loop updates the slot and reports completion. I kept the examples below as code-derived behavior. I don't have a full physical alignment table for every wraparound, tie, and interrupted move.

## Route calculation and completion

The step-count firmware calculates forward distance as (requested + 8 - current) modulo 8 and reverse distance as (current + 8 - requested) modulo 8. It chooses the smaller distance, with forward motion for a four-slot tie. This is a concrete implementation of the shortest-route note, rather than simply assuming the motor always turns in one direction.

For example, from slot 1 to slot 8, the forward distance is seven slots and the reverse distance is one, so the firmware requests one reverse slot. From slot 2 to slot 6, both distances are four, so it takes the documented forward tie. Requesting the current slot performs no index and immediately reports that slot while maintaining driver hold. These are derived examples of the code, not recorded physical tests.

startDiskMove() refuses indexing if the auger is moving, the disk is already busy, a disk alarm is latched, or the step calibration isn't integral. It sets direction, enables the driver, allows a 20 ms enable-settling interval and a 20 microsecond direction-settling interval, then starts Timer2. The disk is configured for 1000 pulses per second in the recovered configuration.

The number of timer compare events is twice the number of steps because the output toggles once high and once low for each full pulse. The interrupt decrements that count and disconnects the output when the move ends. Completion is then handled in the main loop, which updates the slot reference and emits DONE DISK SLOT n. That response separates an accepted command from a completed move.

The Pi-side recipe worker waits for a motion response and checks that the slot number in DONE DISK SLOT matches the requested target. It doesn't lower the actuator merely because an OK line says motion started. That matters here because the mechanical coupling must stay clear throughout indexing.

## More views

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

## Code for this revision

Exact archived source excerpts. The file labels identify their revisions.

### timer_controller_later.ino · lines 552–578

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
void goToDiskSlot(uint8_t requestedSlot) {
  if (!diskPositionKnown) {
    Serial.println(F("ERR DISK POSITION UNKNOWN - SEND SET SLOT n"));
    return;
  }

  uint8_t forwardDistance =
      (requestedSlot + DISK_SLOT_COUNT - diskCurrentSlot) %
      DISK_SLOT_COUNT;
  uint8_t reverseDistance =
      (diskCurrentSlot + DISK_SLOT_COUNT - requestedSlot) %
      DISK_SLOT_COUNT;

  if (forwardDistance == 0) {
    setDiskDriverEnabled(true);
    Serial.print(F("DONE DISK SLOT "));
    Serial.println(diskCurrentSlot);
    return;
  }

  // For the four-slot tie, use the forward direction.
  if (forwardDistance <= reverseDistance) {
    startDiskMove(1, forwardDistance, requestedSlot);
  } else {
    startDiskMove(-1, reverseDistance, requestedSlot);
  }
}
```

### timer_controller_later.ino · lines 525–550

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
void updateDiskCompletion() {
  if (!diskMoveFinished) {
    return;
  }

  noInterrupts();
  diskMoveFinished = false;
  interrupts();

  digitalWrite(DISK_STEP_PIN, LOW);

  if (diskPositionKnown && diskPendingTargetSlot >= 1 &&
      diskPendingTargetSlot <= DISK_SLOT_COUNT) {
    diskCurrentSlot = diskPendingTargetSlot;
  }

  diskPendingDirection = 0;
  diskPendingTargetSlot = 0;

  if (diskPositionKnown) {
    Serial.print(F("DONE DISK SLOT "));
    Serial.println(diskCurrentSlot);
  } else {
    Serial.println(F("DONE DISK SLOT UNKNOWN"));
  }
}
```

Less rotation was useful, but it couldn't come at the expense of lowering into a moving disk. The completion response mattered more to the shared-drive sequence than the time saved by taking the shorter route.

<details>
<summary>Notes added while reconstructing this entry</summary>

These formulas and responses document the bidirectional step-count revision. Later switch and counterclockwise descriptions belong to a different state of the app. The available record contains the routing implementation, but no complete physical trial set for wraparound, ties, same-slot requests, and interruption recovery.

</details>

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R26_choose_the_shortest_carousel_route_and_wait_for_completed_indexing.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-11-03: J25 The controller needs to know which hopper is there

**Total time spent: 2 hours**

*Milestone 4 | Retrospective build notes*

Eight positions gives me 45 degrees per station, but the controller can't do much with that until it's tied to the driver configuration. The saved direct-drive setup uses 200 full steps and 32 microsteps: 6400 pulses per revolution, 800 per slot.

The integral count was useful. I didn't want rounding at each station gradually changing the commanded alignment. But having a clean calculation didn't make the starting slot known, and it didn't detect missed motion.

![Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_rotary.jpg)

Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.

In the recovered step-count firmware, position starts UNKNOWN. The operator aligns a hopper and declares its slot with SET SLOT. That's a reference-setting operation, not automatic homing. It matters because a program can keep perfectly tidy counts from a wrong starting assumption.

There's still a version mismatch in the archive: later app wording mentions a switch and indent, while the recovered disk code uses bidirectional counted steps without that switch-homing implementation. I can explain each version, but I can't merge them into a final setup the source doesn't identify.

## Steps, slots, and UNKNOWN

The timer-based disk firmware specifies eight slots, 200 full steps per motor revolution, 32 microsteps, and a 1:1 motor-to-disk ratio. The calibration is therefore 200 times 32 divided by eight, or 800 step pulses per station and 6400 per revolution. This is the configuration actually declared in the saved file; the driver must physically use the matching microstep mode for the calculation to hold.

The geometry gives 45 degrees per slot, while the motor configuration gives electrical pulses per slot. They agree only if the gearing, microstep mode, direction, and physical reference are correct. Changing the driver microstep switch without updating the software would change disk travel even though the slot-number arithmetic remains unchanged.

The step-count firmware starts with position unknown. SET SLOT n validates the requested range 1 through 8, refuses while auger or disk motion is active, stores the current slot, marks position known, and enables the disk driver. It doesn't rotate to a sensor or discover the physical location; the operator must already align the disk correctly before declaring the slot.

A requested movement is rejected when the reference is unknown. DISK STOP and DISK DISABLE stop motion and invalidate position as appropriate. That state handling prevents the program from continuing to treat an interrupted movement as a completed index. A later open/reset cycle also needs the known slot restored if the physical disk has not moved.

The later app mentions a switch, an indent, and counterclockwise indexing. The recovered disk firmware instead uses bidirectional counted steps and no matching switch-homing implementation. These are different source states. The account therefore describes the SET SLOT reference procedure for the saved firmware, while the final matched switch-based configuration remains unidentified.

## More views

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

## Code for this revision

Exact archived source excerpts. The file labels identify their revisions.

### timer_controller_later.ino · lines 59–75

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
const uint8_t DISK_SLOT_COUNT = 8;
const uint32_t DISK_MOTOR_FULL_STEPS_PER_REV = 200UL;
const uint32_t DISK_DRIVER_MICROSTEPS = 32UL;
const uint32_t DISK_MOTOR_REVS_PER_DISK_REV_NUMERATOR = 1UL;
const uint32_t DISK_MOTOR_REVS_PER_DISK_REV_DENOMINATOR = 1UL;

const uint32_t DISK_STEP_CALCULATION_NUMERATOR =
    DISK_MOTOR_FULL_STEPS_PER_REV * DISK_DRIVER_MICROSTEPS *
    DISK_MOTOR_REVS_PER_DISK_REV_NUMERATOR;
const uint32_t DISK_STEP_CALCULATION_DENOMINATOR =
    DISK_SLOT_COUNT * DISK_MOTOR_REVS_PER_DISK_REV_DENOMINATOR;
const uint32_t DISK_STEPS_PER_SLOT =
    DISK_STEP_CALCULATION_NUMERATOR / DISK_STEP_CALCULATION_DENOMINATOR;

const uint32_t DISK_STEP_FREQUENCY_HZ = 1000UL;
const uint16_t DISK_ENABLE_SETTLE_MS = 20;
const uint16_t DISK_DIRECTION_SETTLE_US = 20;
```

### timer_controller_later.ino · lines 776–795

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
  if (parseSlotArgument("SET SLOT ", requestedSlot)) {
    if (requestedSlot == 0) {
      Serial.println(F("ERR SLOT MUST BE 1..8"));
      return;
    }

    if (augerMode != AUGER_STOPPED || diskMoveActive) {
      Serial.println(F("ERR MOTION ACTIVE"));
      return;
    }

    diskCurrentSlot = requestedSlot;
    diskPositionKnown = true;
    setDiskDriverEnabled(true);
    Serial.print(F("OK DISK SLOT SET "));
    Serial.println(diskCurrentSlot);
    return;
  }

  requestedSlot = 0;
```

For this firmware, 800 pulses means one intended station, starting from a position the operator has established. Interrupt a move and that position may no longer be trustworthy. Keeping UNKNOWN as a real state was more useful than pretending the last requested slot was where the disk must have ended up.

<details>
<summary>Notes added while reconstructing this entry</summary>

The pulse count defines intended travel, while a known physical starting alignment gives slot numbers their meaning. Repeated alignment around all eight stations and recovery after interruption are separate physical checks. No measured home-position error or full station-error series is preserved with this revision.

</details>

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R25_convert_carousel_positions_to_step_counts_and_establish_a_known_reference.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-11-03: J24 Getting the separate mechanisms onto one frame

**Total time spent: 2 hours**

*Milestone 4 | Retrospective build notes*

I built the frame from aluminum extrusion, cutting the members with an electric saw and assembling the structure around the mechanisms. The BOM lists 3030 T-slot parts and connectors. This was where the project stopped being a set of things that could sit separately on the bench.

The alignment chain was pretty unforgiving. Motor to auger, auger and hopper to outlet, outlet to receiving cup, cup on the scale. Moving one mounting position could affect several of those relationships.

![V18 frame: Sketch 1 on Top plane, including rail/attachment layout and visible 50 and 35 dimensions in the centimetre-based model.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_frame_sketch.jpg)

V18 frame: Sketch 1 on Top plane, including rail/attachment layout and visible 50 and 35 dimensions in the centimetre-based model.

![V18 frame: Extrude 1 creates the first base rail solids from selected Sketch 1 faces, blind depth 3 cm.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_frame_rails.jpg)

V18 frame: Extrude 1 creates the first base rail solids from selected Sketch 1 faces, blind depth 3 cm.

The screen and electronics needed places too. I wanted the controls reachable, but not at the cost of blocking powder loading, cleaning access, or the drive's raised space. Everything that looked like spare room in one isolated CAD model was potentially needed by something else.

The archived frame sequence below shows the layout, rails, uprights, and plates. Those are nominal design dimensions. I don't have the complete physical cut list or measured overall envelope in this record. The assembly photo is the bridge to the actual build, not a substitute for every fitting adjustment made during it.

## Frame construction notes

The V18 Superstructure studio begins with Sketch 1 on the Top plane, containing the frame layout and repeated rail and attachment geometry. Visible dimensions include 50 and 35 in the centimetre-based studio. Extrude 1 creates the first base rail solids from multiple selected sketch faces at a 3 cm depth.

Subsequent features build the structure upward and add plates. Extrude 3 uses selected Sketch 1 regions at a 0.5 cm depth, with existing uprights and new base plate geometry visible in the preview. Further sketches, extrusions, and mirrors lead to the saved superstructure, preserving the order from layout to rails, uprights, and plates.

Extrude 2 selects four faces of Sketch 1, creates New solids, and uses a 48 cm blind depth for the uprights. That is the archived CAD member height. Attachments and supports can extend the overall machine beyond a nominal rail length, so it doesn't independently establish the measured assembled envelope.

Integration brought several alignment requirements together. The disk axis had to be supported by the frame, the selected hopper outlet had to sit over the receiving container, and the lifted motor's axis had to meet the auger coupling when lowered. The scale also needed access for the cup and a support arrangement that didn't mechanically interfere with the powder path.

## Building up the frame

![V18 frame: Extrude 3 creates plate geometry at 0.5 cm depth; previously created rails and uprights remain in the construction preview.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_frame_baseplates.jpg)

V18 frame: Extrude 3 creates plate geometry at 0.5 cm depth; previously created rails and uprights remain in the construction preview.

![V18 saved Superstructure after closing the feature preview. This historical model is distinct from the later Main assembly.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_frame_complete.jpg)

V18 saved Superstructure after closing the feature preview. This historical model is distinct from the later Main assembly.

![V18 frame: Extrude 2 creates four upright solids from Sketch 1 faces at 48 cm blind depth.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_frame_uprights.jpg)

V18 frame: Extrude 2 creates four upright solids from Sketch 1 faces at 48 cm blind depth.

![Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_superstructure.jpg)

Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.

![Current Main workspace SuperStructureAssem. Only one hopper is visible in this assembly view. CAD includes mate or linked-reference warnings; the image is not proof of a fully populated or validated mechanism.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_assembly.jpg)

Current Main workspace SuperStructureAssem. Only one hopper is visible in this assembly view. CAD includes mate or linked-reference warnings; the image is not proof of a fully populated or validated mechanism.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

![Full frame, carousel, drive, and screen CAD from M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_4.jpg)

Full frame, carousel, drive, and screen CAD from M4.

The machine had an overall structure now. That made the next software work less abstract: a slot number had to correspond to the hopper under a real lifted drive, above a real cup. Good-looking packaging wasn't enough if that chain of alignment didn't survive motion.

<details>
<summary>Notes added while reconstructing this entry</summary>

I used the 3030 extrusion and connectors identified in the BOM, cutting and assembling the frame as described in M4. The saved CAD contains nominal design dimensions; the fabrication record doesn't preserve a complete measured cut list, kerf allowances, and bracket offsets. Those remain limits on dimensional reproduction from this account alone.

The frame also carried the screen and electronics. Their placement affected control access, visibility of mass feedback, removal of contact parts, and wiring service. The later full assembly CAD shows one populated hopper and linked or mate warnings. It records packaging, without constituting a resolved simulation of a fully loaded eight-hopper machine.

The physical assembly photograph shows the carousel and drive packaged into the frame. The archived construction views provide the preceding CAD stages, while photographs of every physical installation step aren't preserved. I kept those two forms of evidence separate rather than treating a final view as a record of frame squaring and every fitting adjustment.

</details>

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R24_construct_the_extrusion_frame_and_integrate_the_carousel_scale_lift_and_screen.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-11-02: J23 Lowering the motor wasn't enough to connect it

**Total time spent: 2 hours**

*Milestone 4 | Retrospective build notes*

This coupling problem held up the integrated machine. I could select a hopper and bring the motor down, but the two mating features didn't necessarily arrive at an angle where they could engage.

It was especially awkward because the connection could work once assembled. That wasn't the same job as reconnecting after an independent auger stop. The mechanism had to find engagement from whatever relative orientation was left, without me lining the faces up by hand.

![V18 auger motor adapter: Sketch 15 on a face of Extrude 2, displayed 2.5 cm circular profile before the adapter base is added.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_adapter_base_sketch.jpg)

V18 auger motor adapter: Sketch 15 on a face of Extrude 2, displayed 2.5 cm circular profile before the adapter base is added.

![V18 motor adapter: Extrude 13 adds two selected Sketch 15 regions at 0.2 cm blind depth into Part 4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_adapter_base_extrude.jpg)

V18 motor adapter: Extrude 13 adds two selected Sketch 15 regions at 0.2 cm blind depth into Part 4.

I tried different interface ideas and moved to serrated mating teeth. The notes describe that as the practical solution. More repeated teeth reduced the dependence on one particular angular alignment, although I don't have an orientation sweep or engagement failure-rate log to put numbers behind it.

The earlier keyed adapter in V18 is worth showing because it makes the registration issue visible. It isn't a recovered feature history for the later serrations, and I haven't matched it to the exact failed print. I don't want a convenient saved model to quietly stand in for a different physical part.

## The earlier adapter and the tooth redesign

The V18 auger studio preserves a keyed motor-adapter stage. Sketch 15 is on a face of Extrude 2 with a displayed 2.5 cm circular profile. Extrude 13 adds two selected regions at 0.2 cm depth into Part 4. Sketch 13 lies on a face of that extrusion, displays a 2.3 cm circular boundary, and divides the profile into keyed regions; Onshape marks it not fully defined. Extrude 11 adds two regions at 0.75 cm depth into Part 4. These features explain an angularly registered geometry, but this archive isn't matched to the exact failed printed coupler or to the later serrated tooth dimensions.

I changed the interface to repeated serrated teeth. More repeated mating features reduced dependence on one relative orientation, and the milestone notes report that change as the practical solution. No orientation sweep or engagement success-rate series is preserved, so the reported behavior remains distinct from a guarantee for every possible initial angle.

## Saved adapter stages

![V18 motor adapter: Sketch 13 on a face of Extrude 13 shows a 2.3 cm circular boundary and keyed engagement profile. Onshape reports this sketch is not fully defined.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_adapter_key_sketch.jpg)

V18 motor adapter: Sketch 13 on a face of Extrude 13 shows a 2.3 cm circular boundary and keyed engagement profile. Onshape reports this sketch is not fully defined.

![V18 motor adapter: Extrude 11 adds two Sketch 13 regions at 0.75 cm blind depth into Part 4, forming the keyed wall/engagement geometry.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_adapter_key_extrude.jpg)

V18 motor adapter: Extrude 11 adds two Sketch 13 regions at 0.75 cm blind depth into Part 4, forming the keyed wall/engagement geometry.

![V18 saved auger with keyed motor adapter. This is a recovered orientation-dependent design stage; its identity with the exact failed printed coupler has not been established, and it is not the later serrated revision.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_adapter_complete.jpg)

V18 saved auger with keyed motor adapter. This is a recovered orientation-dependent design stage; its identity with the exact failed printed coupler has not been established, and it is not the later serrated revision.

![Earlier CAD screenshot of an auger drive assembly. Original image from the milestone document.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_11.jpg)

Earlier CAD screenshot of an auger drive assembly. Original image from the milestone document.

![Full frame, carousel, drive, and screen CAD from M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_4.jpg)

Full frame, carousel, drive, and screen CAD from M4.

![B4 servo actuator assem. CAD of the lift concept with lead screw, brackets, and motor assembly. Confirm its relationship to the built mechanism.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_b4_lift.jpg)

B4 servo actuator assem. CAD of the lift concept with lead screw, brackets, and motor assembly. Confirm its relationship to the built mechanism.

The shared-drive idea depended on this detail more than the early layout made it seem. The disk could get to the right hopper and the lift could get to the right height, yet neither would help if the faces couldn't seat. I needed a connection that could form again, not just one that could transmit torque when already together.

<details>
<summary>Notes added while reconstructing this entry</summary>

The first coupling concept had an angular-registration problem. The motor-side feature and auger-side feature could mate only when they arrived at a specific orientation. The carousel selected the correct hopper, but lowering the drive didn't guarantee that the coupling features lined up. The notes describe this as a roadblock because unsuccessful engagement prevented further integrated tests.

The failure showed that coincident shaft axes were necessary but insufficient. Angular orientation and engagement depth determined whether the features could lower into place. A model could appear concentric while opposing projections still collided during the approach, explaining why a connection that transmitted torque when assembled could fail during automatic re-engagement.

Tooth count, spacing, height, flank shape, lead-in, clearance, and axial overlap govern whether the halves seat or meet tip-to-tip. Both halves also need a secure shaft connection. The notes establish the serrated redesign, but its detailed tooth-generating sketch and dimensions aren't available in this source set.

The relevant performance question was repeatable seating after independent auger stops, followed by torque transfer. A single assembled connection could not address the original failure mode. The record doesn't supply a measured failure rate or a controlled old-versus-new engagement series, so I've not assigned one to the redesign.

The lift, disk, and coupling now had complementary jobs: separate the drive, select a hopper, and reconnect to transmit torque. That relationship dictated the later application's order of operations. It also explained why changing only actuator travel or motor speed would not solve a misregistered engagement face.

</details>

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R23_replace_the_angle_sensitive_drive_coupling_with_serrated_mating_teeth.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-11-02: J22 The drive has to get out of the way

**Total time spent: 2 hours**

*Milestone 4 | Retrospective build notes*

Sharing the motor saved hardware, but now I had to physically move it out of the carousel's way. Leave it engaged and the disk can't index. Lower it too soon and it can meet the wrong part of the moving mechanism.

The sequence I needed was straightforward: raise, rotate, lower. Making the mechanism follow it with known positions was the less straightforward part.

![B4 servo actuator assem. CAD of the lift concept with lead screw, brackets, and motor assembly. Confirm its relationship to the built mechanism.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_b4_lift.jpg)

B4 servo actuator assem. CAD of the lift concept with lead screw, brackets, and motor assembly. Confirm its relationship to the built mechanism.

I initially considered building the lift and then chose to buy a mechanism under the cost constraints in the notes. The B4 branch still has the servo/lead-screw concept, while the later app talks to a separate actuator controller. Those are different stages, not a collection of actuators that were all installed at once.

I also had to be careful with the travel value in software. The later app uses 69,000 steps, which looks very definite but isn't a stroke measurement by itself. Without the actual lead, gearing, and microsteps it doesn't tell me millimeters. The app's UP position is an operator-established reference too, not an automatically sensed top limit.

## Lift geometry and references

The required clearance depends on coupling overlap, the nearby hopper envelope, and how the drive is guided. The motor and its wiring move with the stage, while the carousel passes beneath it. A commanded travel value only becomes a physical stroke after applying the actual microsteps, lead, and gearing; it isn't an independent measurement of clearance.

The later app sets a travel constant of 69,000 steps and sends ACTUATOR UP or ACTUATOR DOWN to a separate XIAO over USB serial, with a default actuator port of /dev/ttyACM1 at 115200 baud. That is a commanded step count, not millimetres. The mechanical conversion requires the actuator's steps per revolution, microsteps, and lead or gearing.

The app also starts from an assumption that the actuator is physically at its top reference. It has a SET CURRENT AS UP operation and blocks a recipe if the position is UNKNOWN. The source states there are no actuator limit switches in that operating arrangement. This reference-setting behavior must not be described as automatically sensing the top end of travel.

## More views

![B4 workspace SuperStructureAssem. The alternate arrangement shows a servo and lead-screw lift structure above the auger drive. This is a CAD revision, not proof of installed final hardware.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_b4_assembly.jpg)

B4 workspace SuperStructureAssem. The alternate arrangement shows a servo and lead-screw lift structure above the auger drive. This is a CAD revision, not proof of installed final hardware.

![Full frame, carousel, drive, and screen CAD from M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_4.jpg)

Full frame, carousel, drive, and screen CAD from M4.

![Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_superstructure.jpg)

Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.

The lift gave the carousel room to move. It didn't guarantee the drive would connect when it came back down. That became the next roadblock: the axes could line up and the coupling could still land at the wrong angle.

<details>
<summary>Notes added while reconstructing this entry</summary>

The shared-motor architecture required a motion sequence the single doser didn't need. While a hopper is feeding, the motor must engage its auger. While the carousel indexes, that engagement must be clear of the rotating parts. The lift supplies the missing degree of freedom: raise the drive, index the disk, then lower the drive to the selected hopper.

The B4 branch preserves a servo/lead-screw lift concept. The notes record moving from a plan to construct the lift to purchasing a mechanism, and the later app communicates with a separate actuator controller. I kept these stages distinct because the saved sources don't identify one unchanged lift across the entire project.

The next mechanical issue was engagement at the bottom of the stroke. Even with enough clearance to index, the coupler could fail if the auger and motor reached incompatible angular orientations. That motivated the separate coupling redesign rather than increasing actuator travel or motor speed.

</details>

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R22_develop_the_lift_mechanism_that_clears_the_drive_before_indexing.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-11-01: J21 Back to the carousel, and a lot less solid material

**Total time spent: 2 hours**

*Milestone 4 | Retrospective build notes*

Once the single doser had real work behind it, I went back to the carousel. The early model was a solid disk with eight pockets. The later one opened that up into a much lighter-looking plate-and-rib arrangement. It was a fairly visible change, but the feature sequence is more useful than just putting two finished renders beside each other.

The original blank was 330 mm across and 60 mm thick. That's a substantial piece of geometry to carry into a rotating assembly. The pocket layout also constrained what could change: make a hopper opening bigger and I lose material between stations or near the edge.

![V5 solid carousel: Sketch 1, Top-plane circle with displayed diameter 33 cm, before creating the disk blank.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_base_sketch.jpg)

V5 solid carousel: Sketch 1, Top-plane circle with displayed diameter 33 cm, before creating the disk blank.

![V5 solid carousel: Extrude 1 creates a 6 cm deep New solid disk blank before pocket removal.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_blank.jpg)

V5 solid carousel: Extrude 1 creates a 6 cm deep New solid disk blank before pocket removal.

The later model kept the overall diameter but changed the pockets and supporting structure. The lightening feature reports a 42.4% weight reduction in CAD. I don't have a weighed before-and-after print comparison or a stiffness test, so that number stays a CAD result.

I wanted the construction stages kept visible here: the circle and blank, the pockets, then the later plate, ribs, and mirror. Otherwise it's too easy to make the carousel sound like one decision, when the saved geometry shows a fairly different support arrangement by the later revision.

## The saved construction sequence

The V5 Rotary Disk studio starts with Sketch 1, a 33 cm diameter circle on the Top plane. Extrude 1 makes a new solid with a 6 cm blind depth, giving a nominal 330 mm diameter and 60 mm thickness. That is the early blank, rather than the later installed open structure.

Sketch 2 is on a face of that blank and lays out the eight pockets. Its displayed dimensions include a 12 cm center-to-pocket radial dimension and a 7 cm pocket diameter. Eight equally spaced pocket centers imply 45-degree spacing. For this geometry, adjacent centers are approximately 91.84 mm apart, calculated as twice the 120 mm radius times sin(22.5 degrees). A 70 mm pocket leaves approximately 21.84 mm between adjacent circular boundaries before any further cuts.

The outer edge also has limited material around each pocket. The disk radius is 165 mm; the station radius plus pocket radius is 120 + 35 = 155 mm. The nominal radial material outside a pocket is therefore about 10 mm at its outermost point. These calculations are geometric interpretations of this archived sketch, not finite-element results or measurements of a printed disk.

Extrude 2 removes the eight regions of Sketch 2 to a blind depth of 3 cm. The sequence shows the solid blank, pocket layout, cut preview, and saved pocketed model. In this revision the pocket feature selects faces from one sketch; the construction isn't inferred from the appearance of eight completed recesses.

Rotary Disk V2 is a later open supporting arrangement. I compared its saved state with the earlier solid construction so the two revisions remained distinguishable. The change visibly altered the load-carrying material and access around the hopper stations, while measured stiffness and print-mass comparisons aren't preserved in the record.

The V18 Rotary Disk V2 archive gives more specific detail for the open structure. Sketch 1 retains a displayed 33 cm outer diameter but shows an 8.5 cm pocket diameter, larger than the earlier 7 cm pockets. Extrude 1 creates an initial plate at 0.635 cm depth, or 6.35 mm. The custom Part Lightening feature uses Manual mode, selects a face of Extrude 2 and 32 rib lines from Sketch 2, and sets wall and rib thicknesses to 0.5 cm each. Its tool-diameter parameter is 0.67 cm and its blind cut depth is 2.5 cm. The feature reports a 42.4% part-weight reduction in CAD; that isn't a measured weight reduction of the printed machine. Plane 1 is offset 3 cm from the selected face of Sketch 1. Mirror 1 uses Part mirror in Add mode, selects Part 2, mirrors about Plane 1, and lists Part 1 as the merge scope. Those references define the repeated plate arrangement. The new views preserve the sketch, initial plate, lightening parameters, mirror reference, mirror operation, and saved disk state separately.

## Pocket cuts, ribs, and the later plates

![V5 solid carousel: Sketch 2 on the disk face shows eight pockets, displayed 12 cm radial location and 7 cm diameter.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_pocket_sketch.jpg)

V5 solid carousel: Sketch 2 on the disk face shows eight pockets, displayed 12 cm radial location and 7 cm diameter.

![V5 solid carousel: Extrude 2 removes the eight pocket regions to 3 cm blind depth. Intermediate feature preview.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_pocket_cut.jpg)

V5 solid carousel: Extrude 2 removes the eight pocket regions to 3 cm blind depth. Intermediate feature preview.

![V5 solid carousel saved model after closing the pocket feature preview. Selected feature edges remain highlighted; later suppressed features remain visible in the tree.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_complete.jpg)

V5 solid carousel saved model after closing the pocket feature preview. Selected feature edges remain highlighted; later suppressed features remain visible in the tree.

![Earlier solid eight-cavity rotary disk for comparison with the open structure.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_3.jpg)

Earlier solid eight-cavity rotary disk for comparison with the open structure.

![Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_rotary.jpg)

Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.

![V18 Rotary Disk V2: Sketch 1 on Top plane. The displayed outer diameter is 33 cm and a pocket diameter is 8.5 cm; the rest of the crowded dimensions need direct CAD inspection.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_disk_sketch.jpg)

V18 Rotary Disk V2: Sketch 1 on Top plane. The displayed outer diameter is 33 cm and a pocket diameter is 8.5 cm; the rest of the crowded dimensions need direct CAD inspection.

![V18 Rotary Disk V2: Extrude 1 creates the initial plate from Sketch 1 regions. Historical construction preview.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_disk_plate.jpg)

V18 Rotary Disk V2: Extrude 1 creates the initial plate from Sketch 1 regions. Historical construction preview.

![V18 Rotary Disk V2: Part Lightening feature inspected as a construction stage, with its parameters and cut structure shown.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_disk_lightening.jpg)

V18 Rotary Disk V2: Part Lightening feature inspected as a construction stage, with its parameters and cut structure shown.

![V18 Rotary Disk V2: Plane 1 parameter view defining the reference used by Mirror 1. Read-only historical inspection.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_disk_plane.jpg)

V18 Rotary Disk V2: Plane 1 parameter view defining the reference used by Mirror 1. Read-only historical inspection.

![V18 Rotary Disk V2: Mirror 1 duplicates the selected plate about Plane 1, producing the upper/lower arrangement.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_disk_mirror.jpg)

V18 Rotary Disk V2: Mirror 1 duplicates the selected plate about Plane 1, producing the upper/lower arrangement.

![V18 saved Rotary Disk V2 after closing its feature preview. The archive contains feature warnings; this view is geometry evidence, not a rigidity or operation test.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_disk_complete.jpg)

V18 saved Rotary Disk V2 after closing its feature preview. The archive contains feature warnings; this view is geometry evidence, not a rigidity or operation test.

![Later open rotary structure with upper and lower plates and spacers.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_1.jpg)

Later open rotary structure with upper and lower plates and spacers.

There was now much more to the disk than repeating one hopper eight times. Pocket size, material between stations, support, and drive alignment all had to coexist. The open model gave the assembly its later form; the frame and lifted drive still had to make that form useful.

<details>
<summary>Notes added while reconstructing this entry</summary>

Support, fastening, plate spacing, hopper seating, and the connection to the disk drive are assembly constraints in addition to the modeled pocket geometry. The CAD sequence explains how the saved parts were constructed, while the physical photograph establishes that a carousel assembly was built. Neither alone supplies a loaded deflection or indexing-error measurement.

</details>

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)
- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R21_build_the_solid_eight_pocket_carousel_and_evolve_it_into_an_open_two_plate_structure.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-11-01: J20 The 55 mg tests didn't go nearly as well

**Total time spent: 2 hours**

*Milestone 3 | Retrospective build notes*

The 5 g results made the smaller target worth trying. At 0.055 g, though, 3% only gives me 0.00165 g of room. That's 1.65 mg. A difference that barely looks noticeable on the scale becomes a large part of the whole dose.

Only three of the eight recorded runs met the target: sugar, cocoa, and baking soda. Salt overshot. Several others undershot, with flour ending at 0.047 g. That is about 14.55% absolute error. Definitely not a result I can smooth over with the successful 5 g table.

![Single doser positioned above the balance. This photo provides setup context, not a trial result.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_7.jpg)

Single doser positioned above the balance. This photo provides setup context, not a trial result.

There isn't one obvious correction hiding in the signs of the errors, either. Simply adding a fixed amount to every target wouldn't fix both the high and low results. Pulse size, clumps, delayed feedback, and the stopping logic could all be involved. I don't have the traces to separate their contributions here.

The notes mention consecutive same-target tests, but the eight-powder sheet isn't that repeated series. Its two sections are different requested masses. I can't use them as replicates just because they're called trials. I need the actual repeated values before calculating a spread or claiming this is consistent.

## Working through the small-dose result

At a 0.055 g target, the absolute allowance for 3% is 0.00165 g, or 1.65 mg. A 0.001 g difference already represents about 1.82% of the request. The recorded values and recalculated errors are shown in the table below; all error values use the same absolute percentage formula as the 5 g trials.

Run times ranged from 54 seconds for salt to 3 minutes 21 seconds for flour. Several finer or more cohesive materials took longer despite the very small target. Long finishing pauses and small additions are consistent with that pattern, but no phase trace identifies the cause of each trial's duration.

## Recorded measurements

| Powder | Target (g) | Recorded mass (g) | Absolute error | Time | Within 3% |
| --- | ---: | ---: | ---: | --- | --- |
| Granulated sugar | 0.055 | 0.056 | 1.82% | 0:57 | Yes |
| Table salt | 0.055 | 0.058 | 5.45% | 0:54 | No |
| Cocoa powder | 0.055 | 0.054 | 1.82% | 1:03 | Yes |
| Ground cinnamon | 0.055 | 0.052 | 5.45% | 1:10 | No |
| Baking soda | 0.055 | 0.054 | 1.82% | 2:43 | Yes |
| Cornstarch | 0.055 | 0.053 | 3.64% | 2:49 | No |
| Powdered sugar | 0.055 | 0.049 | 10.91% | 3:07 | No |
| All purpose flour | 0.055 | 0.047 | 14.55% | 3:21 | No |

## More views

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## What I need next

This is where the limitation was obvious. A feeder that did well at 5 g was struggling at 55 mg. The next useful test would keep one small target and one configuration fixed, repeat it, and keep every result. More tuning without that comparison would leave me guessing at what helped.

<details>
<summary>Notes added while reconstructing this entry</summary>

Only sugar, cocoa, and baking soda met 3% in these individual runs. Salt overshot while several other powders undershot, so the result doesn't support a single universal correction to the target. Material delivery per motion, scale response, and the stopping logic remained possible interacting factors.

The July 24 FINAL-only behavior below 0.100 g addresses the same class of small-target problem. The code snapshots and test sheet don't establish that these specific results were produced before or after that change. I retained the program comparison as a separate documented revision rather than assigning an improvement to unmatched data.

The milestone notes describe consecutive same-target testing, but its raw series isn't present in the available test sheet. The two target groups in that sheet are different-dose comparisons, not replicates. They can't establish a repeated-run standard deviation or a general probability of meeting the criterion.

A useful next experiment would hold the target, powder, feeder, code, baseline method, and fill conditions fixed, then retain each delivered mass and duration. That would distinguish a consistent offset from variation between runs and provide a direct comparison for revised pulse behavior. It remained a proposed next experiment rather than an added result.

</details>

## Sources

- [8 POWDER TEST](https://docs.google.com/document/d/1DNaEmukRZWxtxSPTQrcbYwlaYKfkptGngnznrOfEVN0/edit)
- [M3: SINGLE DOSER FULL-COVERAGE](https://docs.google.com/document/d/170HU5NltWJAcoOTJfmL8jjjR1hS0Zjfo67U_EM6s5aQ/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R20_evaluate_the_0_055_g_limit_and_separate_accuracy_from_repeatability.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-10-31: J19 Close to 5 g, but it took a while

**Total time spent: 2 hours**

The four clumpier powders all ended up close to the 5 g target in the recorded tests. That was encouraging after the earlier cornstarch trouble. The agitator and feeding changes had given me something that could reach the requested mass with these materials.

The times were harder to ignore. Baking soda took 5:01, cornstarch 4:55, powdered sugar 4:57, and flour 4:39. Reaching a good final reading after that long is useful, but I wouldn't call the speed problem solved.

![V5 agitator: Sketch 10 highlights the two arm profiles before Extrude 8, with the earlier screw geometry present.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_agitator_sketch.jpg)

V5 agitator: Sketch 10 highlights the two arm profiles before Extrude 8, with the earlier screw geometry present.

The notes describe uneven release, including clumps and much smaller additions between them. That fits the practical difficulty: a slow command might do very little until the material changes and more comes out together. The final mass doesn't show all of that behavior along the way.

I also caught an arithmetic mismatch while working through the sheet. Flour is listed at 4.993 g. Against 5 g, that is 0.14% absolute error, not the 0.18% written in the source. I kept the recorded mass and recalculated from it. There's also a later 120 s controller limit, so these roughly five-minute runs can't just be attributed to that newer file.

## Mass, time, and configuration

The earlier mechanical changes addressed different regions: larger flights changed the feeding space, while agitator reach addressed powder outside the screw's active region. These final results don't isolate the contribution of either change because there is no matched one-variable comparison in the available sheet.

## Recorded measurements

| Powder | Target (g) | Recorded mass (g) | Absolute error | Time | Within 3% |
| --- | ---: | ---: | ---: | --- | --- |
| Baking soda | 5 | 4.994 | 0.12% | 5:01 | Yes |
| Cornstarch | 5 | 4.991 | 0.18% | 4:55 | Yes |
| Powdered sugar | 5 | 4.996 | 0.08% | 4:57 | Yes |
| All purpose flour | 5 | 4.993 | 0.14% | 4:39 | Yes |

## More views

![V5 agitator: Extrude 8 adds two sketch faces symmetrically at 0.318 cm depth into tube adapter. The archived tree shows feature warnings, not a fully validated assembly.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_agitator_extrude.jpg)

V5 agitator: Extrude 8 adds two sketch faces symmetrically at 0.318 cm depth into tube adapter. The archived tree shows feature warnings, not a fully validated assembly.

![V10 Part Studio 1, saved July 10 2026. Later view of the auger and agitator arms.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v10_auger_agitator.jpg)

V10 Part Studio 1, saved July 10 2026. Later view of the auger and agitator arms.

![Physical auger and hopper component used to illustrate the cornstarch geometry discussion.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_9.jpg)

Physical auger and hopper component used to illustrate the cornstarch geometry discussion.

The 5 g result was good across all eight powders when combined with the previous group. The slow, uneven feeding was still something to work on. And I still hadn't earned the right to assume the same percentage accuracy would hold when the target dropped by almost two orders of magnitude.

<details>
<summary>Notes added while reconstructing this entry</summary>

The 5.000 g results were baking soda at 4.994 g in 5:01, cornstarch at 4.991 g in 4:55, powdered sugar at 4.996 g in 4:57, and flour at 4.993 g in 4:39. Recalculated absolute errors are 0.12%, 0.18%, 0.08%, and 0.14%. The source's flour percentage is inconsistent with its recorded mass, so the calculation here uses the listed 4.993 g reading.

All four final readings met 3%, while the durations exposed the cost of slower feeding and finishing. Intermittent discharge and clumps could coexist with a close final mass. I treated the time and transport observations as part of performance rather than reducing the result to a pass label.

The record contains no measured residual-powder mass or post-run coverage series for these trials. I don't interpret successful collection as proof that the hopper fully cleared or that no powder remained around walls and arm roots. Those internal states are distinct from the final cup reading.

The later controller's 120 s maximum dispense duration is shorter than all four of these runs. I kept their original recorded times and didn't attribute them to that file. Version matching matters here because a configuration that times out after two minutes could not complete an uninterrupted five-minute test under the same limit.

The outcome gives me one 5 g result for each tested cohesive powder. It doesn't establish general flow behavior for other materials, repeatability across refill levels, or an autonomous recipe containing all four. Those are separate tests with separate evidence.

</details>

## Sources

- [8 POWDER TEST](https://docs.google.com/document/d/1DNaEmukRZWxtxSPTQrcbYwlaYKfkptGngnznrOfEVN0/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R19_validate_5_g_dispensing_of_the_four_cohesive_powders.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-10-30: J18 The 5 g results were encouraging, with a lid problem

**Total time spent: 2 hours**

*Milestone 3 | Retrospective build notes*

The 5 g results were a good sign. Sugar and salt both had a recorded final reading of 5 g, with times of 1:54 and 1:49. Cocoa and cinnamon took longer, but their listed masses were still comfortably inside the 3% target.

I needed that numerical check after so much time changing geometry and control behavior. 'It seems to feed better' only goes so far. Here there were actual final masses and durations to compare.

![Single doser positioned above the balance. This photo provides setup context, not a trial result.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_7.jpg)

Single doser positioned above the balance. This photo provides setup context, not a trial result.

Cocoa still had an annoying side problem: powder escaped near the lid. The scale could end up close to target while some material went somewhere it shouldn't. So a good number in the cup didn't mean containment was finished. I don't have a documented lid change resolving that in this record.

The exact-looking sugar and salt values also need some restraint. They're what was recorded at the shown precision, not proof of literally zero physical error. And each powder has one listed 5 g run here. Useful results, but not the same as repeatedly getting that result under the same conditions.

## What the readings do and do not show

A displayed 5.000 g reading doesn't mean literally zero physical error. It means the recorded reading equals the requested value at the shown precision. The balance's resolution, calibration, drift, and final settling affect how closely that reading represents the actual delivered mass. Those quantities aren't established by the test sheet, so I report the values as recorded rather than adding unsupported measurement certainty.

The behavior notes describe sugar as easy to move but difficult to finish without overshoot because of rapid flow and scale delay. Salt behaved similarly. Cocoa and cinnamon were fine and delivered smaller quantities, leading to longer runs. Cocoa also escaped upward from the lid. That observation matters because material leaving the intended powder path can make the collected mass and total material removed from the hopper differ.

The next comparison used cohesive powders and a much smaller target. That was necessary because success at 5 g provides a comparatively large absolute error allowance and can't establish that the same mechanism can dispense tens of milligrams to the same percentage error.

## Recorded measurements

| Powder | Target (g) | Recorded mass (g) | Absolute error | Time | Within 3% |
| --- | ---: | ---: | ---: | --- | --- |
| Granulated sugar | 5 | 5 | 0.00% | 1:54 | Yes |
| Table salt | 5 | 5 | 0.00% | 1:49 | Yes |
| Cocoa powder | 5 | 5.006 | 0.12% | 3:32 | Yes |
| Ground cinnamon | 5 | 4.985 | 0.30% | 3:05 | Yes |

## More views

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

All four passed the 3% check in these runs. Cocoa took 3:32 compared with sugar's 1:54, so the time difference was still there even when both final readings looked good. Next were the clumpier powders, then the much less forgiving small target.

<details>
<summary>Notes added while reconstructing this entry</summary>

For the 5.000 g target, the sheet records sugar at 5.000 g in 1:54, salt at 5.000 g in 1:49, cocoa at 5.006 g in 3:32, and cinnamon at 4.985 g in 3:05. Absolute percentage error is abs(actual - target) / target times 100, giving 0.00%, 0.00%, 0.12%, and 0.30%. All four recorded values meet 3% at this target.

Containment and dosing error described different outcomes. Cocoa escaping near the lid could increase material removed from the hopper without increasing the amount collected by the scale. The record identifies that symptom, but doesn't preserve a measured escaped-mass result or a confirmed lid change resolving it.

I kept throughput and final error separate. Cocoa took longer than sugar even though both listed results met the criterion. The sheet provides one 5 g result per powder, rather than repeated runs or a matched tuning comparison. That limits the conclusions to the measured trials without discarding their usefulness.

</details>

## Sources

- [8 POWDER TEST](https://docs.google.com/document/d/1DNaEmukRZWxtxSPTQrcbYwlaYKfkptGngnznrOfEVN0/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R18_measure_5_g_performance_with_sugar_salt_cocoa_and_cinnamon.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-10-30: J17 Dropping the scanner and getting off the laptop

**Total time spent: 2 hours**

*Milestone 3 | Retrospective build notes*

I had considered scanning powder containers and looking up their settings in a database. It could work, but it was another piece to integrate and another set of records to keep correct. For the eight test powders, selectable profiles were the simpler route.

So I dropped the scanner-and-database direction for this prototype. The BOM still contains a scanner, which makes sense as part of the design history, but it doesn't mean scanning stayed in the operating workflow.

![Raspberry Pi and display connection with breadboard wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_3.jpg)

Raspberry Pi and display connection with breadboard wiring.

The more useful step was getting the app and controller running together on the Pi without a laptop. Powder selection, mass entry, start, result. Having a screen attached earlier wasn't quite the same thing as having the serial devices and controller launch working from the device itself.

As more controllers were connected, device selection needed more care too. The later app searches ports, avoids opening the scale as if it were the Uno, and passes the chosen Arduino device to the subprocess. It's the kind of detail that disappears in an overall machine photo but matters immediately when the wrong device gets opened.

## Pi and device setup

The standalone workflow needed more than displaying a window on the Pi. The app and controller files had to be available together, Python needed the serial and UI dependencies, device paths had to resolve, and the screen needed a usable input method. The later app's subprocess path is based on its own directory, which avoids relying on whichever working directory happened to launch it.

The interface stores a powder name for each of eight slots and a requested mass for each slot separately. Only items with positive requested amounts enter the active recipe. EMPTY is a distinct slot state, and the later start function rejects a positive amount assigned to an EMPTY slot. That separation prevents an amount entry from silently inventing the contents of a hopper.

Serial discovery became important as more controllers were attached. The later app enumerates its preferred path, stable /dev/serial/by-id aliases, /dev/ttyACM devices, and /dev/ttyUSB devices. It removes duplicate real paths and excludes the scale and an already-open actuator device. It then checks responses to identify the Uno rather than assuming that every ACM device is the auger/disk controller.

The later app passes the verified Arduino path and baud rate to the controller child, avoiding a handoff where the app checks one device and the child opens another default. It also passes the known disk slot. These details belong to later multi-device integration, while the M3 milestone establishes the reported single-doser workflow on the Pi without a laptop.

## More views

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## Code for this revision

Exact archived source excerpts. The file labels identify their revisions.

### app_later.py · lines 212–219

Recovered full later Library app; contains automatic recipes, serial discovery, and switch-indexing wording.

```python
def get_active_recipe_items():
    items = []
    for i in range(1, 9):
        name = slots[i]["name"]
        amount = recipe[i]
        if amount > 0:
            items.append({"slot": i, "name": name, "amount": amount})
    return items
```

### app_later.py · lines 313–336

Recovered full later Library app; contains automatic recipes, serial discovery, and switch-indexing wording.

```python
def disk_arduino_candidates():
    # Enumerate live ports, including ACM2/ACM3 and stable USB device aliases.
    candidates = (
        [ARDUINO_PORT]
        + sorted(glob.glob("/dev/serial/by-id/*"))
        + sorted(glob.glob("/dev/ttyACM*"))
        + sorted(glob.glob("/dev/ttyUSB*"))
    )
    excluded = {os.path.realpath(SCALE_PORT)}
    if actuator_serial is not None and actuator_serial.is_open:
        actuator_port = getattr(actuator_serial, "port", None)
        if actuator_port:
            excluded.add(os.path.realpath(actuator_port))
    unique = []
    seen = set()
    for port in candidates:
        if not port or not os.path.exists(port):
            continue
        actual_port = os.path.realpath(port)
        if actual_port in excluded or actual_port in seen:
            continue
        seen.add(actual_port)
        unique.append(port)
    return unique
```

The single-doser workflow could now live on the machine. I don't have evidence for automatic startup after a cold boot, so I'm not adding that claim. The reported step here was being able to operate the doser on the Pi without keeping the laptop attached.

<details>
<summary>Notes added while reconstructing this entry</summary>

The barcode concept would have required a scanner, a mapping from container identifiers to powder records, and a database containing useful behavior settings. M3 notes record abandoning that route after recognizing that the tested powders could be handled through two control families. The important simplification was removing a dependency from the operating workflow, not claiming that all powders behave identically.

The source supports the file-location and device-discovery architecture, and the milestone notes describe standalone operation. The record doesn't establish automatic startup after a cold boot or preserve a complete deployment transcript. I've not added those behaviors to the reported on-device achievement.

</details>

## Sources

- [M3: SINGLE DOSER FULL-COVERAGE](https://docs.google.com/document/d/170HU5NltWJAcoOTJfmL8jjjR1hS0Zjfo67U_EM6s5aQ/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)
- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [Standard Operating Procedure: Safely Utilizing and Operating PharmaTech Rx's Doser](https://docs.google.com/document/d/1p1OGP37uR5EISkR5pwSQ_23Vjzx4Qd3G_bUwq5q5h0U/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R17_replace_the_barcode_plan_with_selectable_profiles_and_run_the_doser_from_the_pi.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-10-29: J16 A 55 mg request shouldn't start like a large dose

**Total time spent: 2 hours**

*Milestone 3 | Retrospective build notes*

The fixed thresholds were getting awkward across different target sizes. The bulk phase could be too cautious for a larger request and still be too aggressive for a tiny one. I kept revising where the controller changed behavior instead of only increasing motor speed.

The July 21 and July 24 snapshots give me a useful comparison. In the older code, a 5 g request didn't begin in TURBO because the condition was greater than a fixed 5 g remaining. The later version made that cutoff depend on the target.

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

At the small end, the change was more direct. Below 0.100 g, start with FINAL pulses. A 0.055 g sugar request had begun in FINE under the July 21 logic; the July 24 version treated it as FINAL from the beginning. That is a much clearer description of the change than simply saying I made the small doses more precise.

I also lengthened the near-target waits for the free-flowing profile. It cost time. The hope was to stop asking for more powder before the previous addition was fully reflected in the reading. I can't attach the recorded 55 mg results to one snapshot because the test sheet doesn't identify its code revision.

## What changed between the snapshots

The dated code emails provide an actual before/after pair. The July 21 motor_scale.py used a fixed 5.000 g TURBO cutoff and a 0.500 g micro-mode limit. At exactly a 5 g target, its initial remaining value wasn't greater than 5.000, so it didn't start in TURBO. The July 24 motor_scale_control.py introduced target-size-aware cutoffs instead of using that fixed bulk threshold for every request.

The July 24 code introduces an ultra-small limit of 0.100 g and a micro-dose limit of 0.500 g. Requests below 0.100 g start with FINAL pulses. Requests from 0.100 g to below 0.500 g use FINE followed by FINAL. A 0.055 g sugar request therefore changes from an initial FINE pulse in the July 21 logic to FINAL in the July 24 logic.

For free-flowing targets below 1.500 g, the TURBO cutoff becomes the larger of 0.250 g and 30% of the target. Targets up to 10.000 g use a 1.000 g cutoff, and larger targets use 2.000 g. For the other family, the respective choices are max(0.150 g, 20% of target), 0.600 g, and 1.000 g. These values define when the bulk phase ends; they don't mean the complete dose must stay inside those errors.

The July 24 free-flowing profile also changes continuous-to-pulse, APPROACH-to-FINE, and FINE-to-FINAL cutoffs to 0.500, 0.150, and 0.050 g remaining. Its settling intervals become 0.800 s after continuous motion, 0.300 s after APPROACH, and 2.0 s after each FINE or FINAL pulse. The non-free-flowing settings become 0.300, 0.120, and 0.040 g, with settling intervals of 0.350, 0.120, 0.220, and 0.300 s.

## Code for this revision

Exact archived source excerpts. The file labels identify their revisions.

### motor_2026-07-21.py · lines 119–145

Code attachment sent July 21; a dated availability checkpoint, not a work-time record.

```python
def select_auger_command(target: float, remaining: float, powder_mode: str) -> str:
    """Choose the Arduino command for the current amount remaining."""
    profile = PROFILES[powder_mode]
    powder_token = profile.command_name

    # Tiny targets never enter continuous mode because there is too
    # little mass available to absorb startup and chute overshoot.
    if target < MICRO_MODE_LIMIT:
        if remaining > profile.pulse_approach_to_fine:
            return f"AUGER PULSE {powder_token} APPROACH"
        if remaining > profile.pulse_fine_to_final:
            return f"AUGER PULSE {powder_token} FINE"
        return f"AUGER PULSE {powder_token} FINAL"

    if remaining > TURBO_REMAINING:
        return f"AUGER CONT {powder_token} TURBO"

    if remaining > profile.continuous_to_pulse:
        return f"AUGER CONT {powder_token} NORMAL"

    if remaining > profile.pulse_approach_to_fine:
        return f"AUGER PULSE {powder_token} APPROACH"

    if remaining > profile.pulse_fine_to_final:
        return f"AUGER PULSE {powder_token} FINE"

    return f"AUGER PULSE {powder_token} FINAL"
```

### motor_2026-07-24.py · lines 121–144

Code attachment sent July 24; adds dose-size-dependent phase selection.

```python
def turbo_cutoff_remaining(target: float, powder_mode: str) -> float:
    """Return the remaining mass where TURBO changes to a slower mode.

    Free-flowing examples:
    - 1.000 g target: TURBO until about 0.300 g remains.
    - 2.000-10.000 g target: TURBO until 1.000 g remains.
    - Above 10.000 g: TURBO ends at 2.000 g remaining to leave extra
      room for material momentum and powder already falling.

    Non-free-flowing powder receives smaller headroom because its flow is
    slower and normally stops more quickly.
    """
    if powder_mode == FREE_FLOWING:
        if target < SMALL_TARGET_LIMIT:
            return max(0.250, target * 0.30)
        if target <= LARGE_TARGET_LIMIT:
            return 1.000
        return 2.000

    if target < SMALL_TARGET_LIMIT:
        return max(0.150, target * 0.20)
    if target <= LARGE_TARGET_LIMIT:
        return 0.600
    return 1.000
```

### motor_2026-07-24.py · lines 157–187

Code attachment sent July 24; adds dose-size-dependent phase selection.

```python
def select_auger_command(target: float, remaining: float, powder_mode: str) -> str:
    """Choose a target-aware Arduino command for the current remaining mass."""
    profile = profile_for(target, powder_mode)
    powder_token = profile.command_name

    # 20-90 mg-style doses start with the smallest physical movement.
    if target < ULTRA_SMALL_DOSE_LIMIT:
        return f"AUGER PULSE {powder_token} FINAL"

    # Small sub-gram doses do not use continuous movement. They use FINE
    # pulses first, then switch to the one-step/tiny FINAL pulse near target.
    if target < MICRO_DOSE_LIMIT:
        if remaining > profile.pulse_fine_to_final:
            return f"AUGER PULSE {powder_token} FINE"
        return f"AUGER PULSE {powder_token} FINAL"

    turbo_cutoff = turbo_cutoff_remaining(target, powder_mode)

    if remaining > turbo_cutoff:
        return f"AUGER CONT {powder_token} TURBO"

    if remaining > profile.continuous_to_pulse:
        return f"AUGER CONT {powder_token} NORMAL"

    if remaining > profile.pulse_approach_to_fine:
        return f"AUGER PULSE {powder_token} APPROACH"

    if remaining > profile.pulse_fine_to_final:
        return f"AUGER PULSE {powder_token} FINE"

    return f"AUGER PULSE {powder_token} FINAL"
```

### motor_2026-07-24.py · lines 89–112

Code attachment sent July 24; adds dose-size-dependent phase selection.

```python
PROFILES = {
    FREE_FLOWING: PowderProfile(
        # Free-flowing powder has more material in flight after fast motion.
        continuous_to_pulse=0.500,
        pulse_approach_to_fine=0.150,
        pulse_fine_to_final=0.050,
        continuous_settle=0.800,
        approach_settle=0.300,
        fine_settle=2.0,
        final_settle=2.0,
        command_name="FREE",
    ),
    NON_FREE_FLOWING: PowderProfile(
        # Non-free-flowing powder can normally run closer to the target.
        continuous_to_pulse=0.300,
        pulse_approach_to_fine=0.120,
        pulse_fine_to_final=0.040,
        continuous_settle=0.350,
        approach_settle=0.120,
        fine_settle=0.220,
        final_settle=0.300,
        command_name="NONFREE",
    ),
}
```

This gave the program a better way to distinguish tiny requests from multi-gram ones. The code change is clear; its measured benefit isn't established by the unmatched test sheet. I would need the same target and configuration on both sides of the revision to make that comparison properly.

<details>
<summary>Notes added while reconstructing this entry</summary>

The longer near-target delays, particularly the 2.0 s free-flowing FINE and FINAL intervals, trade run time for additional observation of the last addition. The July 24 email establishes availability of the revision, but doesn't connect each listed powder result to that version. The measured trials and the code comparison remain separate pieces of evidence.

The later cleaned controller uses another arrangement, including a 0.005 g tolerance and a 120 s maximum duration. Those settings describe a subsequent source state. They don't establish an improvement over the July versions without a matched measured run, and the larger absolute tolerance is particularly relevant to evaluating small targets.

</details>

## Sources

- [M3: SINGLE DOSER FULL-COVERAGE](https://docs.google.com/document/d/170HU5NltWJAcoOTJfmL8jjjR1hS0Zjfo67U_EM6s5aQ/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R16_make_phase_thresholds_depend_on_dose_size_the_july_21_to_july_24_controller_revision.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-10-29: J15 Trying to get more out of the NEMA 17

**Total time spent: 2 hours**

*Milestone 3 | Retrospective build notes*

The feeder was slow enough that I started with the software. I changed speed requests, acceleration behavior, and powder settings to see how much more useful motion I could get. Replacing the motor before understanding the delays would have made it harder to tell what actually helped.

But a bigger requested rate doesn't mean the loaded shaft follows it. The notes describe reaching the NEMA 17's practical limit in this setup and changing to a NEMA 23. They report an improvement in usable dispensing speed afterward.

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

That was encouraging, though it wasn't a controlled torque or throughput comparison. I don't have a matching series with the same fill, feeder, and finishing settings before and after. I can describe the upgrade without attaching a made-up percentage improvement to it.

The larger hardware also brought mounting, coupling, power, and signal changes along with it. And I still needed the slow finishing phases. More bulk-feed capability didn't make the scale instant or turn a clump into a predictable amount of powder.

## Drive and timing notes

The early Arduino implementation starts continuous motion at 400 pulses/s and ramps at a configured 9000 steps/s squared, updating every 5000 microseconds. STEP high and low intervals are generated in software. A separate AccelStepper test uses a fixed 600-step/s command. These are distinct experiments with different timing and pin assumptions.

M3 notes state that the investigation eventually identified the NEMA 17 as a limitation and that it was replaced by a NEMA 23. The BOM lists integrated closed-loop NEMA 23 motors with pulse/direction control. That later motor architecture also changed driver handling and wiring, so the hardware upgrade was more than increasing a speed constant in Python.

The larger motor didn't remove the need to slow near the target. A machine can feed rapidly in the bulk phase while still requiring short movements and settling pauses in the final phase. I retained phased dosing after the hardware change so that improving throughput would not simply recreate the sugar-overshoot problem.

## More views

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

## Code for this revision

Exact archived source excerpts. The file labels identify their revisions.

### auger_july.ino · lines 50–52

Recovered Library auger-only source; its 10,932-byte size matches the July email attachment. Content identity was not proved by size alone.

```cpp
const uint32_t CONTINUOUS_START_RATE = 400;
const uint32_t ACCELERATION_STEPS_PER_SECOND_SQUARED = 9000;
const uint32_t ACCEL_UPDATE_INTERVAL_US = 5000;
```

### timer_controller_later.ino · lines 83–95

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
const uint32_t FREE_TURBO_HZ  = 20000;
const uint32_t FREE_NORMAL_HZ = 2400;

// Cornstarch/non-free-flowing values.
// 20 kHz is the user's measured sweet spot: ~1 g every ~2 seconds.
const uint32_t NONFREE_TURBO_HZ  = 20000;
const uint32_t NONFREE_NORMAL_HZ = 9000;

// Fast but controlled ramp for continuous modes.
const uint32_t CONTINUOUS_START_HZ = 2000;
const uint32_t RAMP_STEP_HZ        = 500;
const uint32_t RAMP_UPDATE_MS      = 10;

```

The motor upgrade moved the project forward, but it wasn't the last speed problem. Later I had to look at how the Arduino generated the pulses themselves. Different bottleneck, different change. I don't want to collapse both into 'the old motor was too slow.'

<details>
<summary>Notes added while reconstructing this entry</summary>

The single doser was usable but slow. I first investigated software because requested speed, acceleration, and finishing behavior all influence a run's duration. That investigation was reasonable, but a higher command rate isn't proof that the physical shaft follows every step under powder load. I needed to compare commanded motion with actual rotation and powder output.

The notes report improved usable speed after the motor replacement, but contain no controlled before-and-after torque or duration series. Feeder geometry, hopper fill, and finishing parameters could also affect throughput. I retained the qualitative upgrade result without assigning a numerical gain to the motor alone.

The later M5 timing revision addressed software-generated pulses, which is a separate issue from loaded motor capability. Changing the motor and changing the pulse source occurred at different stages and solved different parts of the system. That distinction helped keep a requested frequency separate from verified shaft behavior.

</details>

## Sources

- [M3: SINGLE DOSER FULL-COVERAGE](https://docs.google.com/document/d/170HU5NltWJAcoOTJfmL8jjjR1hS0Zjfo67U_EM6s5aQ/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R15_investigate_loaded_speed_limits_and_upgrade_the_nema_17_drive.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-10-28: J14 A PCB sounded like the way out of the wiring

**Total time spent: 2 hours**

*Milestone 2 | Retrospective build notes*

The breadboard was useful, but it was getting awkward to package. Loose wiring is one thing on a bench and another when it has to live on the frame. I started planning a PCB to organize the controller connections and give the electronics a more manageable footprint.

The schematic image records that direction. It wasn't a finished board running the machine, even though I expected the PCB work to lead into a later milestone. The circuit was still changing underneath that plan.

![Electronics schematic proposal from M2. It is not evidence that a PCB was manufactured.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_1.jpg)

Electronics schematic proposal from M2. It is not evidence that a PCB was manufactured.

That was the catch. A board for the early Pi and TMC2209 arrangement wouldn't automatically suit the later Arduino interface or integrated NEMA 23 drive. Pins, enable behavior, alarms, actuator connections: those were still moving targets.

I didn't end up finalizing the PCB. It's easy to make that sound like a small omitted step, but it was a real change of direction. I still needed to mount the circuit and keep testing; I just hadn't reached a stable enough electrical design to freeze into that board.

## Why the board never stabilized

The challenge was that the electrical architecture was still evolving. The first Pi/TMC2209 arrangement, the later Arduino command interface, and the eventual integrated NEMA 23 drivers didn't share one unchanged pin map. A board layout based on an early configuration could become obsolete when motor, enable polarity, pulse generation, or actuator control changed.

## More views

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

![IMG_8167.HEIC Drive preview: breadboard wiring beside an unsoldered perfboard. Supports the board-packaging discussion; does not show a completed failed perfboard circuit.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/photo_perfboard_comparison.jpg)

IMG_8167.HEIC Drive preview: breadboard wiring beside an unsoldered perfboard. Supports the board-packaging discussion; does not show a completed failed perfboard circuit.

The packaging problem stayed with the project. A PCB could eventually make it neater, but trying to lock down the wrong revision wouldn't save much work. For now I kept the electronics changeable and came back to mounting later.

<details>
<summary>Notes added while reconstructing this entry</summary>

By the end of early feedback development, the breadboard combined power, motor-control, and Pi connections. The PCB proposal aimed to reduce loose wiring and improve mounting. The M2 notes anticipated that improvement in M3, but the record doesn't establish a fabricated board operating in the machine.

The electrical functions spanned supply connections, controller logic, STEP/DIR/EN, serial scale feedback, and later alarm and actuator paths. A fixed board would need compatible interfaces for the chosen revision. The available schematic image records the proposal, while a complete verified schematic and routed-board revision aren't preserved.

I later abandoned the custom PCB because the design had not stabilized enough to finalize it. This explains the continued use of adaptable connections and a printed mount. The decision was a change in implementation strategy, rather than a missing fabricated-board success.

Keeping the circuit modifiable allowed motor control and integration to continue. The tradeoff was retaining more manual wiring and a greater dependence on version-specific pin maps. A permanent board could address those issues after the electrical architecture settled, rather than forcing the prototype to conform to an early layout.

</details>

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R14_plan_the_electronics_mounting_and_pcb_while_the_control_system_is_still_changing.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-10-28: J13 The program ended. The motor kept moving.

**Total time spent: 2 hours**

*Milestone 2 | Retrospective build notes*

The slow rotation after motor_scale terminated was a problem I couldn't leave in place. The software had finished, but the feeder could still be adding powder. From the machine's point of view, the run wasn't actually over.

I rerouted EN to a Pi GPIO, which is the fix described in my M2 notes. Those notes call it electrical noise. I don't have a waveform showing the cause, so I can stand behind the symptom and wiring change without pretending the diagnosis went further than it did.

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

That also pushed me to stop relying on one program exiting neatly. The July Python code explicitly sends STOP ALL during cleanup and handles termination signals. The firmware has a communication watchdog. Later, the app had its own cancellation work to do with the child process and positioning states.

It isn't exciting compared with adding a carousel, but this is the sort of behavior that can ruin an otherwise decent dispense. Every way out of a run needs attention, not only the one where the target is reached and everything cooperates.

## The stop paths in the code

Enable control provides a way to deactivate the driver as well as stop step commands. The July firmware uses LOW to enable, while the later integrated motor setup uses HIGH. Those are version-specific electrical assumptions: reversing the intended polarity could leave a driver active when software believes it is disabled.

The July Python shutdown function guards against repeated cleanup, sets its running state false, prints its shutdown action, sends STOP ALL through the Arduino client, waits briefly, closes connections, and exits. SIGINT and SIGTERM both call that path. This turns an ordinary process stop into an explicit motor-control action rather than assuming closing the terminal is enough.

The firmware adds another layer: it stops automatically if serial contact is absent for 2000 ms while motion is active. Python sends a heartbeat approximately every 0.50 s during continuous feeding. The intent is to stop if the Pi program disappears even when it can't deliver its normal shutdown command. That watchdog complements EN control; it doesn't prove that every wiring or power fault has been handled.

In the later app, cancellation sends stop commands, signals the child process, marks actuator position UNKNOWN, and invalidates the disk reference. If the child remains alive, the app escalates to a kill after a delay. This is a later coordination layer in addition to the initial GPIO change and firmware watchdog.

## More views

![Raspberry Pi and display connection with breadboard wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_3.jpg)

Raspberry Pi and display connection with breadboard wiring.

## Code for this revision

Exact archived source excerpts. The file labels identify their revisions.

### motor_2026-07-21.py · lines 409–430

Code attachment sent July 21; a dated availability checkpoint, not a work-time record.

```python
def shutdown(exit_code: int = 0) -> None:
    global running, shutdown_started

    if shutdown_started:
        return
    shutdown_started = True
    running = False

    print("SHUTDOWN -> sending STOP ALL", flush=True)

    if arduino is not None:
        arduino.emergency_stop()
        time.sleep(0.05)
        arduino.close()

    if scale_serial is not None:
        try:
            scale_serial.close()
        except Exception:
            pass

    raise SystemExit(exit_code)
```

### timer_controller_later.ino · lines 676–685

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
void updateWatchdog() {
  if (augerMode == AUGER_STOPPED) {
    return;
  }

  if ((uint32_t)(millis() - lastSerialContactMs) > SERIAL_WATCHDOG_MS) {
    stopAugerImmediate(false);
    Serial.println(F("FAULT WATCHDOG"));
  }
}
```

I ended up with several stop paths, each for a different failure or exit case. I still don't have measured shaft-stop times for all of them. The practical change was that stopping had become something the programs deliberately requested, instead of something I assumed would follow from closing them.

<details>
<summary>Notes added while reconstructing this entry</summary>

The early symptom was slow rotation after motor_scale terminated. I rerouted EN to a Pi GPIO as recorded in the M2 notes. Although those notes attribute the behavior to noise, no waveform or comparable measurement establishes the exact electrical mechanism. The observed unwanted motion and the enable-wiring change are the supported parts of the diagnosis.

The saved code shows normal cleanup, signal handling, and lost-communication stop routes. It doesn't contain a measured physical stop time for each case. I kept the distinction between sending a stop and observing the shaft stopped, especially because residual motion could add powder after apparent software completion.

</details>

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R13_stop_unwanted_motion_after_program_termination_and_add_layered_shutdown_behavior.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-10-27: J12 Sugar settings made cornstarch crawl

**Total time spent: 2 hours**

*Milestone 2 | Retrospective build notes*

The cautious finishing settings made sense for sugar. Put cornstarch through the same sort of small movements and the end of a run could get extremely slow. Sometimes a command that added useful sugar barely delivered anything from the clumpier material.

I split the behavior into two control families instead of continuing to look for one setting that suited everything. Powder selection now chose speed, pulse size, and waiting time. It was a much more manageable direction than maintaining eight separate control programs.

![Physical auger and hopper component used to illustrate the cornstarch geometry discussion.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_9.jpg)

Physical auger and hopper component used to illustrate the cornstarch geometry discussion.

I had to keep the labels from misleading me, though. Cocoa and cinnamon fed relatively readily in the mechanism according to the notes, but the archived program places them in NON_FREE_FLOWING. That name means 'use these parameters' in this code. It isn't a complete description of the powder.

Also, pulse speed and pulse size aren't the same adjustment. More steps changes the angular movement; a higher rate gets through those steps faster. Then the settling delay controls when I look at the scale again. Those three knobs were easy to blur together when all I wanted was a run that finished faster.

## Profiles and pulse settings

The July Python archive maps granulated sugar and table salt to FREE_FLOWING. Powdered sugar, baking soda, cornstarch, ground cinnamon, flour, and cocoa are mapped to NON_FREE_FLOWING. The descriptive behavior notes call cocoa and cinnamon fine and relatively free-flowing, so the software family name isn't a universal physical classification. It identifies a chosen control profile for this implementation.

In the July Arduino configuration, free-flowing APPROACH/FINE/FINAL pulses contain 8, 4, and 1 steps at 1100, 700, and 400 pulses per second. The other family uses 20, 10, and 3 steps at 1500, 1000, and 650 pulses per second. Continuous FREE rates are 4000 TURBO and 2500 NORMAL, while NONFREE uses 6000 and 4000. These values are electrical step pulses, not rotations per minute or grams dispensed.

The distinction between pulse size and pulse speed is important. Changing step rate alters how fast a commanded movement occurs; changing the number of steps changes its angular extent. Neither has a fixed mass conversion across all powders. Settling time adds a third variable because the controller may need to wait for discharged material to arrive and for the averaged scale value to catch up.

The later controller stores editable profiles in dictionaries, normalizes case and spacing in powder names, rejects unknown names, and checks for finite, ordered thresholds. It also contains a per-powder override dictionary, empty in the recovered file. That provides an extension point without establishing that all eight materials received individual calibration.

## More views

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## Code for this revision

Exact archived source excerpts. The file labels identify their revisions.

### auger_july.ino · lines 43–80

Recovered Library auger-only source; its 10,932-byte size matches the July email attachment. Content identity was not proved by size alone.

```cpp
const uint32_t FREE_TURBO_RATE = 4000;
const uint32_t FREE_NORMAL_RATE = 2500;

const uint32_t NONFREE_TURBO_RATE = 6000;
const uint32_t NONFREE_NORMAL_RATE = 4000;

// Ramp continuous motion up instead of jumping instantly to full speed.
const uint32_t CONTINUOUS_START_RATE = 400;
const uint32_t ACCELERATION_STEPS_PER_SECOND_SQUARED = 9000;
const uint32_t ACCEL_UPDATE_INTERVAL_US = 5000;

// ============================================================
// PULSE TUNING
// ============================================================

const uint16_t FREE_APPROACH_STEPS = 8;
const uint32_t FREE_APPROACH_RATE = 1100;

const uint16_t FREE_FINE_STEPS = 4;
const uint32_t FREE_FINE_RATE = 700;

const uint16_t FREE_FINAL_STEPS = 1;
const uint32_t FREE_FINAL_RATE = 400;

const uint16_t NONFREE_APPROACH_STEPS = 20;
const uint32_t NONFREE_APPROACH_RATE = 1500;

const uint16_t NONFREE_FINE_STEPS = 10;
const uint32_t NONFREE_FINE_RATE = 1000;

const uint16_t NONFREE_FINAL_STEPS = 3;
const uint32_t NONFREE_FINAL_RATE = 650;

// If the Pi disappears while the auger is moving, stop automatically.
const uint32_t SERIAL_WATCHDOG_MS = 2000;

// ============================================================
// MOTOR STATE
```

### controller_later.py · lines 81–100

Recovered later Library controller; its settings are distinct from both July snapshots.

```python
def get_profile(powder_name: str) -> tuple[str, dict]:
    key = " ".join(powder_name.lower().split())
    if key not in POWDER_CATEGORIES:
        raise ValueError(f"Add {powder_name!r} to POWDER_CATEGORIES before dispensing.")
    category = POWDER_CATEGORIES[key]
    if category not in ("FREE", "NONFREE"):
        raise ValueError(f"Invalid category for {powder_name!r}: {category}")
    settings = CATEGORY_PROFILES[category].copy()
    overrides = POWDER_OVERRIDES.get(key, {})
    unknown = overrides.keys() - settings.keys()
    if unknown:
        raise ValueError(f"Unknown profile settings: {sorted(unknown)}")
    settings.update(overrides)
    if any(not isinstance(v, (int, float)) or not math.isfinite(v) or v < 0
           for v in settings.values()):
        raise ValueError("Profile values must be finite, nonnegative numbers.")
    if not (settings["tolerance_g"] < settings["fine_to_final_g"] <
            settings["normal_to_fine_g"] < settings["turbo_to_normal_g"]):
        raise ValueError("Thresholds must increase: tolerance < final < fine < normal.")
    return category, settings
```

## Still to check

Two families made the configuration less unwieldy. They still needed checking against each powder's actual result. A shared dictionary is convenient, but it can't make flour behave like salt just because both names are in the same menu.

<details>
<summary>Notes added while reconstructing this entry</summary>

A small finishing motion that limited sugar overshoot could deliver very little cornstarch. I made powder selection affect two layers: the mapping from a name to a control family and the motion and settling parameters assigned to that family. This preserved one control structure while allowing different behavior.

This left me with a smaller configuration space than eight completely independent programs or a barcode database. I still needed to retain the final measured result for each powder. Shared parameters can simplify operation, but the powder tests determine whether that simplification is adequate at the intended mass.

</details>

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R12_separate_powder_behavior_into_configurable_motion_and_settling_profiles.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-10-27: J11 Stopping the motor didn't stop the added mass

**Total time spent: 2 hours**

*Milestone 2 | Retrospective build notes*

Sugar was exposing the gap between a motor command and a scale result. I could be close to the target on screen while more powder was already on its way. Stop at the displayed target, and the last bit could land afterward.

I changed to faster feeding with a larger amount left, then shorter additions near the end. The important part was the pause after continuous motion. Stop, let the last addition show up, then decide what to do next. Sending a small pulse immediately from the same old reading would miss the point.

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

This helped define the phases, but it also made run time a tuning problem. Tiny pulses and generous waits could make finishing painfully slow. Shorter waits could put me back in the overshoot problem. Sugar and salt were useful here because they moved readily enough for that delay to matter.

The values below are the July 21 settings. Later versions changed them. I want to keep that distinction clear because a list of thresholds is only useful if I know which program it belongs to.

## The July 21 phase settings

The July 21 controller selects among continuous TURBO, continuous NORMAL, and APPROACH/FINE/FINAL pulses. For a free-flowing profile, continuous motion ends at 1.250 g remaining; APPROACH changes to FINE at 0.120 g remaining; FINE changes to FINAL at 0.030 g remaining. The matching non-free-flowing cutoffs are 0.500, 0.120, and 0.050 g. These are grams remaining, not percentages of the target and not elapsed times.

The transition out of continuous mode is deliberately a separate action. The controller sends an auger stop, clears its active-command state, waits for the profile's continuous-settling interval, and restarts the loop using a later mass reading. It doesn't immediately issue the first pulse using the same pre-stop value. That separation is the key implementation detail behind 'slow down near the target.'

For free-flowing material, the July 21 settling values are 0.650 s after continuous motion, 0.220 s after APPROACH, 0.450 s after FINE, and 0.750 s after FINAL. For the other family, they are 0.300, 0.100, 0.160, and 0.220 s. The Arduino owns how many steps are in each pulse; Python owns the decision about when to issue one and how long to wait before re-evaluating mass.

Targets below 0.500 g bypass continuous motion in that archive. For a 0.055 g sugar target at the start, the remaining amount is below 0.120 but above 0.030, so the old logic chooses a FINE pulse. The later July 24 revision changes that behavior. This example makes the evolution visible: a small target can't safely inherit the bulk-feed behavior of a large dose just because the powder name is the same.

The 3% project criterion differs from the code's absolute 0.001 g stop tolerance. In the July loop, remaining <= tolerance is tested before the separate overshoot branch, so an overshoot can satisfy the first condition. That implementation detail limits what the 'target reached' path means. I assessed dose error from the recorded final mass rather than treating a successful process exit as proof of accuracy.

## Code for this revision

Exact archived source excerpts. The file labels identify their revisions.

### motor_2026-07-21.py · lines 119–145

Code attachment sent July 21; a dated availability checkpoint, not a work-time record.

```python
def select_auger_command(target: float, remaining: float, powder_mode: str) -> str:
    """Choose the Arduino command for the current amount remaining."""
    profile = PROFILES[powder_mode]
    powder_token = profile.command_name

    # Tiny targets never enter continuous mode because there is too
    # little mass available to absorb startup and chute overshoot.
    if target < MICRO_MODE_LIMIT:
        if remaining > profile.pulse_approach_to_fine:
            return f"AUGER PULSE {powder_token} APPROACH"
        if remaining > profile.pulse_fine_to_final:
            return f"AUGER PULSE {powder_token} FINE"
        return f"AUGER PULSE {powder_token} FINAL"

    if remaining > TURBO_REMAINING:
        return f"AUGER CONT {powder_token} TURBO"

    if remaining > profile.continuous_to_pulse:
        return f"AUGER CONT {powder_token} NORMAL"

    if remaining > profile.pulse_approach_to_fine:
        return f"AUGER PULSE {powder_token} APPROACH"

    if remaining > profile.pulse_fine_to_final:
        return f"AUGER PULSE {powder_token} FINE"

    return f"AUGER PULSE {powder_token} FINAL"
```

### motor_2026-07-21.py · lines 540–564

Code attachment sent July 21; a dated availability checkpoint, not a work-time record.

```python
        # The first transition out of continuous mode always stops and
        # settles before any pulse is issued. The next loop uses the new
        # scale reading and may already decide that the target is reached.
        if is_continuous_command(active_command):
            arduino.stop_auger()
            active_command = None
            print(
                f"Continuous phase complete; settling {profile.continuous_settle:.2f} s",
                flush=True,
            )
            time.sleep(profile.continuous_settle)
            continue

        if is_pulse_command(desired_command):
            print(f"PULSE -> {desired_command}", flush=True)
            arduino.run_pulse(desired_command)
            active_command = None
            time.sleep(settle_time_for(desired_command, powder_mode))
            continue

        raise RuntimeError(f"Unhandled auger command: {desired_command}")


if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_stop_signal)
```

There was another catch in the July loop: the order of the stopping checks could let an overshoot take the 'target reached' path. So even the completion message wasn't enough. The final scale reading still had to be the result I judged.

<details>
<summary>Notes added while reconstructing this entry</summary>

The central control problem was that motor stop and mass stop weren't simultaneous. Powder could already be in the outlet or falling toward the cup, and the scale could report that mass after a delay. If I continued feeding until the displayed mass reached the target, the last commanded material could arrive too late to be accounted for. The notes identify this clearly for sugar and salt.

</details>

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R11_replace_continuous_feeding_near_the_target_with_stop_settle_and_pulse_phases.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-10-26: J10 Making the screen talk to the controller

**Total time spent: 2 hours**

*Milestone 2 | Retrospective build notes*

I wanted the doser to be operable without changing a number in the Python file for every run. The Pi's seven-inch touchscreen became the place to choose the powder and enter the requested mass. Even with one working hopper, I was already thinking in slots because the carousel would need that later.

I split the app from the motor-and-scale controller. The screen handled the request; the other program dealt with the balance and feeding phases. That sounded tidy, but it also meant the two programs needed to agree on what they sent each other.

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

The later implementation launches the controller as a subprocess and reads its output in the background. I didn't want waiting on serial data to freeze the interface. The progress labels also mattered more than they looked like they should: the app searches for 'Dispensed:' and 'Remaining:', so changing that text in only one file would break the display connection.

The early SOP is the simpler workflow: select slot 1, choose and load powder, tare, enter mass, save, start. The full recipe checks in the later app came afterward. I'm keeping those stages distinct instead of making the first touchscreen version sound like it already did everything.

## The handoff between programs

The later app archive gives a detailed implementation of that design: CustomTkinter creates a fullscreen 800 by 480 interface, maintains slot and recipe data separately, and includes an on-screen keyboard. The powder list contains EMPTY plus the eight tested household powders. A recipe item contains the slot, powder name, and requested amount. This is later implementation evidence, not a claim that all recipe features were present in the first M2 interface.

The launch function chooses motor_scale_control.py, builds its path relative to the app file, and starts it with sys.executable, unbuffered output, a target argument, and a powder-name argument. Standard error is merged into standard output. A background reader places each received line into a queue, and the Tk event loop checks that queue through after() callbacks. That avoids blocking the touchscreen while serial feedback and motor control continue.

The output labels 'Dispensed:' and 'Remaining:' form a contract between the programs. The app extracts their following numbers with regular expressions, and the controller retains those labels in its output. Changing one side alone could leave the display stale while feeding continued, making the text protocol part of the implemented interface.

## Code for this revision

Exact archived source excerpts. The file labels identify their revisions.

### app_later.py · lines 890–895

Recovered full later Library app; contains automatic recipes, serial discovery, and switch-indexing wording.

```python
def read_motor_output(process):
    try:
        for line in process.stdout:
            output_queue.put(line.strip())
    except Exception:
        pass
```

### app_later.py · lines 898–919

Recovered full later Library app; contains automatic recipes, serial discovery, and switch-indexing wording.

```python
def process_output_queue():
    global dispensed_this_run, remaining_to_dispense
    while not output_queue.empty():
        line = output_queue.get()
        print("[MOTOR]", line)
        dispensed_match = re.search(r"Dispensed:\s*([-+]?\d*\.?\d+)", line)
        remaining_match = re.search(r"Remaining:\s*([-+]?\d*\.?\d+)", line)
        if dispensed_match:
            try:
                dispensed_this_run = max(0.0, float(dispensed_match.group(1)))
            except Exception:
                pass
        if remaining_match:
            try:
                remaining_to_dispense = max(0.0, float(remaining_match.group(1)))
            except Exception:
                pass
        else:
            remaining_to_dispense = max(0.0, current_run_target - dispensed_this_run)
        update_progress_labels()
    if motor_process is not None:
        root.after(100, process_output_queue)
```

### app_later.py · lines 1050–1083

Recovered full later Library app; contains automatic recipes, serial discovery, and switch-indexing wording.

```python
def launch_motor(amount_to_dispense, powder_type=None):
    global motor_process
    global current_run_target, remaining_to_dispense, dispensed_this_run
    global stopped_by_user, active_run_script_name
    stopped_by_user = False
    current_run_target = max(0.0, amount_to_dispense)
    remaining_to_dispense = current_run_target
    dispensed_this_run = 0.0
    if current_run_target <= 0.001:
        completed_screen()
        return
    script_name = choose_motor_script(current_run_target)
    active_run_script_name = script_name
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    print(f"Using motor script: {script_name}")
    if powder_type is None:
        powder_type = active_run_items[recipe_run_index]["name"]
    # Hand off the same verified Uno port, not the original environment default.
    close_disk_serial()
    child_environment = os.environ.copy()
    child_environment["ARDUINO_PORT"] = ARDUINO_PORT
    child_environment["ARDUINO_BAUD"] = str(ARDUINO_BAUD)
    if disk_position_known:
        child_environment["DISK_CURRENT_SLOT"] = str(disk_current_slot)
    else:
        child_environment.pop("DISK_CURRENT_SLOT", None)
    motor_process = subprocess.Popen(
        [sys.executable, "-u", script_path, str(current_run_target), powder_type],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1,
        env=child_environment)
    threading.Thread(target=read_motor_output, args=(motor_process,), daemon=True).start()
    running_screen(script_name)
    process_output_queue()
    check_motor_process()
```

The useful result was a request going from the screen to a separate controller and progress coming back. Still two programs to keep in agreement, though. Once positioning was added, that handoff would carry state and device choices as well as the powder and target.

<details>
<summary>Notes added while reconstructing this entry</summary>

The interface gathers the powder and requested grams, displays progress, and exposes stop controls. The separate controller owns scale feedback and auger phase decisions. This division let the application describe the user's request while the controller translated measured mass into motion.

The later app adds startup checks for empty recipe slots, unknown disk position, and active motion. Those safeguards belong to the later integrated source. The initial single-doser workflow and the complete recipe app share the process boundary, but they aren't presented as one unchanged version.

The source excerpts preserve the launch arguments and progress-parsing mechanism even where original development screenshots are unavailable. They explain how a target entered in the interface becomes a controller process and how its reported progress returns to the screen.

</details>

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [Standard Operating Procedure: Safely Utilizing and Operating PharmaTech Rx's Doser](https://docs.google.com/document/d/1p1OGP37uR5EISkR5pwSQ_23Vjzx4Qd3G_bUwq5q5h0U/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R10_build_the_touchscreen_workflow_and_hand_targets_to_a_separate_controller_process.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-10-26: J09 The scale reading is behind the powder

**Total time spent: 2 hours**

I connected the balance to the Pi through its RS232 output and a USB-to-serial adapter. Now the program could use what reached the cup instead of estimating mass from how long the motor ran. That was the feedback I needed, but it came with some awkward timing.

Powder could already be in the cup before the new mass appeared in the serial reading. Smoothing the readings could make them look calmer while adding more delay. So a clean number on screen wasn't automatically a current number.

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

I used a starting baseline and calculated the increase from it. That handled the cup mass and gave me a sensible way to deal with later ingredients already sitting on the scale. I also kept the scale reader separate from the control loop, with a timestamp for the last valid update.

The other obvious bad case was a disconnected scale leaving an old low reading in memory. The auger couldn't be allowed to keep feeding against that forever. The July code has a stale-data timeout for that reason. I don't have a timed disconnect test for this version, but the stop path itself is in the source.

## Reading and using the mass

The controller defaults to /dev/ttyUSB0 at 9600 baud for the scale and /dev/ttyACM0 at 115200 baud for Arduino commands. These are separate serial devices with different roles. The mass data comes from the balance protocol through the RS232 adapter; it isn't a measurement mode created by the color of a USB socket.

In the July controller, parse_weight() finds the first signed decimal number in a received line and converts it to a float. Invalid lines produce no accepted reading. This simple parser assumes that the first numeric field is mass and the unit is grams. The raw balance message isn't preserved in the record, so stability and unit interpretation can't be inferred beyond the parser's assumptions.

The scale reader runs in a background thread. It appends accepted values to a deque with a maximum length of eight, computes their mean, and records the time of the last valid update while holding a lock. The control loop reads that shared state rather than waiting on a serial line each time. That keeps serial I/O separate from control decisions, but averaging eight samples also means the displayed/control mass can lag behind a changing physical load.

Startup waits for at least five accepted readings, with a six-second timeout. The initial baseline routine samples the current averaged mass into another ten-value window and looks for a spread no larger than 0.003 g over a four-second interval. If it doesn't find that condition, it returns the latest value. This routine is an attempt at a stable starting mass, not a metrological proof of balance accuracy or ten independent balance transmissions.

The dispense amount is calculated as current mass minus the starting mass; remaining mass is requested target minus that difference. This allows a cup already on the scale to become the reference rather than assuming the raw balance reading starts at zero. The same distinction becomes important in a multi-ingredient recipe, where the next ingredient starts above the mass of earlier ingredients.

The July control loop stops if 2.50 seconds pass without a valid scale update. This gives feedback validity a physical consequence: an old low mass can't remain a reason to feed indefinitely. The saved code establishes the timeout path, while no unplugged-scale timing measurement is available for that revision.

## Code for this revision

Exact archived source excerpts. The file labels identify their revisions.

### motor_2026-07-21.py · lines 108–116

Code attachment sent July 21; a dated availability checkpoint, not a work-time record.

```python
def parse_weight(line: str) -> Optional[float]:
    """Extract the first signed decimal number from a scale line."""
    match = re.search(r"[-+]?\d*\.?\d+", line)
    if match is None:
        return None
    try:
        return float(match.group())
    except ValueError:
        return None
```

### motor_2026-07-21.py · lines 346–366

Code attachment sent July 21; a dated availability checkpoint, not a work-time record.

```python
def read_scale() -> None:
    global current_weight, last_scale_update

    while running:
        try:
            if scale_serial is None:
                return
            line = scale_serial.readline().decode(errors="ignore").strip()
            if not line:
                continue
            value = parse_weight(line)
            if value is None:
                continue
            with weight_lock:
                weight_buffer.append(value)
                current_weight = sum(weight_buffer) / len(weight_buffer)
                last_scale_update = time.monotonic()
        except Exception as exc:
            if running:
                print(f"Scale read warning: {exc}", flush=True)
            time.sleep(0.05)
```

### motor_2026-07-21.py · lines 390–401

Code attachment sent July 21; a dated availability checkpoint, not a work-time record.

```python
def get_stable_weight(timeout: float = 4.0, spread: float = 0.003) -> float:
    readings: deque[float] = deque(maxlen=10)
    start = time.monotonic()

    while time.monotonic() - start < timeout:
        value = get_weight()
        readings.append(value)
        if len(readings) == readings.maxlen and max(readings) - min(readings) <= spread:
            return sum(readings) / len(readings)
        time.sleep(0.05)

    return get_weight()
```

Getting serial data was a big step, but it didn't remove uncertainty. The controller still had to deal with delay, averaging, and invalid input. That is why the next change couldn't just be 'stop when the display equals the target.' Too much could happen between those readings.

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R09_read_serial_scale_data_and_establish_the_baseline_mass_for_each_dispense.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-10-25: J08 Getting commanded motion out of the feeder

**Total time spent: 2 hours**

*Milestone 2 | Retrospective build notes*

I put together the first drive setup with the NEMA 17, TMC2209, and a breadboard, using the Pi 4 as the initial control connection. This was where the printed mechanism started becoming something I could command instead of only inspect or move by hand.

I needed to keep the task small enough to debug. Direction, STEP pulses, and enable first. A spinning auger would be progress, but it wouldn't tell me how many grams had reached the cup. That was a separate job for the scale.

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

The saved test files make one source of confusion obvious: the pin assignments changed. The small AccelStepper test uses STEP 3 and DIR 2, while the July controller uses STEP 2 and DIR 3. Both are real versions. Mixing them would give me a wiring problem that had nothing to do with powder.

The exact original Pi GPIO map and TMC2209 current setting aren't in the record I'm reconstructing from. I've kept the concrete later pin maps below rather than filling that gap with whichever version happens to be easiest to find.

## Pin maps to keep straight

STEP, DIR, and EN control different aspects of the drive. STEP requests incremental motion, DIR selects its direction, and EN activates or disables the driver according to its polarity. The motor winding connections and shared signal reference are separate from those logic functions. A breadboard layout records packaging, while the corresponding pin assignments identify a particular controller revision.

The later July Arduino source makes the eventual command interface concrete: auger STEP is pin 2, DIR is pin 3, and ENABLE is pin 4. In that file, LOW enables the driver and HIGH disables it, while HIGH is the dispensing direction. That's the archived Arduino configuration. It isn't the original Pi GPIO map. The timer-based firmware later uses different pins and the opposite enable level, so those diagrams must be kept version-specific.

The standalone repository test uses AccelStepper::DRIVER with stepPin 3 and directionPin 2, sets a 1000-step/s maximum, and calls runSpeed() at 600 steps/s. That is a motor-only test with a different pin order from the July controller. It doesn't contain the mass-feedback loop or establish the final integrated wiring.

## More views

![Raspberry Pi and display connection with breadboard wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_3.jpg)

Raspberry Pi and display connection with breadboard wiring.

## Code for this revision

Exact archived source excerpts. The file labels identify their revisions.

### auger_july.ino · lines 20–37

Recovered Library auger-only source; its 10,932-byte size matches the July email attachment. Content identity was not proved by size alone.

```cpp
const uint8_t AUGER_STEP_PIN = 2;
const uint8_t AUGER_DIR_PIN = 3;
const uint8_t AUGER_ENABLE_PIN = 4;

// Most stepper drivers use LOW = enabled and HIGH = disabled.
const uint8_t DRIVER_ENABLE_LEVEL = LOW;
const uint8_t DRIVER_DISABLE_LEVEL = HIGH;

// Change HIGH to LOW if the auger turns in the wrong direction.
const uint8_t DISPENSE_DIRECTION = HIGH;

// ============================================================
// SPEED TUNING
// ============================================================
// Values are STEP pulses per second, not motor RPM.
// At 1/16 microstepping on a 200-step motor:
//   3200 steps/s = 60 RPM
//   4000 steps/s = 75 RPM
```

### timer_controller_later.ino · lines 39–55

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
const uint8_t AUGER_STEP_PIN   = 9;   // OC1A
const uint8_t AUGER_DIR_PIN    = 8;
const uint8_t AUGER_ENABLE_PIN = 10;
const uint8_t AUGER_ALM_PIN    = 7;

const uint8_t DISK_STEP_PIN    = 11;  // OC2A
const uint8_t DISK_DIR_PIN     = 12;
const uint8_t DISK_ENABLE_PIN  = 4;
const uint8_t DISK_ALM_PIN     = 6;

const uint8_t DRIVER_ENABLE_LEVEL  = HIGH;
const uint8_t DRIVER_DISABLE_LEVEL = LOW;
const uint8_t DISPENSE_DIR_LEVEL   = LOW;
const uint8_t DISK_FORWARD_DIR_LEVEL = HIGH;
const uint8_t DISK_REVERSE_DIR_LEVEL = LOW;

// ============================================================
```

There was now an electrical route to drive the feeder. The next missing piece was a quantity the program could trust. Without scale input, I was still controlling motion and hoping the powder did something useful in response.

<details>
<summary>Notes added while reconstructing this entry</summary>

M2 began with one active hopper, so the electrical prototype used one NEMA 17 and a TMC2209 on a breadboard. The Raspberry Pi 4 provided the initial control connection, and the touchscreen added the user interface. At this point I needed to prove direction, enable control, and repeatable commanded motion separately from target-mass accuracy.

The saved record establishes the breadboard components and the motion-test configurations. It doesn't preserve a complete electrical test sequence, supply measurements, or the TMC2209 current setting for the initial setup. I've retained that boundary while documenting the actual code values, rather than describing unrecorded checks as successful trials.

This was the motor setup for the first scale-controlled doser. The next step was to read meaningful mass data, because a rotating motor alone can't tell the machine how much powder reached the cup.

</details>

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)
- [steppermotortest.ino](https://github.com/aaravs-s/pharmatech/blob/main/firmware/steppermotortest.ino)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R08_wire_the_first_nema_17_and_tmc2209_drive_and_establish_controlled_motion.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-10-25: J07 Adding arms without losing the screw

**Total time spent: 2 hours**

*Milestone 1 | Retrospective build notes*

I worked on a two-arm agitator connected to the same rotating component as the auger. That way one drive connection could move the screw and disturb powder farther out in the hopper. The saved models show the open triangular arms extending beyond the screw's narrow sweep.

The reach mattered more than the isolated shape. An arm could look large on its own and still miss the wall region once it was inside the hopper. Go too far the other way and it could scrape the housing. This was exactly the part the first attempt hadn't accounted for well enough.

![V5 agitator: Sketch 10 highlights the two arm profiles before Extrude 8, with the earlier screw geometry present.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_agitator_sketch.jpg)

V5 agitator: Sketch 10 highlights the two arm profiles before Extrude 8, with the earlier screw geometry present.

![V5 agitator: Extrude 8 adds two sketch faces symmetrically at 0.318 cm depth into tube adapter. The archived tree shows feature warnings, not a fully validated assembly.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_agitator_extrude.jpg)

V5 agitator: Extrude 8 adds two sketch faces symmetrically at 0.318 cm depth into tube adapter. The archived tree shows feature warnings, not a fully validated assembly.

I also considered a second screw with flights that funnel downward. That's in the planning note, but I don't have a documented comparison showing both alternatives successfully printed and tested. The constant-pitch model and the tapered proposal need to stay separate.

Adding the arms also asked more of the drive. It now had to push through powder at the agitator as well as at the screw. That was going to matter when I started trying to run the loaded feeder faster. For this stage, I was getting the mechanical arrangement into a form I could actually control.

## Arm geometry

The V5 feature history shows the arm geometry in Sketch 10 on the Top plane. The construction view highlights the arm profiles around the existing shaft and screw. Extrude 8 then selects two faces of that sketch, uses Add, enables Symmetric extrusion, sets the displayed depth to 0.318 cm, and merges into the part named tube adapter. The archived depth is approximately 3.18 mm. Recreating this feature requires the arm sketch and merge target as well as the thickness.

The open triangular arms extend the rotating envelope beyond the screw. Their purpose is to encounter powder outside the narrow feeding region and move it toward the feeder. The clearance requirement belongs to the complete hopper assembly: an isolated arm view can't establish the minimum gap throughout rotation.

Adding arms also introduced a mechanical load change. The drive now moved the screw and encountered powder through the agitator at the same time. That made loaded rotation, powder accumulation near the arm roots, and the printed attachment points relevant to later speed testing. The notes describe agitation helping with clumps, but don't record stresses or a measured power comparison.

## Saved arm and screw views

![V5 Part Studio 1, saved July 2 2026. Auger geometry with two agitator arms.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_auger_agitator.jpg)

V5 Part Studio 1, saved July 2 2026. Auger geometry with two agitator arms.

![V10 Part Studio 1, saved July 10 2026. Later view of the auger and agitator arms.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v10_auger_agitator.jpg)

V10 Part Studio 1, saved July 10 2026. Later view of the auger and agitator arms.

The feeder was no longer just a screw sitting in a hopper. There was a reason for the arm reach and a route for moving powder toward the feeding region. Next came the wiring and scale feedback. Plenty left to do before any of this could stop at a requested mass.

<details>
<summary>Notes added while reconstructing this entry</summary>

I proposed attaching two agitator arms beneath the rotating component so the same connection could turn the screw and agitation features. The design note considered both an existing-style screw with added arms and an alternative with downward-funneling flights. Only the saved configurations and explicitly recorded trials are treated as completed work in this account.

The saved Helix 1 has a single target pitch over its height. I kept that uniform screw distinct from the funneling proposal because their profiles aren't interchangeable. The recovered record doesn't establish a comparative result for the tapered alternative.

The mechanical platform now combined a single powder path with a driven screw and an agitation design for stagnant material. Closed-loop operation still required a separate set of electrical and software interfaces: motor wiring, valid scale readings, profile commands, and reliable stopping. Those became the focus of M2.

</details>

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)
- [STUFF TO FIX TONIGHT](https://docs.google.com/document/d/1usu-M_TCbRc7j5A3ndAVeFQoTAXTW40O4JjwxquL32A/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R07_model_the_two_arm_agitator_and_compare_uniform_and_tapered_flight_concepts.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-10-24: J06 Cornstarch changed the problem

**Total time spent: 2 hours**

*Milestone 1 | Retrospective build notes*

Cornstarch didn't behave like sugar at all. It clumped, jammed, and left powder around the hopper that the screw wasn't touching. Watching the auger rotate wasn't enough to tell whether the material was actually feeding.

I made the auger wider and used larger flights. The notes describe better movement after that change, with less of the tight compression I was getting in the earlier arrangement. I don't have a torque comparison for it, so 'better movement' is as far as that result goes.

![Physical auger and hopper component used to illustrate the cornstarch geometry discussion.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_9.jpg)

Physical auger and hopper component used to illustrate the cornstarch geometry discussion.

The untouched material near the sides was another issue. A bigger drive wouldn't magically bring it into the screw. I tried an agitator, but that attempt had both a failed print and an arm that didn't cover the full hopper width. Two separate problems, which was annoying: even a successful print of that shape wouldn't have reached the powder I needed it to reach.

The next geometry needed more sweep near the walls, with enough clearance to rotate after printing. I had to think about what volume of powder the mechanism actually disturbed, rather than only how much material appeared at the outlet.

## Two problems to separate

The first agitator attempt failed in printing and didn't account for the full width of the hopper. Even a successful print of an undersized arm would have left the stagnant wall region largely untouched. The redesign therefore needed an arm envelope that approached the hopper boundary while leaving enough clearance to rotate after printing and assembly.

The untouched powder near the hopper wall was an important result in its own right. Material collected in the cup could conceal that inactive region. It explained why an agitator needed to influence powder outside the screw's immediate sweep instead of only improving movement at the outlet.

## More views

![V5 flight section: Sketch 1 on Top plane before Sweep 1. The highlighted section supplies the profile for the helix sweep.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_flight_sketch.jpg)

V5 flight section: Sketch 1 on Top plane before Sweep 1. The highlighted section supplies the profile for the helix sweep.

![V5 flight: Sweep 1 adds the Sketch 1 faces along Curve 1 into tube adapter; no extra Twist or Scale is enabled.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_flight_sweep.jpg)

V5 flight: Sweep 1 adds the Sketch 1 faces along Curve 1 into tube adapter; no extra Twist or Scale is enabled.

![V10 Part Studio 1, saved July 10 2026. Later view of the auger and agitator arms.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v10_auger_agitator.jpg)

V10 Part Studio 1, saved July 10 2026. Later view of the auger and agitator arms.

I couldn't treat this as one generic 'powder isn't flowing' fault anymore. There was the screw's transport problem and the hopper's stagnant-region problem. The next arm design needed to address the second one without creating another rubbing or printing problem.

<details>
<summary>Notes added while reconstructing this entry</summary>

Cornstarch produced two related but different symptoms. It was hard to push through the auger consistently and sometimes jammed; it also remained in regions of the hopper the screw didn't reach. A larger motor might help overcome resistance, but it would not automatically bring stationary powder from the wall into the active feed region. I needed to treat transport through the screw and circulation inside the hopper as separate design problems.

I increased the auger's width and flight size for cornstarch. The intention was to reduce tight compression in the feeding space and give the material a larger surface to engage. The reported improvement was qualitative powder movement; the record doesn't contain a measured torque reduction or an optimum-profile study.

The dimensions all affected each other: screw outside diameter, housing bore, flight pitch, arm reach, and hopper wall position. Changing one affected both feeding and clearance. The saved V5 and V10 models show later auger-and-arm states, but the exact dimensional progression of the first cornstarch prototype isn't preserved.

The subsequent two-arm configuration connected circulation to screw rotation. That created a way to encounter powder farther from the center while the screw conveyed material through the feeder. The initial failed print and limited reach explain why adding those features was a functional redesign rather than an aesthetic change.

</details>

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R06_diagnose_cornstarch_jamming_and_the_first_agitator_s_incomplete_coverage.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-10-24: J05 Sugar was falling out before I started

**Total time spent: 2 hours**

*Milestone 1 | Retrospective build notes*

I revisited the removable hopper after spending time on the connection. It was meant to make cleaning easier, but the joint itself added more surfaces and recesses. Combining the funnel and enclosure removed an interface and cut down the part count. The early integrated disk concept took that simplification further, although the carousel structure changed again later.

Then sugar gave me a much more immediate problem: it came out during loading, before I intentionally turned the auger. The feeder was doing something, just not something I had commanded.

![Cross-section CAD illustrating the internal hopper, auger path, and base.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_8.jpg)

Cross-section CAD illustrating the internal hopper, auger path, and base.

I narrowed the opening near the auger exit so there was more resistance to that passive flow. The idea was to hold sugar back while idle but still let the screw drive it through. My notes describe this fixing the immediate loading spill. I don't have before-and-after aperture dimensions or a leakage-mass series, so I can't turn that observation into a zero-leakage specification.

This was a useful reminder to sort out the mechanical behavior before asking software to compensate for it. A better stop threshold couldn't prevent powder falling out before a run had even begun.

## The flow path

The early integrated-cavity concept appears in the solid carousel. The later skeletal two-plate structure is a subsequent revision with a different support arrangement. Comparing them preserves the evolution of the machine: reducing interfaces was an early design direction, while the eventual carousel continued to change during integration.

I narrowed the opening at the auger end according to the milestone notes. The aim was to restrict the bypass path through which sugar could fall immediately, while retaining a route for material pushed by the screw. This connects outlet geometry to the intended control model: the scale loop is most useful when auger motion is the main cause of additional material entering the cup.

## More views

![Single doser positioned above the balance. This photo provides setup context, not a trial result.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_7.jpg)

Single doser positioned above the balance. This photo provides setup context, not a trial result.

![V5 solid carousel: Sketch 1, Top-plane circle with displayed diameter 33 cm, before creating the disk blank.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_base_sketch.jpg)

V5 solid carousel: Sketch 1, Top-plane circle with displayed diameter 33 cm, before creating the disk blank.

![V5 solid carousel: Extrude 1 creates a 6 cm deep New solid disk blank before pocket removal.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_blank.jpg)

V5 solid carousel: Extrude 1 creates a 6 cm deep New solid disk blank before pocket removal.

![V5 solid carousel: Extrude 2 removes the eight pocket regions to 3 cm blind depth. Intermediate feature preview.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_pocket_cut.jpg)

V5 solid carousel: Extrude 2 removes the eight pocket regions to 3 cm blind depth. Intermediate feature preview.

![V5 solid carousel saved model after closing the pocket feature preview. Selected feature edges remain highlighted; later suppressed features remain visible in the tree.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_complete.jpg)

V5 solid carousel saved model after closing the pocket feature preview. Selected feature edges remain highlighted; later suppressed features remain visible in the tree.

Sugar didn't need agitation in the trials described here, which made the feeder look fairly straightforward for a while. Cornstarch was a different story. Restricting flow is helpful when material escapes too easily; it becomes a problem when the next material barely wants to move.

<details>
<summary>Notes added while reconstructing this entry</summary>

The removable hopper was initially a means to make cleaning easier, not an end in itself. I revisited it after the thread and locking iterations. If both the hopper and funnel still needed their internal surfaces wiped, separation could add cleaning work at the joint instead of reducing it. Combining the funnel and enclosure reduced the number of parts and removed an interface from the powder path.

Sugar exposed another issue during loading. Material escaped from the downstream end before the auger was intentionally turning. That was uncontrolled discharge, so adjusting a software stop threshold would not address it. The mechanical path needed enough resistance to retain the powder while the machine was idle and being filled.

My milestone notes report that narrowing the end addressed the immediate sugar-loading spill and that sugar didn't require agitation in those trials. The record contains neither the before-and-after aperture dimensions nor a measured leakage series. I regard the result as a practical response to the observed loading problem, with performance across other materials left to their own tests.

The outcome was a simpler contact path and improved control over sugar before motion began. Cornstarch then challenged the same geometry in the opposite way: instead of passing too easily, it clumped, jammed, and left material untouched. That gave the next update a concrete reason to change the flights and add agitation.

</details>

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R05_simplify_the_powder_path_and_reduce_sugar_leaking_during_loading.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-10-23: J04 The thread looked better in CAD

**Total time spent: 2 hours**

*Milestone 1 | Retrospective build notes*

The threaded hopper connection seemed like a good idea. Screw it in, keep it secure, unscrew it for cleaning. No separate latch to design. I liked how much that one interface was supposed to do.

Then I tried the printed parts. The farther they screwed together, the harder they became to turn. Instead of seating smoothly, the material started to fray and deform. That was a pretty direct answer to whether this version was usable.

![Printed blue threaded hopper components from the M1 notes.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_1.jpg)

Printed blue threaded hopper components from the M1 notes.

I couldn't pin it on one measured cause. Clearance, rough surfaces, thread geometry, alignment, print distortion: several things could have contributed. What I did know was that a cleaning interface shouldn't damage itself during assembly. Forcing it harder wasn't much of a design strategy.

I looked at the short locking movement on a blender container and tried a slot-and-tab arrangement instead. Insert the hopper, make a short movement to lock it, and let a seating surface locate it. That reduced the long sliding contact of the thread. It still left the fit, retention, and outlet alignment to get right.

## What the two interfaces ask of the print

The alternative changed the engagement path. Instead of sliding along several turns of printed thread, the hopper would insert into an interface with slots and projecting tabs, then lock through a short movement. The blender mechanism supplied the general reference. The details to work out were tab thickness, slot width, the insertion clearance, the locking stop, and the supporting surface that made the hopper sit flush.

The locking interface still had to locate the hopper, not merely retain it. Insertion clearance could make the connection easier to assemble while allowing unwanted rotation or lift. Full seating also mattered because an off-center outlet would undermine the powder path even if the tabs could be pushed into their slots.

## More views

![Printed cylindrical hopper or receiver component from the M1 notes.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_6.jpg)

Printed cylindrical hopper or receiver component from the M1 notes.

![Annotated hopper section showing the screw-in funnel concept and internal drive.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_5.jpg)

Annotated hopper section showing the screw-in funnel concept and internal drive.

![Hopper interface with locking features from the M1 notes; exact CAD revision not identified.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_3.jpg)

Hopper interface with locking features from the M1 notes; exact CAD revision not identified.

The tab-and-slot idea gave me another route, but I was also starting to question why this joint existed at all. If both sides still needed cleaning, was making them separate actually saving any work? That question ended up mattering more than making the original thread fit.

<details>
<summary>Notes added while reconstructing this entry</summary>

The connection was supposed to satisfy two requirements at once: constrain the hopper during operation and allow removal for cleaning. A thread looked attractive because it combined retention and alignment in one printed interface. The physical trial showed why nominal mating geometry wasn't enough. The parts printed, but resistance increased as they were screwed together, and the surfaces crumpled or frayed rather than seating cleanly.

The observation was progressive binding and damage. Clearance, pitch mismatch, surface roughness, first-layer distortion, and alignment were plausible contributors, but no controlled measurement series isolated one of them. I changed the engagement approach rather than assigning the failure to an unmeasured tolerance error.

This revision exposed another design question: even if a short locking connection was easier to use, did the added joint actually simplify cleaning? Both sides still introduced contact surfaces and recesses. That led me to revisit the separation of the hopper and funnel in the next iteration.

</details>

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R04_test_the_removable_threaded_hopper_and_replace_it_with_a_short_locking_interface.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-10-23: J03 The auger print had to work first

**Total time spent: 2 hours**

*Milestone 1 | Retrospective build notes*

Before I could learn anything useful about powder flow, I had to get a usable auger off the printer. The early attempts had bed-adhesion problems. Applying glue helped keep the print attached, which finally let me move past that immediate obstacle.

It's a frustrating kind of delay because it isn't the feeding problem I set out to solve. But a warped screw or damaged flight would change the clearance inside the housing, so carrying a bad print into the next test would only make the diagnosis messier.

![V5 screw path: Helix 1, circular edge input, 2 deg start angle, 3.81 cm height, 0.635 cm target pitch, clockwise.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_helix.jpg)

V5 screw path: Helix 1, circular edge input, 2 deg start angle, 3.81 cm height, 0.635 cm target pitch, clockwise.

![V5 flight section: Sketch 1 on Top plane before Sweep 1. The highlighted section supplies the profile for the helix sweep.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_flight_sketch.jpg)

V5 flight section: Sketch 1 on Top plane before Sweep 1. The highlighted section supplies the profile for the helix sweep.

I used an auger because I could control its motion and then measure what that motion delivered. I didn't expect a fixed grams-per-revolution number to work across all eight powders. The scale would eventually handle the mass; the screw first needed to give me a reasonably controllable way of adding it.

The construction views here are from the later V5 model. They show the helix, flight profile, and sweep clearly, along with the arms added later. They aren't pictures of the failed first print. I don't have its exact settings or model revision in the saved record.

## Helix and sweep settings

The archived V5 model exposes the screw construction through Helix 1, Sketch 1, and Sweep 1. In Helix 1, the selected input is a circular edge from Extrude 2. The helix uses pitch input, a 2-degree start angle, a height end condition of 3.81 cm, a target pitch of 0.635 cm, and clockwise handedness. In millimetres, the height is 38.1 and the pitch is 6.35. Dividing height by pitch gives six turns for this helix definition.

The path alone isn't a screw flight. Sketch 1 defines the section to be carried along it on the Top plane. In the construction view, the shaft and helix are present while the small flight section remains highlighted at the start of the path. Sweep 1 then selects the faces of Sketch 1, uses Curve 1 as its path, and adds the resulting material to the part named tube adapter. The archived feature has no additional profile-control mode, and Twist and Scale are unchecked.

These settings define a constant-pitch screw. A later planning note proposed flights that funnel downward, which is a different geometric idea. The six-turn helix shown here documents the uniform construction; it doesn't establish that the tapered alternative was manufactured or tested.

A successful print still had to function inside the housing. Flight thickness, shaft straightness, surface roughness, and seam position all affect the space between the screw and its enclosure. Adhesion solved the immediate manufacturing obstacle, while the following powder trials tested the suitability of the feeding geometry.

## From profile to screw

![V5 flight: Sweep 1 adds the Sketch 1 faces along Curve 1 into tube adapter; no extra Twist or Scale is enabled.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_flight_sweep.jpg)

V5 flight: Sweep 1 adds the Sketch 1 faces along Curve 1 into tube adapter; no extra Twist or Scale is enabled.

![V5 Part Studio 1, saved July 2 2026. Auger geometry with two agitator arms.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_auger_agitator.jpg)

V5 Part Studio 1, saved July 2 2026. Auger geometry with two agitator arms.

Getting a usable print only cleared the first hurdle. It still had to rotate inside the housing and move actual powder. Sugar and cornstarch were going to be much more informative than judging the flight by how clean it looked on the screen.

<details>
<summary>Notes added while reconstructing this entry</summary>

The manufacturing record identifies bed adhesion as the early printing problem and glue as the practical change that allowed a usable print. The failed print's exact revision and first-layer settings aren't preserved. The later V5 views explain the screw construction, including the subsequently added arms, without claiming to depict that first failed part.

The result of this update was a usable prototype for powder trials. It wasn't a calibrated grams-per-revolution device yet. Sugar loading and cornstarch movement supplied the next information about whether the outlet resistance and flight geometry suited different materials.

</details>

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)
- [Existing Forge journals](https://forge.hackclub.com/projects/763)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R03_build_the_auger_from_a_helix_and_flight_profile_then_obtain_a_usable_print.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)

# 2026-10-16: Getting the first powder path into CAD

**Total time spent: 5 hours**


I started with the holder, tube adapter, and bottom feeder. Nothing especially dramatic yet, but these were the parts that had to agree with each other. The shaft centerline mattered across all three. Getting each part to look right separately wasn't going to help if they forced the auger off-axis when assembled.

I also wanted to be able to take the feeder apart. Powder would touch the hopper, screw, outlet, and the joints between them, so cleaning couldn't be something I considered after everything was mounted. At this point, separate parts seemed like a sensible way to keep access and make revisions less painful.

![V1 holder: Sketch 2 on Front plane, before holder extrusion; displayed concentric diameters approximately 1.476 in and 1.777 in.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v1_hopper_sketch.jpg)

V1 holder: Sketch 2 on Front plane, before holder extrusion; displayed concentric diameters approximately 1.476 in and 1.777 in.

![V1 holder: Extrude 1, New solid, blind depth 4.724 in. Read-only feature construction preview.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v1_hopper_extrude.jpg)

V1 holder: Extrude 1, New solid, blind depth 4.724 in. Read-only feature construction preview.

The V1 model below is useful because I can follow the actual features instead of trying to explain the whole shape from an assembly screenshot. Sketch, extrusion, adapter, then the geometry around the lower shaft support. The dimensions are for this early model. The design kept changing after it.

Having a complete path to assemble was the goal here. I needed something physical to push back against the CAD assumptions, especially around fit and shaft support.

## The V1 features

The V1 Part Studio contains three main groups: powder holder, tube adapter, and bottom feeder. The holder is built through Sketch 2 and Extrude 1, the adapter through Sketch 3 and Extrude 2, and the feeder through subsequent sketches, extrusions, and Revolve 1. Separating these features preserved the construction of each interface while keeping them in one assembly context.

The holder starts with concentric circular geometry on the Front plane. The displayed sketch diameters are approximately 1.476 in and 1.777 in. Those values correspond to about 37.49 mm and 45.14 mm; their radial difference is about 3.82 mm. This is the early holder's wall geometry, not a claim that the eventual hopper used those same dimensions. Extrude 1 creates a new solid from the selected sketch face to a blind depth of 4.724 in, approximately 119.99 mm.

The adapter is created separately. Its archived Extrude 2 uses two sketch regions, a 5.118 in blind depth, and a checked starting offset of 0.197 in. Converted for comparison, those are approximately 130.00 mm and 5.00 mm. The offset is an important part of the feature definition: omitting it when recreating the model would change where the adapter begins relative to the holder and feeder.

The bottom feeder adds geometry around the shaft end. Revolve 1 selects faces of Sketch 6 and uses an edge of that sketch as its axis. A full Add revolve merges the result into the bottom-feeder part. The profile determines the section around the axis, while the axis itself determines how that section becomes the rounded support geometry.

I treated the separate parts as one assembly problem. The adapter bore, shaft centerline, and feeder support have to remain concentric; a small offset can make a nominally suitable shaft bind. The construction views follow the holder sketch, extrusion, adapter definition, feeder revolution, and complete V1 model, retaining the relationships behind the finished shape.

## The rest of the V1 construction

![V1 adapter: Extrude 2, New solid, depth 5.118 in, starting offset 0.197 in. Read-only feature construction preview.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v1_adapter_extrude.jpg)

V1 adapter: Extrude 2, New solid, depth 5.118 in, starting offset 0.197 in. Read-only feature construction preview.

![V1 feeder: Revolve 1 adds faces of Sketch 6 around its selected edge, full revolve, merged into bottom feeder.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v1_feeder_revolve.jpg)

V1 feeder: Revolve 1 adds faces of Sketch 6 around its selected edge, full revolve, merged into bottom feeder.

![V1 complete saved feeder model, after closing the feature preview. Holder, adapter, and bottom feeder are present.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v1_complete.jpg)

V1 complete saved feeder model, after closing the feature preview. Holder, adapter, and bottom feeder are present.

![Physical single-hopper prototype during powder handling.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_4.jpg)

Physical single-hopper prototype during powder handling.

![Single doser positioned above the balance. This photo provides setup context, not a trial result.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_7.jpg)

Single doser positioned above the balance. This photo provides setup context, not a trial result.

There was now a single doser I could put above the receiving container. That felt like a much more useful starting point than adding more of the carousel. Next was the screw itself, and finding out which parts of the nice concentric model survived printing and assembly.

# 2026-10-14: Define the requirements and develop the shared eight-hopper architecture

**Total time spent: 5 hours**

## Objective
Translate the compounding workflow into a machine layout and decide which hardware belongs on each hopper versus at the fixed dispensing station.

## Design process

I started by turning the idea of automated compounding into requirements I could design around. The machine needed to select an ingredient, dispense a requested mass, and use a scale to decide when to stop. I organized the project into five milestones so I could first prove the powder-feeding mechanism, then add feedback control, improve the single doser, expand to several powders, and finally integrate the complete sequence.

The original targets included eight powder positions, a 100 g capacity per doser, a 50 × 50 × 50 cm operating envelope, and final mass within 3% of the requested dose. I chose granulated sugar, table salt, cocoa, cinnamon, baking soda, cornstarch, powdered sugar, and flour to expose different feeding problems. Those were design targets rather than proof that every condition was already satisfied. The powder-contact geometry also needed attention because trapped residue and difficult disassembly could make an otherwise functional feeder impractical to clean.

This gave me a way to judge each iteration: does the change improve powder movement, reduce uncontrolled discharge, simplify cleaning, or help automate the sequence? It also kept me from building the entire carousel before I knew one doser would work.

I chose a rotary disk with eight hopper positions so several powders could share a dispensing station above one scale. Each powder would have its own hopper and feeding path, while the disk would bring the selected ingredient to the active position. This made the layout compact and gave the mechanism a clear route from one powder to a recipe containing several ingredients.

Eight evenly spaced positions imply 45 degrees between adjacent stations. That geometry matters later because the controller needs a repeatable relationship between a slot number and disk motion. At this point, though, the priority was the mechanical arrangement: leave room for the hopper, auger shaft, outlet, drive engagement, and receiving container. The disk also needed enough structure around the cavities to carry the loaded hoppers without distorting the alignment.

I deliberately separated the carousel concept from the first physical prototype. Printing all eight positions immediately would have repeated the same unknown feeder geometry eight times. A single doser let me test the part that actually moves the powder before committing to the larger structure.

I realized that an auger motor and agitator motor on every hopper could require sixteen motors for the eight-position machine. That would add cost, wiring, rotating mass, and maintenance points. I instead developed a shared drive concept in which the motors remain at the dispensing station and engage only the hopper currently above the scale.

The early idea used a motor for the auger and another for agitation. Later notes also explore driving both elements through a common rotating component, so the exact motor arrangement needs to be tied to the revision being described. The consistent design decision was to share the active drive hardware rather than duplicate motors around the carousel.

This made the coupling interface a central engineering problem. The disk needs to move freely while the drive is disengaged, but the shaft needs to transfer torque when a hopper reaches the active position. Angular alignment, engagement depth, and clearance could all prevent that transition. Reducing the motor count therefore simplified the overall machine while making the engagement mechanism more important.

## Construction and implementation detail

I separated the ingredient-selection problem from the mass-measurement problem. The disk chooses which powder path sits over the receiving container; the auger controls movement through that path; the scale measures the consequence of that motion. This distinction matters because selecting the correct hopper does not guarantee the correct mass, and controlling motor steps does not establish how much a particular powder actually dispensed.

The first architecture therefore had three interfaces to resolve: the hopper-to-feeder connection, the rotating disk-to-frame support, and the stationary motor-to-rotating auger engagement. Each powder retained its own contact path. Sharing a drive motor could reduce electrical duplication without requiring different ingredients to pass through the same auger. The contact surfaces would still need cleaning and inspection; independent paths alone do not demonstrate an absence of contamination.

For the eight-position layout, I used equal angular spacing as the starting constraint. A full revolution divided by eight gives 45 degrees per station. The later archived disk makes this concept concrete: eight pockets surround the central axis. I had to account for the hopper diameter, radial position, room around the center attachment, and the space needed by the fixed drive station. Those dimensions are coupled: enlarging a hopper can force a larger disk or reduce the material between stations.

I also distinguished capacity from dosing range. A 100 g hopper-capacity target describes how much material the hopper should hold; it does not by itself validate a 100 g dispensing run. Likewise, a 3% accuracy target needs a specified requested mass. At 5 g, 3% permits 0.150 g of error, while at 0.055 g it permits only 0.00165 g. I needed a test plan that included both useful larger doses and the difficult small-dose case rather than treating the percentage as one universal setting.

The shared drive station became the main architectural tradeoff. It reduced the number of motors carried around the carousel, but required reliable vertical engagement and disengagement. I deferred the complete carousel build while testing one powder path. That left a practical next step: obtain a printable single doser and learn whether its interfaces and powder movement were good enough to reproduce eight times.

## Image sequence

![Early eight-position solid rotary disk concept from the M1 notes.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_2.jpg)

Early eight-position solid rotary disk concept from the M1 notes.

![Early rotary and fixed-drive concept in top view.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_10.jpg)

Early rotary and fixed-drive concept in top view.

![Earlier CAD screenshot of an auger drive assembly. Original image from the milestone document.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_11.jpg)

Earlier CAD screenshot of an auger drive assembly. Original image from the milestone document.

![V5 solid carousel: Sketch 1, Top-plane circle with displayed diameter 33 cm, before creating the disk blank.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_base_sketch.jpg)

V5 solid carousel: Sketch 1, Top-plane circle with displayed diameter 33 cm, before creating the disk blank.

![V5 solid carousel: Sketch 2 on the disk face shows eight pockets, displayed 12 cm radial location and 7 cm diameter.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_pocket_sketch.jpg)

V5 solid carousel: Sketch 2 on the disk face shows eight pockets, displayed 12 cm radial location and 7 cm diameter.

## Result and handoff

The design direction was an eight-position carousel feeding one scale through separate powder paths and a shared active drive station. These were requirements and layout decisions, not completed-system test results.

## Complete from your records

Record the original requirement sheet, intended dose range, frame envelope, hopper capacity measurement, and the actual motor count for this revision.

[IMAGE PLACEHOLDER: Original annotated system sketch showing the rotating parts, stationary drive, and receiving scale.]

[IMAGE PLACEHOLDER: Early top-view CAD layout before the disk pockets were cut; use the archived V5 sequence as a later construction reference, not a contemporaneous sketch.]

# 2026-07-19: Rotary disc + Agitator

**Total time spent: 2.5 hours**

Focus: First Auger Prototype + Print Troubleshooting

**Objective**:
Create and test the first auger prototype to determine whether an auger can provide controlled powder dispensing.

Today I designed and printed the first auger prototype. I chose an auger because it gives more control than a basic gravity-fed outlet. A simple hole would allow powder to fall unpredictably, especially for free-flowing materials. An auger, however, should move powder in smaller amounts based on rotation, making it easier to control dosage through motor steps.

The first print had adhesion issues. The auger did not stick to the print bed reliably, which caused print quality problems and made the part difficult to produce consistently. I solved this by adding glue to the print surface, which improved the first-layer adhesion and allowed the prototype to print more successfully.

At this stage, I intentionally avoided adding an agitator. The goal was to isolate the auger as the main dispensing mechanism. If the hopper, auger, and agitator were all tested at once, it would be harder to know which part caused a failure. By starting with only the auger, I could test the basic powder movement first.

The first printed auger also helped reveal the importance of print orientation, bed adhesion, and thread geometry. Since the auger contains a long spiral feature, even small print defects can affect how powder moves through the channel. A rough or warped auger could increase friction, cause jamming, or make dispensing inconsistent.

Image Placeholder

![image.png](https://cdn.hackclub.com/019f7893-0bc4-7d67-9798-fd7d325dc70c/image.png)
First auger CAD model with rotary disc functionality

![image.png](https://cdn.hackclub.com/019f7894-b40f-738d-848e-a4a318a68fb3/image.png)
Auger with agitator capability as well!

End-of-Day Notes
The auger is still the strongest dispensing option because it gives mechanical control over powder movement.
Print quality matters because defects in the auger can directly affect dosing consistency.
The next step is to design a hopper enclosure around the auger and test powder flow.

# 2026-07-03: Motor Optimization + Clip-In Drive Concept

**Total time spent: 4 hours**

### Focus: Motor Optimization + Clip-In Drive Concept

**Objective:**
Reduce the number of motors required for the final eight-hopper system while keeping the powder paths isolated.

Today I focused on improving the motor layout. The original idea of placing motors on every hopper was functional, but it was not efficient for a compact machine. I developed a new concept where the motors stay fixed above the dispensing position instead of rotating with the disk.

In this version, the rotary disk moves the desired hopper above the scale. Once the hopper reaches the dispensing position, a fixed motor station would mechanically engage with that hopper. One motor would drive the auger, and a second motor could drive the agitator when needed. This would allow the active hopper to be powered without adding motors to every powder container.

This approach has several advantages. It reduces the total motor count, simplifies wiring, lowers cost, and keeps the disk lighter. It also makes the final system easier to service because the motors would be mounted in one fixed location rather than distributed across the entire rotating mechanism.

The biggest challenge I have mechanically is the **spider coupling mechanism**. The motor shafts need to reliably connect to the auger and agitator every time the disk rotates a new hopper into place. If the connection is misaligned, the motor may slip, jam, or fail to transfer torque. Because of this, the coupling will eventually need alignment features, such as keyed shafts, tapered guides, magnets, spring-loaded couplers, or compliant interfaces.

> **Key engineering problem:**
> The hopper must rotate freely when inactive, but lock into the motor drive system accurately when it reaches the dispensing station.

### Image Placeholder

![image.png](https://cdn.hackclub.com/019f263e-3107-7e95-939b-1a4125f7a2dc/image.png) 
Fixed dual-motor station concept for powering only the active hopper.

![image.png](https://cdn.hackclub.com/019f263e-f0e9-74ba-bcfa-710b7909c17e/image.png) Early clip-in drive concept for engaging the auger without placing motors on every hopper.

### End-of-Day Notes

* A fixed motor station is more efficient than motorizing every hopper.
* The rotary disk can stay mechanically simpler and lighter.
* Future work needs to focus on shaft alignment and reliable motor coupling.

---

# 2026-07-01: Mechanical Doser + Hopper Development

**Total time spent: 3 hours**

### Focus: Initial Doser Architecture + Rotary Hopper Concept

**Objective:**
Develop the ther first initial mechanical concept for a multi-powder dosing system which can dispense controlled amounts of powder while reducing cross-contamination between ingredients.

Today I created the first overall mechanical concept for the dosing system. The main idea was to use a **rotary disk** containing **eight separate hopper positions**, with each hopper dedicated to one powder. The disk would rotate until the selected powder hopper is aligned above the scale, allowing the system to dispense only the active ingredient.

The first version of the design included an **auger and agitator for each hopper**. The auger would provide controlled dispensing by pushing powder through the outlet, while the agitator would keep the powder moving inside the hopper. This seemed especially important because powders can behave very differently depending on particle size, moisture, clumping, and flowability.

A major design concern appeared early: giving every hopper its own motor would make the full device too complex. For an eight-hopper system, a separate auger and agitator motor per hopper could require sixteen motors, which would increase cost, wiring complexity, control difficulty, and mechanical weight. Because of this, I started looking for a way to keep the powder paths separate without placing motors on every hopper.

> **Design decision:**
> Instead of immediately printing the full rotary disk, I decided to first validate a single hopper and auger. This would make the prototype easier to test and reduce wasted print time if the basic dispensing geometry failed.

### Image Placeholder
![image.png](https://cdn.hackclub.com/019f1fc6-01f0-7a89-aaa4-84be04bdd33d/image.png)
Initial rotary disk concept with eight isolated hopper cavities for separate powders.
Concept showing how the selected hopper would rotate into position above the scale.

### End-of-Day Notes

* The rotary disk concept gives the system a clear path toward multi-powder dispensing.
* The biggest early issue is motor efficiency.
* The next step is to design a motor engagement system and begin prototyping one hopper before scaling to the full disk.

---

# 2026-06-30: Plan Project Overview

**Total time spent: 2 hours**

# Project Journal: Automated Powder Compounding System

## 1. Project Overview & Strategy
Before I start the project, I want to make a detailed overview of what the project as a whole is going to consist of, what different features I'm going to include, as well as a general timeframe. 

In order to separate this into manageable chunks, I'm going to split the project into **five different milestones** and key deliverables I want to achieve. This will keep me on a strict schedule so I can actually get this done before school starts!

---

## 2. Technical Deliverables & Specifications

### The Target Powders (Material Testing Suite)
The machine needs to be able to dispense all types of powders. I researched and picked eight different powders, all with completely different characteristics to test the mechanism:

| Powder | Physical Characteristic | Testing Purpose / Challenge |
| :--- | :--- | :--- |
| **Granulated Sugar** | Coarse, free-flowing | My baseline reference. |
| **Powdered Sugar** | Very fine | Prone to clumping and bridging. |
| **Table Salt** | Small, dense, free-flowing | Different particle size than sugar. |
| **Baking Soda** | Very fine and cohesive | Tests bridging behavior. |
| **Cornstarch** | Ultra-fine, light, electrostatic | Sticks to surfaces like crazy. |
| **Ground Cinnamon** | Fibrous and cohesive | A total torture-test for most feeders. |
| **All-Purpose Flour** | Cohesive, packs easily | Common compounding analog. |
| **Cocoa Powder** | Fine and oily-feeling | Cleanability challenge. |

### Core System Specifications

* **Accuracy:** Final product should be within **3% accuracy** of the listed dose.
* **Minimal Powder Loss:** Dispensing must waste as little powder as possible. No flyaways, scattering, or static-driven loss that misses the container; what leaves the doser should end up in the dose.
* **Per-Doser Capacity:** Each individual doser holds up to **100 g** of powder.
* **Power:** Runs from a single standard **120 V wall outlet**.
* **Footprint:** Operating size fits within a **50 × 50 × 50 cm** cube. (With long-term plans for the potential for twenty dosers to fit in this footprint).
* **Budget & Sourcing:**
    * The BOM should be as low as possible obviously :)
    * **Standard Parts Only:** Built from off-the-shelf or 3D-printable components—no custom castings or proprietary one-offs.

### Pharmacy-Grade Sanitation & Safety
* **No Cross-Contamination:** One doser per powder, or a documented isolation mechanism (lockable hopper, dedicated chute, purge cycle, or swappable cartridge) that proves no powder ends up in the wrong dose.
* **Pharmacy-Grade, Non-Porous Surfaces:** Every single powder-contact surface must be pharmacy-grade and non-porous: stainless, anodized aluminum, or food-/pharma-safe polymer (**PETG, PEEK, polished resin**). No raw 3D-print layer lines, bare wood, untreated MDF, or porous foams in the powder path.
* **Single-Wipe Cleanable:** The ultimate cleanability test—a single Clorox / disinfectant wipe in one swipe should leave a contact surface visibly clean. No powder caked in seams, no pockets that hold residue, and nothing tacky or grabby. It should also be dishwasher safe.

### Fits Unguator Jars
The system needs to accept and position the range of Unguator jar sizes used in compounding (from small through large) as the receiving container, and dispense cleanly into each without manual re-rigging between sizes.

* **50 g Jar:** Ø 4.5 cm × 5 cm tall
* **100 g Jar:** Ø 6 cm × 5.8 cm tall
* **200 g Jar:** Ø 6 cm × 11.5 cm tall
* **300 g Jar:** Ø 8.5 cm × 8 cm tall
* **500 g Jar:** Ø 8.5 cm × 12 cm tall
* **1000 g Jar:** Ø 11 cm × 14.8 cm tall

---

## 3. Implementation Roadmap & Milestones

### Milestone 1: Mechanical Doser
* **The Goal:** Build the part that physically dispenses the powder. It should dispense controlled amounts of powder and can even be hand-automated for now. 
* **Why it matters:** Since this is the base of the entire project, I want to get this fine-tuned first, and *then* I can focus on adding motors and more functionality. 
* **Success Criteria:** It needs to work with at least cornstarch and granulated sugars, both of which are somewhat polar opposites, and it should be able to deal with powders that compact themselves like flour.

### Milestone 2: Doser + Scale Closed Loop
* **The Goal:** Add the controller and scale so the machine weighs powder as it dispenses and stops itself.
* **Why it matters:** This creates a "closed-loop" control system where the scale's reading feeds back to the controller, replacing hand-counting and guessing on time. 
* **Success Criteria:** The system needs to automatically hit that 3% accuracy mark.

### Milestone 3: Single-Doser Full Coverage
* **The Goal:** Push the single-doser machine hard and prove it's accurate across the whole weight range, handles every single powder on the test list, and repeats run after run. 
* **Why it matters:** If this dispenser works good, then it can easily be replicated, hence why it's very important to get this to work! 
* **Success Criteria:** Consistent delivery across all 8 powders, plus screen functionality and control should be fully present on the device.

### Milestone 4: Multi-Doser Compounding
* **The Goal:** Have several dosers feed one scale and build a compound (a mixture of ingredients) where every amount adds up correctly. 
* **Success Criteria:** The machine tracks which powder is loaded in which doser, and the on-device interface grows to build recipes and manage settings.

### Milestone 5!!: Polish Everything and Make it Have Pharmacy Potential
* **The Goal:** Give the pill compounder full autonomy. 
* **Success Criteria:** An operator loads the powders, enters a recipe on the device, hits go, and walks away while the machine makes the compound from start to finish, logging every step along the way.


This is how a pill compounding pharmacy typically looks BTW, the goal is the final machine should be able to somewhat fit in this enclosure but be able to automatically do this process instead of having someone else do it
![image.png](https://cdn.hackclub.com/019f170e-5db8-7e5b-bb37-68e21c47d7b3/image.png)

