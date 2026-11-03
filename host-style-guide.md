# The prompt: one master brief, plus image and video templates

All three models gave a copy-ready prompt. I combined them below and fixed a few problems. Paste **Prompt 1** into your scriptwriting model (ChatGPT, Claude, Gemini). Use **Prompts 2 and 3** later, once you're generating images and video.

## 1. Where Models Agree

| Finding | Gemini 4 Argon Thinking | GPT-6 Astra Thinking | Grok 4.7 Thinking | Evidence |
|---|---|---|---|---|
| Create an original character; don't copy Mr. DNA | ✓ | ✓ | ✓ | All three tell the model to "invent" or "design an original" host |
| His body is the subject, and every gag teaches | ✓ | ✓ | ✓ | Each prompt has a rule like "the body is the prop" |
| Hand-drawn cel look, explicitly not 3D | ✓ | ✓ | ✓ | All three ban glossy or Pixar-style 3D |
| Sincere, folksy host who's never sarcastic | ✓ | ✓ | ✓ | All three ban sarcasm and memes |
| Mute test as the quality check | ✓ | ✓ | ✓ | Picture alone should explain the process |
| Plan everything before generating video | ✓ | ✓ | ✓ | Character sheet and script come first |

## 2. Where Models Disagree

| Topic | Gemini 4 Argon Thinking | GPT-6 Astra Thinking | Grok 4.7 Thinking | Why They Differ |
|---|---|---|---|---|
| Format | Three prompts: script, image, video | One general brief | One long master brief | Different guesses about your toolchain |
| How detailed | Mid-length | Loose; works for any topic | A full 12-beat shot list | Flexibility vs. control |
| Voice | Texan drawl | "Folksy," original | Light Texan drawl | GPT-6 avoids imitating the original actor |
| Lines from the film | None | None | Slips in actual film lines | Grok breaks its own no-copy rule; I removed them |

## 3. Unique Discoveries

| Model | Unique Finding | Why It Matters |
|---|---|---|
| Gemini 4 Argon Thinking | A separate character-sheet prompt for image models | Keeps the character consistent across video shots |
| GPT-6 Astra Thinking | "Don't let the metaphor hide limitations" | Useful for real technical topics |
| Grok 4.7 Thinking | End by cutting back to a room less sure than he is | Captures the film's irony |

## 4. Comprehensive Analysis

Grok 4.7 Thinking's version was the most complete, so I used it as the base for Prompt 1. GPT-6 Astra Thinking's version is shorter and works for any topic. Gemini 4 Argon Thinking was the only one to split the work by tool, so Prompts 2 and 3 come from it.

What I changed:
- **Removed quoted film lines.** Grok's version had them while also telling the model not to copy the film's dialogue.
- **Settled the voice** on a light Texan drawl, which matches the original.
- **Kept the 12-beat structure,** written so it works for any topic.

### Prompt 1 — Script and storyboard (paste first)

```text
ROLE
You are an animation director and scriptwriter. Create a 75–110 second animated explainer about [TOPIC] for [AUDIENCE], in the spirit of the 1993 Jurassic Park "Mr. DNA" orientation film (Kurtz & Friends cel animation, modeled on 1950s Frank Capra Bell science films like Hemo the Magnificent).

Capture the method, not the trademark. Invent an original character, original dialogue, original catchphrase. Do not copy the film's design, lines, or voice performance.

THE ESSENCE
The subject becomes a character. The character becomes a demonstration. The demonstration becomes a little magic trick.
It should feel like a cheerful theme-park pre-show film. The host sincerely believes the brochure: no sarcasm, no winking, no memes, no influencer energy.
Every gag must teach something. If a joke doesn't explain the idea, cut it.

CHARACTER
- A friendly little scientific showman whose body IS the subject (e.g., a helix of colored beads, a strand of code, a chain of parts).
- Face on the top of the form: big oval eyes, thick dark eyebrows, wide friendly smile. Simple white cartoon gloves, stubby feet.
- Flat cel colors, hard black ink lines, limited cheerful palette. No gradients, no glow, no 3D shading.
- Elastic scale: small enough to pop off a fingertip, big enough to fill the frame.
- Cartoon physics: short anticipation, squash and stretch, slight overshoot, then a held pose. Use stillness so the next action reads.
- Emotions beyond smiling: curiosity, pride, surprise, comic frustration.

VOICE
Warm, quick, light Southwestern drawl. A small-town science teacher who still loves the exhibit. Contractions, short sentences, one repeated metaphor. One slapstick yelp allowed. One triumphant catchphrase moment (write an original one). Talk to one curious visitor, not a stadium.

VISUAL RULES
1. 1990s 2D cel animation, animated on twos (12 fps). Strong poses and holds.
2. Collage of media with hard cuts: live-action host, flat color fields, nature/real-world footage, lab or equipment footage, diagrams.
3. Signature move: the cartoon crosses into live action. He pops off a real finger, leaps into footage, gets stuck in an object, escapes through a tool, jumps in front of racing data.
4. One idea per shot. The picture says it first; narration never just describes what we already see.
5. Simple, bold backgrounds that change color to mark each chapter.
6. Camera mostly locked. Movement comes from the character and props.
7. Text is physical: letters and labels are objects he holds, drops, or plugs into gaps. No motion-graphics text or HUDs.

STRUCTURE (12 beats, mostly 4–7 seconds each)
Follow a strict cause-and-effect chain: source → problem → extraction → scale → gap → fix → result.
Every line needs a visual verb: pull, reveal, separate, connect, unfold, inspect, transform.
1. Live host with a prop containing the subject. The cartoon peeks out and pops free.
2. Flat color field, character large. Introduces himself and the idea in one sentence.
3. Diagram background he shoves aside like a curtain.
4. He leaps into a real-world or process shot.
5. The obstacle: he gets stuck or swallowed by the problem (stretch gag, muffled yell).
6. Time or scale jump. He pops back out and names the result.
7. Lab or tool shot. He escapes through the tool.
8. Complexity race: data or parts rush past, he gets dizzy and shoved aside.
9. The fix: he carries the missing pieces and plugs the gap.
10. The payoff: he steps aside and presents the result. End on wonder.
11. Hard cut back to the live room. He's still smiling; the room is a little less sure.
12. Optional: a small wave, then black.

ACCURACY
Keep the science correct. Use one metaphor. Where it stops matching reality, say so in one short line. No fake certainty.

SOUND
Light, curious orchestral underscore that ducks under the voice. Specific sound effects tied to actions: cork pop on entrance, slide whistle on a stretch, sticky squelch on the trap, whoosh on data, crack on the reveal. Use them selectively.

DELIVERABLES (in this order; no video until 1–4 are approved)
1. One-sentence premise.
2. Style bible, under 400 words, including what to avoid.
3. Character sheet descriptions: front, side, squash, stretch, stuck, dizzy, presenting. State what his body can't do.
4. Timed script table:
   Time | Picture | Action | Line | Expression | Sound | What it teaches
5. One video prompt per shot: start pose, action, end pose, background, camera, continuity note.
6. Accuracy check: flag any misleading metaphor.
7. Mute test: if the picture alone doesn't show the process, fix the picture.

AVOID
Glossy 3D or Pixar looks, generic corporate motion graphics, a mascot standing beside bullet points, constant camera moves, random bouncing, dense labels, fast cuts that hide cause and effect, jokes unrelated to the lesson.

SUCCESS TEST
Sound off: the process is clear. Picture off: the narration makes sense. He makes the idea happen, and enjoys it.
```

### Prompt 2 — Character sheet (Midjourney, Flux, etc.)

```text
1990s traditional 2D hand-drawn cel animation model sheet of an original science mascot: [DESCRIBE BODY, e.g., an anthropomorphic double helix made of colored beads connected by white rungs], big oval eyes, thick black eyebrows, wide friendly smile, thin rubber-hose arms, white four-fingered cartoon gloves, stubby feet. Six poses on plain white: waving, stretched like a spring, squashed flat, stuck and struggling, dizzy holding head, presenting with both hands. 1950s educational-cartoon style, flat gouache colors, hard black ink outlines, no 3D shading, no gradients.
```

### Prompt 3 — Per-shot video (Runway, Kling, Veo, Sora); attach the character sheet as a reference image

```text
STYLE: Early-1990s traditional 2D hand-drawn cel animation composited over [BACKGROUND: e.g., flat royal-blue field / live-action 1990s lab footage]. Flat colors, thick black ink outlines, subtle cel drop shadow, 35mm film grain, light projector flicker, animated on twos. Strictly 2D, NOT 3D CGI, NOT Pixar, NOT anime.
ACTION: The cartoon mascot [ONE ACTION FROM SCRIPT TABLE]. Brief anticipation, squash-and-stretch, slight overshoot, settles into a cheerful held pose. Locked camera.
```

**One editing tip:** most video tools generate smooth motion, which kills the cel look. In editing, drop the cartoon layer to 12–15 fps, keep the background at 24 fps, and add a soft drop shadow under the character. Make the cartoon and the live-action footage separately, then layer them, rather than generating both in one pass.

Sources
