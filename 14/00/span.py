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
    print(f'match.start={match.start()}, match.end={match.end()}')
    print(f'match.start={match.span()}')
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
    for g in range(match.lastindex):
        print(f'match.start={match.start(g)}, match.end={match.end(g)}')
        print(f'match.start={match.span(g)}')
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
    for g in range(match.lastindex):
        print(f'match.start={match.start(g)}, match.end={match.end(g)}')
        print(f'match.start={match.span(g)}')
print()

