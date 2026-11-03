# MISSION BRIEF: PLANES HANGAR (v10 FINAL PRODUCTION MASTER)
You are an animation director, compositor, and audio engineer. Rebuild the video presentation for "Planes Hangar" using the visual storytelling, character immersion, and comedic timing of the 1993 Jurassic Park "Mr. DNA" explainer sequence.

---

## 1. AUDIO, TTS & TIMELINE DIRECTIVES (CRITICAL)

- **Eliminate Glitched Prefixes & Terminal Suffix Buzzing:**
  - Fix clipped starting syllables (e.g., change glitched "A-howdy" at 0:00 to a crisp, friendly "Howdy!").
  - Remove all trailing unnatural "z" or buzzing sounds on word endings (e.g., "tag-z" at 0:52, "helper-s" at 1:08, "long-s" at 2:09).
  - Eliminate mid-word phonetic drops (e.g., "making-of" clipping at 2:20) and trailing glottal artifacts (e.g., "a crew-uh" at 2:32).
- **Enforce +50ms Tail Decay on All Audio Clips:**
  - Add at least +50ms of clean padding to every audio chunk so automated timeline slicing never cuts off natural phonetic decay.
- **Physical Timeline Pausing (No Rushing):**
  - Render every dialogue beat as an independent audio chunk.
  - Insert physical gaps of silence (0.4s to 0.8s) between lines on the timeline so animations, callout cards, and comedic reactions land before the next sentence begins.
- **Deadpan Tone on "Started with planes...":**
  - Deliver *"Started with planes..."* in a slow, deadpan tone -> 0.5s pause with camera zoom on the forklift mascot's sheepish face -> deliver *"...ended with planes."*

---

## 2. SCENE-BY-SCENE VISUAL & ANIMATION DIRECTIVES

### SCENE 1: The Problem (0:00 – 0:13)
- **Visual:** Action clip from the 3D kids' airplane game -> Cut to dark terminal window showing only: `> Running agent... 2h 23m (nothing else)` with a pulsing cursor and an animated question mark.

### SCENE 2: The Airfield Reveal & 1-Plane Sandbox (0:13 – 0:50)
- **Airfield Flash (0:13 – 0:18):**
  - Establish with a tighter, highly active airfield: **4 rows maximum (remove 2 rows from the 6-row layout)**.
  - Show animated light beacons and moving ground vehicles across the pads so it feels active and chaotic without being oversized.
- **Isolate Single Plane (0:18 – 0:50):**
  - Immediately zoom in and isolate **Pad 1 with Rochelle** (pink/white plane). All other pads fade to dark.
- **Character Continuity (Rochelle):**
  - Both the preview card and the pad must show **Rochelle**.
  - Show the 1.3 MB high-poly game model card with her in-game dialogue popup:
    - *Full Model:* *"Bonjour, mon ami! Ready to race!"*
  - Swap to the 84 KB low-poly City Model with a self-aware quip:
    - *Low-Poly Model:* *"Mon dieu, I am on a polygon diet!"*
- **Ground Crew Spotlights:**
  - Maintain the darkened screen and yellow spotlighting on each ground vehicle as it is introduced: Fuel Truck (flashing amber brain) -> Baggage Cart (reading files) -> Tug (running commands) -> Camera Truck (filming) -> CPU Badge -> Cost Tag.

### SCENE 3: The Radio & Control Tower Flow (0:50 – 1:06)
- **Visual:** Pan up to the Tower and Radio. Animate the complete message routing:
  1. User Chat message pings the **Radio** (Haiku helper).
  2. Radio updates the **Ops Board** and forwards data to the **Control Tower (Orchestrator)**.
  3. The Tower dispatches work orders glowing straight down the taxi line.

### SCENE 4: Dynamic Field Expansion & Evolution Story (1:06 – 1:40)
- **Camera Viewport Fix:**
  - When the new order arrives and new pads spawn, **keep the camera framed wide enough to show Pads 1, 2, and 3 simultaneously**. Do not crop out Pad 2 on the right edge.
- **The Evolution Montage:**
  - Show a clear visual progression of how the dashboard evolved away from its original goal as complexity grew:
    1. *Generation 1:* Simple planes sitting on plain grass.
    2. *Generation 2:* Adding towers, trucks, and metrics.
    3. *Generation 3 (The Breakdown):* Every individual tool call getting its own unorganized cart, turning the screen into an overwhelming traffic jam (*"Yikes!"*).
    4. *Generation 4 (Current Solution):* Organizing the chaos by giving every plane/agent its own dedicated pad and ground crew.
- **The Deadpan Punchline:**
  - Camera zooms in slightly on the forklift mascot's embarrassed expression:
    *"Started with planes... [pause] ...ended with planes."*

### SCENE 5: Full-Day Living & Breathing Timelapse (1:40 – 2:05)
- **Time Window & Canvas Scaling:**
  - The clock in the top corner must cover an entire workday shift: **3:00 PM to 12:00 AM (Midnight)**.
  - The airfield canvas and terminal layout must physically expand with pads during active bursts and collapse/shrink during quiet lulls.
  - **Do not hide the "Making-of video" Pad** during the timelapse—keep it visible on the tarmac.
  - Remove idle ghost planes; pads must actively spawn and despawn based on workload.
- **Variable-Speed Badges:**
  - Display `600x QUIET` during idle lulls (clock spins rapidly, empty pads collapse).
  - Display `150x BUSY` during active bursts (swarms of carts, flashing amber beacons, orders flying).

### SCENE 6: Tarmac Drop & El Chupacabra Interview (2:05 – 2:45)
- **Perspective Shift:**
  - The forklift mascot breaks out of the lower-third picture-in-picture frame and rolls directly onto the runway tarmac.
- **Pad 1 Setup:**
  - Parked on Pad 1 ("Making this video") is **El Chupacabra** (red racing plane with green cape), surrounded by the Camera Truck, Script Cart, and QC Tug.
- **The Crew & Plane Interview:**
  - Mascot drives up to the Camera Truck, checks in with the Script Cart, checks in with the QC Tug, and turns directly to El Chupacabra for a character exchange before addressing the viewer.
- **Sign-off Line:**
  - Mascot delivers the closing line to camera: *"We built a game for a four-year-old... and then we ended up building a companion game for his dad as well!"*

### SCENE 7: Outro Title Card (2:45 – 2:48)
- **Visual:** Clean centered text on slate background:
  `Made by MJ and his son,`
  `with an orchestrator and a crew of agents.`
- **Audio:** 3 seconds of upbeat theme music swell. **No spoken voiceover.**

---

## 3. MASTER SCRIPT & DIALOGUE TIMINGS

```text
[SCENE 1: THE PROBLEM]
Howdy! We were building an airplane game for my four-year-old pilot, with help from a crew of AI agents.
[0.6s pause]
Trouble is, while they work, this is all you get: Running...
[0.5s pause]
...Running what?!
[0.8s pause]

[SCENE 2: THE 1-PLANE SANDBOX & ROCHELLE]
So we built 'em an airfield of their own, just to watch.
[0.5s pause]
Let's start with just one plane—that's one agent on the job.
[0.4s pause]
Recognize the plane? It's Rochelle, straight out of my son's game!
[0.2s pause]
[Rochelle VO - Full Model]: "Bonjour! Ready to race!"
[0.2s pause]
[Rochelle VO - Low-Poly Model]: "Mon dieu, I am on a polygon diet!"
[0.4s pause]
The full-size models got a little heavy for a phone, so we made these light little versions.
[0.6s pause]
See that fuel truck? That's its brain, flashing amber while it thinks.
[0.4s pause]
And when it calls a tool, out rolls the ground crew!
[0.4s pause]
Baggage reads files. The tug runs commands. And that camera truck films.
[0.5s pause]
That number shows how hard the computer is working... and that tag? That's the bill!
[0.4s pause]
An estimate up front, and the real cost after—so you learn what things really cost.
[0.8s pause]

[SCENE 3: THE RADIO & TOWER]
Now, how does everybody know what's happening?
[0.4s pause]
Right beside the tower is the Radio: our lightweight Haiku helper. It watches the whole crew and keeps this board up to date, so the director never has to.
[0.5s pause]
Up in the tower is the Orchestrator, our director. It plans the work, and shoots each order right down the taxi line.
[0.7s pause]

[SCENE 4: FIELD GROWS & EVOLUTION]
And when more jobs come in—whoa! Look at that, a whole flurry of activity! Watch the airfield stretch out to make room. Good thing you know what you're looking at now!
[0.7s pause]
Now, it didn't start this tidy. At first, it was simple. But as the crew grew, every single action got its own cart, moving further away from what we wanted to see... and pretty soon?
[0.4s pause]
Yikes! Traffic jam.
[0.5s pause]
So we gave every crew its own pad and organized the chaos.
[0.8s pause, deadpan voice]
Started with planes...
[0.5s pause, zoom on sheepish forklift face]
...ended with planes.
[0.8s pause]

[SCENE 5: FULL-DAY TIMELAPSE]
Hold onto your hubcaps! Here's one whole day's work—skipping the quiet hours, and slowing down when the crew gets busy.
[2.0s music & sfx only — clock scrubs 3:00 PM to 12:00 AM, canvas dynamically expands and contracts, Making-of pad remains active]
You can watch the whole airfield breathe, scaling up and scaling down all day long.
[0.8s pause]

[SCENE 6: TARMAC INTERVIEW & EL CHUPACABRA]
Let's head down to the tarmac and get a closer look!
[0.4s pause]
Hey there! Watch the lens, buddy—that's me, making this video!
[0.4s pause]
[Forklift to Script Cart]: "How's that script looking?"
[Script Cart VO]: "On revision eight, boss!"
[Forklift to Camera Truck]: "Got the angles locked?"
[Camera Truck VO]: "Framed and rolling!"
[Forklift to QC Tug]: "And QC?"
[QC Tug VO]: "Zero overlaps. Clear for takeoff!"
[0.4s pause]
[Forklift to El Chupacabra]: "And how's our star plane holding up?"
[El Chupacabra VO - Dramatic Luchador]: "Ah, Señor Forklift! I fly with the passion of ten thousand eagles! ...Just make sure the camera gets my good side, sí?"
[0.5s pause]
[Forklift chuckles]: "Keep up the good work, crew!"
[0.6s pause]
[Forklift turns to camera]: "We built a game for a four-year-old... and then we ended up building a companion game for his dad as well!"
[0.6s pause]
"Thanks for riding along, partner. Now go check on your crew!"

[SCENE 7: OUTRO CARD]
[Visual slate only — No spoken voiceover]
"Made by MJ and his son, with an orchestrator and a crew of agents."

---
## ORCHESTRATOR NOTES (authoritative where they differ; supersedes v10-master-brief.md)
1. Radio path (Scene 3 visual): the radio does not take chat messages or forward to the tower. Draw crew activity -> Radio -> Board. The tower's orders still fly down the taxi line. The narration already says this correctly.
2. Pad numbering: Scene 2 puts Rochelle on Pad 1 and Scene 6 says Pad 1 is "Making this video" with El Chupacabra. Keep Rochelle on Pad 1 for the sandbox; in Scene 6 the "Making this video" stand (whatever its number) holds El Chupacabra, clearly labelled. Do not show two different planes on the same pad.
3. Rochelle's line: the script says "Bonjour! Ready to race!"; the visual section says "Bonjour, mon ami! Ready to race!". Use the script line.
4. Generation 1 (planes on plain grass) was never saved; recreate it honestly and label it "recreated", as before.
5. "One whole day ... all day long": the clock runs 3:00 PM to midnight (real Monday history). Keep MJ's words; the clock shows the true times.
6. Sheepish face: Hoist needs a new embarrassed expression (eyes glancing aside, small mouth, a slight blush or sweat drop) for the deadpan punch-in.
7. Keep every v10 fix (Hoist parked clear with a shadow, the camera truck turn, short pointer, one clock, sparse SFX, no review timecode, wave on exit).
