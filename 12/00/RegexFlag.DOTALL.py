#!python3.6
import re
#特殊文字 '.' を、改行を含む任意の文字と、とにかくマッチさせます；このフラグがなければ、 '.' は、改行 以外の 任意の文字とマッチします。
#フラグの有無で何が変わるのかわからない。
print(re.S)
print(re.DOTALL)
#pattern = r'^ab'
#pattern = r'あいう'
pattern = r'あい.'
#pattern = r'^あい.$'
#pattern = r'あいう$'#「末尾が"あいう"に一致するもの」と期待していたが「あいう」完全一致のみ対象になった。なぜ…
#pattern = r'あいう\Z'#「末尾が"あいう"に一致するもの」と期待していたが「あいう」完全一致のみ対象になった。なぜ…
#pattern = r'^あいう$'
#pattern = '.*あいう$'
#pattern = None
#pattern = r''
#patternA = re.compile(pattern)
#patternA = re.compile(pattern, re.A)
patternA = re.compile(pattern, re.DOTALL)
for target in ['あいう', 'あいう\nあいう', 'ab\nあいう']:
    print(patternA.match(target))

print(re.match(r'^ab', 'abcdefg', re.DOTALL))
