# [4.12.5. コードオブジェクト](https://docs.python.jp/3/library/stdtypes.html#code-objects)

< [4.12. その他の組み込み型](https://docs.python.jp/3/library/stdtypes.html#other-built-in-types) < [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## 説明

> コードオブジェクトは、関数本体のような “擬似コンパイルされた” Python の実行可能コードを表すために実装系によって使われます。コードオブジェクトはグローバルな実行環境への参照を持たない点で関数オブジェクトとは異なります。コードオブジェクトは組み込み関数 compile() によって返され、また関数オブジェクトの __code__ 属性として取り出せます。 code モジュールも参照してください。

* [compile](https://docs.python.jp/3/library/functions.html#compile)
* [code](https://docs.python.jp/3/library/code.html#module-code)

> コードオブジェクトは、組み込み関数 exec() や eval() に (ソース文字列の代わりに) 渡すことで、実行や評価できます。

* [exec()](https://docs.python.jp/3/library/functions.html#exec)
* [eval()](https://docs.python.jp/3/library/functions.html#eval)

> 詳細は、 標準型の階層 を参照してください。

* [標準型の階層](https://docs.python.jp/3/reference/datamodel.html#types)

### ソースコード

```python
src = """def f():
    print('abc')
f()
"""
#co = compile("print('abc')", '', 'exec')
co = compile(src, '', 'exec')
exec(co)
co = compile("print('abc')", '', 'exec')
eval(co)
co = compile("print('abc')", '', 'single')
eval(co)
```
```sh
$ python 0.py 
abc
abc
abc
```

