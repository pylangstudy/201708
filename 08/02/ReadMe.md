# [6.1.3. 書式指定文字列の文法](https://docs.python.jp/3/library/string.html#format-string-syntax)

< [6.1. string — 一般的な文字列操作](https://docs.python.jp/3/library/string.html#module-string) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## 文法

> str.format() メソッドと Formatter クラスは、文字列の書式指定に同じ文法を共有します (ただし、 Formatter サブクラスでは、独自の書式指定文法を定義することが可能です)。 この文法は フォーマット済み文字列リテラル の文法と関係してはいますが、異なるものです。

コード|書式指定文字列の文法
------|--------------------
[str.format()](https://docs.python.jp/3/library/stdtypes.html#str.format), [string.Formatter](https://docs.python.jp/3/library/string.html#string.Formatter)|ここで説明する文法
`f''`|[フォーマット済み文字列リテラル](https://docs.python.jp/3/reference/lexical_analysis.html#f-strings)の文法

コードの記法ごとに異なる文法を用いるらしい。

```python
import string
import datetime
print(string.Formatter().format('現在日時は{0:%Y-%m-%d %H:%M:%S.%f}です。', datetime.datetime.now()))
print('現在日時は{0:%Y-%m-%d %H:%M:%S.%f}です。'.format(datetime.datetime.now()))
print(f'現在日時は{datetime.datetime.now():%Y-%m-%d %H:%M:%S.%f}です。')
```
```sh
$ python 0.py 
現在日時は2017-08-08 08:59:55.735793です。
現在日時は2017-08-08 08:59:55.736302です。
現在日時は2017-08-08 08:59:55.736561です。
```

## 置換フィールド`{}`

> 書式指定文字列は波括弧 {} に囲まれた “置換フィールド” を含みます。波括弧に囲まれた部分以外は全て単純な文字として扱われ、変更を加えることなく出力へコピーされます。波括弧を文字として扱う必要がある場合は、二重にすることでエスケープすることができます: {{ および }} 。

```python
import string
import datetime
print(string.Formatter().format('現在日時は{{0:%Y-%m-%d %H:%M:%S.%f}}です。', datetime.datetime.now()))
print('現在日時は{{0:%Y-%m-%d %H:%M:%S.%f}}です。'.format(datetime.datetime.now()))
print(f'現在日時は{{datetime.datetime.now():%Y-%m-%d %H:%M:%S.%f}}です。')
```
```sh
$ python 1.py 
現在日時は{0:%Y-%m-%d %H:%M:%S.%f}です。
現在日時は{0:%Y-%m-%d %H:%M:%S.%f}です。
現在日時は{datetime.datetime.now():%Y-%m-%d %H:%M:%S.%f}です。
```

### 置換フィールドの文法

```
replacement_field ::=  "{" [field_name] ["!" conversion] [":" format_spec] "}"
field_name        ::=  arg_name ("." attribute_name | "[" element_index "]")*
arg_name          ::=  [identifier | integer]
attribute_name    ::=  identifier
element_index     ::=  integer | index_string
index_string      ::=  <any source character except "]"> +
conversion        ::=  "r" | "s" | "a"
format_spec       ::=  <described in the next section>
```

こんなの見せられてもわからない。以下、コードで書いてみた。

## ソースコード

```python
import string
import datetime
print('{}'.format('A'))
print('{} {}'.format('A', 'B'))
print('{0} {1} {0} {1}'.format('A', 'B'))
print('{name}'.format(name='A'))
print('私は{name}、{age}歳。'.format(name='山田太郎', age=99))

t = ('山田太郎', 99)
print('私は{0[0]}、{0[1]}歳。'.format(t))
print('私は{t[0]}、{t[1]}歳。'.format(t=t))

d = {'name':'山田太郎', 'age':99}
print('私は{name}、{age}歳。'.format(**d))

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
h = Human('鈴木一郎', 88)
print('私は{0.name}、{0.age}歳。'.format(h))
print('私は{h.name}、{h.age}歳。'.format(h=h))
print('私は{name}、{age}歳。'.format(name=h.name, age=h.age))

print('{}'.format(h))
print('{!r}'.format(h))
print('{!s}'.format(h))
print('{!a}'.format(h))
print('{h!r}'.format(h=h))
print('{h!s}'.format(h=h))
print('{h!a}'.format(h=h))
print('{h.name!r}'.format(h=h))
print('{h.name!s}'.format(h=h))
print('{h.name!a}'.format(h=h))
print('{h.age!r}'.format(h=h))
print('{h.age!s}'.format(h=h))
print('{h.age!a}'.format(h=h))

print('{h.name!r:>16}'.format(h=h))#文字幅が1,2の違いがありズレる
print('{h.age!r:>16}'.format(h=h))
h = Human('Tanaka', 77)
print('{h.name!r:>16}'.format(h=h))
print('{h.age!r:>16}'.format(h=h))
print('{h.name!s:>16}'.format(h=h))
print('{h.age!s:>16}'.format(h=h))
```
```sh
$ python 2.py 
A
A B
A B A B
A
私は山田太郎、99歳。
私は山田太郎、99歳。
私は山田太郎、99歳。
私は山田太郎、99歳。
私は鈴木一郎、88歳。
私は鈴木一郎、88歳。
私は鈴木一郎、88歳。
<__main__.Human object at 0xb7105f2c>
<__main__.Human object at 0xb7105f2c>
<__main__.Human object at 0xb7105f2c>
<__main__.Human object at 0xb7105f2c>
<__main__.Human object at 0xb7105f2c>
<__main__.Human object at 0xb7105f2c>
<__main__.Human object at 0xb7105f2c>
'鈴木一郎'
鈴木一郎
'\u9234\u6728\u4e00\u90ce'
88
88
88
          '鈴木一郎'
              88
        'Tanaka'
              77
          Tanaka
              77
```

