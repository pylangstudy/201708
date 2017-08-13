#!python3.6
#coding:utf-8
#regex.split(string, maxsplit=0)
#split() 関数と同様で、コンパイルしたパターンを使います。ただし、 match() と同じように、省略可能な pos, endpos 引数で検索範囲を指定することができます。
#上記のように説明があるのに、引数にはpos,endposが書いていない…
#実験結果によると、日本語説明文のほうが間違い。regex.split(string, maxsplit=0)が正しい。
import re

regex = re.compile(r'^ab')
print(regex)
for target in ['ab', 'abcdefg', 'cdefg', 'abcdabcd', 'cdabAB', 'ABcd']:
    print(target, regex.split(target))
print()

regex = re.compile(r'^ab', re.IGNORECASE)
print(regex)
for target in ['ab', 'abcdefg', 'cdefg', 'abcdabcd', 'cdabAB', 'ABcd']:
    print(target, regex.split(target))
print()

regex = re.compile(r'ab', re.IGNORECASE)
print(regex)
for target in ['ab', 'abcdefg', 'cdefg', 'abcdabcd', 'cdabAB', 'ABcd']:
    print(target, regex.split(target))
print()

regex = re.compile(r'ab', re.IGNORECASE)
maxsplit = 1
print(regex, 'maxsplit:', maxsplit)
#pos = 2
#print(regex, 'pos:', pos)
for target in ['ab', 'abcdefg', 'cdefg', 'abcdabcd', 'cdabAB']:
#    print(target, regex.split(target, pos, endpos=len(target)))#TypeError: 'endpos' is an invalid keyword argument for this function
    print(target, regex.split(target, maxsplit=maxsplit))
print()

regex = re.compile(r'ab', re.IGNORECASE)
pos = 2
print(regex, 'pos:', pos)
for target in ['ab', 'abcdefg', 'cdefg', 'abcdabcd', 'cdabAB']:
    match = regex.split(target, pos, endpos=len(target))
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
