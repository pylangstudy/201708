import readline

class SimpleCompleter:
    def __init__(self, options): self.options = sorted(options)
    def complete(self, text, state):
        response = None
        if state == 0:
            # このテキストは初めてなのでマッチリストを作成する
            if text:
                self.matches = [s 
                                for s in self.options
                                if s and s.startswith(text)]
#                print('%s matches: %s', repr(text), self.matches)
            else:
                self.matches = self.options[:]
#                print('(empty input) matches: %s', self.matches)
        # たくさんある場合、マッチリストから state 番目の値を返す
#        print(f'text={text}, state={state}')
        try: response = self.matches[state]
        except IndexError: response = None
#        print('complete(%s, %s) => %s', repr(text), state, repr(response))
        return response

def input_loop():
    line = ''
    while line != 'stop':
        line = input('Prompt ("stop" to quit): ')
        print('Dispatch %s' % line)

commands = ['start', 'stop', 'list', 'print']
print('commands:', commands)
# 補完関数を登録する
readline.set_completer(SimpleCompleter(commands).complete)
print(readline.get_completer())

# 補完に tab キーを使用する
readline.parse_and_bind('tab: complete')

# ユーザへテキストを表示する
input_loop()
