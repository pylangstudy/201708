#!python3.6
#coding:utf-8
import stringprep
import unicodedata

print(unicodedata.unidata_version)

#code がテーブル C.2.1 (ASCII 制御文字) かどうか判定します。
print(stringprep.in_table_c21(' '))
print(stringprep.in_table_c21('　'))
print(stringprep.in_table_c21('\t'))
print(stringprep.in_table_c21('-'))
print(stringprep.in_table_c21('a'))
print(stringprep.in_table_c21('あ'))
"""
for code in range(0x2FFFF+1):
    if stringprep.in_table_a1(chr(code)) or stringprep.in_table_b1(chr(code)) or stringprep.in_table_c4(chr(code)) or stringprep.in_table_c5(chr(code)) or stringprep.in_table_c8(chr(code)): continue
    print('{:5x} {} {}'.format(code, chr(code), stringprep.in_table_c21(chr(code))))
for code in range(0xE0000, (0xE0FFF+1)):
    if stringprep.in_table_a1(chr(code)) or stringprep.in_table_b1(chr(code)) or stringprep.in_table_c4(chr(code)) or stringprep.in_table_c5(chr(code)) or stringprep.in_table_c8(chr(code)): continue
    print('{:5x} {} {}'.format(code, chr(code), stringprep.in_table_c21(chr(code))))
"""