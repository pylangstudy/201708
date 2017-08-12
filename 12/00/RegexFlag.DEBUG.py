#!python3.6
import re
#デバッグ情報を出力します。

print(re.DEBUG)
#pattern = r'^ab'
pattern = r'あいう'
#pattern = r'あいう$'
#pattern = '.*あいう$'
#pattern = None
#pattern = r''
#patternA = re.compile(pattern)
#patternA = re.compile(pattern, re.A)
patternA = re.compile(pattern, re.DEBUG)
for target in ['a', 'abc', 'ab012', 'ab 01', 'abあいう', 'あいう']:
    print(patternA.match(target))

print(re.match(r'^ab', 'abcdefg', re.DEBUG))
print(re.match(r'^ab', 'abcdefg', re.ASCII | re.DEBUG))
