# Hangar Ops Board: hands-on QA (read-only pass)

Tested: /home/claude/wt-out/board-index.html, Playwright chromium, phone 390x844 (touch) and desktop 1280x800 (mouse), events from /home/claude/radio.log merged with the base feed. Clock pinned to Nov 2 9:59 PM local, so cutv5, replayfix and tester are on pads; director, cutv4, proofv3 were made active for the 5-6 agent run.
Harness caveats: radio.log has no spawn/report events, so I synthesised spawn (est 3M tokens) and report events for agents that only had acts. Anything about estimate values being the same ("~3.00M est.") is my data, not a bug. Chromium here uses software GL, so real frame rate cannot be measured (about 0.4 to 1 s per frame); I report draw calls and triangles instead. The served file has no `<meta name="viewport">`; with isMobile emulation the page lays out at 980 px wide and shrinks to 40%. I assumed the artifact wrapper injects it and tested with a real 390 px layout viewport. Console: no page errors, only GL driver "GPU stall due to ReadPixels" warnings.
Screenshots: /home/claude/wt-out/qa-shots/handson/

## Bugs, most serious first

1. Percent of week disagrees between card and lists for the same agent (phone and desktop).
   Repro: tap the cutv5 plane, read "5.2M weighted tokens, about 0.39% of week". Compare "ON THE PADS NOW" and "Effort by task" for cutv5: "0.64% of week". Same for the radio operator: card 0.34%, Effort list 1.67% (5x).
   Expected: one number everywhere. Actual: lists use raw tokens / perPct, cards apply the model weight (Sonnet 0.6, Haiku 0.2). Effort rows also sum to 14.1% while the weekly gauge says 95.6% used, with no note that rows are unweighted.
   Shots: ph-card-cutv5.png, ph-card-radio.png

2. Token totals disagree and are not labelled: tile "Tokens used 112.44M" (equals the sum of Effort rows) vs "Totals ... 342.86M tokens" vs the orchestrator card "17.81M tokens / 18.3M weighted".
   Repro: scroll below the stage on either size.
   Expected: either the same figure or a visible label saying what each one counts (reported vs incl. cache reads). Actual: three unexplained numbers. Also "weighted tokens" is larger than "tokens" on the Sonnet card (5.2M vs 5.10M), which reads backwards.

3. Agent cards cover the thing you tapped on a phone (390x844).
   Repro: scroll to the stage, tap the cutv5 or replayfix plane. Card is 250 px wide x 412-429 px tall on a 342 x 559 stage, and it sits over the plane (and most of the apron). Tapping another plane while it is open (cutv5 then tester) leaves cutv5 selected because the card is on top of tester; you must close first.
   Expected: card anchored beside/below the target or a bottom sheet that leaves the plane visible. Actual: card covers target.
   Related: on first load the stage starts at y=601 (below the fold). Tapping a plane in the visible top part opens a card that extends to y=1151, off screen, with no scroll-into-view.
   Shots: ph-card-cutv5.png, ph-card-replayfix.png (first run, before scroll fix, shows the off-screen case: base-ph.png shows the fold)

4. CPU % chips cover agent name labels when 5-6 agents are parked (phone).
   Repro: 6 agents on pads, phone. Chips "7%" and "108%" sit over "proofv3 task" so it reads "proofv...k"; "75%" sits on the pad 4/5 edge. With 3 agents the chips just touch each other and the dashed lane. Desktop: the "Filming, 65 s" pill overlaps the "75%" chip (24x5 px) and sits on top of the radio dish / tower base.
   Expected: no label hides another name. Shots: ph-5agents.png, dt-stage.png

5. Touch cannot pan the 3D view when zoomed in (phone).
   Repro: tap "+" until the apron is bigger than the stage (ZOOM below 1), drag with a finger. PAN stays 0,0. Code only starts panning for pointerType "mouse". On desktop, mouse drag works. Zoomed in on a phone you cannot reach the left/right pads. (No pinch zoom either.)
   Shot: ph-zoomin.png (zoomed, nothing to pan with)

6. Stale usage numbers with a passed reset and a wrong-sounding forecast.
   Repro: load with the last usage reading older than its reset (resets Mon 3:00 PM, session "resets Mon 3:40 AM", both already past at 9:59 PM Mon). Panel still shows "95.6% used, 4.4% left, At this pace you run out after the reset", and session "0.0% used, 100% left, resets Mon 3:40 AM". Session shows "reset; send a new reading" but the weekly gauge shows no stale hint at all, so a red "run out" warning is shown for a week that already reset.
   Expected: mark the reading as stale or hide the forecast once resetAt has passed. Shot: base-ph.png

7. Tap outside does not close the card when the tap is outside the stage (both sizes).
   Repro: open any plane card, scroll or tap the page header or any panel. Card stays (SEL still set). X, Esc and tapping empty apron do close it. Only the stage has a click handler.

8. The word "claude" still appears: Machine details table (tap the Machine panel) lists owner "claude" and process "claude" (lowercase). Expected "Orchestrator". Everywhere else it correctly says Orchestrator.
   Shot: ph-machine-expanded.png

9. Replay timeline is hard to use for "today". Replay starts at the first event of the feed (Oct 31 8:38 PM), the slider spans about 50 hours, so a 5% slider step is about 2.5 hours and today's evening is the last 10 percent of the track. Replay at 600x takes about 5 minutes to reach today. Log rows show only a clock time (no date): at Nov 2 11:52 AM the top log row reads "11:34 PM" (that is Nov 1), confusing. The "Estimates vs actual today" line is shown while scrubbing Nov 1 and says "today" with changing numbers; at Nov 2 11:52 AM it shows "actual $0.00". Reload while in replay silently returns to Live (replay position not kept).
   Shots: ph-scrub-0.5.png, ph-scrub-0.8.png

10. Small touch targets and label/prop overlaps on phone. CPU chips are 19x13 px and 30x13, agent chips 22x22 px (tappable, below 44 px). Prop tags (Desk, Camera, Screen) overlap the parked planes on the runway strip and the "09" marker; the tower roof sign ("OPUS 18.3M $83.19") is unreadable at phone size and the beacon rotor crosses it. Vehicle live-status pills ("Working, 53 s") are hidden on phone widths below 420 px so the active-tool timer is only in the list.
    Shots: ph-stage-live.png, ph-5agents.png

11. Performance risk (not measurable here): 3 agents = 562 draw calls / 236k triangles / 504 geometries; 6 agents = 773 to 797 draw calls / 333k triangles. That is high for a phone GPU; expect low frame rates on older iPhones with 5+ agents. Suggest instancing or LOD for crew vehicles and fewer draw calls per agent.

12. "Effort by task" lists all 46 agents from every day (page is about 2,300 px of rows on phone, no inner scroll) while its summary says "today"; many rows say "est n/a". The page becomes very long on phone. The Radio operator shows $6.37 actual against est $4.56 while "running" for 1748 min.

## What works well
- No horizontal overflow at 390 px; no DOM label overlaps detected with 3 agents; no console errors.
- Every plane (3 on pads, 6 finished, tower, radio) and all 17 crew carts opened the right card on both sizes when tapped at their live position; Esc and the X close every card; tapping empty apron closes.
- Finished agents leave the stands and park on the runway strip; ON THE PADS tile, pads on screen and the list always agree (3 and 6 in my runs, 2 or 1 while scrubbing), and FINISHED + pads + stopped = AGENTS RUN.
- Effort row tokens sum exactly to the Tokens tile (112.44M); Machine CPU 99% agrees with 108% + 75% + 7% of 2 cores.
- Zoom +/-/Fit and desktop drag-pan and wheel zoom work; zoom persists across reload.
- Live, Replay, Pause/Play, speed (60x, 600x, 3000x) and scrubbing behave, paused time holds, finished agents appear and disappear sensibly while scrubbing, log panel scrolls internally.
- Orchestrator wording is applied to names, log and cards.
