# Planes Hangar: a write-up for outside reviewers

Written 2026-11-01 from the test build's source (one file, index.html, about 19,000 lines) and from screenshots taken at iPhone size (390 x 844 points, portrait). Screenshot filenames are given in brackets so a human reader can match them; the reviewing assistant does not need them.

## 1. Summary

Planes Hangar is a private, noncommercial web game a father built for his 4-year-old son. The family is bilingual (English and Spanish), and the boy plays it on an iPhone held upright, sometimes cast to the TV. The idea: the 21 real aircraft that inspired the characters in Disney's *Planes* films (2013) and *Planes: Fire & Rescue* (2014), plus a few characters made for this game, are shown as the real machines in real paint, with friendly faces and their own voices. The boy can build each plane step by step, paint and decorate it, watch it fly, and race it. The learning is hidden inside the racing: in a learning race, a plane falls behind and asks the child for help, and answering its question (counting, adding, first sounds, saying a word) gives it a boost. The owner's rule is that learning should live in the races, not in side activities that feel like books. Tech: a single HTML file using three.js (r128) for 3D, Web Audio for engines and music, pre-recorded neural voice lines (Kokoro) per plane and language, local storage for saves with optional sync across devices, and no microphone needed for any mode (one mode can use it if allowed).

## 2. The games and modes

### 2.1 Start screen: the airfield (01-start-field.png)

What the child does: the game opens on a runway with every aircraft parked nose-toward-camera, each with a name tag. A banner says "Tap a plane!" (spoken too). He taps one; it hops, says its own name, the camera swoops in, and the hangar opens with that plane in full 3D. A "Race now!" button sits top right, and Sky City has its own button.

Teaches: nothing formal; plane names and recognition by shape.

Feedback: the hop, the name in the plane's own voice. Age fit: very good. One tap, big targets, spoken result. The name tags are text, so a pre-reader finds planes by picture.

### 2.2 The hangar (02-hangar.png)

What the child does: one plane stands in a hangar; he can drag to spin it and pinch to zoom. An info card at the top gives the real name ("PZL-Mielec M-18 Dromader"), "Inspired Dusty Crophopper in Disney's Planes (2013)", and an info button with wingspan, length, and first flight. A dock along the bottom has six buttons: **Build it, Design, Take off, Race, Learn**, plus a pink **Win show** button floating above. A speaker button turns read-aloud on and off; EN/ES switches language at any time. A list button opens a sheet with every aircraft.

Some planes have a tap-to-reveal extra in the hangar: the Space Shuttle's payload bay doors open (with the robot arm and a satellite), the Beluga's nose opens to show another plane's body inside, and Bristles (a kid's block plane) snaps apart and clicks back together.

Age fit: good as a home base. The info card is reading-level text written for adults ("Real aircraft in real-world paint, not the movie characters. Drag to turn, scroll or pinch to zoom.").

### 2.3 Build it (03-build.png)

What the child does: the plane comes apart, and he puts it back together in about 6 to 9 steps (fuselage, engine, wing, tail, landing gear, cockpit, propeller). Each step shows a numbered panel ("1. Set the fuselage on the bench") with a sentence or two of real aviation fact ("An 18-cylinder Pratt & Whitney Double Wasp, 2,000 horsepower") and a part chip he can tap to find the part. He taps "Next step" and the part flies into place. At the end: "No parts left. Time to fly."

Teaches: sequencing, part names (fuselage, propeller, landing gear, tail fin), simple cause and effect ("two big wheels up front and a small tail wheel: that is called a taildragger").

Levels: none; every plane has its own steps. Length: one to three minutes. Feedback: the part's animation, the voice reading each step if read-aloud is on. Age fit: the motion and part names suit a 4-year-old; the step text is written for an adult to read aloud. Without read-aloud on, a pre-reader just taps Next.

### 2.4 Design (the paint studio) (04-design.png)

What the child does: a bottom panel with five tabs. **Paint**: preset schemes shown as pictures, two colors, a full color picker, "Surprise me", and Fade (colors melting nose to tail, with sliders). **Draw**: finger painting on the 3D plane with brush, spray can, fill, eraser, undo. **Stickers**: a large library (flames, stars, trophies, race numbers, country flags, shark mouth and more), placed on glowing spots, then resized and turned; a grown-up can add their own image. **Graphics**: racing swooshes and nose panels. **Face**: eye style, where the eyes and smile sit, a close-up editor, and an optional superhero cape. Every change saves and shows up in races and in Sky City.

Teaches: colors and color names (spoken), creative choice, fine motor control (drawing).

Age fit: the preset pictures, stickers and finger painting suit a 4-year-old well. The sliders, close-up editor, fade controls and text hints ("Pick a sticker, then tap a glowing spot or anywhere on the plane. Tap a sticker on the plane to zoom in and adjust it.") are grown-up level.

### 2.5 Take off (free flight)

What the child does: taps Take off. The plane taxis out of the hangar, rolls down the runway, takes off, flies laps around the airport with its real engine sound, and lands when he taps Land. "Fly again" repeats. It is a watch-and-tap show, not steering.

Teaches: the phases of a flight (taxi, takeoff, landing), engine sounds. Length: about a minute or as long as he likes. Age fit: good; passive.

### 2.6 Classic race (06-classic-race.png)

What the child does: taps Race. A setup sheet asks for a race type, a course (or Random), laps (1 to 5, default 2), announcer on or off, and 2 to 8 planes. There are 11 courses, including farm, canyon, snowy mountains, coast, temple ruins, an ocean fleet, **Carrier Launch** (the racers take off from an aircraft carrier) and **Sky City Sprint**. Each has moving scenery (windmills, whales, skiers, ships) and its own rock music.

Barnaby Propwash (Pancho Vuelo in Spanish) opens with a short line naming the racers; Polly Puffwell the blimp calls the play-by-play; rivals banter when they pass each other. Boost rings, lap banners, a photo finish, fireworks, then the winner's win show (2.13). The winner is different every time and the child does not steer. The camera keeps the whole group in view, because the boy cares more about seeing all the planes than about who wins.

Teaches: nothing formal. Length: about 2 to 4 minutes for two laps. Age fit: very good to watch; the setup sheet is text-heavy.

### 2.7 Number race (07-number-race.png; 07b-number-race-new.png shows the new written problem and try-again flow)

What the child does: the first plane picked is his. It starts a little slower than the others. About every 17 to 21 seconds of race time, the race slows almost to a stop, the camera turns to the plane that needs help, and that plane says one short line in its own voice ("Can you help me?"). Polly the blimp then asks the question aloud. A card shows pictures (for example 4 ducks) and three big number buttons. The buttons stay faded and do nothing (except a small wiggle) until the question has been spoken, so he has to listen first. A right answer: chime, "ZOOM!", a boost for his plane, a star on the trail, thanks in the plane's voice. If no one answers, the plane makes a gentle plea at about 15, 40 and 60 seconds ("Hey buddy, I could really use your help!"), never repeating the question and never scolding. A "Hear it again" button repeats the question.

Teaches: counting, numeral recognition, early addition and beyond. There are over 140 things to count (ducks, cookies, helicopters) and over 100 lead-in lines so questions do not feel the same.

Levels (saved; up after three right-first-time answers in a row, down after two misses in a row; each level mixes in the ones below):
1. Count to 3
2. Count to 5
3. Find the number
4. Count to 10
5. Add within 5 (two groups of pictures with a plus sign)
6. Add within 10
7. Add past ten (sums 11 to 15)
8. Take away within 10 (the ones that go fade and float up)
9. The missing number ("3 and how many more make 7?", missing ones drawn as outlines)
10. Counting by twos, fives and tens ("2, 4, 6, what comes next?")
11. The biggest or smallest of three numbers (an elephant or a mouse as the cue)
12. Little story problems read aloud ("Dusty sees three clouds. Two more clouds float by. How many clouds are there now?")

Levels 7 to 12 were added on 2026-10-31 because the boy was "maxing out" the earlier ones.

Wrong answers, as built today: one try per question. A wrong tap ends the question kindly: Polly says why ("That's 4. There are more."), counts along with him while each picture lights up, says the right answer as it lights up, and says the question will come back. No boost and no lost places. The same question returns two or three questions later with answers shuffled. This was added because the boy was tapping every button until one was right.

**Recent change (now live):** the card shows the written problem (for example "2 + 2") above the pictures, and a wrong answer means "try again until right": Polly says "Try again!", the wrong choice fades out, with no answer reveal and no counting out loud for him. This follows the owner's teaching rule for all learning games: never give the answer; when he picks wrong, say why that pick is wrong, grey it out, and let him find the answer from what is left.

Rewards: boosts, stars on the trail, "You got N stars!" on the results card, and usually winning, since a child who keeps answering usually wins. Length: a two-lap race gives roughly 6 to 10 questions. Age fit: levels 1 to 6 match typical age-4 to age-5 math goals. Levels 9 to 12 (missing addend, skip counting, story problems) are typically kindergarten to first-grade work.

### 2.8 Letter Race (English only) (08-letter-race.png)

What the child does: the same race flow as the number race. The asking plane shows a big letter and says its name and sound and the question: "This is B. It sounds like buh. Which word starts with B?" Then it reads each of three pictures as it lights up ("Ball? ... Sun? ... Cat?"). He taps a picture. Right: chime, boost, praise that names the word and letter ("Yes! Ball starts with B!"). Wrong: the reason ("That's sun, it starts with S"), that picture fades, and the question returns later ("We'll see that one again soon!"). A "Say it again" button replays.

Teaches: letter names, letter sounds, initial sounds (phonemic awareness), later lowercase letters, digraphs, ending and middle sounds.

Levels (saved; three right first picks in a row move up, two missed questions in a row move down):
1. First letters (the wrong pictures start with a clearly different kind of sound)
2. Trickier first letters
3. More letters and short vowels, words that start with a blend
4. Sounds that are close (b/p, d/t, m/n, f/v, s/z, k/g as a distractor)
5. Little letters (lowercase)
6. Two letters, one sound (sh, ch, th)
7. Ending sounds
8. Middle sounds

A grown-up setting can show capitals only. Hidden when the game is in Spanish. Age fit: levels 1 to 4 fit a 4-year-old learning letters; 6 to 8 are typical kindergarten and first-grade phonics.

### 2.9 Word race, "Say it!" (09-say-it-word-race.png)

What the child does: a speech-practice race. Every few seconds a card shows a word with its picture. The asking plane says it, the card says "Your turn! Say it!", and he says the word out loud. The phone never listens or judges: a grown-up taps **Good try** (small boost, the word comes back once more) or **Clear!** (star burst, big boost, a step toward the next level). Some cards are a listening pair ("Which one did I say?" with two pictures, English only) or a phrase whose words light up one by one.

Teaches: articulation and speech practice, built so a parent or speech therapist can set the targets. Word sets:
- **F sounds** (9 levels: short words, longer words, F-L and F-R blends, big words, two words, sentences, F in the middle, F at the end, F everywhere; three "Clear!" taps move up a level)
- **Takeoff L** (/l/, often said as w), **Formation** (l-clusters), **Landing** (final sounds that get dropped), **Phrases** (words that run together)
- **My words**: a grown-up types up to 24 words or picks picture words; a practice log records tries and clears per word per day (counts only, no recordings).

Cue badges ("Tongue up for takeoff!", "Land the plane at the end!") tie the speech tip to flying. Words are drawn from shuffle bags so nothing repeats until a set is used up. Age fit: good with a grown-up present; it does not work without one, since a grown-up must tap after each try.

### 2.10 Word Launch (English only) (10-word-launch.png)

What the child does: during the race, his plane hovers in front of a row of 3D rings, one per part of a word ("pro, pel, ler") or one per word of a phrase. He says each part and his plane flies through that ring; then "Now launch it!", he says the whole word and his plane shoots past the others. If the microphone is allowed (on by default where available), a simple loudness detector moves the plane through each ring, and the phone's speech recognizer can check the whole word (this uses Apple's or Google's service; the voice is never saved). Without a microphone, each ring is a big tap target and a grown-up's "Said it!" button judges the whole word. "Try again", "Say it louder!", "Say it again" are available.

Teaches: syllable segmentation and blending, multisyllable words, speech fluency.

Levels (saved; clean launches in a row move up): Two parts, Three parts, Long words, Words and phrases, Sentences, Tricky starts, Giant words, Long sentences. Age fit: clapping syllables is an age-4 skill; levels 5 and up (sentences, giant words) are a stretch.

Note: the owner's stated rule is that no learning game should require a microphone; this mode works without one but defaults to using it when the phone allows.

### 2.11 Control Tower

What the child does: he is the control tower. The planes wait on the start line for a big "Take off!" button (no countdown). He says a command out loud, or taps it: **Stop!** (the planes hang in the air), **Faster!**, **Up!**, **Down!**, **Spin!**. A grown-up taps what he said. The plane he spoke to does it at once and says it back with one word more, in its own voice (a modeled expansion, a speech-therapy technique). When he is quiet for a while, the planes give him a reason to talk: they say they are ready, sink, slow down, or another plane asks for a turn.

Teaches: expressive language, giving commands, turn-taking, action words and opposites (up/down, stop/faster). No levels; a turn count is saved. Age fit: very good; open-ended and silly. Depends on a grown-up for the tapping.

### 2.12 Radio Out (English only)

What the child does: a mission, not a race. His plane's radio is broken; two jets, Echo and Bravo (F/A-18s), escort him home over the sea. They say a sentence and he says it back; each answer flies him through rings on the way to the aircraft carrier, and at the end he lands on the deck with a hook and deck crew. Teaches: sentence repetition, listening. Age fit: a good story frame; long sentences may be hard.

### 2.13 Win shows (11-win-show.png)

Every plane has its own celebration when it wins, written to its personality: for example the Concorde's sonic boom, El Chupacabra's maracas, Fire Dusty's water drop, Windlifter carrying a giant log, Franz turning into a car, Angel joined by five Blue Angels jets, and smoke-trail dances for others. Tapping the plane during a show adds an extra flip.

The **Win show** button in the hangar starts a short solo flight where the current plane finishes and plays its show without a full race, with "Watch again" and "Back to hangar". Age fit: excellent; this is pure delight and a strong reward.

### 2.14 Sky City

What the child does: from the hangar list or the start screen, he opens a watch-only flythrough of a huge futuristic city (towers too tall to see the bottom of, sky lanes of traffic at many speeds). All the planes, plus extra real aircraft, fly through it with faces on, and one of his own painted planes is always on screen. Time of day: night, dusk or day. Synthwave music (upbeat by day, moody at night). No narration and nothing to do but watch; the only controls are a close button, time of day, picture quality and sound. Sky City Sprint is the same city as a race course. Age fit: good for calm watching; no learning.

### 2.15 Story Hangar (05-learn-menu.png shows the Learn menu)

What the child does: a 2D picture-story mode reached from the Learn button. Four stories so far (for example "Dusty and the Red Balloon", "Rochelle's Rainy Day", "The Lost Teddy", "El Chupacabra's Big Race"). Each page is a drawn scene with plane pictures and a short line the narrator reads. Some pages ask a who, what or where question with 2 or 3 picture choices; a wrong tap dims that choice, the narrator repeats the line and the right one glows; if nobody taps, the narrator says the answer. After the last page he retells the story using five icons (who, where, problem, what they did, ending); a grown-up taps a star for each part he tells. From the second retelling, the page pictures are hidden. Teaches: listening comprehension, story structure, retelling. Level: 2 or 3 choices.

Note: this mode and the next are outside the races, which the owner's rule says to avoid.

### 2.16 Hide and Seek

What the child does: one drawn airport with 13 hiding spots, each tied to a position word (under, behind, in front of, next to, between, on, in). Find mode: "Where's Dusty? He's behind the hangar!" He taps the plane or the object. A wrong tap: "Not there. Look behind the hangar!" and the peeking part wiggles; if nobody taps, the answer glows and the plane hops out. A round is 5 finds. Then Tell mode: he drags a plane to a spot and says where it is; a grown-up taps the position word he used, and the narrator models the full sentence. Teaches: spatial concepts and prepositions, an age-3-to-5 language goal.

### 2.17 Learn menu (05-learn-menu.png)

Big cards for every learning mode plus Sky City, each with an icon, a title and a one-line text description.

## 3. Cross-cutting design

**Characters.** 21 aircraft, for example the PZL M-18 Dromader (Dusty) and a floatplane version (Fire Dusty), F4U Corsair (Skipper), P-51D Mustang (Ripslinger), DH.88 Comet (Bulldog), Gee Bee (El Chupacabra), Taylor Aerocar (Franz), two CAP 10s flying as one racer (Ned and Zed), helicopters (Blade Ranger, Windlifter), and the game's own characters: Baby Beluga, the Space Shuttle, Bristles (a kid's block plane), the Concorde and Angel (a Blue Angels Super Hornet). All have faces that blink.

**Voices.** Every plane has its own recorded voice in English and Spanish, pitched to its size, with accents where they fit (British Bulldog, French Rochelle, German Franz). The camera shows the plane from the front while it talks and its mouth moves. Polly the blimp asks the learning questions; Barnaby is the announcer; a narrator reads stories, build steps and menus. Lines without a recording fall back to the phone's own voice.

**Bilingual switch.** EN/ES is always visible at the top and changes everything, including voices, at once. Number race, Word race, Control Tower, Story Hangar and Hide and Seek are bilingual. Letter Race, Word Launch and Radio Out are English only (the owner builds English first, Spanish later). Sky City text is shown but never spoken.

**Anti-mashing rules.** Answer buttons stay asleep until the question has been spoken. Number and letter questions give rewards only for a right first try (number race moving to retry-until-right with no reveal). Missed questions come back later with shuffled answers. Levels drop after two misses in a row, so guessing pushes the game easier.

**Repetition and variety.** Large content pools (140+ counting objects, many lead-ins, shuffle bags for words), questions that return after a miss, retold stories with pictures removed.

**Saves.** Everything saves locally (designs, drawings, uploaded pictures, levels, word lists, practice log, settings). Inside the Claude app, saves also sync to the owner's private storage so the planes look the same on every device. Saves carry over from build to build.

**Parent controls.** Race setup, level pickers for each learning race, the My words editor and practice log, the Good try / Clear! / Said it! buttons, Word Launch microphone settings, volumes, announcer and read-aloud switches. There is no parent lock: the child can reach every setting.

**Sound.** Engine sounds synthesized to match each real engine (radials, inline V12s, jets, rotors), original rock music per course, synthwave in Sky City, chimes and sparkles for right answers, a soft "boing" for bumps (never a crash). Engines go quiet while a question is asked.

**Sessions.** No timers or session limits. A race is 2 to 4 minutes; the child moves freely between hangar, design, races and shows.

## 4. Known weak spots

- **Reading load.** Many screens carry adult-level text: the info card, build step facts, the race setup sheet, the Design hints, Learn menu descriptions, Word Launch settings. Some of it is spoken when read-aloud is on, but much is labels only.
- **Pre-reader stuck points.** The race setup (type, course, laps, announcer, planes) is a text list; the Design tabs and sliders; sticker categories; the results card buttons ("Race again", "Next", "Back to hangar") are text. Without a grown-up, a 4-year-old likely taps at random here.
- **Letter Race cards print the word.** Each picture has its word written under it with the first letter colored (for example "NINJA" under the ninja when the target is N), so a child can match letter shapes instead of listening for the sound.
- **Grown-up dependence.** Word race, Control Tower, Story retell and Hide and Seek Tell mode all need a grown-up to tap after the child speaks. Played alone, these modes stall.
- **Difficulty ceiling vs age.** Number levels 9 to 12 and letter levels 6 to 8 are kindergarten-to-first-grade work. Promotion after three right answers in a row is fast; a child can reach material beyond his age within a few races.
- **The reward is tied to winning.** His plane starts slower and wins by answering, and right answers give boosts. Learning is mostly a means to an extrinsic reward.
- **Feedback rules differ by mode.** Story Hangar and Hide and Seek reveal the answer when he waits or misses; the number race now has him retry until right with no reveal; the letter race ends the question after one miss. This does not yet match the owner's rule of never giving the answer.
- **Talk density.** Announcer, blimp play-by-play, color commentary, banter, pleas and questions all share the audio. Questions every 17 to 21 seconds plus pleas at 15, 40 and 60 seconds may feel like pressure.
- **Microphone.** Word Launch uses the microphone by default where allowed, against the owner's stated "no microphone" rule (it works without one).
- **Spanish gaps.** Three learning modes are English only.
- **Memory and crashes on iPhone.** The game is very heavy for a phone browser: 21 detailed models, per-plane voice packs, scenery and music. Past problems: a test build hit the hosting's 256 MiB limit (2026-10-13); a number race held about 450 MB of decoded speech before being halved (2026-10-26); iPhone has killed the tab for memory, which shows up as the game suddenly reloading. Automatic crash reports were added on 2026-11-01. Loading a race takes noticeable time.
- **Breadth.** There are many modes, tools and options; the dock plus Learn sheet presents about 15 activities. Feature growth has been fast (most of it in October 2026).
- **Side modes.** Story Hangar and Hide and Seek are separate 2D activities, which the owner's rule says to avoid.

## 5. Prompt for the reviewing assistant

Copy everything below this line, together with the write-up above, into the reviewing assistant.

---

You are reviewing a private learning game for one child. Read the write-up above in full; it is the only information you have, so do not assume features it does not describe.

Context: the player is a 4-year-old boy in a bilingual English and Spanish home. He is a pre-reader who is learning letters, letter sounds, counting and early addition. He plays alone or with a parent on an iPhone held upright. He loves planes, cares more about seeing all the planes doing interesting things than about winning, and gets bored when he already knows the answers. His father's design rules: learning should live inside the races, not in side activities that feel like books; the game must never give him the answer (when he picks wrong, say why that pick is wrong, grey it out, and let him find the answer from what is left); no learning game may require a microphone; new learning features are built in English first, then Spanish.

Please give:

1. **Evaluation against established practice.** Compare the game with what early-childhood research and experienced children's media makers recommend for learning games for ages 3 to 5. Draw on, for example: the "four pillars" of learning (active, engaged, meaningful, socially interactive) from Hirsh-Pasek and colleagues; the NAEYC position on developmentally appropriate practice; Sesame Workshop and PBS KIDS guidance on curriculum-driven play and feedback for young children; findings on scaffolding, adaptive difficulty and productive struggle; research on extrinsic rewards; guidance for bilingual learners; and research on joint media engagement (playing together with a parent). Say clearly what the game already does well, and where it departs from practice. Cite the sources you rely on by name and year.
2. **Concrete improvements, ranked by impact for this child.** For each: what to change, why (tie it to evidence or to his age), how it should look and sound on screen, and the rough effort (small, medium, large). Pay attention to the pre-reader stuck points, the difficulty ceiling, feedback after wrong answers, talk density, and what a 4-year-old can do with no grown-up nearby.
3. **New game modes** that fit the planes theme and his age: pre-reader, letters and letter sounds, rhyming and syllables, counting and early addition, shapes and patterns, in both English and Spanish. Prefer modes that live inside racing or flying. For each: a name, what he does step by step, what it teaches, how difficulty grows, how a wrong answer is handled under the never-give-the-answer rule, and why it suits a 4-year-old.
4. **What to cut or simplify.** Name the features, screens, levels or options that add load without helping him learn or enjoy it, and what to replace them with.

Keep the answer practical and specific to this game. Use plain language and no jargon without a short explanation.
