#!python3.6
import string
d = {'name': 'Yamada', 'age': -64}
print(string.Formatter().format('{name} {age}', **d))
print('{name} {age}'.format(**d))
print(f'{d["name"]} {d["age"]}')

print(string.Formatter().format('{name:<8} {age:<8}', **d))
print('{name:<8} {age:<8}'.format(**d))
print(f'{d["name"]:<8} {d["age"]:<8}')

print(string.Formatter().format('{name:>8} {age:>8}', **d))
print('{name:>8} {age:>8}'.format(**d))
print(f'{d["name"]:>8} {d["age"]:>8}')

print(string.Formatter().format('{name:^8} {age:^8}', **d))
print('{name:^8} {age:^8}'.format(**d))
print(f'{d["name"]:^8} {d["age"]:^8}')

d = {'name': 'Yamada', 'age': -64}
print(string.Formatter().format('{name} {age}', **d))
print('{name} {age}'.format(**d))
print(f'{d["name"]} {d["age"]}')

print(string.Formatter().format('{name} {age:=8}', **d))
print('{name} {age:=8}'.format(**d))
print(f'{d["name"]} {d["age"]:=8}')

print(string.Formatter().format('{name} {age:=08}', **d))
print('{name} {age:=08}'.format(**d))
print(f'{d["name"]} {d["age"]:=08}')

