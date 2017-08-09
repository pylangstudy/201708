# [6.1.3.2. 書式指定例](https://docs.python.jp/3/library/string.html#format-examples)

< [6.1.3. 書式指定文字列の文法](https://docs.python.jp/3/library/string.html#format-string-syntax) < [6.1. string — 一般的な文字列操作](https://docs.python.jp/3/library/string.html#module-string) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## 書式

> この節では、 str.format() 構文の例を紹介し、さらに従来の %-書式と比較します。

> 多くの場合、新構文に {} を加え、 % の代わりに : を使うことで、古い %-書式に類似した書式になります。例えば、'%03.2f' は '{:03.2f}' と変換できます。

> 以下の例で示すように、新構文はさらに新たに様々なオプションもサポートしています。


## 位置引数を使ったアクセス:

```python
#!python3.6
import string
print('{0}, {1}, {2}'.format('a', 'b', 'c'))
print('{}, {}, {}'.format('a', 'b', 'c'))
print('{2}, {1}, {0}'.format('a', 'b', 'c'))
print('{2}, {1}, {0}'.format(*'abc'))
print('{0}{1}{0}'.format('abra', 'cad'))
```
```sh
$ python 0.py 
a, b, c
a, b, c
c, b, a
c, b, a
abracadabra
```

## 名前を使ったアクセス:

```python
#!python3.6
print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordinates: {latitude}, {longitude}'.format(**coord))
```
```sh
 $ python 1.py 
Coordinates: 37.24N, -115.81W
Coordinates: 37.24N, -115.81W
```

## 引数の属性へのアクセス:

```python
#!python3.6
c = 3-5j
print(('The complex number {0} is formed from the real part {0.real} '
 'and the imaginary part {0.imag}.').format(c))
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)
print(str(Point(4, 2)))
```
```sh
$ python 2.py 
The complex number (3-5j) is formed from the real part 3.0 and the imaginary part -5.0.
Point(4, 2)
```

## 引数の要素へのアクセス:

```python
#!python3.6
coord = (3, 5)
print('X: {0[0]};  Y: {0[1]}'.format(coord))
```
```sh
$ python 3.py 
X: 3;  Y: 5
```

## %s と %r の置き換え:

```python
#!python3.6
print("repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2'))
```
```sh
$ python 4.py 
repr() shows quotes: 'test1'; str() doesn't: test2
```

## テキストの幅を指定した整列:

```python
#!python3.6
print('{:<30}'.format('left aligned'))
print('{:>30}'.format('right aligned'))
print('{:^30}'.format('centered'))
print('{:*^30}'.format('centered'))
```
```sh
$ python 5.py 
left aligned                  
                 right aligned
           centered           
***********centered***********
```

## %+f と %-f, % f の置換、そして符号の指定:

```python
#!python3.6
print('{:+f}; {:+f}'.format(3.14, -3.14))
print('{: f}; {: f}'.format(3.14, -3.14))
print('{:-f}; {:-f}'.format(3.14, -3.14))
```
```sh
$ python 6.py 
+3.140000; -3.140000
 3.140000; -3.140000
3.140000; -3.140000
```

## %x と %o の置換、そして値に対する異なる底の変換:

```python
#!python3.6
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))
```
```sh
$ python 7.py 
int: 42;  hex: 2a;  oct: 52;  bin: 101010
int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010
```

## 千の位のセパレータにカンマを使用する:

```python
#!python3.6
print('{:,}'.format(1234567890))
```
```sh
$ python 8.py 
1,234,567,890
```

## パーセントを表示する:

```python
#!python3.6
points = 19
total = 22
print('Correct answers: {:.2%}'.format(points/total))
```
```sh
$ python 9.py 
Correct answers: 86.36%
```

## 型特有の書式指定を使う:

```python
#!python3.6
import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))
```
```sh
$ python A.py 
2010-07-04 12:15:58
```

## 引数をネストする、さらに複雑な例:

```python
#!python3.6
for align, text in zip('<^>', ['left', 'center', 'right']):
    '{0:{fill}{align}16}'.format(text, fill=align, align=align)
octets = [192, 168, 0, 1]
print('{:02X}{:02X}{:02X}{:02X}'.format(*octets))
print(int(str(octets[0]), 16))

width = 5
for num in range(5,12): 
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()
```
```sh
$ python B.py 
C0A80001
402
    5     5     5   101 
    6     6     6   110 
    7     7     7   111 
    8     8    10  1000 
    9     9    11  1001 
   10     A    12  1010 
   11     B    13  1011 
```

