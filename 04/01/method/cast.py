import array

#1D/long から 1D/unsigned byte へのキャスト:
print('1D/long から 1D/unsigned byte へのキャスト')
a = array.array('l', [1,2,3])
x = memoryview(a)
print(x.format)
print(x.itemsize)
print(len(x))
print(x.nbytes)

y = x.cast('B')
print(y.format)
print(y.itemsize)
print(len(y))
print(y.nbytes)

#1D/unsigned byte から 1D/char へのキャスト:
print('1D/unsigned byte から 1D/char へのキャスト')
b = bytearray(b'zyz')
x = memoryview(b)
#x[0] = b'a'#TypeError: memoryview: invalid type for format 'B'
y = x.cast('c')
y[0] = b'a'
print(b)
print(x.tolist())
print(y.tolist())

#1D/byte から 3D/int へ、そして 1D/signed char へのキャスト:
print('1D/byte から 3D/int へ、そして 1D/signed char へのキャスト')
import struct
buf = struct.pack("i"*12, *list(range(12)))
x = memoryview(buf)
y = x.cast('i', shape=[2,2,3])
print(buf)
print(x.tolist())
print(y.tolist())
print(y.format)
print(y.itemsize)
print(len(y))
print(y.nbytes)
z = y.cast('b')
print(z.format)
print(z.itemsize)
print(len(z))
print(z.nbytes)

#1D/unsigned char から 2D/unsigned long へのキャスト:
print('1D/unsigned char から 2D/unsigned long へのキャスト')
buf = struct.pack("L"*6, *list(range(6)))
x = memoryview(buf)
y = x.cast('L', shape=[2,3])
print(buf)
print(x.tolist())
print(y.tolist())
print(len(y))
print(y.nbytes)
print(y.tolist())
