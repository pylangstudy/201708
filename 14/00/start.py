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
print()

email = "tony@tiremove_thisger.net"
m = re.search("remove_this", email)
print(email[:m.start()] + email[m.end():])
