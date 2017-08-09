#!python3.6
for align, text in zip('<^>', ['left', 'center', 'right']):
    '{0:{fill}{align}16}'.format(text, fill=align, align=align)
octets = [192, 168, 0, 1]
print('{:02X}{:02X}{:02X}{:02X}'.format(*octets))
print(int(str(octets[0]), 16))

width = 5
for num in range(5,12): 
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()
