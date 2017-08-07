# [5.2. 具象例外](https://docs.python.jp/3/library/exceptions.html#concrete-exceptions)

[5. 組み込み例外](https://docs.python.jp/3/library/exceptions.html#built-in-exceptions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

> 以下の例外は、通常送出される例外です。

## 説明

名前|説明
----|----
exception AssertionError|assert 文が失敗した場合に送出されます。
exception AttributeError|属性参照 (属性参照 を参照) や代入が失敗した場合に送出されます
exception EOFError|input() が何もデータを読まずに end-of-file (EOF) に達した場合に送出されます。
exception FloatingPointError|浮動小数点演算が失敗した場合に送出されます。
exception GeneratorExit|ジェネレータ や コルーチン が閉じられたときに送出されます。
exception ImportError|import 文でモジュールをロードしようとして問題が発生すると送出されます。
exception ModuleNotFoundError|ImportError のサブクラスで、import 文でモジュールが見つからない場合に送出されます。また、 sys.modules に None が含まれる場合にも送出されます。
exception IndexError|シーケンスの添字が範囲外の場合に送出されます。
exception KeyError|マッピング (辞書) のキーが、既存のキーの集合内に見つからなかった場合に送出されます。
exception KeyboardInterrupt|ユーザが割り込みキー (通常は Control-C または Delete) を押した場合に送出されます。
exception MemoryError|ある操作中にメモリが不足したが、その状況は (オブジェクトをいくつか消去することで) まだ復旧可能かもしれない場合に送出されます。
exception NameError|ローカルまたはグローバルの名前が見つからなかった場合に送出されます。
exception NotImplementedError|この例外は RuntimeError から派生しています。
exception OSError([arg]), (errno, strerror[, filename[, winerror[, filename2]]])|この例外はシステム関数がシステム関連のエラーを返した場合に送出されます。例えば “file not found” や “disk full” のような I/O の失敗が発生したときです。`errno, winerror, strerror, filename, filename2`
exception OverflowError|算術演算の結果が表現できない大きな値になった場合に送出されます。これは整数では起こりません (むしろ MemoryError が送出されることになるでしょう)。しかし、歴史的な理由のため、要求された範囲の外の整数に対して OverflowError が送出されることがあります。
exception RecursionError|この例外は RuntimeError を継承しています。インタープリタが最大再帰深度 (sys.getrecursionlimit() を参照) の超過を検出すると送出されます。
exception ReferenceError|weakref.proxy() によって生成された弱参照 (weak reference) プロキシを使って、ガーベジコレクションによって回収された後の参照対象オブジェクトの属性にアクセスした場合に送出されます。
exception RuntimeError|他のカテゴリに分類できないエラーが検出された場合に送出されます。
exception StopIteration|組込み関数 next() と iterator の __next__() メソッドによって、そのイテレータが生成するアイテムがこれ以上ないことを伝えるために送出されます。
exception StopAsyncIteration|イテレーションを停止するために、 asynchronous iterator オブジェクトの __anext__() メソッドによって返される必要があります。
exception SyntaxError|パーザが構文エラーに遭遇した場合に送出されます。属性 filename, lineno, offset, text を持ちます。
exception IndentationError|正しくないインデントに関する構文エラーの基底クラスです。
exception TabError|タブとスペースを一貫しない方法でインデントに使っているときに送出されます。
exception SystemError|インタプリタが内部エラーを発見したが、状況は全ての望みを棄てさせるほど深刻ではないと思われる場合に送出されます。
exception SystemExit|この例外は sys.exit() 関数から送出されます。`code`
exception TypeError|組み込み演算または関数が適切でない型のオブジェクトに対して適用された際に送出されます。
exception UnboundLocalError|関数やメソッド内のローカルな変数に対して参照を行ったが、その変数には値が代入されていなかった場合に送出されます。
exception UnicodeError|Unicode に関するエンコードまたはデコードのエラーが発生した際に送出されます。 ValueError のサブクラスです。`encoding, reason, object, start, end`
exception UnicodeEncodeError|Unicode 関連のエラーがエンコード中に発生した際に送出されます。 UnicodeError のサブクラスです。
exception UnicodeDecodeError|Unicode 関連のエラーがデコード中に発生した際に送出されます。 UnicodeError のサブクラスです。
exception UnicodeTranslateError|Unicode 関連のエラーが変換中に発生した際に送出されます。 UnicodeError のサブクラスです。
exception ValueError|組み込み演算や関数が、正しい型だが適切でない値を受け取った場合や、 IndexError のような詳細な例外では説明のできない状況で送出されます。
exception ZeroDivisionError|除算や剰余演算の第二引数が 0 であった場合に送出されます。
exception EnvironmentError|
exception IOError|
exception WindowsError|Windows でのみ利用できます。

