# [6.2.5.4. 電話帳の作成](https://docs.python.jp/3/library/re.html#making-a-phonebook)

< [6.2.5. 正規表現の例](https://docs.python.jp/3/library/re.html#regular-expression-examples) < [6.2. re — 正規表現操作](https://docs.python.jp/3/library/re.html#module-re) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## データ

> split() は文字列を与えられたパターンで分割し、リストにして返します。下記の、電話帳作成の例のように、このメソッドはテキストデータを読みやすくしたり、 Python で編集したりしやすくする際に、非常に役に立ちます。

> 最初に、入力を示します。通常、これはファイルからの入力になるでしょう。ここでは、3重引用符の書式とします :

```python
text = """Ross McFluff: 834.345.1254 155 Elm Street
...
Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way
...
...
Heather Albrecht: 548.326.4584 919 Park Place"""
```

## split

> 個々の記録は、1つ以上の改行で区切られています。まずは、文字列から空行を除き、記録ごとのリストに変換しましょう。

```python
entries = re.split("\n+", text)
print(entries)
```

### データ区分

> そして、各記録を、名、姓、電話番号、そして、住所に分割してリストにします。分割のためのパターンに使っている空白文字が、住所には含まれるため、 split() の maxsplit 引数を使います。 :

```
[re.split(":? ", entry, 3) for entry in entries]
```

> パターン、 :? は姓に続くコロンにマッチします。そのため、コロンは分割結果のリストには現れません。 maxsplit を 4 にすれば、ハウスナンバーと、ストリート名を分割することができます。 :

```python
#!python3.6
import re
text = """Ross McFluff: 834.345.1254 155 Elm Street
Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way
Heather Albrecht: 548.326.4584 919 Park Place"""

entries = re.split("\n+", text)
print(entries)
print()
print([re.split(":? ", entry, 3) for entry in entries])

print()
print([re.split(":?", entry, 3) for entry in entries])

print()
print([re.split(": ", entry, 3) for entry in entries])
```
```sh
$ python 0.py 
['Ross McFluff: 834.345.1254 155 Elm Street', 'Ronald Heathmore: 892.345.3428 436 Finley Avenue', 'Frank Burger: 925.541.7625 662 South Dogwood Way', 'Heather Albrecht: 548.326.4584 919 Park Place']

[['Ross', 'McFluff', '834.345.1254', '155 Elm Street'], ['Ronald', 'Heathmore', '892.345.3428', '436 Finley Avenue'], ['Frank', 'Burger', '925.541.7625', '662 South Dogwood Way'], ['Heather', 'Albrecht', '548.326.4584', '919 Park Place']]

/home/mint/.pyenv/versions/3.6.1/lib/python3.6/re.py:212: FutureWarning: split() requires a non-empty pattern match.
  return _compile(pattern, flags).split(string, maxsplit)
[['Ross McFluff', ' 834.345.1254 155 Elm Street'], ['Ronald Heathmore', ' 892.345.3428 436 Finley Avenue'], ['Frank Burger', ' 925.541.7625 662 South Dogwood Way'], ['Heather Albrecht', ' 548.326.4584 919 Park Place']]

[['Ross McFluff', '834.345.1254 155 Elm Street'], ['Ronald Heathmore', '892.345.3428 436 Finley Avenue'], ['Frank Burger', '925.541.7625 662 South Dogwood Way'], ['Heather Albrecht', '548.326.4584 919 Park Place']]
```

`:? `でなく`:?`にすると、`FutureWarning`が出た。そして半角スペースで分離しなくなった。

```sh
/home/mint/.pyenv/versions/3.6.1/lib/python3.6/re.py:212: FutureWarning: split() requires a non-empty pattern match.
  return _compile(pattern, flags).split(string, maxsplit)
[['Ross McFluff', ' 834.345.1254 155 Elm Street'], ['Ronald Heathmore', ' 892.345.3428 436 Finley Avenue'], ['Frank Burger', ' 925.541.7625 662 South Dogwood Way'], ['Heather Albrecht', ' 548.326.4584 919 Park Place']]
```

`:? `でなく`: `にすると、`FutureWarning`が消えた。それ以外は`:?`と同じく半角スペースで分離しなくなった。

```sh
[['Ross McFluff', '834.345.1254 155 Elm Street'], ['Ronald Heathmore', '892.345.3428 436 Finley Avenue'], ['Frank Burger', '925.541.7625 662 South Dogwood Way'], ['Heather Albrecht', '548.326.4584 919 Park Place']]
```

なぜそうなるのか。よくわからない。以下のように考えて理解した。

* `:`: 単なるコロン文字
* `:?`: `:`が1つ以上あるか0文字か
* ` `: 単なる半角スペース文字
* `:? `: `:`が1つ以上あるか0文字かあり、後ろに半角スペースが1字ある (`: ` or ` `)

`: ` or ` `いずれかの場合で分離するために`:? `である必要があった、ということか。慣れないせいか正規表現の理解には苦労する。

## 正規表現Webツール

* https://nelog.jp/regular-expression-online-tools
* http://qiita.com/AQRiL_1132/items/c185c7ad84c129e5a2df

URL|Python正規表現|URLシェア|入力の楽さ|見やすさ|応答速度|Pythonソースコード生成
---|--------------|---------|----------|--------|--------|----------------------
https://regex101.com/|○|○|○|○|✗|○
https://www.debuggex.com/|○|○|△|○|○|?
http://www.rexv.org/|○|✗|△|○|○|?
http://www.regexplanet.com/|○|○|✗|✗|?

