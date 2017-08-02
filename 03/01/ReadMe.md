# [4.8. バイナリシーケンス型 — bytes, bytearray, memoryview(原文)](https://docs.python.jp/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview)

< [4.7. テキストシーケンス型 — str](https://docs.python.jp/3/library/stdtypes.html#text-sequence-type-str) < [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

> バイナリデータを操作するためのコア組み込み型は bytes および bytearray です。これらは、別のバイナリオブジェクトのメモリにコピーを作成すること無くアクセスするための バッファプロトコル を利用する memoryview でサポートされています。

> array モジュールは、32 ビット整数や IEEE754 倍精度浮動小数点値のような基本データ型の、効率的な保存をサポートしています。

* [bytes](https://docs.python.jp/3/library/functions.html#bytes)
* [bytearray](https://docs.python.jp/3/library/functions.html#bytearray)
* [memoryview](https://docs.python.jp/3/library/stdtypes.html#memoryview)

## [4.8.1. bytes](https://docs.python.jp/3/library/stdtypes.html#bytes)

### シーケンス型

> bytes はバイトの不変なシーケンスです。多くのメジャーなプロトコルがASCIIテキストエンコーディングをベースにしているので、 bytes オブジェクトは ASCII 互換のデータに対してのみ動作する幾つかのメソッドを提供していて、文字列オブジェクトと他の多くの点で近いです。

### リテラル

> まず、 bytes リテラルの構文は文字列リテラルとほぼ同じで、 b というプリフィックスを付けます:

> * シングルクォート: b'still allows embedded "double" quotes'

> * ダブルクォート: b"still allows embedded 'single' quotes".

> * 3重クォート: b'''3 single quotes''', b"""3 double quotes"""

#### ASCII以外はエスケープ必須

> bytes リテラルでは (ソースコードのエンコーディングに関係なく) ASCII文字のみが許可されています。 127より大きい値を bytes リテラルに記述する場合は適切なエスケープシーケンスを書く必要があります。

#### rプレフィックス

> 文字列リテラルと同じく、 bytes リテラルでも r プリフィックスを用いてエスケープシーケンスの処理を無効にすることができます。 bytes リテラルの様々な形式やサポートされているエスケープシーケンスについては 文字列およびバイト列リテラル を参照してください。

* [文字列およびバイト列リテラル](https://docs.python.jp/3/reference/lexical_analysis.html#strings)

#### 1Byteデータのシーケンス

> bytesリテラルと repr 出力は ASCII テキストをベースにしたものですが、 bytes オブジェクトは、各値が 0 <= x < 256 の範囲に収まるような整数 (この制限に違反しようとすると ValueError が発生します) の不変なシーケンスとして振る舞います。多くのバイナリフォーマットがASCIIテキストを元にした要素を持っていたり何らかのテキスト操作アルゴリズムによって操作されるものの、任意のバイナリデータが一般にテキストになっているわけではないことを強調するためにこのように設計されました (何も考えずにテキスト操作アルゴリズムをASCII非互換なバイナリデータフォーマットに対して行うとデータを破壊することがあります)。

### bytes生成

> リテラル以外に、幾つかの方法で bytes オブジェクトを作ることができます:

> * 指定された長さの、0で埋められた bytes オブジェクト: bytes(10)

> * 整数の iterable から: bytes(range(20))

> * 既存のバイナリデータからバッファプロトコルでコピーする: bytes(obj)

### 組み込み関数

> bytes ビルトイン関数も参照してください。

* [bytes()](https://docs.python.jp/3/library/functions.html#func-bytes)

### bytesクラスのメソッド

16 進数で 2 桁の数は正確に 1 バイトに相当するため、16 進整はバイナリデータを表現する形式として広く使われています。 従って、 bytes 型にはその形式でデータを読み取るための追加のクラスメソッドがあります。

* classmethod bytes.fromhex(string)
* bytes.hex()

```python
print(bytes.fromhex('FF'))
print(bytes.fromhex('FF 1A'))
print(b'\xFF'.hex())
print(b'\xFF\x1A'.hex())
```
```sh
$ python 0.py 
b'\xff'
b'\xff\x1a'
ff
ff1a
```

### インデクサ

> bytes オブジェクトは (タプルに似た) 整数のシーケンスなので、 bytes オブジェクト b について、 b[0] は整数になり、 b[0:1] は長さ 1 の bytes オブジェクトになります。 (この動作は、文字列に対するインデックス指定もスライスも長さ 1 の文字列を返すのと対照的です。)

### repr()

> bytes オブジェクトの repr 出力はリテラル形式 (b'...') になります。 bytes([46, 46, 46]) などの形式よりも便利な事が多いからです。 bytes オブジェクトはいつでも list(b) で整数のリストに変換できます。

### 注釈

> Python 2.x ユーザーへ: Python 2.x では多くの場面で 8bit 文字列 (2.x が提供しているビルトインのバイナリデータ型) と Unicode 文字列の間の暗黙の変換が許可されていました。これは Python がもともと 8bit 文字列しか持っていなくて、あとから Unicode テキストが追加されたので、後方互換性を維持するためのワークアラウンドでした。 Python 3.x ではこれらの暗黙の変換はなくなりました。 8-bit バイナリデータと Unicode テキストは明確に違うもので、 bytes オブジェクトと文字列オブジェクトを比較すると常に等しくなりません。 

