#!/usr/bin/env python3
"""Comprueba el contenido portable, la pauta y las fuentes compartidas."""
from pathlib import Path
from decimal import Decimal, ROUND_CEILING
import hashlib
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []

def check(ok, message):
    if not ok:
        errors.append(message)

paths = [p for p in root.rglob('*') if p.is_file() and not ({'.git', 'build', 'local'} & set(p.relative_to(root).parts))]
allowed_images = {Path('typst/recursos/logo-pucv-blanco.png')}  # logo de la portada del documento de respaldo
for path in paths:
    relative = path.relative_to(root)
    check(path.suffix.lower() not in {'.png', '.jpg', '.jpeg', '.webp', '.html', '.mp4'} or relative in allowed_images, f'Revisar inclusión no prevista: {relative}')
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
transcript_names = set()
for line in (root/'transcripciones/README.md').read_text().splitlines():
    if not line.startswith('|'):
        continue
    cells = [x.strip() for x in line.strip('|').split('|')]
    if len(cells) != 6 or not re.fullmatch(r'\d+', cells[3]):
        continue
    name = re.search(r'\]\(([^)]+)\)', cells[2]).group(1)
    path = root/'transcripciones'/name
    check(name not in transcript_names, f'Transcripción duplicada en índice: {name}')
    transcript_names.add(name)
    check(path.is_file(), f'Falta transcripción: {name}')
    if not path.is_file():
        continue
    stamps = re.findall(r'^\[([\d:]+)\]', path.read_text(), re.M)
    check(bool(stamps) and len(stamps) == int(cells[3]) and stamps[-1] == cells[4], f'Segmentos o tiempo final cambiaron: {name}')
    def seconds(stamp):
        total = 0
        for value in stamp.split(':'):
            total = total * 60 + int(value)
        return total
    times = [seconds(stamp) for stamp in stamps]
    check(all(a <= b for a, b in zip(times, times[1:])), f'Tiempos fuera de orden: {name}')
    digest = cells[5].strip('`')
    check(hashlib.sha256(path.read_bytes()).hexdigest() == digest, f'Hash de transcripción distinto: {name}')
    transcripts += 1
    segments += len(stamps)
expected_transcripts = {f'clase-{cls:02d}_parte-{part}.md' for cls in range(1, 5) for part in (1, 2)}
check(transcripts == 8 and transcript_names == expected_transcripts, 'Se esperan ocho partes distintas de las clases 1 a 4.')
for part, first in ((1, '0:00'), (2, '1:30:22')):
    path = root/'transcripciones'/f'clase-04_parte-{part}.md'
    if path.is_file():
        stamps = re.findall(r'^\[([\d:]+)\]', path.read_text(), re.M)
        check(bool(stamps) and stamps[0] == first, f'Inicio continuo de clase 4 alterado: parte {part}')
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
    check(all(c[0] > 0 for c in capacity.values()), 'Capacidad por tramo debe ser positiva.')
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

else:
    check(False, 'Falta total de matriz por etapa.')
check(set(prepilot) == {k for k,v in allocation.items() if v[0] > 0}, 'Corte piloto debe incluir todas las épicas con carga F1.')
if prepilot and listed_prepilot:
    check(tuple(sum(v[i] for v in prepilot.values()) for i in range(2)) == listed_prepilot, 'Total del corte piloto incorrecto.')
    check(listed_prepilot == (Decimal('36'),Decimal('11.7')), 'Corte piloto distinto de 36/11,7.')
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


# Base vigente: los resultados se calculan desde parámetros y calendario Markdown.
base_params = {}
calendar = {}
stress_rows = {}
field_cost_rows = {}
for cells in rows('registros/base_ejecucion.md'):
    if len(cells) == 3 and re.fullmatch(r'BASE-\d\d', cells[0]):
        base_params[cells[0]] = number(cells[1])
    elif len(cells) == 4 and re.fullmatch(r'S\d\d', cells[0]):
        calendar[int(cells[0][1:])] = tuple(map(number, cells[1:]))
    elif len(cells) == 5 and re.fullmatch(r'EST-\d\d', cells[0]):
        stress_rows[cells[0]] = tuple(map(number, cells[2:]))
    elif len(cells) == 3 and cells[0] in {
        'Veinte persona-días de preparación adicional', 'Bolsa de traslados de cuatro células',
        'Resto para formación, adopción y operación/transición', 'Total COST-06'}:
        field_cost_rows[cells[0]] = number(cells[1])
check(set(base_params) == {f'BASE-{i:02d}' for i in range(1,27)}, 'Faltan parámetros de base de ejecución.')
check(set(calendar) == set(range(1,27)), 'El calendario debe contener S01 a S26 una vez.')
check(len(stress_rows) == 6, 'Faltan pasos del escenario de estrés.')
base_results = {}
if len(base_params) == 26 and len(calendar) == 26 and len(capacity) == 3 and len(cells_model) == 9:
    bp = lambda i: base_params[f'BASE-{i:02d}']
    for sprint, (paid, reserved, effective_units) in calendar.items():
        check(0 <= reserved <= paid and paid-reserved == effective_units,
              f'Calendario inconsistente en S{sprint:02d}.')
    paid_units = sum(v[0] for v in calendar.values())
    effective_units = sum(v[2] for v in calendar.values())
    rate = bp(5)*bp(3)/bp(4)
    teams_cost = paid_units*rate
    check(abs(teams_cost-categories['COST-01'][0]) < Decimal('0.00001'),
          'Calendario pagado no concilia COST-01; revisar tarifa o presupuesto.')
    f1_end, f2_end, gate2_sprint = map(int, [bp(7),bp(8),bp(9)])
    calculated_capacity = {
        'F1':sum(v[2] for s,v in calendar.items() if 1 < s <= f1_end),
        'F2':sum(v[2] for s,v in calendar.items() if f1_end < s <= f2_end),
        'F3':sum(v[2] for s,v in calendar.items() if s > f2_end),
    }
    check(all(calculated_capacity[k] == capacity[k][0] for k in calculated_capacity),
          'Capacidad de 06 distinta del calendario vigente.')
    check(effective_units == sum(v[0] for v in capacity.values()), 'Total efectivo distinto del calendario.')
    early_capacity = sum(v[2] for s,v in calendar.items() if s <= int(bp(6)))
    early_load = listed_prepilot[0]
    check(early_load <= early_capacity, 'El corte piloto excede capacidad efectiva con arranque.')
    campaign_capacity = sum(v[2] for s,v in calendar.items() if f2_end < s < gate2_sprint)
    campaign_capacity += calendar[gate2_sprint][2]*bp(10)
    later_capacity = calculated_capacity['F3']-campaign_capacity
    check(listed_allocation[2] <= campaign_capacity and listed_allocation[3] <= later_capacity,
          'Carga campaña/R3 excede capacidad calculada por calendario.')
    # La celda comparada informa habilitación y otra aporta acompañamiento.
    expected_cell_params = {1:bp(14),2:bp(11),3:bp(12),4:bp(17),5:bp(13),
                            6:bp(15)/bp(12),7:allocation['E11'][1],8:bp(1),9:bp(2)}
    check(all(cells_model[f'CEL-{i:02d}'] == value for i,value in expected_cell_params.items()),
          'Parámetros CEL distintos de la base vigente.')
    required_habilitation = bp(14)*bp(15)
    required_hypercare = bp(14)*bp(16)
    required_field = required_habilitation+required_hypercare
    daily_capacity = bp(11)*bp(12)*bp(13)
    available_field = daily_capacity*bp(17)
    active_days = (required_field/daily_capacity).to_integral_value(rounding=ROUND_CEILING)
    total_days = active_days+bp(20)
    gross_cells = bp(11)*bp(12)*bp(17)
    internal_gross = allocation['E11'][1]*bp(1)*bp(2)
    check(required_field <= available_field and active_days <= bp(17) and total_days <= bp(21),
          'Habilitación/acompañamiento no caben en la base de células.')
    check(gross_cells+bp(18) == internal_gross+bp(19),
          'Preparación/células no concilian E11 y campo externo; no consumir holgura R2 por inferencia.')
    extra_field_cost = bp(19)*rate/(bp(1)*bp(2))
    remaining_change_cost = categories['COST-06'][0]-extra_field_cost-bp(22)
    expected_field_costs = {
        'Veinte persona-días de preparación adicional':extra_field_cost,
        'Bolsa de traslados de cuatro células':bp(22),
        'Resto para formación, adopción y operación/transición':remaining_change_cost,
        'Total COST-06':categories['COST-06'][0],
    }
    check(set(field_cost_rows) == set(expected_field_costs), 'Falta descomposición de COST-06.')
    check(all(abs(field_cost_rows.get(k,Decimal('-1'))-v) <= Decimal('0.0001')
              for k,v in expected_field_costs.items()), 'COST-06 no concilia campo, viajes y resto.')
    check(remaining_change_cost >= 0, 'Campo/viajes exceden COST-06.')
    # Leer el estrés y los topes; no convertir sus condiciones en ofertas reales.
    check(abs(categories['COST-01'][2]-teams_cost*(1+bp(23))) < Decimal('0.0001'),
          'Estrés COST-01 no concilia tarifa y calendario.')
    periods_after_gate2 = bp(4)-bp(9)+(1-bp(10))
    canceled_cost = periods_after_gate2*rate*(1+bp(23))
    reduced_later_capacity = later_capacity-periods_after_gate2
    reduced_later_load = listed_allocation[3]-epics['E10'][3]-epics['E8b'][3]
    check(reduced_later_load <= reduced_later_capacity, 'R3 reducido no cabe tras retirar el equipo.')
    reductions = [Decimal(0),Decimal(0),canceled_cost,
                  categories['COST-02'][2]-bp(24),categories['COST-03'][2]-bp(25),
                  categories['COST-04'][2]-bp(26)]
    check(all(value >= 0 for value in reductions), 'Tope superior al extremo de referencia.')
    stress_total = sum(v[2] for v in categories.values())
    raw_stress = stress_total
    ceiling = budget['Marco preliminar total']
    for i,reduction in enumerate(reductions,1):
        stress_total -= reduction
        expected_row = (reduction,stress_total,max(Decimal(0),stress_total-ceiling))
        actual = stress_rows.get(f'EST-{i:02d}')
        check(actual is not None and all(abs(a-b) <= Decimal('0.0001') for a,b in zip(actual,expected_row)),
              f'Escalera de estrés EST-{i:02d} no corresponde a calendario/categorías/topes.')
    check(stress_total <= ceiling, 'Las palancas propuestas todavía exceden el techo; falta decisión.')
    base_results = dict(paid=paid_units,effective=effective_units,pilot_load=early_load,
                        pilot_capacity=early_capacity,pilot_usage=early_load/early_capacity*100,
                        field_required=required_field,field_available=available_field,
                        days=total_days,window=bp(21),raw_stress=raw_stress,
                        mitigated_stress=stress_total,ceiling=ceiling)

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

# Cobertura documental de interesados; no acredita satisfacción o aceptación.
stakeholders = {}
for cells in rows('registros/matriz_stakeholders.md'):
    if len(cells) == 7 and re.fullmatch(r'STK-\d\d', cells[0]):
        check(cells[0] not in stakeholders, f'Stakeholder duplicado: {cells[0]}')
        check(all(cells[i] for i in range(1,7)), f'Campos de interés/tensión/respuesta vacíos: {cells[0]}')
        stakeholders[cells[0]] = cells[1].split(', p. ')[0]
expected_stakeholders = [
    'Gerente General / Sponsor', 'Gerente Comercial', 'Gerente de Operaciones',
    'Gerente de Logística', 'Gerente de Tecnología', 'CISO', 'Gerente de Finanzas',
    'Gerentes de Tienda', 'Product Owner E-commerce', 'Arquitectura Empresarial',
    'Equipos de desarrollo', 'Proveedor WMS', 'Proveedor Cloud',
]
check(stakeholders == {f'STK-{i:02d}': name for i,name in enumerate(expected_stakeholders,1)},
      'La matriz debe conservar los trece stakeholders oficiales de pp. 6/7.')

for error in errors:
    print('ERROR:', error)
if errors:
    sys.exit(1)
print(f'OK: {len(paths)} archivos, siete entregables, pesos de rúbrica 100%, {transcripts} transcripciones y {segments} segmentos.')
print(f'OK: fuentes, {presentations} presentaciones, enlaces y nómina de cuatro; sin rutas personales, contactos o capturas detectados.')
print('OK: WSJF, PERT, categorías presupuestarias, tramos y cargas; pauta de 12 láminas/25 minutos.')
print('OK: calendario, campo externo, acompañamiento y escalera de estrés calculados desde base_ejecucion.md.')
print('OK: trece stakeholders con interés, tensión, respuesta y evidencia previstos; no certifica satisfacción ni nota.')
if base_results:
    b = base_results
    print(f"BASE: {b['paid']:g} pagados/{b['effective']:g} efectivos; corte {b['pilot_load']:g}/{b['pilot_capacity']:g} ({b['pilot_usage']:.2f}%); campo {b['field_required']:g}/{b['field_available']:g}; actividad/preparación {b['days']:g}/{b['window']:g} días.")
    print(f"ESTRÉS MM: bruto {b['raw_stress']:g}; con reducción/topes condicionados {b['mitigated_stress']:.4f}; techo {b['ceiling']:g}.")
print('REVISAR: ratificación de base, recursos de campo, traslados, precios máximos/cancelabilidad y datos de beneficio. Sin aprobación empresarial ni confianza de fecha certificada.')
