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

presentations = 0
for line in (root/'insumos/presentaciones/README.md').read_text().splitlines():
    if not line.startswith('|'):
        continue
    cells = [x.strip() for x in line.strip('|').split('|')]
    if len(cells) != 4 or not re.fullmatch(r'0[3-6]', cells[0]):
        continue
    match = re.search(r'\]\(([^)]+)\)', cells[1])
    check(match is not None, f'Falta enlace de presentación: {cells[0]}')
    if match is None:
        continue
    path = root/'insumos/presentaciones'/match.group(1)
    check(path.is_file(), f'Falta presentación: {path.name}')
    if path.is_file():
        check(path.read_bytes().startswith(b'%PDF-'), f'Archivo no es PDF: {path.name}')
        check(hashlib.sha256(path.read_bytes()).hexdigest() == cells[3].strip('`'), f'Hash de presentación distinto: {path.name}')
    presentations += 1
check(presentations == 4, 'Se esperan las presentaciones docentes 03 a 06.')

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
check(transcripts == 6, 'Se esperan seis partes disponibles de las clases 1 a 3.')
check(len(list((root/'trabajo').glob('[0-9][0-9]_*.md'))) == 7, 'Se esperan siete documentos de entregables.')

def rows(name):
    for line in (root/name).read_text().splitlines():
        if line.startswith('|'):
            yield [cell.strip() for cell in line.strip('|').split('|')]

def number(value):
    return Decimal(value.replace('.', '').replace(',', '.'))

# Estimación y WSJF recibidos: operaciones verificables, sin certificar hipótesis.
epics = {}
listed_pert_total = None
categories = {}
listed_cost_total = None
funding = {}
capacity = {}
budget = {}
for cells in rows('trabajo/06_estimacion.md'):
    if len(cells) == 7 and re.fullmatch(r'E\d+(?:a|b)?', cells[0]):
        o,m,pess,listed_e,listed_sigma = map(number,cells[2:7])
        e = (o+4*m+pess)/6
        sigma = (pess-o)/6
        check(o <= m <= pess, f'Rango PERT inválido: {cells[0]}')
        check(abs(listed_e-e) <= Decimal('0.051'), f'Esperado PERT incorrecto: {cells[0]}')
        check(abs(listed_sigma-sigma) <= Decimal('0.051'), f'Sigma PERT incorrecta: {cells[0]}')
        epics[cells[0]] = (o,m,pess,e,sigma)
    elif len(cells) == 7 and cells[0] == 'Total':
        listed_pert_total = tuple(map(number,cells[2:7]))
    elif len(cells) == 6 and re.fullmatch(r'COST-\d\d',cells[0]):
        base,low,high = map(number,cells[2:5])
        check(low <= base <= high, f'Rango presupuestario inválido: {cells[0]}')
        categories[cells[0]] = (base,low,high)
    elif len(cells) == 6 and cells[0] == 'Subtotal':
        listed_cost_total = tuple(map(number,cells[2:5]))
    elif len(cells) == 4 and cells[0] in {'T1','T2','T3','RES'}:
        funding[cells[0]] = number(cells[3])
    elif len(cells) == 5 and cells[0] in {'F1','F2','F3'}:
        cap,load,usage = number(cells[2]),number(cells[3]),number(cells[4].strip('%'))
        check(abs(load/cap*100-usage) < Decimal('0.005'), f'Utilización incorrecta: {cells[0]}')
        capacity[cells[0]] = (cap,load)
    elif len(cells) == 3 and cells[0] in {'Base de categorías','Reserva de contingencia','Marco preliminar total','Extremo alto de categorías'}:
        budget[cells[0]] = number(cells[1])
check(len(epics) == 12, 'Se esperan doce filas de épica: E1 a E11 con E8 desdoblada.')
if epics and listed_pert_total is not None:
    totals = tuple(sum(row[i] for row in epics.values()) for i in range(4))
    sigma_total = sum(row[4]**2 for row in epics.values()).sqrt()
    check(all(abs(a-b) <= Decimal('0.051') for a,b in zip(totals+(sigma_total,),listed_pert_total)), 'Total PERT o sigma total incorrectos.')
else:
    check(False, 'Falta total PERT verificable.')
check(len(categories) == 7, 'Se esperan siete categorías de costo.')
if categories:
    cost_totals = tuple(sum(row[i] for row in categories.values()) for i in range(3))
    check(cost_totals == listed_cost_total, 'Subtotal base/O/P incorrecto.')
    if len(budget) == 4:
        check(cost_totals[0] == budget['Base de categorías'], 'Base distinta de suma de categorías.')
        check(cost_totals[2] == budget['Extremo alto de categorías'], 'Extremo alto incorrecto.')
        check(budget['Base de categorías']+budget['Reserva de contingencia'] == budget['Marco preliminar total'], 'Base más reserva incorrecta.')
        check(budget['Marco preliminar total'] <= 1500, 'Marco preliminar supera techo del caso; revisar antes de comprometer.')
    else:
        check(False,'Faltan relaciones presupuestarias.')
check(len(funding) == 4 and len(capacity) == 3,'Faltan tramos de financiación o capacidad.')
if len(funding) == 4 and len(budget) == 4:
    check(sum(funding[k] for k in ['T1','T2','T3']) == budget['Base de categorías'],'Tramos no suman base.')
    check(funding['RES'] == budget['Reserva de contingencia'],'Reserva de tramos distinta de presupuesto.')
if len(capacity) == 3 and epics:
    check(sum(c[0] for c in capacity.values()) == 120, 'Revisar capacidad efectiva propuesta 120.')
    check(abs(sum(c[1] for c in capacity.values())-sum(e[3] for e in epics.values())) < Decimal('0.01'),'Cargas por tramo no suman esfuerzo.')

ratios = {}
for cells in rows('trabajo/05_priorizacion.md'):
    if len(cells) == 8 and re.fullmatch(r'E\d+(?:a|b)?',cells[0]):
        v,u,risk,cod,size,listed = map(number,cells[2:8])
        check(v+u+risk == cod, f'Costo de retraso relativo incorrecto: {cells[0]}')
        check(size > 0 and abs(cod/size-listed) <= Decimal('0.051'),f'WSJF incorrecto: {cells[0]}')
        check(cells[0] in epics,f'WSJF sin esfuerzo definido: {cells[0]}')
        ratios[cells[0]] = listed
check(len(ratios) == 9,'Se esperan nueve ratios WSJF, además de tres épicas obligatorias.')

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

# Plan desarrollado: conserva PERT y cargas sin certificar productividad ni fechas.
allocation = {}
listed_allocation = None
prepilot = {}
listed_prepilot = None
cells_model = {}
for cells in rows('registros/plan_alcance_roadmap.md'):
    if len(cells) == 6 and cells[0] in epics:
        values = tuple(map(number, cells[1:]))
        check(all(v >= 0 for v in values), f'Carga negativa: {cells[0]}')
        check(abs(sum(values[:4])-values[4]) < Decimal('0.0003'), f'Suma por etapa incorrecta: {cells[0]}')
        check(abs(values[4]-epics[cells[0]][3]) < Decimal('0.0001'), f'La distribución altera PERT: {cells[0]}')
        allocation[cells[0]] = values
    elif len(cells) == 6 and cells[0] == 'Total':
        listed_allocation = tuple(map(number, cells[1:]))
    elif len(cells) == 3 and cells[0] in epics:
        prepilot[cells[0]] = tuple(map(number, cells[1:]))
    elif len(cells) == 3 and cells[0] == 'Total':
        listed_prepilot = tuple(map(number, cells[1:]))
    elif len(cells) == 3 and re.fullmatch(r'CEL-\d\d', cells[0]):
        cells_model[cells[0]] = number(cells[1])
check(set(allocation) == set(epics), 'La matriz de etapas debe cubrir todas las épicas, una vez.')
if allocation and listed_allocation:
    computed = tuple(sum(v[i] for v in allocation.values()) for i in range(5))
    check(all(abs(a-b) < Decimal('0.0003') for a,b in zip(computed,listed_allocation)), 'Totales de asignación por etapa incorrectos.')
    check(listed_allocation == (Decimal('47.7'),Decimal('23'),Decimal('5'),Decimal('28.3'),Decimal('104')), 'Cargas propuestas distintas de las conciliadas con el equipo.')
    if len(capacity) == 3:
        check(listed_allocation[0] == capacity['F1'][1] and listed_allocation[1] == capacity['F2'][1], 'F1/F2 no coinciden con estimación.')
        check(sum(listed_allocation[2:4]) == capacity['F3'][1], 'Campaña/R3 no suman F3.')
    f3_capacity = 4*len([16,*range(18,27)])
    campaign_capacity = 4+2  # Sprint 16 y primera mitad del 18.
    check(f3_capacity-campaign_capacity == 34, 'Revisar separación de capacidad antes/después de G2.')
    check(listed_allocation[2] <= 6 and listed_allocation[3] <= 34, 'Carga excede capacidad propuesta de campaña/R3.')
else:
    check(False, 'Falta total de matriz por etapa.')
check(set(prepilot) == {k for k,v in allocation.items() if v[0] > 0}, 'Corte piloto debe incluir todas las épicas con carga F1.')
if prepilot and listed_prepilot:
    check(tuple(sum(v[i] for v in prepilot.values()) for i in range(2)) == listed_prepilot, 'Total del corte piloto incorrecto.')
    check(listed_prepilot == (Decimal('36'),Decimal('11.7')), 'Corte piloto distinto de 36/11,7.')
    check(36 <= 4*5+3*6, 'Corte piloto excede capacidad hasta sprint 8.')
    for ident,values in prepilot.items():
        check(all(v >= 0 for v in values) and abs(sum(values)-allocation[ident][0]) < Decimal('0.0001'), f'Corte piloto no conserva carga F1: {ident}')
else:
    check(False, 'Falta corte piloto verificable.')
check(len(cells_model) == 9, 'Faltan parámetros del mecanismo de altas propuesto.')
if len(cells_model) == 9:
    c = lambda i: cells_model[f'CEL-{i:02d}']
    check(c(1) == sum(waves[1:]), 'Modelo de altas distinto de 58 tiendas.')
    needed = c(1)*c(3)*c(6)
    effective = c(2)*c(3)*c(4)*c(5)
    gross = c(2)*c(3)*c(4)
    epic_gross = c(7)*c(8)*c(9)
    check(0 < c(5) <= 1 and needed <= effective, 'Altas no caben bajo disponibilidad propuesta.')
    check(gross <= epic_gross and c(7) == allocation['E11'][1], 'Células no caben en E11/R2 o se cambia su asignación.')
    check((needed,effective,gross,epic_gross) == (116,135,180,210), 'Operaciones de dimensionamiento de altas cambiaron; revisar narrativa.')

members = [cells[0] for cells in rows('EQUIPO.md') if cells[0] not in {'Integrante', '---'}]
check(len(members) == 4 and len(set(members)) == 4, 'La nómina activa debe contener cuatro integrantes distintos.')

# El archivo recibido es fuente, no la versión común editable.
source_digest = re.search(r'SHA-256 del avance preservado: `([0-9a-f]{64})`', (root/'insumos/README.md').read_text())
check(source_digest is not None, 'Falta hash del avance recibido.')
if source_digest:
    check(hashlib.sha256((root/'insumos/avance_equipo_2026-10-21.md').read_bytes()).hexdigest() == source_digest.group(1), 'El avance preservado cambió; editar la integración en trabajo/.')

# El nuevo insumo se conserva como fuente, no como documento corregido.
new_digest = re.search(r'SHA-256 del avance del 23: `([0-9a-f]{64})`', (root/'insumos/README.md').read_text())
check(new_digest is not None, 'Falta hash del avance recibido el 23.')
if new_digest:
    check(hashlib.sha256((root/'insumos/avance_equipo_2026-10-23.md').read_bytes()).hexdigest() == new_digest.group(1),'El avance recibido del 23 fue modificado.')

# Antecedente del 22: comprobar operaciones archivadas, no su vigencia o dotación.
parameters = {}
listed_calculations = {}
for cells in rows('registros/escenario_provisional.md'):
    if re.fullmatch(r'PAR-\d\d', cells[0]):
        parameters[cells[0]] = number(cells[1])
    elif re.fullmatch(r'CAL-\d\d', cells[0]):
        listed_calculations[cells[0]] = number(cells[1])
check(len(parameters) == 15, 'Revisar los quince parámetros del modelo de habilitación.')
if len(parameters) == 15:
    q = lambda n: parameters[f'PAR-{n:02d}']
    extra = q(2)-q(1)
    required = extra*q(3)*q(4)
    effective = q(5)*q(3)*q(6)*q(7)
    expected_calculations = {
        'CAL-01': extra, 'CAL-02': required, 'CAL-03': effective,
        'CAL-04': effective // (q(3)*q(4)),
        'CAL-05': q(5)*q(3)*q(8)*q(7),
        'CAL-06': q(1)*q(3)*q(4), 'CAL-07': q(2)*q(9)*q(10),
        'CAL-08': q(13)*q(14)*q(15),
        'CAL-09': q(5)*q(3)*(q(6)+q(8)), 'CAL-10': effective-required,
    }
    check(listed_calculations == expected_calculations, 'Cantidades calculadas no corresponden a parámetros de habilitación.')
    check(q(11)*q(3)*q(12) >= expected_calculations['CAL-06'], 'Capacidad de piloto insuficiente bajo parámetros.')
    check(0 < q(7) <= 1, 'Disponibilidad efectiva debe estar entre 0 y 1.')
    check(effective >= required, 'La expansión no cabe en ventana planificada bajo los parámetros actuales.')

slides = []
for cells in rows('presentacion/pauta_construccion.md'):
    if len(cells) == 7 and cells[0].isdigit():
        slides.append((int(cells[0]), number(cells[1])))
check([n for n, minutes in slides] == list(range(1,13)), 'La pauta de construcción propone doce láminas numeradas en orden.')
check(sum(minutes for n, minutes in slides) == 25, 'La pauta de construcción debe sumar los 25 minutos propuestos.')

for error in errors:
    print('ERROR:', error)
if errors:
    sys.exit(1)
print(f'OK: {len(paths)} archivos, siete entregables, pauta 100%, {transcripts} transcripciones y {segments} segmentos.')
print(f'OK: fuentes, {presentations} presentaciones, enlaces y nómina de cuatro; sin rutas personales, contactos o capturas detectados.')
print('OK: WSJF, PERT, categorías presupuestarias, tramos y cargas; pauta de 12 láminas/25 minutos.')
print('OK: asignación por épica/etapa, corte de primera salida y dimensión propuesta de 58 altas sin duplicar E11.')
print('REVISAR: ratificación de alcance/calendario, dedicación por especialidad, costos y exposición monetaria del experimento; no se certifica confianza de fecha.')
