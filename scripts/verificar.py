#!/usr/bin/env python3
"""Comprueba el contenido portable, la pauta y las fuentes compartidas."""
from pathlib import Path
import hashlib
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []

def check(ok, message):
    if not ok:
        errors.append(message)

paths = [p for p in root.rglob('*') if p.is_file() and not ({'.git', 'build', 'local'} & set(p.relative_to(root).parts))]
for path in paths:
    relative = path.relative_to(root)
    check(path.suffix.lower() not in {'.png', '.jpg', '.jpeg', '.webp', '.html', '.mp4'}, f'Revisar inclusión no prevista: {relative}')
    if path.suffix not in {'.md', '.typ', '.json'}:
        continue
    text = path.read_text()
    check(not re.search(r'/Users/|[A-Za-z]:\\Users\\', text), f'Ruta personal en {relative}')
    check(not re.search(r'\+56\s*9|[\w.+-]+@gmail\.com|codex-clipboard-|whatsapp', text, re.I), f'Contacto o material privado en {relative}')
    if path.suffix == '.md':
        if relative.parts[0] != 'transcripciones':
            check('\u2014' not in text, f'Revisar puntuación en {relative}')
        for m in re.finditer(r'\]\((?:<([^>]+)>|([^()]+))\)', text):
            target = m.group(1) or m.group(2)
            if re.match(r'[a-zA-Z]+://', target) or target.startswith('#'):
                continue
            target = target.split('#', 1)[0]
            check(not Path(target).is_absolute() and (path.parent/target).exists(), f'Enlace local inválido en {relative}: {target}')

weights = []
for line in (root/'insumos/pauta.md').read_text().splitlines():
    if line.startswith('|'):
        cells = [x.strip() for x in line.strip('|').split('|')]
        if len(cells) > 1 and re.fullmatch(r'\d+%', cells[1]):
            weights.append(int(cells[1].strip('%')))
check(len(weights) == 8 and sum(weights) == 100, 'La pauta debe conservar ocho criterios y 100%.')

source = root/'insumos/enunciado-zeus-etapa1.pdf'
expected = re.search(r'`([0-9a-f]{64})`', (root/'insumos/README.md').read_text()).group(1)
check(hashlib.sha256(source.read_bytes()).hexdigest() == expected, 'El enunciado no coincide con el hash registrado.')

transcripts = 0
segments = 0
for line in (root/'transcripciones/README.md').read_text().splitlines():
    if not line.startswith('|'):
        continue
    cells = [x.strip() for x in line.strip('|').split('|')]
    if len(cells) != 6 or not re.fullmatch(r'\d+', cells[3]):
        continue
    name = re.search(r'\]\(([^)]+)\)', cells[2]).group(1)
    path = root/'transcripciones'/name
    stamps = re.findall(r'^\[([\d:]+)\]', path.read_text(), re.M)
    check(len(stamps) == int(cells[3]) and stamps[-1] == cells[4], f'Segmentos o tiempo final cambiaron: {name}')
    digest = cells[5].strip('`')
    check(hashlib.sha256(path.read_bytes()).hexdigest() == digest, f'Hash de transcripción distinto: {name}')
    transcripts += 1
    segments += len(stamps)
check(transcripts == 4, 'Se esperan cuatro partes disponibles de las clases 1 y 2.')
check(len(list((root/'trabajo').glob('[0-9][0-9]_*.md'))) == 7, 'Se esperan siete documentos de entregables.')
for error in errors:
    print('ERROR:', error)
if errors:
    sys.exit(1)
print(f'OK: {len(paths)} archivos, siete entregables, pauta 100%, {transcripts} transcripciones y {segments} segmentos.')
print('OK: fuentes y enlaces verificados; sin rutas personales, contactos o capturas detectados.')
