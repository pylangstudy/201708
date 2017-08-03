print('----- isalnum() -----')
s = b'abcdef123'
print(s.isalnum(), s)
s = b'abc 123'
print(s.isalnum(), s)
s = b'abc def_g123'
print(s.isalnum(), s)
"""
#SyntaxError: bytes can only contain ASCII literal characters.
s = b'①'; print(s.isalnum(), s)
s = b'⑴'; print(s.isalnum(), s)
s = b'⒈'; print(s.isalnum(), s)
s = b'⓵'; print(s.isalnum(), s)
s = b'⓿'; print(s.isalnum(), s)
s = b'➀'; print(s.isalnum(), s)
s = b'➊'; print(s.isalnum(), s)
"""
print('----- isalpha() -----')
c = b'azAz'
print(c.isalpha(), c)

print('----- isdecimal(), isdigit(), isnumeric() -----')
c = b'19'
#print(c.isdecimal(), c)#AttributeError: 'bytes' object has no attribute 'isdecimal'
print(c.isdigit(), c)
#print(c.isnumeric(), c)#AttributeError: 'bytes' object has no attribute 'isnumeric'

c = b'19.2'
#print(c.isdecimal(), c)
print(c.isdigit(), c)
#print(c.isnumeric(), c)

c = b'-19'
#print(c.isdecimal(), c)
print(c.isdigit(), c)
#print(c.isnumeric(), c)

c = b'+19'
#print(c.isdecimal(), c)
print(c.isdigit(), c)
#print(c.isnumeric(), c)

#https://stackoverflow.com/questions/22789392/str-isdecimal-and-str-isdigit-difference-example
c = b'\u00BD' # ½
#print(c.isdecimal(), c)
print(c.isdigit(), c)
#print(c.isnumeric(), c)


#----------------------------


print('----- isalnum() -----')
s = bytearray(b'abcdef123')
print(s.isalnum(), s)
s = bytearray(b'abc 123')
print(s.isalnum(), s)
s = bytearray(b'abc def_g123')
print(s.isalnum(), s)
"""
#SyntaxError: bytes can only contain ASCII literal characters.
s = bytearray(b'①'); print(s.isalnum(), s)
s = bytearray(b'⑴'); print(s.isalnum(), s)
s = bytearray(b'⒈'); print(s.isalnum(), s)
s = bytearray(b'⓵'); print(s.isalnum(), s)
s = bytearray(b'⓿'); print(s.isalnum(), s)
s = bytearray(b'➀'); print(s.isalnum(), s)
s = bytearray(b'➊'); print(s.isalnum(), s)
"""
print('----- isalpha() -----')
c = bytearray(b'azAz')
print(c.isalpha(), c)

print('----- isdecimal(), isdigit(), isnumeric() -----')
c = bytearray(b'19')
#print(c.isdecimal(), c)
print(c.isdigit(), c)
#print(c.isnumeric(), c)

c = bytearray(b'19.2')
#print(c.isdecimal(), c)
print(c.isdigit(), c)
#print(c.isnumeric(), c)

c = bytearray(b'-19')
#print(c.isdecimal(), c)
print(c.isdigit(), c)
#print(c.isnumeric(), c)

c = bytearray(b'+19')
#print(c.isdecimal(), c)
print(c.isdigit(), c)
#print(c.isnumeric(), c)

#https://stackoverflow.com/questions/22789392/str-isdecimal-and-str-isdigit-difference-example
c = bytearray(b'\u00BD') # ½
#print(c.isdecimal(), c)
print(c.isdigit(), c)
#print(c.isnumeric(), c)

