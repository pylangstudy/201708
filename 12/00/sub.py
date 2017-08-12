import re

#pattern = r'^ab'
pattern = r'ab'
pattern1 = re.compile(pattern)
for target in ['abc', 'ABCabc']: print(pattern1.sub('あい', target))
print()
for target in ['abc', 'ABCabc']: print(pattern1.sub('あい', target, re.IGNORECASE))
print()
for target in ['abc', 'ABCabc']: print(re.sub(pattern, 'あい', target))
print()
for target in ['abc', 'ABCabc']: print(re.sub(pattern, 'あい', target, re.IGNORECASE))
print()

#compile側でIGNORECASEを指定せねば検索するときに有効にならないらしい
#re.sub(,,re.IGNORECASE)で指定しても変わらない。変更不可なら紛らわしので各メソッドのflag引数を消して欲しい。
pattern = r'ab'
pattern1 = re.compile(pattern, re.IGNORECASE)
for target in ['abc', 'ABCabc']: print(pattern1.sub('あい', target))
print()

#compile側でIGNORECASEを指定せねば検索するときに有効にならないらしい
pattern = r'ab'
pattern1 = re.compile(pattern, re.IGNORECASE)
for target in ['abc', 'ABCabc']: print(pattern1.sub('xy', target, re.DEBUG))#メソッド側のflag(re.DEBUG)は無効
print()
