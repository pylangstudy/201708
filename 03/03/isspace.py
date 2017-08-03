s = b'abc'; print(s.isspace(), s)
s = b'a-c'; print(s.isspace(), s)
s = b'a c'; print(s.isspace(), s)
s = b'a\tc'; print(s.isspace(), s)
s = b'   '; print(s.isspace(), s)#半角スペースつ3
s = b'\r\n'; print(s.isspace(), s)
#s = b'　'; print(s.isspace(), s)#全角スペース SyntaxError: bytes can only contain ASCII literal characters.

s = bytearray(b'abc'); print(s.isspace(), s)
s = bytearray(b'a-c'); print(s.isspace(), s)
s = bytearray(b'a c'); print(s.isspace(), s)
s = bytearray(b'a\tc'); print(s.isspace(), s)
s = bytearray(b'   '); print(s.isspace(), s)#半角スペースつ3
s = bytearray(b'\r\n'); print(s.isspace(), s)
#s = bytearray(b'　'); print(s.isspace(), s)#全角スペース SyntaxError: bytes can only contain ASCII literal characters.
