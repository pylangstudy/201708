import array
a = array.array('l', [-11111111, 22222222, -33333333, 44444444])
m = memoryview(a)
print(m[0])
print(m[-1])
print(m[::2].tolist())
