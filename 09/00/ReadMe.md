# [6.1.3.1. 書式指定ミニ言語仕様](https://docs.python.jp/3/library/string.html#format-specification-mini-language)

< [6.1.3. 書式指定文字列の文法](https://docs.python.jp/3/library/string.html#format-string-syntax) < [6.1. string — 一般的な文字列操作](https://docs.python.jp/3/library/string.html#module-string) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## 書式指定

> 書式指定 (“Format specifications”) は書式指定文字列の個々の値を表現する方法を指定するための、置換フィールドで使用されます (書式指定文字列の文法 および フォーマット済み文字列リテラル を参照してください) 。 それらは、組み込み関数の format() 関数に直接渡されます。 それぞれの書式指定可能な型について、書式指定がどのように解釈されるかが規定されます。

* [書式指定文字列の文法](https://docs.python.jp/3/library/string.html#formatstrings)
* [フォーマット済み文字列リテラル](https://docs.python.jp/3/reference/lexical_analysis.html#f-strings)
* [format()](https://docs.python.jp/3/library/functions.html#format)

### オプション(書式指定子)

> 多くの組み込み型は、書式指定に関して以下のオプションを実装します。しかしながら、いくつかの書式指定オプションは数値型でのみサポートされます。

> 一般的な取り決めとして、空の書式指定文字列 ("") は、値に対して str() を呼び出したときと同じ結果を与えます。通常、空でない書式指定文字列はその結果を変更します。

> 一般的な書式指定子 (standard format specifier) の書式は以下です:

```
format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
fill            ::=  <any character>
align           ::=  "<" | ">" | "=" | "^"
sign            ::=  "+" | "-" | " "
width           ::=  integer
grouping_option ::=  "_" | ","
precision       ::=  integer
type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
```

## align

> 有効な align 値を指定する場合、その前に fill 文字を付けることができます。 この文字には任意の文字を指定でき、省略された場合はデフォルトの空白文字となります。 formatted string literal の中や str.format() メソッドを使う場合はリテラルの波括弧 (“{” と “}”) を fill 文字として使えないことに注意してください。 ただし、波括弧を入れ子になった置換フィールド内に挿入することはできます。 この制限は format() 関数には影響しません。

> 様々な align オプションの意味は以下のとおりです:

オプション|意味
----------|----
`<`|左詰め
`>`|右詰め
`=`|符号の後ろを埋めます。`+000000120`のような形で表示されます。
`^`|中央寄せ

> 最小のフィールド幅が定義されない限り、フィールド幅はデータを表示するために必要な幅と同じになることに注意して下さい。そのため、その場合には、 align オプションは意味を持ちません。

```python
#!python3.6
import string
d = {'name': 'Yamada', 'age': -64}
print(string.Formatter().format('{name} {age}', **d))
print('{name} {age}'.format(**d))
print(f'{d["name"]} {d["age"]}')

print(string.Formatter().format('{name:<8} {age:<8}', **d))
print('{name:<8} {age:<8}'.format(**d))
print(f'{d["name"]:<8} {d["age"]:<8}')

print(string.Formatter().format('{name:>8} {age:>8}', **d))
print('{name:>8} {age:>8}'.format(**d))
print(f'{d["name"]:>8} {d["age"]:>8}')

print(string.Formatter().format('{name:^8} {age:^8}', **d))
print('{name:^8} {age:^8}'.format(**d))
print(f'{d["name"]:^8} {d["age"]:^8}')

d = {'name': 'Yamada', 'age': -64}
print(string.Formatter().format('{name} {age}', **d))
print('{name} {age}'.format(**d))
print(f'{d["name"]} {d["age"]}')

print(string.Formatter().format('{name} {age:=8}', **d))
print('{name} {age:=8}'.format(**d))
print(f'{d["name"]} {d["age"]:=8}')

print(string.Formatter().format('{name} {age:=08}', **d))
print('{name} {age:=08}'.format(**d))
print(f'{d["name"]} {d["age"]:=08}')
```
```sh
$ python 0.py 
Yamada -64
Yamada -64
Yamada -64
Yamada   -64     
Yamada   -64     
Yamada   -64     
  Yamada      -64
  Yamada      -64
  Yamada      -64
 Yamada    -64   
 Yamada    -64   
 Yamada    -64   
Yamada -64
Yamada -64
Yamada -64
Yamada -     64
Yamada -     64
Yamada -     64
Yamada -0000064
Yamada -0000064
Yamada -0000064
```

## sign

> sign オプションは数値型に対してのみ有効であり、以下のうちのひとつとなります:

オプション|意味
----------|----
`+`|符号の使用を、正数、負数の両方に対して指定します。
`-`|符号の使用を、負数に対してのみ指定します (デフォルトの挙動です)。
空白|空白を正数の前に付け、負号を負数の前に使用することを指定します。

```python
#!python3.6
import string
d = {'name': 'Yamada', 'age': 64}
print(string.Formatter().format('{name} {age:+}', **d))
print('{name} {age:+}'.format(**d))
print(f'{d["name"]} {d["age"]:+}')

print(string.Formatter().format('{name} {age: }', **d))
print('{name} {age: }'.format(**d))
print(f'{d["name"]} {d["age"]: }')

d = {'name': 'Yamada', 'age': -64}
print(string.Formatter().format('{name} {age:-}', **d))
print('{name} {age:-}'.format(**d))
print(f'{d["name"]} {d["age"]:-}')
```
```sh
$ python 1.py 
Yamada +64
Yamada +64
Yamada +64
Yamada  64
Yamada  64
Yamada  64
Yamada -64
Yamada -64
Yamada -64
```

## `#`

> '#' オプションは、変換に「別形式」を使用します。別形式は、異なる型に対して違った風に定義されます。このオプションは、整数、浮動小数点数、複素数、10進数の型でのみ有効です。整数に対して2進法、8進法、または16進法の出力が使用される場合、このオプションは出力される値にそれぞれ '0b', '0o', '0x' 接頭辞を加えます。浮動小数点数、複素数、10進数については、別形式では、小数点文字の後に数字がなくても変換結果には常に小数点文字が含まれます。通常は、数字が続く場合にのみ小数点文字がこれらの変換結果に現われます。さらに、'g' と 'G' の変換については、最後の 0 は結果から取り除かれません。

```python
#!python3.6
import string
v = 15
print(string.Formatter().format('{v:#}', v=v))
print('{v:#}'.format(v=v))
print(f'{v:#}')

print(string.Formatter().format('{v:#b}', v=v))
print(string.Formatter().format('{v:#o}', v=v))
print(string.Formatter().format('{v:#d}', v=v))
print(string.Formatter().format('{v:#x}', v=v))
print(string.Formatter().format('{v:#X}', v=v))
print('{v:#b}'.format(v=v))
print('{v:#o}'.format(v=v))
print('{v:#d}'.format(v=v))
print('{v:#x}'.format(v=v))
print('{v:#X}'.format(v=v))
print(f'{v:#b}')
print(f'{v:#o}')
print(f'{v:#d}')
print(f'{v:#x}')
print(f'{v:#X}')

v = 1.23
print(string.Formatter().format('{v:#g}', v=v))
print(string.Formatter().format('{v:#G}', v=v))
print('{v:#g}'.format(v=v))
print('{v:#G}'.format(v=v))
print(f'{v:#g}')
print(f'{v:#G}')
#v = 987654321.12345
v = 100.200
print(string.Formatter().format('{v:#g}', v=v))
print(string.Formatter().format('{v:#G}', v=v))
print('{v:#g}'.format(v=v))
print('{v:#G}'.format(v=v))
print(f'{v:#g}')
print(f'{v:#G}')
```
```sh
$ python 2.py 
15
15
15
0b1111
0o17
15
0xf
0XF
0b1111
0o17
15
0xf
0XF
0b1111
0o17
15
0xf
0XF
1.23000
1.23000
1.23000
1.23000
1.23000
1.23000
100.200
100.200
100.200
100.200
100.200
100.200
```

16進数`0xF`の書式にはできないのか……。`0XF`は読みづらい。`0x1f`より`0x1F`のほうが見やすい。かゆいところに手が届かないというか、わざとかゆくしてないか？

## `,`

> ',' オプションは、千の位のセパレータにカンマを使うことを合図します。ロケール依存のセパレータには、代わりに 'n' の整数表現形式を使ってください。

> バージョン 3.1 で変更: ',' オプションが追加されました (PEP 378 も参照)。

## `_`

> '_' オプションは、浮動小数点数の表現型と整数の表現型 'd' における千倍ごとの区切り文字にアンダースコアを使うというしるしです。 整数の表現型の 'b', 'o', 'x', 'X' では、4桁ごとにアンダースコアが挿入されます。 他の表現型でこのオプションを指定するとエラーになります。

> バージョン 3.6 で変更: '_' オプションが追加されました (PEP 515 も参照)。

```python
#!python3.6
import string

v = 12345.6789012
print(string.Formatter().format('{v:,}', v=v))
print('{v:,}'.format(v=v))
print(f'{v:,}')

print(string.Formatter().format('{v:_}', v=v))
print('{v:_}'.format(v=v))
print(f'{v:_}')

v = 0xFFFF
print(string.Formatter().format('{v:,}', v=v))
print('{v:,}'.format(v=v))
print(f'{v:,}')

print(string.Formatter().format('{v:_}', v=v))
print('{v:_}'.format(v=v))
print(f'{v:_}')
```
```sh
$ python 3.py 
12,345.6789012
12,345.6789012
12,345.6789012
12_345.6789012
12_345.6789012
12_345.6789012
65,535
65,535
65,535
65_535
65_535
65_535
```

## `width`

> width は10進数の整数で、最小のフィールド幅を定義します。指定されない場合、フィールド幅はその内容により決定されます。

[align](#align)参照。

## 符号つきゼロ埋め

> alignment が明示的に与えられない場合、 width フィールドにゼロ ('0') 文字を前置することは、数値型のための符号を意識した 0 パディングを可能にします。これは fill 文字に '0' を指定して、 alignment タイプに '=' を指定したことと等価です。

[align](#align)参照。

## `precision`

> precision は10進数で、'f' および 'F' で指定される浮動小数点数の小数点以下、あるいは 'g' および 'G' で指定される浮動小数点数の小数点の前後に表示される桁数を指定します。非数型に対しては、最大フィールド幅を表します。言い換えると、フィールドの内容から何文字を使用するかということです。precision は整数型に対しては使うことができません。

```python
#!python3.6
import string
v = 1.23456789
print(string.Formatter().format('{v:.3f}', v=v))
print('{v:.3f}'.format(v=v))
print(f'{v:.3f}')

v = 123456789.987654321
print(string.Formatter().format('{v:.3e}', v=v))
print('{v:.3e}'.format(v=v))
print(f'{v:.3e}')

v = 123456789.987654321j+8
print(string.Formatter().format('{v:.3g}', v=v))
print('{v:.3g}'.format(v=v))
print(f'{v:.3g}')
```
```sh
$ python 4.py 
1.235
1.235
1.235
1.235e+08
1.235e+08
1.235e+08
8+1.23e+08j
8+1.23e+08j
8+1.23e+08j
```

## `type`

> 最後に、type は、データがどのように表現されるかを決定します。

```python
#!python3.6
import string
print('----------整数の表現型----------')
v = 15
print(string.Formatter().format('{v:b}', v=v))
print(string.Formatter().format('{v:o}', v=v))
print(string.Formatter().format('{v:d}', v=v))
print(string.Formatter().format('{v:x}', v=v))
print(string.Formatter().format('{v:X}', v=v))
print('{v:b}'.format(v=v))
print('{v:o}'.format(v=v))
print('{v:d}'.format(v=v))
print('{v:x}'.format(v=v))
print('{v:X}'.format(v=v))
print(f'{v:b}')
print(f'{v:o}')
print(f'{v:d}')
print(f'{v:x}')
print(f'{v:X}')

v = 0
print(string.Formatter().format('{v:c}', v=v))
print('{v:c}'.format(v=v))
print(f'{v:c}')

v = 1234567890
print(string.Formatter().format('{v:n}', v=v))
print('{v:n}'.format(v=v))
print(f'{v:n}')

print('----------浮動小数点数と10進数の表現型----------')
v = 1234567890
print(string.Formatter().format('{v:e}', v=v))
print('{v:e}'.format(v=v))
print(f'{v:e}')
print(string.Formatter().format('{v:E}', v=v))
print('{v:E}'.format(v=v))
print(f'{v:E}')
print(string.Formatter().format('{v:.3e}', v=v))
print('{v:.3e}'.format(v=v))
print(f'{v:.3e}')
print(string.Formatter().format('{v:.3E}', v=v))
print('{v:.3E}'.format(v=v))
print(f'{v:.3E}')
print(string.Formatter().format('{v:g}', v=v))
print('{v:g}'.format(v=v))
print(f'{v:g}')
print(string.Formatter().format('{v:G}', v=v))
print('{v:G}'.format(v=v))
print(f'{v:G}')

v = 0.1234567890
print(string.Formatter().format('{v:f}', v=v))
print('{v:f}'.format(v=v))
print(f'{v:f}')
print(string.Formatter().format('{v:F}', v=v))
print('{v:F}'.format(v=v))
print(f'{v:F}')
print(string.Formatter().format('{v:.3f}', v=v))
print('{v:.3f}'.format(v=v))
print(f'{v:.3f}')
print(string.Formatter().format('{v:.3F}', v=v))
print('{v:.3F}'.format(v=v))
print(f'{v:.3F}')
print(string.Formatter().format('{v:g}', v=v))
print('{v:g}'.format(v=v))
print(f'{v:g}')
print(string.Formatter().format('{v:G}', v=v))
print('{v:G}'.format(v=v))
print(f'{v:G}')

v = 1234567890
print(string.Formatter().format('{v:n}', v=v))
print('{v:n}'.format(v=v))
print(f'{v:n}')

v = 0.5
print(string.Formatter().format('{v:%}', v=v))
print('{v:%}'.format(v=v))
print(f'{v:%}')
v = 0.123456789
print(string.Formatter().format('{v:.3%}', v=v))
print('{v:.3%}'.format(v=v))
print(f'{v:.3%}')
v = 0.999999999
print(string.Formatter().format('{v:.3%}', v=v))
print('{v:.3%}'.format(v=v))
print(f'{v:.3%}')
```
```sh
$ python 5.py 
----------整数の表現型----------
1111
17
15
f
F
1111
17
15
f
F
1111
17
15
f
F



1234567890
1234567890
1234567890
----------浮動小数点数と10進数の表現型----------
1.234568e+09
1.234568e+09
1.234568e+09
1.234568E+09
1.234568E+09
1.234568E+09
1.235e+09
1.235e+09
1.235e+09
1.235E+09
1.235E+09
1.235E+09
1.23457e+09
1.23457e+09
1.23457e+09
1.23457E+09
1.23457E+09
1.23457E+09
0.123457
0.123457
0.123457
0.123457
0.123457
0.123457
0.123
0.123
0.123
0.123
0.123
0.123
0.123457
0.123457
0.123457
0.123457
0.123457
0.123457
1234567890
1234567890
1234567890
50.000000%
50.000000%
50.000000%
12.346%
12.346%
12.346%
100.000%
100.000%
100.000%
```

> 利用可能な文字列の表現型は以下です:

型|意味
--|----
`s`|文字列。これがデフォルトの値で、多くの場合省略されます。
`None`|`s` と同じです。

> 利用可能な整数の表現型は以下です:

型|意味
--|----
`b`|2進数。出力される数値は2を基数とします。
`c`|文字。数値を対応する Unicode 文字に変換します。
`d`|10進数。出力される数値は10を基数とします。
`o`|8進数。出力される数値は8を基数とします。
`x`|16進数。出力される数値は16を基数とします。 10進で9を越える数字には小文字が使われます。
`X`|16進数。出力される数値は16を基数とします。 10進で9を越える数字には大文字が使われます。
`n`|数値。現在のロケールに従い、区切り文字を挿入することを除けば、 `d` と同じです。
`None`|`d` と同じです。

> これらの表現型に加えて、整数は ('n' と None を除く) 以下の浮動小数点数の表現型で書式指定できます。 そうすることで整数は書式変換される前に float() を使って浮動小数点数に変換されます。

> 利用可能な浮動小数点数と10進数の表現型は以下です:

型|意味
--|----
'e`|指数表記です。指数を示す ‘e’ を使って数値を表示します。デフォルトの精度は 6 です。
'E`|指数表記です。大文字の ‘E’ を使うことを除いては、 'e' と同じです。
'f`|固定小数点数です。数値を固定小数点数として表示します。デフォルトの精度は 6 です。
'F`|固定小数点数です。nan が NAN に、inf が INF に変換されることを除き 'f' と同じです。
'g`|汎用フォーマットです。精度を p >= 1 の数値で与えた場合、数値を有効桁 p で丸め、桁に応じて固定小数点か指数表記で表示します。
'G`|汎用フォーマットです。数値が大きくなったとき、 'E' に切り替わることを除き、 'g' と同じです。無限大と NaN の表示も大文字になります。
'n`|数値です。現在のロケールに合わせて、数値分割文字が挿入されることを除き、 'g' と同じです。
'%`|パーセンテージです。数値は 100 倍され、固定小数点数フォーマット ('f') でパーセント記号付きで表示されます。
`None`|'g' に似ていますが、固定小数点表記を使ったとき、小数点の後に少なくとも 1 つの数字があることが異なります。

### `g`の補足

> 精度のルールは以下のように決まっています: 書式指定の結果が 'e' 型で p-1 の精度の場合、指数は exp になると仮定します。そうすると、 -4 <= exp < p のとき数値は表現型 'f' で精度 p-1-exp に書式変換されます。それ以外の場合、数値は 'e' 型で精度 p-1 に書式指定されます。この両方の場合で重要でない、連続した 0 は取り除かれます, そして残った桁が無い場合小数点は取り除かれます。

> 正と負の無限大と 0 および NaN は精度に関係なくそれぞれ inf, -inf, 0, -0 および nan となります。

> 0 の精度は 1 の精度と同等に扱われます。デフォルトの精度は 6 です。

### `None`の補足

デフォルトの精度は、その値を表現するのに必要なだけの高さです。全体的な効果は、他のフォーマット修飾子で変更されていても str() の出力と一致するようになっています。

