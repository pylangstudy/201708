import struct
print(struct.pack('<2B', 0, (2**8)-1))#リトルエンディアン, unsigned char * 2件
print(struct.pack('>2B', 0, (2**8)-1))#ビッグエンディアン, unsigned char * 2件

print(struct.pack('<H', (2**8)-1))#リトルエンディアン, unsigned short * 1件
print(struct.pack('>H', (2**8)-1))#ビッグエンディアン, unsigned short * 1件

print(struct.unpack('<H', struct.pack('<H', (2**8)-1)))
print(struct.unpack('>H', struct.pack('>H', (2**8)-1)))

#b = bytes(4)
#struct.pack_into('<H', b, 2, (2**8)-1)#TypeError: argument must be read-write bytes-like object, not bytes
#print(b)
ba = bytearray(4)#引数=2だとstruct.error: pack_into requires a buffer of at least 2 bytesとなる。アラインメントで4Byte(32bit)必要？
print(ba)
struct.pack_into('<H', ba, 2, (2**8)-1)
print(ba)
