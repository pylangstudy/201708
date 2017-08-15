import difflib
print(difflib.get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy']))
import keyword
print(difflib.get_close_matches('wheel', keyword.kwlist))
print(difflib.get_close_matches('pineapple', keyword.kwlist))
print(difflib.get_close_matches('accept', keyword.kwlist))
