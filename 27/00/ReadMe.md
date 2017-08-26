# [6.6. stringprep — インターネットのための文字列調製](https://docs.python.jp/3/library/stringprep.html)

< [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

* ソースコード: [Lib/stringprep.py](https://github.com/python/cpython/tree/3.6/Lib/stringprep.py)
* [RFC 3454](https://tools.ietf.org/html/rfc3454.html)
* http://www.jdna.jp/survey/rfc/rfc3454j.html
* https://www.ibm.com/support/knowledgecenter/ja/SSLTBW_2.2.0/com.ibm.zos.v2r2.cunu100/strpconv.htm?cp=SSLTBW_2.2.0

stringprepはPythonにおけるRFC3454実装と思われる。RFC3454はUnicode文字列の処理ルールのことらしい。

> 国際化文字列...は多様な入力と表示形態を持つため、一貫した方法で文字列を比較することは困難である。

> 本文書はUnicode文字列に対する処理ルールの枠組みを規定する。

> その意図は、全世界の典型的ユーザーが納得できる形で文字列の入力と文字列の比較が正常に動作する可能性を大きくすることにある。

> stringprepプロトコルはプロトコル識別子の値、社名や人名、国際化ドメイン名、他の文字列に有用なものである。

[unicodedata](https://docs.python.jp/3/library/unicodedata.html)とあわせてUnicode文字を正確に扱えるようになりそう。

## 使い方

使い方がわからなかった。

> stringprep.in_table_a1(code)(原文)

>    code がテーブル A.1 (Unicode 3.2 における未割り当てコードポイント: unassigned code point) かどうか判定します。

とあった。引数codeには0x00000〜0x2FFFFのint値を入力するものだと思っていた。しかし以下エラーが出た。

> TypeError: category() argument must be a unicode character, not int

正しくはUnicode文字1字を入力するらしい。（だったら引数名はcodeでなくchrなどにして欲しかった）

GitHubで使われているコードを検索した。引数に`text[x]`が渡されているコードがあったので、1文字を渡していることが予想できた。

https://github.com/search?utf8=%E2%9C%93&q=stringprep.in_table_a1+extension%3Apy&type=Code&ref=advsearch&l=&l=

Pythonは型の宣言がないせいでわかりづらい。同様の調査はあらゆる場面で必要になる。

## 一覧

メソッド|説明
--------|----
in_table_a1(code)|code がテーブル A.1 (Unicode 3.2 における未割り当てコードポイント: unassigned code point) かどうか判定します。
in_table_b1(code)|code がテーブル B.1 (一般には何にも対応付けられていない: commonly mapped to nothing) かどうか判定します。
map_table_b2(code)|テーブル B.2 (NFKC で用いられる大小文字の対応付け) に従って、code に対応付けられた値を返します。
map_table_b3(code)|テーブル B.3 (正規化を伴わない大小文字の対応付け) に従って、code に対応付けられた値を返します。
in_table_c11(code)|code がテーブル C.1.1 (ASCII スペース文字) かどうか判定します。
in_table_c12(code)|code がテーブル C.1.2 (非 ASCII スペース文字) かどうか判定します。
in_table_c11_c12(code)|code がテーブル C.1 (スペース文字、C.1.1 および C.1.2 の和集合) かどうか判定します。
in_table_c21(code)|code がテーブル C.2.1 (ASCII 制御文字) かどうか判定します。
in_table_c22(code)|code がテーブル C.2.2 (非 ASCII 制御文字) かどうか判定します。
in_table_c21_c22(code)|code がテーブル C.2 (制御文字、C.2.1 および C.2.2 の和集合) かどうか判定します。
in_table_c3(code)|code がテーブル C.3 (プライベート利用) かどうか判定します。
in_table_c4(code)|code がテーブル C.4 (非文字コードポイント: non-character code points) かどうか判定します。
in_table_c5(code)|code がテーブル C.5 (サロゲーションコード) かどうか判定します。
in_table_c6(code)|code がテーブル C.6 (平文:plain text として不適切) かどうか判定します。
in_table_c7(code)|code がテーブル C.7 (標準表現:canonical representation として不適切) かどうか判定します。
in_table_c8(code)|code がテーブル C.8 (表示プロパティの変更または撤廃) かどうか判定します。
in_table_c9(code)|code がテーブル C.9 (タグ文字) かどうか判定します。
in_table_d1(code)|code がテーブル D.1 (双方向プロパティ “R” または “AL” を持つ文字) かどうか判定します。
in_table_d2(code)|code がテーブル D.2 (双方向プロパティ “L” を持つ文字) かどうか判定します。

