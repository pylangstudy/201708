#!python3.6
import difflib

a='abc\ndef\nhij\n#無視できる行\n#abc\n   \n#\n#a\n# a'
b='abc\nd555ef\nhij\n#無視できちゃう行\n#abc\n   \n#\n#a\n# a'
a=a.splitlines()
b=b.splitlines()
print('========== ndiff format ==========')
for buf in difflib.ndiff(a,b):
    print(buf, 'IS_LINE_JUNK:', difflib.IS_LINE_JUNK(buf))
