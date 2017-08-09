#!python3.6
import string

v = 12345.6789012
print(string.Formatter().format('{v:,}', v=v))
print('{v:,}'.format(v=v))
print(f'{v:,}')

print(string.Formatter().format('{v:_}', v=v))
print('{v:_}'.format(v=v))
print(f'{v:_}')

v = 0xFFFF
print(string.Formatter().format('{v:,}', v=v))
print('{v:,}'.format(v=v))
print(f'{v:,}')

print(string.Formatter().format('{v:_}', v=v))
print('{v:_}'.format(v=v))
print(f'{v:_}')

