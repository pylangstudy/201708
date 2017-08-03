s = b'a,b,c'; print(s.partition(b','))
s = b'a,b,c'; print(s.partition(b'-'))
#s = 'a,b,c'; print(s.partition(None)) #TypeError: must be str, not NoneType
#s = 'a,b,c'; print(s.partition('')) #ValueError: empty separator

s = b'a,b,c'; print(s.rpartition(b','))
s = b'a,b,c'; print(s.rpartition(b'-'))
#s = 'a,b,c'; print(s.rpartition(None)) #TypeError: must be str, not NoneType
#s = 'a,b,c'; print(s.rpartition('')) #ValueError: empty separator

s = bytearray(b'a,b,c'); print(s.partition(bytearray(b',')))
s = bytearray(b'a,b,c'); print(s.partition(bytearray(b'-')))
s = bytearray(b'a,b,c'); print(s.rpartition(bytearray(b',')))
s = bytearray(b'a,b,c'); print(s.rpartition(bytearray(b'-')))

