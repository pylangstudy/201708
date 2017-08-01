# [4.7. テキストシーケンス型 — str](https://docs.python.jp/3/library/stdtypes.html#text-sequence-type-str)

< [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## [4.7. テキストシーケンス型 — str](https://docs.python.jp/3/library/stdtypes.html#text-sequence-type-str)

### 文字列 str

> Python のテキストデータは str オブジェクト、すなわち 文字列 として扱われます。文字列は Unicode コードポイントのイミュータブルな シーケンス です。

### 記述

#### 引用符

> 文字列リテラルには様々な記述方法があります:

> * シングルクォート: '"ダブル" クォートを埋め込むことができます'

> * ダブルクォート: "'シングル' クォートを埋め込むことができます"。

> * 三重引用符: '''三つのシングルクォート''', """三つのダブルクォート"""

> 三重引用符文字列は、複数行に分けることができます。関連付けられる空白はすべて文字列リテラルに含まれます。

```python
print('abc')
print("ABC")
print('''abc
def''')
print("""ABC
DEF""")
```
```sh
$ python 0.py 
abc
ABC
abc
def
ABC
DEF
```

### 結合

> 単式の一部であり間に空白のみを含む文字列リテラルは、一つの文字列リテラルに暗黙に変換されます。つまり、("spam " "eggs") == "spam eggs" です。

```python
print('abc' 'def')
print("abc" "def")
print('abc' "def")
print("abc" 'def')

print('abc ' 'def')
print('abc  ' 'def')
print('abc  ' ' def')
print('abc  ' '  def')
```
```sh
$ python 1.py 
abcdef
abcdef
abcdef
abcdef
abc def
abc  def
abc   def
abc    def
```

### raw文字列

> エスケープシーケンスを含む文字列や、ほとんどのエスケープシーケンス処理を無効にする r (“raw”) 接頭辞などの、文字列リテラルの様々な形式は、文字列およびバイト列リテラル を参照してください。

* [文字列およびバイト列リテラル](https://docs.python.jp/3/reference/lexical_analysis.html#strings)

```python
print('\t\n')
print(r'\t\n')
```
```sh
$ python 2.py 
	

\t\n
```

### str()

文字列は他のオブジェクトに str コンストラクタを使うことでも生成できます。

“character” 型が特別に用意されているわけではないので、文字列のインデックス指定を行うと長さ 1 の文字列を作成します。つまり、空でない文字列 s に対し、s[0] == s[0:1] です。

ミュータブルな文字列型もありませんが、ミュータブルな断片から効率よく文字列を構成するのに str.join() や io.StringIO が使えます。

バージョン 3.3 で変更: Python 2 シリーズとの後方互換性のため、文字列リテラルの u 接頭辞が改めて許可されました。それは文字列リテラルとしての意味には影響がなく、 r 接頭辞と結合することはできません。


```python
print(str(123))
print(''.join(['abc', 'def']))
import io
strio = io.StringIO()
strio.write('abc')
strio.write('def')
print(strio.getvalue())
strio.close()
```
```sh
$ python 3.py 
123
abcdef
abcdef
```

#### r''とu''の結合

```python
print(r'\r\n' + u'abc')
```
```sh
$ python 4.py 
\r\nabc
```

> バージョン 3.3 で変更: Python 2 シリーズとの後方互換性のため、文字列リテラルの u 接頭辞が改めて許可されました。それは文字列リテラルとしての意味には影響がなく、 r 接頭辞と結合することはできません。

とのことだが、結合できているように見える。

## str

### コンストラクタ

* class str(object='')
* class str(object=b'', encoding='utf-8', errors='strict')

> object の 文字列 版を返します。 object が与えられなかった場合、空文字列が返されます。それ以外の場合 str() の動作は、 encoding や errors が与えられたかどうかによって次のように変わります。

> encoding も errors も与えられない場合、 str(object) は object.__str__() の結果を返します。これは “略式の” つまり読み易い object の文字列表現です。文字列オブジェクトに対してはその文字列自体を返します。 object が __str__() メソッドを持たない場合、str() は代わりに repr(object) の結果を返します。

> encoding か errors の少なくとも一方が与えられた場合、 object は bytes-like object (たとえば bytes や bytearray) でなくてはなりません。object が bytes (もしくは bytearray) オブジェクトである場合は、 str(bytes, encoding, errors) は bytes.decode(encoding, errors) と等価です。そうでない場合は、 bytes.decode() が呼ばれる前に buffer オブジェクトの下層にある bytes オブジェクトが取得されます。 buffer オブジェクトについて詳しい情報は、 バイナリシーケンス型 — bytes, bytearray, memoryview や バッファプロトコル (buffer Protocol) を参照してください。

> encoding 引数や errors 引数無しに bytes オブジェクトを str() に渡すと、略式の文字列表現を返す 1 つ目の場合に該当します。(Python のコマンドラインオプション -b も参照してください) 例えば:

```python
>>> str(b'Zoot!')
"b'Zoot!'"
```

> str クラスとそのメソッドについて詳しくは、 テキストシーケンス型 — str や 文字列メソッド の節を参照してください。フォーマットされた文字列を出力するには、 フォーマット済み文字列リテラル と カスタムの文字列書式化 の節を参照してください。加えて、 テキスト処理サービス の節も参照してください。

* [フォーマット済み文字列リテラル](https://docs.python.jp/3/reference/lexical_analysis.html#f-strings)
* [カスタムの文字列書式化](https://docs.python.jp/3/library/string.html#string-formatting)
* [テキスト処理サービス](https://docs.python.jp/3/library/text.html#stringservices)

```python
print(str(123))
print(str(b'abc'))
print(str(b'abc', encoding='utf-8'))
print(b'abc'.decode(encoding='utf-8'))
```
```sh
$ python 5.py 
123
b'abc'
abc
abc
```

