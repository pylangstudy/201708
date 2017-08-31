import struct

ba = bytearray(4)#引数=2だとstruct.error: pack_into requires a buffer of at least 2 bytesとなる。アラインメントで4Byte
struct.pack_into('<H', ba, 0, (2**12)-1)
print(ba)
print('unpack_from:', struct.unpack_from('<B', ba, offset=0))
print(ba)
print('unpack_from:', struct.unpack_from('<B', ba, offset=1))
print(ba)
print('unpack_from:', struct.unpack_from('<B', ba, offset=2))
print(ba)

