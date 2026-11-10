// Static checks, no browser. Run: node tools/test/check-static.mjs
//  1. the inline script of index.html passes `node --check`
//  2. every file named in vo/index.json exists under vo/
//  3. UI.en and UI.es have the same keys (gaps are WARNINGS, not failures)
import fs from 'fs';
import os from 'os';
import path from 'path';
import { execFileSync } from 'child_process';
import { fileURLToPath } from 'url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const html = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
let failed = 0, warned = 0;
const ok = (m) => console.log('PASS  ' + m);
const bad = (m) => { failed++; console.log('FAIL  ' + m); };
const warn = (m) => { warned++; console.log('WARN  ' + m); };

// ---- 1. the inline script
const blocks = [...html.matchAll(/<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/g)].map((m) => m[1]);
const big = blocks.reduce((a, b) => (b.length > a.length ? b : a), '');
if (!big) bad('no inline script found in index.html');
else {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'hangar-static-'));
  const f = path.join(dir, 'inline.js');
  fs.writeFileSync(f, big);
  try {
    execFileSync(process.execPath, ['--check', f], { stdio: 'pipe' });
    ok(`inline script (${big.split('\n').length} lines, ${(big.length / 1024).toFixed(0)} KB) passes node --check`);
  } catch (e) {
    bad('inline script fails node --check:\n' + String(e.stderr || e.message).split('\n').slice(0, 8).join('\n'));
  }
  fs.rmSync(dir, { recursive: true, force: true });
}

// ---- 2. vo/index.json
try {
  const idx = JSON.parse(fs.readFileSync(path.join(root, 'vo', 'index.json'), 'utf8'));
  const packs = new Set();
  for (const v of Object.values(idx.clips || {})) for (const c of v) packs.add(c[0]);
  const missing = [...packs].filter((p) => !fs.existsSync(path.join(root, 'vo', p + '.mp3')));
  if (missing.length) bad(`vo/index.json names ${missing.length} missing file(s): ${missing.slice(0, 10).join(', ')}${missing.length > 10 ? ' ...' : ''}`);
  else ok(`vo/index.json: ${Object.keys(idx.clips).length} clips, all ${packs.size} pack files exist`);
} catch (e) { bad('vo/index.json unreadable: ' + e.message); }

// ---- 3. UI.en / UI.es keys. A small scanner finds each object literal and reads its top-level keys.
const src = big;
function matchBrace(s, i) {   // s[i] === '{'; returns the index of its closing brace (strings, templates, comments, regexes skipped)
  const stack = [];
  let prev = '';
  for (; i < s.length; i++) {
    const c = s[i];
    if (c === '/' && s[i + 1] === '/') { i = s.indexOf('\n', i); if (i < 0) return -1; continue; }
    if (c === '/' && s[i + 1] === '*') { i = s.indexOf('*/', i) + 1; continue; }
    if (c === '\'' || c === '"') { for (i++; s[i] !== c; i++) if (s[i] === '\\') i++; prev = c; continue; }
    if (c === '`') { i = skipTpl(s, i); prev = c; continue; }
    if (c === '/' && /[(,=:\[!&|?{};]/.test(prev || ';')) { for (i++; s[i] !== '/'; i++) { if (s[i] === '\\') i++; else if (s[i] === '[') { for (i++; s[i] !== ']'; i++) if (s[i] === '\\') i++; } } prev = '/'; continue; }
    if (c === '{') stack.push(c);
    else if (c === '}') { stack.pop(); if (!stack.length) return i; }
    if (!/\s/.test(c)) prev = c;
  }
  return -1;
}
function skipTpl(s, i) {      // s[i] === '`'; returns the index of the closing backtick
  for (i++; s[i] !== '`'; i++) {
    if (s[i] === '\\') i++;
    else if (s[i] === '$' && s[i + 1] === '{') { i = matchBrace(s, i + 1); }
  }
  return i;
}
function topKeys(s, open, close) {   // keys at depth 1 of the literal s[open..close]
  const keys = [];
  let depth = 0, expectKey = true, prev = '';
  for (let i = open; i <= close; i++) {
    const c = s[i];
    if (c === '/' && s[i + 1] === '/') { i = s.indexOf('\n', i); continue; }
    if (c === '/' && s[i + 1] === '*') { i = s.indexOf('*/', i) + 1; continue; }
    if (depth === 1 && expectKey) {
      const m = /^(?:([A-Za-z_$][\w$]*)|'([^']*)'|"([^"]*)")\s*:/.exec(s.slice(i, i + 200));
      if (m) { keys.push(m[1] ?? m[2] ?? m[3]); i += m[0].length - 1; expectKey = false; prev = ':'; continue; }
    }
    if (c === '\'' || c === '"') { for (i++; s[i] !== c; i++) if (s[i] === '\\') i++; prev = c; continue; }
    if (c === '`') { i = skipTpl(s, i); prev = c; continue; }
    if (c === '/' && /[(,=:\[!&|?{};]/.test(prev || ';')) { for (i++; s[i] !== '/'; i++) { if (s[i] === '\\') i++; else if (s[i] === '[') { for (i++; s[i] !== ']'; i++) if (s[i] === '\\') i++; } } prev = '/'; continue; }
    if (c === '{' || c === '[' || c === '(') depth++;
    else if (c === '}' || c === ']' || c === ')') depth--;
    else if (c === ',' && depth === 1) expectKey = true;
    if (!/\s/.test(c)) prev = c;
  }
  return keys;
}
const tables = { en: new Set(), es: new Set() };
const start = src.indexOf('const UI = {');
if (start < 0) bad('could not find "const UI = {" in the inline script');
else {
  const open = src.indexOf('{', start), close = matchBrace(src, open);
  const body = src.slice(open, close + 1);
  for (const L of ['en', 'es']) {
    const m = new RegExp('(^|\\n)  ' + L + ':\\{').exec(body);
    if (!m) { bad('UI.' + L + ' literal not found'); continue; }
    const o = body.indexOf('{', m.index + 1), c = matchBrace(body, o);
    topKeys(body, o, c).forEach((k) => tables[L].add(k));
  }
  let extra = 0;
  for (const m of src.matchAll(/Object\.assign\(\s*UI\.(en|es)\s*,\s*\{/g)) {
    const o = m.index + m[0].length - 1, c = matchBrace(src, o);
    topKeys(src, o, c).forEach((k) => tables[m[1]].add(k)); extra++;
  }
  console.log(`      UI tables: en ${tables.en.size} keys, es ${tables.es.size} keys (${extra} Object.assign additions merged)`);
  if (tables.en.size < 100 || tables.es.size < 100) bad('UI key extraction looks wrong (fewer than 100 keys)');
  else {
    const onlyEn = [...tables.en].filter((k) => !tables.es.has(k)), onlyEs = [...tables.es].filter((k) => !tables.en.has(k));
    if (!onlyEn.length && !onlyEs.length) ok('UI.en and UI.es have the same keys');
    if (onlyEn.length) warn(`${onlyEn.length} key(s) in UI.en but not UI.es (the game falls back to English?): ${onlyEn.join(', ')}`);
    if (onlyEs.length) warn(`${onlyEs.length} key(s) in UI.es but not UI.en: ${onlyEs.join(', ')}`);
  }
}

console.log(`\nstatic: ${failed ? 'FAILED' : 'ok'} (${failed} failure(s), ${warned} warning(s))`);
process.exit(failed ? 1 : 0);
