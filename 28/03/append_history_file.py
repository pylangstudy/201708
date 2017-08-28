"""
import readline

history_file = 'history_file.txt'

#def complete(text, state):
#    print(f'state:{state}, text:{text}, readline.get_line_buffer():{readline.get_line_buffer()}')
#readline.set_completer(complete)
readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')

while True:
    line = input('Prompt ("stop" to quit): ')
    if line == 'stop':
        break
    print('ENTERED: "%s"' % line)
    #TypeError: an integer is required (got type str)
    readline.append_history_file(0, history_file)
"""


import atexit
import os
import readline
history_file = 'history_file.txt'
readline.set_history_length(1000)
readline.read_history_file(history_file)
print(f'readline.get_history_length():{readline.get_history_length()}')


readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')
while True:
    line = input('Prompt ("stop" to quit): ')
    if line == 'stop':
        break
    print('ENTERED: "%s"' % line)
    #TypeError: an integer is required (got type str)
#    readline.append_history_file(0, history_file)
    readline.append_history_file(1, history_file)

"""
#histfile = os.path.join(os.path.expanduser("~"), ".python_history")
history_file = 'history_file.txt'
try:
    readline.read_history_file(history_file)
    h_len = readline.get_history_length()
    print(f'h_len:{h_len}')
except FileNotFoundError:
    open(history_file, 'wb').close()
    h_len = 0
def save(prev_h_len, history_file):
    print(f'prev_h_len:{prev_h_len}, history_file:{history_file}')
    new_h_len = readline.get_history_length()
    readline.set_history_length(1000)
    readline.append_history_file(new_h_len - prev_h_len, history_file)
atexit.register(save, h_len, history_file)
"""

