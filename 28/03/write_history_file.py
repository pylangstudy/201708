import readline

#get_line_buffer()はset_completer()の引数に渡すことで価値があるもの？
#http://ja.pymotw.com/2/readline/#id3

#TABキー押下すると以下のprint文が実行された。
#get_line_buffer()はset_completer()時なら文字列を返すが、入力完了後だと空文字となる。
#しかしset_completer()時は引数textでget_line_buffer()の値を受け取れているように見える。get_line_buffer()を使う意義がない。一体いつどんな場面で使うべきなのか謎。

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
    readline.write_history_file(history_file)

