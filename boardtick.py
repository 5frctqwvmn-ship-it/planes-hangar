import sys, time, json, os, datetime, re
sys.path.insert(0, '/home/claude')
from agtok import tok
D = '/tmp/claude-0/-home-claude/917e4d6d-feb4-59ad-982a-2757f59bd3a4/tasks/'
ME = '/root/.claude/projects/-home-claude/917e4d6d-feb4-59ad-982a-2757f59bd3a4.jsonl'
SKIP_ME = {'ArtifactData', 'Monitor', 'TaskStop', 'ToolSearch'}
last_tok, seen, lastxt = {}, {}, {}
start = time.time() - 30
BASE = 1793571840000   # 4:24 PM Nov 1, when MJ's usage page read 89%
def wsum(us):
    """weighted token total over usage dicts that are already one-per-message"""
    t = [0, 0, 0, 0]
    for u in us:
        t[0] += u.get('input_tokens', 0) or 0; t[1] += u.get('output_tokens', 0) or 0; t[2] += u.get('cache_creation_input_tokens', 0) or 0; t[3] += u.get('cache_read_input_tokens', 0) or 0
    return round(t[0] + 1.25 * t[2] + .1 * t[3] + 5 * t[1]), t
def tokd(path, since=0):
    """weighted tokens of a transcript, counting each message id once (a transcript repeats one message's usage on every line)"""
    best = {}
    try:
        for l in open(path):
            try: d = json.loads(l)
            except Exception: continue
            m = d.get('message')
            if not isinstance(m, dict) or m.get('role') != 'assistant' or not isinstance(m.get('usage'), dict): continue
            if since and ts(d.get('timestamp', '')) < since: continue
            k = m.get('id') or d.get('uuid'); o = m['usage'].get('output_tokens', 0) or 0
            if k not in best or o >= best[k][0]: best[k] = (o, m['usage'])
    except FileNotFoundError: return None
    return wsum(u for _, u in best.values())[0]
def mytok(): return tokd(ME, BASE) or 0

def ts(s):
    try: return int(datetime.datetime.fromisoformat(s.replace('Z', '+00:00')).timestamp() * 1000)
    except Exception: return 0

def kindof(name, i):
    # which crew member does this step: think, read, write, shell, film, render, draw, git, talk, publish
    if name in ('Read', 'Grep', 'Glob'): return 'read'
    if name in ('Write', 'Edit'): return 'write'
    if name in ('SendMessage', 'SendUserMessage', 'SendUserFile'): return 'talk'
    if name in ('Artifact', 'ArtifactData'): return 'publish'
    if name == 'Agent': return 'talk'
    if name in ('Monitor', 'TaskOutput'): return 'wait'
    if name == 'Bash':
        c = str(i.get('command', ''))
        if 'ffmpeg' in c: return 'render'
        if 'playwright' in c or '.mjs' in c or 'node ' in c: return 'film'
        if 'git ' in c: return 'git'
        if 'python' in c and ('PIL' in c or '.py' in c): return 'draw'
        return 'shell'
    return 'shell'

def label(name, i):
    d = i.get('description') or i.get('summary') or ''
    if d: return d
    if name in ('Read', 'Edit', 'Write'): return f"{ {'Read':'Reading','Edit':'Editing','Write':'Writing'}[name] } {os.path.basename(i.get('file_path',''))}"
    if name == 'Bash':
        full = str(i.get('command',''))
        k = kindof(name, i)
        if k == 'film': return 'Filming the game in the test browser'
        if k == 'render':
            m = re.search(r'([\w-]+)\.mp4', full)
            return 'Encoding video' + (f' {m.group(1)}' if m else '')
        if k == 'draw':
            m = re.search(r'([\w-]+)\.py', full)
            return 'Drawing frames' + (f' with {m.group(1)}' if m else '')
        if k == 'git': return 'Saving work to git'
        c = full.strip().split('\n')[-1]
        return 'Running: ' + c[:60]
    if name == 'Grep': return f"Searching for {str(i.get('pattern',''))[:30]}"
    if name == 'Glob': return 'Listing files'
    if name == 'Artifact': return f"Artifact {i.get('action','publish')}"
    return name

def actions(path, key, rmap):
    out = []
    try:
        with open(path) as f:
            f.seek(seen.get(key, 0)); data = f.read(); seen[key] = f.tell()
    except FileNotFoundError: return out
    for l in data.splitlines():
        try: d = json.loads(l)
        except Exception: continue
        m = d.get('message')
        if not isinstance(m, dict) or m.get('role') != 'assistant': continue
        t = ts(d.get('timestamp', ''))
        if t < start * 1000: continue
        for b in m.get('content') or []:
            if not isinstance(b, dict) or b.get('type') != 'tool_use': continue
            n, i = b.get('name'), b.get('input') or {}
            if key == 'claude' and n in SKIP_ME: continue
            if n == 'SendMessage':
                to = rmap.get(str(i.get('to', '')), str(i.get('to', ''))[:12])
                out.append({'t': t, 'type': 'msg', 'id': to, 'text': (i.get('summary') or str(i.get('message', ''))[:80])[:90]})
            elif n == 'Agent':
                out.append({'t': t, 'type': 'act', 'id': key, 'text': 'Briefing a new agent: ' + str(i.get('description', ''))[:60]})
            else:
                out.append({'t': t, 'type': 'act', 'id': key, 'tool': n, 'kind': kindof(n, i), 'text': label(n, i)[:90]})
    # collapse repeats, keep the latest 3
    ded = []
    for e in out:
        if ded and ded[-1]['text'] == e['text'] and ded[-1]['id'] == e['id']: ded[-1] = e
        else: ded.append(e)
    return ded[-3:]


# ---- in-flight steps, command history, turn ends (A, B, C) ----
STATE_F = '/home/claude/board-feed-state.json'
TR = {}          # board id -> tracker
ER = {}          # board id -> time (ms) of the latest report/done/stop the orchestrator logged for it
INFLIGHT_SKIP = {'SendMessage', 'SendUserMessage', 'SendUserFile', 'Agent', 'ArtifactData', 'ToolSearch', 'TaskStop', 'ReadNotifications'}
def _newtr(): return {'off': 0, 'pend': {}, 'hist': [], 'mid': None, 'end': False, 'lastts': 0, 'grow': time.time(), 'size': -1, 'busy': None}
WAITRE = re.compile(r'\buntil\b|\bsleep\s+\d{2,}|while\b[^;]*\bsleep|inotifywait|tail\s+-f|\bwait\b\s+\$|\bwatch\s')
def live_text(n, i):
    k = kindof(n, i)
    if n == 'Bash' and WAITRE.search(str(i.get('command', ''))):
        d = i.get('description') or ''
        return 'wait', (d if d else 'Waiting for the command to finish')[:90]
    if n == 'Monitor': return 'wait', (i.get('description') or 'Waiting on a monitor')[:90]
    return k, label(n, i)[:90]
GENERIC = {'/home/claude', '/home/claude/wt-out', '/home/claude/wt', '/tmp', '/root', '/usr', '/opt'}
def cmd_tokens(c):
    out = set()
    for pth in re.findall(r'(?:/[\w.@+~-]+){3,}', c):
        pth = pth.rstrip('/.')
        if pth in GENERIC or pth.startswith(('/usr/', '/bin/', '/dev/', '/proc/', '/etc/', '/opt/node-tools', '/root/.', '/tmp/claude-0/-home-claude')) and pth.count('/') < 6: continue
        if pth.startswith('/home/claude/') and pth.count('/') < 4: continue
        out.add(pth)
    for f in re.findall(r'[\w][\w.-]{3,}\.(?:js|mjs|cjs|py|sh|mp4|webm|html|json|txt|log|ts|wav|mp3)\b', c):
        if f not in ('index.html', 'package.json', 'shot.js'): out.add(f)
    return out
def _walk_reports(o, t):
    if isinstance(o, dict):
        if o.get('type') in ('report', 'done', 'stop') and o.get('id'): ER[str(o['id'])] = max(ER.get(str(o['id']), 0), int(o.get('t') or t))
        for v in o.values(): _walk_reports(v, t)
    elif isinstance(o, list):
        for v in o: _walk_reports(v, t)
def track(path, key):
    T = TR.setdefault(key, _newtr())
    try:
        sz = os.path.getsize(path)
        if sz < T['off']: T.update(_newtr())
        with open(path, 'rb') as f: f.seek(T['off']); data = f.read()
    except OSError: return T
    if sz != T['size']:
        T['size'] = sz
        try: T['grow'] = os.path.getmtime(path)
        except OSError: pass
    n = data.rfind(b'\n')
    if n < 0: return T
    T['off'] += n + 1
    for l in data[:n].splitlines():
        try: d = json.loads(l)
        except Exception: continue
        m = d.get('message')
        if not isinstance(m, dict): continue
        t = ts(d.get('timestamp', '')) or int(time.time() * 1000); bl = m.get('content') if isinstance(m.get('content'), list) else []
        if m.get('role') == 'assistant':
            mid = m.get('id') or d.get('uuid')
            if mid != T['mid']:   # a new assistant message means every earlier step has returned or was cut off
                T['pend'] = {k: v for k, v in T['pend'].items() if v['mid'] == mid}; T['mid'] = mid
            T['end'] = m.get('stop_reason') == 'end_turn'; T['lastts'] = max(T['lastts'], t)
            if T['end']: T['busy'] = None   # final reply of the turn closes the orchestrator-busy window
            for b in bl:
                if not isinstance(b, dict) or b.get('type') != 'tool_use': continue
                nm, i = b.get('name'), b.get('input') or {}
                if key == 'claude' and nm == 'ArtifactData': _walk_reports(i, t)
                if nm in INFLIGHT_SKIP or (nm == 'Bash' and i.get('run_in_background')): 
                    if nm == 'Bash': T['hist'].append({'id': b.get('id'), 's': t / 1000, 'e': t / 1000, 'tok': cmd_tokens(str(i.get('command', '')))})
                    continue
                kd, tx = live_text(nm, i)
                T['pend'][b.get('id')] = {'mid': mid, 'name': nm, 'kind': kd, 'text': tx, 'since': t}
                if nm == 'Bash': T['hist'].append({'id': b.get('id'), 's': t / 1000, 'e': None, 'tok': cmd_tokens(str(i.get('command', '')))})
        elif m.get('role') == 'user':
            T['end'] = False; T['lastts'] = max(T['lastts'], t); got = False
            for b in bl:
                if isinstance(b, dict) and b.get('type') == 'tool_result':
                    got = True; T['pend'].pop(b.get('tool_use_id'), None)
                    for h in T['hist']:
                        if h['id'] == b.get('tool_use_id') and h['e'] is None: h['e'] = t / 1000
            if not got: T['pend'].clear()   # a fresh prompt: anything unanswered was interrupted
            if key == 'claude' and not got and not d.get('isMeta') and not d.get('isSidechain') and (d.get('origin') or {}).get('kind') == 'human':
                T['busy'] = t   # a real user message opens the busy window
    nw = time.time()
    T['hist'] = [h for h in T['hist'] if (h['e'] or nw) > nw - 3600][-80:]
    for k in [k for k, v in T['pend'].items() if v['since'] < (nw - 10800) * 1000]: del T['pend'][k]
    return T

def live_steps(key):
    T = TR.get(key)
    if not T: return []
    st = [{'kind': v['kind'], 'text': v['text'], 'since': v['since'], 'tool': v['name']} for v in sorted(T['pend'].values(), key=lambda v: v['since'])][-4:]
    if key == 'claude' and T.get('busy') and not T['end']:
        # open until the final end_turn message, or no pending tool and no new transcript line for 90 s (hard cap 3 h)
        if time.time() * 1000 - T['busy'] < 10800000 and (T['pend'] or time.time() - T['lastts'] / 1000 < 90):
            st = [{'kind': 'think', 'text': 'Working on your request', 'since': T['busy'], 'tool': 'Model'}] + st[-3:]
    return st
LV = {}
def live_events(keys, nowm):
    out = []
    for k in list(dict.fromkeys(list(keys) + list(LV))):
        st = live_steps(k); sig = json.dumps(st, sort_keys=True); pv = LV.get(k)
        if (pv is None and not st): continue
        if pv is None or pv['sig'] != sig or (st and nowm - pv['t'] >= 30):
            LV[k] = {'sig': sig, 't': nowm}; out.append({'t': int(nowm * 1000), 'type': 'live', 'id': k, 'steps': st})
    return out

# ---- auto-finish (C) ----
AR = {}; PREV = []
try:
    _st = json.load(open(STATE_F)); AR = _st.get('ar', {}); PREV = _st.get('prev', [])
except Exception: pass
def save_state():
    try: json.dump({'ar': AR, 'prev': PREV}, open(STATE_F + '.tmp', 'w')); os.replace(STATE_F + '.tmp', STATE_F)
    except Exception: pass
def autofinish(rows, nowm):
    global PREV
    out = []; cur = [[b, a] for b, a in rows if b != 'radio']; ch = False
    for b, a in cur:
        T = TR.get(b)
        if not T or not T['lastts']: continue
        k = b + ' ' + a; st = AR.get(k)
        if st:
            if T['lastts'] > st['ts'] + 1000 and not T['end']:   # it got another message and is working again
                del AR[k]; ch = True; out.append({'t': int(nowm * 1000), 'type': 'resume', 'id': b, 'text': 'Back at work'})
            continue
        if (T['end'] and not T['pend']) or (not T['pend'] and nowm - T['grow'] >= 180):
            AR[k] = {'ts': T['lastts']}; ch = True
            if ER.get(b, 0) < T['lastts'] - 120000:   # the orchestrator has not reported it
                out.append({'t': int(nowm * 1000), 'type': 'report', 'id': b, 'tokens': tokd(D + a + '.output') or 0, 'text': 'Finished'})
            T['pend'].clear()
    for b, a in PREV:   # dropped from board-running.txt
        if [b, a] in cur or b == 'radio': continue
        k = b + ' ' + a; T = TR.get(b)
        if k in AR: continue
        AR[k] = {'ts': (T or {}).get('lastts', 0)}; ch = True
        if ER.get(b, 0) < ((T or {}).get('lastts', 0) or 1) - 120000 or not T:
            out.append({'t': int(nowm * 1000), 'type': 'report', 'id': b, 'tokens': tokd(D + a + '.output') or 0, 'text': 'Finished'})
        if T: T['pend'].clear()
    if cur != PREV: PREV = cur; ch = True
    if ch: save_state()
    return out

# ---- cumulative stats ----
SF = '/home/claude/board-stats.json'
ACC = {'base': BASE, 'ts': 0, 'cs': {}, 'm': {'cs': 0, 'pc': 0, 'pm': 0}}
try:
    _a = json.load(open(SF))
    if _a.get('base') == BASE: ACC = _a
except Exception: pass
SC = {}; SOFF = {}
def scan(path, key, since=0):
    c = SC.setdefault(key, {'c': 0, 'tl': {}, 'ti': 0, 'to': 0, 'tw': 0, 'tr': 0, 'ids': set(), 'bid': set(), 'mw': {}, 'mu': {}})
    try:
        with open(path, 'rb') as f:
            f.seek(SOFF.get(key, 0)); data = f.read()
    except FileNotFoundError: return
    n = data.rfind(b'\n')
    if n < 0: return
    SOFF[key] = SOFF.get(key, 0) + n + 1
    for l in data[:n].splitlines():
        try: d = json.loads(l)
        except Exception: continue
        m = d.get('message')
        if not isinstance(m, dict) or (since and ts(d.get('timestamp', '')) < since): continue
        u = m.get('usage')
        mw = None
        if u and m.get('role') == 'assistant':
            mw = c['mw'].setdefault(m.get('id') or d.get('uuid'), [0, set(), -1])
            mu = c['mu'].get(m.get('id') or d.get('uuid'))
            if mu is None: c['mu'][m.get('id') or d.get('uuid')] = [m.get('model') or '', u, mw[1]]
            elif u.get('output_tokens', 0) >= mu[1].get('output_tokens', 0): mu[0], mu[1] = (m.get('model') or mu[0]), u
            if (u.get('output_tokens', 0) or 0) >= mw[2]:   # repeated lines of one message: keep the latest usage once, never add
                mw[2] = u.get('output_tokens', 0) or 0
                mw[0] = (u.get('input_tokens', 0) or 0) + 1.25 * (u.get('cache_creation_input_tokens', 0) or 0) + .1 * (u.get('cache_read_input_tokens', 0) or 0) + 5 * mw[2]
        if m.get('role') != 'assistant': continue
        mid = m.get('id') or d.get('uuid')
        if mid not in c['ids']: c['ids'].add(mid); c['c'] += 1
        for b in m.get('content') or []:
            if mw is not None and isinstance(b, dict) and b.get('type') == 'tool_use':
                mw[1].add('read' if b.get('name') == 'ToolSearch' else kindof(b.get('name'), b.get('input') or {}))
            if isinstance(b, dict) and b.get('type') == 'tool_use' and b.get('id') not in c['bid']:
                c['bid'].add(b.get('id')); c['tl'][b.get('name')] = c['tl'].get(b.get('name'), 0) + 1
# ---- public API list prices, USD per million tokens: in, 5m write, 1h write, cache hit, out
PRICES = {'fable': (10, 12.5, 20, .25, 50), 'opus': (4, 5, 8, .2, 20), 'sonnet': (2, 2.5, 4, .1, 10),
          'haiku': (.1, .125, .2, .01, .5), 'haiku_big': (.5, .625, 1, .05, 2.5)}
def model_name(mod):
    mod = (mod or '').lower()
    for k, n in (('fable', 'Fable'), ('opus', 'Opus'), ('sonnet', 'Sonnet'), ('haiku', 'Haiku')):
        if k in mod: return n
    return None
def msg_usd(mod, u):
    n = model_name(mod)
    if not n: return None, 0.0
    k = n.lower(); inp = u.get('input_tokens', 0) or 0; cr = u.get('cache_read_input_tokens', 0) or 0
    cw = u.get('cache_creation_input_tokens', 0) or 0; cc = u.get('cache_creation') or {}
    w1, w5 = cc.get('ephemeral_1h_input_tokens'), cc.get('ephemeral_5m_input_tokens')
    if w1 is None and w5 is None: w1, w5 = cw, 0
    else: w1, w5 = w1 or 0, w5 or 0
    if k == 'haiku' and inp + cr + cw > 100000: k = 'haiku_big'
    p = PRICES[k]
    return n, (inp * p[0] + w5 * p[1] + w1 * p[2] + cr * p[3] + (u.get('output_tokens', 0) or 0) * p[4]) / 1e6
def cost_of(c):
    tot, bym, byk = 0.0, {}, {}
    for mod, u, roles in c['mu'].values():
        n, usd = msg_usd(mod, u)
        if not n: continue
        tot += usd; bym[n] = bym.get(n, 0) + usd
        ks = sorted(roles) or ['think']
        for k in ks: byk[k] = byk.get(k, 0) + usd / len(ks)
    return tot, bym, byk
def kt_of(c):
    kt = {}
    for w, ks, _o in c['mw'].values():
        ks = sorted(ks) or ['think']
        for k in ks: kt[k] = kt.get(k, 0) + w / len(ks)
    return {k: round(v) for k, v in kt.items()}
def stats_event(rows):
    scan(ME, 'claude', BASE)
    for bid, aid in rows: scan(D + aid + '.output', bid)
    A = {}; CT = 0.0; CM = {}
    for k, c in SC.items():
        w, (c['ti'], c['to'], c['tw'], c['tr']) = wsum(v[1] for v in c['mu'].values())   # one usage per message id
        A[k] = {'c': c['c'], 'tl': c['tl'], 'ti': c['ti'], 'to': c['to'], 'tw': c['tw'], 'tr': c['tr'], 'w': w, 'kt': kt_of(c), 'usd': round(cost_of(c)[0], 4), 'usdM': {a: round(b, 4) for a, b in cost_of(c)[1].items()}, 'kusd': {a: round(b, 4) for a, b in cost_of(c)[2].items()}, 'cs': round(ACC['cs'].get(k, 0))}
    for k, c in SC.items():
        t, bm, _ = cost_of(c); CT += t
        for a, b in bm.items(): CM[a] = CM.get(a, 0) + b
    for k, v in ACC['cs'].items():
        if k not in A and k not in ('system',): A[k] = {'c': 0, 'tl': {}, 'ti': 0, 'to': 0, 'tw': 0, 'tr': 0, 'w': 0, 'cs': round(v)}
    return {'t': int(time.time() * 1000), 'type': 'stats', 'id': 'stats', 'actors': A, 'cost': {'total': round(CT, 4), 'byModel': {a: round(b, 4) for a, b in CM.items()}}, 'm': {'cs': round(ACC['m']['cs']), 'pc': round(ACC['m']['pc']), 'pm': round(ACC['m']['pm']), 'sys': round(ACC['cs'].get('system', 0))}}
def acc_update(m, procs_all):
    now = time.time(); dt = min(120, now - ACC['ts']) if ACC['ts'] else 60; ACC['ts'] = now
    for o, cpu in procs_all.items(): ACC['cs'][o] = ACC['cs'].get(o, 0) + cpu / 100 * dt
    ACC['m']['cs'] += m['cpu'] / 100 * m['cores'] * dt; ACC['m']['pc'] = max(ACC['m']['pc'], m['cpu']); ACC['m']['pm'] = max(ACC['m']['pm'], m['memMB'])
    try: json.dump(ACC, open(SF + '.tmp', 'w')); os.replace(SF + '.tmp', SF)
    except Exception: pass
last_stats = [None]

# ---- machine snapshot ----
HZ = os.sysconf('SC_CLK_TCK'); PG = os.sysconf('SC_PAGE_SIZE'); NC = os.cpu_count() or 1
last_mach = {'cpu': None, 'set': None}
def _stat(pid):
    try:
        s = open(f'/proc/{pid}/stat').read(); r = s.rindex(')'); f = s[r+2:].split()
        return int(f[1]), int(f[11]) + int(f[12]), s[s.index('(')+1:r]   # ppid, utime+stime, comm
    except Exception: return None
def _cmd(pid):
    try: return open(f'/proc/{pid}/cmdline').read().replace('\0', ' ').strip()
    except Exception: return ''
def _cwd(pid):
    try: return os.readlink(f'/proc/{pid}/cwd')
    except Exception: return ''
def _total():
    f = open('/proc/stat').readline().split()[1:]; v = list(map(int, f)); return sum(v), v[3] + v[4]
try: BTIME = int([l for l in open('/proc/stat') if l.startswith('btime')][0].split()[1])
except Exception: BTIME = 0
def _pstart(pid):
    """epoch seconds the process started (stat field 22 is in clock ticks since boot)"""
    try:
        s_ = open(f'/proc/{pid}/stat').read(); f = s_[s_.rindex(')') + 2:].split()
        return BTIME + int(f[19]) / HZ
    except Exception: return 0
def _owners_tokens(ids, now):
    """token -> the single agent whose recent Bash commands name it; tokens named by two agents are ambiguous and dropped"""
    who = {}
    for a in ids:
        T = TR.get(a)
        if not T: continue
        for h in T['hist']:
            for tk in h['tok']: who.setdefault(tk, set()).add(a)
    return {tk: next(iter(v)) for tk, v in who.items() if len(v) == 1}
def _owner(pid, ids, info, ctx):
    """ids: running board ids plus the orchestrator. Order: (1) a script/file/dir named in an agent's recent Bash command appears in this process or an ancestor,
    (2) the process started inside exactly one agent's Bash-command window, (3) folder name, last resort. Never an agent outside the roster."""
    tokmap, now = ctx
    ps = _pstart(pid); p, hops = pid, 0
    while p > 1 and hops < 30:
        hay = _cwd(p) + ' ' + _cmd(p); hit = {}
        for tk, a in tokmap.items():
            if tk in hay and re.search(re.escape(tk) + r'(?![\w.-])', hay): hit[a] = hit.get(a, 0) + 1
        if hit:
            b = sorted(hit.items(), key=lambda kv: -kv[1])
            if len(b) == 1 or b[0][1] > b[1][1]: return b[0][0]
        st = info.get(p) or _stat(p); p = st[0] if st else 0; hops += 1
    if ps:
        c = [a for a in ids if any(h['s'] - 5 <= ps <= (h['e'] if h['e'] else now) + 5 for h in (TR.get(a) or {}).get('hist', []))]
        if len(c) == 1: return c[0]
    p, hops = pid, 0
    while p > 1 and hops < 30:
        hay = _cwd(p) + ' ' + _cmd(p)
        for i in ids:
            if i != 'claude' and (f'/home/claude/wt/{i}' in hay or f'/home/claude/wt-out/{i}' in hay): return i
        if '/home/claude/wt-out/video' in hay or '/home/claude/wt/vid-' in hay:
            vid = [i for i in ids if i.startswith(('video', 'animatic', 'film'))]
            if len(vid) == 1: return vid[0]
        st = info.get(p) or _stat(p); p = st[0] if st else 0; hops += 1
    return None
def _kind(comm, cmd):
    c = (comm + ' ' + cmd).lower()
    if comm.startswith('claude'): return 'script', 'claude'
    if 'chrom' in c: return 'browser', 'browser test'
    if 'ffmpeg' in c: return 'video', 'video render'
    if 'http.server' in c: return 'server', 'http.server ' + (cmd.split('http.server')[-1].split() or [''])[0]
    if any(k in c for k in ('vite', 'webpack', 'esbuild', 'tsc', 'cargo', 'make ')): return 'build', 'build'
    if comm.startswith('node') or comm.startswith('python'):
        a = [x for x in cmd.split()[1:] if not x.startswith('-')]
        return 'script', (os.path.basename(a[0]) if a else comm)[:24]
    return None, None
def machine_snap(rows, now=None):
    ids = [b for b, _ in rows if b != 'radio'] + ['claude']
    for b, a in rows:
        if b != 'radio': track(D + a + '.output', b)
    track(ME, 'claude'); ctx = (_owners_tokens(ids, time.time()), time.time())
    t0, i0 = _total(); p0 = {}
    for d in os.listdir('/proc'):
        if d.isdigit():
            s = _stat(int(d))
            if s: p0[int(d)] = s
    time.sleep(1.0)
    S1 = {pid: _stat(pid) for pid in p0}   # per-process second sample first, then the machine total, so deltas never cover a longer window than dt
    t1, i1 = _total(); dt = max(1, t1 - t0); procs = {}
    me = os.getpid()
    for pid, (pp, j0, comm) in p0.items():
        s = S1.get(pid)
        if not s or pid == me: continue
        cpu = min(NC * 100, (s[1] - j0) / dt * NC * 100)
        if cpu < 0.5: continue
        cmd = _cmd(pid); kind, lab = _kind(comm, cmd)
        if not kind or 'boardtick' in cmd: continue
        try: rss = int(open(f'/proc/{pid}/statm').read().split()[1]) * PG / 1048576
        except Exception: rss = 0
        o = _owner(pid, ids, p0, ctx) or ('claude' if _cwd(pid).startswith('/home/claude') and kind != 'browser' else 'system')
        k = (o, kind, lab); a = procs.setdefault(k, [0, 0]); a[0] += cpu; a[1] += rss
    for v in procs.values(): v[0] = min(v[0], NC * 100)
    ALLO = {}
    for k, v in procs.items(): ALLO[k[0]] = ALLO.get(k[0], 0) + v[0]
    tot = sum(ALLO.values())
    if tot > NC * 100:
        f = NC * 100 / tot
        for v in procs.values(): v[0] *= f
        ALLO = {o: c * f for o, c in ALLO.items()}
    top = sorted(procs.items(), key=lambda kv: -kv[1][0])
    top = [{'owner': k[0], 'kind': k[1], 'cpu': round(v[0]), 'memMB': round(v[1]), 'label': k[2] + ('' if k[0] in ('system', 'claude') else ' (' + k[0] + ')')} for k, v in top if v[0] >= 2][:8]
    mi = {l.split(':')[0]: int(l.split()[1]) for l in open('/proc/meminfo') if l.split()[1].isdigit()}
    cpu = round(100 * (1 - (i1 - i0) / dt), 1)
    out = {'t': int((now or time.time()) * 1000), 'type': 'machine', 'id': 'machine', 'cpu': cpu, 'cores': NC, 'memMB': round((mi['MemTotal'] - mi['MemAvailable']) / 1024), 'memTotalMB': round(mi['MemTotal'] / 1024), 'procs': top}
    if now is None: acc_update(out, ALLO)
    return out
def machine_changed(m):
    sset = frozenset((p['owner'], p['kind']) for p in m['procs'])
    ch = last_mach['cpu'] is None or abs(m['cpu'] - last_mach['cpu']) > 10 or sset != last_mach['set']
    if ch: last_mach['cpu'], last_mach['set'] = m['cpu'], sset
    return ch


MTIME = os.path.getmtime(__file__)
cad = {'mach': 0, 'stats': 0, 'tok': 0, 'hb': 0}
FLAG = '/home/claude/board-active'
mode = [None]
def recent_me(sec=180):
    """True if the orchestrator transcript got an assistant message in the last `sec` seconds."""
    try:
        sz = os.path.getsize(ME)
        if time.time() - os.path.getmtime(ME) > sec: return False
        with open(ME, 'rb') as f:
            f.seek(max(0, sz - 200000)); tail = f.read().decode('utf-8', 'ignore').splitlines()
        for l in reversed(tail):
            try: d = json.loads(l)
            except Exception: continue
            m = d.get('message')
            if isinstance(m, dict) and m.get('role') == 'assistant': return time.time() - ts(d.get('timestamp', '')) / 1000 <= sec
    except Exception: pass
    return False
while True:
    if os.path.getmtime(__file__) != MTIME:
        os.execv(sys.executable, [sys.executable, '-u', __file__])   # reload when the script is edited
    try: rows = [l.split() for l in open('/home/claude/board-running.txt') if l.strip()]
    except Exception: rows = []
    rmap = {aid: bid for bid, aid in rows}
    nowm = time.time(); ev = []
    active = any(b != 'radio' for b, _ in rows) or os.path.exists(FLAG) or recent_me()
    want = 'active' if active else 'standby'
    if mode[0] != want:
        first = mode[0] is None; mode[0] = want
        if not first or want == 'active': ev.append({'t': int(nowm * 1000), 'type': 'act', 'id': 'radio', 'tool': 'Bash', 'kind': 'shell', 'text': 'Radio: ' + want})
        if want == 'active': cad.update({'mach': 0, 'stats': 0, 'tok': 0})
        else: cad['hb'] = 0
    if not active:
        # QUIET: only the orchestrator transcript, every 10 s, plus a heartbeat every 4 minutes
        ev += actions(ME, 'claude', rmap)
        track(ME, 'claude'); ev += live_events(['claude'], nowm)
        ev = [e for e in ev if not (e['type'] == 'act' and lastxt.get(e['id']) == e['text'] and e['id'] != 'radio')]
        for e in ev:
            if e['type'] == 'act': lastxt[e['id']] = e['text']
        if nowm - cad['hb'] >= 240: cad['hb'] = nowm; ev.append({'t': int(nowm * 1000), 'type': 'heartbeat', 'id': 'radio'})
        if ev: print('EVENTS ' + json.dumps(ev, separators=(',', ':')), flush=True)
        time.sleep(10); continue
    ev += actions(ME, 'claude', rmap)
    tk = []
    dotok = nowm - cad['tok'] >= 60   # full-file token sums are heavy: every 60 s only
    if dotok: cad['tok'] = nowm
    for bid, aid in rows:
        if bid != 'radio': ev += actions(D + aid + '.output', bid, rmap)
        track(D + aid + '.output', bid)
        w = tokd(D + aid + '.output') if dotok else None   # each message id counted once
        if w:
            if w > last_tok.get(bid, 0) * 1.03: last_tok[bid] = w; tk.append({'t': int(time.time() * 1000), 'type': 'tokens', 'id': bid, 'tokens': w})
    ev = [e for e in ev if not (e['type'] == 'act' and lastxt.get(e['id']) == e['text'] and e['id'] != 'radio')]
    for e in ev:
        if e['type'] == 'act': lastxt[e['id']] = e['text']
    w = mytok() if dotok else 0
    if w > last_tok.get('claude', 0) * 1.05 + 20000: last_tok['claude'] = w; tk.append({'t': int(time.time() * 1000), 'type': 'tokens', 'id': 'claude', 'tokens': w})
    ev += tk
    track(ME, 'claude')
    ev += live_events([b for b, _ in rows if b != 'radio'] + ['claude'], nowm)
    ev += autofinish(rows, nowm)
    if nowm - cad['mach'] >= 30:   # machine snapshot (takes ~1 s) every 30 s
        cad['mach'] = nowm
        try:
            m = machine_snap(rows)
            if machine_changed(m): ev.append(m)
        except Exception: pass
    if nowm - cad['stats'] >= 60:   # heavier stats and cost recompute every 60 s
        cad['stats'] = nowm
        try:
            se = stats_event(rows); sig = json.dumps([se['actors'], se['cost'], se['m']], sort_keys=True)
            if sig != last_stats[0]: last_stats[0] = sig; ev.append(se)
        except Exception: pass
    if ev: print('EVENTS ' + json.dumps(ev, separators=(',', ':')), flush=True)
    time.sleep(5)   # act/msg/spawn events go out within about 5 s
