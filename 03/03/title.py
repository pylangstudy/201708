s = b'abc'; print(s, s.title())

def show(s):
    print(s)
    print(s.title())

show(b'hello world!')
show(b"they're bill's friends from the UK")

import re
def titlecase(s):
    return re.sub(rb"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0)[0:1].upper() +
#                  lambda mo: mo.group(0)[0].upper() +
                              mo.group(0)[1:].lower(),
                  s)
print(titlecase(b"they're bill's friends from the UK"))
