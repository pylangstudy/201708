# [4.13. 特殊属性](https://docs.python.jp/3/library/stdtypes.html#special-attributes)

< [4.12. その他の組み込み型](https://docs.python.jp/3/library/stdtypes.html#other-built-in-types) < [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## 説明

> 実装は、いくつかのオブジェクト型に対して、適切な場合には特殊な読み出し専用の属性を追加します。そのうちいくつかは dir() 組込み関数で報告されません。

属性|説明
----|----
object.__dict__|オブジェクトの (書き込み可能な) 属性を保存するために使われる辞書またはその他のマッピングオブジェクトです。
instance.__class__|クラスインスタンスが属しているクラスです。
class.__bases__|クラスオブジェクトの基底クラスのタプルです。
definition.__name__|クラス、関数、メソッド、デスクリプタ、ジェネレータインスタンスの名前です。
definition.__qualname__|クラス、関数、メソッド、デスクリプタ、ジェネレータインスタンスの 修飾名 です。バージョン 3.3 で追加.
class.__mro__|この属性はメソッドの解決時に基底クラスを探索するときに考慮されるクラスのタプルです。
class.mro()|このメソッドは、メタクラスによって、そのインスタンスのメソッド解決の順序をカスタマイズするために、上書きされるかも知れません。このメソッドはクラスのインスタンス化時に呼ばれ、その結果は __mro__ に格納されます。
class.__subclasses__()|それぞれのクラスは、それ自身の直接のサブクラスへの弱参照を保持します。このメソッドはそれらの参照のうち、生存しているもののリストを返します。

### ソースコード

```python
class A:
    def MyMethod(self): pass

a = A()
print(A.__dict__)
print(a.__dict__)
print(a.__class__)
print(A.__bases__)
print(A.__name__)
print(A.__qualname__)

print(A.__mro__)
#print(a.__mro__)
print(A.mro())
#print(a.mro())
#print(A.__subclasses__())
print(int.__subclasses__())
```
```sh
$ python 0.py 
{'__module__': '__main__', 'MyMethod': <function A.MyMethod at 0xb711f8e4>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
{}
<class '__main__.A'>
(<class 'object'>,)
A
A
(<class '__main__.A'>, <class 'object'>)
[<class '__main__.A'>, <class 'object'>]
[<class 'bool'>]
```

