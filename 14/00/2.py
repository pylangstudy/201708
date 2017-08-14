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
    for i in range(match.lastindex): print(match[i])
    print(match.expand(r'\1 is matched.'))
