# [5. 組み込み例外](https://docs.python.jp/3/library/exceptions.html#built-in-exceptions)

< [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## 説明

### `BaseException`

> Python において、すべての例外は BaseException から派生したクラスのインスタンスでなければなりません。特定のクラスを言及する except 節を伴う try 文において、その節はそのクラスから派生した例外クラスも処理しますが、そのクラスの派生 元 の例外クラスは処理しません。サブクラス化の関係にない 2 つの例外クラスは、それらが同じ名前だった場合でも等しくなりえません。

### 組み込み例外

> 以下に挙げる組み込み例外は、インタプリタや組み込み関数によって生成されます。特に注記しないかぎり、これらはエラーの詳しい原因を示す “関連値 (associated value)” を持ちます。この値は、複数の情報 (エラーコードや、そのコードを説明する文字列など) の文字列かタプルです。関連値は通常、例外クラスのコンストラクタに引数として渡されます。

### 例外の送出

> ユーザによるコードも組み込み例外を送出できます。これを使って、例外ハンドラをテストしたり、インタプリタが同じ例外を送出する状況と “ちょうど同じような” エラー条件であることを報告したりできます。しかし、ユーザのコードが適切でないエラーを送出するのを妨げる方法はないので注意してください。

### 例外のユーザ定義

> 組み込み例外クラスは新たな例外を定義するためにサブクラス化することができます。新しい例外は、Exception クラスかそのサブクラスの一つから派生することをお勧めします。 BaseException からは派生しないで下さい。例外を定義する上での詳しい情報は、 Python チュートリアルの ユーザー定義例外 の項目にあります。

* [ユーザー定義例外](https://docs.python.jp/3/tutorial/errors.html#tut-userexceptions)

### 例外キャッチ

> except または finally 節内で例外を送出 (または再送出) するとき、__context__ は自動的に最後に捕まった例外に設定されます。新しい例外が処理されなければ、最終的に表示されるトレースバックは先に起きた例外も最後の例外も含みます。

### raise ... from ...

> 現在処理中の例外を raise を使って再送出するのではなく新規に例外を送出する場合、raise と一緒に from を使うことで暗黙の例外コンテキストを捕捉することができます:

```pytnon
raise new_exc from original_exc
```

> from に続く式 (expression) は例外か None でなくてはなりません。式は送出される例外の __cause__ として設定されます。 __cause__ を設定することは、 __suppress_context__ 属性を True にすることも意味するので、 raise new_exc from None を使うことで効率的に古い例外を新しいもので置き換えて表示する (たとえば KeyError を AttributeError に置き換え、古い例外はデバッグ時の調査で使えるよう __context__ に残す) ことができます。

Python文書の説明ではよくわからないのでググった。

* http://qiita.com/msmhrt/items/f941355b2139f0b81efc

### traceback

> デフォルトの traceback 表示コードは、例外自体の traceback に加え、これらの連鎖された例外を表示します。__cause__ で明示的に連鎖させた例外は、存在するならば常に表示されます。__context__ で暗黙に連鎖させた例外は、__cause__ が None かつ __suppress_context__ が false の場合にのみ表示されます。

> いずれにせよ、連鎖された例外に続いて、その例外自体は常に表示されます。そのため、traceback の最終行には、常に送出された最後の例外が表示されます。

## ソースコード

```python
class SomeException(Exception): pass
raise SomeException()
```
```sh
$ python 0.py 
Traceback (most recent call last):
  File "0.py", line 2, in <module>
    raise SomeException()
__main__.SomeException
```

```python
class ModuleException(Exception): pass
try: raise Exception()
except Exception as e: raise ModuleException(e) from e
```
```sh
$ python 1.py 
Traceback (most recent call last):
  File "1.py", line 2, in <module>
    try: raise Exception()
Exception

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "1.py", line 3, in <module>
    except Exception as e: raise ModuleException(e) from e
__main__.ModuleException
```

