import re

#pattern = r'^ab'
pattern = r'ab'
pattern1 = re.compile(pattern)
for target in ['abc', 'ABCabc']: print(pattern1.match(target))
print()
for target in ['abc', 'ABCabc']: print(pattern1.match(target, re.IGNORECASE))#全部Noneになる
print()
for target in ['abc', 'ABCabc']: print(re.match(pattern, target))
print()
for target in ['abc', 'ABCabc']: print(re.match(pattern, target, re.IGNORECASE))
