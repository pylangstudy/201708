import textwrap
tw = textwrap.TextWrapper()
text = '12345678901234567890123456789012345678901234567890123456789012345678901234567890'
print(tw.wrap(text))
print(tw.fill(text))

tw = textwrap.TextWrapper(width=40)
print(tw.wrap(text))

tw = textwrap.TextWrapper(expand_tabs=True)
text = '1234567890	1234567890'
print(tw.wrap(text))
tw = textwrap.TextWrapper(expand_tabs=True, tabsize=4)
text = '1234567890	1234567890'
print(tw.wrap(text))

tw = textwrap.TextWrapper(expand_tabs=True, replace_whitespace=True)
print(tw.wrap(text))
tw = textwrap.TextWrapper(expand_tabs=True, replace_whitespace=False)
print(tw.wrap(text))
tw = textwrap.TextWrapper(expand_tabs=False, replace_whitespace=True)
print(tw.wrap(text))
tw = textwrap.TextWrapper(expand_tabs=False, replace_whitespace=False)
print(tw.wrap(text))

#Space&Tab
text = ' 	1234567890	1234567890	 '
tw = textwrap.TextWrapper(drop_whitespace=True)
print(tw.wrap(text))
tw = textwrap.TextWrapper(drop_whitespace=False)
print(tw.wrap(text))

text = '12345678901234567890123456789012345678901234567890123456789012345678901234567890'
tw = textwrap.TextWrapper(width=40, initial_indent='   ')
print(tw.wrap(text))
tw = textwrap.TextWrapper(width=40, subsequent_indent='   ')
print(tw.wrap(text))

#fix_sentence_endingsは`([a-z]+\. )`の文字列を半角スペース2つ間を空けて区切る。じつに理解しがたい謎API。
text = 'abc. def! ghi? jkl. mn. opqrstu. vwxyz.'
tw = textwrap.TextWrapper(fix_sentence_endings=True)
print(tw.wrap(text))

text = '12345678901234567890123456789012345678901234567890123456789012345678901234567890'
tw = textwrap.TextWrapper(fix_sentence_endings=True)
print(tw.wrap(text))
tw = textwrap.TextWrapper(fix_sentence_endings=False)
print(tw.wrap(text))

#何も変わらない… https://github.com/pallets/jinja/issues/550
text = 'abc-def'
tw = textwrap.TextWrapper(break_on_hyphens=True, break_long_words=True)
print(tw.wrap(text))
tw = textwrap.TextWrapper(break_on_hyphens=False, break_long_words=True)
print(tw.wrap(text))

text = '12345678901234567890123456789012345678901234567890123456789012345678901234567890'
tw = textwrap.TextWrapper(width=10, max_lines=3)
print(tw.wrap(text))
tw = textwrap.TextWrapper(width=10, max_lines=3, placeholder='続く…')
print(tw.wrap(text))
