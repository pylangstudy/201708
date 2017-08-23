#!python3.6
import difflib
a = "qabxcd\nqabxcd\nqabxcd"
b = "abycdf\nabycdf\nabycdf"
print(f'a:{a}\nb:{b}')
s = difflib.SequenceMatcher(None, a, b)
print(list(s.get_grouped_opcodes(n=3)))
for l in s.get_grouped_opcodes(n=3):
    for tag, i1, i2, j1, j2 in l:
        print('{:7}   a[{}:{}] --> b[{}:{}] {!r:>8} --> {!r}'.format(tag, i1, i2, j1, j2, a[i1:i2], b[j1:j2]))

#https://docs.python.jp/3/library/difflib.html#difflib.SequenceMatcher.get_grouped_opcodes
#> グループは get_opcodes() と同じ書式で返されます。
#とあるが、get_opcodes()のコード例と同様にしてもエラーになった。
#ValueError: too many values to unpack (expected 5)

