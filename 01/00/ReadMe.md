# [4.6.2. イミュータブルなシーケンス型](https://docs.python.jp/3/library/stdtypes.html#immutable-sequence-types)

< [4.6. シーケンス型 — list, tuple, range](https://docs.python.jp/3/library/stdtypes.html#sequence-types-list-tuple-range) < [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## 

> イミュータブルなシーケンス型が一般に実装している演算のうち、ミュータブルなシーケンス型がサポートしていないのは、組み込みの hash() だけです。

> このサポートにより、tuple インスタンスのようなイミュータブルなシーケンスは、 dict のキーとして使え、 set や frozenset インスタンスに保存できます。

> ハッシュ不可能な値を含むイミュータブルなシーケンスをハッシュ化しようとすると、 TypeError となります。

* ``

## ソースコード

### dict型のキーにtupleが使える

```python
d = {(1,'a'): '1a', (2,'b'): '2b'}
print(d)
print(d[(1,'a')])
print(d[(2,'b')])
for k, v in d.items(): print(k, v)

s = set(d.keys())
print(s)
fs = frozenset(d.keys())
print(fs)
```
```sh
$ python 0.py 
{(1, 'a'): '1a', (2, 'b'): '2b'}
1a
2b
(1, 'a') 1a
(2, 'b') 2b
{(1, 'a'), (2, 'b')}
frozenset({(1, 'a'), (2, 'b')})
```

* dict型のキーにtupleが使える
* tuple型キーはset,frozensetに保存できる

### 基本

```python
print(3 in (1,2,3,4,5))
print((2,3) in (1,2,3,4,5))
print((1,2,3,4,5) in (1,2,3,4,5))
print(3 not in (1,2,3,4,5))
print((1,2) + (3,4))
print((1,2) * 2)
s = (0,1,2,3,4,5,6,7,8,9)
print(s[3])
print(s[3:7])
print(s[2:9:3])
print(len(s))
print(min(s))
print(max(s))
s0 = tuple(x*10 for x in range(10))
print(s0)
print(s0.count(30))
print(s0.index(30))
print(s0.index(30, 1,4))
print(s0.index(30, 1,3)) #ValueError: 30 is not in list
```
```sh
$ python 1.py 
True
False
False
False
(1, 2, 3, 4)
(1, 2, 1, 2)
3
(3, 4, 5, 6)
(2, 5, 8)
10
0
9
(0, 10, 20, 30, 40, 50, 60, 70, 80, 90)
1
3
3
Traceback (most recent call last):
  File "1.py", line 20, in <module>
    print(s0.index(30, 1,3)) #ValueError: 30 is not in list
ValueError: tuple.index(x): x not in tuple
```

