import struct
b = struct.pack('HH', 0, 65535)
m = memoryview(b)
print(m.format)

import array
a = array.array('i', [1,2])
m = memoryview(a)
print(m.format)
