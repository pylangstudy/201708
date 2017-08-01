# [4.6.3. ミュータブルなシーケンス型](https://docs.python.jp/3/library/stdtypes.html#mutable-sequence-types)

< [4.6. シーケンス型 — list, tuple, range](https://docs.python.jp/3/library/stdtypes.html#sequence-types-list-tuple-range) < [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## [4.6.3. ミュータブルなシーケンス型](https://docs.python.jp/3/library/stdtypes.html#mutable-sequence-types)

> 以下のテーブルにある演算は、ほとんどのミュータブルなシーケンスでサポートされています。カスタムのシーケンス型にこれらの演算を完全に実装するのが簡単になるように、 collections.abc.MutableSequence ABC が提供されています。

* [collections.abc.MutableSequence](https://docs.python.jp/3/library/collections.abc.html#collections.abc.MutableSequence)

> このテーブルで、 s はミュータブルなシーケンス型のインスタンス、 t は任意のイテラブルオブジェクト、 x は s に課された型と値の条件を満たす任意のオブジェクト (例えば、 bytearray は値の制限 0 <= x <= 255 に合う整数のみを受け付けます) です。

## ソースコード

```python
s = list(range(10))
print(s)
s[3] = 333
print(s)
s[3:6] = [33,44,55]
print(s)
del s[3:6]
print(s)

s = list(range(10))
del s[2:9:3]
print(s)

s = []
print(s)
s.append(111)
print(s)
s.append(222)
print(s)
s.clear()
print(s)

s0 = s.copy()
print(s0, s)
s0.append(123)
print(s0, s)

s = [1,2] + [3,4]
print(s)
s.extend([5,6])
print(s)
s.insert(3, 34)
print(s)
print(s.pop())
print(s)
s.reverse()
print(s)
s.remove(34)
print(s)
del s[0]
print(s)

s = [1,2]
print(s)
s *= 2
print(s)
```
```sh
$ python 0.py 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 333, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 33, 44, 55, 6, 7, 8, 9]
[0, 1, 2, 6, 7, 8, 9]
[0, 1, 3, 4, 6, 7, 9]
[]
[111]
[111, 222]
[]
[] []
[123] []
[1, 2, 3, 4]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 34, 4, 5, 6]
6
[1, 2, 3, 34, 4, 5]
[5, 4, 34, 3, 2, 1]
[5, 4, 3, 2, 1]
[4, 3, 2, 1]
[1, 2]
[1, 2, 1, 2]
```

