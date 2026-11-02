# v4 progress (update after each step)
Done scenes (scenes/*.mp4): s1_open s2_writeup s3_prompt s3_list s3_ba s4_airport s5a_models s5b_code s5_build s5_paint s5e_voice s5_angel s5_ozzie s9_stab s10_numbers s11_end
Pending: s6_crew s7_ships (raw4/crew*, ships_*, deck_* captured by `node tools4/jobs.mjs crew,ships`, wait for raw4/<name>/DONE), board chapter s8_*.
Board: tools4/boardrec.mjs records archive/board-versions v2..v7 + dash + day into raw4/board_*; tools4/scenes_e.py renders s8_afternoon s8_board s8_dash s8_day. Concatenated as ONE scene via tools4/mkboard.sh -> scenes/s8_board.mp4
Render: cd tools4; python3 scenes_d.py s6_crew s7_ships; python3 scenes_e.py ...
Assemble: bash tools4/assemble4.sh   (uses scenes/s8_board.mp4 if present; drop_in_board.sh <file> to swap)
Honest gaps: changes 1-18 of board plan have no per-version recordings (only the early trucks replay raw/board); shown as a text timeline over that replay.
crew/ships recapture with aerial shots running (jobs.mjs crew,ships)
s8_afternoon, s8_board rendered. pending s8_dash s8_day (raw4/board_dash, board_day), s6_crew rerender, s7_ships
s8_dash s8_day rendered
Plan change: board chapter must END on change 29 (planes version, not built yet). Slots left: scenes/s8_day.mp4 (whole-day replay) and a final s8_planes.mp4. s8_day currently rendered on v7 only as a placeholder; REMOVE or replace scenes/s8_day.mp4 once the planes board exists, then add s8_planes after it in tools4/assemble4.sh LIST and run it.
s6_crew s7_ships rendered; assembling
CUT ASSEMBLED: /home/claude/wt-out/video/planes-hangar-making-of-v4.mp4 (4:30) + making-of-v4-sheet.jpg. Missing slots: change 28/29 board beats and whole-day replay (scenes/s8_day_v7_placeholder.mp4 is a v7-only version; rename to s8_day.mp4 if wanted). To add: put s8_planes.mp4 and s8_day.mp4 in scenes/, add s8_planes to LIST in tools4/assemble4.sh, run it.
## V5 (notes in v5-notes.md)
Running: raw4/world_* (jobs.mjs world) and raw4/b5_* (tools4/boardrec5.mjs, boards served from v5/boards port 8804). Earliest board on disk (orig1) already has trucks+orchestrator: no planes-first version recoverable (report it).
Plan v5 order: title, angel/ozzie intro + code + build + paint + voice(counts only) + win shows, writeup+prompt (one line for 4 changes), world passes (props/ships old vs new + stability bar fixed), airport (layout optimizations), board (orig1 -> v2..v9, afternoon list), day on v9, numbers, end. Captions in a band below the footage (v4lib.band_cap).
