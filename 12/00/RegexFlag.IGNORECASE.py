#!python3.6
import re
#英大文字・小文字を区別せずにマッチングを行います。

print(re.IGNORECASE)
pattern = r'^ab'
#pattern = r'あいう'
#pattern = r'あいう$'
#pattern = '.*あいう$'
#pattern = None
#pattern = r''
#patternA = re.compile(pattern)
#patternA = re.compile(pattern, re.A)
patternA = re.compile(pattern, re.IGNORECASE)
for target in ['a', 'ab', 'abc', 'ABC', 'aB012', 'Ab 01', 'あいう', 'ABあいう']:
    print(patternA.match(target))

print(re.match(r'^ab', 'aBcdefg', re.IGNORECASE))
print(re.match(r'^ab', 'Abcdefg', re.IGNORECASE | re.DEBUG))
