d = {(1,'a'): '1a', (2,'b'): '2b'}
print(d)
print(d[(1,'a')])
print(d[(2,'b')])
for k, v in d.items(): print(k, v)

s = set(d.keys())
print(s)
fs = frozenset(d.keys())
print(fs)
