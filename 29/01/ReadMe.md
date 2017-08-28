# [6.7.5. 開始フック](https://docs.python.jp/3/library/readline.html#startup-hooks)

< [6.7. readline — GNU readline のインタフェース](https://docs.python.jp/3/library/readline.html) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

> 以下の関数はグローバルな履歴リストを操作します:

メソッド|説明
--------|----
readline.set_startup_hook([function])|Set or remove the function invoked by the rl_startup_hook callback of the underlying library. If function is specified, it will be used as the new hook function; if omitted or None, any function already installed is removed. The hook is called with no arguments just before readline prints the first prompt.（基本となるライブラリのrl_startup_hookコールバックによって呼び出される関数を設定または削除します。 functionが指定されている場合、それは新しいフック関数として使用されます。省略された場合、またはNoneの場合、すでにインストールされている関数は削除されます。 readlineが最初のプロンプトを表示する直前に、引数なしでフックが呼び出されます。）
readline.set_pre_input_hook([function])|Set or remove the function invoked by the rl_pre_input_hook callback of the underlying library. If function is specified, it will be used as the new hook function; if omitted or None, any function already installed is removed. The hook is called with no arguments after the first prompt has been printed and just before readline starts reading input characters. This function only exists if Python was compiled for a version of the library that supports it.（基礎となるライブラリのrl_pre_input_hookコールバックによって呼び出された関数を設定または削除します。 functionが指定されている場合、それは新しいフック関数として使用されます。省略された場合、またはNoneの場合、すでにインストールされている関数は削除されます。フックは、最初のプロンプトが表示された後、readlineが入力文字の読み込みを開始する直前に引数なしで呼び出されます。この関数は、Pythonがそれをサポートするライブラリのバージョン用にコンパイルされた場合にのみ存在します。）

以下参照。

* http://ja.pymotw.com/2/readline/
* http://tiswww.case.edu/php/chet/readline/readline.html
* https://github.com/search?utf8=%E2%9C%93&q=readline.set_startup_hook%28+extension%3Apy&type=Code&ref=advsearch&l=&l=
