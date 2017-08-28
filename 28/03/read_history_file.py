import readline

history_file = 'history_file.txt'
readline.read_history_file(history_file)

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
    readline.write_history_file(history_file)

