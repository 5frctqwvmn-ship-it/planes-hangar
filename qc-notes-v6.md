# QC notes: cut-v6.mp4 (126.8 s)

Reviewed against v6-brief.md (with the MJ ADDENDUM on pauses), v6-decisions.md and director-brief.md. Method: frames at 4 fps and 2 fps contact sheets (_qc/v6/sheet*.jpg), full-size checks of doubtful frames, motion/freeze measurement per second on the board area, sherpa-onnx whisper on the mix and on single clips, pitch tracking (librosa pyin) on every voice clip, silencedetect and momentary loudness on the mix.

## Verdict

Needs another pass. The pause rule is met on paper (no gap under 0.25 s; comma gaps 0.39 to 0.43 s) and the structure now matches the v6 script, but four things stop it being showable: (1) it runs 126.8 s; (2) the commas and questions do not sound like a person showing something: every comma fragment ends with a full sentence-final pitch drop and every question falls, so lists still read as a list of full stops; (3) several named things are not on screen when named (the airfield, the amber light, the tug, the tower, the "organized" board); (4) the one-job walkthrough does not exist on screen: at 1:14.5 to 1:17.7 the stick points at empty space under a stale RADIO card, over 2.4 s of dead air.

## Cut list (126.8 s to about 109 s)

Guided by the brief's priority: comprehension first, then pacing, then fidelity. Seconds are measured from the index and pause report.

| # | Where | Cut or change | Saves |
|---|---|---|---|
| C1 | 0:26.1 s3b | Cut "Same plane, easy on your phone." The CITY MODEL card already says "same plane, light". s3 to s4b gap becomes 0.6 s. | 3.0 s |
| C2 | 0:29.4 s4b | Cut "And for the airfield, we already had a whole hangar full." Move the board reveal to i6 (see fix 3) so the picture carries "the planes come from the game". Keep a 0.8 s hold on the board before h1. | 3.2 s |
| C3 | 0:40.2 h3b | Shorten to "and when it gets to work, out rolls the crew." The current line says "reads a file or runs a command", then h4 and h5 say exactly that again two seconds later. | about 1.2 s |
| C4 | 1:13.6 to 1:18.0 (t5 to e1, 4.46 s) | Replace the broken 3.2 s stale-pointer demo with a 2.5 s working walkthrough (fix 4). | 2.0 s |
| C5 | 1:30.3 e7 + e7b | Cut "An icon for every job, a parking spot for every crew." Show the tidy board under e6 instead (fix 6). Brings the history beat to about 16 s, close to the decided 15 s. | 3.9 s |
| C6 | 1:49.5 c2 | Cut "What's going on while I'm waiting?" Its setup line ("This whole thing started with one question") was dropped, so it now lands as an orphan question; the origin is carried by "We built a game for a four-year-old. Then we built one for his dad." | 2.5 s |
| C7 | 0:17.0 i6 to s1 | Gap 1.23 s to 0.8 s. | 0.4 s |
| C8 | 1:37.5 e8b to d1 | Gap 1.29 s to 0.9 s (still a long beat after the point line). | 0.4 s |
| C9 | 2:02.5 credit card | Hold 4.3 s to 3.5 s (with the larger text from fix 15 it still reads twice). | 0.8 s |
| C10 | 0:00 to 0:00.6 | Lead-in before "Howdy!" 0.6 s to 0.3 s. | 0.3 s |
| | | **Total** | **about 17.7 s, new runtime about 109 s** |

Spare cuts if the rebuild lands over 110 s: h11 to t1 gap 1.25 s to 0.9 s (0.35 s); s1 to "Every plane here comes straight from the game." (about 0.4 s).

Do not cut: "Running." / "Running what?", "Yikes!" / "Traffic jam.", the 1.5 s Sunday SFX-only hold, "That's me, making this video." (the highlight works), "So you learn what things really cost."

**Sky City gag: tighten, do not cut.** It does not fail: the idea (big plane too heavy for a phone, light twin made for the board) reads from the two cards even with sound off. What hurts it is length (15.3 s, four lines), a frozen background (0:22.4 to 0:29.0 is a still frame) and Hoist just standing next to the cards. With C1 and C2 it becomes three lines and about 9 s; with fix 5 Hoist does the joke with his body.

**Dropped lines:** leave green light out (the legend shows it and amber is the one light the story needs). Leave the tower-carts line out at this length; restoring it costs about 3.5 s and would push past 110 s. If MJ wants it back, build it with fix 2's method and take the two spare cuts.

## Numbered fixes (most important first)

1. **Commas and questions sound read, not shown (whole film; audio).** Pitch tracking of every clip: every comma fragment ends with a full statement drop, same as a full stop: "It takes your request," -4.1 semitones, "plans the work," -4.5, "An estimate up front," -6.8, "It flashes amber while it thinks," -5.1, "Started with planes," -4.2, "Same plane," -4.6, "Thanks for riding along," -6.1. That is why "request [pause] plans the work [pause] and sends" sounds like three separate statements read off a card. Questions also fall: "And that tag?" -5.2, "and pretty soon?" -6.7, "And that plane right there?" -4.5. **Fix:** keep MJ's rule (each list item its own clip, silence inserted in the edit), but synthesize every non-final item with the next word as context and trim it off: synth "It takes your request, and", cut at the onset of "and", keep "It takes your request" (Kokoro then gives "request" its continuation lift). Same for t3b ("plans the work, and"), h3, h10, e2, e7 if kept, e8 ("Started with planes, ended"), i2, i3, i6, s4b, d1, d5, c11. For the yes/no and teaser questions (h9, e3, d4), synth with a trailing context word ("And that tag? Hm.") and trim; if the end still falls, bend the last 0.2 s up 2 to 3 semitones with a 10 ms crossfade. **Accept when:** comma fragment ends within 2 semitones of its own median or above it, sentence ends still fall 3 or more, h9/e3/d4 end rising, and every gap is still 0.25 s or more.

2. **Dead air in the pauses (0:06.8, 0:17.7, 0:59.4, 1:01.9, 1:13.6 to 1:14.7, 1:15.3 to 1:17.7, 1:37.9, 1:48.9; audio).** Silencedetect at -45 dB finds 12 holes where the mix drops to digital silence, worst 2.37 s at 1:15.3. A pause over silence sounds like a dropout, not a host taking a breath while he shows you something. **Fix:** crossfade cues 0.5 s at each section join; give the S3 cue a sustained pad so it never drops out; add a room-tone floor around -40 dBFS under the whole voice stem. Re-run silencedetect: no span under -45 dB longer than 0.15 s except the final frames.

3. **0:13.8 i6, "airfield" over the terminal (S1b; said = shown, comprehension).** "So we built them an airfield of their own" plays over the black terminal; the next shot (0:18.1) is game footage of Sky City, so a first-time viewer thinks the airfield is the game. This is exactly the game-vs-dashboard confusion the brief asks to fix. **Fix:** on the word "airfield" (about 0:14.6) cut to the wide board with planes on their pads, hold through "just to watch". Then s1 "Every one of these planes comes straight from the game" plays over the board with a 0.4 s ring on two planes, then cut to the Sky City gag. With C2 the board then returns for h1.

4. **1:05 to 1:17.7, the one-job walkthrough is not shown (S3; comprehension, mute test).** The four chips at the top ("1 REQUEST ... 4 STATUS + COST") are the only walkthrough; chip 4 never lights until 1:17; nothing shows a request; and at 1:14.5 the shot cuts back to the tour close-up while the stick still points at the radio's old screen position (now off the left edge, the stick crosses the whole board to nothing) under the RADIO card. **Fix:** stay in the wide shot. On t3 "It takes your request," drop a small REQUEST ticket into the tower (Hoist can flick it in; chip 1 lights). On t3c the stick tip rides the moving arc dot (not the arc start) down to plane 2 (chip 2). t5 radio as now. Then 2.5 s silent: the stick moves to plane 2, its crew rolls out (chip 3 lights as the first cart moves), push in 1.3x on its tag as the number ticks (chip 4). Swap the left card to "ONE JOB / request, tower, crew, cost". No cut back to the close-up.

5. **0:18.1 to 0:29.0, Sky City gag frozen and static (S2).** Board-area motion is zero from 0:22.4 to 0:29.0 (a still game frame for 6.6 s, likely the reported "6 s freeze"); the two picture cards are small and partly covered by the subtitle (bottom-left) and Hoist (right edge); the "strain" SFX at 0:22.9 plays with no strain on screen. **Fix:** keep the game footage moving (continue city.mjs footage or a slow 1.05x push). Make the gag physical: on s2, Hoist lifts the FULL MODEL card on his forks and sags (squash, strain SFX); on s3, the CITY MODEL card pops onto his forks and he springs up (pop). Enlarge the cards so "1.3 MB" and "84 KB" are at least 22 px tall and clear of the subtitle and Hoist.

6. **1:18 to 1:34, history picture contradicts the words (S4; mute test).** "Every little action got its own cart ... Traffic jam" plays over a sparse old board that is frozen from 1:24.5 to 1:28.1 (motion zero), while "So we organized the chaos" cuts to a board that looks more crowded (icons everywhere). Sound off, it reads backwards. **Fix:** under e2 to e5 use the busiest old-version clip (V22b, 16 agents) moving, carts piling up, with a 1.1x push-in on "Traffic jam" synced to the screech. Under e6 cut straight to the current tidy board (the 1:34.5 shot) and hold it through e8/e8b; ring the planes on "Started with planes".

7. **0:38.1 h3, "flashes amber" with no amber (S2; said = shown).** The fuel truck under the stick has a green halo the whole time (checked frame by frame 0:37.5 to 0:41.5) and the stick tip sits on top of its small beacon. **Fix:** pick a moment in the tour recording where that fuel truck's halo is amber, or use a fuel truck that is amber at 0:38 (there are amber halos on screen, e.g. bottom left at 0:38), and park the stick tip just beside the beacon, not on it. On h3b "out rolls the crew", sweep the stick to the carts that roll out or ring them.

8. **0:46.4 h5, "The tug" points at the legend (S2; said = shown).** The stick tip lands on "green working" in the legend strip below the board; the tug is above it at about (160, 590) in frame coordinates. **Fix:** retarget the tug pointer to the tug cart itself; if it is behind the legend at that moment, nudge the tour camera up 40 px for this beat or pick a tug higher on the board.

9. **1:03.1 t1, tower named before it is shown (S3).** "Up at the tower" says "tower" about 1:03.6; the camera is still pulling out and the stick lands at 1:04.0. Also the board is frozen 1:00.2 to 1:02.8 under h11. **Fix:** start the pull-out at 1:01.9 (right after h11 ends, inside its 0.9 s pause) so the wide is settled and the tower ringed by 1:02.9; the freeze goes away with it.

10. **0:44.4 baggage pointer only 0.1 s ahead of "Baggage" (S2).** The stick is still swinging at the first syllable. **Fix:** land it at 44.1 or earlier; rule of thumb for every pointer: settled 0.3 s before the name.

11. **0:53 to 1:02, cost numbers disagree (S2; mute test).** The plane's tag reads "SONNET 2.1M $1.52" while the popup reads "ESTIMATE $13.05 / ACTUAL $14.49". A careful viewer sees two different prices for one thing. **Fix:** make the popup numbers match the job the stick points at (for example estimate $1.40, actual $1.52), or point at a job whose tag shows the popup total.

12. **Clip glitches (audio).** h10b is heard as "afters" in its own clip (tail breath or sibilant): re-synth "and the real number after." and trim the tail tighter. h9 is heard as "On that tag": the 30 ms pre-roll clips the soft "And"; raise pre-roll to 80 ms for every clip that starts with a vowel.

13. **1:05 to 1:17.7, chip row covers the board controls (S3).** The four chips sit over "+ - Fit" and the "LIVE" pill and are about 11 px text. **Fix:** move them into the empty left label box under the card, or a strip below the top bar, at 16 px or more.

14. **Transition frames.** 1:08.0: the label card goes blank with a stray dash for one frame between TOWER and ORDER; switch cards on one frame or crossfade. 1:49.0: one near-black frame with a small Hoist before the close-up; replace with a 0.3 s crossfade or a push-in to Hoist.

15. **Close (S6).** CPU card: "180% = the share of a processor it is using" will puzzle a general viewer; change to "CPU 180% = nearly two processor cores busy". Credit text is about 16 px; make it 1.5x and keep it on screen 3.5 s. Hoist slides off at 2:00 without the wave the director brief asks for; add a two-beat wave on "Now go check on your crew!". The 1.5 s tarmac visual after "his dad" is only about 0.7 s (1:56.5 to 1:57.2); make it a full 1.5 s (time already counted inside the current gap).

16. **SFX.** Momentary loudness shows no clear bump at the whoosh, zip, boing or pop cues; they are effectively inaudible. Raise them about 6 dB in the pauses (keep them under the voice), especially the zip at the start of the Sunday hold and the screech on "Traffic jam", which are doing the job of the pause.

## Pause check summary (MJ addendum)

- Gaps: all 45 between-item gaps are 0.39 s or more; all 10 inside-item comma gaps are 0.39 to 0.43 s. Each is audible as a gap. Rule passes.
- Sound like a person showing: no, for the two reasons in fixes 1 and 2 (fragments end like full stops, questions fall, pauses fall into dead air). The rhythm of gaps is varied enough; the intonation and the silent bed are what make it sound read.
- Named object highlighted before its name: passes for plane, fuel truck, camera truck, CPU, tag, estimate, radio, "that plane"; fails for airfield (fix 3), amber (7), tug (8), tower (9), crew rolling out (7), the jam and the organized board (6), request (4); marginal for baggage (10) and the order (dot, fix 4).

## Keep list (do not break)

- Opening on real game footage with "Howdy!" and the race plane; Hoist in his box.
- The terminal beat: "Running." with the radar ring, "Running what?" with the big "?" and the 0.9 to 1.0 s holds after each.
- Gap lengths as measured (only the trims in the cut list change them).
- Label cards with "= its brain", "= reading files" etc.; the pointer ring pop on plane, fuel truck, camera truck, CPU pill, tag, radio dish.
- The estimate/actual popup coming out of the tag.
- The tower wide shot with the purple briefing arc.
- "Yikes!" / "Traffic jam." with boing and screech and the 0.8 to 1.0 s beats.
- Sunday at 150x with the 1.5 s SFX-only hold; "And that plane right there?" with the ring on the Making-of-video plane before "That's me, making this video."
- "We built a game for a four-year-old. Then we built one for his dad." on the Hoist close-up; card-only credit with music, no narration.
- Loudness -16.2 LUFS; no on-screen "Claude"; no em dashes in on-screen text.

---

# Re-check v7 (cut-v7.mp4, 103.0 s)

Quick re-check of the v6 top 5, the transition frames, SFX audibility and one speech-to-text pass on the full mix. Frames in _qc/v7/.

## Verdict

Not ready to show MJ yet. The picture fixes landed well. The comma fix overshot: the new trimming clips the ends of several words. One line also slipped back to wording the brief forbids. Three fixes remain (below); everything else is minor.

## Top-5 status

1. **Comma and question intonation: partly fixed, with a new defect.** Pitch tracking now shows comma fragments ending between -2.3 and +2.7 semitones of their median (v6: -3.4 to -7.6), and statements still fall. That is the fix. Questions now end at or above the median (i5 +0.3, h9 +0.5, e3 -0.1, d4 -0.6), but they get there by jumping to about 240 Hz, roughly 9 semitones over his 125 Hz base. The clips also got much shorter than in v6: h9 0.94 to 0.53 s, i5 0.93 to 0.53 s, d4 1.41 to 0.88 s, d1 3.08 to 2.42 s, c11 2.51 to 1.95 s. Whisper on the isolated v7 clips hears "and that time", "running white", "and that plane right" (no "there"), "Sunday after fast-forwarded", "Thanks for writing a little partner", and still "afters". The v6 clips of the same lines transcribed correctly. The full mix shows the same: "Sunday after", "plane right", "writing a", "pretty simple".
2. **No dead air: fixed.** silencedetect at -45 dB finds no span over 0.15 s.
3. **Board on "airfield": fixed.** The wide board arrives at 0:13.4 on the word; s1 plays over it with rings on the planes; Sky City follows with moving footage, large cards, and Hoist lifting the card on his forks.
4. **One-job walkthrough: fixed.** REQUEST ticket at the tower (0:54), stick rides the arc dot (0:55.9), radio, then plane (1:02.5) and a push-in on the tag (1:03.5), with the chips lighting in step. The cost popup now matches the tag ($1.40 / $1.52).
5. **Named objects: mostly fixed.** Tug now correct (0:35.4, the blue cart with the terminal icon). The tower pull-out settles before "tower". Amber shows as a pulsing amber ring on the fuel truck (an overlay; the truck's own ground halo stays green). "Organized" now cuts to the tidy board at 1:14.5. Still open: the jam (see R3). The stick also stays on the fuel truck during "out rolls the crew" instead of moving to the carts.

**Transitions:** frame-stepped the TOWER to ORDER card switch (0:56.1) and 1:08: both clean, no blank card. At 1:29.0 the board dips through grey to the close-up over about 3 frames, with no black frame. That's acceptable.

**SFX:** pops, whooshes, zip and slide now sit about 10 dB over the bed; radar (about 20 dB) and boing are clearly audible; the screech is moderate. The strain at about 0:20.2 shows no rise at all, so it is still inaudible.

**Runtime:** 103.0 s. That is inside the brief's 90 to 110 s but under the 105 to 110 s target; R1 and R2 will add about 1 s back, which is fine.

## Remaining fixes (most important first)

R1. **Clipped word endings from the context-trim and bend (i5, h9, e3, d4, d1, c11, h10b; also check t3, t3b, e8, h10, which shrank 0.2 to 0.3 s).** Two fixes:
- **Context cut:** place the cut at the detected onset of the context word, plus 40 ms of tail. Assert that each trimmed fragment is no shorter than its v6 standalone clip minus 0.1 s.
- **Questions:** limit the bend to the last 150 ms and +3 semitones at most, so the stressed word stays near his normal pitch.

Re-synth h10b with a tighter tail. Accept when whisper on every isolated clip matches the script (as v6 did) and question ends stay at or above their median.

R2. **0:39.2 h8 regression: "That number is how hard the computer is working."** The brief says not to say that, and v6-decisions says to name the CPU plainly. Restore "That number is the CPU it's using." and keep the new card text ("nearly two processor cores busy").

R3. **1:05 to 1:14 "Traffic jam" still shows a sparse old board.** Sound off, there is no jam. Use the busy V22b clip (16 agents) under e2 to e5 with carts visibly piling up, and push in on "Traffic jam" with the screech.

## Minor (do if cheap)

- Make the strain SFX audible.
- On "out rolls the crew", sweep the stick to the carts.
- Hoist still slides off without a wave.
- The chip stack at bottom left partly covers the legend lines.
- The plane swaps from shuttle to airliner at 1:28 under "That's me".
- The mix opens with "Howdy" slightly masked (whisper heard "Tao Di"); raise it 2 dB or duck the bed under it.
