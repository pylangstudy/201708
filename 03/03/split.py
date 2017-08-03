s = b'a,b,c'
print(s.split(b','))
#print(s.lsplit(b','))#AttributeError: 'bytes' object has no attribute 'lsplit'
print(s.rsplit(b','))

s = bytearray(b'a,b,c')
print(s.split(bytearray(b',')))
#print(s.lsplit(bytearray(b',')))#AttributeError: 'bytearray' object has no attribute 'lsplit'
print(s.rsplit(bytearray(b',')))
