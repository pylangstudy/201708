# [4.11. コンテキストマネージャ型](https://docs.python.jp/3/library/stdtypes.html#context-manager-types)

< [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## with文

> Python の with 文は、コンテキストマネージャによって定義される実行時コンテキストの概念をサポートします。これは、文の本体が実行される前に進入し文の終わりで脱出する実行時コンテキストを、ユーザ定義クラスが定義できるようにする一対のメソッドで実装されます:

## 

* contextmanager.__enter__()
* contextmanager.__exit__(exc_type, exc_val, exc_tb)

`contextmanager.`でなく`object.`ではないのか？

* http://blog.amedama.jp/entry/2015/10/02/234946

どうやら実装方法が2種類あるらしい。

* ユーザ定義クラス実装
* `@contextlib.contextmanager`デコレータ実装

### ユーザ定義クラス実装

```python
#class A(contextmanager): pass #NameError: name 'contextmanager' is not defined
class A:
    def __enter__(self):
        print('__enter__')
    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__', exc_type, exc_value, traceback)

with A() as a:
    print('A')

with A() as a:
    raise Exception('ERROR!')
    print('A')
```
```sh
$ python 0.py 
__enter__
A
__exit__ None None None
__enter__
__exit__ <class 'Exception'> ERROR! <traceback object at 0xb716743c>
Traceback (most recent call last):
  File "0.py", line 13, in <module>
    raise Exception('ERROR!')
Exception: ERROR!
```

正常時、異常時、どちらもenter, exit両方実行されている。

### `@contextlib.contextmanager`デコレータ実装

```python
import contextlib

@contextlib.contextmanager
def manager():
    print('enter')
    yield
    print('exit')

with manager() as a:
    print('A')

with manager() as a:
    raise Exception('ERROR!')
    print('A')
```
```sh
$ python 1.py 
enter
A
exit
enter
Traceback (most recent call last):
  File "1.py", line 13, in <module>
    raise Exception('ERROR!')
Exception: ERROR!
```

異常時、exitが実行されていない。with文は異常時の終了処理が目的のはずなのに……。

#### try-finally文

```python
import contextlib

@contextlib.contextmanager
def manager():
    print('enter')
    try: yield
    finally: print('exit')

with manager() as a:
    print('A')

with manager() as a:
    raise Exception('ERROR!')
    print('A')
```
```sh
$ python 2.py 
enter
A
exit
enter
exit
Traceback (most recent call last):
  File "2.py", line 13, in <module>
    raise Exception('ERROR!')
Exception: ERROR!
```

これで異常時にexitが実行された。

## try-finally実装

with文など使わず、最初からtry-finallyすればいい話では？

```python
print('enter')
try:
    print('A')
finally:
    print('exit')

print('enter')
try:
    raise Exception('ERROR!')
    print('A')
finally:
    print('exit')
```
```sh
$ python 3.py 
enter
A
exit
enter
exit
Traceback (most recent call last):
  File "3.py", line 9, in <module>
    raise Exception('ERROR!')
Exception: ERROR!
```

共通処理が多いが、不可能ではない。問題はDRYに書けないことか。

* http://qiita.com/howmuch/items/95efab2e61f735a150e3

## 使い分け

3つの方法は、それぞれ使い分けたほうが良さそう。

実装方法|使いどころ
--------|----------
ユーザ定義クラス|ある処理の実装箇所を明確にしたいとき（複雑な処理ゆえ内部名前空間(class)が必要で、かつ、2回以上使われるとき）
`@contextlib.contextmanager`|モジュール内で2回以上同じことをするとき
try-finally|モジュール内で1回も同じことをしないとき

ユーザクラスやデコレータは関数名など入れ物を用意し、名付けねばならないため面倒。しかし2回以上使うならDRYに書くために必要。

