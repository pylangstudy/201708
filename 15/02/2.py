#!python3.6
import re
print('match', re.match('X', 'A\nB\nX', re.MULTILINE))
print('search', re.search('^X', 'A\nB\nX', re.MULTILINE))

