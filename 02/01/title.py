s = 'abc'; print(s, s.title())

def show(s):
    print(s)
    print(s.title())

show('hello world!')
show("they're bill's friends from the UK")

import re
def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0)[0].upper() +
                              mo.group(0)[1:].lower(),
                  s)
print(titlecase("they're bill's friends from the UK"))
