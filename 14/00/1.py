#http://d.hatena.ne.jp/yumimue/20071220/1198141598
import re

regex = re.compile(r'ab', re.IGNORECASE)
match = regex.search('abcd')
print(regex.sub('XY', 'abcd'))
if match: print(match.expand('XY'))

match = regex.search('abcd')
print(match.groups())
if match: print(match.expand(r'XY'))

li_tag = '''<li>Apple</li>
<li>Orange</li>
<li>Meron</li>
<li>Grape</li>
<li>Cherry</li>
'''
print('-------------- re.sub() --------------')
result = re.sub(r'<li>(.+?)<\/li>', r'\1', li_tag, re.IGNORECASE)
print(result)
print('--------------')
result = re.sub(r'^<li>(.+?)<\/li>$', r'\1', li_tag, re.MULTILINE | re.IGNORECASE)
print(result)
print('--------------')
result = re.sub(r'<li>(.+?)<\/li>', r'\1', li_tag, re.MULTILINE | re.IGNORECASE)
print(result)

print('-------------- re.search() --------------')
match = re.search(r'<li>(.+?)<\/li>', li_tag, re.IGNORECASE)
print(match.lastindex)
print(match.expand(r'{\1}'))
"""
print('--------------')
match = re.search(r'^<li>(.+?)<\/li>$', li_tag, re.IGNORECASE)
print(match.lastindex)#AttributeError: 'NoneType' object has no attribute 'lastindex'
print(match.expand(r'{\1}'))
"""
print('--------------')
match = re.search(r'<li>(.+?)<\/li>', li_tag, re.MULTILINE | re.IGNORECASE)
print(match.lastindex)#AttributeError: 'NoneType' object has no attribute 'lastindex'
print(match.expand(r'{\1}'))
print('--------------')
match = re.search(r'^<li>(.+?)<\/li>$', li_tag, re.MULTILINE | re.IGNORECASE)
print(match.lastindex)#AttributeError: 'NoneType' object has no attribute 'lastindex'
print(match.expand(r'{\1}'))

print('-------------- regex.search() --------------')
regex = re.compile(r'<li>(.+?)<\/li>', re.IGNORECASE)
match = regex.search(li_tag)
print(match.lastindex); print(match.expand(r'{\1}'));
print('--------------')
"""
regex = re.compile(r'^<li>(.+?)<\/li>$', re.IGNORECASE)
match = regex.search(li_tag)
print(match.lastindex); print(match.expand(r'{\1}'));#AttributeError: 'NoneType' object has no attribute 'lastindex'
print('--------------')
"""
regex = re.compile(r'<li>(.+?)<\/li>', re.MULTILINE | re.IGNORECASE)
match = regex.search(li_tag)
print(match.lastindex); print(match.expand(r'{\1}'));
print('--------------')
regex = re.compile(r'^<li>(.+?)<\/li>$', re.MULTILINE | re.IGNORECASE)
match = regex.search(li_tag)
print(match.lastindex); print(match.expand(r'{\1}'));
print('--------------')

print('-------------- re.findall() --------------')
regex = re.compile(r'<li>(.+?)<\/li>', re.IGNORECASE)
print(regex.findall(li_tag))
print('--------------')
regex = re.compile(r'^<li>(.+?)<\/li>$', re.IGNORECASE)
print(regex.findall(li_tag))
print('--------------')
regex = re.compile(r'<li>(.+?)<\/li>', re.MULTILINE | re.IGNORECASE)
print(regex.findall(li_tag))
print('--------------')
regex = re.compile(r'^<li>(.+?)<\/li>$', re.MULTILINE | re.IGNORECASE)
print(regex.findall(li_tag))

print('-------------- re.finditer() --------------')
regex = re.compile(r'<li>(.+?)<\/li>', re.IGNORECASE)
matches = regex.finditer(li_tag)
for match in matches:
    print(match)
    print(match.lastindex, match.groups())
#print(match.lastindex); print(match.expand(r'{\1}'));
print('--------------')

"""
print('-------------- re.findall() --------------')
print('--------------')
match = re.findall(r'<li>(.+?)<\/li>', li_tag, re.MULTILINE | re.IGNORECASE)
print(match.lastindex)#AttributeError: 'NoneType' object has no attribute 'lastindex'
print(match.expand(r'{\1}'))
"""
"""
print('-------------- regex.findall() --------------')
regex = re.compile(r'<li>(.+?)<\/li>', re.MULTILINE | re.IGNORECASE)
#match = regex.findall(li_tag)#AttributeError: 'list' object has no attribute 'lastindex'
#match = regex.fullmatch(li_tag)#AttributeError: 'NoneType' object has no attribute 'lastindex'
#match = regex.match(li_tag)
match = regex.search(li_tag)
print(match.lastindex)
print(match.groups())
print(match.expand(r'{\1}'))
#print(match.expand(r'{\1} {\2}'))
"""
"""
print('--------------')
match = re.search(r'^<li>(.+?)<\/li>$', li_tag, re.IGNORECASE)
print(match.lastindex)#AttributeError: 'NoneType' object has no attribute 'lastindex'
print(match.expand(r'{\1}'))
"""
"""
print('--------------')
match = re.search(r'<li>(.+?)<\/li>', li_tag, re.MULTILINE | re.IGNORECASE)
print(match.lastindex)#AttributeError: 'NoneType' object has no attribute 'lastindex'
print(match.expand(r'{\1}'))

print('--------------')
match = re.search(r'^<li>(.+?)<\/li>$', li_tag, re.MULTILINE | re.IGNORECASE)
print(match.lastindex)#AttributeError: 'NoneType' object has no attribute 'lastindex'
print(match.expand(r'{\1}'))





print('--------------aaaaaaaaaaaaa')
regex = re.compile(r'<li>(.+?)<\/li>', re.MULTILINE | re.IGNORECASE)
match = regex.search(li_tag, re.MULTILINE | re.IGNORECASE)
print(match.lastindex)#AttributeError: 'NoneType' object has no attribute 'lastindex'
print(match.expand(r'{\1}'))

print('--------------')
#regex = re.compile(r'^<li>(.+?)<\/li>$', re.MULTILINE | re.IGNORECASE)
match = regex.search(li_tag)
print(match.lastindex)#1
print(match.expand(r'{\1}'))
#print(match.expand(r'{\1} {\2} {\3} {\4}'))#sre_constants.error: invalid group reference 2 at position 7
#result = re.expand(r'<li>(.+?)<\/li>', r'\1', li_tag)

print('--------------')
regex = re.compile(r'<li>(.+?)<\/li>', re.IGNORECASE)
match = regex.search(li_tag)
print(match.lastindex)
print(match.expand(r'{\1} {\2} {\3} {\4}'))
#result = re.expand(r'<li>(.+?)<\/li>', r'\1', li_tag)
"""
