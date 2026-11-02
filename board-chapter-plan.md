# Ops board chapter: plan approved by MJ (Nov 1, 10:31 PM)

Goal: show the PROGRESS. Every one of the 27 changes below appears on screen, in order, as live moving footage of that version (never a still screenshot), about 5 seconds each so the caption can be read. Morph between versions (old layout slides and dissolves into the new one, like the live board reorganizing). Label each: "Change 7 of 27: high-detail trucks". Major changes (marked BIG) get a short pause, a slightly longer hold, and an arrow/circle callout saying what changed and WHY.

Sources: archive/board-versions/ (v2 to v7 final, tonight), the board artifact's 26 published versions (history), git, older video scenes (s03_crew, s03_crew2, s03b_board, s3_board), raw/b3r frames, live-events. If a version cannot be recovered, recreate it honestly from the closest saved one and caption it "recreated", or skip and say so; never fake.

## Afternoon: building the board
1. BIG First version: planes as the agents.
2. BIG Planes become blocky ground-crew trucks.
3. BIG Control tower added for the orchestrator (Claude).
4. Real-time updates: every agent start logged the moment it happens.
5. BIG Radio operator added (first as a person). Why: a cheap Haiku agent relays updates so the board stays live without spending the orchestrator's time.
6. Radio becomes a satellite dish.
7. BIG High-detail trucks, the same models as the game's audience (dual use).
8. Tower and dish brought to the same detail.
9. Model colours and legend; legend moved from top to bottom left.
10. Declutter: short chips, tap to expand, overlapping labels hide.
11. Status lights: green working, amber waiting, grey idle.
12. Claude's messages to each agent shown, plus the radio log.
13. Weekly and session usage bars with % used, % left, reset times.
14. Each agent's tokens, estimate and share of the week.
15. Effort by task, totals panel, model-weighted usage.
16. BIG CPU and machine gauges as glowing bay rings plus Machine panel. Why: see where compute goes.
17. Zoom and Fit, phone fit.
18. Link button added, then removed in favour of pinning.

## Tonight: making it readable
19. Work-crew ring and walkers carrying each step.
20. Radio to top left, barn top right; radio quieter.
21. Always-visible flat people, station labels, radio name tag.
22. Tiny 3D carts; model colour only on tags.
23. BIG THE UNLOCK: agents separated from their sub-processes. Icons on carts, beacons, green/amber/red lights, command arcs from the tower, 5 bays. Why: see what an agent does when it spins up, which tool calls, when it is working vs idle. Most screen time.
24. Round pads, carts circling their owner, labels built into tower and dish, hangar removed.
25. Tower and radio into a top strip, agents get the space, airfield markings, desktop fills frame.
26. BIG Final airfield: real control tower ("CLAUDE" up the shaft, model on the roof), "HAIKU" dish with cloud uplink, CPU-driven carts for long jobs, one-line legend. Everything visible, it feels alive.
27. "On the pads now" moved up under the controls.

Then: the dashboard tour on the final board (CPU, limits, totals, log, effort by task: "so we can see where our usage goes and make better decisions"), then the whole day in one take on the final board.

## Added 11:03 PM (MJ)
28. BIG Token counts on every actor and cart, CPU readings capped correctly, run-out forecast under the usage bars.
29. BIG The ending: back to planes. Each agent becomes one of the game's own high-detail planes on its stand, serviced by the game's ground-crew vehicles (fuel = thinking, catering = writing, baggage = reading, tug = commands, maintenance = rendering, inspection = filming, stairs = messages). Callout: "It started with planes. It ends with planes, now with a crew you can watch." The board chapter and the whole-day replay must END on this version; if it is not built yet when you reach the board chapter, render everything else and leave the final beat as a slot to drop in.
