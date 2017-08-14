import re

li_tag = '''a=1
b=2
c=3
'''
regex = re.compile(r'(.+?)=(.+?)', re.IGNORECASE)
matches = regex.finditer(li_tag)
for match in matches:
    print(match)
    print(match.lastindex, match.groups())
    for i in range(match.lastindex): print(match[i])
    print(match.expand(r'\1 value is \2'))
