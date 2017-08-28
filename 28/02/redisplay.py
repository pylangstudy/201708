import readline

#get_line_buffer()はset_completer()の引数に渡すことで価値があるもの？
#http://ja.pymotw.com/2/readline/#id3

#redisplay()の使いどころがわからない。あってもなくても同じに見える。
def complete(text, state):
    readline.insert_text('AAA')
    print(f'state:{state}, text:{text}, readline.get_line_buffer():{readline.get_line_buffer()}')
    readline.redisplay()
readline.set_completer(complete)
readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')

while True:
    readline.insert_text('BBB')
    line = input('Prompt ("stop" to quit): ')
    if line == 'stop':
        break
    print('ENTERED: "%s"' % line)
    print('readline.get_line_buffer():', readline.get_line_buffer())
    readline.redisplay()


