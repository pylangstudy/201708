import re
#string 全体が正規表現 pattern にマッチした場合、対応する match オブジェクト を返します。文字列にパターンにマッチする場所が無い場合は None を返します; これは長さが 0 のマッチとは違うということを注意しておきます。バージョン 3.4 で追加.

#pattern = r'^ab'
pattern = r'ab'
pattern1 = re.compile(pattern)
for target in ['abc', 'ABCabc']: print(pattern1.fullmatch(target))
print()
for target in ['abc', 'ABCabc']: print(pattern1.fullmatch(target, re.IGNORECASE))#全部Noneになる
print()
for target in ['abc', 'ABCabc']: print(re.fullmatch(pattern, target))
print()
for target in ['abc', 'ABCabc']: print(re.fullmatch(pattern, target, re.IGNORECASE))
print()
print(re.fullmatch(pattern, 'ab'))
print(re.fullmatch(pattern, 'AB'))
print(re.fullmatch(pattern, 'AB', re.IGNORECASE))
