s = b'abcabc'; print(s, s.replace(b'a', b'A'))
s = b'abcabc'; print(s, s.replace(b'ab', b'12'))
s = b'abcabc'; print(s, s.replace(b'a', b'A', 1))
s = b'abcabc'; print(s, s.replace(b'z', b'Z'))

s = bytearray(b'abcabc'); print(s, s.replace(bytearray(b'a'), bytearray(b'A')))
s = bytearray(b'abcabc'); print(s, s.replace(bytearray(b'ab'), bytearray(b'12')))
s = bytearray(b'abcabc'); print(s, s.replace(bytearray(b'a'), bytearray(b'A'), 1))
s = bytearray(b'abcabc'); print(s, s.replace(bytearray(b'z'), bytearray(b'Z')))
