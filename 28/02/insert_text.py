import readline

#get_line_buffer()はset_completer()の引数に渡すことで価値があるもの？
#http://ja.pymotw.com/2/readline/#id3

#TABキー押下するとinsert_text()が実行された。入力完了後だと挿入されない。
#おそらく入力補完時の挿入用関数なのだろう。
def complete(text, state):
    readline.insert_text('AAA')
    print(f'state:{state}, text:{text}, readline.get_line_buffer():{readline.get_line_buffer()}')
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


