# [4.8.3. bytes と bytearray の操作](https://docs.python.jp/3/library/stdtypes.html#bytes-and-bytearray-operations)

< [4.8. バイナリシーケンス型 — bytes, bytearray, memoryview(原文)](https://docs.python.jp/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview) < [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## 操作

> bytes と bytearray は両方共 一般のシーケンス操作 をサポートしています。また、両方とも bytes-like object をサポートしている任意のオブジェクトを対象に操作することもできます。この柔軟性により bytes と bytearray を自由に混ぜてもエラーを起こすことなく扱うことができます。ただし、操作の結果のオブジェクトはその操作の順序に依存することになります。

### 注釈

> 文字列のメソッドが引数として bytes を受け付けないのと同様、bytes オブジェクトと bytearray オブジェクトのメソッドは引数として文字列を受け付けません。例えば、以下のように書かなければなりません:

```python
a = "abc"
b = a.replace("a", "f")
```

```python
a = b"abc"
b = a.replace(b"a", b"f")
```

## ASCII互換前提

> いくつかの bytes と bytearray の操作は ASCII と互換性のあるバイナリフォーマットが使われていると仮定していますので、フォーマットの不明なバイナリデータに対して使うことは避けるべきです。こうした制約については以下で説明します。

### 注釈

> これらの ASCII ベースの演算を使って ASCII ベースではないバイナリデータを操作すると、データを破壊する恐れがあります。 

## メソッド一覧

bytes, bytearray両方で使える。37メソッド。

メソッド|概要
--------|----
count(sub[, start[, end]])|[start, end] の範囲に、部分シーケンス sub が重複せず出現する回数を返します。
decode(encoding="utf-8", errors="strict")|与えられたバイト列からデコードされた文字列を返します。
endswith(suffix[, start[, end]])|バイナリデータが指定された suffix で終わる場合は True を、そうでなければ False を返します。 
find(sub[, start[, end]])|s[start:end] に部分シーケンス sub が含まれる場合、データ中のその sub の最小のインデックスを返します。
index(sub[, start[, end]])|find() と同様ですが、部分シーケンスが見つからなかった場合 ValueError を送出します。
join(iterable)|イテラブル iterable 中のバイナリデータを結合した bytes または bytearray オブジェクトを返します。
maketrans(from, to)|この静的メソッドは、 bytes.translate() に渡すのに適した変換テーブルを返します。
partition(sep)|区切り sep が最初に出現する位置でシーケンスを分割し、 3 要素のタプルを返します。
replace(old, new[, count])|部分シーケンス old を全て new に置換したシーケンスを返します。
rfind(sub[, start[, end]])|シーケンス中の領域 s[start:end] に sub が含まれる場合、その最大のインデックスを返します。
rindex(sub[, start[, end]])|rfind() と同様ですが、部分シーケンス sub が見つからなかった場合 ValueError を送出します。
rpartition(sep)|区切り sep が最後に出現する位置でシーケンスを分割し、 3 要素のタプルを返します。
startswith(prefix[, start[, end]])|バイナリデータが指定された prefix で始まる場合は True を、そうでなければ False を返します。 
translate(table, delete=b'')|オプション引数 delete に現れるすべてのバイトを除去し、残ったバイトを与えられた変換テーブルに従ってマップした、バイト列やバイト配列オブジェクトのコピーを返します。
center(width[, fillbyte])|長さ width の中央寄せされたシーケンスのコピーを返します。
ljust(width[, fillbyte])|長さ width の左寄せされたシーケンスのコピーを返します。
lstrip([chars])|先頭から特定のバイト値を除去したコピーを返します。
rjust(width[, fillbyte])|長さ width の右寄せされたシーケンスのコピーを返します。
rsplit(sep=None, maxsplit=-1)|sep を区切りとして、同じ型の部分シーケンスに分割します。
rstrip([chars])|末尾から特定のバイト値を除去したコピーを返します。
split(sep=None, maxsplit=-1)|sep を区切りとして、同じ型の部分シーケンスに分割します。
strip([chars])|先頭および末尾から特定のバイト値を除去したコピーを返します。
capitalize()|各バイトを ASCII 文字と解釈して、最初のバイトを大文字にし、残りを小文字にしたシーケンスのコピーを返します。
expandtabs(tabsize=8)|桁 (column) 位置と指定されたタブ幅 (tab size) に応じて、全ての ASCII タブ文字を 1 つ以上の ASCII スペース文字に置換したシーケンスのコピーを返します。
isalnum()|シーケンスが空でなく、かつ全てのバイト値が ASCII 文字のアルファベットまたは数字である場合は true を、そうでなければ false を返します。
isalpha()|シーケンスが空でなく、かつ全てのバイト値が ASCII 文字のアルファベットである場合は true を、そうでなければ false を返します。
isdigit()|シーケンスが空でなく、かつ全てのバイト値が ASCII 文字の数字である場合は true を、そうでなければ false を返します。
islower()|シーケンス中に小文字アルファベットの ASCII 文字が一つ以上あり、かつ大文字アルファベットの ASCII 文字が一つも無い場合に true を返します。
isspace()|シーケンスが空でなく、かつ全てのバイト値が ASCII 空白文字である場合は true を、そうでなければ false を返します。
istitle()|シーケンスが空でなく、かつ ASCII のタイトルケース文字列になっている場合は true を、そうでなければ false を返します。
isupper()|シーケンス中に大文字アルファベットの ASCII 文字が一つ以上あり、かつ小文字アルファベットの ASCII 文字が一つも無い場合に true を返します。
lower()|シーケンスに含まれる大文字アルファベットの ASCII 文字を全て小文字アルファベットに変換したシーケンスのコピーを返します。
splitlines(keepends=False)|バイナリシーケンスを ASCII の改行コードで分割し、各行をリストにして返します。
swapcase()|シーケンスに含まれる小文字アルファベットの ASCII 文字を全て大文字アルファベットに変換し、さらに大文字アルファベットを同様に小文字アルファベットに変換したシーケンスのコピーを返します。
title()|タイトルケース化したバイナリシーケンスを返します。
upper()|シーケンスに含まれる小文字アルファベットの ASCII 文字を全て大文字アルファベットに変換したシーケンスのコピーを返します。
zfill(width)|長さが width になるよう ASCII b'0' で左詰めしたシーケンスのコピーを返します。

