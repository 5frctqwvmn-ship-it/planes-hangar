# "How Planes Hangar was built": shot list (about 4 minutes, 1080x1920 vertical, 30 fps)

Captions burnt in (big, rounded sans, white with a dark shadow, never covering the planes), light instrumental music, no narration. Every claim on screen must be true to the records in /home/claude/archive (README.md milestones, data/git-log.txt, data/agents.json, data/orchestrator-steps.json, data/board/events/*.json). Artistic licence is fine in pacing and framing, not in facts.

1. Cold open (0:00-0:15). Today's game: Angel's six-jet diamond holds in smoke, then blasts off screen. Caption: "Planes Hangar. Built for one 4-year-old pilot."
2. Day one (0:15-0:45). The earliest kept version (milestone m01-start, Oct 23) running in its hangar and a race, beside a scrolling "flight log" of the first commits from data/git-log.txt. Caption: "October 23: the first version that's still saved."
3. The crew (0:45-1:30). The Hangar Ops Board (https://claude.ai/artifact/DNSSxDdmvaKByFM1ibBhsw, or the local copy /home/claude/wt-out/board-index.html fed with data/board/events) replaying at high speed: trucks rolling to bays, radio arcs from the tower, the shipped row filling. Overlay counters: agents started, how many at once, model mix (Opus / Sonnet / Haiku), published builds. Caption: "One orchestrator. A crew of AI agents, each on its own job."
4. The passes (1:30-3:00). Before/after wipes using the same camera on both versions (milestone branches, plus ?classic=ships / ?classic=props / ?classic=all on today's build):
   - maps pass 2 then declutter (m02, m05)
   - stability: the memory chart from about 1 GB down to about 250 MB per race (draw it as a simple animated bar chart)
   - learning games: number race with "2 + 2" and touch-to-count, Letter Race, Say it!
   - Angel arrives (m06), the airport start screen (m07), Ozzie tilting his rotors (m08)
   - ground crew on the carrier deck, then in Navy / Arctic / desert colours (m09, m10)
   - ships and set pieces, classic vs new (today's build with and without ?classic=all)
   - real Hornets parked on the deck
   Use the existing before/after sheets in /home/claude/archive/images/ where filming would cost more than it adds.
5. By the numbers (3:00-3:30). Animated counters from the records: commits, builds published (100+), agents run, weighted tokens by model, planes in the roster (22), voice lines.
6. Ending (3:30-3:50). Ozzie lifts off rotors-up, tilts forward and flies off; credits: "Made by MJ and his son, with Claude as orchestrator and a crew of agents."
