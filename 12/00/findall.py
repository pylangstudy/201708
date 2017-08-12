import re

#pattern = r'^ab'
pattern = r'ab'
pattern1 = re.compile(pattern)
for target in ['abc', 'ABCabc']: print(pattern1.findall(target))
print()
for target in ['abc', 'ABCabc']: print(pattern1.findall(target, re.IGNORECASE))#1つ目がNoneになる
print()
for target in ['abc', 'ABCabc']: print(re.findall(pattern, target))
print()
for target in ['abc', 'ABCabc']: print(re.findall(pattern, target, re.IGNORECASE))
