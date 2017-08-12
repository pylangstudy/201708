import re

#pattern = r'^ab'
pattern = r'ab'
pattern1 = re.compile(pattern)
for target in ['abc', 'ABCabc']: print(pattern1.split(target))
print()
for target in ['abc', 'ABCabc']: print(pattern1.split(target, re.IGNORECASE))#全部Noneになる
print()
for target in ['abc', 'ABCabc']: print(re.split(pattern, target))
print()
for target in ['abc', 'ABCabc']: print(re.split(pattern, target, re.IGNORECASE))
print()
print(re.split('\W+', 'Words, words, words.'))
print(re.split('(\W+)', 'Words, words, words.'))
print(re.split('\W+', 'Words, words, words.', 1))
print(re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE))
print()
print(re.split('x*', 'axbc'))#FutureWarning: split() requires a non-empty pattern match.
print()
print(re.split("^$", "foo\n\nbar\n", flags=re.M))#ValueError: split() requires a non-empty pattern match.
