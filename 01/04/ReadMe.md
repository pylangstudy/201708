# [4.6.6. range](https://docs.python.jp/3/library/stdtypes.html#ranges)

< [4.6. シーケンス型 — list, tuple, range](https://docs.python.jp/3/library/stdtypes.html#sequence-types-list-tuple-range) < [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## class range(stop), class range(start, stop[, step])

> range 型は、数のイミュータブルなシーケンスを表し、一般に for ループにおいて特定の回数のループに使われます。

## ソースコード

### リスト生成

```python
print('----- range(3) -----')
print(range(3))
for x in range(3): print(x)
print('----- range(3, 10) -----')
print(range(3, 10))
for x in range(3, 10): print(x)
print('----- range(-3) -----')
print(range(-3))
for x in range(-3): print(x)
print('----- range(0,-3) -----')
print(range(0,-3))
for x in range(0,-3): print(x)
print('----- range(-3,0) -----')
print(range(-3,0))
for x in range(-3,0): print(x)
print('----- range(0,-3,-1) -----')
print(range(0,-3,-1))
for x in range(0,-3,-1): print(x)
```
```sh
$ python 0.py 
----- range(3) -----
range(0, 3)
0
1
2
----- range(3, 10) -----
range(3, 10)
3
4
5
6
7
8
9
----- range(-3) -----
range(0, -3)
----- range(0,-3) -----
range(0, -3)
----- range(-3,0) -----
range(-3, 0)
-3
-2
-1
----- range(0,-3,-1) -----
range(0, -3, -1)
0
-1
-2
```

### start,stop,step

```python
def show(r):
    print(r)
    print(r.start)
    print(r.stop)
    print(r.step)

show(range(3))
show(range(3,7,2))
show(range(0,-3,-1))
```
```sh
$ python 1.py 
range(0, 3)
0
3
1
range(3, 7, 2)
3
7
2
range(0, -3, -1)
0
-3
-1
```

### インデクサ

```python
r = range(10)
print(1 in r)
print(-1 in r)
print(r[3])
print(r[2:5])
print(r[-1])
```
```sh
$ python 2.py 
True
False
3
range(2, 5)
9
```

