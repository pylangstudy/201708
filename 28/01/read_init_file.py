import readline

readline.read_init_file('myreadline.rc')
while True:
    line = input('Prompt ("stop" to quit): ')
    if line == 'stop': break
    print('ENTERED: "%s"' % line)
