# Section-by-section workflow (MJ, Nov 3 4:27 PM)
The film is split into 5 sections. Each one is built and approved separately as a cheap preview. After MJ approves all five, they are stitched and rendered once in HD.

## Sections (script lines from v10-final-master.md MASTER SCRIPT)
- s1-intro: Scene 1 plus the start of Scene 2, from "Howdy!" through "...so we made these light little versions." That covers the crowded game race, the terminal, the airfield flash (4 rows), the isolation on Pad 1 with Rochelle, and Rochelle's talking-face cards. This agent also delivers El Chupacabra's talking-face clip for s5.
- s2-crew-tower: from "See that fuel truck?" through the end of Scene 3 ("...right down the taxi line."). Crew spotlights, CPU number, cost tag and estimate vs actual, then the Radio and Tower flow (crew -> Radio -> Board; orders fly from the Tower down the taxi line).
- s3-evolution: Scene 4. More jobs arrive, the field stretches with Pads 1 to 3 in frame, "Bigger job, bigger plane", the four-generation montage, "Yikes! Traffic jam", the pads, and the deadpan look to camera.
- s4-timelapse: Scene 5. 3 PM to 12:00 AM time-lapse, 600x QUIET / 150x BUSY badges, the field growing and shrinking, the Making-of stand always visible.
- s5-tarmac: Scene 6 and Scene 7. Hoist drops onto the tarmac, interviews the script cart, camera truck and QC tug, then El Chupacabra (talking-face card from s1), the Beluga aside, the sign-off, the wave, and the silent credit card.

## Rules for every section
- Read v10-final-master.md (incl. ORCHESTRATOR NOTES), v11-notes-mj1.md, and this file. The previous combined build is in _anim11/ (scripts, clips, Hoist sprites hoist11.py, compose11.py, rec11.js, board-film11.html). Reuse it by COPYING into your own section folder; never edit files in _anim11/ or another section's folder.
- PREVIEW MODE: 960x540, 15 fps, ffmpeg -preset ultrafast -crf 28; board recorded at viewport 960x540. Lay out everything in 1920x1080 coordinates scaled by 0.5, so the final HD render is the same picture.
- Output: sections/<name>/preview-pN.mp4 (N = pass number) and notes in sections/<name>/progress.md. After each preview, append "- [PREVIEW pN READY] <time>" to your progress.md and report back. Then STOP and wait for MJ's notes.
- Voice: Hoist's voice is being re-auditioned (MJ finds the current one not warm). Use the existing _anim11 audio clips as placeholders now. When a voice is picked, re-synthesize your lines with the shared tool in _anim11 (tts11.py, strict STT match, 50 ms tail pad, script pauses).
- No em dashes on screen. Never show the word "Claude" (use "Orchestrator"). Nothing personal about MJ's son beyond "four-year-old".
- CPU is shared by 5 agents, so render only what you need, at preview size.

## Voice per section (MJ, 4:29 PM): each section uses a DIFFERENT Hoist voice so MJ can compare them in context
- s1-intro: am_michael, speed 0.80
- s2-crew-tower: am_eric, speed 0.80
- s3-evolution: am_puck, speed 0.82
- s4-timelapse: am_echo, speed 0.80
- s5-tarmac: bm_george, speed 0.82
Re-synthesize ONLY your section's Hoist lines with your voice (same machinery as _anim11/tts11.py/rescue11.py: strict STT match on the trimmed clip, 50 ms tail pad, light processing only, no pitch shift). Copy the tools into your folder; write the clips there. Keep the other characters' voices as they are. Put a small corner tag on the preview, "Voice: <name>", so MJ knows which is which (preview only).

## LOCK RULES (MJ, 6:02 PM): approved = reproducible one-to-one in HD
- Every section keeps ONE build script that renders both sizes from the same inputs: `build.py --preview` (960x540, 15 fps) and `build.py --hd` (1920x1080, 30 fps). Coordinates are in 1920x1080 units, scaled by 0.5 for the preview. No separate code paths for layout.
- Every input goes in a spec file, sections/<name>/spec.json: script lines and clip files, voice and speed, timings, camera positions and zooms, crop boxes, overlay positions, colours, music cue, random seeds, which board data and plane IDs. No hidden randomness and no "re-record and hope". Board and game captures must be deterministic: drive time by frame index (virtual clock through the film hooks), never by wall-clock real time, so an HD capture of the same spec gives the same shot.
- Keep every pass. Never overwrite: preview-pN.mp4 plus spec-pN.json plus a changelog line in progress.md saying exactly what changed and why.
- When MJ says something was good, mark it LOCKED in progress.md ("LOCKED: crew dimming spotlight, p1, spec keys ..."), and do not change it again unless he asks.
- Before claiming a pass is done, re-run the build from spec and confirm the output matches frame for frame (hash a few frames).

## SHARED MACHINE LIMITS (8 GB RAM, 5 agents): mandatory
- Only ONE TTS (Kokoro) process per agent at a time; never run TTS jobs in parallel (each holds about 0.8 GB).
- Browser captures (game or board, Playwright) take the lock: `flock /home/claude/wt-out/video/sections/.capture.lock <your capture command>`. One capture at a time across all agents.
- Before a capture, check `free -m`: if "available" is under 1500 MB, wait and retry rather than crash the page.

## TOKEN BUDGET (MJ at 53% of the week, 6:26 PM): mandatory
- Do NOT hand back status-only reports. Report ONCE per pass, when the preview file exists (or when truly blocked). While a long job runs, wait on it in the background instead of reporting.
- Keep reports under 120 words. Keep tool output small (head/tail, no big dumps). No extra passes beyond what MJ or the director asked.
- Every capture under the lock must have a hard timeout: `flock .capture.lock timeout 900 node ...`. A hung capture holds the lock for everyone (one hung for 18 min at 0% CPU at 7:45 PM and was killed).

## SHOT SHEET BEFORE RENDER (MJ, 8:32 PM): mandatory, every pass
Before rendering any video (and before any long capture), make sections/<name>/shots-pN.jpg: one full-size still per camera angle and key moment in the pass (every shot change, every card or face close-up, start and end of every camera move), each labelled with its timestamp and spec keys. Report the sheet and STOP; the orchestrator approves the angles, then you render. The render must use exactly those camera settings (the same spec keys), so the video matches the approved stills.
