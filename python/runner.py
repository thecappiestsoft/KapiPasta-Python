import sys, io, json

class _Tee(io.TextIOBase):
    def __init__(self):
        self.disp = []
        self.out = []
    def write(self, t):
        t = str(t)
        self.n = getattr(self, 'n', 0) + len(t)
        if self.n > 100000:
            raise RuntimeError('Za dużo wypisanego tekstu / Too much output - infinite loop?')
        self.disp.append(t)
        self.out.append(t)
        return len(t)
    def flush(self):
        pass

def _find_line(tb):
    line = None
    while tb is not None:
        if tb.tb_frame.f_code.co_filename == '<kod>':
            line = tb.tb_lineno
        tb = tb.tb_next
    return line

def _run(code, stdin='', setup='', check='', limit=0):
    tee = _Tee()
    old = sys.stdout
    sys.stdout = tee
    lines = stdin.split('\n') if stdin else []
    pos = [0]
    def _inp(prompt=''):
        if pos[0] >= len(lines):
            raise EOFError('input() nie ma już danych - wpisz je w polu "Dane wejściowe"')
        v = lines[pos[0]]
        pos[0] += 1
        tee.disp.append(str(prompt) + v + '\n')
        return v
    ns = {'__name__': '__main__', 'input': _inp, '__src': code}
    res = {'err': None, 'etype': None, 'line': None, 'checkfail': None}
    cnt = [0]
    def _lt(frame, ev, arg):
        if ev == 'line':
            cnt[0] += 1
            if cnt[0] > limit:
                raise TimeoutError('Program działa za długo - może pętla nieskończona? / Program runs too long - infinite loop?')
        return _lt
    def _gt(frame, ev, arg):
        return _lt if frame.f_code.co_filename == '<kod>' else None
    if limit:
        sys.settrace(_gt)
    try:
        if setup:
            exec(setup, ns)
        try:
            exec(compile(code, '<kod>', 'exec'), ns)
        except SyntaxError as e:
            res['etype'] = type(e).__name__
            res['line'] = e.lineno
            res['err'] = type(e).__name__ + ': ' + str(e.msg)
        except RecursionError as e:
            res['etype'] = 'RecursionError'
            res['line'] = None
            res['err'] = 'RecursionError: ' + str(e)
        except BaseException as e:
            res['etype'] = type(e).__name__
            res['line'] = _find_line(e.__traceback__)
            res['err'] = type(e).__name__ + ': ' + str(e)
        if res['err'] is None and check:
            ns['__out'] = ''.join(tee.out)
            sys.stdout = io.StringIO()
            try:
                exec(check, ns)
            except AssertionError as e:
                res['checkfail'] = str(e) or 'Wynik nie zgadza się z oczekiwanym.'
            except BaseException as e:
                res['checkfail'] = type(e).__name__ + ': ' + str(e)
    finally:
        sys.settrace(None)
        sys.stdout = old
    res['disp'] = ''.join(tee.disp)
    res['out'] = ''.join(tee.out)
    return res

def _run_json(code, stdin='', setup='', check=''):
    return json.dumps(_run(code, stdin, setup, check, 2000000))
