#!python3.6
import re

def displaymatch(match):
    if match is None:
        return None
#    return '<Match: %r, groups=%r>' % (match.group(), match.groups())
    print('<Match: %r, groups=%r>' % (match.group(), match.groups()))

valid = re.compile(r"^[a2-9tjqk]{5}$")
displaymatch(valid.match("akt5q"))  # Valid.
displaymatch(valid.match("akt5e"))  # Invalid.
displaymatch(valid.match("akt"))    # Invalid.
displaymatch(valid.match("727ak"))  # Valid.
