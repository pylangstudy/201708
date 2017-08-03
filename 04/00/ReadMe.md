# [4.8.4. printf 形式での bytes の書式化](https://docs.python.jp/3/library/stdtypes.html#printf-style-bytes-formatting)

< [4.8. バイナリシーケンス型 — bytes, bytearray, memoryview(原文)](https://docs.python.jp/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview) < [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## 注釈

> ここで述べる書式化演算には様々な癖があり、よく間違いの元になっています (タプルや辞書を正しく表示できないなど)。もし表示する値がタプルや辞書かもしれない場合、それをタプルに包むようにしてください。

str型なら[str.format()](https://docs.python.jp/3/library/stdtypes.html#str.format)推奨だったが、bytesにはないのか……。

## ソースコード

```python
print('%s' % b'abc')
print(b'%(language)s has %(number)03d quote types.' % {b'language': b"Python", b"number": 2})

print('%s' % 'abc')
#print('%c' % 'abc') #TypeError: %c requires int or char
#print('%c' % b'A') #TypeError: %c requires int or char
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
b'abc'
b'Python has 002 quote types.'
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

