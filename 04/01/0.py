b = b'abcefg'
print(b)
v = memoryview(b)
print(v)
print(v[1])
print(v[-1])
print(v[1:4])
print(bytes(v[1:4]))
for i in v: print('{0:#x}'.format(i), end=' ')

