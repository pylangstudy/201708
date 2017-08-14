import re

li_tag = '''<li>Apple</li>
<li>Orange</li>
<li>Meron</li>
<li>Grape</li>
<li>Cherry</li>
'''
regex = re.compile(r'<li>(.+?)<\/li>', re.IGNORECASE)
matches = regex.finditer(li_tag)
for match in matches:
    print(match)
    print(match.lastindex, match.groups())
    print(f'match.pos={match.pos}')
    print(f'match.endpos={match.endpos}')
    print(f'match.lastindex={match.lastindex}')
    print(f'match.lastgroup={match.lastgroup}')
    print(f'match.re={match.re}')
    print(f'match.string={match.string}')
print()

li_tag = '''a=1
b=2
c=3
'''
regex = re.compile(r'(.+?)=(.+?)', re.IGNORECASE)
matches = regex.finditer(li_tag)
for match in matches:
    print(match)
    print(match.lastindex, match.groups())
    print(f'match.pos={match.pos}')
    print(f'match.endpos={match.endpos}')
    print(f'match.lastindex={match.lastindex}')
    print(f'match.lastgroup={match.lastgroup}')
    print(f'match.re={match.re}')
    print(f'match.string={match.string}')
print()

li_tag = '''a=1
b=2
c=3
'''
regex = re.compile(r'(?P<key>.+?)=(?P<value>.+?)', re.IGNORECASE)
matches = regex.finditer(li_tag)
for match in matches:
    print(match)
    print(match.lastindex, match.groups())
    print(f'match.pos={match.pos}')
    print(f'match.endpos={match.endpos}')
    print(f'match.lastindex={match.lastindex}')
    print(f'match.lastgroup={match.lastgroup}')
    print(f'match.re={match.re}')
    print(f'match.string={match.string}')
print()

