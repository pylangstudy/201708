import re

pattern = r'ab'
pattern1 = re.compile(pattern)
for target in ['abc', 'ABCabc']: print(pattern1.finditer(target))
print([f for target in ['abc', 'ABCabc'] for f in pattern1.finditer(target)])
print()
for target in ['abc', 'ABCabc']: print(pattern1.finditer(target, re.IGNORECASE))#1つ目がNoneになる
print([f for target in ['abc', 'ABCabc'] for f in pattern1.finditer(target, re.IGNORECASE)])
print()
for target in ['abc', 'ABCabc']: print(re.finditer(pattern, target))
print([f for target in ['abc', 'ABCabc'] for f in re.finditer(pattern1, target)])
print()
for target in ['abc', 'ABCabc']: print(re.finditer(pattern, target, re.IGNORECASE))
#print([f for target in ['abc', 'ABCabc'] for f in re.finditer(pattern1, target, re.IGNORECASE)])#ValueError: cannot process flags argument with a compiled pattern
