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

# ESC-02: comprobar rangos disponibles sin presentar pendientes como calculados.
costs = {}
pending_costs = []
package_rows = list(c for c in rows('trabajo/06_estimacion.md') if re.fullmatch(r'PAQ-\d\d', c[0]))
check(len(package_rows) == 7, 'Se esperan siete paquetes de estimación.')
for cells in package_rows:
    check(len(cells) == 7, f'Columnas de estimación incorrectas: {cells[0]}')
    if len(cells) != 7:
        continue
    values = cells[2:6]
    if values == ['Pendiente'] * 4:
        pending_costs.append(cells[0])
        continue
    valid = all(re.fullmatch(r'\d+(?:\.\d{3})*(?:,\d+)?', v) for v in values)
    check(valid, f'Completar O/M/P/E o marcar todos Pendiente: {cells[0]}')
    if not valid:
        continue
    o, m, p, listed = map(number, values)
    expected_cost = (o + 4*m + p) / 6
    check(o <= m <= p, f'Rango de costo inválido: {cells[0]}')
    check(abs(listed-expected_cost) <= Decimal('0.005'), f'Tres puntos incorrectos: {cells[0]}')
    costs[cells[0]] = (o, m, p, expected_cost)

priority_weights = {}
scores = {}
pending_scores = []
for cells in rows('trabajo/05_priorizacion.md'):
    if len(cells) == 3 and re.fullmatch(r'\d+%', cells[1]):
        priority_weights[cells[0]] = Decimal(cells[1].strip('%'))
    elif len(cells) == 9 and re.fullmatch(r'CAP-\d\d', cells[0]):
        if cells[1:] == ['Pendiente'] * 8:
            pending_scores.append(cells[0])
        else:
            scores[cells[0]] = cells
check(len(priority_weights) == 7 and sum(priority_weights.values()) == 100, 'Pesos de priorización deben sumar 100%.')
for ident, cells in scores.items():
    notes = list(map(number, cells[1:8]))
    check(all(1 <= note <= 5 for note in notes), f'Nota fuera de escala: {ident}')
    expected_score = sum(note*priority_weights[key] for note,key in zip(notes,['V','U','D','R','I','C','K'])) / 100
    check(expected_score == number(cells[8]), f'Puntaje incorrecto: {ident}')
check(len(scores) + len(pending_scores) == 7, 'Se esperan siete capacidades priorizables; otras dos son transversales obligatorias.')

backlog = (root/'trabajo/04_alcance_y_backlog.md').read_text()
assumptions = (root/'registros/acuerdos_y_supuestos.md').read_text()
for path in (root/'trabajo').glob('[0-9][0-9]_*.md'):
    for ident in set(re.findall(r'\bSUP-\d\d\b', path.read_text())):
        check(ident in assumptions, f'Supuesto sin definición: {ident} en {path.name}')
    for ident in set(re.findall(r'\b(?:CAP|PAQ)-\d\d\b', path.read_text())):
        check(ident in backlog, f'Capacidad/paquete sin definición: {ident} en {path.name}')
# Comprobar las cantidades del roadmap; no acredita capacidad de despliegue.
accumulated = 0
waves = []
for cells in rows('trabajo/07_roadmap.md'):
    if len(cells) == 5 and (cells[0] == 'Piloto' or re.fullmatch(r'O[1-4]', cells[0])):
        valid = cells[2].isdigit() and cells[3].isdigit()
        check(valid, f'Cantidades de ola inválidas: {cells[0]}')
        if valid:
            accumulated += int(cells[2])
            check(accumulated == int(cells[3]), f'Acumulado incorrecto: {cells[0]}')
            waves.append(int(cells[2]))
check(len(waves) == 5 and accumulated == 68 and sum(waves[1:]) == 58, 'Revisar cobertura piloto/olas y objetivo 68.')

members = [cells[0] for cells in rows('EQUIPO.md') if cells[0] not in {'Integrante', '---'}]
check(len(members) == 4 and len(set(members)) == 4, 'La nómina activa debe contener cuatro integrantes distintos.')

# El archivo recibido es fuente, no la versión común editable.
source_digest = re.search(r'SHA-256 del avance preservado: `([0-9a-f]{64})`', (root/'insumos/README.md').read_text())
check(source_digest is not None, 'Falta hash del avance recibido.')
if source_digest:
    check(hashlib.sha256((root/'insumos/avance_equipo_2026-10-21.md').read_bytes()).hexdigest() == source_digest.group(1), 'El avance preservado cambió; editar la integración en trabajo/.')

for error in errors:
    print('ERROR:', error)
if errors:
    sys.exit(1)
print(f'OK: {len(paths)} archivos, siete entregables, pauta 100%, {transcripts} transcripciones y {segments} segmentos.')
print('OK: fuentes, enlaces y nómina de cuatro; sin rutas personales, contactos o capturas detectados.')
print('OK: puntajes numéricos, acumulados de olas y referencias del escenario integrado.')
if pending_costs:
    print(f'PENDIENTE: {len(pending_costs)} paquetes sin costo; total, reserva, capacidad y financiación requieren revisión. No se certifica una estimación terminada.')
else:
    print('REVISAR: rangos calculados; revisar manualmente total, reserva, capacidad y asequibilidad.')
if pending_scores:
    print('PENDIENTE: priorización sin puntuar: ' + ', '.join(pending_scores))
