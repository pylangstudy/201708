import re

pattern = r'ab'
pattern1 = re.compile(pattern)
for target in ['abc', 'ABCabc']: print(pattern1.subn('あい', target))
print()
for target in ['abc', 'ABCabc']: print(pattern1.subn('あい', target, re.IGNORECASE))
print()
for target in ['abc', 'ABCabc']: print(re.subn(pattern, 'あい', target))
print()
for target in ['abc', 'ABCabc']: print(re.subn(pattern, 'あい', target, re.IGNORECASE))
print()

pattern = r'ab'
pattern1 = re.compile(pattern, re.IGNORECASE)
for target in ['abc', 'ABCabc']: print(pattern1.subn('あい', target))
print()

pattern = r'ab'
pattern1 = re.compile(pattern, re.IGNORECASE)
for target in ['abc', 'ABCabc']: print(pattern1.subn('xy', target, re.DEBUG))#メソッド側のflag(re.DEBUG)は無効
print()
