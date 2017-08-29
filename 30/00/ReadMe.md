# [6.7.6. 補完](https://docs.python.jp/3/library/readline.html#completion)

< [6.7. readline — GNU readline のインタフェース](https://docs.python.jp/3/library/readline.html) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

> The following functions relate to implementing a custom word completion function. This is typically operated by the Tab key, and can suggest and automatically complete a word being typed. By default, Readline is set up to be used by rlcompleter to complete Python identifiers for the interactive interpreter. If the readline module is to be used with a custom completer, a different set of word delimiters should be set.

翻訳。

> 以下の機能は、カスタム単語補完機能の実装に関連しています。これは通常Tabキーで操作され、入力中の単語を提案して自動的に入力します。デフォルトでは、rlcompleterは対話型インタプリタのPython識別子を完成させるためにReadlineを使用するように設定されています。 readlineモジュールをカスタムコンプリータで使用する場合は、別のワードデリミタセットを設定する必要があります。

メソッド|説明
--------|----
readline.set_completer([function])|completer 関数を設定または削除します。function が指定された場合、新たな completer 関数として用いられます; 省略された場合や None の場合、現在インストールされている completer 関数は削除されます。completer 関数は function(text, state) の形式で、関数が文字列でない値を返すまで state を 0, 1, 2, ..., にして呼び出します。この関数は text から始まる補完結果として次に来そうなものを返さなければなりません。The installed completer function is invoked by the entry_func callback passed to rl_completion_matches() in the underlying library. The text string comes from the first parameter to the rl_attempted_completion_function callback of the underlying library.（インストールされているコンプリータ関数は、基礎となるライブラリのrl_completion_matches（）に渡されたentry_funcコールバックによって呼び出されます。テキスト文字列は、基礎となるライブラリのrl_attempted_completion_functionコールバックの最初のパラメータから得られます。）
readline.get_completer()|completer 関数を取得します。completer 関数が設定されていなければ None を返します。
readline.get_completion_type()|Get the type of completion being attempted. This returns the rl_completion_type variable in the underlying library as an integer.（実行しようとしている補完のタイプを取得します。これは、基礎となるライブラリのrl_completion_type変数を整数として返します。）
readline.get_begidx(), readline.get_endidx()|Get the beginning or ending index of the completion scope. These indexes are the start and end arguments passed to the rl_attempted_completion_function callback of the underlying library.（完了スコープの開始または終了インデックスを取得します。これらのインデックスは、基礎となるライブラリのrl_attempted_completion_functionコールバックに渡される開始引数と終了引数です。）
readline.set_completer_delims(string), readline.get_completer_delims()|Set or get the word delimiters for completion. These determine the start of the word to be considered for completion (the completion scope). These functions access the rl_completer_word_break_characters variable in the underlying library.（完了のために区切り文字を設定または取得します。これらは、完了のために考慮すべき単語の開始点（完了範囲）を決定する。これらの関数は、基礎となるライブラリのrl_completer_word_break_characters変数にアクセスします。）
readline.set_completion_display_matches_hook([function])|Set or remove the completion display function. If function is specified, it will be used as the new completion display function; if omitted or None, any completion display function already installed is removed. This sets or clears the rl_completion_display_matches_hook callback in the underlying library. The completion display function is called as function(substitution, [matches], longest_match_length) once each time matches need to be displayed.（完了表示機能を設定または解除します。 functionが指定されている場合、それは新しい補完表示関数として使用されます。省略した場合、またはNoneを指定した場合は、すでにインストールされている完了表示機能が削除されます。これにより、基礎となるライブラリのrl_completion_display_matches_hookコールバックが設定またはクリアされます。補完表示関数は、一致するたびに表示される必要がある関数（代入、[matches]、longest_match_length）として呼び出されます。）

* set_completer: キーワードの頭文字などを入力してTAB押下
* set_completion_display_matches_hook: TABのみ入力

補完キーワードが`['start', 'stop', 'list', 'print']`の場合、`s` + `TAB` キー押下すると`st`となる。`start`と`stop`の２種類あるからそれ以上は表示されないらしい。`l` + `TAB`で`list`, `p` + `TAB`で`print`と補完される。

複数ある場合は、共通部分までの表示ではなく、候補をひとつずつ遷移するのが好ましい。もしくは7個以上の候補があるなら個数と全補完キーワードを網羅するとか。どう実装すればいいのかわからない。


以下参照。

* http://ja.pymotw.com/2/readline/
* http://tiswww.case.edu/php/chet/readline/readline.html
* https://github.com/search?utf8=%E2%9C%93&q=readline.set_startup_hook%28+extension%3Apy&type=Code&ref=advsearch&l=&l=

