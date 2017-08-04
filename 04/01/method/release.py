m = memoryview(b'abc')
m.release()
#print(m[0])#ValueError: operation forbidden on released memoryview object

with memoryview(b'abc') as m:
    print(m[0])
print(m[0])#ValueError: operation forbidden on released memoryview object

