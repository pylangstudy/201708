# [6.3. difflib — 差分の計算を助ける](https://docs.python.jp/3/library/difflib.html#module-difflib)

< [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* [Lib/difflib.py](https://github.com/python/cpython/tree/3.6/Lib/difflib.py)

## 差分チェック

> このモジュールは、シーケンスを比較するためのクラスや関数を提供しています。例えば、ファイルの差分を計算して、それを HTML や context diff, unified diff などいろいろなフォーマットで出力するために、このモジュールを利用することができます。ディレクトリやファイル群を比較するためには、 filecmp モジュールも参照してください。

* [filecmp](https://docs.python.jp/3/library/filecmp.html#module-filecmp)

クラス|説明
------|----
class difflib.SequenceMatcher|似た単語を探せる。類似率を取得できる。
class difflib.Differ|いわゆるdiff。差分チェック。
class difflib.HtmlDiff|diff結果をHTML文字列データにできる。[例](https://raw.githubusercontent.com/pylangstudy/201708/master/16/00/difflib.HtmlDiff.make_file.html)

[例](https://raw.githubusercontent.com/pylangstudy/201708/master/16/00/difflib.HtmlDiff.make_file.html)にあるものが標準ライブラリだけで生成できるのが素敵。

### メソッド

メソッド|説明
--------|----
difflib.context_diff|差分をcontext diffフォーマット(以下「コンテクスト形式」)で返す
difflib.unified_diff|差分をunified diff フォーマット(以下「ユニファイド形式」)で返す
difflib.diff_bytes|バイナリデータを対象に差分チェックする
difflib.ndiff|差分をDifferスタイルで返す

詳細は各ソースコードの実行結果参照。

```python
import difflib

a='abc\ndef\nhij'
b='abc\nd555ef\nhij'
a=a.splitlines()
b=b.splitlines()

print('========== context_diff format ==========')
for buf in difflib.context_diff(a, b):
    print(buf)

print('\n\n')
print('========== unified_diff format ==========')
for buf in difflib.unified_diff(a,b):
    print(buf)

print('\n\n')
print('========== ndiff format ==========')
for buf in difflib.ndiff(a,b):
    print(buf)

print('\n\n')
print('========== difflib.Differ().compare() ==========')
#http://ja.pymotw.com/2/difflib/
d = difflib.Differ()
diff = d.compare(a, b)
print('\n'.join(diff))
```
```sh
$ python difflib.Differ.py 
========== context_diff format ==========
*** 

--- 

***************

*** 1,3 ****

  abc
! def
  hij
--- 1,3 ----

  abc
! d555ef
  hij
========== unified_diff format ==========
--- 

+++ 

@@ -1,3 +1,3 @@

 abc
-def
+d555ef
 hij
========== ndiff format ==========
  abc
- def
+ d555ef
  hij
========== difflib.Differ().compare() ==========
  abc
- def
+ d555ef
  hij
```

## 類似チェック

`difflib.SequenceMatcher`による類似チェック。

```python
import difflib
...
strs = [
    "スパゲティ",
    "スパゲティー",
    "スパゲッティ",
    "スパゲッティー",
    u"ｽﾊﾟｹﾞﾃｨ",
    u"ｽﾊﾟｹﾞﾃｨ-",
    u"ｽﾊﾟｹﾞｯﾃｨ",
    u"ｽﾊﾟｹﾞｯﾃｨ-",
]
...
import unicodedata
for (str1, str2) in [(str1, str2) for str1 in strs for str2 in strs if str1 < str2]:
    normalized_str1 = unicodedata.normalize('NFKC', str1)
    normalized_str2 = unicodedata.normalize('NFKC', str2)
    print(str1, "<~>", str2)
    s = difflib.SequenceMatcher(None, normalized_str1, normalized_str2).ratio()
    print("match ratio:", s)
```
```sh
$ python difflib.SequenceMatcher.py 
...
スパゲティ <~> スパゲティー
match ratio: 0.9090909090909091
スパゲティ <~> ｽﾊﾟｹﾞﾃｨ
match ratio: 1.0
スパゲティ <~> ｽﾊﾟｹﾞﾃｨ-
match ratio: 0.9090909090909091
スパゲティ <~> ｽﾊﾟｹﾞｯﾃｨ
match ratio: 0.9090909090909091
スパゲティ <~> ｽﾊﾟｹﾞｯﾃｨ-
match ratio: 0.8333333333333334
スパゲティー <~> ｽﾊﾟｹﾞﾃｨ
match ratio: 0.9090909090909091
スパゲティー <~> ｽﾊﾟｹﾞﾃｨ-
match ratio: 0.8333333333333334
スパゲティー <~> ｽﾊﾟｹﾞｯﾃｨ
match ratio: 0.8333333333333334
スパゲティー <~> ｽﾊﾟｹﾞｯﾃｨ-
match ratio: 0.7692307692307693
スパゲッティ <~> スパゲティ
match ratio: 0.9090909090909091
スパゲッティ <~> スパゲティー
match ratio: 0.8333333333333334
スパゲッティ <~> スパゲッティー
match ratio: 0.9230769230769231
スパゲッティ <~> ｽﾊﾟｹﾞﾃｨ
match ratio: 0.9090909090909091
スパゲッティ <~> ｽﾊﾟｹﾞﾃｨ-
match ratio: 0.8333333333333334
スパゲッティ <~> ｽﾊﾟｹﾞｯﾃｨ
match ratio: 1.0
スパゲッティ <~> ｽﾊﾟｹﾞｯﾃｨ-
match ratio: 0.9230769230769231
スパゲッティー <~> スパゲティ
match ratio: 0.8333333333333334
スパゲッティー <~> スパゲティー
match ratio: 0.9230769230769231
スパゲッティー <~> ｽﾊﾟｹﾞﾃｨ
match ratio: 0.8333333333333334
スパゲッティー <~> ｽﾊﾟｹﾞﾃｨ-
match ratio: 0.7692307692307693
スパゲッティー <~> ｽﾊﾟｹﾞｯﾃｨ
match ratio: 0.9230769230769231
スパゲッティー <~> ｽﾊﾟｹﾞｯﾃｨ-
match ratio: 0.8571428571428571
ｽﾊﾟｹﾞﾃｨ <~> ｽﾊﾟｹﾞﾃｨ-
match ratio: 0.9090909090909091
ｽﾊﾟｹﾞｯﾃｨ <~> ｽﾊﾟｹﾞﾃｨ
match ratio: 0.9090909090909091
ｽﾊﾟｹﾞｯﾃｨ <~> ｽﾊﾟｹﾞﾃｨ-
match ratio: 0.8333333333333334
ｽﾊﾟｹﾞｯﾃｨ <~> ｽﾊﾟｹﾞｯﾃｨ-
match ratio: 0.9230769230769231
ｽﾊﾟｹﾞｯﾃｨ- <~> ｽﾊﾟｹﾞﾃｨ
match ratio: 0.8333333333333334
ｽﾊﾟｹﾞｯﾃｨ- <~> ｽﾊﾟｹﾞﾃｨ-
match ratio: 0.9230769230769231
```

表記ゆれに関しては他にも多くの課題がある。`difflib.SequenceMatcher`だけでは解決できない。

* 全角/半角
* 日本語(漢字、ひらがな、カタカナ)
* 英語(カタカナ英語、英語スペル(アルファベット(大文字, 小文字))、アメリカ英語、イギリス英語)
* 俗語、俗称、方言、ネットスラング

http://blog.mudatobunka.org/entry/2016/05/08/154934

本格的にやるには、形態素解析用ライブラリとデータのカスタマイズが必要か。

