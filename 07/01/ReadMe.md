# [4.12.4. メソッド](https://docs.python.jp/3/library/stdtypes.html#methods)

< [4.12. その他の組み込み型](https://docs.python.jp/3/library/stdtypes.html#other-built-in-types) < [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## 説明

> メソッドは属性表記を使って呼び出される関数です。メソッドには二種類あります: (リストの append() のような) 組み込みメソッドと、クラスインスタンスのメソッドです。組み込みメソッドは、それをサポートする型と一緒に記述されています。

> インスタンスを通してメソッド (クラスの名前空間内で定義された関数) にアクセスすると、特殊なオブジェクトが得られます。それは束縛メソッド (bound method) オブジェクトで、インスタンスメソッド (instance method) とも呼ばれます。呼び出された時、引数リストに self 引数が追加されます。束縛メソッドには 2 つの特殊読み込み専用属性があります。 m.__self__ はそのメソッドが操作するオブジェクトで、 m.__func__ はそのメソッドを実装している関数です。 m(arg-1, arg-2, ..., arg-n) の呼び出しは、 m.__func__(m.__self__, arg-1, arg-2, ..., arg-n) の呼び出しと完全に等価です。

> 関数オブジェクトと同様に、メソッドオブジェクトは任意の属性の取得をサポートしています。しかし、メソッド属性は実際には下層の関数オブジェクト (meth.__func__) に記憶されているので、バインドされるメソッドにメソッド属性を設定することは許されていません。メソッドに属性を設定しようとすると AttributeError が送出されます。メソッドの属性を設定するためには、次のようにその下層の関数オブジェクトに明示的に設定する必要があります:

* [標準型の階層](https://docs.python.jp/3/reference/datamodel.html#types)

### ソースコード

```python
class C:
    def method(self): print('C.method()')

c = C()
#c.method.whoami = 'my name is method'  # AttributeError: 'method' object has no attribute 'whoami'
c.method()
print(c.method)
print(c.method.__func__)
print(c.method.__self__)
c.method.__func__(c.method.__self__)

c.method.__func__.whoami = 'my name is method'
print(c.method.whoami)
```
```sh
$ python 0.py 
C.method()
<bound method C.method of <__main__.C object at 0xb71bad2c>>
<function C.method at 0xb71b98e4>
<__main__.C object at 0xb71bad2c>
C.method()
my name is method
```

