#!python3.6
import string
v = 1.23456789
print(string.Formatter().format('{v:.3f}', v=v))
print('{v:.3f}'.format(v=v))
print(f'{v:.3f}')

v = 123456789.987654321
print(string.Formatter().format('{v:.3e}', v=v))
print('{v:.3e}'.format(v=v))
print(f'{v:.3e}')

v = 123456789.987654321j+8
print(string.Formatter().format('{v:.3g}', v=v))
print('{v:.3g}'.format(v=v))
print(f'{v:.3g}')
