# [6.1.2. カスタムの文字列書式化](https://docs.python.jp/3/library/string.html#custom-string-formatting)

< [6.1. string — 一般的な文字列操作](https://docs.python.jp/3/library/string.html#module-string) < [6. テキスト処理サービス](https://docs.python.jp/3/library/text.html#text-processing-services) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## 説明

> 組み込みの文字列 (string) クラスには、 PEP 3101 で記述されている format() メソッドによって複雑な変数置換と値のフォーマットを行う機能があります。 string モジュールの Formatter クラスでは、組み込みの format() メソッドと同じ実装を使用して、独自の文字列フォーマットの振る舞いを作成してカスタマイズすることができます。

* [PEP 3101](https://www.python.org/dev/peps/pep-3101)
* [str.format()](https://docs.python.jp/3/library/stdtypes.html#str.format)
* [string](https://docs.python.jp/3/library/string.html#module-string).[Formatter](https://docs.python.jp/3/library/string.html#string.Formatter)

おそらくFormatterはユーザ定義型に対してユーザ定義型用フォーマット書式子を定義する仕組みなのだろう。大抵はユーザ定義型.str()メソッドまたはプロパティ参照で十分だと思う。日付型のように複雑な書式パターンがある場合はFormatterの実装が有効か。

## 一覧

名前|説明
----|----
class string.Formatter|Formatter クラスは、以下のメソッドを持ちます:
format(format_string, *args, **kwargs)|主要な API メソッドです。書式文字列と、任意の位置引数およびキーワード引数のセットを取ります。これは、vformat() を呼び出す単なるラッパーです。バージョン 3.5 で撤廃: キーワード引数 format_string としてフォーマット文字列を渡すことは非推奨となりました。
vformat(format_string, args, kwargs)|この関数はフォーマットの実際の仕事をします。この関数は、 *args および **kwargs シンタックスを使用して、辞書を個々の引数として unpack してから再度 pack するのではなく、引数としてあらかじめ用意した辞書を渡したい場合のために、独立した関数として公開されます。 vformat() は、書式文字列を文字データと置換フィールドに分解する仕事をします。それは、以下に記述する様々なメソッドを呼び出します。さらに、 Formatter ではサブクラスによって置き換えられることを意図した次のようないくつかのメソッドが定義されています。
parse(format_string)|format_stringを探査し、タプル、 (literal_text, field_name, format_spec, conversion) のイテラブルを返します。これは vformat() が文字列を文字としての文字データや置換フィールドに展開するために使用されます。
get_field(field_name, args, kwargs)|引数として与えた parse() (上記参照) により返される field_name を書式指定対象オブジェクトに変換します。返り値はタプル、 (obj, used_key) です。
get_value(key, args, kwargs)|与えられたフィールドの値を取り出します。
check_unused_args(used_args, args, kwargs)|希望に応じて未使用の引数がないか確認する機能を実装します。
format_field(value, format_spec)|format_field() は単純に組み込みのグローバル関数 format() を呼び出します。このメソッドは、サブクラスをオーバーライドするために提供されます。
convert_field(value, conversion)|(get_field() が返す) 値を (parse() メソッドが返すタプルの形式で) 与えられた変換タイプとして変換します。デフォルトバージョンは ‘s’ (str), ‘r’ (repr), ‘a’ (ascii) 変換タイプを理解します。

## ソースコード

```python
import string
import datetime
class MyFormatter(string.Formatter):
    def format(self, format_string, *args, **kwargs):
        print('format()', 'format_string:', format_string, '*args', *args, '**kwargs', **kwargs)
        return super().format(format_string, *args, **kwargs)
    def vformat(self, format_string, args, kwargs):
        print('vformat()', 'format_string:', format_string, 'args', args, 'kwargs', kwargs)
        return super().vformat(format_string, args, kwargs)
    def parse(self, format_string):
        print('parse()', 'format_string:', format_string)
        return super().parse(format_string)
    def get_field(self, field_name, args, kwargs):
        print('get_field()', 'format_string:', field_name, 'args:', args, 'kwargs:', kwargs)
        return super().get_field(field_name, args, kwargs)
    def get_value(self, key, args, kwargs):
        print('get_value()', 'key:', key, 'args:', args, 'kwargs:', kwargs)
        return super().get_value(key, args, kwargs)
    def check_unused_args(self, used_args, args, kwargs):
        print('check_unused_args()', 'used_args:', used_args, 'args:', args, 'kwargs:', kwargs)
        return super().check_unused_args(used_args, args, kwargs)
    def format_field(self, value, format_spec):
        print('format_field()', 'value:', value, 'format_spec:', format_spec)
        return super().format_field(value, format_spec)
    def convert_field(self, value, conversion):
        print('convert_field()', 'value:', value, 'conversion:', conversion)
        return super().convert_field(value, conversion)
        
f = MyFormatter()
#print(f.format('現在日時は{0:%Y-%m-%d %H:%M:%S.%f}です。', datetime.datetime.now()))
print(f.format('name={} age={}', 'Yamada', 99))
#print(f.format('name={name} age={age}', name='Yamada', age=99))#TypeError: 'name' is an invalid keyword argument for this function
print()
#print(f.format('name={name} age={age}', {'name':'Yamada', 'age':99}))#KeyError: 'name'
```
```sh
$ python 2.py 
format() format_string: name={} age={} *args Yamada 99 **kwargs
vformat() format_string: name={} age={} args ['Yamada', 99] kwargs {}
parse() format_string: name={} age={}
get_field() format_string: 0 args: ['Yamada', 99] kwargs: {}
get_value() key: 0 args: ['Yamada', 99] kwargs: {}
convert_field() value: Yamada conversion: None
parse() format_string: 
format_field() value: Yamada format_spec: 
get_field() format_string: 1 args: ['Yamada', 99] kwargs: {}
get_value() key: 1 args: ['Yamada', 99] kwargs: {}
convert_field() value: 99 conversion: None
parse() format_string: 
format_field() value: 99 format_spec: 
check_unused_args() used_args: {0, 1} args: ['Yamada', 99] kwargs: {}
name=Yamada age=99
```
