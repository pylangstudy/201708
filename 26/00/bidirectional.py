import unicodedata
print(unicodedata.name('a'))
print(unicodedata.name('_'))

for code in range(0x2FFFF):
    try: print('{:5x} {} {}'.format(code, chr(code), unicodedata.bidirectional(chr(code))))
    except Exception as e: print('{:5x} {}'.format(code, e))
for code in range(0xE0000, (0xE0FFF+1)):
    try: print('{:5x} {} {}'.format(code, chr(code), unicodedata.bidirectional(chr(code))))
    except Exception as e: print('{:5x} {}'.format(code, e))
    
#chr()
#unichr()
#UnicodeEncodeError: 'utf-8' codec can't encode character '\ud800' in position 5: surrogates not allowed
#https://ja.wikipedia.org/wiki/Unicode%E4%B8%80%E8%A6%A7_D000-DFFF
