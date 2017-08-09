#!python3.6
import string
d = {'name': 'Yamada', 'age': 64}
print(string.Formatter().format('{name} {age:+}', **d))
print('{name} {age:+}'.format(**d))
print(f'{d["name"]} {d["age"]:+}')

print(string.Formatter().format('{name} {age: }', **d))
print('{name} {age: }'.format(**d))
print(f'{d["name"]} {d["age"]: }')

d = {'name': 'Yamada', 'age': -64}
print(string.Formatter().format('{name} {age:-}', **d))
print('{name} {age:-}'.format(**d))
print(f'{d["name"]} {d["age"]:-}')
