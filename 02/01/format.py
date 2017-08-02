print('{}'.format('abc'))
print('{} {}'.format('abc', 123))
print('{1} {0} {1}'.format('abc', 123))

print('{0:>10}'.format('abc'))
print('{0:>b}'.format(15))
print('{0:>o}'.format(15))
print('{0:>d}'.format(15))
print('{0:>x}'.format(15))

import datetime
print('{0:%Y-%m-%d %H:%M:%S.%f}'.format(datetime.datetime.now()))
