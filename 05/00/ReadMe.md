# [4.9. set（集合）型 — set, frozenset](https://docs.python.jp/3/library/stdtypes.html#set-types-set-frozenset)

< [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## set

### 集合

> set オブジェクトは、固有の hashable オブジェクトの順序なしコレクションです。通常の用途には、帰属テスト、シーケンスからの重複除去、積集合、和集合、差集合、対称差 (排他的論理和) のような数学的演算の計算が含まれます。(他のコンテナについては組み込みの dict, list, tuple クラスや collections モジュールを参照してください。)

### 順序なし

> 集合は、他のコレクションと同様、 x in set, len(set), for x in set をサポートします。コレクションには順序がないので、集合は挿入の順序や要素の位置を記録しません。従って、集合はインデクシング、スライシング、その他のシーケンス的な振舞いをサポートしません。

### mutable, immutable

> set および frozenset という、2つの組み込みの集合型があります。 set はミュータブルで、add() や remove() のようなメソッドを使って内容を変更できます。ミュータブルなため、ハッシュ値を持たず、また辞書のキーや他の集合の要素として用いることができません。一方、frozenset 型はイミュータブルで、ハッシュ可能 です。作成後に内容を改変できないため、辞書のキーや他の集合の要素として用いることができます。

### 生成

空でない set (frozenset ではない) は、set コンストラクタに加え、要素を波括弧中にカンマで区切って列挙することでも生成できます。例: {'jack', 'sjoerd'}。

どちらのクラスのコンストラクタも同様に働きます:

## メソッド一覧

各ソースコードファイル参照。

### set, frozenset共通

メソッド|説明
--------|----
`len(x)`|集合 s の要素数 (s の濃度) を返します。
`x in s`|x が s のメンバーに含まれるか判定します。
`x not in s`|x が s のメンバーに含まれていないことを判定します。
isdisjoint(other)|集合が other と共通の要素を持たないとき、True を返します。
`set <= other`, `issubset(other)`|set の全ての要素が other に含まれるか判定します。
`set < other`|set が other の真部分集合であるかを判定します。
`set >= other`, `issuperset(other)`|other の全ての要素が set に含まれるか判定します。
`set > other`|set が other の真上位集合であるかを判定します。
`set | other`, `s.union(other)`|set と全ての other の要素からなる新しい集合を返します。
`set & other`, `s.intersection(other)`|set と全ての other に共通する要素を持つ、新しい集合を返します。
`set - other`, `difference(*others)`|set に含まれて、かつ、全ての other に含まれない要素を持つ、新しい集合を返します。
`set ^ other`, `symmetric_difference(other)`|set と other のいずれか一方だけに含まれる要素を持つ新しい集合を返します。
`copy()`|s の浅いコピーを新しい集合として返します。

* 集合: s, other
* 要素: x

### setのみ

メソッド|説明
--------|----
`set |= other`, `update(*others)`|全ての other の要素を追加し、 set を更新します。
`set &= other`, `intersection_update(*others)`|元の set と全ての other に共通する要素だけを残して set を更新します。
`set -= other`, `difference_update(*others)`|other に含まれる要素を取り除き、 set を更新します。
`set ^= other`, `symmetric_difference_update(other)`|どちらかにのみ含まれて、共通には持たない要素のみで set を更新します。
`add(elem)`|要素 elem を set に追加します。
`remove(elem)`|要素 elem を set から取り除きます。
`discard(elem)`|要素 elem が set に含まれていれば、取り除きます。
`pop()`|s から任意の要素を取り除き、それを返します。
`clear()`|set の全ての要素を取り除きます。
     
* 集合: s, other
* 集合or要素: elem

