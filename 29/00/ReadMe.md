# [6.7.4. 履歴リスト](https://docs.python.jp/3/library/readline.html#history-list)

< [6.7. readline — GNU readline のインタフェース](https://docs.python.jp/3/library/readline.html) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

> 以下の関数はグローバルな履歴リストを操作します:

メソッド|説明
--------|----
readline.clear_history()|現在の履歴をクリアします。これにより下層のライブラリーの clear_history() が呼ばれます。Python がこの機能をサポートするライブラリーのバージョンでコンパイルされたときのみ、この関数は存在します。
readline.get_current_history_length()|履歴に現在ある項目の数を返します。 (get_history_length() は履歴ファイルに書かれる最大行数を返します。)
readline.get_history_item(index)|現在の履歴の index 番目の項目を返します。添字は1から始まります。これにより下層のライブラリーの history_get() が呼ばれます。
readline.remove_history_item(pos)|履歴から指定された位置の項目を削除します。添字は0から始まります。これにより下層のライブラリーの remove_history() が呼ばれます。
readline.replace_history_item(pos, line)|指定された位置の項目を line で置き換えます。添字は0から始まります。これにより下層のライブラリーの replace_history_entry() が呼ばれます。
readline.add_history(line)|最後に入力したかのように、 line を履歴バッファに追加します。これにより下層のライブラリーの add_history() が呼ばれます。
readline.set_auto_history(enabled)|Enable or disable automatic calls to add_history() when reading input via readline. The enabled argument should be a Boolean value that when true, enables auto history, and that when false, disables auto history.バージョン 3.6 で追加.CPython 実装の詳細: Auto history is enabled by default, and changes to this do not persist across multiple sessions. （readline経由で入力を読み込むときにadd_history（）への自動呼び出しを有効または無効にします。有効な引数は、trueの場合は自動履歴を有効にし、falseの場合は自動履歴を無効にするブール値にする必要があります。バージョン3.6で追加.CPython実装の詳細：自動履歴はデフォルトで有効になっており、複数のセッション。）

以下参照。

* http://ja.pymotw.com/2/readline/
* http://tiswww.case.edu/php/chet/readline/readline.html

