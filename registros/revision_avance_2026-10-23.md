# Comparación del avance del equipo, 23 de octubre

**Conviene actualizar la propuesta con este avance.** WSJF, estimación por épica, capacidad escalonada, presupuesto y financiación reemplazan las tablas ilustrativas/incompletas de 05 y 06. Se conserva el [texto recibido](../insumos/avance_equipo_2026-10-23.md); las precisiones de esta revisión no se atribuyen a sus autores como acuerdos ya aceptados.

Actualización posterior del mismo día: Maverick desarrolla [alcance/roadmap y plan de apoyo](plan_alcance_roadmap.md). Ya hay una propuesta de calendario, reparto por épica/etapa, funciones, corte piloto y mecanismo de altas. Los hallazgos siguientes conservan el diagnóstico de la integración inicial; revisión de especialidades, contratos/costos y ratificación colectiva siguen pendientes. No presentar aquellas propuestas nuevas como datos recibidos del equipo.

## Qué mejora y se incorpora

- WSJF ordena opciones y se complementa con precedencias y restricciones obligatorias. No es necesario conservar nuestra matriz ponderada como otro ranking vigente.
- Observabilidad básica E8a desde R1 y centralizada E8b posterior resuelven una ambigüedad importante del primer borrador.
- E1 a E11, con E8 dividido, permiten estimar 12 filas y relacionarlas con el alcance CAP/PAQ sin renombrar toda la documentación.
- Esfuerzo, capacidad, categorías y tramos tienen cantidades que pueden calcularse y defenderse como supuestos del ejercicio.
- Mantienen B, híbrido, 10 tiendas/M5 y 68/M7; por sí mismo el nuevo texto no aprueba los supuestos adicionales que desarrollamos el 22.

## Cálculos comprobados

| Concepto | Resultado | Lectura |
| --- | --- | --- |
| PERT por épica y total | O 68; M 99; P 160; E 104 equipo-sprints | Correctos. Usar valores completos antes de redondear. |
| Varianza total bajo independencia | 24,2222; desviación 4,9216 equipo-sprints | El 4,9 recibido es correcto. |
| Aproximaciones normales propuestas | E + 0,84σ = 108,1342; E + 1,65σ = 112,1207 | Se pueden conservar como sensibilidad teórica, explicando supuestos; no demuestran confianza real de fecha. |
| Capacidad efectiva | 56 + 24 + 40 = 120 equipo-sprints | Correcta para la tabla de sprints recibida. Falta conciliarla con meses, roles y calendario pagado. |
| Cargas por tramo | 47,7 + 23,0 + 33,3 = 104,0 | Correcta su suma; falta distribución de cada épica a los tramos. |
| Utilización R1/R2 y precongelamiento | 85,18%; 95,83%; 88,375% conjunto | No sustituir el pico de R2 por el promedio; mover trabajo exige dependencias y disponibilidad. |
| Presupuesto base y extremos | Base 1.330 MM; O 1.215; P 1.500 | Sumas correctas de siete categorías; montos son supuestos recibidos, sin cotizaciones verificadas. |
| Reserva y tramos | 170 MM; 675 + 345 + 310 = 1.330; total 1.500 | Correctos. Reserva = 12,78% de base; extremo alto consume toda la reserva. |

## Ajustes necesarios para una defensa consistente

| ID | Prioridad | Hallazgo | Tratamiento propuesto y fundamento |
| --- | --- | --- | --- |
| REV23-01 | Alta | «Viable con confianza entre 80% y 95%» y compromiso P80 por release | Conservar cálculo PERT como aproximación bajo independencia/normalidad. La suma de esfuerzo no incorpora red, concurrencia, roles ni riesgos compartidos; faltan asignaciones por release para calcular percentiles por tramo. Presentaciones 05 pp. 5/6/9 y 06 pp. 5 a 9. |
| REV23-02 | Alta | 26 sprints/año, 24 efectivos, 14 MM por equipo-mes y 7 por equipo-sprint se usan como equivalencias exactas | 840/120 = 7 es costo medio asignado por equipo-sprint efectivo, no tarifa contractual de dos semanas. La tabla tiene 129 equipo-sprints pagados si sprint 1 usa 5 equipos y sprint 17 usa 4. Si 26 sprints cubren 12 meses, equivalen a 59,54 equipo-meses, cerca de 60. No afirmar que necesariamente faltan 63 MM usando además dos sprints por mes: eso mezclaría calendarios. Conciliar fechas/dotación en un solo calendario y conservar 840 como supuesto redondeado hasta hacerlo. |
| REV23-03 | Alta | Cuatro equipos «después de Black Friday», pero tabla los reduce desde sprint 16 y R3 incluye mes 8 | Aclarar fecha de cambio de dotación. Mes 8 está financiado por tramo 2 y orientado a campaña; no comprometer entregas R3 antes de G2/M9. La capacidad poscongelamiento no es automáticamente capacidad autorizada para todo R3. |
| REV23-04 | Alta | 47,7/23/33,3 no tienen matriz de contribución por épica; R2 usa 96% | Mantener cargas como distribución propuesta, no asignación demostrada. Desglosar E1 a E11 por tramo/rol y revisar integración, pruebas, formación y aceptación local. Nuestra hipótesis de cinco brigadas queda como alternativa anterior, no otra dotación añadida al nuevo presupuesto. |
| REV23-05 | Alta | Costos «cotización» e «históricos de la empresa» no tienen respaldo en el material | Cambiar a valores supuestos del equipo y método que se aplicaría. No afirmar consultas reales. El caso solo aporta alternativas y techo (pp. 5/7); sesión 05 p. 5 exige base de estimación explícita. |
| REV23-06 | Alta | OMS 180 incluye implementación y hay E3 de equipo; WMS 70, seguridad 35 y capacitación 45 también pueden coincidir con esfuerzo estimado | Distinguir trabajo contratado/incluido y trabajo de equipos. Los 840 ya pagan la capacidad para E1 a E11: no sumar otra vez 104 × 7 como gasto adicional. Falta frontera de cada categoría y asignación a PAQ; comprobar costos internos/tienda y recurrentes. |
| REV23-07 | Alta | Reserva 170 «cubre» extremo externo y también ERP sin API/capacidad insuficiente | El extremo alto declarado sí suma 1.500 y consume exactamente 170 sobre base. No garantiza cubrir además equipos extra, demora, consumo fuera de rangos o riesgos correlacionados. No son dos reservas. Si se exceden rangos, decidir alcance/capacidad/techo antes de comprometer. |
| REV23-08 | Media | «Todo R3 es variable de ajuste», aunque devoluciones ≥85% es objetivo M12 | Diferir primero experimento/ruteo avanzado/centralización adicional según impacto. Recortar devolución o integración necesaria exige revisar Charter/beneficios. Seguridad y observabilidad básica permanecen obligatorias. |
| REV23-09 | Media | Experimento 3–5 tiendas frente a nuestra propuesta de 2 y tope incremental 30 MM | Priorizar 3–5 del avance recibido. Retirar 2 tiendas/30 MM como condiciones vigentes; no son decisiones del equipo. E10 tiene esfuerzo esperado 5,33 equipo-sprints, ya dentro de capacidad; costo imputado no es gasto nuevo ni equivale por sí solo a costo incremental. Delimitar pedidos/duración/exposición en G2 sin mezclar escenarios. |
| REV23-10 | Media | Se declara rango ±30–40% | Mostrar los rangos existentes: esfuerzo 68 a 160 respecto de 104 implica −34,62%/+53,85%; costo 1.215 a 1.500 respecto de 1.330 implica −8,65%/+12,78%. Son extremos supuestos, no intervalos de confianza; no agregar otro porcentaje sin base. |
| REV23-11 | Media | Velocidad de sprints 1–3 se compara contra 80% de lo supuesto, pero sprint 1 se descuenta por arranque | Recalibrar con periodos comparables de cada equipo, excluyendo arranque/estabilización. No comparar story points entre equipos. Seis a ocho semanas no garantizan automáticamente un histórico suficiente/estable para Monte Carlo. |
| REV23-12 | Media | IA «no mueve ningún KPI» y ERP es de baja incertidumbre por requisitos conocidos | Mantener exclusiones por falta de necesidad/valor incremental demostrado en este horizonte, no imposibilidad de aportar. Integración conocida como requisito puede ser incierta como solución. Conservar correcciones de 02 en vez de reintroducir afirmaciones del primer borrador. |
| REV23-13 | Media | Business Case 1.3 describe B y 1.4 queda inconcluso; alcance incluido del Charter omite devoluciones pese a R3/objetivo | Conservar comparación A/B/C/no actuar, beneficios, costo y supuestos de nuestra integración; añadir explicitud de devoluciones. No reemplazar 01/02/03 por un texto menos completo. Restituir desigualdades y requisito «dentro de los primeros cinco meses» del enunciado. |

## Cómo queda la versión común

05 adopta WSJF y secuencia del equipo; 06 integra las cifras recibidas como estimación preliminar, con cálculos verificados y limitaciones visibles. 01/03 incorporan base 1.330, reserva 170 y primer tramo 675 sin simular autorización. 04 agrega equivalencias E/CAP/PAQ. 07 conserva 68/M7, añade la carga por tramo y registra calendario/recursos por conciliar.

El escenario del 22 queda como antecedente de detalle: sus brigadas y 2 tiendas/30 MM experimentales no se suman ni se imponen al avance actual. Piloto 1 CD/2 familias, umbrales SUP-16 y cantidades de formación son propuestas previas pendientes de ratificar, no condiciones declaradas por el nuevo texto. El equipo debe alinear la estimación con el alcance que efectivamente decida defender.

## Antes de cerrar la entrega

1. Rogelio y Maverick: una tabla calendario/dotación/capacidad y una matriz épica → tramo/rol; identificar preparación/soporte de campaña M8 y distribución R1/R2.
2. Revisar fronteras de costos y si los 840 son monto contratado fijo o estimación de dedicación; no añadir costos de brigadas por duplicado.
3. Confirmar alcance del experimento 3–5 tiendas y qué puede diferirse sin incumplir objetivos; ratificar o modificar catálogo/CD y metas piloto previas.
4. Mantener probabilidades como aproximaciones condicionales, actualizar láminas de costo/autorización y ensayar sensibilidad. Fecha/formato de carga siguen sujetos al aula.
