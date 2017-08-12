#!python3.6
import re
#このフラグによって、より良い、読みやすい正規表現を書くことができます。パターンの論理的なセクションを視覚的に区切り、コメントも入れることができます。パターン内の空白は、文字クラス内にあるかエスケープされていないバックスラッシュが前にある場合以外は無視されます。文字クラス内にもなく、エスケープされていないバックスラッシュが前にもない '#' が行内にある場合は、そのような '#' のうち一番左にあるものからその行の末尾までが無視されます。
print(re.X)
print(re.VERBOSE)
#a = re.compile(r"""\d +  # the integral part
#                   \.    # the decimal point
#                   \d *  # some fractional digits""", re.X)
#b = re.compile(r"\d+\.\d*")
#pattern = r'^ab'
#pattern = r'あいう'
pattern = r'あい. #コメント挿入できる'
#pattern = r'^あい.$'
#pattern = r'あいう$'#「末尾が"あいう"に一致するもの」と期待していたが「あいう」完全一致のみ対象になった。なぜ…
#pattern = r'あいう\Z'#「末尾が"あいう"に一致するもの」と期待していたが「あいう」完全一致のみ対象になった。なぜ…
#pattern = r'^あいう$'
#pattern = '.*あいう$'
#pattern = None
#pattern = r''
#patternA = re.compile(pattern)
#patternA = re.compile(pattern, re.A)
patternA = re.compile(pattern, re.VERBOSE)
for target in ['あいう', 'あいう\nあいう', 'ab\nあいう']:
    print(patternA.match(target))

print(re.match(r'^ab', 'abcdefg', re.VERBOSE))
