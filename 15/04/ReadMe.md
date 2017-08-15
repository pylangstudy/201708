# [6.2.5.5. テキストの秘匿](https://docs.python.jp/3/library/re.html#text-munging)

< [6.2.5. 正規表現の例](https://docs.python.jp/3/library/re.html#regular-expression-examples) < [6.2. re — 正規表現操作](https://docs.python.jp/3/library/re.html#module-re) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## データ

> sub() はパターンにマッチした部分を文字列や関数の返り値で置き換えます。この例では、”秘匿” する文字列に、関数と共に sub() を適用する例を示します。言い換えると、最初と最後の文字を除く、単語中の文字の位置をランダム化します。

```python
def repl(m):
    inner_word = list(m.group(2))
    random.shuffle(inner_word)
    return m.group(1) + "".join(inner_word) + m.group(3)
text = "Professor Abdolmalek, please report your absences promptly."
re.sub(r"(\w)(\w+)(\w)", repl, text)
'Poefsrosr Aealmlobdk, pslaee reorpt your abnseces plmrptoy.'
re.sub(r"(\w)(\w+)(\w)", repl, text)
'Pofsroser Aodlambelk, plasee reoprt yuor asnebces potlmrpy.'
```

```python
#!python3.6
import re
import random
def repl(m):
    inner_word = list(m.group(2))
    random.shuffle(inner_word)
    return m.group(1) + "".join(inner_word) + m.group(3)
text = "Professor Abdolmalek, please report your absences promptly."
print(text)
print(re.sub(r"(\w)(\w+)(\w)", repl, text))
print(re.sub(r"(\w)(\w+)(\w)", repl, text))
```
```sh
$ python 0.py 
Professor Abdolmalek, please report your absences promptly.
Psoofserr Aoamllebdk, plseae rrpoet yuor ancbeses pmrotply.
Pfsosroer Allomdbeak, please rpoert yuor aneecbss plrmptoy.
```

各単語における先頭文字〜末尾文字はそのままで、間の文字の順序をランダムに入れ替える。

なぜそうなるのか？

* `\w`: 任意の Unicode 単語文字にマッチします。ASCII フラグを使用すると [a-zA-Z0-9_] のみにマッチします。
* `(\w)`: 任意文字をグループ化する
* `\w+`: 1文字以上の任意文字
* `(\w+)`: 1文字以上の任意文字をグループ化する

`[任意文字1字] + [1つ以上の任意文字] + [任意文字1字]`となる。3つともグループ化されているので、`match.group(位置)`で取得できる。あとは`[1つ以上の任意文字]`のグループで取得された文字をリスト化して文字列にし、ランダムに並び替えて結合し直す。

## 正規表現Webツール

* https://nelog.jp/regular-expression-online-tools
* http://qiita.com/AQRiL_1132/items/c185c7ad84c129e5a2df

URL|Python正規表現|URLシェア|入力の楽さ|見やすさ|応答速度|Pythonソースコード生成
---|--------------|---------|----------|--------|--------|----------------------
https://regex101.com/|○|○|○|○|✗|○
https://www.debuggex.com/|○|○|△|○|○|?
http://www.rexv.org/|○|✗|△|○|○|?
http://www.regexplanet.com/|○|○|✗|✗|?

