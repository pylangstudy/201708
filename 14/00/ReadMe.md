# [6.2.4. match オブジェクト](https://docs.python.jp/3/library/re.html#match-objects)

< [6.2. re — 正規表現操作](https://docs.python.jp/3/library/re.html#module-re) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

正規表現の[全体像](https://github.com/pylangstudy/201708/tree/master/13/00)。

## matchオブジェクト

> マッチオブジェクトは常にブール値 True を持ちます。 match() と search() はマッチしなかった場合に None を返すので、単純な if ステートメントによってマッチしたかどうかをテストできます:

```python
match = re.search(pattern, string)
if match:
    process(match)
```
```python
#!python3.6
#coding:utf-8
import re
match = re.search(r'^ab', 'ABC', re.IGNORECASE)
if match: print('一致した。')
else: print('一致しない。')

match = re.search(r'^ab', 'CDE', re.IGNORECASE)
if match: print('一致した。')
else: print('一致しない。')
```
```sh
$ python 0.py 
一致した。
一致しない。
```

> マッチオブジェクトは以下のメソッドと属性をサポートしています:

## メソッド

メソッド|概要
--------|----

match.expand(template)|テンプレート文字列 template に対し、sub() メソッドがするようなバックスラッシュ置換をして得られる文字列を返します。バージョン 3.5 で変更: マッチしないグループは空文字列に置き換えられます。
match.group([group1, ...])|マッチした1個以上のサブグループを返します。バージョン 3.6 で追加.
match.groups(default=None)|パターンにマッチしたすべてのサブグループを含む、パターン内で指定されたグループ数分の要素を持つタプルを返します。
match.start([group]), match.end([group])|group とマッチした部分文字列の先頭と末尾のインデックスを返します。 
match.span([group])|マッチ m について、大きさ2のタプル (m.start(group), m.end(group)) を返します。

## 値

値|概要
--|----
match.pos|正規表現オブジェクト の search() か match() に渡された pos の値です。
match.endpos|正規表現オブジェクト の search() か match() に渡された endpos の値です。
match.lastindex|最後にマッチした取り込みグループの整数インデックスです。
match.lastgroup|最後にマッチした取り込みグループの名前です。
match.re|このマッチインスタンスを match() あるいは search() メソッドで生成した正規表現オブジェクトです。
match.string|match() または search() へ渡された文字列です。

## グループ化した値の取得

```python
import re

li_tag = '''<li>Apple</li>
<li>Orange</li>
<li>Meron</li>
<li>Grape</li>
<li>Cherry</li>
'''
regex = re.compile(r'<li>(.+?)<\/li>', re.IGNORECASE)
matches = regex.finditer(li_tag)
for match in matches:
    print(match)
    print(match.lastindex, match.groups())
```

### 複数のmatchオブジェクトを取得するには`finditer()`しかない

* 要点: 複数のmatchオブジェクトを取得するには`finditer()`しかない

`search()`, `match()`, `fullmatch()`, は1つ目のmatchオブジェクトしか返さない。`sub()`, `split()`, `findall()`は文字列を返してmatchオブジェクトは返さない。

メソッド|一致|戻り値
--------|----|------
search|部分一致|match(最初のmatchオブジェクトのみ)
match|前方一致|match(最初のmatchオブジェクトのみ)
fullmatch|完全一致|match(最初のmatchオブジェクトのみ)
finditer|部分一致|iter<match>(全matchオブジェクト)
findall|部分一致|list<str>

#### 極めてわかりにくいメソッド名

メソッド名から違いを想像するのが不可能。

名付けのせいで紛らわしいのが分かりにくさに拍車をかけている。加えてPythonはオーバーロードできないので同一名で別引数パターンのメソッドが作れない。よって別の名前にするしかないという言語仕様上の背景がある。

### 参考

Python文書と比べても、とてもシンプルでわかりやすかった。感謝。

http://d.hatena.ne.jp/yumimue/20071220/1198141598

### 全体像

正規表現でグループ化した値を取得するまでの全体像。

```
import re
|
re.compile()
|
regex
|
regex.finditer()
|
iter<match>
|
match
|
match.groups()
|
tuple<str>
```

### わかりにくい→毎回調査→面倒→使わず無価値化…

ものすごく長い。また、これを発見するまでにあらゆる組合せを試す羽目になった。どのメソッドで何ができるのか、よくわからない。覚えていないと同じことを繰り返しそう。しかしメソッド名がわかりにくくて数が多いため覚えられない。Python文書もわかりにくい。

結論としては、とにかく面倒でもfinditer()を使えばメソッド使い分けを意識しなくて済むだろうか？どうにかしないと、以下のようにPythonで正規表現を使わなくなる結果になりそう。

* どんな正規表現で表せばいいのか
* Pythonではどのように実装すればいいのか
    * どういう操作をするときに、何のパッケージ、モジュール、メソッド、変数、引数、型を使えばいいのか
        * `finditer()`, `search()`, `match()`, `fullmatch()`, `sub()`, `split()`, `findall()`などの名前から各種メソッドの違いがわからない→使い分けられず混乱する→毎回資料をみざるをえない→面倒になる→結果的にPythonやreモジュールの使用を避けてしまう→価値なし

正規表現だけでも難しいのに、Python言語による面倒さがさらに使いづらさを助長していると思う。他の言語でも使いづらいものなのだろうか？

### グループが複数あるとき

```python
import re

li_tag = '''a=1
b=2
c=3
'''
regex = re.compile(r'(.+?)=(.+?)', re.IGNORECASE)
matches = regex.finditer(li_tag)
for match in matches:
    print(match)
    print(match.lastindex, match.groups())
    for i in range(match.lastindex): print(match[i])
    print(match.expand(r'\1 value is \2'))
```

左側の`(.+?)`と、右側の`(.+?)`をそれぞれ取得できる。`match.groups()`で。

ここまでできれば、かなり自由に制御できそう。

こういう、シンプルなコードで正規表現の多機能さがアピールされている例が欲しかった。他のsearch()などのメソッドは略式やオマケと考えていいのでは？`finditer()`の使い方を覚えれば全部できるのでは？

## 正規表現Webツール

* https://nelog.jp/regular-expression-online-tools
* http://qiita.com/AQRiL_1132/items/c185c7ad84c129e5a2df

URL|Python正規表現|URLシェア|入力の楽さ|見やすさ|応答速度|Pythonソースコード生成
---|--------------|---------|----------|--------|--------|----------------------
https://regex101.com/|○|○|○|○|✗|○
https://www.debuggex.com/|○|○|△|○|○|?
http://www.rexv.org/|○|✗|△|○|○|?
http://www.regexplanet.com/|○|○|✗|✗|?

