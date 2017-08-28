import readline
import datetime
readline.set_startup_hook(lambda: print('===== set_startup_hook ====='))
readline.set_pre_input_hook(lambda: print('----- set_pre_input_hook -----'))
history_file = 'history_file.txt'
readline.set_history_length(1000)
readline.read_history_file(history_file)
print(f'readline.get_history_length():{readline.get_history_length()}')

#ファイル保存はせず、履歴に追加する
for i in range(5): readline.add_history(f'{datetime.datetime.now():%Y-%m-%d %H:%M:%S.%f}')

readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')
while True:
    line = input('Prompt ("stop" to quit): ')
    if line == 'stop':
        break
    print('ENTERED: "%s"' % line)
    readline.append_history_file(1, history_file)

    index = readline.get_current_history_length() - 1
#    readline.replace_history_item(index, f'{datetime.datetime.now():%Y-%m-%d %H:%M:%S.%f}' + readline.get_history_item(index))#入力直後のを置き換えたかったのに、その1つ前のになってしまう……
    readline.replace_history_item(index, f'{datetime.datetime.now():%Y-%m-%d %H:%M:%S.%f}\t' + line)
