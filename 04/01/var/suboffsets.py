import array
m = memoryview(array.array('H', [32000, 32001, 32002]))
print('suboffsets', m.suboffsets)
