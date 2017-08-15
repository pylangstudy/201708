#!python3.6
import re

def displaymatch(match):
    if match is None:
        return None
#    return '<Match: %r, groups=%r>' % (match.group(), match.groups())
    print('<Match: %r, groups=%r>' % (match.group(), match.groups()))

pair = re.compile(r".*(.).*\1")
displaymatch(pair.match("717ak"))     # Pair of 7s.
displaymatch(pair.match("718ak"))     # No pairs.
displaymatch(pair.match("354aa"))     # Pair of aces.
