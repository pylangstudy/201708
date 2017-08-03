print(b''.join([b'ab',b'cd']))
print(b','.join([b'ab',b'cd']))
print(b'<-->'.join([b'ab',b'cd',b'ef']))
#print(b' '.join([x for x in bytes(range(5))]))#TypeError: sequence item 0: expected a bytes-like object, int found

#print([hex(x).replace('0x','') for x in range(5)])
#print([bytes.fromhex(hex(x).replace('0x','')) for x in range(5)])
#print(b' '.join([bytes.fromhex(hex(x).replace('0x','')) for x in range(5)]))#TypeError: sequence item 0: expected a bytes-like object, int found

print()
print(bytearray(b'').join([bytearray(b'ab'),bytearray(b'cd')]))
print(bytearray(b',').join([bytearray(b'ab'),bytearray(b'cd')]))
print(bytearray(b'<-->').join([bytearray(b'ab'),bytearray(b'cd'),bytearray(b'ef')]))
#print(bytearray(b' ').join([bytearray(x) for x in range(5)]))
