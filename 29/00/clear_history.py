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
    readline.clear_history()#クリアするので保存されない
    readline.append_history_file(1, history_file)

