#!python3.6
import re

# re.compile(target): 同一patternを複数回使うなら効率的
pattern = r'^ab'
pattern1 = re.compile(pattern)
target = 'abcdefg'
result = pattern1.match(target)
print(result)
for target in ['ab', 'abc', 'Zab']:
    print(pattern1.match(target))

# re.match(pattern, target): 同一patternを1回だけ使うなら効率的
pattern = r'^ab'
target = 'abcdefg'
result = re.match(pattern, target)
print(result)
for target in ['ab', 'abc', 'Zab']:
    print(re.match(pattern, target))

#target = 'abcdefg'
#result 
