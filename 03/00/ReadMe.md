# [4.7.2. printf 形式の文字列書式化](https://docs.python.jp/3/library/stdtypes.html#printf-style-string-formatting)

< [4.7. テキストシーケンス型 — str](https://docs.python.jp/3/library/stdtypes.html#text-sequence-type-str) < [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## 注釈

> ここで述べる書式化演算には様々な癖があり、よく間違いの元になっています (タプルや辞書を正しく表示できないなど)。新しい フォーマット文字列リテラル や str.format() インタフェースの方が間違いにくく、より強力で、柔軟で、さらに拡張可能です。 

* [str.format()](https://docs.python.jp/3/library/stdtypes.html#str.format)

この項は流し気味でいいか。

## ソースコード

```python
print('%s' % 'abc')
#print('%c' % 'abc') #TypeError: %c requires int or char
print('%c' % 'A')
print('%d' % 15)
print('%i' % 15)
print('%x' % 15)
print('%o' % 15)
print('%e' % 1000)
print('%E' % 1000)
print('%g' % 1.23)
print('%G' % 1.23)
print('%r' % 15) # repr()
print('%s' % 15) # str()
print('%a' % 15) # ascii()
```
```sh
$ python 0.py 
abc
A
15
15
f
17
1.000000e+03
1.000000E+03
1.23
1.23
15
15
15
```

