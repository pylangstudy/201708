s = b'abcdefgabc'
print(s)
print('c:', s.rfind(b'c'))
print('z:', s.rfind(b'z'))
print('def:', s.rfind(b'def'))

print('c:', s.find(b'c'))
print('z:', s.find(b'z'))
print('def:', s.find(b'def'))
print(b'cd' in s)


s = bytearray(b'abcdefgabc')
print(s)
print('c:', s.rfind(bytearray(b'c')))
print('z:', s.rfind(bytearray(b'z')))
print('def:', s.rfind(bytearray(b'def')))

print('c:', s.find(bytearray(b'c')))
print('z:', s.find(bytearray(b'z')))
print('def:', s.find(bytearray(b'def')))
print(b'cd' in s)
