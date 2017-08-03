# [4.8.2. bytearray オブジェクト](https://docs.python.jp/3/library/stdtypes.html#bytearray-objects)

< [4.8. バイナリシーケンス型 — bytes, bytearray, memoryview(原文)](https://docs.python.jp/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview) < [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## ミュータブル版

> bytearray オブジェクトは bytes オブジェクトの可変なバージョンです。

## 生成

> bytearray に専用のリテラル構文はないので、コンストラクタを使って作成します:

> * 空のインスタンスを作る: bytearray()

> * 指定された長さの0で埋められたインスタンスを作る: bytearray(10)

> * 整数の iterable から: bytearray(range(20))

> * 既存のバイナリデータからバッファプロトコルを通してコピーする: bytearray(b'Hi!')

## 操作

> bytearray オブジェクトは可変なので、 bytes と bytearray の操作 で解説されている bytes オブジェクトと共通の操作に加えて、 mutable シーケンス操作もサポートしています。

* [bytes と bytearray の操作](https://docs.python.jp/3/library/stdtypes.html#bytes-methods)

> bytearray ビルトイン関数も参照してください。

* [bytearray](https://docs.python.jp/3/library/functions.html#func-bytearray)

> 16 進数で 2 桁の数は正確に 1 バイトに相当するため、16 進整はバイナリデータを表現する形式として広く使われています。 従って、 bytearray 型にはその形式でデータを読み取るための追加のクラスメソッドがあります。

* classmethod bytearray.fromhex(string)
* bytearray.hex()


```python
print(bytearray.fromhex('FF'))
print(bytearray.fromhex('FF 1A'))
print(bytearray(b'\xFF').hex())
print(bytearray(b'\xFF\x1A').hex())
```
```sh
$ python 0.py 
bytearray(b'\xff')
bytearray(b'\xff\x1a')
ff
ff1a
```

### インデクサ

> bytearray オブジェクトは整数のシーケンス (リストのようなもの) なので、 bytearray オブジェクト b について、 b[0] は整数になり、 b[0:1] は長さ 1 の bytearray オブジェクトになります。(これは、文字列においてインデックス指定もスライスも長さ 1 の文字列を返すのと対照的です。)

### リテラル表記

> bytearray オブジェクトの表記はバイトのリテラル形式 (bytearray(b'...')) を使用します。これは bytearray([46, 46, 46]) などの形式よりも便利な事が多いためです。 bytearray オブジェクトはいつでも list(b) で整数のリストに変換できます。

