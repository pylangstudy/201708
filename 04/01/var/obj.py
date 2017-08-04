b  = bytearray(b'xyz')
m = memoryview(b)
print(m.obj is b)
