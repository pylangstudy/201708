s = b'abc'; print(s.isupper(), s)
s = b'Abc'; print(s.isupper(), s)
s = b'aBc'; print(s.isupper(), s)
s = b'abC'; print(s.isupper(), s)
s = b'abc'; print(s.isupper(), s)
s = b'ABC'; print(s.isupper(), s)
s = b'abc'; print(s.capitalize().isupper(), s.capitalize())

s = bytearray(b'abc'); print(s.isupper(), s)
s = bytearray(b'Abc'); print(s.isupper(), s)
s = bytearray(b'aBc'); print(s.isupper(), s)
s = bytearray(b'abC'); print(s.isupper(), s)
s = bytearray(b'abc'); print(s.isupper(), s)
s = bytearray(b'ABC'); print(s.isupper(), s)
s = bytearray(b'abc'); print(s.capitalize().isupper(), s.capitalize())
