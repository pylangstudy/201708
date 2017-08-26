#!python3.6
#coding:utf-8
import stringprep
import unicodedata

print(unicodedata.unidata_version)

for code in range(0x2FFFF+1):
    if stringprep.in_table_a1(chr(code)) or stringprep.in_table_b1(chr(code)) or stringprep.in_table_c4(chr(code)) or stringprep.in_table_c5(chr(code)) or stringprep.in_table_c8(chr(code)): continue
    print('{:5x} {} {}'.format(code, chr(code), stringprep.in_table_a1(chr(code))))
for code in range(0xE0000, (0xE0FFF+1)):
    if stringprep.in_table_a1(chr(code)) or stringprep.in_table_b1(chr(code)) or stringprep.in_table_c4(chr(code)) or stringprep.in_table_c5(chr(code)) or stringprep.in_table_c8(chr(code)): continue
    print('{:5x} {} {}'.format(code, chr(code), stringprep.in_table_a1(chr(code))))

"""
def get_th():
    titles = ['codepoint', 'char', 'name', 'category', 'east_asian_width']
    th = '|'.join(titles) + '\n'
    for t in titles: th += '-' * len(t) + '|'
    th = th[:-1]; th += '\n'
    return th
def get_td(code):
    try: return '{:5x}|{}|{}|{}|{}\n'.format(code, chr(code), unicodedata.name(chr(code), None), unicodedata.category(chr(code)), unicodedata.east_asian_width(chr(code)))
    except Exception as e: print('{:5x} {}'.format(code, e)); return None

def get_td(f):
    for code in range(0x2FFFF+1):
        try: f.write('{:5x}|{}|{}|{}|{}\n'.format(code, chr(code), unicodedata.name(chr(code), None), unicodedata.category(chr(code)), unicodedata.east_asian_width(chr(code))))
        except Exception as e: print('{:5x} {}'.format(code, e))
    for code in range(0xE0000, (0xE0FFF+1)):
        try: f.write('{:5x}|{}|{}|{}|{}\n'.format(code, chr(code), unicodedata.name(chr(code), None), unicodedata.category(chr(code)), unicodedata.east_asian_width(chr(code))))
        except Exception as e: print('{:5x} {}'.format(code, e))

with open(f'unicode_{unicodedata.unidata_version}.tsv', mode='w', encoding='utf-8') as f:
    f.write(get_th())
    get_td(f)
"""

