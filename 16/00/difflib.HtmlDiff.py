#!python3.6
#http://ja.pymotw.com/2/difflib/
import difflib

a='abc\ndef\nhij\n日本語UTF-8'
b='abc\nd555ef\nhij\n日本人UTF-8'

# 食わせる文字はlistじゃないとダメ
a=a.splitlines()
b=b.splitlines()

d = difflib.HtmlDiff()
print(d.make_table(a, b))
print('\n\n')
print(d.make_file(a, b))
with open('difflib.HtmlDiff.make_file.html', 'w') as f: f.write(d.make_file(a, b))
