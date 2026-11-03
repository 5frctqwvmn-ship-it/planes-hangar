# MISSION BRIEF: PLANES HANGAR (v10 MASTER CUT)
You are an animation director, compositor, and audio engineer. Rebuild the video presentation for "Planes Hangar" using the visual mechanics and pacing of the 1993 Jurassic Park "Mr. DNA" explainer sequence.

---

## 1. CORE DIRECTIVES & SYSTEM FIXES

### Audio & Voice Fixes (Critical)
- **Eliminate Glitched Prefixes & Word Clipping:** Remove all synthetic concatenation and clipping artifacts (e.g., fix "A-howdy" -> clean "Howdy!", "tag-z" -> clean "tag", "helper-s" -> clean "helper", "long-s" -> clean "long").
- **Preserve Natural Decay:** Add +50ms boundary padding around all spoken phrases so word tails are not clipped mid-phoneme by automated splicing.
- **Insert Hard-Coded Timeline Pauses:** Render each dialogue beat as an independent audio chunk. Lay physical silence (0.4s to 0.8s) between chunks on the timeline rather than relying on TTS punctuation.

### Visual Framing & Layout Rules
- **Scene 2 Airfield Flash:** Trim the establishing flash to **4 rows total** (remove 2 rows) and ensure beacons/vehicles are actively animated across the pads.
- **Scene 2 Sandbox Character:** Pad 1 features **Rochelle** (pink/white plane). The high-res game card (1.3 MB) and the low-poly city model (84 KB) must feature Rochelle to match the pad.
- **Scene 4 Framing Fix:** When expanding to multiple planes, ensure **Pads 1, 2, and 3 remain fully framed** inside the camera viewport without cropping Pad 2 on the right edge.
- **Scene 5 Full-Day Living Timelapse:** Clock must run across an extended shift (**3:00 PM to 12:00 AM / Midnight**). Inactive pads must dynamically despawn and collapse the airfield canvas during quiet hours (600x) and respawn during bursts (150x). No static ghost planes.
- **Scene 6 Tarmac Mascot & El Chupacabra:** Mascot breaks out of the lower-third PIP box, rolls onto Pad 1, interviews the tool crew (Camera, Script, QC), and banters directly with **El Chupacabra** before the final sign-off.
- **Scene 7 Outro:** Final credit card appears on screen only. **Do not narrate the credits.**

---

## 2. TIMED SCRIPT & STORYBOARD SPECIFICATIONS

### SCENE 1: The Problem (0:00 – 0:13)
- **Visual:** Kids' 3D airplane game footage -> Cut to terminal screen: `> Running agent... 2h 23m (nothing else)` with a pulsing cursor and a question mark.
- **Audio:**
  [Narrator]: "Howdy! We were building an airplane game for my four-year-old pilot, with help from a crew of AI agents."
  `[0.6s pause]`
  "Trouble is, while they work, this is all you get: Running..."
  `[0.5s pause]`
  "...Running *what?!*"
  `[0.8s pause]`

---

### SCENE 2: The 1-Plane Sandbox & Rochelle Gag (0:13 – 0:48)
- **Visual:** 
  1. Brief 1-second establishing flash of the 4-row active airfield.
  2. Camera immediately isolates and zooms into **Pad 1 with Rochelle** (pink/white plane). All other pads fade out.
  3. Pop up the 1.3 MB high-poly Rochelle model card -> Swap to the 84 KB low-poly model with speech bubbles.
  4. Darken the screen and spotlight each ground vehicle as it is named (Fuel Truck / Amber -> Baggage -> Tug -> Camera -> CPU Badge -> Cost Tag).
- **Audio:**
  [Narrator]: "So we built 'em an airfield of their own, just to watch."
  `[0.5s pause]`
  "Let's start with just one plane—that's one agent on the job."
  `[0.4s pause]`
  "Recognize the plane? It's Rochelle, straight out of my son's game!"
  `[0.2s pause]`
  [Rochelle VO - Full Model]: *"Bonjour! Ready to race!"*
  `[0.2s pause]`
  [Rochelle VO - Low-Poly Model]: *"Mon dieu, I am on a polygon diet!"*
  `[0.4s pause]`
  [Narrator]: "The full-size models got a little heavy for a phone, so we made these light little versions."
  `[0.6s pause]`
  "See that fuel truck? That's its brain, flashing amber while it thinks. And when it calls a tool, out rolls the ground crew!"
  `[0.4s pause]`
  "Baggage reads files. The tug runs commands. And that camera truck films."
  `[0.5s pause]`
  "That number shows how hard the computer is working... and that tag? That's the bill! An estimate up front, and the real cost after—so you learn what things really cost."
  `[0.8s pause]`

---

### SCENE 3: The Radio & Control Tower Flow (0:48 – 1:04)
- **Visual:** Pan up to the Tower and Radio. Animate glowing message path: User Chat -> Radio (Haiku Helper) -> Ops Board -> Orchestrator (Tower). The Tower then dispatches an order glowing down the taxi line.
- **Audio:**
  [Narrator]: "Now, how does everybody know what's happening? Right beside the tower is the Radio—our lightweight Haiku helper. It watches the whole crew and keeps this board up to date, so the director never has to."
  `[0.5s pause]`
  "Up in the tower is the Orchestrator, our director. It plans the work, and shoots each order right down the taxi line."
  `[0.6s pause]`

---

### SCENE 4: Dynamic Expansion & Evolution Montage (1:04 – 1:35)
- **Visual:** 
  1. As the order reaches the taxi line, **Pads 2 and 3 spawn in**. Camera frames all 3 pads cleanly without edge cropping.
  2. Quick evolution sequence: show early text-based layout -> show intermediate messy stage where every tool call got an unorganized cart -> flash *"Yikes! Traffic jam!"* -> snap back to the organized, numbered pad layout.
  3. Mascot delivers the deadpan line with a subtle camera punch-in on his sheepish face.
- **Audio:**
  [Narrator]: "And when more jobs come in—whoa! Look at that, a whole flurry of activity! Watch the airfield stretch out to make room. Good thing you know what you're looking at now!"
  `[0.7s pause]`
  "Now, it didn't start this tidy. At first, it was simple. But as the crew grew, every single action got its own cart... and pretty soon? *Yikes!* Traffic jam."
  `[0.5s pause]`
  "So we gave every crew its own pad and organized the chaos."
  `[0.8s pause]`
  "[Deadpan delivery] Started with planes..."
  `[0.4s pause — camera punch-in on sheepish forklift face]`
  "...ended with planes."
  `[0.8s pause]`

---

### SCENE 5: Full-Day Variable-Speed Timelapse (1:35 – 2:00)
- **Visual:**
  - Clock runs from **3:00 PM to 12:00 AM (Midnight)**.
  - Active bursts scrub at **150x** (pads spawning, trucks swarming, orders flying).
  - Quiet/idle stretches scrub at **600x** (empty pads collapse, clock hands spin quickly).
  - The canvas dynamically shrinks and expands to show a living system.
- **Audio:**
  [Narrator]: "Hold onto your hubcaps! Here's one whole day's work—skipping the quiet hours, and slowing down when the crew gets busy."
  `[2.0s TIMELAPSE MUSIC & FOLEY ONLY — let visual breathe]`
  "You can watch the whole airfield breathe, scaling up and scaling down all day long."
  `[0.8s pause]`

---

### SCENE 6: Tarmac Drop & El Chupacabra Interview (2:00 – 2:40)
- **Visual:**
  1. Mascot leaves the lower-third frame and drives onto Pad 1 ("Making this video").
  2. Parked on Pad 1 is **El Chupacabra** (red racing plane with green cape), surrounded by the Camera Truck, Script Cart, and QC Tug.
  3. Mascot drives up, checks on the tool carts, then turns to banter directly with El Chupacabra.
  4. Mascot turns to camera for the final wrap-up.
- **Audio & Dialogue:**
  [Forklift]: "Let's head down to the tarmac and get a closer look! Hey there! Watch the lens, buddy—that's me, making this video!"
  `[0.4s pause]`
  [Forklift to Script Cart]: "How's that script looking?"
  [Script Cart VO]: "On revision eight, boss!"
  [Forklift to QC Tug]: "And QC?"
  [QC Tug VO]: "Zero overlaps. Clear for takeoff!"
  `[0.4s pause]`
  [Forklift turning to El Chupacabra]: "And how's our star plane holding up?"
  [El Chupacabra VO - Dramatic Luchador]: *"Ah, Señor Forklift! I fly with the passion of ten thousand eagles! ...Just make sure the camera gets my good side, sí?"*
  `[0.5s pause]`
  [Forklift chuckles]: "Keep up the good work, crew!"
  `[0.6s pause]`
  [Forklift to camera]: "We built a game for a four-year-old... and then we ended up building a companion game for his dad as well!"
  `[0.6s pause]`
  "Thanks for riding along, partner. Now go check on your crew!"

---

### SCENE 7: Outro Card (2:40 – 2:43)
- **Visual:** Centered slate card on slate-gray background:
  `Made by MJ and his son,`
  `with an orchestrator and a crew of agents.`
- **Audio:** Upbeat theme music swell. **No spoken voiceover.**

---
## ORCHESTRATOR NOTES (authoritative where they differ)
- Scene 3 visual: the radio's data path is crew activity -> Radio -> Board (the narration is already correct). Do not draw "User Chat -> Radio -> Tower". The tower's order still flies down the taxi line.
- Characters: use the GAME'S OWN plane models and names from its roster (/home/claude/wt/test/index.html). Check whether the roster has a pink/white plane named Rochelle and a red plane with a green cape named El Chupacabra; if a name is not in the roster, use the closest real roster plane and tell the orchestrator the substitution. Character voices: Kokoro French voice (ff_siwis) for the pink plane, Spanish voice (em_alex or ef_dora) for the red one, dramatic delivery, light radio filter so they read as different speakers from Hoist.
- Scene 5: real board history Mon Nov 2 from 3:00 PM to midnight CST exists in /home/claude/radio.log and the board db; use it with true clock times. Replay mode on the current board already removes finished pads and reflows; record from it.
- Voice: keep the standing method (each sentence/list item its own clip; comma phrases synthesized with the next word as context and trimmed at the start of that word plus 50 ms of natural tail; questions level or slightly rising; speech-to-text-matched variants; hard silences on the timeline). The brief's +50 ms boundary padding is the tail rule.
- Length: this script has more words than v8; expect about 3:00 at 135 wpm. Build it as written; MJ decides cuts after seeing it.
