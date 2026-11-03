import time, os, sys, json
LOG = '/home/claude/radio.log'; OFF = '/home/claude/radio.off'; OUT = '/home/claude/radio-out'
os.makedirs(OUT, exist_ok=True)
try: off = int(open(OFF).read())
except Exception: off = 0
end = time.time() + 540
seen = set(os.listdir(OUT))
while time.time() < end:
    try:
        with open(LOG) as f:
            f.seek(off); data = f.read()
    except FileNotFoundError: data = ''
    if data.strip():
        off += len(data.encode()); open(OFF, 'w').write(str(off))
        ids = []
        for l in data.splitlines():
            if not l.startswith('EVENTS '): continue
            try: evs = json.loads(l[7:])
            except Exception: continue
            for e in evs:
                t = int(e.get('t', 0))
                while f'e{t}.json' in seen: t += 1
                e['t'] = t; name = f'e{t}.json'; seen.add(name)
                json.dump(e, open(os.path.join(OUT, name), 'w'))
                ids.append(f'e{t}')
        if ids:
            for i in range(0, len(ids), 50): print('DOCS ' + ' '.join(ids[i:i+50]))
            sys.exit(0)
    time.sleep(2)
print('NONE')
