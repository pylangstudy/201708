#!python3.6
import locale
import re
#\ w、\ W、\ b、\ B、\ s、\ Sを現在のロケールに依存させます。ロケールのメカニズムは非常に信頼できず、一度に1つの "文化"しか扱わないため、このフラグの使用はお勧めしません。代わりにUnicodeのマッチングを使用するべきです。これはPython 3 for Unicode（str）パターンのデフォルトです。このフラグは、バイトパターンでのみ使用できます。
#エラーで使えなかった。非推奨というか使い方すらわからない。
#http://hhsprings.pinoko.jp/site-hhs/2015/11/re-locale%E3%80%81re-unicode-%E3%81%AE%E3%81%AF%E3%81%AA%E3%81%97/
locale.setlocale(locale.LC_ALL, 'ja_JP.utf8')
print(re.L)
print(re.LOCALE)
#pattern = r'^ab'
#pattern = r'あいう'
#pattern = r'^あいう'
#pattern = r'\u3042\u3043\u3044' #「末尾が"あいう"に一致するもの」と期待していたが「あいう」完全一致のみ対象になった。なぜ…
#pattern = b'\u3042\u3043\u3044' #「末尾が"あいう"に一致するもの」と期待していたが「あいう」完全一致のみ対象になった。なぜ…
#pattern = b'\x3042\x3043\x3044' #「末尾が"あいう"に一致するもの」と期待していたが「あいう」完全一致のみ対象になった。なぜ…
#pattern = b'\x30\42\x30\43\x30\44' #「末尾が"あいう"に一致するもの」と期待していたが「あいう」完全一致のみ対象になった。なぜ…
#pattern = rb'\\u3042\\u3043\\u3044' #「末尾が"あいう"に一致するもの」と期待していたが「あいう」完全一致のみ対象になった。なぜ…
#pattern = '\u3042\u3043\u3044' #「末尾が"あいう"に一致するもの」と期待していたが「あいう」完全一致のみ対象になった。なぜ…
#pattern = b'あいう'
#pattern = r'あいう\Z'#「末尾が"あいう"に一致するもの」と期待していたが「あいう」完全一致のみ対象になった。なぜ…
#pattern = r'^あいう$'
#pattern = '.*あいう$'
#pattern = None
#pattern = r''
#patternA = re.compile(pattern)
#patternA = re.compile(pattern, re.A)
patternA = re.compile(pattern, re.LOCALE)#ValueError: cannot use LOCALE flag with a str pattern
for target in ['あいう']:
#for target in ['\u3042\u3043\u3044']:
#for target in [b'a', b'abc', b'ab012', b'ab 01', b'abあいう', b'あいう', b'あいうab']:
    print(patternA.match(target))

print(re.match(r'^ab', 'abcdefg', re.LOCALE))
