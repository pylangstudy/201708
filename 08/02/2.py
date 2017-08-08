import string
import datetime
print('{}'.format('A'))
print('{} {}'.format('A', 'B'))
print('{0} {1} {0} {1}'.format('A', 'B'))
print('{name}'.format(name='A'))
print('私は{name}、{age}歳。'.format(name='山田太郎', age=99))

t = ('山田太郎', 99)
print('私は{0[0]}、{0[1]}歳。'.format(t))
print('私は{t[0]}、{t[1]}歳。'.format(t=t))

d = {'name':'山田太郎', 'age':99}
#print('私は{d.name}、{d.age}歳。'.format(d=d))#AttributeError: 'dict' object has no attribute 'name'
#print('私は{d["name"]}、{d["age"]}歳。'.format(d=d))#KeyError: '"name"'
print('私は{name}、{age}歳。'.format(**d))

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
h = Human('鈴木一郎', 88)
print('私は{0.name}、{0.age}歳。'.format(h))
print('私は{h.name}、{h.age}歳。'.format(h=h))
print('私は{name}、{age}歳。'.format(name=h.name, age=h.age))

print('{}'.format(h))
print('{!r}'.format(h))
print('{!s}'.format(h))
print('{!a}'.format(h))
print('{h!r}'.format(h=h))
print('{h!s}'.format(h=h))
print('{h!a}'.format(h=h))
print('{h.name!r}'.format(h=h))
print('{h.name!s}'.format(h=h))
print('{h.name!a}'.format(h=h))
print('{h.age!r}'.format(h=h))
print('{h.age!s}'.format(h=h))
print('{h.age!a}'.format(h=h))

print('{h.name!r:>16}'.format(h=h))#文字幅が1,2の違いがありズレる
print('{h.age!r:>16}'.format(h=h))
h = Human('Tanaka', 77)
print('{h.name!r:>16}'.format(h=h))
print('{h.age!r:>16}'.format(h=h))
print('{h.name!s:>16}'.format(h=h))
print('{h.age!s:>16}'.format(h=h))
