# [4.10. マッピング型 — dict](https://docs.python.jp/3/library/stdtypes.html#mapping-types-dict)

< [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## 辞書(dict)型

> マッピング (mapping) オブジェクトは、ハッシュ可能 (hashable) な値を任意のオブジェクトに対応付けます。マッピングはミュータブルなオブジェクトです。現在、標準マッピング型は辞書 (dictionary) だけです。 (他のコンテナについては組み込みの list, set, および tuple クラスと、 collections モジュールを参照してください。)

### キー

> 辞書のキーは ほぼ 任意の値です。ハッシュ可能 (hashable) でない値、つまり、リストや辞書その他のミュータブルな型 (オブジェクトの同一性ではなく値で比較されるもの) はキーとして使用できません。キーとして使われる数値型は通常の数値比較のルールに従います: もしふたつの数値が (例えば 1 と 1.0 のように) 等しければ、同じ辞書の項目として互換的に使用できます。 (ただし、コンピュータは浮動小数点数を近似値として保管するので、辞書型のキーとして使用するのはたいてい賢くありません。)

### 書式

> 辞書は key: value 対のカンマ区切りのリストを波括弧でくくることで作成できます。例えば: {'jack': 4098, 'sjoerd': 4127} あるいは {4098: 'jack', 4127: 'sjoerd'} 。あるいは、 dict コンストラクタでも作成できます。

# 関数

各ソースコードファイル参照。19件。

操

## 操作

8件。

操作|説明
--------|----
`class dict(**kwarg), (mapping, **kwarg), (iterable, **kwarg)`|新しい辞書を返します。
`len(d)`|
`d[key]`|
`d[key] = value`|
`del d[key]`|
`key in d`|
`key not in d`|
`iter(d)`|

## メソッド

11件。

メソッド|説明
--------|----
`clear()`|
`copy()`|
`classmethod fromkeys(seq[, value])`|
`get(key[, default])`|
`items()`|
`keys()`|
`pop(key[, default])`|
`popitem()`|
`setdefault(key[, default])`|
`update([other])`|
`values()`|


## [types.MappingProxyType](https://docs.python.jp/3/library/types.html#types.MappingProxyType)

### 参考

> dict の読み込み専用ビューを作るために [types.MappingProxyType](https://docs.python.jp/3/library/types.html#types.MappingProxyType) を使うことができます。 

