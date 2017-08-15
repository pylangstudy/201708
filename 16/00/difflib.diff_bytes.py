#!python3.6
#str型でなくbyte型で処理できる。バイナリデータを対象にできる。
import difflib

a='abc\ndef\nhij'
b='abc\nd555ef\nhij'
#str配列に変換
a=a.splitlines()
b=b.splitlines()
#byte配列に変換
a = [t.encode() for t in a]
b = [t.encode() for t in b]
print('========== unified_diff format ==========')
for buf in difflib.diff_bytes(difflib.unified_diff, a, b):
    print(buf)
