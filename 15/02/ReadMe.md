# [6.2.5.3. search() vs. match()](https://docs.python.jp/3/library/re.html#search-vs-match)

< [6.2.5. 正規表現の例](https://docs.python.jp/3/library/re.html#regular-expression-examples) < [6.2. re — 正規表現操作](https://docs.python.jp/3/library/re.html#module-re) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## search, match の違い

> Python は正規表現ベースの 2 個の基本的な関数、文字列の先頭でのみのマッチを確認する re.match() および、文字列内の位置にかかわらずマッチを確認する re.search() (Perl でのデフォルトの挙動) を提供しています。

```python
re.match("c", "abcdef")    # No match
re.search("c", "abcdef")   # Match
<_sre.SRE_Match object; span=(2, 3), match='c'>
```
```python
#!python3.6
import re
print('match', re.match("c", "abcdef"))
print('search', re.search("c", "abcdef"))
```
```sh
$ python 0.py 
match None
search <_sre.SRE_Match object; span=(2, 3), match='c'>
```

> '^' で始まる正規表現は、 search() において、マッチを文字列の先頭からに制限するために使用します:

```python
re.match("c", "abcdef")    # No match
re.search("^c", "abcdef")  # No match
re.search("^a", "abcdef")  # Match
<_sre.SRE_Match object; span=(0, 1), match='a'>
```
```python
#!python3.6
import re
print('match', re.match("c", "abcdef"))
print('search', re.search("^c", "abcdef"))
print('search', re.search("^a", "abcdef"))
```
```sh
$ python 1.py 
match None
search None
search <_sre.SRE_Match object; span=(0, 1), match='a'>
```

> ただし、 MULTILINE モードの match() では文字列の先頭にのみマッチするのに対し、正規表現に '^' を使った search() では各行の先頭にもマッチします。

```python
re.match('X', 'A\nB\nX', re.MULTILINE)  # No match
re.search('^X', 'A\nB\nX', re.MULTILINE)  # Match
<_sre.SRE_Match object; span=(4, 5), match='X'>
```
```python
#!python3.6
import re
print('match', re.match('X', 'A\nB\nX', re.MULTILINE))
print('search', re.search('^X', 'A\nB\nX', re.MULTILINE))
```
```sh
$ python 2.py 
match None
search <_sre.SRE_Match object; span=(4, 5), match='X'>
```

「大は小を兼ねる」ということで、search()を覚えておけばmatch()を代用できる。match()はPython独自のsearch()略式系にすぎない。

## 正規表現Webツール

* https://nelog.jp/regular-expression-online-tools
* http://qiita.com/AQRiL_1132/items/c185c7ad84c129e5a2df

URL|Python正規表現|URLシェア|入力の楽さ|見やすさ|応答速度|Pythonソースコード生成
---|--------------|---------|----------|--------|--------|----------------------
https://regex101.com/|○|○|○|○|✗|○
https://www.debuggex.com/|○|○|△|○|○|?
http://www.rexv.org/|○|✗|△|○|○|?
http://www.regexplanet.com/|○|○|✗|✗|?

