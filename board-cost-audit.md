# Hangar Ops Board: cost and usage audit

Auditor: Opus agent `audit` (aa89bd4413554d851), read-only. Audited Nov 2, 2026, about 11:30 PM to 11:40 PM Austin time (CST). All times below are CST.

Sources: `/home/claude/boardtick.py` (cost code unchanged since 23:28), `/home/claude/wt-out/board-index.html` (as of 23:32, after the cachefix agent moved "% of week" to dollars), `/home/claude/radio.log`, every transcript under `/root/.claude/projects/-home-claude/917e4d6d-...` (orchestrator plus 70 subagents), the usage readings the orchestrator wrote to the board database, and the Claude Code `cost-state` lines inside the orchestrator transcript.

Prices: Anthropic, "Pricing", https://platform.claude.com/docs/en/about-claude/pricing (the page shows no publication date; fetched Nov 2, 2026). Per million tokens (input, 5m write, 1h write, cache hit, output): Fable 5.1 $10 / 12.50 / 20 / 0.25 / 50; Opus 5.5 $4 / 5 / 8 / 0.20 / 20; Sonnet 5.5 $2 / 2.50 / 4 / 0.10 / 10; Haiku 5.5 up to 100K prompt $0.10 / 0.125 / 0.20 / 0.01 / 0.50, over 100K $0.50 / 0.625 / 1 / 0.05 / 2.50 (prompt size counts cache reads and writes, per request). No long-context premium on the other models. Batch is 50% off (not used). US data residency is 1.1x (not used: every request says `inference_geo: global`). Fast mode is Opus 5.5 $8 / $40 (not used: every request says `speed: standard`, `service_tier: standard`). Web search is $10 per 1,000 (no request recorded any `web_search_requests`). No minimum charge is listed. Thinking is billed as output; the transcripts' `output_tokens` already include it (Claude Code's own cost tally matches my output-only pricing, see finding 9).

## Verdict

**The per-message pricing is correct. The totals and every usage percentage built on them are not.**

- The feed prices each message exactly right. My own recount matches it to the cent on every transcript it scans: orchestrator $102.8486, radio $22.1553, cutv6 $11.5904, audit $2.3906, roster $0.7749 at the 23:36 stats event. The price table, the 5m/1h split, the Haiku over-100K tier and the one-usage-per-message-id rule all check out.
- The problem is what gets summed. The board total ($141 at 23:36) is neither "this session" nor "this week". It leaves out finished agents ($66 since the reset). It adds $35 of the orchestrator's spend from last week. And it double counts when a board id is reused. Real list-price spend since the weekly reset at 3:00 PM is **$171.87**. Real spend for the whole Claude Code session, by Claude Code's own tally, is about **$4,317**.
- The weekly gauge (currently about **14.6%**) is too low. MJ's readings put it at about **18.6%** (blended) or **19.6%** (Fable-aware). His readings also show that Fable is metered roughly 14x harder per list dollar than the other models. Fable-only usage is already about **17%** of the week against a 50% Fable cap, and the page does not track that meter at all.
- The session gauge never moves: two session readings are never paired, so it shows the last reading or 0.
- The run-out forecast uses the same broken total.

## Recomputed cost per actor vs the feed

Since the weekly reset (Mon Nov 2, 3:00 PM) up to the 23:36 stats event. "Feed" is what the latest stats event shows for that actor. "All" is the transcript's full list-price cost (for the orchestrator, since the feed's BASE of Nov 1, 4:24 PM).

| Actor (board id) | Agent | Since reset, by model ($) | Since reset ($) | All ($) | Feed now ($) |
|---|---|---|---|---|---|
| Orchestrator | main | Fable 40.28, Opus 27.14 | 67.42 | 102.85 | 102.85 |
| radio #1 | ae41ee3b | Haiku 19.52 | 19.52 | 19.52 | not listed |
| letters | a2d24ef8 | Sonnet 0.84 | 0.84 | 0.84 | not listed |
| video6 | aa340dbf | Sonnet 1.13 | 1.13 | 15.27 | not listed |
| cost | afcb539d | Sonnet 2.51 | 2.51 | 2.51 | not listed |
| storyboard | a6659c52 | Sonnet 1.95 | 1.95 | 1.95 | not listed |
| animatic | a985bbf9 | Sonnet 0.78 | 0.78 | 0.78 | not listed |
| animatic2 | a59a1a75 | Sonnet 4.12 | 4.12 | 4.12 | not listed |
| feedfix | a864c218 | Sonnet 1.29 | 1.29 | 1.29 | not listed |
| director (Sonnet) | ad2fb2b3 | Sonnet 0.49 | 0.49 | 0.49 | not listed |
| radio #2 | aef3a8c6 | Haiku 3.37 | 3.37 | 3.37 | not listed |
| proofv3 | a6163e01 | Sonnet 3.22 | 3.22 | 3.22 | not listed |
| radio #3 | af30c813 | Haiku 0.03 | 0.03 | 0.03 | not listed |
| cutv4 + cutv5 + cutv6 (one resumed agent) | a0992819 | Sonnet 11.66 | 11.66 | 11.66 | 11.66 (as cutv6) |
| thinkfix | a4ec26a2 | Sonnet 0.27 | 0.27 | 0.27 | not listed |
| radio #4 (current) | ae3a0f8b | Haiku 22.17 | 22.17 | 22.17 | 22.24 |
| estcost | aedb87d5 | Sonnet 0.23 | 0.23 | 0.23 | not listed |
| director (Fable, run twice) | a5f57b04 | Fable 19.88 | 19.88 | 19.88 | not listed |
| replayfix | a9c5995e | Sonnet 0.63 | 0.63 | 0.63 | not listed |
| tester | a6e61814 | Sonnet 1.25 | 1.25 | 1.25 | not listed |
| bugfix | a13690a7 | Sonnet 4.84 | 4.84 | 4.84 | not listed |
| cachefix | abdf71f9 | Sonnet 1.00 | 1.00 | 1.00 | 1.00 |
| audit | aa89bd44 | Opus 2.49 | 2.49 | 2.49 | 2.63 |
| roster | a13397c2 | Sonnet 0.77 | 0.77 | 0.77 | 0.77 |
| **Total** | | Fable 60.17, Haiku 45.09, Sonnet 36.91, Opus 29.53 | **171.87** | | **141.15** |

Small gaps in the last column (radio, audit) are only timing: those agents were still writing. At the same instant the two figures match exactly.

All 70 transcripts on disk, all time: $872. Claude Code's own `cost-state` for the session (which started Sep 27): $4,316.58 at 8:19 PM. Most of that is Opus work from before the orchestrator transcript was compacted and pruned.

## Findings

**1. Finished agents drop out of the total whenever the feed restarts. (Largest error.)**
- What is wrong: `SC` (the per-actor scan cache) lives only in memory. The feed calls `os.execv` to reload itself every time `boardtick.py` is edited. After a reload, `stats_event` scans only the orchestrator and the agents currently in `board-running.txt`. Nothing about finished agents is saved: `board-stats.json` keeps CPU only.
- Evidence: the feed total falls from $99.15 to $77.21 (8:05 to 8:46 PM), from $141.66 to $105.56 (10:46 PM), and from $137.20 to $133.73 (11:27 PM). Finished actors (cost, storyboard, animatic, animatic2, feedfix, director, cutv5, tester and others) vanish from `stats.actors`.
- Size: $66.37 of this week's spend is missing from the current total, 39% of the real $171.87.
- Fix: save each actor's priced message map (`mu`, keyed by agent id) to disk, or rebuild costs every cycle from every `subagents/agent-*.jsonl` whose messages fall in the window. Do not rely on `board-running.txt` alone.

**2. Scan offsets are keyed by board id, not by agent id, so a new agent under an old board id is read from the wrong offset.**
- What is wrong: `SOFF[key]` and `SC[key]` use the board id ("radio", "director", "cutv5"). When radio moved from ae41ee to aef3a8 at 7:27 PM, the feed seeked the new file to the old file's byte offset. The new file was shorter, so nothing was read.
- Evidence: "radio" stays at exactly $19.5236 in the 7:28 PM and 7:51 PM stats events while aef3a8 ran and spent $1.91 in that span ($3.37 in total).
- Size: $1.91 to $3.37 per radio respawn missed while the feed stays up. Each new radio also inherits the old radio's dollars under the same key.
- Fix: key `SOFF`, `SC` and `seen` by agent id (or by board id plus agent id), and sum per board id only for display.

**3. A resumed agent gets double counted under each new board id.**
- What is wrong: cutv4, cutv5 and cutv6 are all agent a099281934204d23d (resumed). The director (Fable) is a5f57b04, run twice. A new board id starts scanning from offset 0, so its cost repeats the earlier phases.
- Evidence: the 10:26 PM stats show cutv4 $5.1988 plus cutv5 $9.1616, where cutv5 already contains cutv4's $5.20. Today cutv6 shows $11.66, which includes about $10.5 of cutv4 and cutv5 work done before cutv6 was spawned.
- Size: $5.20 overcount in the total at 10:26 PM. The estimate-vs-actual line for cutv6 is about 7x too high (the true cutv6 share is about $1.2).
- Fix: count each (agent id, message id) once across the whole roster. For per-task cost, snapshot the agent's cumulative cost at the board id's spawn time and report only the difference.

**4. The orchestrator is counted from a stale baseline.**
- What is wrong: `BASE = 1793571840000` (Nov 1, 4:24 PM, an old calibration point) is still the orchestrator's start. Agents are counted over their whole transcript. Nothing is counted from the weekly reset (Nov 2, 3:00 PM).
- Evidence: orchestrator since BASE is $102.85; since the reset it is $67.42.
- Size: $35.43 of last week's spend sits inside "% of week" and the totals. The orchestrator row currently claims 13.5% of week ($102.85 / $7.64).
- Fix: when a `usage` event with a new `resetAt` arrives, use that week's start (resetAt minus 7 days) as the window for every actor. Send per-window sums (`usdWeek`, `usdSinceReading`) from the feed.

**5. The dollars-per-1% calibration ($7.64) comes from the broken total, and one blended rate cannot fit Fable.**
- What is wrong: `calibrate()` uses `stUsd(stats)` at the two readings: $52.29 at 3:31 PM and $98.15 at 7:53 PM, so $45.86 over 6 points is $7.64 per 1%. The real spend between the readings is $58.92 (Fable $19.13, Haiku $20.67, Sonnet $12.31, Opus $6.82). The feed missed $13.06 of it (findings 1 and 2), so the true blended rate is $9.82 per 1%. Reading rounding (6 plus or minus 1 points) gives a range of $8.42 to $11.78.
- What the readings imply: MJ's Fable-only figure (3% at 3:31 PM, 8% at 7:53 PM) is in weekly-limit units and is part of the all-models figure. From the reset to 3:31 PM, $8.59 of Fable made 3%. From 3:31 to 7:53 PM, $19.13 of Fable made 5%. Together, $27.72 of Fable made 8%: **about $3.47 of list-price Fable per 1% of week** (range $3.26 to $3.70). Over the same 4h53m, $50.03 of non-Fable spend moved "all models minus Fable" by only about 1 point (0 to 2 after rounding): **about $50 per 1%** (at least $25). Plan metering is therefore far from proportional to list price. Fable counts about 14x more per list dollar than Opus, Sonnet or Haiku (at least 7x).
- Size: today's gauge is 9 + ($141.15 - $98.15) / $7.64, about **14.6%**. Real spend since 7:53 PM is $93.94. Blended at $9.82 that gives about **18.6%**. Fable-aware (Fable $32.45 / $3.47 plus non-Fable $61.49 / $50) gives about **19.6%**, with **Fable-only about 17.4%** (since the reset: $60.17 / $3.47). The gauge reads 4 to 5 points (22% to 26%) too low.
- Per-actor "% of week" is skewed both ways. Fable actors are understated about 2.2x (they should use $3.47, not $7.64). Non-Fable actors are overstated about 6.5x (radio shows 2.9% but is about 0.4%). The Fable director (QC) cost about 5.7% of the week but would show about 2.6%.
- Fix: run two meters. Fable% = Fable dollars / Fable dollars-per-1%. Week% = Fable% + non-Fable dollars / non-Fable dollars-per-1%. Fit both from the per-model dollars the feed already sends (`usdM`), using the Fable-only and all-models numbers from each reading (add `fablePct` to `usage` events instead of keeping it only in the text). Show the Fable meter against its 50% cap. Show whole percents or a range: the readings are integers.

**6. The session gauge is never calibrated, and the 3:31 PM reading's reset time is probably wrong.**
- What is wrong: `calibrate(SR, null)` pairs readings only when their resets differ by strictly less than 3600e3 ms. The 3:31 PM reading has resetAt 7:00 PM; the 7:53 PM reading has resetAt 8:00 PM. The difference is exactly 1 hour, so they are never paired. The session estimate becomes the last `basePct` plus 0.
- Also: a 3:31 PM reading with a 7:00 PM reset implies a 2:00 to 7:00 PM window, but nothing ran between 2 and 3 PM ($0.00). The weekly reading kept rising continuously through 7:00 PM. So the window was very likely 3:00 to 8:00 PM, and the 7:00 PM reset was a misread.
- Consequence: from 7:00 to 7:53 PM the gauge showed 0% "waiting for a new reading" while the session was really at about 45% to 53%. Since 8:00 PM it shows 0% again, although a new session has been running.
- Implied rate: 15% to 53% (38 points) for $58.92 is **about $1.55 of list price per 1% of session**, blended. So one full session is about 15% to 17% of the week.
- Fix: correct the 3:31 PM reading's resetAt to 8:00 PM. Pair readings whose resets are within 1 hour inclusive. Use $1.55 per 1% (or a Fable-aware pair) as the fallback. After resetAt, start a new estimate at 0 plus the dollars since resetAt, labelled "est.", instead of showing 0.

**7. The run-out forecast uses the same broken totals.**
- What is wrong: `paceOf` takes `max(0, usdTot(now) - usdTot(45 min ago)) / upp / hours`. A feed restart drops `usdTot`, which is clamped to 0. For 45 minutes after each restart the pace reads near 0, and "you run out" is pushed past the reset. A reused board id can make it spike instead. It uses the blended $7.64, which hides the binding limit: the Fable cap. Fable is at about 17.4% of 50%, and each cold Fable turn by the orchestrator costs $7 to $12 (about 2% to 3.5% of week). The forecast is only drawn at 80% or above, so it would never warn about the Fable cap. A 45-minute window over such lumpy spend is also noisy.
- Size: the pace is understated by the share missing from `usdTot`: 55% since 7:53 PM ($42.61 counted vs $93.94 real).
- Fix: compute pace from per-window dollars summed over all agents (finding 1). Forecast the Fable meter against 50% and the weekly meter against 100% separately. Show the Fable warning from 35% to 40% on. Use a 2 to 3 hour window, or an average weighted by model.

**8. Estimate vs actual: wrong units in the fallback rates, and wrong actuals for reused ids.**
- Measured dollars per million weighted tokens (input + 1.25x writes + 0.1x reads + 5x output) since the reset: Opus 2.2 to 3.4, Sonnet 1.35 to 1.43, Haiku 0.42 to 0.49 (the radio runs above the 100K tier), Fable 7.0 to 15.8 (the orchestrator's cold 1h cache writes). `EST_FALLBACK` = {opus 2.5, sonnet 1.2, haiku 0.07, fable 6.5}. Haiku is about 6.5x too low and Fable up to 2.4x too low. The fallback is used most of the time, because `rateTable` learns only from finished agents still in `stats.actors`, which finding 1 removes.
- Actuals: `actUsd` is the cumulative cost of whatever transcript the board id points to. That is wrong for resumed agents (cutv6, finding 3), and it falls to "No actual cost reported" once a finished agent leaves the feed.
- `rateTable` averages per-agent ratios rather than total dollars over total weighted tokens, so small agents weigh too much. This is minor.
- Fix: send `est` in dollars at spawn (the orchestrator knows the model), or fix the fallbacks to {opus 2.8, sonnet 1.4, haiku 0.45, fable 10}. Keep finished agents' costs (finding 1). Compute rates as dollars summed over weighted tokens summed. Charge resumed work against the spawn snapshot (finding 3).

**9. Usage the transcripts never show (small).**
- Claude Code's `cost-state` lines in the orchestrator transcript keep a running list-price total per model (session plus subagents). Between snapshots it matches my transcript recount for Sonnet ($13.11 vs $13.12), Haiku ($19.57 vs $19.52) and Fable ($17.94 vs $17.81). This confirms the prices and that thinking is inside `output_tokens`.
- Opus is higher in the cost-state by $1.21 (9%), $0.22 and $0.11 over the three snapshot intervals since Nov 2 8:35 AM. These are hidden orchestrator side requests (compaction, summaries and the like) that write no assistant line.
- Compaction requests (orchestrator Nov 1, 7:02 PM; radio Nov 2, 5:54 PM and 11:18 PM) are not in the transcripts either; they are cheap because they hit the cache.
- The 6 WebSearch and 10 WebFetch calls run as separate requests that are not logged: at most about $0.06 in search fees plus small token costs.
- The 12 `<synthetic>` API-error lines carry zero usage and are correctly unpriced.
- No compaction, sidechain or tool-result line carries usage that the feed misses. No message id appears in two files.
- Size: about $1.5 this week (under 1%).
- Fix (optional): add the deltas of the newest `cost-state` as an "unlogged" line, or use it as a check value.

**10. The orchestrator transcript has lost its history; the label "this session" is wrong.**
- The orchestrator file holds assistant messages only from Nov 1, 7:01 PM. Its compaction dropped 12.1M tokens (`cumulativeDroppedTokens`). So "since 4:24 PM" really means "since 7:01 PM", and the panel text "this session's work would cost about $X" shows $141 against a real session cost of about $4,317 (cost-state), or $172 this week.
- Fix: label the figure "this week" and use the week window (finding 4). If a lifetime figure is wanted, show cost-state's `totalCostUSD`.

**11. Old token-weight code left in the page.**
- `MF` (Opus 1, Sonnet 0.6, Haiku 0.2, with the orchestrator always "opus" even on its Fable turns) and `out.cum` are still computed, under the comment "fitted to MJ's usage readings". The readings do not support them. The old perPct constants (8M per 1% week, 1.7M per 1% session) predicted 2.3% and 10.6% for the 3:31 to 7:53 PM span, against the real 6% and 38%: 2.7x and 3.6x too low. The dollar switch fixed this.
- Fix: delete `MF` and `cum` and that comment, so nothing reads them again.

**12. Formatting and windows (minor).**
- `ktok` prints "1000k" for 999,500 to 999,999 and "0k" below 500. Use the `ctok` rule (switch to M at 999,500; show raw counts under 1k).
- The weekly gauge's `toFixed(1)` suggests 0.1-point precision. The calibration is only good to about plus or minus 17%, so show whole percents.
- The "today" effort rows use the browser's local midnight, which is fine for Austin. They mix windows, though: an agent's row is its whole transcript cost, while the orchestrator's row is spend since midnight.
- The weekly resetAt values are right (Mon Nov 9, 3:00 PM = 1794258000000).
- Dollar rounding (2 decimals under $100, whole dollars above) is fine.

## Cost drivers worth knowing (not math errors)

- **Cold Fable turns by the orchestrator.** A single Fable turn rewrites the full 360K to 600K context into the 1h cache at $20 per million: $7.28 (8:35 AM), $7.30 (3:03 PM), $9.22 (5:04 PM), $9.91 (7:26 PM), $11.99 (11:18 PM). These cache writes are about $50 of the orchestrator's $55.86 Fable spend. The 5:04 PM and 7:26 PM turns alone explain MJ's Fable meter going from 3% to 8%. Each costs about 2% to 3.5% of the week.
- **The radio runs above Haiku's 100K tier.** 3,133 of its requests went over 100K, costing $52.61 where the 100K tier would have cost $10.52. This week's radio cost is $45. That is only about 0.9% of the week under plan metering, but it is 26% of list-price spend.

## Method

- Script: `/tmp/claude-0/-home-claude/917e4d6d-feb4-59ad-982a-2757f59bd3a4/scratchpad/audit/recount.py`.
- It reads every assistant line with usage in the orchestrator transcript and all 70 subagent transcripts. Per (file, message id) it keeps the line with the highest `output_tokens`, prices it by that line's own `model`, and splits cache writes by `cache_creation.ephemeral_1h/5m` (present on every message). Haiku requests whose input plus cache read plus cache write exceeds 100,000 use the higher tier. It adds $0.01 per recorded web search (none were recorded).
- It found 9,279 priced messages, all with the TTL split. All are `service_tier standard`, `inference_geo global` and `speed standard`. Every `usage.iterations` array has one entry.
- Windows: the weekly reset is Nov 2, 3:00 PM (1793653200000); the readings are at 3:31 PM (1793655060000) and 7:53 PM (1793670780000).
