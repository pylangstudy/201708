# [6.2.5.8. Raw String記法](https://docs.python.jp/3/library/re.html#raw-string-notation)

< [6.2.5. 正規表現の例](https://docs.python.jp/3/library/re.html#regular-expression-examples) < [6.2. re — 正規表現操作](https://docs.python.jp/3/library/re.html#module-re) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## データ

> Raw string記法 (r"text") により、バックスラッシュ ('\') を個々にバックスラッシュでエスケープすることなしに、正規表現を正常な状態に保ちます。例えば、下記の2つのコードは機能的に等価です。 :

```python
>>> re.match(r"\W(.)\1\W", " ff ")
<_sre.SRE_Match object; span=(0, 4), match=' ff '>
>>> re.match("\\W(.)\\1\\W", " ff ")
<_sre.SRE_Match object; span=(0, 4), match=' ff '>
```

> 文字通りのバックスラッシュにマッチさせたいなら、正規表現中ではエスケープする必要があります。 Raw string記法では、 r"\\" ということになります。 Raw string記法を用いない場合、 "\\\\" としなくてはなりません。下記のコードは機能的に等価です。 :

```python
>>> re.match(r"\\", r"\\")
<_sre.SRE_Match object; span=(0, 1), match='\\'>
>>> re.match("\\\\", r"\\")
<_sre.SRE_Match object; span=(0, 1), match='\\'>
```

```python
#!python3.6
import re
print(re.match(r"\W(.)\1\W", " ff "))
print(re.match("\\W(.)\\1\\W", " ff "))
print()
print(re.match(r"\\", r"\\"))
print(re.match("\\\\", r"\\"))
```
```sh
$ python 0.py 
<_sre.SRE_Match object; span=(0, 4), match=' ff '>
<_sre.SRE_Match object; span=(0, 4), match=' ff '>

<_sre.SRE_Match object; span=(0, 1), match='\\'>
<_sre.SRE_Match object; span=(0, 1), match='\\'>
```

`\`自体にマッチさせるケースより、エスケープ文字(`\n`等)を使うケースのほうが多いはず。よって、基本的に`r''`形式で書いたほうが楽で見やすい。

## 正規表現Webツール

* https://nelog.jp/regular-expression-online-tools
* http://qiita.com/AQRiL_1132/items/c185c7ad84c129e5a2df

URL|Python正規表現|URLシェア|入力の楽さ|見やすさ|応答速度|Pythonソースコード生成
---|--------------|---------|----------|--------|--------|----------------------
https://regex101.com/|○|○|○|○|✗|○
https://www.debuggex.com/|○|○|△|○|○|?
http://www.rexv.org/|○|✗|△|○|○|?
http://www.regexplanet.com/|○|○|✗|✗|?

