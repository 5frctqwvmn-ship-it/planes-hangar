# PRODUCTION SPECIFICATION: PLANES HANGAR (V8)
# Style Reference: 1993 Jurassic Park "Mr. DNA" (Cel Host / Live-System Interaction)

## 1. VISUAL STAGING DIRECTIVES

### Beat A: The Hook (0:00 – 0:12)
- Split: Top shows the 3D kids' airplane game racing; cut to black screen with terminal text: `Running agent...`
- Forklift in bottom PiP box.
- VO: "Howdy! We were building an airplane game for my four-year-old pilot, with help from a crew of AI agents. While they work, this is all you get: 'Running...' Running what?!"

### Beat B: 1-Plane Sandbox Tutorial (0:12 – 0:38)
- Visual Rule: Cut to the airfield. Flash the wide board for 1 second, then immediately crop/isolate PAD 1 ONLY (hide pads 2 and 3 and all extraneous lines).
- Sequence of highlights:
  1. Highlight the plane on Pad 1: "So we built 'em an airfield of their own, just to watch. Every plane out here is one agent on the job."
  2. Swap/compare model: "Every plane comes straight from my son's game. The full-size ones got a little heavy for a phone, so we built these light little versions."
  3. Fuel truck zooms & flashes amber: "See that fuel truck? That's its brain. Flashes amber while it thinks..."
  4. Ground crew deploys (Baggage / Tug / Camera): "...and when it calls a tool, out rolls the crew! Baggage reads files. The tug runs commands. And the camera truck films."
  5. CPU meter & Cost tag illuminate: "That number tracks how hard its computer is working... and that tag? That's the bill. An estimate up front, and the real cost after. So you learn what things really cost."

### Beat C: The Radio & Tower Dispatch (0:38 – 0:52)
- Pan up to the Tower and Radio.
- Show message pulse: Chat/Ops -> Radio icon -> Tower.
- Show order beam firing down the taxi line:
  "Up top in the tower is the director. And right beside it is the Radio: our cheap little Haiku messenger that carries word from the chat to the board and up to the tower. The director plans the work and shoots each order right down the taxi line."

### Beat D: Spawning & Dynamic Map Expansion (0:52 – 1:08)
- As orders hit the tarmac, spawn Pad 2 and Pad 3. The camera zooms out as the map dynamically widens to accommodate the new planes.
- VO: "And when more jobs come in—whoa! Look at that, a whole flurry of activity! Watch the airfield stretch out to make room. Good thing you know what you're looking at now!"
- History gag: Flash the old chaotic all-carts overlay for 1.5 seconds on "Yikes!", then snap back to clean pads.
- VO: "Now, it didn't start this tidy. Every little action got its own cart, and pretty soon? Yikes! Traffic jam. So we gave every crew its own pad and organized the chaos. Started with planes... ended with planes."

### Beat E: Adaptive Full-Day Timelapse (1:08 – 1:22)
- Full airfield view with an on-screen clock widget (e.g., `8:00 AM -> 6:00 PM`) and speed indicator.
- Playback logic:
  - Idle/quiet stretches run at 600× (clock spins rapidly).
  - Busy multi-agent sprints run at 150× (swarming trucks, spawning pads).
- VO: "Hold onto your hubcaps! Here's a full day's work—zipping past the quiet hours, and slowing down when the crew gets busy. You can watch the whole airfield breathe—scaling up, scaling down, all day long."

### Beat F: The On-Field Ground Crew Interview (1:22 – 1:44)
- PERSPECTIVE SHIFT: The forklift says: "Let's head down to the tarmac and get a closer look!"
- The PiP frame disappears. The forklift drives directly onto the 3D tarmac beside the video-making plane.
- The camera truck turns toward him.
- Dialogue & Banter:
  - Forklift: "Hey there! See that camera truck? Careful, don't get too close to the lens—that's me making this video!"
  - Forklift (turns to Script Truck): "What're you working on over here?"
  - Worker Bubble: [Chewing through v8 script revisions!]
  - Forklift (turns to QC Tug): "And you?"
  - Worker Bubble: [Checking camera angles and fixing overlapping nodes!]
  - Forklift: "Lookin' sharp, fellas. I'll let you get back to work!"

### Beat G: Wrap-Up & Sign-Off (1:44 – 1:55)
- Camera pulls back to full hangar view as forklift waves.
- VO: "We built a game for a four-year-old... and then we built one for his dad. Thanks for riding along, partner. Now go check on your crew!"
- Final Card: Silent display of "Made by MJ and his son, with an orchestrator and a crew of agents." (Music swell, NO voiceover).

---

## 2. AUDIO & TTS GENERATION CONSTRAINTS
- Split voice generation into 7 separate audio files (Beats A through G). Do not generate in a single pass.
- Insert explicit silence (0.6s to 1.0s) between major visual transitions.
- Match speaking rate to a conversational, relaxed drawl (~130–140 WPM).
---
## ORCHESTRATOR NOTES (accuracy fixes, keep MJ's intent)
- Beat C radio line: the radio does NOT carry word from the chat to the tower. What it really does: it watches every agent and keeps the board up to date, so the director never has to. Use: "And right beside it is the Radio: our cheap little Haiku helper that watches the whole crew and keeps this board up to date, so the director never has to." Message pulse visual: from a plane's crew to the radio dish to the board (not chat to tower). The tower's orders still fly down the taxi line.
- Beat B CPU line: MJ's v8 wording ("That number tracks how hard its computer is working") is the current direction and supersedes the earlier "CPU it's using".
- Beat E: recorded board history only exists from Sunday Nov 1 4:24 PM onward. Use the busiest real stretch with the clock widget showing the real times (e.g. Mon Nov 2 3:00 PM to midnight), adaptive speed 600x idle / 150x busy. Do not label it 8 AM to 6 PM.
- Keep the standing voice rules: each sentence and list item its own clip, comma phrases synthesized with the next word as context and trimmed by the speech-to-text-matched variant method, questions end level or slightly rising (max +3 semitones over the last 150 ms), real silences in the edit, speech-to-text check on every clip. 7 chunks (Beats A to G), 130 to 140 words per minute.
