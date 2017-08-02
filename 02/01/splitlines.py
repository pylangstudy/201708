s = 'a\nb\rc\r\nd\ve\ff\x1cg\x1dh\x1ei\x85j\u2028k\u2029l'
print(s)
print(s.splitlines())
print(s.splitlines(True))
s = '\n'
print(s)
print(s.splitlines())
print(s.splitlines(True))
print(s.split())
