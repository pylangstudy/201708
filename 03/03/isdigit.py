print(b'aAzZ'.isdigit())
print(b'1'.isdigit())
#print(b'①'.isdigit())#SyntaxError: bytes can only contain ASCII literal characters.

print(bytearray(b'aAzZ').isdigit())
print(bytearray(b'1').isdigit())
#print(bytearray(b'①').isdigit())#SyntaxError: bytes can only contain ASCII literal characters.

