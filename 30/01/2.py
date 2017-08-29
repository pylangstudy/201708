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




import atexit
import code
import os
import readline

class HistoryConsole(code.InteractiveConsole):
    def __init__(self, locals=None, filename="<console>",
                 histfile=os.path.expanduser("~/.console-history")):
        code.InteractiveConsole.__init__(self, locals, filename)
        self.init_history(histfile)

    def init_history(self, histfile):
        readline.parse_and_bind("tab: complete")
        readline.parse_and_bind('set editing-mode vi')
        if hasattr(readline, "read_history_file"):
            try: readline.read_history_file(histfile)
            except FileNotFoundError: pass
            atexit.register(self.save_history, histfile)

    def save_history(self, histfile):
        readline.set_history_length(1000)
        readline.write_history_file(histfile)

histfile = os.path.join('history_file.txt')
hc = HistoryConsole(histfile=histfile)
while True:
    line = input('Prompt ("stop" to quit): ')
    if line == 'stop': break
    print('ENTERED: "%s"' % line)

