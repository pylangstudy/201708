import types
print(types.__dict__)
for k in types.__dict__['__builtins__'].keys(): print(k)
