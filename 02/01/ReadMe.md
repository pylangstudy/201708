# [4.7.1. 文字列メソッド](https://docs.python.jp/3/library/stdtypes.html#string-methods)

< [4.7. テキストシーケンス型 — str](https://docs.python.jp/3/library/stdtypes.html#text-sequence-type-str) < [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## [4.7.1. 文字列メソッド](https://docs.python.jp/3/library/stdtypes.html#string-methods)

> 文字列は 共通の シーケンス演算全てに加え、以下に述べるメソッドを実装します。

> 文字列は、二形式の文字列書式化をサポートします。一方は柔軟さが高くカスタマイズできます (str.format()、 書式指定文字列の文法 、および カスタムの文字列書式化 を参照してください)。他方は C 言語の printf 形式の書式化に基づいてより狭い範囲と型を扱うもので、正しく扱うのは少し難しいですが、扱える場合ではたいていこちらのほうが高速です (printf 形式の文字列書式化)。

> 標準ライブラリの テキスト処理サービス 節は、その他テキストに関する様々なユーティリティ (re モジュールによる正規表現サポートなど) を提供するいくつかのモジュールをカバーしています。

## 一覧

44メソッド。

メソッド|説明
--------|----
str.capitalize()|最初の文字を大文字にし、残りを小文字にした文字列のコピーを返します。
str.casefold()|大文字小文字に関係ないマッチに使えます。
str.center(width[, fillchar])|width の長さをもつ中央寄せされた文字列を返します。
str.count(sub[, start[, end]])|出現する回数を返します。
str.encode(encoding="utf-8", errors="strict")|バイト列オブジェクトを返します。[標準エンコーディング](https://docs.python.jp/3/library/codecs.html#standard-encodings),[エラーハンドラ](https://docs.python.jp/3/library/codecs.html#error-handlers)
str.endswith(suffix[, start[, end]])|文字列が指定された suffix で終わるなら True を、そうでなければ False を返します。
str.expandtabs(tabsize=8)|文字列内の全てのタブ文字が 1 つ以上のスペースで置換された、文字列のコピーを返します。
str.find(sub[, start[, end]])|s[start:end] に部分文字列 sub が含まれる場合、その最小のインデックスを返します。
str.format(*args, **kwargs)|[書式指定文字列の文法](https://docs.python.jp/3/library/string.html#formatstrings)を参照。
str.format_map(mapping)|format()の引数dict版。
str.index(sub[, start[, end]])|find() と同様ですが、部分文字列が見つからなかったとき ValueError を送出します。
str.isalnum()|文字列中の全ての文字が英数字で、かつ 1 文字以上あるなら真を、そうでなければ偽を返します。
str.isalpha()|文字列中の全ての文字が英字で、かつ 1 文字以上あるなら真を、そうでなければ偽を返します。
str.isdecimal()|文字列中の全ての文字が十進数字で、かつ 1 文字以上あるなら真を、そうでなければ偽を返します。
str.isdigit()|文字列中の全ての文字が数字で、かつ 1 文字以上あるなら真を、そうでなければ偽を返します。
str.isidentifier()|[識別子 (identifier) およびキーワード (keyword)](https://docs.python.jp/3/reference/lexical_analysis.html#identifiers)節の言語定義における有効な識別子であれば真を返します。予約済みの識別子か判定するには[keyword.iskeyword() ](https://docs.python.jp/3/library/keyword.html#keyword.iskeyword)
str.islower()|文字列中の大小文字の区別のある文字 [4] 全てが小文字で、かつ大小文字の区別のある文字が 1 文字以上あるなら真を、そうでなければ偽を返します。
str.isnumeric()|文字列中の全ての文字が数を表す文字で、かつ 1 文字以上あるなら真を、そうでなければ偽を返します。
str.isprintable()|文字列中のすべての文字が印字可能であるか、文字列が空であれば真を、そうでなければ偽を返します。
str.isspace()|文字列が空白文字のみで構成され、かつ 1 文字以上ある場合には真を、そうでなければ偽を返します。
str.istitle()|文字列がタイトルケース文字列であり、かつ 1 文字以上ある場合、真を返します。
str.isupper()|全てが大文字なら真
str.join(iterable)|イテラブル iterable 中の文字列を結合した文字列を返します。
str.ljust(width[, fillchar])|長さ width の左揃えした文字列を返します。
str.lower()|全てが小文字に変換された、文字列のコピーを返します。
str.lstrip([chars])|文字列の先頭の文字を除去したコピーを返します。
static str.maketrans(x[, y[, z]])|str.translate() に使える変換テーブルを返します。
str.partition(sep)|文字列を sep の最初の出現位置で区切り、 3 要素のタプルを返します。
str.replace(old, new[, count])|文字列をコピーし、現れる部分文字列 old 全てを new に置換して返します。
str.rfind(sub[, start[, end]])|s[start:end] に sub が含まれる場合、その最大のインデックスを返します。
str.rindex(sub[, start[, end]])|rfind() と同様ですが、 sub が見つからなかった場合 ValueError を送出します。
str.rjust(width[, fillchar])|width の長さをもつ右寄せした文字列を返します。
str.rpartition(sep)|文字列を sep の最後の出現位置で区切り、 3 要素のタプルを返します。
str.rsplit(sep=None, maxsplit=-1)|sep を区切り文字とした、文字列中の単語のリストを返します。 
str.rstrip([chars])|文字列の末尾部分を除去したコピーを返します。
str.split(sep=None, maxsplit=-1)|文字列を sep をデリミタ文字列として区切った単語のリストを返します。
str.splitlines([keepends])|文字列を改行部分で分解し、各行からなるリストを返します。
str.startswith(prefix[, start[, end]])|文字列が指定された prefix で始まるなら True を、そうでなければ False を返します。 
str.strip([chars])|文字列の先頭および末尾部分を除去したコピーを返します。
str.swapcase()|大文字が小文字に、小文字が大文字に変換された、文字列のコピーを返します。
str.title()|文字列をタイトルケースにして返します。単語ごとに先頭大文字、他は全て小文字にする。
str.translate(table)|与えられた変換テーブルに基づいて文字列を構成する各文字をマッピングし、マッピング後の文字列のコピーを返します。
str.upper()|全てが大文字に変換された、文字列のコピーを返します。
str.zfill(width)|長さが width になるよう ASCII '0' で左詰めした文字列のコピーを返します。

## ソースコード

各ソースコードファイル参照。

