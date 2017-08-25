import textwrap
s = 'hello\n\n \nworld'
print(textwrap.indent(s, '  '))
print('-------------------')
print(textwrap.indent(s, prefix='+ ', predicate=lambda line: True))
