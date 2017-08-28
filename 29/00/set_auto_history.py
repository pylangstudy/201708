import readline
import datetime

#readline.set_auto_history(False)#add_history()自動呼出を無効にする

history_file = 'history_file.txt'
readline.set_history_length(1000)
readline.read_history_file(history_file)
print(f'readline.get_history_length():{readline.get_history_length()}')

for i in range(5): readline.add_history(f'{datetime.datetime.now():%Y-%m-%d %H:%M:%S.%f}')

readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')
while True:
    line = input('Prompt ("stop" to quit): ')
    if line == 'stop':
        break
    print('ENTERED: "%s"' % line)

#    index = readline.get_current_history_length() - 1
#    readline.replace_history_item(index, f'{datetime.datetime.now():%Y-%m-%d %H:%M:%S.%f}' + readline.get_history_item(index))#入力直後のを置き換えたかったのに、その1つ前のになってしまう……
#    readline.replace_history_item(index, f'{datetime.datetime.now():%Y-%m-%d %H:%M:%S.%f}\t' + line)

    readline.add_history(f'{datetime.datetime.now():%Y-%m-%d %H:%M:%S.%f}\t' + line)
    readline.append_history_file(1, history_file)

