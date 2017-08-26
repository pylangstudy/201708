#!python3.6
#coding:utf-8
import stringprep
import unicodedata

print(unicodedata.unidata_version)

#code がテーブル C.1.1 (ASCII スペース文字) かどうか判定します。
print(stringprep.in_table_c11(' '))
print(stringprep.in_table_c11('　'))
print(stringprep.in_table_c11('\t'))
print(stringprep.in_table_c11('-'))
print(stringprep.in_table_c11('a'))
print(stringprep.in_table_c11('あ'))
"""
for code in range(0x2FFFF+1):
    if stringprep.in_table_a1(chr(code)) or stringprep.in_table_b1(chr(code)) or stringprep.in_table_c4(chr(code)) or stringprep.in_table_c5(chr(code)) or stringprep.in_table_c8(chr(code)): continue
    print('{:5x} {} {}'.format(code, chr(code), stringprep.in_table_c11(chr(code))))
for code in range(0xE0000, (0xE0FFF+1)):
    if stringprep.in_table_a1(chr(code)) or stringprep.in_table_b1(chr(code)) or stringprep.in_table_c4(chr(code)) or stringprep.in_table_c5(chr(code)) or stringprep.in_table_c8(chr(code)): continue
    print('{:5x} {} {}'.format(code, chr(code), stringprep.in_table_c11(chr(code))))
"""
