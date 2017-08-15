#!python3.6
#いわゆるdiff。データの差分を見つける。
#http://mitsukuni.org/blog/2009/04/24/python-difflib%E3%81%8C%E4%BE%BF%E5%88%A9%E3%81%99%E3%81%8E%E3%82%8B%E4%BB%B6/
import difflib

a='abc\ndef\nhij'
b='abc\nd555ef\nhij'

# 食わせる文字はlistじゃないとダメ
a=a.splitlines()
b=b.splitlines()

print('========== context_diff format ==========')
for buf in difflib.context_diff(a, b):
    print(buf)

#print('\n\n')
print('========== unified_diff format ==========')
for buf in difflib.unified_diff(a,b):
    print(buf)

#print('\n\n')
print('========== ndiff format ==========')
for buf in difflib.ndiff(a,b):
    print(buf)

#print('\n\n')
print('========== difflib.Differ().compare() ==========')
#http://ja.pymotw.com/2/difflib/
d = difflib.Differ()
diff = d.compare(a, b)
print('\n'.join(diff))
