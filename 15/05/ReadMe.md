# [6.2.5.6. 全ての副詞を見つける](https://docs.python.jp/3/library/re.html#finding-all-adverbs)

< [6.2.5. 正規表現の例](https://docs.python.jp/3/library/re.html#regular-expression-examples) < [6.2. re — 正規表現操作](https://docs.python.jp/3/library/re.html#module-re) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## データ

> findall() はパターンにマッチする 全てに マッチします。 search() がそうであるように、最初のものだけに、ではありません。例えば、なにかの文章の全ての副詞を見つけたいとき、下記のように findall() を使います。 :

```python
text = "He was carefully disguised but captured quickly by police."
re.findall(r"\w+ly", text)
['carefully', 'quickly']
```
```python
#!python3.6
import re
import random
text = "He was carefully disguised but captured quickly by police."
print(re.findall(r"\w+ly", text))
```
```sh
$ python 0.py 
['carefully', 'quickly']
```

なぜそうなるのか？

* `\w`: 任意の Unicode 単語文字にマッチします。ASCII フラグを使用すると [a-zA-Z0-9_] のみにマッチします。
* `\w+`: 1つ以上の任意文字
* `\w+ly`: 1つ以上の任意文字の後ろに`ly`文字列がある

## 正規表現Webツール

* https://nelog.jp/regular-expression-online-tools
* http://qiita.com/AQRiL_1132/items/c185c7ad84c129e5a2df

URL|Python正規表現|URLシェア|入力の楽さ|見やすさ|応答速度|Pythonソースコード生成
---|--------------|---------|----------|--------|--------|----------------------
https://regex101.com/|○|○|○|○|✗|○
https://www.debuggex.com/|○|○|△|○|○|?
http://www.rexv.org/|○|✗|△|○|○|?
http://www.regexplanet.com/|○|○|✗|✗|?

