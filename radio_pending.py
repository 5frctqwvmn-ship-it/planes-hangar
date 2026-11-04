# list up to 50 relay files not yet sent to the board db (oldest first); prints "DOCS id id ..." or "NONE"
import os, sys
OUT = '/home/claude/radio-out'; SENT = '/home/claude/radio-sent.txt'
try: sent = set(open(SENT).read().split())
except FileNotFoundError: sent = set()
ids = sorted(f[:-5] for f in os.listdir(OUT) if f.endswith('.json') and f[:-5] not in sent)
n = int(sys.argv[1]) if len(sys.argv) > 1 else 50
print('DOCS ' + ' '.join(ids[:n]) if ids else 'NONE'); print('BACKLOG', len(ids))
