# [6.1.4. テンプレート文字列](https://docs.python.jp/3/library/string.html#template-strings)

< [6.1.3. 書式指定文字列の文法](https://docs.python.jp/3/library/string.html#format-string-syntax) < [6.1. string — 一般的な文字列操作](https://docs.python.jp/3/library/string.html#module-string) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## 書式

> テンプレート (template) を使うと、 PEP 292 で解説されているようにより簡潔に文字列置換 (string substitution) を行えるようになります。通常の % ベースの置換に代わって、テンプレートでは以下のような規則に従った $ ベースの置換をサポートしています:

* [PEP 292](https://www.python.org/dev/peps/pep-0292)

> * $$ はエスケープ文字です; $ 一つに置換されます。

> * $identifier は "identifier" のマッピングキーに合致する置換プレースホルダーを指定します。デフォルトでは、 "identifier" は大文字と小文字を区別しない ASCII 英数字 (アンダースコアを含む) からなら文字列に制限されています。文字列はアンダースコアか ASCII 文字から始まるものでなければなりません。$ の後に識別子に使えない文字が出現すると、そこでプレースホルダ名の指定が終わります。

> * ${identifier} は $identifier と同じです。プレースホルダ名の後ろに識別子として使える文字列が続いていて、それをプレースホルダ名の一部として扱いたくない場合、例えば "${noun}ification" のような場合に必要な書き方です。

> 上記以外の書き方で文字列中に $ を使うと ValueError を送出します。

> string モジュールでは、上記のような規則を実装した Template クラスを提供しています。 Template のメソッドを以下に示します:


## 

項目|説明
----|----
class string.Template(template)|コンストラクタはテンプレート文字列になる引数を一つだけ取ります。
substitute(mapping, **kwds)|テンプレート置換を行い、新たな文字列を生成して返します。
safe_substitute(mapping, **kwds)|substitute() と同じですが、このメソッドが「安全 (safe) 」と呼ばれているのは、置換操作が常に例外を送出する代わりに利用可能な文字列を返そうとするからです。:
template|コンストラクタの引数 template に渡されたオブジェクトです。

### ソースコード

```python
#!python3.6
from string import Template
s = Template('$who likes $what')
print(s.substitute(who='tim', what='kung pao'))

d = dict(who='tim')
#print(Template('Give $who $100').substitute(d))#ValueError: Invalid placeholder in string: line 1, col 11
#print(Template('$who likes $what').substitute(d))#KeyError: 'what'
print(Template('$who likes $what').safe_substitute(d))
```
```sh
$ python 0.py 
tim likes kung pao
tim likes $what
```

## サブクラスを派生

> さらに進んだ使い方:Template のサブクラスを派生して、プレースホルダの書式、区切り文字、テンプレート文字列の解釈に使われている正規表現全体をカスタマイズできます。こうした作業には、以下のクラス属性をオーバライドします:

>    delimiter – プレースホルダの開始を示すリテラル文字列です。デフォルトの値は $ です。実装系はこの文字列に対して必要に応じて re.escape() を呼び出すので、正規表現を表すような文字列にしては なりません 。

>    idpattern – 波括弧でくくらない形式のプレースホルダの表記パターンを示す正規表現です (波括弧は自動的に適切な場所に追加されます)。デフォルトの値は [_a-z][_a-z0-9]* という正規表現です。

>    flags – 代入の認識のために使用される正規表現をコンパイルする際に適用される正規表現フラグ。デフォルト値は re.IGNORECASE です。re.VERBOSE が常にフラグに追加されるということに注意してください。したがって、カスタムな idpattern は verbose 正規表現の規約に従わなければなりません。

>    バージョン 3.2 で追加.

```python
#!python3.6
from string import Template
class MyTemplate(Template):
    delimiter = '%'

s = MyTemplate('%who likes %what')
print(s.substitute(who='tim', what='kung pao'))

d = dict(who='tim')
print(MyTemplate('%who likes %what').safe_substitute(d))
```
```sh
$ python 1.py 
tim likes kung pao
tim likes %what
```

```python
#!python3.6
from string import Template
class MyTemplate(Template):
    idpattern = '[a-z]+_[a-z]+' # 英字しか使えなくなる。デフォルトの値は [_a-z][_a-z0-9]*

s = Template('$who0 likes $what0')
print(s.substitute(who0='tim', what0='kung pao'))

#s = MyTemplate('$who likes $what')
#print(s.substitute(who='tim', what='kung pao'))#ValueError: Invalid placeholder in string: line 1, col 1
s = MyTemplate('$wh_o likes $wh_at')
print(s.substitute(wh_o='tim', wh_at='kung pao'))

d = dict(who='tim')
print(MyTemplate('$who likes $what').safe_substitute(d))
```
```sh
$ python 2.py 
tim likes kung pao
tim likes kung pao
$who likes $what
```

## 正規表現パターン全体を指定

> 他にも、クラス属性 pattern をオーバライドして、正規表現パターン全体を指定できます。オーバライドを行う場合、 pattern の値は 4 つの名前つきキャプチャグループ (capturing group) を持った正規表現オブジェクトでなければなりません。これらのキャプチャグループは、上で説明した規則と、無効なプレースホルダに対する規則に対応しています:

>    escaped – このグループはエスケープシーケンス、すなわちデフォルトパターンにおける $$ に対応します。

>    named – このグループは波括弧でくくらないプレースホルダ名に対応します; キャプチャグループに区切り文字を含めてはなりません。

>    braced – このグループは波括弧でくくったプレースホルダ名に対応します; キャプチャグループに区切り文字を含めてはなりません。

>    invalid – このグループはそのほかの区切り文字のパターン (通常は区切り文字一つ) に対応し、正規表現の末尾に出現しなければなりません。

