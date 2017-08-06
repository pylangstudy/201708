# [4.12.6. 型オブジェクト](https://docs.python.jp/3/library/stdtypes.html#type-objects)

< [4.12. その他の組み込み型](https://docs.python.jp/3/library/stdtypes.html#other-built-in-types) < [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## 説明

> 型オブジェクトは様々なオブジェクト型を表します。オブジェクトの型は組み込み関数 type() でアクセスされます。型オブジェクトには特有の操作はありません。標準モジュール types には全ての組み込み型名が定義されています。

* [type()](https://docs.python.jp/3/library/functions.html#type)
* [types](https://docs.python.jp/3/library/types.html#module-types)

> 型はこのように書き表されます: <class 'int'> 。

### ソースコード

```python
import types
print(types.__dict__)
for k in types.__dict__['__builtins__'].keys(): print(k)
```
```sh
$ python 0.py 
{'__name__': 'types', '__doc__': "\nDefine names for built-in types that aren't directly accessible as a builtin.\n", '__package__': '', '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0xb71e1e4c>, '__spec__': ModuleSpec(name='types', loader=<_frozen_importlib_external.SourceFileLoader object at 0xb71e1e4c>, origin='/home/mint/.pyenv/versions/3.6.1/lib/python3.6/types.py'), '__file__': '/home/mint/.pyenv/versions/3.6.1/lib/python3.6/types.py', '__cached__': '/home/mint/.pyenv/versions/3.6.1/lib/python3.6/__pycache__/types.cpython-36.pyc', '__builtins__': {'__name__': 'builtins', '__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.", '__package__': '', '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>), '__build_class__': <built-in function __build_class__>, '__import__': <built-in function __import__>, 'abs': <built-in function abs>, 'all': <built-in function all>, 'any': <built-in function any>, 'ascii': <built-in function ascii>, 'bin': <built-in function bin>, 'callable': <built-in function callable>, 'chr': <built-in function chr>, 'compile': <built-in function compile>, 'delattr': <built-in function delattr>, 'dir': <built-in function dir>, 'divmod': <built-in function divmod>, 'eval': <built-in function eval>, 'exec': <built-in function exec>, 'format': <built-in function format>, 'getattr': <built-in function getattr>, 'globals': <built-in function globals>, 'hasattr': <built-in function hasattr>, 'hash': <built-in function hash>, 'hex': <built-in function hex>, 'id': <built-in function id>, 'input': <built-in function input>, 'isinstance': <built-in function isinstance>, 'issubclass': <built-in function issubclass>, 'iter': <built-in function iter>, 'len': <built-in function len>, 'locals': <built-in function locals>, 'max': <built-in function max>, 'min': <built-in function min>, 'next': <built-in function next>, 'oct': <built-in function oct>, 'ord': <built-in function ord>, 'pow': <built-in function pow>, 'print': <built-in function print>, 'repr': <built-in function repr>, 'round': <built-in function round>, 'setattr': <built-in function setattr>, 'sorted': <built-in function sorted>, 'sum': <built-in function sum>, 'vars': <built-in function vars>, 'None': None, 'Ellipsis': Ellipsis, 'NotImplemented': NotImplemented, 'False': False, 'True': True, 'bool': <class 'bool'>, 'memoryview': <class 'memoryview'>, 'bytearray': <class 'bytearray'>, 'bytes': <class 'bytes'>, 'classmethod': <class 'classmethod'>, 'complex': <class 'complex'>, 'dict': <class 'dict'>, 'enumerate': <class 'enumerate'>, 'filter': <class 'filter'>, 'float': <class 'float'>, 'frozenset': <class 'frozenset'>, 'property': <class 'property'>, 'int': <class 'int'>, 'list': <class 'list'>, 'map': <class 'map'>, 'object': <class 'object'>, 'range': <class 'range'>, 'reversed': <class 'reversed'>, 'set': <class 'set'>, 'slice': <class 'slice'>, 'staticmethod': <class 'staticmethod'>, 'str': <class 'str'>, 'super': <class 'super'>, 'tuple': <class 'tuple'>, 'type': <class 'type'>, 'zip': <class 'zip'>, '__debug__': True, 'BaseException': <class 'BaseException'>, 'Exception': <class 'Exception'>, 'TypeError': <class 'TypeError'>, 'StopAsyncIteration': <class 'StopAsyncIteration'>, 'StopIteration': <class 'StopIteration'>, 'GeneratorExit': <class 'GeneratorExit'>, 'SystemExit': <class 'SystemExit'>, 'KeyboardInterrupt': <class 'KeyboardInterrupt'>, 'ImportError': <class 'ImportError'>, 'ModuleNotFoundError': <class 'ModuleNotFoundError'>, 'OSError': <class 'OSError'>, 'EnvironmentError': <class 'OSError'>, 'IOError': <class 'OSError'>, 'EOFError': <class 'EOFError'>, 'RuntimeError': <class 'RuntimeError'>, 'RecursionError': <class 'RecursionError'>, 'NotImplementedError': <class 'NotImplementedError'>, 'NameError': <class 'NameError'>, 'UnboundLocalError': <class 'UnboundLocalError'>, 'AttributeError': <class 'AttributeError'>, 'SyntaxError': <class 'SyntaxError'>, 'IndentationError': <class 'IndentationError'>, 'TabError': <class 'TabError'>, 'LookupError': <class 'LookupError'>, 'IndexError': <class 'IndexError'>, 'KeyError': <class 'KeyError'>, 'ValueError': <class 'ValueError'>, 'UnicodeError': <class 'UnicodeError'>, 'UnicodeEncodeError': <class 'UnicodeEncodeError'>, 'UnicodeDecodeError': <class 'UnicodeDecodeError'>, 'UnicodeTranslateError': <class 'UnicodeTranslateError'>, 'AssertionError': <class 'AssertionError'>, 'ArithmeticError': <class 'ArithmeticError'>, 'FloatingPointError': <class 'FloatingPointError'>, 'OverflowError': <class 'OverflowError'>, 'ZeroDivisionError': <class 'ZeroDivisionError'>, 'SystemError': <class 'SystemError'>, 'ReferenceError': <class 'ReferenceError'>, 'BufferError': <class 'BufferError'>, 'MemoryError': <class 'MemoryError'>, 'Warning': <class 'Warning'>, 'UserWarning': <class 'UserWarning'>, 'DeprecationWarning': <class 'DeprecationWarning'>, 'PendingDeprecationWarning': <class 'PendingDeprecationWarning'>, 'SyntaxWarning': <class 'SyntaxWarning'>, 'RuntimeWarning': <class 'RuntimeWarning'>, 'FutureWarning': <class 'FutureWarning'>, 'ImportWarning': <class 'ImportWarning'>, 'UnicodeWarning': <class 'UnicodeWarning'>, 'BytesWarning': <class 'BytesWarning'>, 'ResourceWarning': <class 'ResourceWarning'>, 'ConnectionError': <class 'ConnectionError'>, 'BlockingIOError': <class 'BlockingIOError'>, 'BrokenPipeError': <class 'BrokenPipeError'>, 'ChildProcessError': <class 'ChildProcessError'>, 'ConnectionAbortedError': <class 'ConnectionAbortedError'>, 'ConnectionRefusedError': <class 'ConnectionRefusedError'>, 'ConnectionResetError': <class 'ConnectionResetError'>, 'FileExistsError': <class 'FileExistsError'>, 'FileNotFoundError': <class 'FileNotFoundError'>, 'IsADirectoryError': <class 'IsADirectoryError'>, 'NotADirectoryError': <class 'NotADirectoryError'>, 'InterruptedError': <class 'InterruptedError'>, 'PermissionError': <class 'PermissionError'>, 'ProcessLookupError': <class 'ProcessLookupError'>, 'TimeoutError': <class 'TimeoutError'>, 'open': <built-in function open>, 'quit': Use quit() or Ctrl-D (i.e. EOF) to exit, 'exit': Use exit() or Ctrl-D (i.e. EOF) to exit, 'copyright': Copyright (c) 2001-2017 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved., 'credits':     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information., 'license': Type license() to see the full license text, 'help': Type help() for interactive help, or help(object) for help about object.}, 'FunctionType': <class 'function'>, 'LambdaType': <class 'function'>, 'CodeType': <class 'code'>, 'MappingProxyType': <class 'mappingproxy'>, 'SimpleNamespace': <class 'types.SimpleNamespace'>, 'GeneratorType': <class 'generator'>, 'CoroutineType': <class 'coroutine'>, '_ag': <async_generator object _ag at 0xb71701ec>, 'AsyncGeneratorType': <class 'async_generator'>, 'MethodType': <class 'method'>, 'BuiltinFunctionType': <class 'builtin_function_or_method'>, 'BuiltinMethodType': <class 'builtin_function_or_method'>, 'ModuleType': <class 'module'>, 'TracebackType': <class 'traceback'>, 'FrameType': <class 'frame'>, 'GetSetDescriptorType': <class 'getset_descriptor'>, 'MemberDescriptorType': <class 'member_descriptor'>, 'new_class': <function new_class at 0xb71e0a04>, 'prepare_class': <function prepare_class at 0xb71e09bc>, '_calculate_meta': <function _calculate_meta at 0xb71e0a4c>, 'DynamicClassAttribute': <class 'types.DynamicClassAttribute'>, '_functools': <module 'functools' from '/home/mint/.pyenv/versions/3.6.1/lib/python3.6/functools.py'>, '_collections_abc': <module 'collections.abc' from '/home/mint/.pyenv/versions/3.6.1/lib/python3.6/collections/abc.py'>, '_GeneratorWrapper': <class 'types._GeneratorWrapper'>, 'coroutine': <function coroutine at 0xb71e0adc>, '__all__': ['FunctionType', 'LambdaType', 'CodeType', 'MappingProxyType', 'SimpleNamespace', 'GeneratorType', 'CoroutineType', 'AsyncGeneratorType', 'MethodType', 'BuiltinFunctionType', 'BuiltinMethodType', 'ModuleType', 'TracebackType', 'FrameType', 'GetSetDescriptorType', 'MemberDescriptorType', 'new_class', 'prepare_class', 'DynamicClassAttribute', 'coroutine']}
__name__
__doc__
__package__
__loader__
__spec__
__build_class__
__import__
abs
all
any
ascii
bin
callable
chr
compile
delattr
dir
divmod
eval
exec
format
getattr
globals
hasattr
hash
hex
id
input
isinstance
issubclass
iter
len
locals
max
min
next
oct
ord
pow
print
repr
round
setattr
sorted
sum
vars
None
Ellipsis
NotImplemented
False
True
bool
memoryview
bytearray
bytes
classmethod
complex
dict
enumerate
filter
float
frozenset
property
int
list
map
object
range
reversed
set
slice
staticmethod
str
super
tuple
type
zip
__debug__
BaseException
Exception
TypeError
StopAsyncIteration
StopIteration
GeneratorExit
SystemExit
KeyboardInterrupt
ImportError
ModuleNotFoundError
OSError
EnvironmentError
IOError
EOFError
RuntimeError
RecursionError
NotImplementedError
NameError
UnboundLocalError
AttributeError
SyntaxError
IndentationError
TabError
LookupError
IndexError
KeyError
ValueError
UnicodeError
UnicodeEncodeError
UnicodeDecodeError
UnicodeTranslateError
AssertionError
ArithmeticError
FloatingPointError
OverflowError
ZeroDivisionError
SystemError
ReferenceError
BufferError
MemoryError
Warning
UserWarning
DeprecationWarning
PendingDeprecationWarning
SyntaxWarning
RuntimeWarning
FutureWarning
ImportWarning
UnicodeWarning
BytesWarning
ResourceWarning
ConnectionError
BlockingIOError
BrokenPipeError
ChildProcessError
ConnectionAbortedError
ConnectionRefusedError
ConnectionResetError
FileExistsError
FileNotFoundError
IsADirectoryError
NotADirectoryError
InterruptedError
PermissionError
ProcessLookupError
TimeoutError
open
quit
exit
copyright
credits
license
help
```

