#!python3.6
import re
#指定されると、パターン文字 '^' は、文字列の先頭および各行の先頭(各改行の直後)とマッチします；そしてパターン文字 '$' は文字列の末尾および各行の末尾 (改行の直前) とマッチします。デフォルトでは、 '^' は、文字列の先頭とだけマッチし、 '$' は、文字列の末尾および文字列の末尾の改行の直前(がもしあれば)とマッチします。
print(re.M)
print(re.MULTILINE)
#pattern = r'^ab'
#pattern = r'あいう'
pattern = r'^あい.$'
#pattern = r'あいう$'#「末尾が"あいう"に一致するもの」と期待していたが「あいう」完全一致のみ対象になった。なぜ…
#pattern = r'あいう\Z'#「末尾が"あいう"に一致するもの」と期待していたが「あいう」完全一致のみ対象になった。なぜ…
#pattern = r'^あいう$'
#pattern = '.*あいう$'
#pattern = None
#pattern = r''
#patternA = re.compile(pattern)
#patternA = re.compile(pattern, re.A)
patternA = re.compile(pattern, re.MULTILINE)
for target in ['あいう', 'あいう\nあいう', 'ab\nあいう']:
    print(patternA.match(target))

print(re.match(r'^ab', 'abcdefg', re.MULTILINE))
