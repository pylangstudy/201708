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
    print(match.group())
    for i in range(match.lastindex): print(' ', match.group(i))
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
    print(match.group())
    for i in range(match.lastindex): print(' ', match.group(i))
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
    print(match.group())
    print('  key:', match.group('key'))
    print('  value:', match.group('value'))
    for i in range(match.lastindex): print(' ', match.group(i))
