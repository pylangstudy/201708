# [6.2.2. モジュールコンテンツ](https://docs.python.jp/3/library/re.html#regular-expression-syntax)

< [6.2. re — 正規表現操作](https://docs.python.jp/3/library/re.html#module-re) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

わからないことだらけ。正規表現だけでも難しいが、Pythonにおける正規表現はさらに難しい。メソッドやらフラグやらの把握と使い分けの必要性が生じるから。

## re

> このモジュールはいくつかの関数、定数、例外を定義します。この関数の一部はコンパイルした正規表現の完全版メソッドを簡略化したバージョンです。簡単なアプリケーションを除くほとんどで、コンパイルされた形式が用いられるのが普通です。

> バージョン 3.6 で変更: フラグ定数は、enum.IntFlag のサブクラスである RegexFlag のインスタンスになりました、

Pythonのライブラリは必要性が怪しい、中途半端、わかりにくい、などの関数が多い気がする。

## メソッド

メソッド|概要
--------|----
re.compile(pattern, flags=0)|正規表現パターンを正規表現オブジェクトにコンパイルします。
re.search(pattern, string, flags=0)|string を走査し、正規表現 pattern がマッチする最初の場所を探して、対応する match オブジェクト を返します。文字列内にパターンにマッチする場所が無い場合は None を返します;
re.match(pattern, string, flags=0)|もし string の先頭で 0 個以上の文字が正規表現 pattern とマッチすれば、対応する マッチオブジェクト インスタンスを返します。文字列がパターンとマッチしなければ、None を返します;
re.fullmatch(pattern, string, flags=0)|string 全体が正規表現 pattern にマッチした場合、対応する match オブジェクト を返します。文字列にパターンにマッチする場所が無い場合は None を返します;
re.split(pattern, string, maxsplit=0, flags=0)|string を、pattern があるたびに分割します。
re.findall(pattern, string, flags=0)|pattern の string へのマッチのうち、重複しない全てのマッチを文字列のリストとして返します。 string は左から右へと走査され、マッチは見つかった順番で返されます。パターン中に何らかのグループがある場合、グループのリストを返します。グループが複数定義されていた場合、タプルのリストになります。他のマッチの開始部分に接触しないかぎり、空のマッチも結果に含められます。
re.finditer(pattern, string, flags=0)|string 内の RE pattern の重複しないマッチの マッチオブジェクト を yield する イテレータ を返します。
re.sub(pattern, repl, string, count=0, flags=0)|string 内で、pattern のマッチを repl で置き換えた文字列を返します。バージョン 3.5 で非推奨、バージョン 3.7 で削除予定。
re.subn(pattern, repl, string, count=0, flags=0)|sub() と同じ操作を行いますが、タプル (new_string、 number_of_subs_made) を返します。
re.purge()|正規表現キャッシュをクリアします。
exception re.error(msg, pattern=None, pos=None)|これらの関数のいずれかに渡された文字列が有効な正規表現ではない (例: 括弧が対になっていない) 場合、またはコンパイル時やマッチング時になんらかのエラーが発生した場合に発生する例外です。

### RegexFlag

RegexFlag|概要
---------|----
re.ASCII|
re.DEBUG|デバッグ情報を出力します。
re.IGNORECASE|英大文字・小文字を区別せずにマッチングを行います。
re.LOCALE|<strong>非推奨</strong>
re.MULTILINE|対象文字列が複数行のとき、`^`と`$`は行頭と行末を表す（パターンは1行毎に実行される）
re.DOTALL| '.' を、改行を含む任意の文字と、とにかくマッチさせます；このフラグがなければ、 '.' は、改行 以外の 任意の文字とマッチします。（改行さえも``.の対象になる）
re.VERBOSE|パターン文字列内にコメントが書ける。スペースや改行などの空白文字で見やすくできる。

おそらく使うのは`IGNORECASE`,`MULTILINE`くらいだと思う。

### ERROR

exception re.error()の戻り値、エラーインスタンスには、次のような追加の属性があります。

属性|説明
----|----
msg|フォーマットされていないエラーメッセージです。
pattern|正規表現のパターンです。
pos|pattern のコンパイルに失敗した場所のインデックスです。
lineno|pos に対応する行です。
colno|pos に対応する列です。

## ソースコード

### search

```python
import re

#pattern = r'^ab'
pattern = r'ab'
pattern1 = re.compile(pattern)
for target in ['abc', 'ABCabc']: print(pattern1.search(target))
print()
for target in ['abc', 'ABCabc']: print(pattern1.search(target, re.IGNORECASE))#1つ目がNoneになる
print()
for target in ['abc', 'ABCabc']: print(re.search(pattern, target))
print()
for target in ['abc', 'ABCabc']: print(re.search(pattern, target, re.IGNORECASE))
```
```sh
$ python search.py 
<_sre.SRE_Match object; span=(0, 2), match='ab'>
<_sre.SRE_Match object; span=(3, 5), match='ab'>

None
<_sre.SRE_Match object; span=(3, 5), match='ab'>

<_sre.SRE_Match object; span=(0, 2), match='ab'>
<_sre.SRE_Match object; span=(3, 5), match='ab'>

<_sre.SRE_Match object; span=(0, 2), match='ab'>
<_sre.SRE_Match object; span=(0, 2), match='AB'>
```

re.search(...)とregex.search(...)の結果が異なる。re.searchのほうは期待通りである。

### match

```python
import re

#pattern = r'^ab'
pattern = r'ab'
pattern1 = re.compile(pattern)
for target in ['abc', 'ABCabc']: print(pattern1.match(target))
print()
for target in ['abc', 'ABCabc']: print(pattern1.match(target, re.IGNORECASE))#全部Noneになる
print()
for target in ['abc', 'ABCabc']: print(re.match(pattern, target))
print()
for target in ['abc', 'ABCabc']: print(re.match(pattern, target, re.IGNORECASE))
```
```sh
$ python match.py 
<_sre.SRE_Match object; span=(0, 2), match='ab'>
None

None
None

<_sre.SRE_Match object; span=(0, 2), match='ab'>
None

<_sre.SRE_Match object; span=(0, 2), match='ab'>
<_sre.SRE_Match object; span=(0, 2), match='AB'>
```

search同様、re.matchのほうは期待通り。regex.matchのほうはNoneになる。searchよりもNoneが増えた。

### split

```python
import re

#pattern = r'^ab'
pattern = r'ab'
pattern1 = re.compile(pattern)
for target in ['abc', 'ABCabc']: print(pattern1.split(target))
print()
for target in ['abc', 'ABCabc']: print(pattern1.split(target, re.IGNORECASE))#全部Noneになる
print()
for target in ['abc', 'ABCabc']: print(re.split(pattern, target))
print()
for target in ['abc', 'ABCabc']: print(re.split(pattern, target, re.IGNORECASE))
print()
print(re.split('\W+', 'Words, words, words.'))
print(re.split('(\W+)', 'Words, words, words.'))
print(re.split('\W+', 'Words, words, words.', 1))
print(re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE))
print()
print(re.split('x*', 'axbc'))#FutureWarning: split() requires a non-empty pattern match.
print()
print(re.split("^$", "foo\n\nbar\n", flags=re.M))#ValueError: split() requires a non-empty pattern match.
```
```sh
$ python split.py 
['', 'c']
['ABC', 'c']

['', 'c']
['ABC', 'c']

['', 'c']
['ABC', 'c']

['', 'c']
['ABC', 'c']

['Words', 'words', 'words', '']
['Words', ', ', 'words', ', ', 'words', '.', '']
['Words', 'words, words.']
['0', '3', '9']

/home/mint/.pyenv/versions/3.6.1/lib/python3.6/re.py:212: FutureWarning: split() requires a non-empty pattern match.
  return _compile(pattern, flags).split(string, maxsplit)
['a', 'bc']

Traceback (most recent call last):
  File "split.py", line 21, in <module>
    print(re.split("^$", "foo\n\nbar\n", flags=re.M))
  File "/home/mint/.pyenv/versions/3.6.1/lib/python3.6/re.py", line 212, in split
    return _compile(pattern, flags).split(string, maxsplit)
ValueError: split() requires a non-empty pattern match.
```

挙動がつかめない。

* r`ab`というパターンのとき
    * `ab`が消え、その前後の文字をリストで返している？
* `re.IGNORECASE`にしても結果が変わらないのはなぜ？
    * r`ab`, `re.IGNORECASE`, 対象文字列'ABCabc'のとき、`['','C','c']`になるのではないのか？(`ab`,`AB`が消えるべきでは？)

#### 注釈

Python文書の説明はもっと意味不明。

`re.split('x*', 'axbc')`は現状`['a', 'bc']`を返す。これはFutureWarningであり、正しい答えは`['', 'a', 'b', 'c', '']`らしい。将来のバージョンで実装されるとか。どうしてそれが正しいのかわからない。

> 'x*' は ‘a’ の前、 ‘b’ と ‘c’ との間、 ‘c’ の後の 0 個の ‘x’ にもマッチします

という説明が意味不明。xは1箇所にしか無いのだから、aの後ろにある`x`1箇所だけにマッチすると思うのだが？`['a', 'bc']`が正しいのではないのか？

### findall

```python
import re

#pattern = r'^ab'
pattern = r'ab'
pattern1 = re.compile(pattern)
for target in ['abc', 'ABCabc']: print(pattern1.findall(target))
print()
for target in ['abc', 'ABCabc']: print(pattern1.findall(target, re.IGNORECASE))#1つ目がNoneになる
print()
for target in ['abc', 'ABCabc']: print(re.findall(pattern, target))
print()
for target in ['abc', 'ABCabc']: print(re.findall(pattern, target, re.IGNORECASE))
```
```sh
$ python findall.py 
['ab']
['ab']

[]
['ab']

['ab']
['ab']

['ab']
['AB', 'ab']
```

splitと違ってわかりやすい。一致した文字列をリストで返す。これは使いそう。

### finditer

```python
import re

pattern = r'ab'
pattern1 = re.compile(pattern)
for target in ['abc', 'ABCabc']: print(pattern1.finditer(target))
print([f for target in ['abc', 'ABCabc'] for f in pattern1.finditer(target)])
print()
for target in ['abc', 'ABCabc']: print(pattern1.finditer(target, re.IGNORECASE))#1つ目がNoneになる
print([f for target in ['abc', 'ABCabc'] for f in pattern1.finditer(target, re.IGNORECASE)])
print()
for target in ['abc', 'ABCabc']: print(re.finditer(pattern, target))
print([f for target in ['abc', 'ABCabc'] for f in re.finditer(pattern1, target)])
print()
for target in ['abc', 'ABCabc']: print(re.finditer(pattern, target, re.IGNORECASE))
#print([f for target in ['abc', 'ABCabc'] for f in re.finditer(pattern1, target, re.IGNORECASE)])#ValueError: cannot process flags argument with a compiled pattern
```
```sh
$ python finditer.py 
<callable_iterator object at 0xb711e24c>
<callable_iterator object at 0xb711e24c>
[<_sre.SRE_Match object; span=(0, 2), match='ab'>, <_sre.SRE_Match object; span=(3, 5), match='ab'>]

<callable_iterator object at 0xb711e24c>
<callable_iterator object at 0xb711e24c>
[<_sre.SRE_Match object; span=(3, 5), match='ab'>]

<callable_iterator object at 0xb711e24c>
<callable_iterator object at 0xb711e24c>
[<_sre.SRE_Match object; span=(0, 2), match='ab'>, <_sre.SRE_Match object; span=(3, 5), match='ab'>]

<callable_iterator object at 0xb711e28c>
<callable_iterator object at 0xb711e28c>
```

`re.finditer`の第三引数(flag)に`re.IGNORECASE`を指定すると`ValueError`になった。謎。findallのほうが使いやすそう。

### sub

```python
import re

#pattern = r'^ab'
pattern = r'ab'
pattern1 = re.compile(pattern)
for target in ['abc', 'ABCabc']: print(pattern1.sub('あい', target))
print()
for target in ['abc', 'ABCabc']: print(pattern1.sub('あい', target, re.IGNORECASE))
print()
for target in ['abc', 'ABCabc']: print(re.sub(pattern, 'あい', target))
print()
for target in ['abc', 'ABCabc']: print(re.sub(pattern, 'あい', target, re.IGNORECASE))
print()

#compile側でIGNORECASEを指定せねば検索するときに有効にならないらしい
#re.sub(,,re.IGNORECASE)で指定しても変わらない。変更不可なら紛らわしので各メソッドのflag引数を消して欲しい。
pattern = r'ab'
pattern1 = re.compile(pattern, re.IGNORECASE)
for target in ['abc', 'ABCabc']: print(pattern1.sub('あい', target))
print()

#compile側でIGNORECASEを指定せねば検索するときに有効にならないらしい
pattern = r'ab'
pattern1 = re.compile(pattern, re.IGNORECASE)
for target in ['abc', 'ABCabc']: print(pattern1.sub('xy', target, re.DEBUG))#メソッド側のflag(re.DEBUG)は無効
print()
```
```sh
$ python sub.py 
あいc
ABCあいc

あいc
ABCあいc

あいc
ABCあいc

あいc
ABCあいc
```

やっと気づいたが、sub()などの各種メソッドの引数`flag`にRegexFlagを指定しても有効にならない。何のためのflagなの？



> バージョン 3.6 で変更: pattern 中に``’‘``とASCII文字からなる未知のエスケープがあると、エラーになります。

> バージョン 3.5 で非推奨、バージョン 3.7 で削除予定。

というのが意味不明。3.7からはsub()メソッドが使えなくなるの？なぜ3.6で変更した？代替としてはsubn()メソッドを使うべき？

### subn

```python
import re

pattern = r'ab'
pattern1 = re.compile(pattern)
for target in ['abc', 'ABCabc']: print(pattern1.subn('あい', target))
print()
for target in ['abc', 'ABCabc']: print(pattern1.subn('あい', target, re.IGNORECASE))
print()
for target in ['abc', 'ABCabc']: print(re.subn(pattern, 'あい', target))
print()
for target in ['abc', 'ABCabc']: print(re.subn(pattern, 'あい', target, re.IGNORECASE))
print()

pattern = r'ab'
pattern1 = re.compile(pattern, re.IGNORECASE)
for target in ['abc', 'ABCabc']: print(pattern1.subn('あい', target))
print()

pattern = r'ab'
pattern1 = re.compile(pattern, re.IGNORECASE)
for target in ['abc', 'ABCabc']: print(pattern1.subn('xy', target, re.DEBUG))#メソッド側のflag(re.DEBUG)は無効
print()
```
```sh
$ python subn.py 
('あいc', 1)
('ABCあいc', 1)

('あいc', 1)
('ABCあいc', 1)

('あいc', 1)
('ABCあいc', 1)

('あいc', 1)
('ABCあいc', 1)

('あいc', 1)
('あいCあいc', 2)

('xyc', 1)
('xyCxyc', 2)
```

subメソッドと違い、削除予定はないらしい。どういうこと？

### escape

```python
#!python3.6
#coding:utf-8
import re
import string

print(re.escape('python.exe'))

legal_chars = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`|~:"
print('[%s]+' % re.escape(legal_chars))

operators = ['+', '-', '*', '/', '**']
print('|'.join(map(re.escape, sorted(operators, reverse=True))))

print(re.escape('あいうえお'))
```
```sh
$ python escape.py 
python\.exe
[abcdefghijklmnopqrstuvwxyz0123456789\!\#\$\%\&\'\*\+\-\.\^_\`\|\~\:]+
\/|\-|\+|\*\*|\*
\あ\い\う\え\お
```

Google翻訳した。

> ASCII文字、数字、 '_'以外のすべての文字をエスケープします。これは、正規表現のメタ文字が含まれている可能性がある任意のリテラル文字列と一致させる場合に便利です。例えば：

日本語が含まれると`\`を付与されてしまっている。エスケープ文字として意味ある文字だけを対象にしてくれるわけではない。そもそもエスケープ文字は文脈によって変わる。一体どこが便利なのかわからない。

「エスケープする」という表現が紛らわしい。「先頭に`\`文字を付与する」と読み替えると正確に理解できる。

### purge

```python
#!python3.6
#coding:utf-8
import re

pattern = r'ab'
pattern1 = re.compile(pattern)
for target in ['abc', 'ABCabc']: print(pattern1.search(target))
print()
for target in ['abc', 'ABCabc']: print(pattern1.search(target, re.IGNORECASE))#1つ目がNoneになる
print()
for target in ['abc', 'ABCabc']: print(re.search(pattern, target))
print()
for target in ['abc', 'ABCabc']: print(re.search(pattern, target, re.IGNORECASE))
print()
re.purge()
```
```sh
$ python purge.py 
<_sre.SRE_Match object; span=(0, 2), match='ab'>
<_sre.SRE_Match object; span=(3, 5), match='ab'>

None
<_sre.SRE_Match object; span=(3, 5), match='ab'>

<_sre.SRE_Match object; span=(0, 2), match='ab'>
<_sre.SRE_Match object; span=(3, 5), match='ab'>

<_sre.SRE_Match object; span=(0, 2), match='ab'>
<_sre.SRE_Match object; span=(0, 2), match='AB'>
```

> 正規表現キャッシュをクリアします。

繰り返し処理をするとき、適当なタイミングで呼び出したほうが良いのだろうか？キャッシュの確認ができないので効果があるかどうかもわからない。

### error

```python
#!python3.6
#coding:utf-8
import re

try:
    pattern = r'(ab'
    pattern1 = re.compile(pattern)
except Exception as e:
    print('msg:', e.msg)
    print('pattern:', e.pattern)
    print('pos:', e.pos)
    print('lineno:', e.lineno)
    print('colno:', e.colno)
finally: re.purge()
```
```sh
$ python error.py 
msg: missing ), unterminated subpattern
pattern: (ab
pos: 0
lineno: 1
colno: 1
```

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

