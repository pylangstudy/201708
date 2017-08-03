b = b'abcdefg'
print(b)
print('c:', b.find(b'c'))
print('z:', b.find(b'z'))
print('def:', b.find(b'def'))
print(b'cd' in b)

b = bytearray(b'abcdefg')
print(b)
print('c:', b.find(b'c'))
print('z:', b.find(b'z'))
print('def:', b.find(b'def'))
print(b'cd' in b)
