# move new feed events from radio.log into radio-out files without waiting (no db writes)
import subprocess; subprocess.run(['timeout', '5', 'python3', '/home/claude/waitnext2.py'], capture_output=True)
