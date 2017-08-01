# [4.6.4. リスト型 (list)](https://docs.python.jp/3/library/stdtypes.html#lists)

< [4.6. シーケンス型 — list, tuple, range](https://docs.python.jp/3/library/stdtypes.html#sequence-types-list-tuple-range) < [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

> リストはミュータブルなシーケンスで、一般的に同種の項目の集まりを格納するために使われます (厳密な類似の度合いはアプリケーションによって異なる場合があります)。

## class list([iterable])

### リスト生成

* `[]`
* `[a]`
* `[a, b, c]`
* `[x for x in iterable]`
* `list()`
* `list(iterable)`

> 以下のテーブルにある演算は、ほとんどのミュータブルなシーケンスでサポートされています。カスタムのシーケンス型にこれらの演算を完全に実装するのが簡単になるように、 collections.abc.MutableSequence ABC が提供されています。

* [collections.abc.MutableSequence](https://docs.python.jp/3/library/collections.abc.html#collections.abc.MutableSequence)

> このテーブルで、 s はミュータブルなシーケンス型のインスタンス、 t は任意のイテラブルオブジェクト、 x は s に課された型と値の条件を満たす任意のオブジェクト (例えば、 bytearray は値の制限 0 <= x <= 255 に合う整数のみを受け付けます) です。

## ソースコード

### リスト生成

```python
print([])
print([1])
print([1,2,3])
print([x*10 for x in range(10)])
print(list())
print(list((1,2,3)))
```
```sh
$ python 0.py 
[]
[1]
[1, 2, 3]
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
[]
[1, 2, 3]
```

### sort

```python
s = [2,4,3,1]
s.sort()
print(s)
s.reverse()
print(s)

s = ['1', '2', '12']
print(s)
s.sort()
print(s)
s.sort(key=lambda x:int(x))
print(s)

s.sort(reverse=True)
print(s)
s.sort(key=lambda x:int(x), reverse=True)
print(s)
```
```sh
$ python 1.py 
[1, 2, 3, 4]
[4, 3, 2, 1]
['1', '2', '12']
['1', '12', '2']
['1', '2', '12']
['2', '12', '1']
['12', '2', '1']
```

