# [6.3.3. Differ オブジェクト](https://docs.python.jp/3/library/difflib.html#differ-objects)

< [6.3. difflib — 差分の計算を助ける](https://docs.python.jp/3/library/difflib.html#module-difflib) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## Differ差分

> Differ オブジェクトによって生成された差分が 最小 であるなどとは言いません。むしろ、最小の差分はしばしば直観に反しています。その理由は、どこでもできるとなれば一致を見いだしてしまうからで、ときには思いがけなく100ページも離れたマッチになってしまうのです。一致点を互いに隣接したマッチに制限することで、場合によって長めの差分を出力するというコストを掛けることにはなっても、ある種の局所性を保つことができるのです。

Differオブジェクトの説明なのか？わかりづらい。おそらく、Differによる差分チェックは比較テキストの位置が少しズレただけで不一致となり「差分あり」と判定してしまうから変化箇所が膨大になりやすいと言っているのだろう。

## junkが反映されない

```python
#!python3.6
import difflib
d = difflib.Differ(); print(d)
print(d.compare('abc', 'abcd'))
for diff in d.compare('abc', 'abcd'): print(diff)

print('-----linejunk')
d = difflib.Differ(linejunk=lambda s: ' ' in s)
for diff in d.compare('a bc', 'abc'): print(diff)

print('-----charjunk')
d = difflib.Differ(charjunk=lambda c: ' ' == c)
for diff in d.compare('a bc', 'abc'): print(diff)
```
```sh
 $ python compare.py 
<difflib.Differ object at 0xb716ae2c>
<generator object Differ.compare at 0xb70f817c>
  a
  b
  c
+ d
-----linejunk
  a
-  
  b
  c
-----charjunk
  a
-  
  b
  c
```
差分として表示されてしまっている。

junkの説明すらないので、もしかしたら比較対象から外すという意味ではないのか？意味不明。

`difflib.context_diff()`などdifflibモジュール関数を使えば差分チェックできるのでは？Differクラスを使う理由やメリットが不明。
