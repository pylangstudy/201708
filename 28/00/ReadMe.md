# [6.7. readline — GNU readline のインタフェース](https://docs.python.jp/3/library/readline.html)

< [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## readline モジュール

> readline モジュールでは、補完や Python インタプリタからの履歴ファイルの読み書きを容易にするための多くの関数を定義しています。 このモジュールは直接、または rlcompleter モジュールを介して使うことができます。 rlcompleter モジュールは対話的プロンプトで Python 識別子の補完をサポートするものです。 このモジュールで利用される設定は、インタプリタの対話プロンプトならびに組み込みの input() 関数の両方の挙動に影響します。

* [rlcompleter](https://docs.python.jp/3/library/rlcompleter.html#module-rlcompleter)

### 注釈

> 下層の Readline ライブラリー API は GNU readline ではなく libedit ライブラリーで実装される可能性があります。 MacOS X では readline モジュールはどのライブラリーが使われているかを実行時に検出します。

libedit の設定ファイルは GNU readline のものとは異なります。もし設定文字列をプログラムからロードしているなら、 GNU readline と libedit を区別するために “libedit” という文字列が readline.__doc__ に含まれているかどうかチェックしてください。

```python
import readline
print(readline.__doc__)
```
```sh
$ python 0.py 
Importing this module enables command line editing using GNU readline.
```

私の環境では GNU readline が使われているようだ。

### キーバインディング

> readline のキーバインディングは初期化ファイルで設定できます。 このファイルは、たいていはホームディレクトリに .inputrc という名前で置いてあります。 GNU Readline マニュアルの Readline Init File を参照して、そのファイルの形式や可能な構成、 Readline ライブラリ全体の機能を知ってください。
