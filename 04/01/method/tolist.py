print(memoryview(b'abc').tolist())
import array
a = array.array('d', [1.1, 2.2, 3.3])
m = memoryview(a)
print(m.tolist())
