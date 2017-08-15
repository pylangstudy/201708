#!python3.6
import difflib

a='abc\ndef\nhij'
b='abc\nd555ef\nhij'
a=a.splitlines()
b=b.splitlines()
print('========== ndiff format ==========')
for buf in difflib.ndiff(a,b):
    print(buf)
