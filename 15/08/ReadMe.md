# [6.2.5.9. トークナイザを書く](https://docs.python.jp/3/library/re.html#writing-a-tokenizer)

< [6.2.5. 正規表現の例](https://docs.python.jp/3/library/re.html#regular-expression-examples) < [6.2. re — 正規表現操作](https://docs.python.jp/3/library/re.html#module-re) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## 文字列の解析

> トークナイザやスキャナ は文字列を解析し、文字のグループにカテゴリ分けします。これはコンパイラやインタプリタを作成する最初の一歩として役立ちます。

> テキストのカテゴリは正規表現で指定されます。技術的には、それらを一つのマスター正規表現に結合し、連続したマッチをループさせます:

```python
import collections
import re

Token = collections.namedtuple('Token', ['typ', 'value', 'line', 'column'])

def tokenize(code):
    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    token_specification = [
        ('NUMBER',  r'\d+(\.\d*)?'),  # Integer or decimal number
        ('ASSIGN',  r':='),           # Assignment operator
        ('END',     r';'),            # Statement terminator
        ('ID',      r'[A-Za-z]+'),    # Identifiers
        ('OP',      r'[+\-*/]'),      # Arithmetic operators
        ('NEWLINE', r'\n'),           # Line endings
        ('SKIP',    r'[ \t]+'),       # Skip over spaces and tabs
        ('MISMATCH',r'.'),            # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group(kind)
        if kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
        elif kind == 'SKIP':
            pass
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        else:
            if kind == 'ID' and value in keywords:
                kind = value
            column = mo.start() - line_start
            yield Token(kind, value, line_num, column)

statements = '''
    IF quantity THEN
        total := total + price * quantity;
        tax := price * 0.05;
    ENDIF;
'''

for token in tokenize(statements):
    print(token)
```

> トークナイザは以下の出力を作成します:

```
Token(typ='IF', value='IF', line=2, column=4)
Token(typ='ID', value='quantity', line=2, column=7)
Token(typ='THEN', value='THEN', line=2, column=16)
Token(typ='ID', value='total', line=3, column=8)
Token(typ='ASSIGN', value=':=', line=3, column=14)
Token(typ='ID', value='total', line=3, column=17)
Token(typ='OP', value='+', line=3, column=23)
Token(typ='ID', value='price', line=3, column=25)
Token(typ='OP', value='*', line=3, column=31)
Token(typ='ID', value='quantity', line=3, column=33)
Token(typ='END', value=';', line=3, column=41)
Token(typ='ID', value='tax', line=4, column=8)
Token(typ='ASSIGN', value=':=', line=4, column=12)
Token(typ='ID', value='price', line=4, column=15)
Token(typ='OP', value='*', line=4, column=21)
Token(typ='NUMBER', value='0.05', line=4, column=23)
Token(typ='END', value=';', line=4, column=27)
Token(typ='ENDIF', value='ENDIF', line=5, column=4)
Token(typ='END', value=';', line=5, column=9)
```

これはいい見本。正規表現の有用さが垣間見れる。

## 正規表現Webツール

* https://nelog.jp/regular-expression-online-tools
* http://qiita.com/AQRiL_1132/items/c185c7ad84c129e5a2df

URL|Python正規表現|URLシェア|入力の楽さ|見やすさ|応答速度|Pythonソースコード生成
---|--------------|---------|----------|--------|--------|----------------------
https://regex101.com/|○|○|○|○|✗|○
https://www.debuggex.com/|○|○|△|○|○|?
http://www.rexv.org/|○|✗|△|○|○|?
http://www.regexplanet.com/|○|○|✗|✗|?

