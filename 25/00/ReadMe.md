# [6.4. textwrap — テキストの折り返しと詰め込み](https://docs.python.jp/3/library/textwrap.html)

< [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/textwrap.py](https://github.com/python/cpython/tree/3.6/Lib/textwrap.py)

> textwrap モジュールは、実際の処理を行う TextWrapper とともに、いくつかの便利な関数を提供しています。1つか2つの文字列を wrap あるいは fill するだけの場合は便利関数で十分ですが、多くの処理を行う場合は効率のために TextWrapper のインスタンスを使うべきでしょう。

## textwrapモジュール

メソッド|概要
--------|----
textwrap.wrap(text, width=70, **kwargs)|text (文字列)内の段落を一つだけ折り返しを行います。
textwrap.fill(text, width=70, **kwargs)|text 内の段落を一つだけ折り返しを行い、折り返しが行われた段落を含む一つの文字列を返します。 fill() はこれの省略表現です
textwrap.shorten(text, width, **kwargs)|与えられた text を折りたたみ、切り詰めて、与えられた width に収まるようにします。
textwrap.dedent(text)|text の各行に対し、共通して現れる先頭の空白を削除します。
textwrap.indent(text, prefix, predicate=None)|text の中の選択された行の先頭に prefix を追加します。

## TextWrapperクラス

コンストラクタ|概要
--------------|----
class textwrap.TextWrapper(**kwargs)|TextWrapper コンストラクタはたくさんのオプションのキーワード引数を受け取ります。TextWrapper インスタンス属性(とコンストラクタのキーワード引数)は以下の通りです:
width|(デフォルト: 70) 折り返しが行われる行の最大の長さ。入力行に width より長い単一の語が無い限り、 TextWrapper は width 文字より長い出力行が無いことを保証します。
expand_tabs|(デフォルト: True) もし真ならば、そのときは text 内のすべてのタブ文字は text の expandtabs() メソッドを用いて空白に展開されます。
tabsize|(デフォルト: 8) expand_tabs が真の場合、 text の中のすべてのTAB文字は tabsize と現在のカラムに応じて、ゼロ以上のスペースに展開されます。
replace_whitespace|(デフォルト: True) 真の場合、 wrap() メソッドはタブの展開の後、 wrap 処理の前に各種空白文字をスペース1文字に置換します。置換される空白文字は: TAB, 改行, 垂直TAB, FF, CR ('\t\n\v\f\r') です。
drop_whitespace|(デフォルト: True) 真の場合、(wrap 処理のあとインデント処理の前に) 各行の最初と最後の空白文字を削除します。ただし、段落の最初の空白については、次の文字が空白文字でない場合は削除されません。削除される空白文字が行全体に及ぶ場合は、行自体を削除します。
initial_indent|(default: '') wrap の出力の最初の行の先頭に付与する文字列。最初の行の長さに加算されます。空文字列の場合インデントされません。
subsequent_indent|(デフォルト: '') 一行目以外の折り返しが行われる出力のすべての行の先頭に付けられる文字列。一行目以外の各行の折り返しまでの長さにカウントされます。
fix_sentence_endings|(デフォルト: False) もし真ならば、 TextWrapper は文の終わりを見つけようとし、確実に文がちょうど二つの空白で常に区切られているようにします。これは一般的に固定スペースフォントのテキストに対して望ましいです。
break_long_words|(デフォルト: True) もし真ならば、そのとき width より長い行が確実にないようにするために、 width より長い語は切られます。偽ならば、長い語は切られないでしょう。そして、 width より長い行があるかもしれません。 (width を超える分を最小にするために、長い語は単独で一行に置かれるでしょう。)
break_on_hyphens|(デフォルト: True) 真の場合、英語で一般的なように、ラップ処理は空白か合成語に含まれるハイフンの直後で行われます。偽の場合、空白だけが改行に適した位置として判断されます。ただし、本当に語の途中で改行が行われないようにするためには、 break_long_words 属性を真に設定する必要があります。
max_lines|(デフォルト None) None 以外の場合、出力は行数 max_lines を超えないようにされ、切り詰める際には出力の最後の行を placeholder に置き換えます。
placeholder|(デフォルト: ' [...]') 切り詰める場合に出力の最後の行に置く文字列です。

メソッド|概要
--------|----
wrap(text)|1段落の文字列 text を、各行が width 文字以下になるように wrap します。 wrap のすべてのオプションは TextWrapper インスタンスの属性から取得します。結果の、行末に改行のない行のリストを返します。出力の内容が空になる場合は、返すリストも空になります。
fill(text)|text 内の段落を一つだけ折り返しを行い、折り返しが行われた段落を含む一つの文字列を返します。

