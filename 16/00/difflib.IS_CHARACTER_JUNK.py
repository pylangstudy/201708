#!python3.6
import difflib

a='abc\n \n	\n#日本語'
b='abc\n \n	\n#日本人'
a=a.splitlines()
b=b.splitlines()
print('========== ndiff format ==========')
for buf in difflib.ndiff(a,b):
    print(buf, 'IS_CHARACTER_JUNK(buf[0]):', difflib.IS_CHARACTER_JUNK(buf[0]))
