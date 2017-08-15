# [6.2.5.1. ペアの確認](https://docs.python.jp/3/library/re.html#checking-for-a-pair)

< [6.2.5. 正規表現の例](https://docs.python.jp/3/library/re.html#regular-expression-examples) < [6.2. re — 正規表現操作](https://docs.python.jp/3/library/re.html#module-re) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## matchオブジェクト

> この例では、マッチオブジェクトの表示を少し美しくするために、下記の補助関数を使用します :

```python
def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())
```

> あなたがポーカープログラムを書いているとします。プレイヤーの持ち札はそれぞれの文字が1枚のカードを意味する5文字の文字列によって表現されます。 “a” はエース、 “k” はキング、 “q” はクイーン、 “j” はジャック、 “t” は10、そして “2” から “9” はそれぞれの数字のカードを表します。

> 与えられた文字列が持ち札として有効かどうかの確認は、次のようにして行えます。

```python
valid = re.compile(r"^[a2-9tjqk]{5}$")
displaymatch(valid.match("akt5q"))  # Valid.
"<Match: 'akt5q', groups=()>"
displaymatch(valid.match("akt5e"))  # Invalid.
displaymatch(valid.match("akt"))    # Invalid.
displaymatch(valid.match("727ak"))  # Valid.
"<Match: '727ak', groups=()>"
```

動作するコードにまとめると以下。

```python
#!python3.6
import re

def displaymatch(match):
    if match is None:
        return None
#    return '<Match: %r, groups=%r>' % (match.group(), match.groups())
    print('<Match: %r, groups=%r>' % (match.group(), match.groups()))

valid = re.compile(r"^[a2-9tjqk]{5}$")
displaymatch(valid.match("akt5q"))  # Valid.
displaymatch(valid.match("akt5e"))  # Invalid.
displaymatch(valid.match("akt"))    # Invalid.
displaymatch(valid.match("727ak"))  # Valid.
```

> 最後の持ち札 "727ak" は、ペアを含んでいます。言い換えると同じ値のカードが2枚あります。これを正規表現にマッチさせるために、後方参照を使う場合もあります :

```python
pair = re.compile(r".*(.).*\1")
displaymatch(pair.match("717ak"))     # Pair of 7s.
displaymatch(pair.match("718ak"))     # No pairs.
displaymatch(pair.match("354aa"))     # Pair of aces.
```

`.*(.).*\1`という正規表現がわからない。

* `(.)`: 何かの文字種1字をグループ化する(後方参照の対象)
* `.*`: 何かの文字種1字が0〜1つ以上ある
* `\1`: 最初に見つかった`(.)`

つまり、`.*(.).*\1`は、`[0〜1つ以上] + [1字] + [0〜1つ以上] + [1字]`。

* 最初に見つかった文字が2つある(`(.)`, `\1`)
* 最初に見つかった文字2つの前後には何かの文字が1つ以上あってもいいし、0個でもいい(連続してても良い)

と思って、以下のパターンを試してみたら、妙な結果になった。

https://regex101.com/

対象|一致|グループ
----|----|
aa|aa|a
88|88|8
aa8|aa|a
aa88|aa88|8
88aa|88aa|a
a88a|a88|8
8aa8|8aa|a
```

`aa88`は`aa`に一致しグループは`a`になると思っていた。しかし、`aa88`に一致し`8`がグループになっている。`88aa`も同様。謎。

> どのカードのペアになっているかを調べるには、以下のようにマッチオブジェクトの group() メソッドを使います:

```python
pair.match("717ak").group(1)
# Error because re.match() returns None, which doesn't have a group() method:
pair.match("718ak").group(1)#AttributeError: 'NoneType' object has no attribute 'group'
pair.match("354aa").group(1)
```
```python
#!python3.6
import re

def displaymatch(match):
    if match is None:
        return None
#    return '<Match: %r, groups=%r>' % (match.group(), match.groups())
    print('<Match: %r, groups=%r>' % (match.group(), match.groups()))

pair = re.compile(r".*(.).*\1")
displaymatch(pair.match("717ak"))     # Pair of 7s.
displaymatch(pair.match("718ak"))     # No pairs.
displaymatch(pair.match("354aa"))     # Pair of aces.
displaymatch(pair.match("88aak"))     # Pair of aces.

if pair.match("717ak"): print(pair.match("717ak").group(1))
if pair.match("718ak"): print(pair.match("718ak").group(1))#AttributeError: 'NoneType' object has no attribute 'group'
if pair.match("354aa"): print(pair.match("354aa").group(1))
if pair.match("88aak"): print(pair.match("88aak").group(1))
```
```sh
$ python 2.py 
<Match: '717', groups=('7',)>
<Match: '354aa', groups=('a',)>
<Match: '88aa', groups=('a',)>
7
a
a
```

## 正規表現Webツール

* https://nelog.jp/regular-expression-online-tools
* http://qiita.com/AQRiL_1132/items/c185c7ad84c129e5a2df

URL|Python正規表現|URLシェア|入力の楽さ|見やすさ|応答速度|Pythonソースコード生成
---|--------------|---------|----------|--------|--------|----------------------
https://regex101.com/|○|○|○|○|✗|○
https://www.debuggex.com/|○|○|△|○|○|?
http://www.rexv.org/|○|✗|△|○|○|?
http://www.regexplanet.com/|○|○|✗|✗|?

