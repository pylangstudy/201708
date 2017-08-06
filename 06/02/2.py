import contextlib

@contextlib.contextmanager
def manager():
    print('enter')
    try: yield
    finally: print('exit')

with manager() as a:
    print('A')

with manager() as a:
    raise Exception('ERROR!')
    print('A')
