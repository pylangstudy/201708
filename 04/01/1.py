import struct
#b = struct.pack('b', 127)
#b = struct.pack('B', 255)
#b = struct.pack('h', 32767)
b = struct.pack('bBhH', *[127, 255, 32767, 65535])
print(b)
v = memoryview(b)
#for i in v: print(i)
for i in struct.unpack('bBhH', memoryview(b)): print(i)
