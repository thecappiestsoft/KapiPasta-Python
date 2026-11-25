#!/usr/bin/env python3
"""Bundle the whole app into ONE self-contained HTML file: dist/kapipasta.html
(useful for sharing as a single file or hosting where only one file is allowed).

Usage: python3 tools/build.py && python3 tools/bundle.py
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()

def read(rel):
    return open(os.path.join(ROOT, rel), encoding='utf-8').read()

html = re.sub(r'<link rel="stylesheet" href="([^"]+)">', lambda m: '<style>\n' + read(m.group(1)) + '\n</style>', html)
html = re.sub(r'<script src="([^"]+)"></script>', lambda m: '<script>\n' + read(m.group(1)).replace('</script', '<\\/script') + '\n</script>', html)

os.makedirs(os.path.join(ROOT, 'dist'), exist_ok=True)
out = os.path.join(ROOT, 'dist', 'kapipasta.html')
open(out, 'w', encoding='utf-8').write(html)
print('written', os.path.relpath(out, ROOT), f'{len(html) // 1024} KB')
