import difflib

a='abc\ndef\nhij'
b='abc\nd555ef\nhij'
a=a.splitlines()
b=b.splitlines()

print('========== context_diff format ==========')
for buf in difflib.context_diff(a, b):
    print(buf)

