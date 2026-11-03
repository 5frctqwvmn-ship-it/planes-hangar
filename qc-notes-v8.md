# QC notes: cut-v8.mp4 (169.25 s)

Reviewed against v8-directors-cut.md (MJ's v8 script plus ORCHESTRATOR NOTES), the Beat 6 staging MJ approved, director-brief.md and host-style-guide.md. Method: 2 fps contact sheets (_qc/v8/sheets/s00 to s21.jpg), full-size frames of every named-object moment (_qc/v8/full/), Beat 6 at 12 fps (_qc/v8/b6/sh0 to sh7.jpg) with zoomed crops (_qc/v8/b6z/z1.jpg, z2.jpg, _qc/v8/b6y/z3.jpg), sherpa-onnx whisper base.en on the mix per line and on the single clips (audio8/*.wav), silencedetect and EBU R128 on the mix. I have not listened by ear; music and the worker voice filter still need a human listen.

## Verdict

Needs another pass. Beats 1 to 5 mostly work: the one-plane tutorial is clear and its callouts land on the right vehicles. Four things stop it being showable:

1. It runs 2:49. Getting to about 2:00 means cutting about 110 words from MJ's script (cut list below). At 130 to 140 wpm, the script's words cannot fit in 1:43; 383 words would need about 223 wpm.
2. Beat 6 does not match the approved staging. Hoist points at the tower, not the tarmac. The wing pass is a rectangular mask that cuts him in half. He parks on top of the plane and the camera truck, so the truck's turn and its lens are never visible. The QC bubble sits on a tug. There is no visible ground shadow. He looks pasted on.
3. Several named things are not shown at the moment they are named: the old carts on "every little action got its own cart", "this board", the CPU number (late), and "the lens".
4. A review timecode is burned into every frame (top right).

Loudness is fine: -16.1 LUFS integrated, LRA 3.0 LU, and no span under -45 dB.

## Cut list (169 s to about 2:00)

Each saving is the line's slot (speech plus its pause) minus any hold added back. These are word changes to MJ's script, so MJ needs to approve them. Tier A gets to about 2:16. Tier A plus Tier B gets to about 2:01 at about 135 wpm overall, which keeps the 130 to 140 wpm rule.

### Tier A (story-neutral)

| # | Where | Change | Saves |
|---|---|---|---|
| A1 | 0:08.0 i3 | "Trouble is, while they work, this is all you get." becomes "All you get is this:" | 2.3 s |
| A2 | 0:19.4 j1+j2 | Merge into "Let's start with one plane: one agent on the job." | 1.5 s |
| A3 | 0:28.5 j5+j5b | Cut "The big models got a little heavy for a phone, so we made these light little versions." Pop both model cards (1.3 MB, 84 KB) during j4 and hold them 1.0 s with no voice. The cards carry the joke when muted. | 4.3 s |
| A4 | 0:33.8 k1+k2+k2b | Becomes "That fuel truck is its brain, flashing amber while it thinks." | 1.2 s |
| A5 | 0:52.7 k8+k9 | Becomes "That tag's the bill:" | 1.3 s |
| A6 | 1:02.4 r1 | Cut "Now, how does everybody know what's happening?" r2 opens the beat. | 3.0 s |
| A7 | 1:27.6 f2 | Cut "Look at that, a whole flurry of activity!" The "whoa!" in f1 and the spawning planes carry it. | 3.5 s |
| A8 | 1:33.9 f4 | Cut "Good thing you know what you're looking at now!" It is a compliment and teaches nothing. | 2.9 s |
| A9 | 1:36.8 e1 | Cut "Now, it didn't start this tidy." The red old-way frame starting on e2 marks the shift (fix 6). | 3.0 s |
| A10 | 1:58.7 d2 to d3b | "Here's one whole day's work, skipping the quiet hours, and slowing down when the crew gets busy." becomes "Here's one evening's work." The 150x/600x badge shows the speed change. Music hold drops from 2.0 s to 1.5 s. This also fixes the "one whole day" error, since the footage covers 5:00 to 6:00 PM. | 4.5 s |
| A11 | 2:08.9 d5 | "scaling up and scaling down, all day long." becomes "scaling up, scaling down." | 1.0 s |
| A12 | 2:17.7 m2 | Cut "Hey there!" Speech-to-text hears it as "Tell you they're". m3 "Watch the lens, buddy." becomes his first line on arrival. | 1.1 s |
| A13 | whole film | Trim every clip's head and tail padding so measured gaps equal the scripted gaps. The pause report shows 6.5 s of excess over 65 gaps. Also set section joins to 0.8 s: k11 to r1, r5b to f1, e8b to d1, d5 to m1. | about 4.0 s |
| | | **Tier A total** | **about 33.6 s, runtime about 2:16** |

### Tier B (to reach about 2:00)

| # | Where | Change | Saves |
|---|---|---|---|
| B1 | 2:12.8 m1 | "Let's head down to the tarmac and get a closer look!" becomes "Let's head down to the tarmac!" These are the exact words in the approved staging. | 2.0 s |
| B2 | 1:56.7 d1 | Cut "Hold onto your hubcaps!" MJ dropped it in v6 decisions #4. It came back in v8, so ask him. | 2.0 s |
| B3 | 0:59.0 k11 | Cut "So you learn what things really cost." The estimate/actual pop already shows it. Ask MJ, since this is his teaching point. | 2.8 s |
| B4 | 1:13.6 r3c | Cut "so the director never has to." It comes from the ORCHESTRATOR NOTES accuracy fix, so confirm before cutting. | 2.6 s |
| B5 | 2:40.8 c11+c12 | Becomes "Now go check on your crew, partner!" This keeps the "partner" catchphrase. | 2.2 s |
| B6 | 0:24.4 j3+j4 | Becomes "Recognize it? Straight out of my son's game!" | 1.0 s |
| B7 | 0:39.0 k3 | "And when it calls a tool, out rolls the ground crew!" becomes "When it calls a tool, out rolls the crew!" | 0.6 s |
| B8 | 0:01.5 i2 | "with help from a crew of AI agents" becomes "with a crew of AI agents" | 0.7 s |
| | | **Tier A + B total** | **about 47.5 s, runtime about 2:01 (about 273 words, about 135 wpm)** |

Do not cut: "Running. / Running what?", "Yikes! / Traffic jam.", "Started with planes, ended with planes.", the radio and tower lines (r2, r2b, r3, r3b, r4, r5, r5b), "That's me, making this video!", the interview (m5, w1, m6, w2, w2b, m7), and the origin close (c9, c10).

## Numbered fixes (most important first)

1. **2:12.5 to 2:46, Hoist sits on the plane and covers what he is interviewing (S6; staging, covering, "pasted on").** From 2:18 he parks on the plane's right wing and fuselage, right on top of the yellow camera truck. You never see the truck's turn, its lens ("Watch the lens, buddy") or the truck itself. He is too big (about 40% of the pad, longer than half the wingspan), has no visible ground shadow, and floats over a 3D object instead of standing on asphalt. **Do this:**
   - Park him on the taxi-line asphalt outside the plane's footprint, below and left of the camera truck, with his fork tips about 20 px from the truck, so that the truck, its lens, the 180% pill and the REC light are all clear of his sprite.
   - Scale him so his height is about 1.3x the tug's length at that depth.
   - Add a contact shadow: a dark ellipse at 35% opacity, blurred 4 px, under his wheels, following his projected ground point.
   - Keep the wheel bob at 1 to 2 px, on twos.
   - **Accept when:** in every frame from 2:18 to 2:35, no pixel of Hoist overlaps the plane or the camera truck, and a shadow is visible under him in full-size frames.

2. **2:16.9 to 2:17.8, the wing pass slices Hoist in half (S6).** The occlusion is a rectangle (builder note: "wing hull whole plane box"). It cuts his body along a straight horizontal edge, so only his eyes and mast show above a hard line (see _qc/v8/b6z/z2.jpg, 137.10 to 137.80). This happens near the tail and right wing root, not under a wing. **Do this:**
   - Build the mask from the real plane silhouette: render the same frame with only the plane mesh visible and use its alpha, feathered 1 px.
   - Route his drive so he passes under one wingtip for about 0.5 s, mid-drive, then comes out the other side.
   - If the exact silhouette is not doable, drop the wing pass. A clean drive beats a sliced sprite.

3. **2:13.2 to 2:15.4, he points at the tower on "Let's head down to the tarmac" (S6; said = shown).** A full-height barber-pole stick runs from his box across the whole frame to the ORCHESTRATOR tower top. That is the wrong target, and the stick covers the board for 2 s. **Do this:**
   - Point down and right at Pad 1's "Making this video" plane, landing on the word "tarmac".
   - Keep the stick at most a third of the frame height, with its tip settled beside the plane, not on it.
   - Start the hop 0.2 s after the line ends.

4. **2:17.2 to 2:23, the camera truck's turn and the REC light do not read (S6).** The truck is under Hoist (fix 1). The REC light is a red dot with "REC" text floating on the floor beside the purple camera badge (2:19.4, 2:20.0), not on the truck. **Do this:**
   - After fix 1, make sure the truck visibly yaws at least 45 degrees toward Hoist over 0.6 s, starting on his arrival.
   - Mount the REC dot on the truck's projected camera-mast point, at about 6 px, blinking at 1 Hz.
   - Hold the REC dot through m3 and m4.

5. **2:28 to 2:33, the QC bubble is on the tug and labelled "QC TRUCK" (S6; said = shown, accuracy).** The tail points at the tug's orange command badge, which does not flash green, so there is no beacon flash on "Clear for takeoff". **Do this:** the overlap check really is a shell command, so be honest about it:
   - Change the label to "TUG (running the QC check)".
   - Keep "And QC?".
   - Flash the tug's badge or beacon green twice on w2b "Clear for takeoff!" at 2:31.4, with a soft ding.
   - Alternatively, only if a real QC agent plane exists in the data: send a second inspection vehicle from it. Do not use the camera truck.

6. **1:39.8 to 1:47.9, the old carts appear only on "Yikes!" (S4; said = shown, mute test).** e2 "every little action got its own cart" plays over the tidy new board. The red old-way frame shows for only 1.5 s (1:44.6 to 1:46.1) and drops off exactly as "Traffic jam" starts. The old board shown is sparse and does not look like a jam. **Do this:**
   - Start the old-way frame on e2.
   - Hold it through e5 "Traffic jam." and push in 1.1x on "jam".
   - Use the busiest old-version clip (V22b, 16 agents), moving.
   - Cut back to the tidy board on e6.

7. **Top right, whole film, a review timecode is burned in.** compose8.py line 399 always draws "m:ss". **Do this:** put it behind a flag that is off for the share build.

8. **2:15.6 to 2:46, S6 frame and caption hygiene.**
   - **Box ghost:** a grey rectangle is left where the box was during the hop (2:15.65 to 2:15.82). Fade the box's full alpha to 0, including its backing panel.
   - **Captions:** they jump from the boxed style to a wide box (2:15.7) and then to tiny unboxed text at the very bottom (2:16.5 on), over a ghosted legend strip. Keep the same caption box as Beats 1 to 5, bottom-centred, at least 22 px text.
   - **Board chrome:** the 1.41x crop leaves half the "Fit" button and the "Nov 3 9:33 AM" clock cut off at the top edge. Hide the board chrome in S6, or crop below it.

9. **2:35.5 to 2:46.3, the close is not a close-up and there is no wave (S6, ending).** Hoist stays small, mid-board, on top of the plane. **Do this:**
   - On c9, ease the camera in to Hoist (about 2.2x over 1.2 s, no cut), or have him roll toward the lens until he is about 45% of frame height.
   - He faces camera for c9 and c10.
   - Raise his fork in a wave on the final line, with squash and overshoot.

10. **1:13.6 r3b, "this board" points at empty space (S3).** The "THE BOARD / kept up to date" ring sits on floor right of the tower. **Do this:**
    - On r3b, pulse a glow around the whole field's boundary.
    - Tick one visible tag on Pad 1 (the cost chip or the 180% pill) as the pulse arrives.
    - Put the label at the field's top edge.
    - On r3 "watches the whole crew", the pulse must visibly start at Pad 1's crew vehicles (3 or 4 dots) and travel to the dish. Right now it is unclear where the dots come from (1:10 to 1:11).

11. **0:53 to 1:02, the cost numbers disagree (S2; mute test).** This was fix 11 in v6 and is still open. The tag reads "SONNET 3k $1.50" but the pop reads "ACTUAL $1.52". **Do this:** make them match, either ACTUAL $1.50 or a tag of $1.52.

12. **0:49.6 k7, the CPU callout is late (S2).** "That number" is spoken at about 0:50.0, but the CPU 180% ring and label appear at 0:51.2. **Do this:** have the ring settled by 0:49.8. The 180% pill rides on the moving camera truck, so lock the ring to its tracked position.

13. **Voice clips (audio).**
    - **m7:** the caption and the synth both lack the comma ("Keep up the good work crew!"), and speech-to-text hears "work true". Re-synth "Keep up the good work, crew!" with the comma-part method and fix the caption.
    - **m6 "And QC?":** heard as "and Q save". Synthesize as "And Q. C.?" or "And kyoo-see?", keep the clip that speech-to-text reads as "QC", and keep the end level or rising.
    - **e4 "Yikes!":** heard as "for Yikes". There is a leading fragment, so trim the head to the onset of the "Y".
    - **Tails:** i6 is heard as "just to watch you", d5 as "all day longs" and r2b as "Haiku helpers". These are leftover context-word or breath fragments. Tighten the tail trim to the end of the last phoneme and add a 30 ms fade-out.
    - **e1:** heard as "Now, if it didn't". This line goes in A9. If it is kept, listen for a phantom "if".
    - **c11:** heard as "riding a lot, a partner". Listen; if "along" smears, re-synth.

14. **1:22 to 1:31, order labels cover the tower and radio (S3/S4; covering).** "To Making this video: Brief: film the board" and "Sent out Polish the menus" sit on top of the tower, which is the sender. **Do this:**
    - Shorten them to "ORDER: film the board".
    - Place them beside the taxi line, at least 30 px from the tower and radio.
    - Hold each for 1.5 s.

15. **1:28 to 1:31, the field stretches before "stretch" is said (S4).** The widening happens during f2. With A7 applied, start the stretch on f3's word "stretch" (about 1:32 in the current timeline) and run it for 1.5 s.

16. **0:04 to 0:08, the game's own speech bubble competes with the narration (S1).** "Shake, shake, shake! Look at me, I am a happy racing machine!" covers the title while Hoist talks. **Do this:** use game footage without the bubble (0:00 to 0:03.8 is clean), or a different lap. After A1 and B8, S1 needs only about 5 s of game footage.

17. **Clock continuity (S2 to S6).** The board clock is frozen at "Nov 3 4:00 AM LIVE" through S2 to S4, the time-lapse is "Mon Nov 2" (5:00 to 6:00 PM), and S6 shows "Nov 3 9:33 AM". **Do this:** hide the board's own clock outside S5 so the only clock is the S5 widget. Rename the S5 badge from "5 A DAY, FAST-FORWARDED" to "5 AN EVENING, FAST-FORWARDED".

18. **Sound (audio; needs a listen).** cues8 MUSIC reuses cue 2 for S1b and S3 (the brief asks for a different cue per section); S1 and S7 sharing cue 1 is a fine bookend. SFX=[], so there are no sound effects at all, although the style guide and the staging call for them. **Do this:**
    - Give S3 its own cue.
    - Add exactly four SFX: a boing on the hop (2:15.4), a soft engine putt under the drive, two short chirps before each worker reply (this is the "beepy voice"), and a ding on the green flash.
    - A person must listen to confirm the worker radio filter reads as a different speaker.

19. **Script cart bounce (2:25.7 to 2:28).** The bubble tail lands correctly on the catering truck's write badge, but the truck is at the far left edge and mostly off frame, so the bounce does not read. In the crops, the bubble moves but the cart does not visibly bounce. **Do this:**
    - Frame Pad 1 so the white catering truck is fully in frame during w1.
    - Bounce the truck: 3 px up and down twice on twos, synced to w1's syllables.

## Beat 6 frame-by-frame vs the approved staging

| Staging item | Seen | Pass? |
|---|---|---|
| Hoist points from his box ("Let's head down to the tarmac") | 2:13.2 to 2:15.4, the stick points at the tower top and spans the frame | Fail (fix 3) |
| Hops out with squash and stretch | 2:15.5 to 2:16.1, leaps from the box with a stretch, then lands squashed. Reads well. | Pass |
| Box fades | 2:15.6 to 2:15.8, the box shrinks but leaves a grey rectangle | Partial (fix 8) |
| Camera eases in, no cut, to the video agent's stand | 2:12.6 hard cut from the time-lapse (fine as a scene change), then a smooth ease-in from 2:13 to 2:16 | Pass |
| Drives along the taxi line, scaled by depth, ground shadow, wheel bob | 2:16.1 to 2:16.7, drives right along the pad's top edge and scales down. No shadow visible. Bob not visible at this size. | Partial (fix 1) |
| Passes behind the wing | 2:16.9 to 2:17.8, rectangular mask slices him; not at a wing | Fail (fix 2) |
| Camera truck turns to him, REC blinks | Truck hidden under Hoist; REC is a floor dot beside the badge, from 2:18.8 | Fail (fixes 1, 4) |
| Turns to writing cart, "On revision eight, boss!", beepy, cart bounces | Bubble on the write badge, correct and readable; no SFX; cart barely in frame, no visible bounce | Partial (fixes 18, 19) |
| QC truck, "Zero overlaps. Clear for takeoff!", beacon flashes green | Bubble on the tug labelled "QC TRUCK"; no green flash | Fail (fix 5) |
| "Keep up the good work, crew!" then faces camera | Faces camera from 2:35; comma missing in the caption and the voice | Partial (fix 13) |
| Does he look pasted on? | Yes from 2:18: no shadow, sits on the 3D plane, too large, sliced by the mask | Fail (fix 1) |

## Named object highlighted when named

| Time | Named | Highlighted? |
|---|---|---|
| 0:12.3 | "Running" | Yes, ring on the terminal text |
| 0:15.1 | "airfield" | Cuts to the board at 0:16.3, at the end of the word. Acceptable; better to cut on "airfield" at about 0:15.8. |
| 0:19.4 | plane, one agent | Yes, PLANE ring 0:20.3 |
| 0:24.4 | "the plane", "my son's game" | Model cards at 0:26.8, OK |
| 0:28.5 | big models, light versions | Cards, yes |
| 0:33.8 | fuel truck, amber | Yes, FUEL TRUCK ring 0:34.1 |
| 0:39.0 | ground crew | Crew rolls out at 0:39.2, yes |
| 0:43.0 | baggage | Yes, 0:42.9 (ring overlaps the agent name tag) |
| 0:45.0 | tug | Yes, 0:44.9 |
| 0:47.2 | camera truck | Yes, 0:47.4 (truck partly under the name tag) |
| 0:49.6 | "that number" (CPU) | Late, 0:51.2 (fix 12) |
| 0:52.7 | tag, estimate, actual | Yes, but the numbers disagree (fix 11) |
| 1:05.4 | tower, Radio | Radio ring yes; tower visible, no ring (OK) |
| 1:10.0 | "the whole crew" | Pulse origin unclear (fix 10) |
| 1:11.7 | "this board" | Ring on empty floor (fix 10) |
| 1:16.2 | Orchestrator | Yes, 1:16.8 |
| 1:21.1 | order, taxi line | Yes, 1:20.9; label covers the tower (fix 14) |
| 1:25.0 | more jobs | NEW PLANE labels from 1:25.3, yes |
| 1:31.1 | "airfield stretch" | Stretch happened earlier (fix 15) |
| 1:39.8 | "every little action got its own cart" | No (fix 6) |
| 1:44.7 | Yikes, traffic jam | Old way shown 1:44.6 to 1:46.1, too short and sparse (fix 6) |
| 1:47.9 | "its own pad" | No ring on pads; add a 0.5 s ring on the three pads |
| 1:51.9 | "Started with planes" | No ring; optional ring on the three planes |
| 1:58.7 | day's work, quiet hours, busy | Clock widget and 150x/600x badge, yes |
| 2:18.8 | "the lens" | Hidden under Hoist (fixes 1, 4) |
| 2:24.2 | script cart | Bubble yes, cart barely in frame (fix 19) |
| 2:28.0 | QC | Tug, mislabelled (fix 5) |

## Keep (do not break)

- The game opening and the black terminal with "Running... Running what?", the ring on "Running" and the big question mark.
- A 1 s glimpse of the wide board, then Pad 1 isolated with the other pads dimmed. It teaches the vocabulary cleanly.
- The colour-coded callouts (PLANE, FUEL TRUCK, BAGGAGE, TUG, CAMERA TRUCK, COST TAG) landing on the right vehicles, and the estimate/actual pop with a count-up.
- The FULL MODEL 1.3 MB / LIGHT MODEL 84 KB cards.
- The RADIO "a light Haiku helper" and ORCHESTRATOR "= the director" labels, and orders flying down the taxi line.
- NEW PLANE / "and another" spawns and the field expanding.
- The red-framed "THE OLD WAY: A CART PER ACTION" device (just move it and hold it longer).
- The S5 clock widget: big time, day, 150x BUSY / 600x QUIET badge and the progress bar.
- The Beat 6 hop: stretch on the leap and squash on landing (2:15.5 to 2:16.1), the ease-in with no cut, and depth scaling on the drive.
- The script cart bubble's styling and tail placement.
- The title card text and its 3 s hold.
- The mix: -16.1 LUFS, music and room tone under every pause, no dropouts, chapter badges top left.

## Re-check v9

This was a quick re-check. I judged cut-v9b.mp4 (2:09.4) in full and spot-checked cut-v9a.mp4 (2:21) and cut-v9full.mp4 (2:47) only where they differ. Method:
- 2 fps sheets for v9b (_qc/v9b/sheets/).
- Full-size and zoomed frames of Beat 6 (_qc/v9b/full/, _qc/v9b/z/, _qc/v9b/cu/, plus _qc/v9full/b6.png and _qc/v9a/b6.png).
- Whisper speech-to-text on each full mix, per line (_qc/v9full/stt.txt and _qc/v9a/stt.txt; v9b below), and on the isolated v9b clips, with onset and tail energy checks.
- Silencedetect: 0 spans under -45 dB in all three cuts.

### Top 5 fixes from v8

1. **Hoist parked clear, with a shadow: mostly landed.**
   - From 1:41 he waits on the taxi-line asphalt right of Pad 1, clear of the plane, and his scale is right.
   - He still overlaps the right half of the yellow camera truck and the nose of Pad 2's white cart (see _qc/v9b/z/z.jpg).
   - His fork tips touch the right frame edge.
   - The shadow is only faintly visible while he drives (1:40.2) and not readable once he is parked.
2. **Wing pass: resolved.** It was dropped, as I allowed, and nothing slices him now.
3. **Point down with a short stick: half landed.**
   - The stick points down and is about a third of the frame height. Good.
   - In v9b the stick is fixed to the screen while the camera eases in, so its tip drifts onto Pad 3's catering cart (1:38.3) instead of the "Making this video" plane.
   - In v9a and v9full the tip lands just under Pad 1's name tag, which is acceptable.
4. **Camera truck turn and REC light: partly landed.**
   - REC now blinks at about 1 Hz on the camera badge, next to the truck, from 1:41.4. Readable.
   - The truck does not visibly turn: its heading is the same at 1:39.6 and at 1:41.3.
5. **QC bubble with a green flash: landed.**
   - The label reads "TUG (running the QC check)", the tail sits on the tug's command badge, and the badge flashes green on "Clear for takeoff!" (1:53.8), with a ding.
   - Clutter flash: the timing landed. It runs on e2 through e5 (1:11.0 to 1:18.7) with a push-in on "jam". It still uses the sparse V22b clip, so with the sound off it does not read as a jam.

### Other v8 findings

**Landed:**
- Burned-in timecode removed.
- Game speech bubble gone.
- CPU callout on time (0:39.3).
- Cost tag and actual now match ($1.52).
- Whole-board glow on "this board".
- The crew-to-dish pulse reads.
- Short order labels, clear of the tower.
- Field stretches on "stretch".
- Board clock hidden; the S5 badge reads "5 AN EVENING, FAST-FORWARDED".
- Captions stay boxed in S6, and the board chrome is hidden there.
- The close is a no-cut push-in on Hoist.
- S3 has its own music cue.
- The comma on "Keep up the good work, crew!" is fixed in the caption.
- The script cart moves and turns under its bubble.

**Still open:**
- **Board label:** the "THE BOARD: kept up to date" text spills past its box (0:54.6). Widen the box 16 px.
- **Close-up push:** about 0.6 s (1:57.6 to 1:58.2). Ease it over 1.2 s.
- **Sound effects:** there are now about 30, against "used sparingly". The REC SFX fires at 1:41.4, exactly on "Watch the lens", and the mix is heard as "Watch the land" while the isolated clip reads "lens". Move the REC beep to the end of m3 or later, and thin out the beat 2 pops (one pop per callout is fine; drop the extra chirps on every speed change in S5).
- **Music:** S6 reuses S2's cue 3. Minor.
- **Wave:** I did not confirm a wave on the last line.

### v9b voice (speech-to-text on the mix, isolated clips checked)

| Line | Heard | Cause and remedy |
|---|---|---|
| m6 "And QC?" (1:50.4) | "I'm QC" (clip: "and QC") | The clip ends mid-sound: the last 60 ms rises from -32 to -13 dB, which means a leaked context word was cut hard. Trim to the end of "C", add a 30 ms fade, and check that the head has no leading blip. |
| m7 "Keep up the good work, crew!" (1:55.2) | "And keep up the good work on crew" (clip: "Oh, Drew") | There is a 140 ms leading fragment before "Keep" and a weak "crew". Trim the head to the onset of "K", re-synth "crew!" as its own part, and pick the variant that speech-to-text reads as "crew". |
| e4 "Yikes!" (1:15.8) | "On Yikes!" / "For Yikes" | The clip starts at -39 dB in its first 20 ms (hard cut into sound). Re-cut from the true onset with a 10 ms fade-in. The same artifact is in v9a ("Olyikes") and v9full ("on your ex"). |
| d5n "scaling up, scaling down." (1:33.1) | "A scaling up, a scaling down" | There is a 100 ms fragment before "scaling". Trim the head. |
| k10 "An estimate up front," (0:44.0) | "I'll un-astimate up front" | Leading fragment, and the tail ends at -26 dB (hard cut). Trim the head and fade the tail. |
| c12n "Now go check on your crew, partner!" (2:03.2) | "your crew apart now" (clip: "crew apartner") | The comma pause is missing. Build it as two parts with 0.3 s of silence, so "partner" lands clean. This is the catchphrase. |
| r2b, r4 | "and our ... helpers", "Lup in the tower" | Same as in v8. Minor: listen and trim if audible. |

Everything else reads correctly, including "Haiku", "Orchestrator", "Running what" and "That's me, making this video".

### Verdicts

- **cut-v9b (2:09): the cut to show MJ, after one short pass.** It tells the whole story, and Beat 6 now mostly matches the staging. Fix in this order:
  1. Track the stick tip to Pad 1's plane per frame (or point before the ease-in starts).
  2. Nudge Hoist about 30 px down and left so he clears the camera truck and Pad 2's cart, darken the shadow, and add a visible yaw of 45 degrees or more on the truck over 0.6 s as he arrives.
  3. Fix the six clip edges in the table (m6, m7, e4, d5n, k10, c12n).
  4. Move the REC beep off "lens" and thin the SFX.
  5. Optionally, reach about 2:05 by trimming the remaining 3.2 s of pause excess and taking the m1n drive hold from 3.0 s to 2.4 s.

  If MJ just wants to see progress, it can be shown now as a work-in-progress cut.
- **cut-v9a (2:21): same fixes as v9b, except the pointer, which lands acceptably.** Also fix "Keep up the good work, crew!", heard as "accrue". It is the safe fallback if MJ wants his lines kept, but it drags in Beats 2 and 4.
- **cut-v9full (2:47): reference only, not for showing.** It keeps the false "one whole day ... all day long" over a one-hour time-lapse. It also has these speech-to-text misreads: "Hey there!" heard as "Tell you there", "And QC?" as "Un-Q, see?", "work, crew" as "accrue" and "Yikes!" as "on your ex". On top of that, it has the same Beat 6 issues as v9a.
