# [5.1. 基底クラス](https://docs.python.jp/3/library/exceptions.html#base-classes)

< [5. 組み込み例外](https://docs.python.jp/3/library/exceptions.html#built-in-exceptions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

> 以下の例外は、主に他の例外の基底クラスとして使われます。

## 説明

名前|説明
----|----
exception BaseException|全ての組み込み例外の基底クラスです。ユーザ定義の例外に直接継承されることは意図されていません (継承には Exception を使ってください)。このクラスのインスタンスに str() が呼ばれた場合、インスタンスへの引数の表現か、引数が無い場合には空文字列が返されます。
args|例外コンストラクタに与えられた引数のタプルです。
with_traceback(tb)|このメソッドは tb を例外の新しいトレースバックとして設定し、例外オブジェクトを返します。
exception Exception|システム終了以外の全ての組み込み例外はこのクラスから派生しています。全てのユーザ定義例外もこのクラスから派生させるべきです。
exception ArithmeticError|算術上の様々なエラーに対して送出される組み込み例外 OverflowError, ZeroDivisionError, FloatingPointError の基底クラスです。
exception BufferError|バッファ に関連する操作が行えなかったときに送出されます。
exception LookupError|マッピングまたはシーケンスで使われたキーやインデクスが無効な場合に送出される例外 IndexError および KeyError の基底クラスです。 codecs.lookup() によって直接送出されることもあります。

## ソースコード

```python
import sys
class ModuleException(Exception): pass
try: raise Exception()
except Exception as e:
    tb = sys.exc_info()[2]
    raise ModuleException().with_traceback(tb)
```
```sh
$ python 0.py 
Traceback (most recent call last):
  File "0.py", line 3, in <module>
    try: raise Exception()
Exception

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "0.py", line 6, in <module>
    raise ModuleException().with_traceback(tb)
  File "0.py", line 3, in <module>
    try: raise Exception()
__main__.ModuleException
```

