# [6.7.3. 履歴ファイル](https://docs.python.jp/3/library/readline.html#history-file)

< [6.7. readline — GNU readline のインタフェース](https://docs.python.jp/3/library/readline.html) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

> 以下の関数は行バッファを操作します:

メソッド|説明
--------|----
readline.read_history_file([filename])|readline 履歴ファイルを読み込み、履歴リストに追加します。デフォルトのファイル名は ~/.history です。これにより下層のライブラリーの read_history() が呼ばれます。
readline.write_history_file([filename])|履歴リストを readline 履歴ファイルに保存します。既存のファイルは上書きされます。デフォルトのファイル名は ~/.history です。これにより下層のライブラリーの write_history() が呼ばれます。
readline.append_history_file(nelements[, filename])|履歴の最後の nelements 項目をファイルに追加します。でふぉるのファイル名は ~/.history です。ファイルは存在していなくてはなりません。これにより下層のライブラリーの append_history() が呼ばれます。Python がこの機能をサポートするライブラリーのバージョンでコンパイルされたときのみ、この関数は存在します。バージョン 3.5 で追加.
readline.get_history_length(), readline.set_history_length(length)|Set or return the desired number of lines to save in the history file. The write_history_file() function uses this value to truncate the history file, by calling history_truncate_file() in the underlying library. Negative values imply unlimited history file size.(履歴ファイルに保存する行数を設定または返す。 write_history_file（）関数は、この値を使用して、基礎となるライブラリのhistory_truncate_file（）を呼び出して、履歴ファイルを切り捨てます。 負の値は、無期限の履歴ファイルサイズを意味します。)[Google翻訳](https://translate.google.co.jp/?hl=ja#en/ja/Set%20or%20return%20the%20desired%20number%20of%20lines%20to%20save%20in%20the%20history%20file.%20The%20write_history_file()%20function%20uses%20this%20value%20to%20truncate%20the%20history%20file%2C%20by%20calling%20history_truncate_file()%20in%20the%20underlying%20library.%20Negative%20values%20imply%20unlimited%20history%20file%20size.)

以下参照。

* http://ja.pymotw.com/2/readline/
* http://tiswww.case.edu/php/chet/readline/readline.html

