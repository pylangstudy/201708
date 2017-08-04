v = memoryview(b'abcefg')
print(hash(v) == hash(b'abcefg'))
print(hash(v[2:4]) == hash(b'ce'))
print(hash(v[::-2]) == hash(b'abcefg'[::-2]))
