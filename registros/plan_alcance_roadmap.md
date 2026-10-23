# Desarrollo del alcance y roadmap de Maverick

**Propuesta académica completa para revisión, 23-10-2026.** Apoya los documentos [04](../trabajo/04_alcance_y_backlog.md) y [07](../trabajo/07_roadmap.md). Conserva las medias PERT y tramos recibidos; integra cuatro células y sexto equipo anticipado según la [base de ejecución](base_ejecucion.md). Las distribuciones, ventanas y mecanismos siguientes son supuestos de planificación; no provienen del profesor ni acreditan dotación, productividad o aprobación del grupo.

## Convención de calendario y autorización

Se usan 52 semanas de referencia y 26 sprints de dos semanas. Los meses siguientes son bloques relativos de planificación, no meses civiles de duración idéntica. Antes de ejecutar se convierten a fechas reales, feriados, turnos y fecha de Black Friday. No existe fecha empresarial de inicio en el corpus.

| Mes | Semanas de referencia | Resultado principal / condición |
| --- | --- | --- |
| M1 | 1 a 4 | G0: mandato, selección piloto, contratación por hitos, responsables y medición. |
| M2 | 5 a 8 | VT-01: interfaces/datos y recuperación representativos antes de exponer clientes. |
| M3 | 9 a 13 | Construcción integrada y base comparable; preparación de las diez tiendas. |
| M4 | 14 a 17 | Flujo mínimo aceptado al terminar semana 16; empieza uso y observación. |
| M5 | 18 a 22 | Completar cuatro semanas de observación, analizar y decidir G1 al cierre. |
| M6 | 23 a 26 | Olas O1/O2 y preparación de sitios/soporte siguientes. |
| M7 | 27 a 30 | Olas O3/O4, estabilización, VE-01 y congelamiento posterior a aceptación R2. |
| M8 | 31 a 35 | Campaña y continuidad; sprint 17 reservado para estabilización. |
| M9 | 36 a 39 | G2 al inicio de semana 36; habilitar evolución R3 después de autorización. |
| M10 | 40 a 43 | Devoluciones elegibles y ampliación de observabilidad aceptadas. |
| M11 | 44 a 48 | Medir devoluciones y ejecutar experimento autorizado, máximo cuatro semanas. |
| M12 | 49 a 52 | Evaluar experimento, objetivos, transferencia y cierre con responsables. |

Se proponen cinco equipos en sprints 1–4, seis en 5–15 y cuatro en 16–26. El sexto está disponible en semana 9 y usa el sprint 5 para arranque; produce desde el 6. El sprint 1 reserva cinco unidades de arranque y el 17 cuatro de estabilización. El calendario completo, parámetros y cálculo se conservan en la [base de ejecución](base_ejecucion.md).

F1 conserva 56 efectivos, F2 24 y F3 40. Campaña dispone de seis efectivos y R3 posterior a G2 de 34; el sprint 18 se divide a mitad de periodo. Se pagan 130 equipo-sprints, diez reservados sin producción y 120 efectivos. La conversión 130 × 12/26 × 14 da 840 MM exactos: COST-01 queda sin colchón de redondeo. La reducción a cuatro equipos antes de campaña requiere ratificación de funciones/soporte por Operaciones.

En el escenario de respuesta al estrés se difieren E10/E8b y se reduce un equipo solo después de G2, con contrato cancelable/prorrata. La capacidad posterior pasa a 25,5 frente a esfuerzo 18,9667; las 104 unidades siguientes representan la referencia completa, no el alcance reducido.

## Distribución de esfuerzo por etapa

Unidad: equipo-sprint de referencia. F1 incluye R0/R1; F2 expansión y preparación; campaña excluye la estabilización ya reservada del sprint 17; R3 comienza tras G2. Los cuatro decimales conservan medias y sumas, no precisión observada. La descomposición supone cortes funcionales separables que Tecnología debe validar: todo control imprescindible del flujo que se abre debe estar terminado, aunque la épica continúe para otras interfaces.

| Épica | F1: R0/R1 | F2: R2 | Campaña M8 | R3 tras G2 | Total PERT |
| --- | ---: | ---: | ---: | ---: | ---: |
| E1 | 14,6667 | 0,0000 | 0,0000 | 0,0000 | 14,6667 |
| E2 | 9,0000 | 3,0000 | 1,0000 | 4,0000 | 17,0000 |
| E3 | 8,0000 | 3,0000 | 1,0000 | 3,0000 | 15,0000 |
| E4 | 4,5333 | 4,0000 | 0,5000 | 0,3000 | 9,3333 |
| E5 | 4,0000 | 4,0000 | 0,5000 | 0,0000 | 8,5000 |
| E6 | 2,0000 | 1,5000 | 1,0000 | 1,6667 | 6,1667 |
| E7 | 0,5000 | 4,0000 | 0,6667 | 0,0000 | 5,1667 |
| E8a | 3,0000 | 0,0000 | 0,0000 | 0,0000 | 3,0000 |
| E8b | 0,0000 | 0,0000 | 0,0000 | 4,0000 | 4,0000 |
| E9 | 0,0000 | 0,0000 | 0,0000 | 9,5000 | 9,5000 |
| E10 | 0,0000 | 0,0000 | 0,0000 | 5,3333 | 5,3333 |
| E11 | 2,0000 | 3,5000 | 0,3333 | 0,5000 | 6,3333 |
| Total | 47,7000 | 23,0000 | 5,0000 | 28,3000 | 104,0000 |

Las cargas F1/F2/F3 son exactamente 47,7/23/33,3 antes del redondeo de filas. Campaña usa 5/6 = 83,33%; R3 usa 28,3/34 = 83,24%. R2 mantiene 23/24 = 95,83%. Estas holguras agregadas no demuestran disponibilidad por especialidad ni financian automáticamente trabajo adicional.

### Primera salida usable antes de medir

Se propone un corte mínimo de 36 hasta el fin del sprint 8, semana 16, contra capacidad efectiva 38: **94,74%** de uso. El sexto equipo arranca en sprint 5 y produce desde el 6. Las 11,7 unidades posteriores a salida se distribuyen en sprints 9–11, con capacidad 18, para completar cobertura, estabilizar y preparar expansión. El corte conserva la ventana de observación hasta M5 bajo la disponibilidad asumida en semana 9.

| Épica con carga F1 | Hasta primera salida, semana 16 | Después de salida, hasta G1 |
| --- | ---: | ---: |
| E1 | 11,0000 | 3,6667 |
| E2 | 7,0000 | 2,0000 |
| E3 | 6,5000 | 1,5000 |
| E4 | 3,5000 | 1,0333 |
| E5 | 3,0000 | 1,0000 |
| E6 | 1,5000 | 0,5000 |
| E7 | 0,0000 | 0,5000 |
| E8a | 2,0000 | 1,0000 |
| E11 | 1,5000 | 0,5000 |
| Total | 36,0000 | 11,7000 |

El corte de 36 debe incluir el flujo real completo en diez tiendas: disponibilidad/reserva, pedido/conciliación, preparación/retiro, permisos, alertas atendidas y reversión. No basta cumplir una suma de esfuerzo. La parte posterior solo amplía o mejora un flujo que ya cumple su aceptación. Si el corte mínimo no cabe, revisar viabilidad/capacidad de inmediato; no esperar G1 ni reducir controles.

Base de cuatro semanas propuesta en semanas 9–12; uso comparable en 17–20; análisis hasta semana 22. Un piso de 1.000 pedidos por fase en 28 días calendario equivale a unos 35,7 diarios entre diez tiendas; confirmar horarios y volumen elegible. Es demanda requerida para ese piso, no volumen observado ni garantía estadística. Si no hay muestra comparable, reportar resultado inconcluso y revisar la decisión de expansión.

## Roles que deben confirmar dedicación

| Función empresarial propuesta | Trabajo / periodo | Fuente de capacidad por conciliar |
| --- | --- | --- |
| Tecnología/integración y proveedor WMS | Datos, interfaces, reservas, conciliación y recuperación; desde R0 y cada ola | E1/E2/E3 y COST-01; cambios específicos del proveedor en COST-03, sin duplicar horas. |
| PO e-commerce y representante de tiendas | Criterios, prioridades y aceptación funcional; disponibles desde M1 | Dedicación empresarial explícita entre COST-01/COST-07, según roles y frontera de costo. |
| QA, seguridad y operación técnica | Pruebas, controles, alertas, carga y atención; antes de cada exposición | E6/E7/E8a; separar pentest externo COST-05 y herramientas COST-04. |
| Habilitación local/remota | Cuatro células de dos funciones, 25 jornadas equivalentes dentro de las ventanas de olas | E11/COST-01 aporta 210 persona-días brutos; COST-06 financia veinte adicionales de preparación de campo y traslados. |
| Personal y gerencia de tienda/CD | Preparación de datos, turnos, formación y aceptación del sitio | Costo y reemplazo de turnos dentro de COST-06 o aporte interno declarado; confirmar antes de G1. |
| PM/Arquitectura/Finanzas y facilitación | Dependencias, forecast, autorización y acompañamiento | COST-07 o dedicación ya incluida en equipos; una persona no se cobra en ambos. |

La tabla asigna funciones y ventanas, sin inventar nombres empresariales ni FTE disponibles. La revisión de Rogelio debe comprobar carga por especialidad y fronteras de costo. Esa validación no se sustituye con el promedio de seis personas por equipo.

## Dimensionamiento propuesto de las 58 altas

Cuatro células completan habilitación y acompañamiento con 25 jornadas equivalentes de actividad, distribuidas en los treinta días de olas. Se conservan diez días posteriores para corrección/VE-01, dentro de cuarenta. La dedicación se programa por sitio y relevo, sin reservar a las ocho funciones a tiempo completo durante los treinta días.

| Parámetro | Valor propuesto | Uso |
| --- | ---: | --- |
| CEL-01 | 58 | Altas adicionales. |
| CEL-02 | 4 | Células. |
| CEL-03 | 2 | Funciones por célula. |
| CEL-04 | 25 | Jornadas equivalentes de actividad. |
| CEL-05 | 0,75 | Disponibilidad efectiva supuesta. |
| CEL-06 | 1 | Día de célula de habilitación por tienda, dos persona-días. |
| CEL-07 | 3,5 | Equipo-sprints de E11/R2. |
| CEL-08 | 6 | Personas por equipo de referencia. |
| CEL-09 | 10 | Días hábiles por sprint. |

Habilitación 116 + acompañamiento 29 = **145 persona-días efectivos**, frente a **150** disponibles. Células: 200 persona-días brutos; preparación transversal: treinta. De ese total de 230, E11/R2 aporta 210 y COST-06 veinte de campo. Se conserva la carga de desarrollo R2 de 23/24. La [base](base_ejecucion.md) asigna 2,1538 MM para ese campo y una bolsa propuesta de diez MM de traslados dentro de los 45 de COST-06; el resto disponible es 32,8462.

| Habilitación por tienda | Demanda efectiva, incluido acompañamiento | Jornadas equivalentes de células, redondeadas arriba | Más diez días de preparación |
| --- | ---: | ---: | ---: |
| Un día de célula | 145 | 25 | 35 |
| 1,5 días de célula | 203 | 34 | 44 |
| Dos días de célula | 261 | 44 | 54 |

La primera fila cabe bajo los supuestos; las otras requieren reducir cobertura o reestimar recursos antes de comprometer. El 75% y la valoración de campo son hipótesis, no rendimiento observado ni salario cotizado.

La geografía del caso va de Arica a Punta Arenas (p. 3). Agrupar tiendas por región/CD, combinar referentes locales con apoyo técnico remoto y cotizar itinerarios contra la bolsa. CD2/CD3 se preparan/prueban en ventana propuesta 17–22, con tareas en E2/E11 y proveedor antes de sus olas. Identificar localidad, CD, traslado, turno y responsable en la programación; la cobertura nacional no se demuestra con capacidad agregada.

La aceptación por patrón y listas delegadas evita reunir a todos los especialistas por cada tienda. Cada ola conserva datos, formación, soporte y estabilidad como condiciones. Si tiempos o costos exceden la base, sponsor/comité cambia cobertura/fecha con impacto explícito en beneficios.

## Estado para integrar y defender

El anexo integra frontera, aceptación, calendario y olas con una base cuantificada de cuatro células y sexto equipo anticipado. Falta revisión colectiva del alcance y contraste de Rogelio sobre especialidades, precios/contratos y flujo por tramo. La fecha de carga y el formato final siguen sujetos al aula. No se declara ejecución, financiación o aprobación empresarial.
