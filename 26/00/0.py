#!python3.6
#coding:utf-8
import unicodedata

print(unicodedata.unidata_version)

"""
titles = ['codepoint', 'char', 'name', 'category', 'east_asian_width']
th = '|'.join(titles) + '\n'
for t in titles: th += '-' * len(t) + '|'
th = th[:-1]; th += '\n'

for code in range(0x2FFFF+1):
    try: print('{:5x} {} {} {}'.format(code, chr(code), unicodedata.name(chr(code), None), unicodedata.category(chr(code)), unicodedata.east_asian_width(chr(code)))
    except Exception as e: print('{:5x} {}'.format(code, e))
for code in range(0xE0000, (0xE0FFF+1)):
    try: print('{:5x} {} {} {}'.format(code, chr(code), unicodedata.name(chr(code), None), unicodedata.category(chr(code))))
    except Exception as e: print('{:5x} {}'.format(code, e))
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

"""
def get_td():
    for code in range(0x2FFFF+1):
        try: yield '{:5x}|{}|{}|{}|{}\n'.format(code, chr(code), unicodedata.name(chr(code), None), unicodedata.category(chr(code)), unicodedata.east_asian_width(chr(code)))
        except Exception as e: print('{:5x} {}'.format(code, e))
    for code in range(0xE0000, (0xE0FFF+1)):
        try: yield '{:5x}|{}|{}|{}|{}\n'.format(code, chr(code), unicodedata.name(chr(code), None), unicodedata.category(chr(code)), unicodedata.east_asian_width(chr(code)))
        except Exception as e: print('{:5x} {}'.format(code, e))
"""
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
#    for code in range(0x2FFFF+1): f.write(get_td(code))
#    for code in range(0xE0000, (0xE0FFF+1)): f.write(get_td(code))
#    try:
#        for td in get_td(): f.write(td)
#    except: print('ERROR')
#    for td in get_td(): f.write(td)
#    f.write('abc\ndef')
    
#chr()
#unichr()
#UnicodeEncodeError: 'utf-8' codec can't encode character '\ud800' in position 5: surrogates not allowed
#https://ja.wikipedia.org/wiki/Unicode%E4%B8%80%E8%A6%A7_D000-DFFF
