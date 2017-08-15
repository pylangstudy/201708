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
displaymatch(pair.match("88aak"))     # Pair of aces.

if pair.match("717ak"): print(pair.match("717ak").group(1))
if pair.match("718ak"): print(pair.match("718ak").group(1))#AttributeError: 'NoneType' object has no attribute 'group'
if pair.match("354aa"): print(pair.match("354aa").group(1))
if pair.match("88aak"): print(pair.match("88aak").group(1))
