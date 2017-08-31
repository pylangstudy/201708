# [7.1.1. 関数と例外](https://docs.python.jp/3/library/struct.html#functions-and-exceptions)

< [7.1. struct — バイト列をパックされたバイナリデータとして解釈する](https://docs.python.jp/3/library/struct.html#module-struct) < [7. バイナリデータ処理](https://docs.python.jp/3/library/binary.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/struct.py](https://github.com/python/cpython/tree/3.6/Lib/struct.py)

## < [7.1. struct — バイト列をパックされたバイナリデータとして解釈する](https://docs.python.jp/3/library/struct.html#module-struct)

### 概要

> このモジュールは、 Python の値と Python bytes オブジェクトとして表される C の構造体データとの間の変換を実現します。このモジュールは特に、ファイルに保存されたり、ネットワーク接続を経由したバイナリデータを扱うときに使われます。このモジュールでは、C 構造体のレイアウトおよび Python の値との間で行いたい変換をコンパクトに表現するために、 書式文字列 を使います。

### 注釈

> デフォルトでは、与えられた C の構造体をパックする際に、関連する C データ型を適切にアラインメント(alignment)するために数バイトのパディングを行うことがあります。この挙動が選択されたのは、パックされた構造体のバイト表現を対応する C 構造体のメモリレイアウトに正確に対応させるためです。プラットフォーム独立のデータフォーマットを扱ったり、隠れたパディングを排除したりするには、サイズ及びアラインメントとして native の代わりに standard を使うようにします: 詳しくは バイトオーダ、サイズ、アラインメント を参照して下さい。

### バッファプロトコル

> いくつかの struct の関数 (および Struct のメソッド) は buffer 引数を取ります。 これは バッファプロトコル (buffer Protocol) を実装していて読み取り可能または読み書き可能なバッファを提供するオブジェクトのことです。この目的のために使われる最も一般的な型は bytes と bytearray ですが、バイトの配列とみなすことができるような他の多くの型がバッファプロトコルを実装しています。そのため、それらは bytes オブジェクトから追加のコピーなしで読み出しや書き込みができます。

* [バッファプロトコル](https://docs.python.jp/3/c-api/buffer.html#bufferobjects)
* [bytes](https://docs.python.jp/3/library/functions.html#bytes)
* [bytearray](https://docs.python.jp/3/library/functions.html#bytearray)

## [7.1.1. 関数と例外](https://docs.python.jp/3/library/struct.html#functions-and-exceptions)

メソッド|説明
--------|----
exception struct.error|様々な状況で送出される例外です。引数は何が問題なのかを記述する文字列です。
struct.pack(fmt, v1, v2, ...)|フォーマット文字列 fmt に従い値 v1, v2, ... をパックして、バイト列オブジェクトを返します。引数は指定したフォーマットが要求する型と正確に一致していなければなりません。
struct.pack_into(fmt, buffer, offset, v1, v2, ...)|フォーマット文字列 fmt に従い値 v1, v2, ... をパックしてバイト列にし、書き込み可能な buffer のオフセット offset 位置より書き込みます。オフセットは省略出来ません。
struct.unpack(fmt, buffer)|(pack(fmt, ...) でパックされたであろう) バッファ buffer を、書式文字列 fmt に従ってアンパックします。 値が一つしかない場合を含め、結果はタプルで返されます。 バッファのバイトサイズは、 calcsize() の返り値である書式文字列が要求するサイズと一致しなければなりません。
struct.unpack_from(fmt, buffer, offset=0)|バッファ buffer を、 offset の位置から書式文字列 fmt に従ってアンパックします。 値が一つしかない場合を含め、結果はタプルで返されます。 バッファのバイトサイズから offset を引いたものは、少なくとも calcsize() の返り値である書式文字列が要求するサイズでなければなりません。
struct.iter_unpack(fmt, buffer)|バッファ buffer を、書式文字列 fmt に従ってイテレータ形式でアンパックします。 この関数が返すイテレータは、すべての内容を読み終わるまでバッファから一定の大きさのチャンクを読み取ります。 バッファのバイトサイズは、 calcsize() の返り値である書式文字列が要求するサイズの倍数でなければなりません。イテレーション毎に書式文字列で指定されたタプルを yield します。バージョン 3.4 で追加.
struct.calcsize(fmt)|書式文字列 fmt に従って、構造体 (それと pack(fmt, ...) によって作成されるバイト列オブジェクト) のサイズを返します。

