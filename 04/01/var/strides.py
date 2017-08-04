import array
m = memoryview(array.array('H', [32000, 32001, 32002]))
print('ndim', m.ndim)
print('shape', m.shape)
print('strides', m.strides)
