# 6. Estimación y tratamiento de incertidumbre

**Responsable: Rogelio. ESC-02, propuesta para revisión del equipo. Actualización: 23-10-2026.** Se estiman 104 equipo-sprints de esfuerzo frente a una capacidad propuesta de 120, con presupuesto base 1.330 + reserva 170 = 1.500 MM CLP. Las cifras [recibidas del equipo](../insumos/avance_equipo_2026-10-23.md) son supuestos del ejercicio: no hay cotizaciones, históricos empresariales ni capacidad contratada verificados. La [comparación](../registros/revision_avance_2026-10-23.md) conserva los fundamentos de integración.

## 6.1 Técnica y base

| Componente | Técnica propuesta | Precisión de evidencia |
| --- | --- | --- |
| Integración, conciliación, controles y campaña | Analogía y tres puntos PERT | Requisitos/controles conocidos no vuelven conocida la capacidad de APIs o la solución. Rangos recibidos son supuestos, no históricos observados. |
| APIs/disponibilidad con Kanban | PERT de alto nivel; throughput/ciclo para recalibrar | Usar flujo empírico cuando exista suficiente información comparable y estable; no declarar Monte Carlo realizado. |
| OMS, cambios WMS y cloud | Paramétrica y futura validación contractual/proveedores | «Cotización» es método de contraste previsto; los montos actuales no son ofertas obtenidas. |
| C&C, app, devoluciones y experimento | Comparación relativa por equipo y conversión a equipo-sprints | Seis personas por equipo es supuesto de normalización, no prueba de productividad equivalente. No agregar story points entre equipos. |
| Proyecto | PERT de esfuerzo agregado + presupuesto por categoría + reserva | Escenarios aritméticos no garantizan duración/calendario ni confianza de plazo. |

La base de capacidad supone equipos de unas seis personas, sprints de dos semanas y 26 periodos en el año, de los cuales se excluyen arranque y estabilización para obtener 24 efectivos. El calendario propuesto usa cinco equipos en sprints 1–5, seis en 6–15 y cuatro desde 16, antes de campaña. El costo medio supuesto es 14 MM por equipo-mes, con provisión de 840 MM. También se supone un OMS por suscripción con proveedor de implementación y APIs/eventos útiles en ERP. Cada supuesto requiere contraste técnico, operativo y contractual.

## 6.2 Esfuerzo por épica mediante PERT

Unidad: equipo-sprint de referencia. O es esfuerzo optimista, M el más probable y P el pesimista; E es la media PERT y σ su desviación aproximada. E = (O + 4M + P) / 6; σ = (P − O) / 6. El total usa valores completos antes de redondear las filas. O/P son escenarios supuestos de estimación, no mínimos/máximos garantizados ni percentiles medidos.

| ID | Épica | O | M | P | E | σ |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| E1 | Disponibilidad stock | 10 | 14 | 22 | 14,7 | 2,0 |
| E2 | APIs/integración ERP-WMS-POS | 12 | 16 | 26 | 17,0 | 2,3 |
| E3 | OMS configuración/integración | 10 | 14 | 24 | 15,0 | 2,3 |
| E4 | Click & Collect | 6 | 9 | 14 | 9,3 | 1,3 |
| E5 | App de preparación | 6 | 8 | 13 | 8,5 | 1,2 |
| E6 | Seguridad transversal | 4 | 6 | 9 | 6,2 | 0,8 |
| E7 | Preparación Black Friday | 3 | 5 | 8 | 5,2 | 0,8 |
| E8a | Observabilidad básica | 2 | 3 | 4 | 3,0 | 0,3 |
| E8b | Observabilidad centralizada | 2 | 4 | 6 | 4,0 | 0,7 |
| E9 | Devoluciones omnicanal | 6 | 9 | 15 | 9,5 | 1,5 |
| E10 | Experimento Ship-from-store | 3 | 5 | 9 | 5,3 | 1,0 |
| E11 | Rollout y gestión del cambio | 4 | 6 | 10 | 6,3 | 1,0 |
| Total | Doce filas, E8 desdoblada | 68 | 99 | 160 | 104,0 | 4,9 |

Bajo independencia: Σσ² = 24,2222 y σ total = 4,9216. No sumar desviaciones ni calcular con las desviaciones de fila ya redondeadas. E2 y otras épicas comparten dependencias, por lo que independencia es una simplificación, no un hecho.

## 6.3 Sensibilidad probabilística, no garantía de fecha

| Escenario teórico | Equipo-sprints | Uso de 120 | Interpretación |
| --- | ---: | ---: | --- |
| Esfuerzo esperado | 104,0 | 86,67% | Media PERT; no llamarla P50 empírico. |
| Aproximación normal 80%, E + 0,84σ | 108,1342 | 90,11% | Solo bajo independencia/normalidad supuestas y agregación de esfuerzo. |
| Aproximación normal 95%, E + 1,65σ | 112,1207 | 93,43% | Misma limitación; no demuestra probabilidad de entregar antes de campaña. |
| Suma pesimista de épicas | 160,0 | 133,33% | No cabe en capacidad propuesta; exige respuesta explícita. |

Estas aproximaciones describen sensibilidad del esfuerzo bajo independencia y normalidad supuestas. No incorporan una red de actividades con recursos y correlaciones, por lo que no permiten afirmar una probabilidad de entregar antes de campaña. La matriz por etapas de 07 tampoco proporciona distribuciones de incertidumbre para cada parte de épica. Por ello, las 74 unidades precongelamiento citadas en la fuente no constituyen un P80 de R1/R2 verificado; no se aplica automáticamente el σ total a ese subconjunto.

## 6.4 Capacidad y distribución de carga

| ID | Periodo / sprints efectivos propuestos | Capacidad | Carga recibida | Uso |
| --- | --- | ---: | ---: | ---: |
| F1 | R0/R1: sprints 2–11; 5 equipos en 2–5 y 6 en 6–11 | 56 | 47,7 | 85,18% |
| F2 | R2: sprints 12–15, 6 equipos | 24 | 23,0 | 95,83% |
| F3 | Campaña y R3: sprint 16 y 18–26, 4 equipos | 40 | 33,3 | 83,25% |
| Total | 24 sprints efectivos | 120 | 104,0 | 86,67% |

La suma está correcta. R1/R2 conjunto: 70,7/80 = 88,375%. El 96% de R2 sigue siendo una restricción real del plan propuesto: adelantar trabajo requiere interfaces, ambiente, personas y aceptación disponibles. El [plan de apoyo de Maverick](../registros/plan_alcance_roadmap.md) ya propone una matriz por épica → R0/R1/R2/campaña/R3, conservando estas cargas y medias PERT. Distingue funciones y ventanas, pero requiere revisar dedicación por especialidad; no es una medición ni una asignación de personas contratadas.

El calendario del [plan de apoyo](../registros/plan_alcance_roadmap.md) utiliza 52 semanas/26 sprints y separa capacidad 6 para campaña y 34 para R3 posterior a G2, con cargas 5/28,3. La reducción a cuatro equipos desde sprint 16 ocurre antes de campaña y requiere aceptación de Operaciones; disponer de personal no autoriza anticipar contenido R3.

La provisión de equipos exige distinguir capacidad efectiva y periodos pagados. Los sprints de arranque y estabilización añaden 5 y 4 unidades, respectivamente, a las 120 efectivas: se pagan 129 equipo-sprints. Bajo la conversión de 26 periodos a 12 meses, equivalen a 59,5385 equipo-meses; a 14 MM resultan 833,5385 MM. La propuesta conserva 840, con diferencia de redondeo de 6,4615 MM dentro de COST-01. El cociente 840/120 = 7 MM es asignación media por unidad efectiva, no tarifa contractual exacta.

Rogelio debe contrastar esta convención con contratos, calendario civil y costo mensual. Las tres células de habilitación propuestas en 04/07 forman parte de E11; no se agregan como otra dotación o gasto sobre los equipos presupuestados.

## 6.5 Presupuesto preliminar por categoría

Unidad: **millones de CLP**. Valores supuestos del equipo. Base no significa costo esperado calculado por PERT monetario; O/P son extremos declarados de categoría. Impuestos, costo integral de equipo, condiciones de proveedor y operación posterior a M12 deben precisarse.

| ID | Categoría | Base | O | P | Técnica / frontera por validar |
| --- | --- | ---: | ---: | ---: | --- |
| COST-01 | Capacidad de equipos | 840 | 840 | 840 | Paramétrica supuesta; costo por disponibilidad, no 104 × 7 adicional. |
| COST-02 | OMS año 1 y partner de implementación | 180 | 140 | 240 | Supuesto a contrastar; separar partner de E3/configuración propia. |
| COST-03 | Adaptaciones proveedor WMS | 70 | 50 | 100 | Supuesto a contrastar; separar entrega proveedor de integración propia E2. |
| COST-04 | Cloud y observabilidad | 70 | 50 | 100 | Paramétrica supuesta; consumo, herramientas y licencias, no duplicar ingeniería E8. |
| COST-05 | Seguridad externa/herramientas | 35 | 25 | 50 | Analogía hipotética; distinguir pentest externo de trabajo E6. |
| COST-06 | Adopción, capacitación y rollout local | 45 | 30 | 70 | Supuesto; aclarar turnos, traslados y preparación de sitios, y qué está en E11. El caso no informa ubicación de cada tienda. |
| COST-07 | Gobierno PM/Arquitectura/PMO | 90 | 80 | 100 | Analogía hipotética; evitar cobrar otra vez personas ya en equipos. |
| Subtotal | Siete categorías | 1330 | 1215 | 1500 | Suma de categorías, no cotizaciones verificadas. |

| Concepto | MM CLP | Lectura |
| --- | ---: | --- |
| Base de categorías | 1330 | Cercana a referencia B del caso 1350, sin probar asequibilidad de todo alcance. |
| Reserva de contingencia | 170 | 12,78% de base; gobernada por comité. |
| Marco preliminar total | 1500 | Base + reserva, igual al techo del caso. |
| Extremo alto de categorías | 1500 | Consume toda la reserva respecto de base; no sumar otros 170 para afirmar cobertura. |

El extremo alto sí cabe aritméticamente en 1.500 para esos rangos y capacidad fija. No garantiza cubrir además nuevos equipos, ERP sin API, demora o consumo fuera de rango. Si se usa reserva para una exposición, disminuye la disponible para las otras. Confirmar fronteras de categorías, contrato fijo de capacidad y distribución a PAQ. No sumar costos de 104 equipo-sprints otra vez sobre 840: están dentro de la capacidad pagada propuesta de 120.

Rango de costo frente a base: −8,65%/+12,78%; esfuerzo O/P frente a 104: −34,62%/+53,85%. No afirmar un ±30–40% calibrado ni presentar esos extremos como intervalos probabilísticos.

## 6.6 Financiación propuesta por tramos

| ID | Momento de autorización propuesto | Cubre | MM CLP |
| --- | --- | --- | ---: |
| T1 | G0/M1 | R0/R1, M1–M5, incluida mayor parte de OMS | 675 |
| T2 | G1/M5 | R2 y campaña, M6–M8 | 345 |
| T3 | G2/M9 | R3, M9–M12 | 310 |
| RES | Comité, por riesgos registrados | Reserva, fuera de las liberaciones base | 170 |

T1+T2+T3 = 1.330; más reserva = 1.500. La suma es correcta. Falta distribución categoría/mes/tramo para demostrar que las cuotas cubren cada obligación contractual y dotación; no simular que los tramos están aprobados. Contrato OMS por hitos/aceptación y VT-01/M2 antes de compromisos irreversibles.

## 6.7 Actualización y decisiones pendientes

Reestimar con evidencia de cada equipo/flujo en VT-01 y gates. El inicio del sprint 3 es oportunidad de revisar, no garantía de velocidad representativa. Si la entrega comparable cae por debajo del 80% del forecast interno acordado, investigar dependencia/capacidad y elevar impacto; excluir arranque/estabilización del comparativo. No esperar a G1 para descubrir un bloqueo crítico de API.

Monte Carlo se plantea solo cuando haya histórico suficiente, comparable y razonablemente estable; seis a ocho semanas por sí solas no lo garantizan. Reservas requieren aprobación del comité y no financian alcance nuevo por defecto. Recortar E9 altera objetivo de devolución; no declarar todo R3 prescindible sin actualizar Charter/beneficios.

Antes de cerrar: revisar calendario/carga propuestos en 07, dedicación por especialidad, fronteras de doble conteo y asignación de categorías a PAQ y meses. El piloto Ship-from-store conserva **3 a 5 tiendas** como propone el equipo; 04 concreta máximo cuatro semanas/300 pedidos como hipótesis para ratificación. El techo monetario de exposición se autoriza en G2 antes de iniciar. El gasto del experimento debe permanecer dentro del marco autorizado, sin duplicar E10 sobre la capacidad ya presupuestada.
