#!/usr/bin/env python3
"""Build & verify KapiPasta course content.

Reads lessons from content/pl/*.py (full Polish course) and content/en/*.py
(English overrides merged onto the Polish structure), RUNS every example,
quiz, fill-in, bug and solution with the same Python runner the browser uses,
and writes js/data/course.js.

Usage:  python3 tools/build.py          # verify + build
        python3 tools/build.py --check  # verify only (exit 1 on problems)
"""
import json, os, signal, sys, tempfile, copy, glob, importlib.util
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'python'))
sys.setrecursionlimit(3000)
from runner import _run

def load(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

PL = []
EXTRA_PL = {}
for f in sorted(glob.glob(os.path.join(ROOT, 'content', 'pl', '*.py'))):
    m = load(f)
    PL += getattr(m, 'CH', [])
    for k, v in getattr(m, 'EXTRA', {}).items():
        EXTRA_PL.setdefault(k, []).extend(v)
def resolve(x, i):
    """Bilingual fields: ('polski', 'English') -> pick language i (0 = PL, 1 = EN)."""
    if isinstance(x, tuple) and len(x) == 2 and all(isinstance(v, str) for v in x):
        return x[i]
    if isinstance(x, dict):
        return {k: resolve(v, i) for k, v in x.items()}
    if isinstance(x, list):
        return [resolve(v, i) for v in x]
    return x

BOTH = {}
for f in sorted(glob.glob(os.path.join(ROOT, 'content', 'both', '*.py'))):
    for k, v in getattr(load(f), 'EXTRA2', {}).items():
        BOTH.setdefault(k, []).extend(v)
for k, v in BOTH.items():
    EXTRA_PL.setdefault(k, []).extend(resolve(copy.deepcopy(v), 0))
_ids = {L['id']: L for ch in PL for L in ch['lessons']}
for k, v in EXTRA_PL.items():
    assert k in _ids, ('EXTRA: unknown lesson id', k)
    _ids[k]['tasks'].extend(v)
problems = []

def norm(s):
    lines = [l.rstrip() for l in s.replace('\r', '').split('\n')]
    while lines and lines[-1] == '':
        lines.pop()
    return '\n'.join(lines)

class TO(Exception): pass
def _h(*a): raise TO()
HAS_ALARM = hasattr(signal, 'SIGALRM')
if HAS_ALARM:
    signal.signal(signal.SIGALRM, _h)

def run(code, stdin='', setup='', check=''):
    d = tempfile.mkdtemp(); old = os.getcwd(); os.chdir(d)
    if HAS_ALARM: signal.alarm(3)
    try:
        return _run(code, stdin, setup, check, 2000000)
    except TO:
        return {'timeout': True, 'err': 'TIMEOUT', 'etype': 'TIMEOUT', 'line': None, 'out': '', 'disp': '', 'checkfail': None}
    finally:
        if HAS_ALARM: signal.alarm(0)
        os.chdir(old)

CUR=['pl']
def P(where, msg):
    problems.append(f'[{CUR[0]}] {where}: {msg}')

def verify(CH, lang):
    global ntask
    for ch in CH:
        for L in ch['lessons']:
            c = [sum(1 for t in L['tasks'] if t['l'] == k) for k in (1, 2, 3)]
            if c != [6, 6, 6]:
                P(L['id'], f'levels must be 6/6/6 (got {c[0]}/{c[1]}/{c[2]})')
    for ch in CH:
        for L in ch['lessons']:
            for i, ex in enumerate(L['ex']):
                r = run(ex['code'], ex.get('inp', ''))
                sc = ex['scene']
                if r['err'] and not (sc['s'] == 'err' and not sc.get('caught')):
                    P(f"{L['id']} ex{i}", 'example error ' + r['err'])
                ex['out'] = norm(r['disp'])
                if r['err']:
                    ex['err'] = r['err']; ex['errline'] = r['line']; ex['etype'] = r['etype']
            for j, t in enumerate(L['tasks']):
                ntask += 1
                w = f"{L['id']} t{j} ({t['t']})"
                t['id'] = f"{L['id']}-{j}"
                assert t['l'] in (1, 2, 3)
                if t['t'] == 'quiz':
                    assert 0 <= t['a'] < len(t['opts'])
                    if len(set(t['opts'])) != len(t['opts']): P(w, 'duplicate opts')
                    if t.get('out'):
                        r = run(t['code'], t.get('inp', ''))
                        o = norm(r['out'])
                        if r['err']: P(w, 'quiz code error ' + r['err'])
                        if o != norm(t['opts'][t['a']]): P(w, f'answer mismatch: got {o!r} vs {t["opts"][t["a"]]!r}')
                        for k, op in enumerate(t['opts']):
                            if k != t['a'] and norm(op) == o: P(w, 'another option also correct')
                    if t.get('err'):
                        r = run(t['code'])
                        if r['etype'] != t['opts'][t['a']].split(':')[0]: P(w, f"err mismatch {r['etype']}")
                elif t['t'] == 'fill':
                    parts = t['code'].split('___')
                    if len(parts) - 1 != len(t['ans']): P(w, 'blank count')
                    code = parts[0]
                    for k, a in enumerate(t['ans']):
                        code += a[0] + parts[k + 1]
                    if t.get('run', True):
                        r = run(code, t.get('inp', ''))
                        if r['err']: P(w, 'fill error ' + r['err'])
                        if 'expect' in t and norm(r['out']) != t['expect']: P(w, f"fill expect {r['out']!r}")
                elif t['t'] == 'bug':
                    nl = len(t['code'].split('\n'))
                    assert 0 <= t['line'] < nl, w
                    if t.get('noerr'):
                        if 'while' in t['code'] and 'n += 1' in t['code']:
                            pass
                        else:
                            r = run(t['code'], t.get('inp', ''))
                            if r['err']: P(w, 'noerr but error ' + r['err'])
                            t['got'] = norm(r['out'])
                    else:
                        r = run(t['code'], t.get('inp', ''))
                        if not r['err']: P(w, 'expected error, none')
                        else:
                            t['err'] = r['err']; t['errline'] = r['line']
                            if not t.get('cause') and r['line'] != t['line'] + 1: P(w, f"error line {r['line']} vs {t['line'] + 1}")
                elif t['t'] == 'code':
                    for tc in t['tests']:
                        if tc.get('o') == '@':   # expected output computed from the model solution
                            tc['o'] = norm(run(t['sol'], tc['i'], t.get('setup', ''))['out'])
                    tests = t['tests'] or [dict(i='', o=None)]
                    for tc in tests:
                        r = run(t['sol'], tc['i'], t.get('setup', ''), t.get('check', ''))
                        if r['err'] or r['checkfail']: P(w, f"sol fail {r['err']} {r['checkfail']}")
                        if tc['o'] is not None and norm(r['out']) != norm(tc['o']): P(w, f"sol out {r['out']!r} vs {tc['o']!r}")
                    # starter must not pass
                    ok = True
                    for tc in tests:
                        r = run(t['start'], tc['i'], t.get('setup', ''), t.get('check', ''))
                        if r['err'] or r['checkfail'] or (tc['o'] is not None and norm(r['out']) != norm(tc['o'])): ok = False
                    if ok: P(w, 'starter passes!')
                    if not t['tests'] and not t.get('check'): P(w, 'no tests no check')
                else:
                    P(w, 'unknown type')



def merge(pl, en):
    out = copy.deepcopy(pl)
    for ch in out:
        e = en['chapters'][ch['id']]; ch['name'] = e['name']; ch['topic'] = e['topic']
        for L in ch['lessons']:
            el = en['lessons'][L['id']]
            for k in ('title', 'theory', 'more'):
                if k in el: L[k] = el[k]
            assert len(el['ex']) == len(L['ex']), ('ex count', L['id'])
            for ex, ee in zip(L['ex'], el['ex']): ex.update(ee)
            assert len(el['tasks']) == len(L['tasks']), ('task count', L['id'], len(el['tasks']), len(L['tasks']))
            for t, et in zip(L['tasks'], el['tasks']): t.update(et)
    return out

PLc = copy.deepcopy(PL)
ntask = 0
CHS = {'pl': PL}
EN = {'chapters': {}, 'lessons': {}}
for f in sorted(glob.glob(os.path.join(ROOT, 'content', 'en', '*.py'))):
    m = load(f)
    EN['chapters'].update(getattr(m, 'CHAPTERS', {})); EN['lessons'].update(getattr(m, 'LESSONS', {}))
    for k, v in getattr(m, 'EXTRA', {}).items():
        EN.setdefault('extra', {}).setdefault(k, []).extend(v)
for k, v in BOTH.items():
    EN.setdefault('extra', {}).setdefault(k, []).extend(resolve(copy.deepcopy(v), 1))
for k, v in EN.get('extra', {}).items():
    EN['lessons'][k]['tasks'] = EN['lessons'][k]['tasks'] + v
if EN['lessons'] and not os.environ.get('SKIP_EN'):
    CHS['en'] = merge(PLc, EN)
for lang, CH in CHS.items():
    ntask = 0
    CUR[0] = lang; verify(CH, lang)
    print(lang, 'chapters', len(CH), 'lessons', sum(len(c['lessons']) for c in CH), 'tasks', ntask)
import re
PLW = re.compile(r'[ąćęłńóśźżĄĆĘŁŃÓŚŹŻ]|\b(Błąd|Bład|nic|brak|owoc\w*|arbuz\w*|imie|wiek|liczb\w*|lubi|ma |jest|zadanie|pętl\w*|Wypisz|Wczytaj|tekst\w*|zostaje|suma|ile|lista|slowa|wynik|klasa|Linia|Popraw|pierwsza|szukaj|plecak|kolejka|mandaryn\w*|zwierze|nogi|cena|punkty|silnia|odliczaj|potega|nwd)\b')
def scan(o, path):
    if isinstance(o, dict):
        for k, v in o.items():
            if k in ('id', 'err', 'got', 'out', 'etype', 's', 'hl'): continue
            scan(v, path + '.' + k)
    elif isinstance(o, list):
        for i, v in enumerate(o): scan(v, path + f'[{i}]')
    elif isinstance(o, str):
        m = PLW.search(o)
        if m: print('PL?', path, '|', m.group(0), '|', o[:70].replace('\n', '⏎'))
if 'en' in CHS:  # warn about leftover Polish in the English version
    for ch in CHS['en']:
        for L in ch['lessons']:
            scan({k: v for k, v in L.items() if k != 'id'}, L['id'])

print('\n'.join(problems) or 'OK - no problems')
if problems:
    sys.exit(1)
if '--check' not in sys.argv:
    runner_src = open(os.path.join(ROOT, 'python', 'runner.py'), encoding='utf-8').read()
    out = os.path.join(ROOT, 'js', 'data', 'course.js')
    with open(out, 'w', encoding='utf-8') as f:
        f.write('/* GENERATED by tools/build.py - do not edit by hand. Edit content/ and rebuild. */\n')
        f.write('window.COURSE=' + json.dumps(CHS, ensure_ascii=False) + ';\n')
        f.write('window.RUNNER=' + json.dumps(runner_src) + ';\n')
    print('written', os.path.relpath(out, ROOT))
