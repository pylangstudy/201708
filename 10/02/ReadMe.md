# [6.1.5. ヘルパー関数](https://docs.python.jp/3/library/string.html#helper-functions)

< [6.1.3. 書式指定文字列の文法](https://docs.python.jp/3/library/string.html#format-string-syntax) < [6.1. string — 一般的な文字列操作](https://docs.python.jp/3/library/string.html#module-string) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## 書式

> string.capwords(s, sep=None)(原文)

>    str.split() を使って引数を単語に分割し、 str.capitalize() を使ってそれぞれの単語の先頭の文字を大文字に変換し、 str.join() を使ってつなぎ合わせます。オプションの第2引数 sep が与えられないか None の場合、この置換処理は文字列中の連続する空白文字をスペース一つに置き換え、先頭と末尾の空白を削除します、それ以外の場合には sep は split と join に使われます。

### ソースコード

```python
#!python3.6
import string
print(string.capwords('  abc def ghi  '))
print(string.capwords('  abc,def,ghi  ', ','))
print(string.capwords('abc,def,ghi', ','))
```
```sh
$ python 0.py 
Abc Def Ghi
  abc,Def,Ghi  
Abc,Def,Ghi
```

