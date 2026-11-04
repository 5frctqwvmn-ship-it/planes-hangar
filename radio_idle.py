# idle wait (default 120 s): keep moving feed events into radio-out files, no db writes
import subprocess, time, sys
end = time.time() + (float(sys.argv[1]) if len(sys.argv) > 1 else 120)
while time.time() < end:
    subprocess.run(['timeout', str(max(1, int(end - time.time()))), 'python3', '/home/claude/waitnext2.py'], capture_output=True)
print('IDLE DONE', int(time.time() * 1000))
