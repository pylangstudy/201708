# [6.8. rlcompleter — GNU readline向け補完関数](https://docs.python.jp/3/library/rlcompleter.html)

< [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

rlcompleterは何の役に立つのか。どこで、どうやって使うのか。よくわからなかった。

> rlcompleter モジュールではPythonの識別子やキーワードを定義した readline モジュール向けの補完関数を定義しています。

> このモジュールが Unixプラットフォームでimportされ、 readline が利用できるときには、 Completer クラスのインスタンスが自動的に作成され、 complete() メソッドが readline 補完に設定されます。

> 以下はプログラム例です:

```python
>>> import rlcompleter
>>> import readline
>>> readline.parse_and_bind("tab: complete")
>>> readline. <TAB PRESSED>
readline.__doc__          readline.get_line_buffer(  readline.read_init_file(
readline.__file__         readline.insert_text(      readline.set_completer(
readline.__name__         readline.parse_and_bind(
>>> readline.
```

> rlcompleter モジュールは、 Python の 対話モード と一緒に使用するのを意図して設計されています。Python を -S オプションをつけずに実行している場合、このモジュールが自動的にインポートされ、構成されます (readline の設定 を参照)。

> readline のないプラットフォームでも、このモジュールで定義される Completer クラスは独自の目的に使えます。


TABを2回押下したら出た。readlineモジュールが持つメソッド一覧が。

```sh
$ python
Python 3.6.1 (default, Apr 24 2017, 22:16:16) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import rlcompleter
>>> import readline
>>> readline.parse_and_bind("tab: complete")
>>> readline.
readline.add_history(
readline.append_history_file(
readline.clear_history(
readline.get_begidx(
readline.get_completer(
readline.get_completer_delims(
readline.get_completion_type(
readline.get_current_history_length(
readline.get_endidx(
readline.get_history_item(
readline.get_history_length(
readline.get_line_buffer(
readline.insert_text(
readline.parse_and_bind(
readline.read_history_file(
readline.read_init_file(
readline.redisplay(
readline.remove_history_item(
readline.replace_history_item(
readline.set_auto_history(
readline.set_completer(
readline.set_completer_delims(
readline.set_completion_display_matches_hook(
readline.set_history_length(
readline.set_pre_input_hook(
readline.set_startup_hook(
readline.write_history_file(
>>> readline.
```

対話モードのときにしか使えないらしい。

mymodule.py
```python
def mymethod(): print('mymethod')
```

```sh
$ python 
Python 3.6.1 (default, Apr 24 2017, 22:16:16) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import mymodule
>>> import rlcompleter
>>> import readline
>>> readline.parse_and_bind("tab: complete")
>>> mymodule.
```
直後、TABキー押下すると、以下のようにメソッド名が出た。
```sh
>>> mymodule.mymethod(
```

まさかと思ってrlcompleter,readlineを抜いてやってみたが、普通にできた。

```
$ python 
Python 3.6.1 (default, Apr 24 2017, 22:16:16) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import mymodule
>>> mymodule.mymethod(  
```

一体rlcompleterは何のためにあるのか？

以下参照。

* http://ja.pymotw.com/2/readline/
* http://tiswww.case.edu/php/chet/readline/readline.html
* https://github.com/search?utf8=%E2%9C%93&q=readline.set_startup_hook%28+extension%3Apy&type=Code&ref=advsearch&l=&l=

