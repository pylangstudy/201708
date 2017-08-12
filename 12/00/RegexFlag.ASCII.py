#!python3.6
import re
#\w、\W、\b、\B、\d、\D、\s、および \S において、ASCII 文字のみでマッチングを行います。これは Unicode パターンでのみ意味があり、バイト列パターンでは無視されます。
#re.ASCIIフラグに何の意味があるのか？
#  * パターン文字列で指定すれば不要では？
#      * ASCII文字をパターンに使えばそのまま一致確認する
#      * ASCII文字をパターンに含まなければre.ASCIIフラグの有無に関わらず不一致
print(re.A)
print(re.ASCII)
#pattern = r'^ab'
#pattern = r'あいう'
#pattern = r'^あいう'
pattern = r'あいう$'#「末尾が"あいう"に一致するもの」と期待していたが「あいう」完全一致のみ対象になった。なぜ…
#pattern = r'あいう\Z'#「末尾が"あいう"に一致するもの」と期待していたが「あいう」完全一致のみ対象になった。なぜ…
#pattern = r'^あいう$'
#pattern = '.*あいう$'
#pattern = None
#pattern = r''
#patternA = re.compile(pattern)
#patternA = re.compile(pattern, re.A)
patternA = re.compile(pattern, re.ASCII)#何の意味がある？
for target in ['a', 'abc', 'ab012', 'ab 01', 'abあいう', 'あいう', 'あいうab']:
    print(patternA.match(target))

print(re.match(r'^ab', 'abcdefg', re.ASCII))
