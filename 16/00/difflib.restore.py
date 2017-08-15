#!python3.6
import difflib
a = 'one\ntwo\nthree\n'.splitlines(keepends=True)
b = 'ore\ntree\nemu\n'.splitlines(keepends=True)
print(a); print(b);
diff = difflib.ndiff(a,b)
diff = list(diff)
print(''.join(difflib.restore(diff, 1)))
print(''.join(difflib.restore(diff, 2)))
print('\n\n')

#keepends=Trueしないと改行がrestore()できない。
a = 'one\ntwo\nthree\n'.splitlines()
b = 'ore\ntree\nemu\n'.splitlines()
print(a); print(b);
diff = difflib.ndiff(a,b)
diff = list(diff)
print(''.join(difflib.restore(diff, 1)))
print(''.join(difflib.restore(diff, 2)))
