# [6.2.5.2. scanf() をシミュレートする](https://docs.python.jp/3/library/re.html#simulating-scanf)

< [6.2.5. 正規表現の例](https://docs.python.jp/3/library/re.html#regular-expression-examples) < [6.2. re — 正規表現操作](https://docs.python.jp/3/library/re.html#module-re) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## パターン

> Python には現在のところ、 scanf() に相当するものがありません。正規表現は、 scanf() のフォーマット文字列よりも、一般的により強力であり、また冗長でもあります。以下の表に、 scanf() のフォーマットトークンと正規表現の大体同等な対応付けを示します。

なぜ唐突にC言語のscanf()が槍玉に上がったのか謎。

scanf()トークン|正規表現
---------------|--------
`%c`|`.`
`%5c`|`.{5}`
`%d`|`[-+]?\d+`
`%e`, `%E`, `%f`, `%g`|`[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?`
`%i`|`[-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)`
`%o`|`[-+]?[0-7]+`
`%s`|`\S+`
`%u`|`\d+`
`%x`, `%X`|`[-+]?(0[xX])?[\dA-Fa-f]+`

> 以下のような文字列からファイル名と数値を抽出することを考えます

```
/usr/sbin/sendmail - 0 errors, 4 warnings
```

scanf() フォーマットは次のように使います

```
%s - %d errors, %d warnings
```

同等な正規表現はこのようなものとなります

```
(\S+) - (\d+) errors, (\d+) warnings
``

```python
#!python3.6
import re
valid = re.compile(r"(\S+) - (\d+) errors, (\d+) warnings")
match = valid.match("/usr/sbin/sendmail - 0 errors, 4 warnings")
print(match.groups())
```
```sh
$ python 0.py 
('/usr/sbin/sendmail', '0', '4')
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

