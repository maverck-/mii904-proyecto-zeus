#!/usr/bin/env python3
"""Comprueba el contenido portable, la pauta y las fuentes compartidas."""
from pathlib import Path
from decimal import Decimal
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

def rows(name):
    for line in (root/name).read_text().splitlines():
        if line.startswith('|'):
            yield [cell.strip() for cell in line.strip('|').split('|')]

def number(value):
    return Decimal(value.replace('.', '').replace(',', '.'))

# ESC-01: verificar operaciones y relaciones, sin validar los supuestos de entrada.
costs = {}
listed_total = None
effort_total = Decimal(0)
listed_effort = None
for cells in rows('trabajo/06_estimacion.md'):
    if re.fullmatch(r'PAQ-\d\d', cells[0]):
        o, m, p, listed = map(number, cells[1:5])
        estimate = (o + 4*m + p) / 6
        check(o <= m <= p, f'Rango de costo inválido: {cells[0]}')
        check(abs(listed-estimate) <= Decimal('0.005'), f'Tres puntos incorrectos: {cells[0]}')
        costs[cells[0]] = (o, m, p, estimate)
    elif cells[0] == 'Total' and len(cells) == 6:
        listed_total = tuple(map(number, cells[1:5]))
    elif len(cells) == 5 and re.fullmatch(r'\d+(?:,\d+)?', cells[1]):
        effort = number(cells[1]) * number(cells[2])
        check(effort == number(cells[3]), f'Esfuerzo incorrecto: {cells[0]}')
        effort_total += effort
    elif cells[0] == 'Total' and len(cells) == 5:
        listed_effort = number(cells[3])
check(len(costs) == 7, 'ESC-01 necesita siete paquetes de costo.')
if costs:
    totals = tuple(sum(row[i] for row in costs.values()) for i in range(4))
    check(listed_total is not None and all(abs(a-b) < Decimal('0.01') for a,b in zip(totals, listed_total)), 'Totales de costo incorrectos.')
    check(effort_total == listed_effort, 'Total de persona-meses incorrecto.')
    budget = {}
    for cells in rows('trabajo/06_estimacion.md'):
        if len(cells) == 3 and re.fullmatch(r'\d+,\d+', cells[1]):
            budget[cells[0]] = number(cells[1])
    central = totals[3]
    reserve = budget['Reserva nominal']
    envelope = budget['Sobre de trabajo']
    cap = budget['Techo preliminar del caso']
    check(central == budget['Central de paquetes'], 'Central distinto del total de tres puntos.')
    check(central+reserve == budget['Central más reserva'], 'Central más reserva incorrecto.')
    check(envelope-central-reserve == budget['Margen no asignado del sobre'], 'Margen del sobre incorrecto.')
    check(cap-envelope == budget['Diferencia techo/sobre'], 'Diferencia techo/sobre incorrecta.')
    check(totals[2] == budget['Adverso de partidas'] and totals[2]+reserve == budget['Adverso más reserva nominal'], 'Adverso incorrecto.')

priority_weights = {}
scores = {}
for cells in rows('trabajo/05_priorizacion.md'):
    if len(cells) == 3 and re.fullmatch(r'\d+%', cells[1]):
        priority_weights[cells[0]] = Decimal(cells[1].strip('%'))
    elif len(cells) == 9 and re.fullmatch(r'CAP-\d\d', cells[0]):
        scores[cells[0]] = cells
check(len(priority_weights) == 7 and sum(priority_weights.values()) == 100, 'Pesos de priorización deben sumar 100%.')
for ident, cells in scores.items():
    notes = list(map(number, cells[1:8]))
    check(all(1 <= note <= 5 for note in notes), f'Nota fuera de escala: {ident}')
    expected_score = sum(note*priority_weights[key] for note,key in zip(notes,['V','U','D','R','I','C','K'])) / 100
    check(expected_score == number(cells[8]), f'Puntaje incorrecto: {ident}')
check(len(scores) == 6, 'Se esperan seis capacidades puntuadas; las otras dos son transversales obligatorias.')

backlog = (root/'trabajo/04_alcance_y_backlog.md').read_text()
assumptions = (root/'registros/acuerdos_y_supuestos.md').read_text()
for path in (root/'trabajo').glob('[0-9][0-9]_*.md'):
    for ident in set(re.findall(r'\bSUP-\d\d\b', path.read_text())):
        check(ident in assumptions, f'Supuesto sin definición: {ident} en {path.name}')
    for ident in set(re.findall(r'\b(?:CAP|PAQ)-\d\d\b', path.read_text())):
        check(ident in backlog, f'Capacidad/paquete sin definición: {ident} en {path.name}')
for error in errors:
    print('ERROR:', error)
if errors:
    sys.exit(1)
print(f'OK: {len(paths)} archivos, siete entregables, pauta 100%, {transcripts} transcripciones y {segments} segmentos.')
print('OK: fuentes y enlaces verificados; sin rutas personales, contactos o capturas detectados.')
print('OK: operaciones de costo, esfuerzo, priorización y referencias ESC-01; falta revisión de los supuestos.')
