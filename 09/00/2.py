#!python3.6
import string
v = 15
print(string.Formatter().format('{v:#}', v=v))
print('{v:#}'.format(v=v))
print(f'{v:#}')

print(string.Formatter().format('{v:#b}', v=v))
print(string.Formatter().format('{v:#o}', v=v))
print(string.Formatter().format('{v:#d}', v=v))
print(string.Formatter().format('{v:#x}', v=v))
print(string.Formatter().format('{v:#X}', v=v))
print('{v:#b}'.format(v=v))
print('{v:#o}'.format(v=v))
print('{v:#d}'.format(v=v))
print('{v:#x}'.format(v=v))
print('{v:#X}'.format(v=v))
print(f'{v:#b}')
print(f'{v:#o}')
print(f'{v:#d}')
print(f'{v:#x}')
print(f'{v:#X}')

v = 1.23
print(string.Formatter().format('{v:#g}', v=v))
print(string.Formatter().format('{v:#G}', v=v))
print('{v:#g}'.format(v=v))
print('{v:#G}'.format(v=v))
print(f'{v:#g}')
print(f'{v:#G}')
#v = 987654321.12345
v = 100.200
print(string.Formatter().format('{v:#g}', v=v))
print(string.Formatter().format('{v:#G}', v=v))
print('{v:#g}'.format(v=v))
print('{v:#G}'.format(v=v))
print(f'{v:#g}')
print(f'{v:#G}')
