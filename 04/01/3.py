data = bytearray(b'abcefg')
v = memoryview(data)
print(v.readonly)
v[0] = ord(b'z')
print(data)
v[1:4] = b'123'
print(data)
#v[2:3] = b'spam' #ValueError: memoryview assignment: lvalue and rvalue have different structures
v[2:6] = b'spam'
print(data)
