# Base de ejecución propuesta para B modular

**23-10-2026. Base integrada para ratificación del equipo.** Esta propuesta adopta cuatro células y anticipa el sexto equipo. Los parámetros son supuestos académicos, no contratos ni rendimientos observados. Conserva los siete entregables y la referencia PERT de 104 equipo-sprints. La capacidad externa de campo se registra por separado, sin convertirla en desarrollo intercambiable. Este archivo es la fuente de parámetros del verificador; los insumos originales permanecen intactos.

## Parámetros de cálculo

| ID | Valor | Significado |
| --- | ---: | --- |
| BASE-01 | 6 | Personas por equipo de referencia. |
| BASE-02 | 10 | Días hábiles por sprint de referencia. |
| BASE-03 | 12 | Meses del horizonte empresarial. |
| BASE-04 | 26 | Sprints de referencia por año. |
| BASE-05 | 14 | MM CLP por equipo-mes, supuesto. |
| BASE-06 | 8 | Sprint de corte de primera salida. |
| BASE-07 | 11 | Último sprint de R0/R1. |
| BASE-08 | 15 | Último sprint de R2. |
| BASE-09 | 18 | Sprint que contiene G2 a mitad de periodo. |
| BASE-10 | 0,5 | Fracción de sprint 18 anterior a G2. |
| BASE-11 | 4 | Células de habilitación/acompañamiento. |
| BASE-12 | 2 | Funciones por célula. |
| BASE-13 | 0,75 | Disponibilidad efectiva de las células. |
| BASE-14 | 58 | Altas adicionales a las diez tiendas piloto. |
| BASE-15 | 2 | Persona-días efectivos de habilitación por alta. |
| BASE-16 | 0,5 | Persona-día efectivo de acompañamiento por alta. |
| BASE-17 | 25 | Jornadas equivalentes de actividad de las cuatro células. |
| BASE-18 | 30 | Persona-días brutos de preparación transversal preservados. |
| BASE-19 | 20 | Persona-días adicionales de campo financiados en COST-06. |
| BASE-20 | 10 | Días reservados para corrección/VE-01. |
| BASE-21 | 40 | Ventana hábil total de expansión y preparación. |
| BASE-22 | 10 | MM CLP de bolsa propuesta de traslados, dentro de COST-06. |
| BASE-23 | 0,20 | Estrés de tarifa/costo de equipos. |
| BASE-24 | 180 | Tope propuesto OMS, MM CLP, en escenario de respuesta. |
| BASE-25 | 70 | Tope propuesto WMS, MM CLP, en escenario de respuesta. |
| BASE-26 | 85 | Tope propuesto cloud/observabilidad, MM CLP, en escenario de respuesta. |

## Dotación por sprint

El sexto equipo debe estar disponible en semana 9: su arranque ocupa el sprint 5 y entrega desde el 6. Los cinco equipos iniciales arrancan en el sprint 1; el sprint 17 se reserva para estabilización. Unidades efectivas = equipos pagados menos unidades reservadas sin producción. La dotación de campaña conserva cuatro equipos; su aceptación exige cubrir las funciones de respuesta y soporte, no solo sumar capacidad.

| Sprint | Equipos pagados | Unidades reservadas sin producción | Unidades efectivas |
| --- | ---: | ---: | ---: |
| S01 | 5 | 5 | 0 |
| S02 | 5 | 0 | 5 |
| S03 | 5 | 0 | 5 |
| S04 | 5 | 0 | 5 |
| S05 | 6 | 1 | 5 |
| S06 | 6 | 0 | 6 |
| S07 | 6 | 0 | 6 |
| S08 | 6 | 0 | 6 |
| S09 | 6 | 0 | 6 |
| S10 | 6 | 0 | 6 |
| S11 | 6 | 0 | 6 |
| S12 | 6 | 0 | 6 |
| S13 | 6 | 0 | 6 |
| S14 | 6 | 0 | 6 |
| S15 | 6 | 0 | 6 |
| S16 | 4 | 0 | 4 |
| S17 | 4 | 4 | 0 |
| S18 | 4 | 0 | 4 |
| S19 | 4 | 0 | 4 |
| S20 | 4 | 0 | 4 |
| S21 | 4 | 0 | 4 |
| S22 | 4 | 0 | 4 |
| S23 | 4 | 0 | 4 |
| S24 | 4 | 0 | 4 |
| S25 | 4 | 0 | 4 |
| S26 | 4 | 0 | 4 |

Resultado: **130 equipo-sprints pagados**, 10 reservados y **120 efectivos**. Son 60 equipo-meses × 14 = **840 MM**, sin colchón de redondeo. F1/F2/F3 conservan 56/24/40; el corte piloto mantiene **36/38 = 94,74%**. La disponibilidad del sexto equipo en semana 9 es condición de este calendario.

## Cuarta célula, acompañamiento y costo de campo

Habilitación: 58 × 2 = 116 persona-días efectivos. Acompañamiento: 58 × 0,5 = 29. Total **145**, frente a **150** disponibles en 25 jornadas equivalentes de cuatro células. El mínimo agregado redondeado es 25 días, más diez de preparación, **35 dentro de 40**.

Las 25 jornadas equivalentes se distribuyen dentro de los treinta días de olas de 07, conservando cinco de margen para traslados, relevo y esperas, además de los diez de corrección/VE-01. No se cuentan como cinco días adicionales al calendario. Las cuatro olas mantienen sus ventanas 8/8/7/7; el trabajo de células se programa por sitio dentro de ellas y la ola siguiente requiere aceptación de la anterior.

Trabajo bruto de células: 4 × 2 × 25 = **200 persona-días**. Preparación transversal: **30**, total **230**. E11/R2 aporta 3,5 × 6 × 10 = **210**: 200 de células y diez de preparación. Los veinte restantes son **capacidad adicional de campo en COST-06**, distinta de las personas de desarrollo. R2 conserva carga 23/24 y su holgura original. Los 104 equipo-sprints son referencia de trabajo propio; no representan por sí solos toda la contribución externa.

| Partida dentro de COST-06 | MM CLP | Tratamiento |
| --- | ---: | --- |
| Veinte persona-días de preparación adicional | 2,1538 | Valoración académica a tarifa media 14 × 12/26 / 60 por persona-día; confirmar perfil y costo de campo. |
| Bolsa de traslados de cuatro células | 10,0000 | Asignación presupuestaria propuesta, no cotización ni itinerario verificado. Incluye transporte/alojamiento según necesidad. |
| Resto para formación, adopción y operación/transición | 32,8462 | Conciliar cantidades, reemplazos y dispositivos; evitar duplicar horas de E11. |
| Total COST-06 | 45,0000 | Se redistribuye la base existente, no se agregan 12,1538 otra vez al presupuesto. |

El resto de COST-06 debe sostener el trabajo original con esta redistribución. Cotizar rutas y campo antes de comprometerlos; si la bolsa resulta insuficiente, escalar costo/cobertura. El mecanismo respalda una meta condicionada 68/M7 bajo estos supuestos, sin demostrar disponibilidad real, exactitud física o adopción.

## Respuesta escalonada al estrés combinado

Se parte del extremo bruto **1.668 MM**, no de la base 1.330. Diferir E10/E8b habilita reducir capacidad; el esfuerzo diferido no es ahorro de caja por sí solo. Después de G2 se propone pasar de cuatro a tres equipos por 8,5 sprints equivalentes, con prorrata semanal y cláusula de reducción. R3 baja de 28,3 a 18,9667 unidades de esfuerzo; su capacidad tras G2 baja de 34 a 25,5, preservando devoluciones y controles. La campaña previa conserva su dotación.

| ID | Paso | Reducción monetaria MM | Total MM | Exceso sobre 1.500 MM |
| --- | --- | ---: | ---: | ---: |
| EST-01 | Estrés combinado bruto | 0,0000 | 1668,0000 | 168,0000 |
| EST-02 | Diferir E10/E8b: habilita reducción contractual | 0,0000 | 1668,0000 | 168,0000 |
| EST-03 | Reducir un equipo tras G2, 8,5 sprints a tarifa estresada | 65,9077 | 1602,0923 | 102,0923 |
| EST-04 | OMS: máximo 180 frente a extremo 240 | 60,0000 | 1542,0923 | 42,0923 |
| EST-05 | WMS: máximo 70 frente a extremo 100 | 30,0000 | 1512,0923 | 12,0923 |
| EST-06 | Cloud/observabilidad: máximo 85 frente a extremo 100 | 15,0000 | 1497,0923 | 0,0000 |

Los topes son **condiciones propuestas de contratación**, con alcance y aceptación definidos. Contratar por hitos sin precio máximo no asegura esos ahorros. El límite cloud exige controlar consumo y evitar ampliaciones opcionales, manteniendo observabilidad básica, seguridad y continuidad. Si los proveedores no aceptan, falta capacidad cancelable o el costo a término supera 1.500, el comité debe cambiar cobertura/arquitectura o reconsiderar C antes de contratar; no sumar como conseguidas las reducciones.

El escenario condicionado queda con **2,9077 MM de margen** frente al techo: es estrecho, no una reserva robusta adicional. Requiere las palancas simultáneas y precios aceptados; no cubre automáticamente viajes o dispositivos fuera de las fronteras consideradas. La base sigue en 1.330 + 170; la tabla es una respuesta al estrés, no un aumento autorizado de presupuesto ni un escenario probabilístico.

## Ratificación y control

El grupo debe ratificar catálogo, SUP-16, devolución elegible, límites experimentales y esta base. Datos de volumen/margen y formato/hora del aula permanecen pendientes. La presentación conserva su pauta de doce láminas; su construcción y ensayo son pasos posteriores. `python3 scripts/verificar.py` calcula calendario, campo y escalera a partir de estas tablas y contrasta referencias en los documentos activos.
