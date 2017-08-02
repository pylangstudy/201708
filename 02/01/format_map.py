class Default(dict):
    def __missing__(self, key): return key

print('{name} was born in {country}'.format_map(Default(name='Guido')))

d = Default(name='Yamada', country='Japan')
print('{name} {country}'.format_map(d))

d = {'name': 'Yamada', 'country': 'Japan'}
print('{name} {country}'.format_map(d))

print('{name} {country}'.format_map({'name': 'Yamada', 'country': 'Japan'}))

print('d={d}'.format_map(locals()))

