import struct

ba = bytearray(4)
struct.pack_into('<2H', ba, 0, (2**4), (2**16)-1)
print(ba)
print('----- 2byteずつ')
for ushort in struct.iter_unpack('<H', ba): print(ushort)
print('----- 1byteずつ')
for ub in struct.iter_unpack('<B', ba): print(ub)
