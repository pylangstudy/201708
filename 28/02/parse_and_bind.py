import readline

#text = 'parse text.'
#print(text)
#print(readline.parse_and_bind(text))

readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')
while True:
    line = input('Prompt ("stop" to quit): ')
#    line = raw_input('Prompt ("stop" to quit): ')
    if line == 'stop':
        break
    print('ENTERED: "%s"' % line)
