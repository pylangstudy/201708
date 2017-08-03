#s = b' 　\t\r\na b c 　\t\r\n'#SyntaxError: bytes can only contain ASCII literal characters.
#s = b' a b c '
s = b' \t\r\n a b c \t\r\n'#SyntaxError: bytes can only contain ASCII literal characters.
print(b'>' + s.lstrip() + b'<')
print(b'>' + s.rstrip() + b'<')
print(b'>' + s.strip() + b'<')

s = b'a b c a'
print(b'>' + s.lstrip(b'a') + b'<')
print(b'>' + s.rstrip(b'a') + b'<')
print(b'>' + s.strip(b'a') + b'<')

