# mark relay ids as sent (after a successful batch write)
import sys
open('/home/claude/radio-sent.txt', 'a').write('\n'.join(sys.argv[1:]) + '\n')
