# [4.10.1. 辞書ビューオブジェクト](https://docs.python.jp/3/library/stdtypes.html#dictionary-view-objects)

< [4.10. マッピング型 — dict](https://docs.python.jp/3/library/stdtypes.html#mapping-types-dict) < [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

> dict.keys(), dict.values(), dict.items() によって返されるオブジェクトは、 ビューオブジェクト です。これらは、辞書の項目の動的なビューを提供し、辞書が変更された時、ビューはその変更を反映します。

> 辞書ビューは、イテレートすることで対応するデータを yield できます。また、帰属判定をサポートします:

詳細はソースコード参照。
