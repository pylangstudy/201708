import array, struct
m = memoryview(array.array('H', [32000, 32001, 32002]))
print(m.itemsize)
print(m[0])
print(struct.calcsize('H') == m.itemsize)
