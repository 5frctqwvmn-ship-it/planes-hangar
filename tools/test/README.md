# Planes Hangar tests

No game file is touched by these. Three tools, all plain Node (20 or newer).

    npm install                 # once: installs Playwright
    npx playwright install chromium   # once, unless a Chromium is already there
    npm run test:static         # a second, no browser
    npm run test:smoke          # about 6 to 8 minutes with software WebGL

## check-static.mjs (no browser)

- the inline script in `index.html` passes `node --check`
- every pack file named in `vo/index.json` exists in `vo/`
- `UI.en` and `UI.es` have the same keys (gaps are warnings, not failures: today the Word Launch and Radio Out strings are English only on purpose)

## smoke.mjs (headless Chromium, the game's `?debug` hooks in `window.__hangar`)

Fails on any `pageerror`, any `console.error`, any text in the game's `#errNote` banner, a page that reloads itself (lost graphics context), or a mode that does not return to a sane hangar (plane ready, `RACE.on` false, no loading card, no race HUD, no city).

Steps: boot, memory baseline, switch planes three times, step through the build ruler, open and close the paint, drawing and sticker studio, open and close Sky City, two classic race round trips (start, results card, Back), a memory check, a Letter Race (answer one question, leave with the X), then the known-failing regressions.

- Memory: `renderer.info.memory` (geometries, textures) in the hangar at the start and after two round trips. The margin is in `MEM_MARGIN` at the top of the file, with what was measured next to it. `ROUNDS=5 npm run test:smoke` runs more trips and also checks that growth stops once the caches are warm.
- KNOWN-FAIL steps are bugs not fixed yet. They report but never fail the run. When one is fixed it prints XPASS: remove its `known` argument (the last argument of `step(...)`) so it guards the fix. Today: (a) results Next then Back while the next course builds leaves `RACE.on` true with zero racers; (b) the results narration timer (2.6 s) fires over the next screen.
- `ONLY="regex" npm run test:smoke` runs just the steps whose name matches (steps that need the main page need the earlier ones).
- Not covered: sound output, real touch and drag, the Say it, Word Launch, Radio Out, Control Tower and hide-and-seek games, Spanish, cloud save.

### The CDNs

The page loads three.js r128 and four examples from cdnjs and jsDelivr. The test routes those requests: a copy in `tools/test/vendor/` (`three.min.js`, `GLTFLoader.js`, `RoomEnvironment.js`, `DecalGeometry.js`, `Sky.js`, all three.js r128) is served if present, otherwise the request goes to the network. GitHub Actions reaches the CDNs, so the folder is git-ignored and not needed there. Google Fonts is answered with an empty stylesheet. Frame pacing is switched off with the game's own `window.__nopace`.
