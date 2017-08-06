src = """def f():
    print('abc')
f()
"""
#co = compile("print('abc')", '', 'exec')
co = compile(src, '', 'exec')
exec(co)
co = compile("print('abc')", '', 'exec')
eval(co)
co = compile("print('abc')", '', 'single')
eval(co)
