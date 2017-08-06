print('enter')
try:
    print('A')
finally:
    print('exit')

print('enter')
try:
    raise Exception('ERROR!')
    print('A')
finally:
    print('exit')
