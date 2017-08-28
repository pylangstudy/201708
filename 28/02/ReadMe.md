# [6.7.2. 行バッファ](https://docs.python.jp/3/library/readline.html#line-buffer)

< [6.7. readline — GNU readline のインタフェース](https://docs.python.jp/3/library/readline.html) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

> 以下の関数は行バッファを操作します:

メソッド|説明
--------|----
readline.get_line_buffer()|行バッファ (下層のライブラリーの rl_line_buffer) の現在の内容を返します。
readline.insert_text(string)|テキストをカーサー位置の行バッファに挿入します。これにより下層のライブラリーの rl_insert_text() が呼ばれますが、戻り値は無視されます。
readline.redisplay()|スクリーンの表示を変更して行バッファの現在の内容を反映させます。これにより下層のライブラリーの rl_redisplay() が呼ばれます。

カーサーって何？カーソルまたはキャレットでは？

以下参照。

* http://ja.pymotw.com/2/readline/
* http://tiswww.case.edu/php/chet/readline/readline.html

