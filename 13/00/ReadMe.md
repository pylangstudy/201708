# [6.2.3. 正規表現オブジェクト](https://docs.python.jp/3/library/re.html#regular-expression-syntax)

< [6.2. re — 正規表現操作](https://docs.python.jp/3/library/re.html#module-re) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

> コンパイル済み正規表現オブジェクトは以下のメソッドと属性をサポートします:

## 正規表現オブジェクト

正規表現オブジェクトとは、`re.compile(r'^ab', re.IGNORECASE)`のようにしたものの戻り値である。

よくわからなくなってきたので、以下で一度まとめる。

## 正規表現の全体像

正規表現の制御における全体像がわかりづらい。現時点での私の認識を書き出してみる。（間違っているかもしれない）

### 正規表現におけるオブジェクトの関係

正規表現は、`re`モジュールにはじまり, `regex`(re.compile()の戻り値)オブジェクト, `match`(re.search(), regex.search()等の戻り値)オブジェクトの順に操作していく。

オブジェクト|説明
------------|----
regex|正規表現パターンをコンパイルしたもの
match|正規表現による検索結果

```
import re
|___________________________________________________________________
|                   |                   |           |               |
re.compile()        re.search() etc     re.sub()    re.findall()    re.finditer()
|                   |                   |           | .split()      |
regex               |                   |           |               |
|                   |                   |           |               |
regex.search() etc  |                   |           |               |
|___________________|                   |           |               |
|                                       |           |               |
match                                   |           |               |
|                                       |           |               |
match.groups() etc                      |           |               |
|                                       |           |               |
tuple<str>                              str         list<str>       iter<str>
```

### `re`と`regex`

`re.search()`と`regex.search()`の違いが微妙。イマイチわからない。コンパイル済みか否かではない。

[6.2.2. モジュールコンテンツ](https://docs.python.jp/3/library/re.html#module-contents)によると以下。

> この関数の一部はコンパイルした正規表現の完全版メソッドを簡略化したバージョンです。

`re.search()`は`regex.search()`の省略形らしい。

> コンパイルされた形式が用いられるのが普通です。

つまり、ふつうは`re.search()`でなく`regex.search()`の形式が用いられるらしい。（省略しない形式）

## メソッド

メソッド|概要
--------|----
regex.search(string[, pos[, endpos]])|string を走査し、正規表現がマッチする最初の場所を探して、対応する match オブジェクト を返します。文字列内にパターンにマッチする場所がない場合は None を返します;
regex.match(string[, pos[, endpos]])|string の 先頭の 0 個以上の文字がこの正規表現とマッチする場合、対応する マッチオブジェクト を返します。文字列がパタンーとマッチしない場合、None を返します。
regex.fullmatch(string[, pos[, endpos]])|string 全体がこの正規表現にマッチした場合、対応する match オブジェクト を返します。文字列にパターンにマッチする場所が無い場合は None を返します;バージョン 3.4 で追加.
regex.split(string, maxsplit=0)|split() 関数と同様で、コンパイルしたパターンを使います。ただし、 match() と同じように、省略可能な pos, endpos 引数で検索範囲を指定することができます。
regex.findall(string[, pos[, endpos]])|findall() 関数と同様で、コンパイルしたパターンを使います。ただし、 match() と同じように、省略可能な pos, endpos 引数で検索範囲を指定することができます。
regex.finditer(string[, pos[, endpos]])|finditer() 関数と同様で、コンパイルしたパターンを使います。ただし、 match() と同じように、省略可能な pos, endpos 引数で検索範囲を指定することができます。
regex.sub(repl, string, count=0)|sub() 関数と同様で、コンパイルしたパターンを使います。
regex.subn(repl, string, count=0)|subn() 関数と同様で、コンパイルしたパターンを使います。

### regex.splitの説明文は嘘

> split() 関数と同様で、コンパイルしたパターンを使います。ただし、 match() と同じように、省略可能な pos, endpos 引数で検索範囲を指定することができます。

とあるが、「pos, endpos 引数で検索範囲を指定することができます」は嘘である。コピペミスと思われる。`regex.split(string, maxsplit=0)`の通り、引数はその2つのみ。pos, endpos引数はない。実際にコードを書いて確かめた。split.py参照。

### searchとmatchの違い

メソッド|説明
--------|----
search|部分一致（文字列のどこか一部にパターンが存在すればmatchオブジェクトを返す）
match|先頭一致（文字列の先頭がパターンと一致すればmatchオブジェクトを返す）

* `search(pattern='^ab')` ＝ `match(pattern='ab')`

matchはsearchで代用できる。パターン文字列に先頭を示す`^`を使えばいい。

[6.2.5.3. search() vs. match()](https://docs.python.jp/3/library/re.html#search-vs-match)参照。

MULTILINE モードのときに違いが生じるらしいので、正確には代用できない。

### searchとmatchとfullmatchの違い

メソッド|説明
--------|----
search|部分一致（文字列のどこか一部にパターンが存在すればmatchオブジェクトを返す）
match|前方一致（文字列の先頭がパターンと一致すればmatchオブジェクトを返す）
fullmatch|完全一致

こうなると、後方一致がないのが気になる。`^`や`$`で先頭と末尾を表現すればいいのだろうが、それならsearchだけで全パターン網羅できるのでは？下手にメソッドを使い分けると、正規表現文字列を流用しづらくならないか？

https://so-kai-app.sakura.ne.jp/blog/1527/2016/12/14/

## フラグ

フラグ|概要
--------|----
regex.flags|正規表現のマッチングフラグです。これは compile() で指定されたフラグ、パターン内の (?...) インラインフラグ、およびパターンが Unicode 文字列だった時の UNICODE のような暗黙のフラグとの組み合わせになりなす。
regex.groups|パターンにあるキャプチャグループの数です。
regex.groupindex|(?P<id>) で定義された任意の記号グループ名の、グループ番号への辞書マッピングです。もし記号グループがパターン内で何も使われていなければ、辞書は空です。
regex.pattern|RE オブジェクトがコンパイルされたときに使用された元のパターン文字列です。

## 試してみる

### 参考

Web上で試せるツールを探した。

* https://nelog.jp/regular-expression-online-tools
* http://qiita.com/AQRiL_1132/items/c185c7ad84c129e5a2df

### Webツール

URL|Python正規表現|URLシェア|入力の楽さ|見やすさ|応答速度|Pythonソースコード生成
---|--------------|---------|----------|--------|--------|----------------------
https://regex101.com/|○|○|○|○|✗|○
https://www.debuggex.com/|○|○|△|○|○|?
http://www.rexv.org/|○|✗|△|○|○|?
http://www.regexplanet.com/|○|○|✗|✗|?

Pythonの正規表現に対応したツール。

https://translate.googleusercontent.com/translate_c?act=url&depth=1&hl=ja&ie=UTF8&prev=_t&rurl=translate.google.co.jp&sl=en&sp=nmt4&tl=ja&u=https://github.com/firasdib/Regex101/wiki/FAQ&usg=ALkJrhg6mpYcn6-tWF9X-lZiNLa2aAFZYQ

