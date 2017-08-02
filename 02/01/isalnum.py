print('----- isalnum() -----')
s = 'abcdef123'
print(s.isalnum(), s)
s = 'abc 123'
print(s.isalnum(), s)
s = 'abc def_g123'
print(s.isalnum(), s)
s = '①'; print(s.isalnum(), s)
s = '⑴'; print(s.isalnum(), s)
s = '⒈'; print(s.isalnum(), s)
s = '⓵'; print(s.isalnum(), s)
s = '⓿'; print(s.isalnum(), s)
s = '➀'; print(s.isalnum(), s)
s = '➊'; print(s.isalnum(), s)

print('----- isalpha() -----')
c = 'azAz'
print(c.isalpha(), c)

print('----- isdecimal(), isdigit(), isnumeric() -----')
c = '19'
print(c.isdecimal(), c)
print(c.isdigit(), c)
print(c.isnumeric(), c)

c = '19.2'
print(c.isdecimal(), c)
print(c.isdigit(), c)
print(c.isnumeric(), c)

c = '-19'
print(c.isdecimal(), c)
print(c.isdigit(), c)
print(c.isnumeric(), c)

c = '+19'
print(c.isdecimal(), c)
print(c.isdigit(), c)
print(c.isnumeric(), c)

#https://stackoverflow.com/questions/22789392/str-isdecimal-and-str-isdigit-difference-example
c = '\u00BD' # ½
print(c.isdecimal(), c)
print(c.isdigit(), c)
print(c.isnumeric(), c)

