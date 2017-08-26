#!python3.6
#coding:utf-8
import stringprep
import unicodedata

print(unicodedata.unidata_version)

for code in range(0x2FFFF+1):
    if stringprep.in_table_a1(chr(code)) or stringprep.in_table_b1(chr(code)) or stringprep.in_table_c4(chr(code)) or stringprep.in_table_c5(chr(code)) or stringprep.in_table_c8(chr(code)): continue
    print('{:5x} {} {}'.format(code, chr(code), stringprep.map_table_b3(chr(code))))
for code in range(0xE0000, (0xE0FFF+1)):
    if stringprep.in_table_a1(chr(code)) or stringprep.in_table_b1(chr(code)) or stringprep.in_table_c4(chr(code)) or stringprep.in_table_c5(chr(code)) or stringprep.in_table_c8(chr(code)): continue
    print('{:5x} {} {}'.format(code, chr(code), stringprep.map_table_b3(chr(code))))

