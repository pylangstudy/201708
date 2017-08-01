print(str(123))
print(''.join(['abc', 'def']))
import io
strio = io.StringIO()
strio.write('abc')
strio.write('def')
print(strio.getvalue())
strio.close()
