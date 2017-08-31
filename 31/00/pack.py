import struct
print(struct.pack('<2B', 0, (2**8)-1))#リトルエンディアン, unsigned char * 2件
print(struct.pack('>2B', 0, (2**8)-1))#ビッグエンディアン, unsigned char * 2件

print(struct.pack('<H', (2**8)-1))#リトルエンディアン, unsigned short * 1件
print(struct.pack('>H', (2**8)-1))#ビッグエンディアン, unsigned short * 1件

print(struct.unpack('<H', struct.pack('<H', (2**8)-1)))
print(struct.unpack('>H', struct.pack('>H', (2**8)-1)))
