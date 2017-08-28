# [6.7.1. 初期化ファイル](https://docs.python.jp/3/library/readline.html#init-file)

< [6.7. readline — GNU readline のインタフェース](https://docs.python.jp/3/library/readline.html) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)


> 以下の関数は初期化ファイルならびにユーザ設定関連のものです:

メソッド|説明
--------|----
readline.parse_and_bind(string)|string 引数で渡された最初の行を実行します。これにより下層のライブラリーの rl_parse_and_bind() が呼ばれます。
readline.read_init_file([filename])|readline 初期化ファイルを実行します。デフォルトのファイル名は最後に使用されたファイル名です。これにより下層のライブラリーの rl_read_init_file() が呼ばれます。

例によってPython文書の説明では何をする関数なのかまったくわからない。ググった。以下参照。

* http://ja.pymotw.com/2/readline/
* http://tiswww.case.edu/php/chet/readline/readline.html

```python
import readline

readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')
while True:
    line = input('Prompt ("stop" to quit): ')
    if line == 'stop':
        break
    print('ENTERED: "%s"' % line)
```
```sh
$ python 0.py 
Prompt ("stop" to quit): abc
ENTERED: "abc"
```

viとは操作方法が違うが、以下のような機能があるらしい。

* `TAB`を入力しても無視される
* `ESC`:ノーマルモード、`i`:文字挿入モード、`a`:文字追記モード
    * モード時の表示は何もない
* `ESC`でノーマルモード
    * `h`,`l`を押下するとカーソルが左右に移動する
    * `j`,`k`を押下すると入力履歴が表示される
    * `x`を押下するとDELETEキーと同様の効果
    * `dd`と連続入力すると1行分データが削除される
    * `yy`と連続入力するとクリップボードに1行分データがコピーされる
    * `p`を押下するとクリップボードの文字列がペーストされる
    * `.`を押下すると1行分データがコピペされる
    * `b`を押下すると行頭にカーソル遷移する
    * `e`を押下すると行末にカーソル遷移する

範囲選択できるビジュアルモード`v`が使えなかった。

日本語を使うと、以下が気になった。

* IME入力中の文字が、確定済み文字列を上書きしてしまって見えなくなる。確定すると位置がずれて見えるようになる
