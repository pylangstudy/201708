#!python3.6
import difflib
d = difflib.Differ(); print(d)
print(d.compare('abc', 'abcd'))
for diff in d.compare('abc', 'abcd'): print(diff)

print('-----linejunk')
d = difflib.Differ(linejunk=lambda s: ' ' in s)
for diff in d.compare('a bc', 'abc'): print(diff)

print('-----charjunk')
d = difflib.Differ(charjunk=lambda c: ' ' == c)
for diff in d.compare('a bc', 'abc'): print(diff)
