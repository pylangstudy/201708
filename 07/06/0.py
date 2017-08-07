import sys
class ModuleException(Exception): pass
try: raise Exception()
except Exception as e:
    tb = sys.exc_info()[2]
    raise ModuleException().with_traceback(tb)
