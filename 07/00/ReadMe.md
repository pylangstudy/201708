# [4.12.1. モジュール (module)](https://docs.python.jp/3/library/stdtypes.html#modules)

< [4.12. その他の組み込み型](https://docs.python.jp/3/library/stdtypes.html#other-built-in-types) < [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

> インタプリタは、その他いくつかの種類のオブジェクトをサポートしています。これらのほとんどは 1 つまたは 2 つの演算だけをサポートしています。

## `module.name`

> モジュールに対する唯一の特殊な演算は属性アクセス: m.name です。ここで m はモジュールで、 name は m のシンボルテーブル上に定義された名前にアクセスします。モジュール属性に代入することもできます。 (なお、import 文は、厳密にいえば、モジュールオブジェクトに対する演算ではありません; import foo は foo と名づけられたモジュールオブジェクトの存在を必要とはせず、foo と名づけられたモジュールの (外部の) 定義 を必要とします。)

> 全てのモジュールにある特殊属性が __dict__ です。これはモジュールのシンボルテーブルを含む辞書です。この辞書を書き換えると実際にモジュールのシンボルテーブルを変更することができますが、__dict__ 属性を直接代入することはできません (m.__dict__['a'] = 1 と書いて m.a を 1 に定義することはできますが、m.__dict__ = {} と書くことはできません)。 __dict__ を直接書き換えることは推奨されません。

> インタプリタ内に組み込まれたモジュールは、 <module 'sys' (built-in)> のように書かれます。ファイルから読み出された場合、 <module 'os' from '/usr/local/lib/pythonX.Y/os.pyc'> と書かれます。

### ソースコード

```python
import os, sys, datetime
print(os.name)
#print(sys.name)#AttributeError: module 'sys' has no attribute 'name'
#print(datetime.name)#AttributeError: module 'datetime' has no attribute 'name'

print(sys)
```
```sh
$ python 0.py 
posix
<module 'sys' (built-in)>
```

### インタプリタ

```python
>>> import os, sys, datetime
>>> os.name
'posix'
>>> sys.name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'sys' has no attribute 'name'
>>> datetime.name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'datetime' has no attribute 'name'
```
```python
>>> sys
<module 'sys' (built-in)>
```

