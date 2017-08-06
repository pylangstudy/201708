#class A(contextmanager): pass #NameError: name 'contextmanager' is not defined
class A:
    def __enter__(self):
        print('__enter__')
    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__', exc_type, exc_value, traceback)

with A() as a:
    print('A')

with A() as a:
    raise Exception('ERROR!')
    print('A')
