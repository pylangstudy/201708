# [6.3.1. SequenceMatcherオブジェクト](https://docs.python.jp/3/library/difflib.html#sequencematcher-objects)

< [6.3. difflib — 差分の計算を助ける](https://docs.python.jp/3/library/difflib.html#module-difflib) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## SequenceMatcherクラス

クラス|説明
------|----
class difflib.SequenceMatcher(isjunk=None, a='', b='', autojunk=True)|
set_seqs(a, b)|比較される2つの文字列を設定します。
set_seq1(a)|比較を行う1つ目のシーケンスを設定します。比較される2つ目のシーケンスは変更されません。
set_seq2(b)|比較を行う2つ目のシーケンスを設定します。比較される1つ目のシーケンスは変更されません。
find_longest_match(alo, ahi, blo, bhi)|a[alo:ahi] と b[blo:bhi] の中から、最長のマッチ列を探します。
get_matching_blocks()|マッチしたシーケンス中で個別にマッチしたシーケンスをあらわす、3つの値のリストを返します。
get_opcodes()|a を b にするための方法を記述する5つのタプルを返します。
get_grouped_opcodes(n=3)|最大 n 行までのコンテクストを含むグループを生成するような、ジェネレータ(generator)を返します。
ratio()|[0, 1] の範囲の浮動小数点数で、シーケンスの類似度を測る値を返します。
quick_ratio()|ratio() の上界を、より高速に計算します。
real_quick_ratio()|ratio() の上界を、非常に高速に計算します。

## 役立たずのisjunk

`difflib.SequenceMatcher(isjunk=None, a='', b='', autojunk=True)`の`isjunk`が何の役に立つのか不明。

Python文書には`isjunk`を`lambda x: x in " \t"`とすると「空白とタブ文字を無視して文字のシーケンスを比較します」とある。しかし、以下コードでは違いを確認できなかった。コード例もないため、どう使うのか不明。

```python
...
sm = difflib.SequenceMatcher(a='abc', b='a b	c'); print(sm, sm.ratio());
sm = difflib.SequenceMatcher(isjunk=lambda x: x in " \t", a='abc', b='a b	c'); print(sm, sm.ratio());
```
```sh
$ python SequenceMatcher.py 
...
<difflib.SequenceMatcher object at 0xb71600ac> 0.75
<difflib.SequenceMatcher object at 0xb71d3dac> 0.75
```

ググってみたところ、`ratio()`ではisjunkが考慮されていないらしいことが書いてあった。

> パフォーマンスの理由からシーケンスがisjunkによってフィルタリングされないと仮定します。

実行速度が遅くなるからisjunkは考慮しないと思われる、ということだろう。`ratio()`のほかに`quick_ratio()`, `real_quick_ratio()`という、さらに高速に行うらしい関数はある。それらは当然`isjunk`を考慮しないと思われる。つまり、</strong>isjunk()を考慮した数値は算出できない</strong>ということになる。事実上、isjunkは利用価値がないのでは？

Python文書には一言も書いていない……。Pythonは適当なライブラリが多い印象。

https://stackoverflow.com/questions/38129357/difflib-sequencematcher-isjunk-argument-not-considered

[Google翻訳](https://translate.googleusercontent.com/translate_c?act=url&depth=1&hl=ja&ie=UTF8&prev=_t&rurl=translate.google.co.jp&sl=en&sp=nmt4&tl=ja&u=https://stackoverflow.com/questions/38129357/difflib-sequencematcher-isjunk-argument-not-considered&usg=ALkJrhiGJGGkIxEGiUClPABLuH7eC1YY5w)

## get_grouped_opcodesの説明が嘘

> グループは get_opcodes() と同じ書式で返されます。

とあるが、コード例を同じようにしても動作しなかった。二重for文にすると動作した。よくわからない。

```python
import difflib
a = "qabxcd\nqabxcd\nqabxcd"
b = "abycdf\nabycdf\nabycdf"
print(f'a:{a}\nb:{b}')
s = difflib.SequenceMatcher(None, a, b)
print(list(s.get_grouped_opcodes(n=3)))
for l in s.get_grouped_opcodes(n=3):
    for tag, i1, i2, j1, j2 in l:
        print('{:7}   a[{}:{}] --> b[{}:{}] {!r:>8} --> {!r}'.format(tag, i1, i2, j1, j2, a[i1:i2], b[j1:j2]))
```

