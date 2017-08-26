import unicodedata

#http://d.hatena.ne.jp/expectorate/20131230/1388433282
#https://gist.github.com/ikegami-yukino/8186853

def show(form, code):
    char = chr(code)
    normalized_char = unicodedata.normalize(form, char)
    if char != normalized_char:
        if len(normalized_char) == 1:
            print('{:5x} {} -> {:5x} {}'.format(code, char, ord(normalized_char), normalized_char))
        else:
            print('{:5x} {} -> {}'.format(code, char, normalized_char))

for form in ['NFC','NFKC','NFD','NFKD']:
    print('**********', form, '**********')
    for code in range(0x2FFFF+1): show(form, code)
    for code in range(0xE0000, 0xE0FFF+1): show(form, code)

