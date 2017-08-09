#!python3.6
import string
print('----------整数の表現型----------')
v = 15
print(string.Formatter().format('{v:b}', v=v))
print(string.Formatter().format('{v:o}', v=v))
print(string.Formatter().format('{v:d}', v=v))
print(string.Formatter().format('{v:x}', v=v))
print(string.Formatter().format('{v:X}', v=v))
print('{v:b}'.format(v=v))
print('{v:o}'.format(v=v))
print('{v:d}'.format(v=v))
print('{v:x}'.format(v=v))
print('{v:X}'.format(v=v))
print(f'{v:b}')
print(f'{v:o}')
print(f'{v:d}')
print(f'{v:x}')
print(f'{v:X}')

v = 0
print(string.Formatter().format('{v:c}', v=v))
print('{v:c}'.format(v=v))
print(f'{v:c}')

v = 1234567890
print(string.Formatter().format('{v:n}', v=v))
print('{v:n}'.format(v=v))
print(f'{v:n}')

print('----------浮動小数点数と10進数の表現型----------')
v = 1234567890
print(string.Formatter().format('{v:e}', v=v))
print('{v:e}'.format(v=v))
print(f'{v:e}')
print(string.Formatter().format('{v:E}', v=v))
print('{v:E}'.format(v=v))
print(f'{v:E}')
print(string.Formatter().format('{v:.3e}', v=v))
print('{v:.3e}'.format(v=v))
print(f'{v:.3e}')
print(string.Formatter().format('{v:.3E}', v=v))
print('{v:.3E}'.format(v=v))
print(f'{v:.3E}')
print(string.Formatter().format('{v:g}', v=v))
print('{v:g}'.format(v=v))
print(f'{v:g}')
print(string.Formatter().format('{v:G}', v=v))
print('{v:G}'.format(v=v))
print(f'{v:G}')

v = 0.1234567890
print(string.Formatter().format('{v:f}', v=v))
print('{v:f}'.format(v=v))
print(f'{v:f}')
print(string.Formatter().format('{v:F}', v=v))
print('{v:F}'.format(v=v))
print(f'{v:F}')
print(string.Formatter().format('{v:.3f}', v=v))
print('{v:.3f}'.format(v=v))
print(f'{v:.3f}')
print(string.Formatter().format('{v:.3F}', v=v))
print('{v:.3F}'.format(v=v))
print(f'{v:.3F}')
print(string.Formatter().format('{v:g}', v=v))
print('{v:g}'.format(v=v))
print(f'{v:g}')
print(string.Formatter().format('{v:G}', v=v))
print('{v:G}'.format(v=v))
print(f'{v:G}')

v = 1234567890
print(string.Formatter().format('{v:n}', v=v))
print('{v:n}'.format(v=v))
print(f'{v:n}')

v = 0.5
print(string.Formatter().format('{v:%}', v=v))
print('{v:%}'.format(v=v))
print(f'{v:%}')
v = 0.123456789
print(string.Formatter().format('{v:.3%}', v=v))
print('{v:.3%}'.format(v=v))
print(f'{v:.3%}')
v = 0.999999999
print(string.Formatter().format('{v:.3%}', v=v))
print('{v:.3%}'.format(v=v))
print(f'{v:.3%}')

