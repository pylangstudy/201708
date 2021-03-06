import textwrap
text = '12345678901234567890123456789012345678901234567890123456789012345678901234567890'
#80文字。デフォルトは70字で折り返す。
print(textwrap.fill(text), '\n')
print(textwrap.fill(text, width=40), '\n')
text = '1234567890	1234567890'
print(textwrap.fill(text, expand_tabs=True))
text = '1234567890	1234567890'
print(textwrap.fill(text, expand_tabs=True, tabsize=4))

print(textwrap.fill(text, expand_tabs=True, replace_whitespace=True))
print(textwrap.fill(text, expand_tabs=True, replace_whitespace=False))
print(textwrap.fill(text, expand_tabs=False, replace_whitespace=True))#1Tab→1Space
print(textwrap.fill(text, expand_tabs=False, replace_whitespace=False))#1Tab→\t

#Space&Tab
text = ' 	1234567890	1234567890	 '
print(textwrap.fill(text))
print(textwrap.fill(text, drop_whitespace=True))
print(textwrap.fill(text, drop_whitespace=False))
#Space
text = ' 1234567890 1234567890 '
print(textwrap.fill(text))
print(textwrap.fill(text, drop_whitespace=True))
print(textwrap.fill(text, drop_whitespace=False))
#Tab
text = '	1234567890	1234567890	'
text = ' 	1234567890	1234567890	 '
print(textwrap.fill(text))
print(textwrap.fill(text, drop_whitespace=True))
print(textwrap.fill(text, drop_whitespace=False))

text = '12345678901234567890123456789012345678901234567890123456789012345678901234567890'
print(textwrap.fill(text, width=40, initial_indent='   '), '\n')
print(textwrap.fill(text, width=40, subsequent_indent='   '), '\n')

#fix_sentence_endingsは`([a-z]+\. )`の文字列を半角スペース2つ間を空けて区切る。じつに理解しがたい謎API。
text = 'abc. def! ghi? jkl. mn. opqrstu. vwxyz.'
print(textwrap.fill(text, fix_sentence_endings=True))
text = '1234567890. 1234567890. 1234567890. 1234567890. 1234567890. 1234567890. 1234567890. 1234567890.'
print(textwrap.fill(text, fix_sentence_endings=True))
text = 'ABC. DEF! GHI? JKL. MN. OPQRSTU. VWXYZ.'
print(textwrap.fill(text, fix_sentence_endings=True))

text = '12345678901234567890123456789012345678901234567890123456789012345678901234567890'
print(textwrap.fill(text, break_long_words=True))
print(textwrap.fill(text, break_long_words=False))

#何も変わらない… https://github.com/pallets/jinja/issues/550
text = 'abc-def'
print(textwrap.fill(text, break_on_hyphens=True, break_long_words=True))
print(textwrap.fill(text, break_on_hyphens=False, break_long_words=True))
text = 'ABC-DEF'
print(textwrap.fill(text, break_on_hyphens=True, break_long_words=True))
print(textwrap.fill(text, break_on_hyphens=False, break_long_words=True))
text = '1234567890-1234567890'
print(textwrap.fill(text, break_on_hyphens=True, break_long_words=True))
print(textwrap.fill(text, break_on_hyphens=False, break_long_words=True))

text = '12345678901234567890123456789012345678901234567890123456789012345678901234567890'
print(textwrap.fill(text, width=10, max_lines=3))
print(textwrap.fill(text, width=10, max_lines=3, placeholder='続く…'))
