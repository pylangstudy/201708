m = memoryview(b'abc')
print(m.readonly)
m = memoryview(bytearray(b'abc'))
print(m.readonly)
