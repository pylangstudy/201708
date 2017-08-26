#!python3.6
#coding:utf-8
import stringprep
import unicodedata

print(unicodedata.unidata_version)

#UnicodeEncodeError: 'utf-8' codec can't encode character '\ud800' in position 6: surrogates not allowed
for code in range(0x2FFFF+1):
#    if stringprep.in_table_a1(chr(code)) or stringprep.in_table_b1(chr(code)) or stringprep.in_table_c4(chr(code)) or stringprep.in_table_c5(chr(code)) or stringprep.in_table_c8(chr(code)): continue
    if stringprep.in_table_a1(chr(code)) or stringprep.in_table_b1(chr(code)) or stringprep.in_table_c4(chr(code)) or stringprep.in_table_c8(chr(code)): continue
    if stringprep.in_table_c5(chr(code)): print('{:5x} {} {}'.format(code, chr(code), stringprep.in_table_c5(chr(code))))

"""
for code in range(0xE0000, (0xE0FFF+1)):
    if stringprep.in_table_a1(chr(code)) or stringprep.in_table_b1(chr(code)) or stringprep.in_table_c4(chr(code)) or stringprep.in_table_c5(chr(code)) or stringprep.in_table_c8(chr(code)): continue
    print('{:5x} {} {}'.format(code, chr(code), stringprep.in_table_c4(chr(code))))
"""
