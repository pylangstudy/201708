# [6.1.1. 文字列定数](https://docs.python.jp/3/library/string.html#string-constants)

< [6.1. string — 一般的な文字列操作](https://docs.python.jp/3/library/string.html#module-string) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## 説明

名前|説明
----|----
string.ascii_letters|後述の ascii_lowercase と ascii_uppercase を合わせたもの。この値はロケールに依存しません
string.ascii_lowercase|小文字 'abcdefghijklmnopqrstuvwxyz' 。この値はロケールに依存せず、固定です
string.ascii_uppercase|大文字 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 。この値はロケールに依存せず、固定です
string.digits|文字列 '0123456789' です
string.hexdigits|文字列 '0123456789abcdefABCDEF' です
string.octdigits|文字列 '01234567' です
string.punctuation|C ロケールにおいて、句読点として扱われる ASCII 文字の文字列です
string.printable|印刷可能な ASCII 文字で構成される文字列です。 digits, ascii_letters, punctuation および whitespace を組み合わせたものです
string.whitespace|空白 (whitespace) として扱われる ASCII 文字全てを含む文字列です。ほとんどのシステムでは、これはスペース (space)、タブ (tab)、改行 (linefeed)、復帰 (return)、改頁 (formfeed)、垂直タブ (vertical tab) です

## ソースコード

```python
import string
print('string.ascii_letters', string.ascii_letters)
print('string.ascii_lowercase', string.ascii_lowercase)
print('string.ascii_uppercase', string.ascii_uppercase)
print('string.digits', string.digits)
print('string.hexdigits', string.hexdigits)
print('string.octdigits', string.octdigits)
print('string.punctuation', '>' + string.punctuation + '<')
print('string.printable', '>' + string.printable + '<')
print('string.whitespace', '>' + string.whitespace + '<')
```
```sh
$ python 0.py 
string.ascii_letters abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_lowercase abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits 0123456789
string.hexdigits 0123456789abcdefABCDEF
string.octdigits 01234567
string.punctuation >!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~<
string.printable >0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 	


<
string.whitespace > 	


<
```
