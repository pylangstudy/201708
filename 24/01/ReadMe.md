# [6.3.2. SequenceMatcher の例](https://docs.python.jp/3/library/difflib.html#sequencematcher-examples)

< [6.3. difflib — 差分の計算を助ける](https://docs.python.jp/3/library/difflib.html#module-difflib) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## ヒントになりそうな説明抜き出し

> 空白を “junk” とします:

junkは一致判定しない文字のことだと思われる。しかし前回の調査により、ratio()に反映されないことが判明している。

https://github.com/pylangstudy/201708/tree/master/24/00#%E5%BD%B9%E7%AB%8B%E3%81%9F%E3%81%9A%E3%81%AEisjunk

> 経験によると、 ratio() の値が0.6を超えると、シーケンスがよく似ていることを示します:

> シーケンスのどこがマッチしているかにだけ興味のある時には get_matching_blocks() が手軽でしょう:
