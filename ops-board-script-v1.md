# "A Picture of the Work": the Hangar Ops Board, told backwards
Draft script v1 for MJ's approval (Nov 2). Vertical 1080x1920, about 6 to 7 minutes. Style: a cheerful animated explainer in the spirit of the Jurassic Park DNA sequence: a friendly guide walks you through how it works while pop-up graphics appear as he explains. Narrated aloud (cheapest voice), light music bed. Narrator: HOIST, one of the little forklifts from the game (name open). His lines are spoken (same voice pipeline as the game's planes) and also shown as subtitles in a caption band that never covers the action.

Rules for every scene: the board is always live and moving (real recorded events replayed), never a still. The WHOLE board stays visible at all times (no zoom beyond 1.2x). Every tap is shown: the cursor moves to the item, a ripple marks it, and a small card grows out of that point, leaving the item visible beside it. Hoist sits in a reserved corner and is never covered.

---

## SCENE 1. Title (0:00 to 0:12)
VISUAL: Title card: "A PICTURE OF THE WORK. The Hangar Ops Board." Small line: "Sunday, November 1." A forklift drives into frame from the right, stops, turns its lamp to the camera.
HOIST: "Evening, friend. Name's Hoist. I move boxes for a living. Tonight I'm going to show you the board, and why every little thing on it is there."

## SCENE 2. The objective (0:12 to 0:40)
VISUAL: A plain terminal line: "Running agent... 2h 23m" with a blinking cursor. Nothing else. It sits there. Hoist drives up and taps it with a fork.
HOIST: "Here's the problem. You ask a crew of AI agents to build your game, and this is all you get. Running. For hours. Running what? Reading what? Stuck? Is it burning your whole week's budget on one file? You can't manage what you can't see."
ON SCREEN (one line at a time): "What is each agent doing? · Which tools is it calling? · Is it working or waiting? · What is it costing me?"
HOIST: "So we built a picture of the work. Everything on it answers one of those four questions. Let me show you the finished thing first. Then I'll show you how we got here, because it did not start out looking like this."

## SCENE 2a. Why planes (about 15 s)
VISUAL: Real gameplay of Planes Hangar: the airport start screen, a plane with a face taking off, a race, the ground crew on the apron. Hoist in his panel, pointing.
HOIST: "First, why airplanes? Because the thing this crew is building is a plane game, for a four-year-old pilot. Planes with faces, races, a ground crew. So when we needed a picture of the work, we borrowed the game's own world: an airfield."

## SCENE 2b. Organized chaos (about 10 s)
VISUAL: Wide shot of the ENTIRE finished board with three or four planes on their stands at once, live and moving: beacons spinning, vehicles lit, command arcs coming down from the tower, the dish sending to the cloud, tokens ticking on every tab. HOLD for 10 to 15 seconds with no cuts so the viewer can take it in. No push in.
HOIST: "Ever stood at the window of a busy airport? Trucks everywhere, planes coming and going. Looks like chaos. It isn't. It's organized chaos. Break it down to its parts and it's a symphony: every truck, every light, every line moving in sequence, doing its job. This board is the same. Let's take it one piece at a time."

## SCENE 3. The finished board, the tour (0:40 to 2:30)
VISUAL: The final board (planes version), live replay of a busy stretch of Sunday evening. The camera eases to each item as Hoist names it; a cursor ring taps it and its card opens.
3a. The tower. "That tower is the orchestrator. It never builds anything itself. It briefs the crew, checks the work, and talks to the pilot. The word on the roof is the model it's running. Change the model, the roof changes."
3b. The radio and the cloud. Tap: the dish pulses, dots rise into the cloud. "The radio is the cheapest agent we have. All it does is relay what everybody's doing up to the board every minute. Why a separate agent? Because if the orchestrator did that, you'd pay the expensive model to do a job a cheap one can do. That's the whole trick of this crew: the right size model for each job."
3c. A stand. "Every plane on a stand is one agent at work. Name on the tab, model colour on the ring, and that number is the tokens it's used so far."
3d. The crew around the plane. Tap each vehicle in turn, card opens: "The vehicles are the kinds of work. Fuel truck, that's thinking. Catering, writing. Baggage, reading files. The tug, running commands. Maintenance van, rendering video. The inspection truck, filming the game. Stairs, sending messages. Tap one and you see exactly what it did, newest first."
3e. Beacons and lights. "Beacon on, it's working now. Green light, doing a step. Amber, thinking. Red, stopped. Off, parked. One glance and you know who's busy."
3f. The CPU pill. "Some jobs run for minutes inside one command, like recording the game. The board watches the machine and keeps that vehicle lit, with the CPU it's using."
3g. A command arc. "When the tower briefs an agent, you see it: a pulse down the taxi line with what it said."
3h. The runway. "Finished agents park on the runway. The stations along it are where vehicles drive when they go to work: files, the desk, the camera."
3i. The panels (scroll down). "And the money. Session and week, how fast we're spending, and when we run out at this pace. Which task cost what. The machine. The log. This is how you decide what to build next and what to hold for Monday."
3j. The price tag. Tap the tower, then the radio, then an agent; each card shows "API cost if billed: $X". "One more number. What would this crew cost at the public API prices, if you were paying by the token? The tower, the orchestrator, is the expensive one, because it rereads the whole conversation every time it speaks. The radio costs pennies. That's the cascade: big model to direct, mid-size models to build, the smallest one to keep the lights on." ON SCREEN: the running total by model (real figures from the board).
HOIST: "Four questions. Every piece answers one. Now let me take you back to the beginning."

## SCENE 4. Where it started (2:30 to 2:50)
VISUAL: Wipe to the TRUE first board (recover it from the board artifact version history): planes parked on an airport layout, no tower, no radio, no panels. Live replay of the same events on it.
HOIST: "Version one. Sunday afternoon. Planes for agents, because it's a plane game. That's it. You could see that agents existed. You could not see what they were doing. Watch how far it travels."
ON SCREEN: "V1 of 29"

## SCENE 5. Building the crew (2:50 to 3:30)
VISUAL: Morph through V2 to V8 at about 5 s each, a label on each, a short callout on the big ones.
- V2 Trucks. "First change: the agents became ground crew trucks. The planes are the stars of the game. The crew works on them."
- V3 The tower. "Then the orchestrator got a tower, because the pilot kept asking: who is giving the orders?"
- V4 Live updates. "Then: every agent appears the moment it's started, not when it's done."
- V5 The radio operator. "Then the radio, first drawn as a person. Why? Keeping a board live costs tokens. Give that job to the cheapest model and the expensive one never pays for it."
- V6 The dish. "The person became a dish, because a radio should look like a radio."
- V7 High-detail trucks. "The trucks got rebuilt in full detail. The same models went into the game as the audience. Build it once, use it twice."
- V8 Tower and dish to match. "And the tower and dish were brought up to match. Nothing on the board should look cheaper than the game."

## SCENE 5b. Building the tower and the dish (about 30 s)
VISUAL: Wide board stays on screen; pop-up callouts and insets show the tower and dish as they evolved: the first plain tower block, then the HD tower (glass cab, slanted windows, beacon), the radio as a person, then the dish, then the dish with its cloud. Each piece assembles on screen part by part (shaft, cab, windows, roof, beacon; mount, bowl, feed horn, plate).
HOIST: "The tower is the orchestrator: one director for the whole crew, so it sits highest, where it can see every stand. It started as a box. It got a real glass cab, a beacon that turns, and the model's name on the roof, so you always know which brain is giving orders. The radio started as a little person. A radio operator should look like a radio, so it became a dish. Then it got a cloud, because the board lives in the cloud and that's where the dish is sending."
ON SCREEN: "Tower = the orchestrator · Dish = the cheap relay · Cloud = where the board lives"
NOTE: the board never shows a product name, only "Orchestrator", so anyone can run it with their own agents.

## SCENE 6. Making it readable (3:30 to 4:10)
VISUAL: Morph V9 to V18.
- V9 Model colours and legend. "Colour by model, with a legend. The legend moved to the bottom left because it was covering the tower."
- V10 Declutter. "Labels collapsed to chips. Tap to expand. Overlapping labels hide themselves."
- V11 Status lights. "Green working, amber waiting, grey idle."
- V12 Messages shown. "The tower's orders drawn on the board, plus a log."
- V13 to V15 Usage bars, tokens per agent, effort by task. "Then the money: how much of the week, which job took what."
- V16 CPU rings. "Then the machine: glowing rings for processor load."
- V17 Zoom and phone fit. "It had to fit a phone, because the pilot checks it from the couch."
- V18 The link button. "A button to jump into the game. We took it out again. Pinning the pages worked better. Not every change survives."

## SCENE 7. The hard part: what is it DOING? (4:10 to 5:10)
VISUAL: Morph V19 to V23, this is the heart of the film, slowest pace.
- V19 Walkers. "Here's where it got hard. Fifty tool calls is a number, not a picture. First try: little people carrying each step around."
- V20 Radio moved aside. "The radio moved to a corner. It only updates the board, it shouldn't compete with the workers."
- V21 Flat people. "Then always-visible people, and stations with names."
- V22 Tiny 3D carts. "They didn't match. Flat cutouts next to 3D trucks. So, carts, built the same way as everything else."
- V23 Icons, beacons, lights, arcs. THE UNLOCK, hold longer, callouts with arrows: "This is the one. Separate the agent from the work it spawns. An icon on every cart says what kind of work. A beacon says it's working now. Lights say how. Arcs show the orders coming down. For the first time you could look at this and say: that agent is reading, that one is filming, that one is waiting on the model."

## SCENE 8. Finding the layout (5:10 to 5:50)
VISUAL: Morph V24 to V28.
- V24 Round pads. "Still couldn't tell whose carts were whose. So: pads. Each actor on its own circle, crew around it."
- V25 Tower to the top. "The orchestrator took too much room, and it stopped looking like an airport. The tower went to the top middle, small, and the agents got the space."
- V26 The airfield. "Then a real control tower, stands with numbers, taxi lines, a runway. "Orchestrator" lettered on the tower, the model on the roof. The radio sends to a cloud, because that's where the board lives."
- V27 On the pads list moved up. "Small one: the list of who's working moved under the controls."
- V28 Tokens and the forecast. "Every actor and every cart shows its tokens. And the board tells you when you run out at this pace."
- V28b The price tag. "Then tokens became dollars: what each agent would cost at public API prices, by model, so you can see what the cascade saves."

## SCENE 9. Back to planes (5:50 to 6:20)
VISUAL: Morph to V29, the final board. Camera pulls back to the whole airfield, busy.
HOIST: "And the last change took it home. The agents became the planes again, the game's own planes, one each. And the crew? Us. Fuel, catering, baggage, the tug, the stairs. Servicing a plane the way a real turnaround works. It started with planes. It ends with planes, with a crew you can watch."
ON SCREEN: "V29 of 29"

## SCENE 10. The whole day (6:20 to 6:50)
VISUAL: The final board replays Sunday from 4:24 PM to midnight, dead air removed, a clock in the corner. Finished builds pop up as they land: Angel, Ozzie, the airport, the ground crew, the ships, the board itself.
HOIST: "One Sunday. Thirty-some agents, three at a time, three sizes of model, and one pilot on the couch asking 'what is it doing?' twenty-nine times until he could see it."
ON SCREEN at the end of the replay: "At public API prices: $X total (Opus $a, Sonnet $b, Haiku $c, Fable $d)" using the board's real running total.

## SCENE 10b. "That's me" (the meta beat, about 40 s)
VISUAL: The live board, recorded while THIS film was being made (Nov 2). Camera eases onto the video agent's plane on its stand. A cursor ring taps it; its card opens: "Making-of film, Sonnet".
HOIST: "See that plane right there? That's this film. That's the agent making the video you're watching right now. Let's watch what it does."
VISUAL: Sped-up replay of the video agent's real steps (from its recorded acts), each vehicle lighting in turn, with a small card for each step as it happens:
- Reader (baggage) opens the script: "Reading ops-board-script-v1.md"
- Reader again: the storyboard sheet and the board's saved versions
- Camera operator (inspection truck): "Filming the board in the test browser" (CPU pill 180%)
- Painter (maintenance van): "Drawing frames: captions, callouts"
- Projectionist: "Encoding video s05_versions"
- Writer (catering): "Writing the cut list"
- Archivist (forklift): "Saving work to git"
- Messenger (stairs): "Reporting back to the tower"
Small token and cost counters tick up on the plane's tab as it goes.
HOIST: "Script. Storyboard. Every old version of the board. A camera, a painter, a projector, a filing clerk. Every one of them is a tool call, and every one of them is on the board. That's the whole point. You asked a crew to make something, and now you can watch them do it."
ON SCREEN: "This film: N tool calls, X tokens, $Y at API prices" (real numbers from the board when the cut is final).

## SCENE 11. Close (about 25 s)
VISUAL: Zoom in on Hoist, full face, looking at the camera. A thought bubble pops up with a tiny plane-graph of the week's spend, then pops away.
HOIST: "So that's the board. It started as plain curiosity: what is going on under the hood when I ask a crew of agents to build something? Then it turned into an ops tool. It shows where the money goes, keeps the crew honest, and helps the pilot spend his time and his agents where they count. Thanks for riding along. Now go check on your crew. Bye!"
VISUAL: Hoist waves a fork. Cut to a large, readable credit: "Made by MJ and his son, with an orchestrator and a crew of agents."

## SCENE 11 (old). Close (6:50 to 7:05)
VISUAL: Brass card: "Every piece on this board is there because something was hard to see." Then: "Made by MJ and his son, with an orchestrator and a crew of agents." Hoist backs out of frame, lamp off.
HOIST: "That's the board. Now go check on your crew."

---
Open questions for MJ:
1. Narrator name and voice (Hoist? a different forklift name?). Male/female, warm or wry?
2. Length: this is about 7 minutes. Cut scenes 5 and 6 to half to land near 5 minutes?
3. Spoken narration plus subtitles, or subtitles only with music?
4. Any change to the four questions in scene 2? They are the spine of the film.
