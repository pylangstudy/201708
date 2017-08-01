# [4.6.5. タプル型 (tuple)](https://docs.python.jp/3/library/stdtypes.html#tuples)

< [4.6. シーケンス型 — list, tuple, range](https://docs.python.jp/3/library/stdtypes.html#sequence-types-list-tuple-range) < [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

> タプルはイミュータブルなシーケンスで、一般的に異種のデータの集まり (組み込みの enumerate() で作られた 2-タプルなど) を格納するために使われます。タプルはまた、同種のデータのイミュータブルなシーケンスが必要な場合 (set インスタンスや dict インスタンスに保存できるようにするためなど) にも使われます。

## class tuple([iterable])

### タプル生成

* `()`
* `a,`
* `(a,)`
* `a, b, c`
* `(a, b, c)`
* `tuple()`
* `tuple(iterable)`

## ソースコード

### リスト生成

```python
print(())
print((1,))
print((1,2,3))
print(tuple())
print(tuple((1,)))
print(tuple((1,2,3)))
print(tuple([1,2,3]))
```
```sh
$ python 0.py 
()
(1,)
(1, 2, 3)
()
(1,)
(1, 2, 3)
(1, 2, 3)
```

### [collections.namedtuple](https://docs.python.jp/3/library/collections.html#collections.namedtuple)

名前付きタプル。

```python
import collections
Point = collections.namedtuple('Point', ['x','y'])
p = Point(x=11, y=22)
print(p)
print(p.x, p.y)
print(p[0], p[1])
```
```sh
$ python 1.py 
Point(x=11, y=22)
11 22
11 22
```

