#!python3.6
#coding:utf-8
#regex.search(string[, pos[, endpos]])
import re
regex = re.compile(r'^ab')
print(regex)
for target in ['abcdefg', 'cdefg', 'abcdabcd', 'cdabAB', 'ABcd']:
    print(target, regex.search(target))
print()

regex = re.compile(r'^ab', re.IGNORECASE)
print(regex)
for target in ['abcdefg', 'cdefg', 'abcdabcd', 'cdabAB', 'ABcd']:
    print(target, regex.search(target))
print()

regex = re.compile(r'ab', re.IGNORECASE)
print(regex)
for target in ['abcdefg', 'cdefg', 'abcdabcd', 'cdabAB', 'ABcd']:
    print(target, regex.search(target))
print()

regex = re.compile(r'ab', re.IGNORECASE)
print(regex)
pos = 2
for target in ['abcdefg', 'cdefg', 'abcdabcd', 'cdabAB']:
    print(target, regex.search(target, pos, endpos=len(target)))
print()

regex = re.compile(r'ab', re.IGNORECASE)
print(regex)
for target in ['abcdefg', 'cdefg', 'abcdabcd', 'cdabAB']:
    match = regex.search(target, pos, endpos=len(target))
    print(target, match)
    if match:
        print('  match.expand():', match.expand('XY'))
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
