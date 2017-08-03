s = b'abcdefgabc'
print(s)
print('c:', s.rindex(b'c'))
print('c:', s.index(b'c'))
#print('z:', s.rindex(b'z'))#ValueError: subsection not found

s = bytearray(b'abcdefgabc')
print(s)
print('c:', s.rindex(bytearray(b'c')))
print('c:', s.index(bytearray(b'c')))
#print('z:', s.rindex(bytearray(b'z')))#ValueError: subsection not found
