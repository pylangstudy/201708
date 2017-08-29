import atexit
import os
import readline

#histfile = os.path.join(os.path.expanduser("~"), ".python_history")
histfile = os.path.join('history_file.txt')
try:
    readline.read_history_file(histfile)
    readline.set_history_length(1000)
except FileNotFoundError: pass
atexit.register(readline.write_history_file, histfile)
