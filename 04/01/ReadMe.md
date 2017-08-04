# [4.8.5. メモリビュー](https://docs.python.jp/3/library/stdtypes.html#memory-views)

< [4.8. バイナリシーケンス型 — bytes, bytearray, memoryview(原文)](https://docs.python.jp/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview) < [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## [memoryview](https://docs.python.jp/3/library/stdtypes.html#memoryview)

> memoryview オブジェクトは、Python コードが バッファプロトコル をサポートするオブジェクトの内部データへ、コピーすることなくアクセスすることを可能にします。

## class memoryview(obj)

### obj

> obj を参照する memoryview を作成します。 obj はバッファプロトコルをサポートしていなければなりません。バッファプロトコルをサポートする組み込みオブジェクトには、 bytes 、 bytearray などがあります。

### 最小単位

> memoryview は元となるオブジェクト obj が扱うメモリーの最小単位を 要素 として扱います。多くの単純なオブジェクト、例えば bytes や bytearray では、要素は単バイトになりますが、他の array.array 等の型では、要素はより大きくなりえます。

### 長さ

> メモリビューの長さ len(view) は、 tolist で得られるリストの長さとなります。view.ndim = 0 なら、長さは 1 です。view.ndim = 1 なら、長さはビューの要素数と等しいです。より高次元では、長さはビューのネストされたリスト表現の長さと等しいです。要素一つあたりのバイト数は itemsize 属性から取得できます。

### インデクサ

> memoryview はスライスおよびインデックス指定で内容を取得できます。一次元のスライスは部分ビューになります:

```python
b = b'abcefg'
print(b)
v = memoryview(b)
print(v)
print(v[1])
print(v[-1])
print(v[1:4])
print(bytes(v[1:4]))
for i in v: print('{0:#x}'.format(i), end=' ')
```
```sh
$ python 0.py 
b'abcefg'
<memory at 0xb70f050c>
98
103
<memory at 0xb70f04a4>
b'bce'
0x61 0x62 0x63 0x65 0x66 0x67
```

### [struct](https://docs.python.jp/3/library/struct.html)

```python
import struct
b = struct.pack('bBhH', *[127, 255, 32767, 65535])
print(b)
v = memoryview(b)
for i in struct.unpack('bBhH', memoryview(b)): print(i)
```
```sh
$ python 1.py 
b'\x7f\xff\xff\x7f\xff\xff'
127
255
32767
65535
```

> もしメモリビューの format が struct モジュールによって定義されているネイティブのフォーマット指定子であれば、整数または整数のタプルでのインデックス指定により適切な型の 要素1つ を得ることができます。

### [array](https://docs.python.jp/3/library/array.html)

```python
$ python 2.py 
-11111111
44444444
[-11111111, -33333333]
```
```sh
import array
a = array.array('l', [-11111111, 22222222, -33333333, 44444444])
m = memoryview(a)
print(m[0])
print(m[-1])
print(m[::2].tolist())
```

> 一次元のメモリビューでは、整数または整数 1 つのタプルでインデックス指定できます。多次元のメモリビューでは、その次元数を ndim としたとき、ちょうど ndim 個の整数からなるタプルでインデックス指定できます。ゼロ次元のメモリビューでは、空のタプルでインデックス指定できます。

### bytearray

```python
data = bytearray(b'abcefg')
v = memoryview(data)
print(v.readonly)
v[0] = ord(b'z')
print(data)
v[1:4] = b'123'
print(data)
#v[2:3] = b'spam' #ValueError: memoryview assignment: lvalue and rvalue have different structures
v[2:6] = b'spam'
print(data)
```
```sh
$ python 3.py 
False
bytearray(b'zbcefg')
bytearray(b'z123fg')
bytearray(b'z1spam')
```

> メモリビューの参照しているオブジェクトが書き込み可能であれば、一次元スライスでの代入が可能です。ただしサイズの変更はできません

### ハッシュ

```python
v = memoryview(b'abcefg')
print(hash(v) == hash(b'abcefg'))
print(hash(v[2:4]) == hash(b'ce'))
print(hash(v[::-2]) == hash(b'abcefg'[::-2]))
```
```sh
$ python 4.py 
True
True
True
```

> B’, ‘b’, ‘c’ いずれかのフォーマットのハッシュ可能な (読み込み専用の) 型の1次元メモリビューもまた、ハッシュ可能です。ハッシュは hash(m) == hash(m.tobytes()) として定義されています

### バージョン遷移

> バージョン 3.3 で変更: 1 次元のメモリビューがスライス可能になりました。 ‘B’, ‘b’, ‘c’ いずれかのフォーマットの 1 次元のメモリビューがハッシュ可能になりました。

> バージョン 3.4 で変更: memoryview は自動的に collections.abc.Sequence へ登録されるようになりました。

> バージョン 3.5 で変更: メモリビューは整数のタプルでインデックス指定できるようになりました。

## メソッド一覧

6件。

* __eq__(exporter)
* tobytes()
* hex()
* tolist()
* release()
* cast(format[, shape])

各ソースコードファイル参照。

## 変数一覧

11件。

* obj
* nbytes
* readonly
* format
* itemsize
* ndim
* shape
* strides
* suboffsets
* c_contiguous
* f_contiguous
* contiguous

各ソースコードファイル参照。

