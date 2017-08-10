#!python3.6
import string
print(string.capwords('  abc def ghi  '))
print(string.capwords('  abc,def,ghi  ', ','))
print(string.capwords('abc,def,ghi', ','))
