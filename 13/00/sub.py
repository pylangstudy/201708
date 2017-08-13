#!python3.6
#coding:utf-8
#regex.sub(repl, string, count=0)
import re
regex = re.compile(r'^ab')
print(regex)
for target in ['abcdefg', 'cdefg', 'abcdabcd', 'cdabAB', 'ABcd']:
    print(target, regex.sub('XY', target))
print()

regex = re.compile(r'^ab', re.IGNORECASE)
print(regex)
for target in ['abcdefg', 'cdefg', 'abcdabcd', 'cdabAB', 'ABcd']:
    print(target, regex.sub('XY', target))
print()

regex = re.compile(r'ab', re.IGNORECASE)
print(regex)
for target in ['abcdefg', 'cdefg', 'abcdabcd', 'cdabAB', 'ABcd']:
    print(target, regex.sub('XY', target))
print()

regex = re.compile(r'ab', re.IGNORECASE)
count = 1
print(regex, 'count:', count)
for target in ['abcdefg', 'cdefg', 'abcdabcd', 'cdabAB']:
    print(target, regex.sub('XY', target, count=count))
print()

regex = re.compile(r'ab', re.IGNORECASE)
print(regex)
for target in ['abcdefg', 'cdefg', 'abcdabcd', 'cdabAB']:
    match = regex.sub('XY', target)
    print(target, match)
    if match:
        print('  match.expand():', match.expand('XY'))#AttributeError: 'str' object has no attribute 'expand'
        print('  match.group():', match.group())
        print('  match.groups():', match.groups())
        print('  match.groupdict():', match.groupdict())
        print('  match.start():', match.start())
        print('  match.end():', match.end())
        print('  match.span():', match.span())
        print('  match.pos:', match.pos)
        print('  match.endpos:', match.endpos)
        print('  match.lastindex:', match.lastindex)
        print('  match.lastgroup:', match.lastgroup)
        print('  match.re:', match.re)
        print('  match.string:', match.string)
