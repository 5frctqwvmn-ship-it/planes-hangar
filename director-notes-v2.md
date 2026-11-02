# Director notes on animatic v2 (proof cut, 5:15)

Method: 1 fps frames, 16 contact sheets with timestamps, full-size checks at 0:49 and 1:09 and 4:00, ffmpeg silencedetect, OCR of every 2nd frame for "Claude".
Overall: big improvement. Wide board is held, taps now have ripples and cards sized near a third of frame, Hoist is in his own reserved panel and is never covered, terminal has a blinking cursor, narration is continuous, no "Claude" found. Remaining problems below.

## 1. Zoomed in too far / whole board not visible
1. 02:32-02:59 (scene 5, V2 to V8): the old-build clips are cropped hard; the left and right of the field are cut off ("Radio operator", "Animatic" labels clipped at the frame edges), and the board sits in the top 40% with empty dark below. Whole board is not visible.
2. 03:09-03:25 (scene 6, V9 to V18): the board is tilted and cropped at the top, a tower block is cut off in the corner, the lower half is empty. Same crop problem.
3. 03:26-03:39 (scene 7, V19 to V22): the tilted board is cropped at both edges; the radio and Hangar tags are cut off at the left/right.
4. 04:35-04:41 (scene 10, replay at 600x): the board is whole but the plane and vehicles pile up in the middle so you cannot follow anything; fine as a montage, but see 7.
5. 04:42-05:07 (scene 10b): the live board is now a much wider/closer crop than the tour (plane fills the frame, tower and radio at the very top edge). Radio and tower are barely in frame, so the "stairs/messenger reporting to the tower" beat has nowhere to land.

## 2. Tapped item or action covered by a card, caption or end card
6. 01:00-01:13 (scene 3b, radio): the radio card opens at the dish and then sits over the left stand and the taxi line below the dish; the dish is visible, but the card lands on the Making-of stand. Move the card away from the stands (to the empty lower left).
7. 01:15-01:23 (scene 3c, the stand): card "Animatic proof cut" covers the whole left half including the stand that was tapped; the tapped plane is hidden for 8 s. Needs the card beside the stand, not on it.
8. 01:25-01:31 (scene 3d, vehicle taps): the callout "FUEL = thinking, CATERING = writing, BAGGAGE = reading" sits over the runway/stations at the bottom and the vehicle cards cover the right-hand stand; the cards are slightly larger than a third.
9. 01:54-01:59 (scene 3i): panels scroll as full-screen pages and the board vanishes entirely. This breaks the rule "whole board visible always". Show the panels as an inset or side strip with the board still live.
10. 02:12-02:19 (scene 3j end): the yellow "AT API PRICES: $74.32" box covers the runway, stations and the lower stand while the vehicles are moving there.
11. 04:36-04:40 (scene 10): the "At public API prices" end box covers the lower third of the board during the last replay moments, including the landing plane.
12. 04:52-05:02 (scene 10b): step banner at the top and the "This film: 46 tool calls" box at the bottom (from 05:03) cover the tower and the runway/station row, which is exactly where the vehicles drive.

## 3. Unreadable text
13. 00:12-00:30 (scene 2): grey "(nothing else)" under the terminal line is almost invisible (very low contrast, tiny).
14. 00:32-00:45 (scene 2b): the board is a small image with legend and tab labels illegible; acceptable for a wide hold, but the gold bar under Hoist says "Everything on this board answers a question" and is tiny.
15. 03:59 to 04:14 (scene 8): tab labels, pad names and the legend are at roughly 6 px height; "Making-of video", "Fix the crash on the ca..." are not readable. Chips on each cart are unreadable at all times in 03:26-04:14.
16. Throughout: Hoist's speech bubble text is small (about 9 px) and the subtitle shows only the current sentence fragment; it flips every 1-2 s in places (for example 02:36-02:43, 01:24-01:29, 04:25-04:30), faster than it can be read.
17. 04:55-05:07: the callout banners "STEP 17: Running a command" and the tiny vehicle cards are too small to read; the film says "Reading the script", "Filming the board", but you cannot see which vehicle is doing it.
18. 05:08-05:14 (scene 11, end card): the line "Made by MJ and his son..." is tiny and low contrast; it appears from 05:11 and the film ends at 05:15, so it is on screen about 4 s.

## 4. Tap not visibly shown
19. 01:25-01:29 (scene 3d, first vehicle taps): cursor present but no clear ripple on Thinker/Reader taps; the card just appears. Grow-from-point not visible at 12 fps.
20. 01:32 (Writer tap): cursor jumps in with the card already open.
21. 02:02, 02:05, 02:08 (scene 3j taps on tower, radio, agent): cursor is shown but the card pops in without a visible ripple; the second and third taps could be mistaken for hover.
22. 04:43-04:44 (scene 10b, tap on the plane): the cursor rotates a plane on its own, shows no ripple; the card opens at 04:44 away from the tap point.
23. 03:26-04:14 (scenes 7 and 8, historic versions): no taps shown at all, fine, but the narration says "tap" nowhere, so OK. No issue.
24. 03:38-03:58 (scene 7, the unlock): arcs, lights, icons, beacon are named with pop-up labels but there is no pointer or arrow to the thing named (labels float at the top or bottom).

## 5. Hoist covered or missing
25. 00:00 (scene 1): Hoist is in a white square cutout and not driving in; he is static in the panel. The forklift drives in per the script is not shown. Not covered, but also no character animation after that. Only the three dots pulse.
26. 05:14 (scene 11): the panel card goes blank and the forklift icon moves out; the sequence looks like a bug (blank beige card plus a stray icon). Not covered otherwise; Hoist is never covered anywhere else. Good.

## 6. The word "Claude"
27. None found. Checked by OCR every 2 s and by eye on all sheets; the board says "ORCHESTRATOR" on the tower and "Orchestrator" in cards. Note the tiny Sonnet/Opus/Haiku/Fable names are fine. One thing to verify: the 04:42 card "Making-of film: animatic v2" and 02:00 "Fix the crash on the carrier" are fine.

## 7. Dead air or pacing
28. No narration gap over 3 s at -30 dB (silencedetect found none at -45, -30 or -25 dB with d >= 3 s). The first 11 s (title) carries only three short lines; the picture is a static title card for 10 s: dead air in the visual sense, 00:00-00:10.
29. 00:10-00:25 (scene 2): static terminal for 15 s with only one ripple at 00:14; feels long. Questions appear 00:26-00:29 in 1 s intervals, then wait; fine.
30. 00:32-00:45 (scene 2b): the opening hold is only 13 s and the narration covers it, good; but the board is a small picture and the stands show only one plane. The brief asked for "three or four planes at once"; only one plane is parked and the rest are ghost outlines.
31. 02:21-02:31 (scene 4, V1): recreation of V1 shown 10 s, good, but the red banner "RECREATED FROM MEMORY: the real V1 was not saved" is full-width and covers the top of the field.
32. 02:32-02:59 (scene 5): the V2 to V8 labels change roughly every 5 s with narration that lags (the V5 label appears at 02:37 while the narration still says V4); V5 to V8 flash by in 3 to 4 s each. Too fast to take in.
33. 03:09-03:25 (scene 6): V9 to V18 at about 1.5 s per version; nothing is readable, which is the point of a montage, but the label and the narration do not match (for example "Rings for the CPU" on V13).
34. 04:15-04:29 (scene 9): fine pace.
35. 04:30-04:41 (scene 10): 11 s for a whole Sunday replay, then 04:38 line "what is it doing?" is said but the replay is at its busiest; fine, but the planes have no readable detail.
36. 05:08-05:15: the end card holds 7 s; fine.

## 8. Confusing for a first-time viewer
37. 00:32-00:45: the viewer is dropped into the board with no pointer to what to look at; the caption "Everything on this board answers a question" is cut by a gold bar.
38. 00:46-00:58 (scene 3a): the tower is introduced by a cursor that has no visible start (cursor appears at 00:47 on a random point). The yellow label "THE ORCHESTRATOR" is at the far left, away from the tower; "ROOF = the model it runs" (00:53) points to nothing visible.
39. 01:00 to 01:13: the narration says "dish", the card says "Radio operator" and the gold bar says "Dish = the cheap relay, Cloud = where the board lives"; three names for one thing. Also the cloud is never highlighted.
40. 01:24 to 01:35 (3d): only three of the seven vehicles are tapped (thinker, reader, writer); the narration lists fuel, catering, baggage, tug, van, inspection, stairs; viewer cannot match them.
41. 01:36-01:42: "Green, amber, red" labels cover the legend at the bottom, so the legend itself (the thing being explained) is hidden.
42. 02:21: "V1 of 29 - recreated, the real one was not saved" is honest but confuses the story: the viewer sees planes, then at 02:32 a sudden jump to trucks with no explanation of why the board changed.
43. 03:26-03:37 (scene 7, V19 to V22): "little people carrying each step" is not visible; the people are 8 px dots.
44. 04:15-04:19 (scene 9): "V29 of 29" and "PLANE = one agent" labels, but the planes are tiny and dark on the dark pad; the crew label at 04:20-04:24 floats over the runway.
45. 05:08 to 05:10: the end card reads "Every piece on this board is there because something was hard to see" with Hoist saying "That's the board", then "Now go check on your crew"; the card shows 3 s before the second line, so the card comes before the narration finishes.
46. Hoist never moves or points; he is a static portrait, so the "guide who walks you through" idea is weak. Add a point-at gesture or a bob when speaking.
47. The captions lag narration by about 1 s in several places (for example 01:24 "Tap a vehicle" gold bar while the narration was already at "Fuel truck").

## Five most important fixes
1. Re-frame all historical clips (02:32-04:14, scenes 5 to 8) so the whole board is visible, filling the top two thirds without cropping at the edges; put the labels at at least 11 px and slow V5 to V8 to about 5 s each.
2. Stop covering the subject: move the cards so the tapped stand, vehicle or radio stays visible beside the card (01:00-01:23, 01:25-01:31); put the price box, end box and "This film" box in a strip below the board, not over the runway (02:12-02:19, 04:36-04:40, 05:03-05:07).
3. Make every tap readable: add a bigger ripple ring plus a one-second grow animation from the tap point for 01:25-01:32, 02:02-02:08 and 04:43-04:44, and add the same for scene 3i (keep the board visible, show panels as an inset at 01:54-01:59).
4. Fix the scene 10b framing (04:42-05:07): zoom out to the whole airfield with the tower and radio visible, and make each step's vehicle and step label readable (at least 11 px) and in sync with the narration.
5. Make Hoist alive and the labels consistent: Hoist should drive in at 00:00 and point or bob while speaking; use one name per thing (Radio operator or Dish, pick one); fix the blank end card at 05:13-05:14 and the tiny credit line at 05:11.
