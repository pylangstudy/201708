# [6.2.5.7. 全ての副詞と、その位置を見つける](https://docs.python.jp/3/library/re.html#finding-all-adverbs-and-their-positions)

< [6.2.5. 正規表現の例](https://docs.python.jp/3/library/re.html#regular-expression-examples) < [6.2. re — 正規表現操作](https://docs.python.jp/3/library/re.html#module-re) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## データ

> もし、パターンにマッチするものについて、マッチしたテキスト以上の情報を得たいと考えた時、文字列ではなく マッチオブジェクト を返す finditer() が便利です。以下に例を示すように、なにかの文章のすべての副詞と、 その位置を 調べたい時、以下のように finditer() を使います:

```python
text = "He was carefully disguised but captured quickly by police."
for m in re.finditer(r"\w+ly", text):
...     print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
07-16: carefully
40-47: quickly
```
```python
#!python3.6
import re
text = "He was carefully disguised but captured quickly by police."
for m in re.finditer(r"\w+ly", text):
    print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
```
```sh
$ python 0.py 
07-16: carefully
40-47: quickly
```

「便利です」ではなく「`finditer()`しか手段がない」と思っている。

## 正規表現Webツール

* https://nelog.jp/regular-expression-online-tools
* http://qiita.com/AQRiL_1132/items/c185c7ad84c129e5a2df

URL|Python正規表現|URLシェア|入力の楽さ|見やすさ|応答速度|Pythonソースコード生成
---|--------------|---------|----------|--------|--------|----------------------
https://regex101.com/|○|○|○|○|✗|○
https://www.debuggex.com/|○|○|△|○|○|?
http://www.rexv.org/|○|✗|△|○|○|?
http://www.regexplanet.com/|○|○|✗|✗|?

