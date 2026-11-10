// Planes Hangar smoke test. Headless Chromium through Playwright, the game's own ?debug hooks (window.__hangar).
// Run: node tools/test/smoke.mjs        (see tools/test/README.md)
// Exit code 0 = every normal step passed. "KNOWN-FAIL" steps (bugs not fixed yet) are reported but never fail the run.
import http from 'http';
import fs from 'fs';
import path from 'path';
import { createRequire } from 'module';
import { fileURLToPath } from 'url';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const vendor = path.join(root, 'tools', 'test', 'vendor');

// ---------------------------------------------------------------- settings
const T = { boot: 240000, plane: 120000, intro: 240000, results: 300000, card: 300000, settle: 120000, city: 180000 };
const ROUNDS = Math.max(2, +process.env.ROUNDS || 2);   // race round trips; the memory margin looks at the second, more are for measuring
// Allowed growth after two race round trips. Measured (software GL, 2 planes, farm course): the first trip caches the course and the racers' light
// copies, so geometries 68 -> 225..290 and textures 33 -> 56..61 over two trips, then nothing more (287/61 flat on trips 2 to 5). Margin = 1.4 x the worst seen.
const MEM_MARGIN = { geometries: 400, textures: 85 };
const MEM_STEADY = 12;   // with ROUNDS >= 3: geometries a further trip may add once the caches are warm
const SIZE = { width: 405, height: 720 };
const t00 = Date.now();
const secs = () => ((Date.now() - t00) / 1000).toFixed(0).padStart(4) + 's';
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// ---------------------------------------------------------------- static server
const MIME = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.json': 'application/json', '.mp3': 'audio/mpeg', '.webp': 'image/webp', '.jpg': 'image/jpeg', '.png': 'image/png', '.glb': 'model/gltf-binary', '.bin': 'application/octet-stream', '.css': 'text/css', '.hdr': 'application/octet-stream', '.svg': 'image/svg+xml', '.txt': 'text/plain' };
const server = http.createServer((q, s) => {
  let p = decodeURIComponent(q.url.split('?')[0]);
  if (p === '/') p = '/index.html';
  const f = path.join(root, p);
  if (!f.startsWith(root) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { s.writeHead(404); return s.end('not found'); }
  const size = fs.statSync(f).size, type = MIME[path.extname(f)] || 'application/octet-stream';
  const m = /bytes=(\d+)-(\d*)/.exec(q.headers.range || '');
  if (m) { const a = +m[1], b = m[2] ? +m[2] : size - 1; s.writeHead(206, { 'content-type': type, 'accept-ranges': 'bytes', 'content-range': `bytes ${a}-${b}/${size}`, 'content-length': b - a + 1 }); return fs.createReadStream(f, { start: a, end: b }).pipe(s); }
  s.writeHead(200, { 'content-type': type, 'content-length': size, 'accept-ranges': 'bytes' });
  fs.createReadStream(f).pipe(s);
});
await new Promise((r) => server.listen(0, '127.0.0.1', r));
const base = `http://127.0.0.1:${server.address().port}`;

// ---------------------------------------------------------------- the CDN files the page asks for
// A local copy in tools/test/vendor/ is served when it exists; otherwise the request goes to the network (GitHub Actions).
const CDN = [
  [/cdnjs\.cloudflare\.com\/ajax\/libs\/three\.js\/r128\/three\.min\.js/, 'three.min.js'],
  [/cdn\.jsdelivr\.net\/npm\/three@0\.128\.0\/examples\/js\/loaders\/GLTFLoader\.js/, 'GLTFLoader.js'],
  [/cdn\.jsdelivr\.net\/npm\/three@0\.128\.0\/examples\/js\/environments\/RoomEnvironment\.js/, 'RoomEnvironment.js'],
  [/cdn\.jsdelivr\.net\/npm\/three@0\.128\.0\/examples\/js\/geometries\/DecalGeometry\.js/, 'DecalGeometry.js'],
  [/cdn\.jsdelivr\.net\/npm\/three@0\.128\.0\/examples\/js\/objects\/Sky\.js/, 'Sky.js'],
];
const served = new Set(), passed = new Set();
async function routeNetwork(ctx) {
  await ctx.route((u) => u.hostname !== '127.0.0.1', async (route) => {
    const url = route.request().url();
    for (const [re, name] of CDN) {
      const f = path.join(vendor, name);
      if (re.test(url) && fs.existsSync(f)) { served.add(name); return route.fulfill({ path: f, contentType: 'application/javascript' }); }
    }
    if (/fonts\.googleapis\.com/.test(url)) return route.fulfill({ body: '/* fonts skipped in tests */', contentType: 'text/css' });   // cosmetic only
    passed.add(new URL(url).hostname);
    return route.continue();
  });
}

// ---------------------------------------------------------------- results bookkeeping
const log = [];
let cur = null;   // the step now running: {name, errors: []}
function record(name, status, ms, detail) {
  log.push({ name, status, ms, detail });
  const tag = { pass: 'PASS      ', fail: 'FAIL      ', known: 'KNOWN-FAIL', xpass: 'XPASS     ' }[status];
  console.log(`${secs()}  ${tag} ${name} (${(ms / 1000).toFixed(1)}s)${detail ? '\n          ' + String(detail).split('\n').join('\n          ') : ''}`);
}
// known: a bug that is not fixed yet. It reports but does not fail the run. TODO: when the bug is fixed the step turns XPASS; remove `known` then.
const ONLY = process.env.ONLY ? new RegExp(process.env.ONLY, 'i') : null;   // ONLY='REGRESSION \\(c' runs the steps whose name matches (the main-page steps need the earlier ones)
async function step(name, fn, known) {
  if (ONLY && !ONLY.test(name)) return;
  const t0 = Date.now(); cur = { name, errors: [] };
  let err = null;
  try { await fn(); } catch (e) { err = e; }
  const errs = cur.errors; cur = null;
  const problems = [];
  if (err) problems.push(String((err && err.message) || err).split('\n').slice(0, 6).join('\n'));
  if (errs.length) problems.push('page errors during this step:\n' + errs.slice(0, 5).join('\n'));
  const ms = Date.now() - t0;
  if (known) {
    if (problems.length) record(name, 'known', ms, 'TODO(' + known + '): ' + problems.join('\n'));
    else record(name, 'xpass', ms, 'TODO(' + known + '): this passed, the bug looks fixed. Remove the known-failing flag.');
  } else if (problems.length) record(name, 'fail', ms, problems.join('\n'));
  else record(name, 'pass', ms);
}

// ---------------------------------------------------------------- a game session
let browser;
async function boot(label) {
  const ctx = await browser.newContext({ viewport: SIZE, hasTouch: true, isMobile: true, serviceWorkers: 'block' });
  await routeNetwork(ctx);
  const page = await ctx.newPage(); let navs = 0;
  const sink = (m) => { if (cur) cur.errors.push(m); else strayErrors.push(m); };
  page.on('pageerror', (e) => sink('pageerror: ' + e.message));
  page.on('console', (m) => { if (m.type() === 'error') sink('console.error: ' + m.text().slice(0, 300)); });
  page.on('load', () => { if (navs++ > 0) sink('the page reloaded itself (lost graphics context?)'); });   // pushState navigation does not fire load
  page.on('crash', () => sink('page crashed'));
  await page.addInitScript(() => { window.__nopace = true; });   // the game's own switch: no frame pacing
  await page.goto(`${base}/index.html?debug`, { timeout: T.boot });
  await page.waitForFunction(() => window.__hangar && window.__hangar.state().ready, null, { timeout: T.boot });
  return page;
}
const strayErrors = [];
const H = (page, fn, arg) => page.evaluate(fn, arg);
const state = (p) => H(p, () => window.__hangar.state());
const mem = (p) => H(p, () => { const m = window.__hangar.twinEval((c) => c.renderer.info.memory); return { geometries: m.geometries, textures: m.textures }; });
const errNote = (p) => H(p, () => { const e = document.getElementById('errNote'); return e && !e.hidden ? e.textContent : ''; });
async function noBanner(p, where) { const t = await errNote(p); if (t) throw new Error(`error banner #errNote after ${where}: ${t}`); }

// The hangar is back: ready, a plane shown, no race, no loading card, no results card, no editor.
async function saneHangar(p, where, timeout = T.settle) {
  try {
    await p.waitForFunction(() => {
      const s = window.__hangar.state(), r = window.__hangar.raceInfo();
      return s.ready && !r.on && !s.race && !s.editor && document.getElementById('loading').hidden && document.getElementById('rhud').hidden && document.getElementById('city').hidden && (s.mode === 'home' || s.mode === 'field' || s.mode === 'build');
    }, null, { timeout });
  } catch (e) {
    const d = await H(p, () => ({ s: window.__hangar.state(), r: window.__hangar.raceInfo(), loading: !document.getElementById('loading').hidden, results: !document.getElementById('rResults').hidden, hud: !document.getElementById('rhud').hidden, city: !document.getElementById('city').hidden, racers: window.__hangar.racers().length }));
    throw new Error(`hangar not sane after ${where}: ${JSON.stringify(d)}`);
  }
  await noBanner(p, where);
}

async function loadPlane(p, i) {
  const id = await H(p, (i) => window.__hangar.load(i), i);
  await p.waitForFunction((id) => { const s = window.__hangar.state(); return s.ready && s.model === id; }, id, { timeout: T.plane });
  return id;
}

// classic or other race: start, skip the intro, put every racer a little short of the line, wait for the results card
async function raceToResults(p, ids, course, type, dt = 0.5) {
  await H(p, ([ids, course, type, dt]) => { window.__hangar.setMaxDt(dt); window.__hangar.startRaceWith(ids, course, type); }, [ids, course, type, dt]);
  await p.waitForFunction(() => window.__hangar.state().race === 'intro', null, { timeout: T.intro });
  await H(p, () => window.__hangar.raceGo());
  await H(p, () => window.__hangar.twinEval((c) => c.RACE.racers.forEach((r) => { const dd = r.D - 40 - r.d; r.boostT += dd; r.boost += dd; })));   // same as the racerPut hook
  // the finish and the results phase happen by themselves; the winner's cheer and win routine hold the card for 12+ s of wall time, so skip that wait
  await p.waitForFunction(() => window.__hangar.state().race === 'results', null, { timeout: T.results });
  await H(p, () => window.__hangar.twinEval((c) => { c.RACE.winEnd = 0; c.RACE.winCap = 0; }));
  await p.waitForFunction(() => !document.getElementById('rResults').hidden, null, { timeout: T.card });
  const r = await H(p, () => ({ info: window.__hangar.raceInfo(), n: window.__hangar.racers().length, rows: document.querySelectorAll('#rResList li').length }));
  if (r.info.phase !== 'results' || !r.n || r.rows !== r.n) throw new Error('results card looks wrong: ' + JSON.stringify(r));
}
const click = (p, id) => H(p, (id) => { document.getElementById(id).click(); }, id);

// ================================================================ the run
const wall0 = Date.now();
browser = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--no-sandbox'] });
let page = null, ids = [], base0 = null, afterRound = [];

await step('boot: index.html?debug loads, hangar ready, no errors', async () => {
  page = await boot('main');
  const s = await state(page);
  if (!s.model) throw new Error('no plane loaded');
  await noBanner(page, 'boot');
  ids = await H(page, () => window.__hangar.soloInfo().ids);
  if (!ids || ids.length < 4) throw new Error('plane list looks wrong: ' + JSON.stringify(ids));
});
if (!page && !ONLY) { console.log('cannot continue without a booted page'); await browser.close(); server.close(); process.exit(1); }
console.log(`        CDN files: ${served.size ? 'local copies from tools/test/vendor (' + [...served].join(', ') + ')' : 'none local, network used'}`);

await step('hangar: memory baseline', async () => {
  await sleep(1500);
  base0 = await mem(page);
  console.log(`          baseline renderer.info.memory: ${JSON.stringify(base0)}`);
});

await step('planes: switch three times', async () => {
  const first = (await state(page)).model;
  for (const i of [1, 2, 0]) {
    const id = await loadPlane(page, i);
    await noBanner(page, 'loading ' + id);
    if (id === first && i !== 0) throw new Error('same plane came back');
  }
  await saneHangar(page, 'plane switching');
});

await step('build: step through ruler steps and back', async () => {
  const n = await H(page, () => document.querySelectorAll('#ruler button').length);
  if (n < 3) throw new Error('ruler has ' + n + ' steps');
  for (const k of [2, 0, Math.min(4, n - 1), 0, n - 1]) {   // ends on the last (flight) step: the hangar's home screen
    await H(page, (k) => document.querySelectorAll('#ruler button')[k].click(), k);
    await page.waitForFunction((k) => window.__hangar.state().step === k, k, { timeout: 15000 });
    await sleep(500);
  }
  await noBanner(page, 'build steps');
  await saneHangar(page, 'build steps');
});

await step('studio: open paint, drawing, stickers, close', async () => {
  await click(page, 'designBtn');
  await page.waitForFunction(() => !document.getElementById('studio').hidden, null, { timeout: 15000 });
  for (const tab of ['draw', 'stick', 'paint']) {
    await click(page, 'tab-' + tab);
    await page.waitForFunction((t) => document.getElementById('pane-' + t) && !document.getElementById('pane-' + t).hidden, tab, { timeout: 15000 });
    await sleep(400);
  }
  await click(page, 'studioDone');
  await page.waitForFunction(() => document.getElementById('studio').hidden, null, { timeout: 15000 });
  await saneHangar(page, 'studio');
});

await step('sky city: open, run a few frames, close', async () => {
  await H(page, () => window.__hangar.cityOpen());
  await page.waitForFunction(() => { const c = window.__hangar.city(); return c.on && c.ready && c.frames > 5; }, null, { timeout: T.city });
  await sleep(1500);
  await noBanner(page, 'Sky City open');
  await click(page, 'cityClose');
  await saneHangar(page, 'Sky City');
});

for (let round = 1; round <= ROUNDS; round++) {
  await step(`classic race round trip ${round}: start, results card, Back to hangar`, async () => {
    const racers = ids.slice(0, 2);
    await raceToResults(page, racers, 0, 'classic');
    await click(page, 'rExit');
    await saneHangar(page, 'classic race');
    await sleep(1000);
    afterRound.push(await mem(page));
    console.log(`          memory after round trip ${round}: ${JSON.stringify(afterRound[round - 1])}`);
  });
}

await step('memory: growth after two race round trips is within the margin', async () => {
  const end = afterRound[1] || afterRound[0];
  if (!base0 || !end) throw new Error('no measurements');
  const d = { geometries: end.geometries - base0.geometries, textures: end.textures - base0.textures };
  console.log(`          before ${JSON.stringify(base0)}  after ${JSON.stringify(end)}  growth ${JSON.stringify(d)}  margin ${JSON.stringify(MEM_MARGIN)}`);
  if (afterRound[1]) console.log(`          growth in round trip 2 alone: geometries ${afterRound[1].geometries - afterRound[0].geometries}, textures ${afterRound[1].textures - afterRound[0].textures}`);
  for (const k of ['geometries', 'textures']) if (d[k] > MEM_MARGIN[k]) throw new Error(`${k} grew by ${d[k]} (margin ${MEM_MARGIN[k]})`);
  if (afterRound.length >= 3) {
    const g = afterRound[afterRound.length - 1].geometries - afterRound[1].geometries;
    console.log(`          growth from trip 2 to trip ${afterRound.length}: geometries ${g}`);
    if (g > MEM_STEADY * (afterRound.length - 2)) throw new Error(`geometries keep growing after the caches are warm: +${g} over ${afterRound.length - 2} more trips`);
  }
});

await step('letter race: start, answer one question, leave with the X', async () => {
  await H(page, ([a, b]) => { window.__hangar.setMaxDt(0.3); window.__hangar.startRaceWith([a, b], 0, 'letters'); }, ids.slice(0, 2));
  await page.waitForFunction(() => window.__hangar.state().race === 'intro', null, { timeout: T.intro });
  await H(page, () => window.__hangar.raceGo());
  await page.waitForFunction(() => { const q = window.__hangar.learn().q; return q && document.querySelectorAll('#rqAns button').length > 0; }, null, { timeout: T.results });
  // the answers stay asleep ('wait') until the question has been read out
  await page.waitForFunction(() => !document.getElementById('rqAns').classList.contains('wait'), null, { timeout: T.results });
  const before = await H(page, () => window.__hangar.lrnState());
  if (!before) throw new Error('no letter question state');
  await H(page, () => { const b = [...document.querySelectorAll('#rqAns button')].find((x) => !x.disabled); b.click(); });
  await sleep(1500);
  const after = await H(page, () => ({ l: window.__hangar.learn(), st: window.__hangar.lrnState() }));
  const answered = !after.l.q || after.l.q.done || (after.st && (after.st.done || after.st.stage !== before.stage)) || after.l.stars > 0 || after.l.helped.length > 0 || (after.l.q && after.l.q.tries > 0);
  if (!answered) throw new Error('the answer click changed nothing: ' + JSON.stringify({ before, after }));
  await noBanner(page, 'letter answer');
  await click(page, 'rQuit');
  await saneHangar(page, 'leaving the Letter Race');
});

// ---------------------------------------------------------------- known bugs. (a) breaks the page, so it runs last on the main page
// (b) results narration fires 2.6 s later over the next screen (index.html showResults, about line 10949: setTimeout(say(...), 2600) is never cancelled)
await step('REGRESSION (b): results narration does not fire after leaving the card', async () => {
  const p = page;
  await H(p, () => { const b = document.getElementById('speak'); if (b && b.getAttribute('aria-pressed') === 'false') b.click(); });   // Read aloud on
  await raceToResults(p, ids.slice(0, 2), 0, 'classic');
  await click(p, 'rExit');
  const tExit = await H(p, () => window.__hangar.now());
  await sleep(3600);
  const late = await H(p, (t) => window.__hangar.said(t), tExit);
  const heard = late.filter((x) => [].concat(x.u).some((u) => /^\s*\d+\S*,/.test(String(u))));   // the standings read out: "1st, Fire Dusty."
  if (heard.length) throw new Error(`results narration spoke ${heard.length} line(s) after Back to the hangar: ${JSON.stringify(heard.slice(0, 2))}`);
}, 'cancel the 2600 ms timer in showResults when the card closes');


// (a) results card: Next then Back while the next course builds leaves RACE.on true with zero racers (index.html raceAgain0, about lines 11203 to 11209)
//     the Back here is the race's X (#rQuit): the results card is hidden while the course builds
await step('REGRESSION (a): results Next then Back while the course builds', async () => {
  const p = page;   // last user of the main page: the bug leaves it broken
  await raceToResults(p, ids.slice(0, 2), 0, 'classic');
  await click(p, 'rNext');
  await p.waitForFunction(() => !document.getElementById('loading').hidden, null, { timeout: 15000 });
  await click(p, 'rQuit');
  // let the build finish whatever it does, then look
  await p.waitForFunction(() => document.getElementById('loading').hidden, null, { timeout: T.settle }).catch(() => {});
  await sleep(6000);
  const r = await H(p, () => ({ on: window.__hangar.raceInfo().on, n: window.__hangar.racers().length, phase: window.__hangar.raceInfo().phase }));
  if (r.on && r.n === 0) throw new Error('RACE.on is true with zero racers: ' + JSON.stringify(r));
  await saneHangar(p, 'Next then Back', 60000);
}, 'raceAgain0 awaits buildCourse and then startRaceRun even though endRace ran');

await browser.close();
server.close();

// ---------------------------------------------------------------- summary
const count = (s) => log.filter((x) => x.status === s).length;
console.log('\n================ summary ================');
for (const x of log) console.log(`${{ pass: 'PASS      ', fail: 'FAIL      ', known: 'KNOWN-FAIL', xpass: 'XPASS     ' }[x.status]} ${x.name}`);
if (strayErrors.length) console.log(`\nnote: ${strayErrors.length} page error(s) outside any step: ${strayErrors.slice(0, 3).join(' | ')}`);
if (passed.size) console.log(`note: requests passed through to the network: ${[...passed].join(', ')}`);
console.log(`\n${count('pass')} passed, ${count('fail')} failed, ${count('known')} known-failing, ${count('xpass')} unexpectedly passing (total ${((Date.now() - wall0) / 1000).toFixed(0)} s)`);
process.exit(count('fail') || strayErrors.length ? 1 : 0);
