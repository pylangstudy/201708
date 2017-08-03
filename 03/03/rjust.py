s = b'abc'; print(b'>' + s.rjust(8) + b'<')
s = b'abc'; print(b'>' + s.rjust(8, b'-') + b'<')

s = b'abc'; print(b'>' + s.rjust(8) + b'<')
s = b'abc'; print(b'>' + s.rjust(8, b'-') + b'<')

s = b'abc'; print(b'>' + s.center(8) + b'<')
s = b'abc'; print(b'>' + s.center(8, b'-') + b'<')

s = b'abc'; print(b'>' + s.center(2) + b'<')
s = b'abc'; print(b'>' + s.center(2, b'-') + b'<')


s = bytearray(b'abc'); print(bytearray(b'>') + s.rjust(8) + bytearray(b'<'))
s = bytearray(b'abc'); print(bytearray(b'>') + s.rjust(8, bytearray(b'-')) + bytearray(b'<'))

s = bytearray(b'abc'); print(bytearray(b'>') + s.rjust(8) + bytearray(b'<'))
s = bytearray(b'abc'); print(bytearray(b'>') + s.rjust(8, bytearray(b'-')) + bytearray(b'<'))

s = bytearray(b'abc'); print(bytearray(b'>') + s.center(8) + bytearray(b'<'))
s = bytearray(b'abc'); print(bytearray(b'>') + s.center(8, bytearray(b'-')) + bytearray(b'<'))

s = bytearray(b'abc'); print(bytearray(b'>') + s.center(2) + bytearray(b'<'))
s = bytearray(b'abc'); print(bytearray(b'>') + s.center(2, bytearray(b'-')) + bytearray(b'<'))
