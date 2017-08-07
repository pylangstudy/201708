class ModuleException(Exception): pass
try: raise Exception()
except Exception as e: raise ModuleException(e) from e
