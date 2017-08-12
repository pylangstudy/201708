import re

#pattern = r'^ab'
pattern = r'ab'
pattern1 = re.compile(pattern)
for target in ['abc', 'ABCabc']: print(pattern1.search(target))
print()
for target in ['abc', 'ABCabc']: print(pattern1.search(target, re.IGNORECASE))#1つ目がNoneになる
print()
for target in ['abc', 'ABCabc']: print(re.search(pattern, target))
print()
for target in ['abc', 'ABCabc']: print(re.search(pattern, target, re.IGNORECASE))
