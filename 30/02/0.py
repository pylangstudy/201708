#https://www.programcreek.com/python/example/1102/rlcompleter.Completer
import rlcompleter
import readline
import code
class MyCompleter(rlcompleter.Completer):
    def __init__(self,on_kill=None,*args,**kw):
        code.InteractiveConsole.__init__(self,*args,**kw)
        self.code_to_run = None
        self.ready = threading.Condition()
        self._kill = False
        if on_kill is None:
            on_kill = []
        # Check that all things to kill are callable:
        for _ in on_kill:
            if not callable(_):
    #            raise TypeError,'on_kill must be a list of callables'
                raise TypeError('on_kill must be a list of callables')
        self.on_kill = on_kill
        # Set up tab-completer
        if has_readline:
            import rlcompleter
            try:  # this form only works with python 2.3
                self.completer = rlcompleter.Completer(self.locals)
            except: # simpler for py2.2
                self.completer = rlcompleter.Completer()

            readline.set_completer(self.completer.complete)
            # Use tab for completions
            readline.parse_and_bind('tab: complete')
            # This forces readline to automatically print the above list when tab
            # completion is set to 'complete'.
            readline.parse_and_bind('set show-all-if-ambiguous on')
            # Bindings for incremental searches in the history. These searches
            # use the string typed so far on the command line and search
            # anything in the previous input history containing them.
            readline.parse_and_bind('"\C-r": reverse-search-history')
            readline.parse_and_bind('"\C-s": forward-search-history')

c = MyCompleter()
while True:
    line = input('Prompt ("stop" to quit): ')
    if line == 'stop':
        break
    print('ENTERED: "%s"' % line)
    readline.append_history_file(1, history_file)

#AttributeError: 'MyCompleter' object has no attribute 'resetbuffer'
