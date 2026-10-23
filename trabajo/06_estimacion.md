# 6. Estimación y tratamiento de incertidumbre

**Responsable: Rogelio. ESC-02, propuesta para revisión del equipo. Actualización: 23-10-2026.** Se estiman 104 equipo-sprints de referencia frente a 120 efectivos, con el sexto equipo desde sprint 5 y cuatro células, con presupuesto base 1.330 + reserva 170 = 1.500 MM CLP. Las cifras [recibidas del equipo](../insumos/avance_equipo_2026-10-23.md) son supuestos del ejercicio: no hay cotizaciones, históricos empresariales ni capacidad contratada verificados. La [comparación](../registros/revision_avance_2026-10-23.md) conserva los fundamentos de integración.

## 6.1 Técnica y base

| Componente | Técnica propuesta | Precisión de evidencia |
| --- | --- | --- |
| Integración, conciliación, controles y campaña | Analogía y tres puntos PERT | Requisitos/controles conocidos no vuelven conocida la capacidad de APIs o la solución. Rangos recibidos son supuestos, no históricos observados. |
| APIs/disponibilidad con Kanban | PERT de alto nivel; throughput/ciclo para recalibrar | Usar flujo empírico cuando exista suficiente información comparable y estable; no declarar Monte Carlo realizado. |
| OMS, cambios WMS y cloud | Paramétrica y futura validación contractual/proveedores | «Cotización» es método de contraste previsto; los montos actuales no son ofertas obtenidas. |
| C&C, app, devoluciones y experimento | Comparación relativa por equipo y conversión a equipo-sprints | Seis personas por equipo es supuesto de normalización, no prueba de productividad equivalente. No agregar story points entre equipos. |
| Proyecto | PERT de esfuerzo agregado + presupuesto por categoría + reserva | Escenarios aritméticos no garantizan duración/calendario ni confianza de plazo. |

La base de capacidad supone equipos de unas seis personas, sprints de dos semanas y 26 periodos en el año, de los cuales se excluyen arranque y estabilización para obtener 24 efectivos. El calendario propuesto usa cinco equipos en sprints 1–4, seis en 5–15 y cuatro desde 16, antes de campaña. El costo medio supuesto es 14 MM por equipo-mes, con provisión de 840 MM. También se supone un OMS por suscripción con proveedor de implementación y APIs/eventos útiles en ERP. Cada supuesto requiere contraste técnico, operativo y contractual.

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

**Base integrada:** el sexto equipo está disponible en semana 9, arranca en sprint 5 y entrega desde el 6. Se pagan 130 equipo-sprints y se reservan diez para arranque/estabilización; quedan 120 efectivos. El corte piloto conserva **36/38 = 94,74%**. Parámetros y calendario: [base de ejecución](../registros/base_ejecucion.md).

| ID | Periodo / sprints efectivos propuestos | Capacidad | Carga recibida | Uso |
| --- | --- | ---: | ---: | ---: |
| F1 | R0/R1: sprints 2–11; cinco efectivos en 2–5 y seis en 6–11 | 56 | 47,7 | 85,18% |
| F2 | R2: sprints 12–15, 6 equipos | 24 | 23,0 | 95,83% |
| F3 | Campaña y R3: sprint 16 y 18–26, 4 equipos | 40 | 33,3 | 83,25% |
| Total | 24 sprints efectivos | 120 | 104,0 | 86,67% |

La suma está correcta. R1/R2 conjunto: 70,7/80 = 88,375%. El 96% de R2 sigue siendo una restricción real del plan propuesto: adelantar trabajo requiere interfaces, ambiente, personas y aceptación disponibles. El [plan de apoyo de Maverick](../registros/plan_alcance_roadmap.md) ya propone una matriz por épica → R0/R1/R2/campaña/R3, conservando estas cargas y medias PERT. Distingue funciones y ventanas, pero requiere revisar dedicación por especialidad; no es una medición ni una asignación de personas contratadas.

El calendario del [plan de apoyo](../registros/plan_alcance_roadmap.md) utiliza 52 semanas/26 sprints y separa capacidad 6 para campaña y 34 para R3 posterior a G2, con cargas 5/28,3. La reducción a cuatro equipos desde sprint 16 ocurre antes de campaña y requiere aceptación de Operaciones; disponer de personal no autoriza anticipar contenido R3.

La provisión distingue pago y producción: 130 pagados menos diez reservados = 120 efectivos. Son 60 equipo-meses a 14 MM, **840 exactos**, sin colchón de redondeo. El anticipo del sexto equipo consume el redondeo previo, sin agregar gasto sobre COST-01 bajo esta convención. La disponibilidad en semana 9 es supuesto contractual. El cociente 840/120 = 7 MM es asignación por unidad efectiva, no tarifa por sprint pagado; esa tarifa es 14 × 12/26 = 6,4615 MM.

Las cuatro células tienen 200 persona-días brutos de actividad y treinta de preparación. E11/R2 aporta 210; los veinte restantes son capacidad de campo en COST-06. Se preserva holgura de R2 y se distingue ese campo del trabajo de desarrollo. Dentro de COST-06 = 45 MM se asignan 2,1538 a veinte persona-días de campo, diez a una bolsa de traslados y 32,8462 al resto de adopción/formación/operación. Son asignaciones académicas pendientes de ratificación/cotización, no gastos adicionales sumados de nuevo a 1.330.

## 6.5 Presupuesto preliminar por categoría

Unidad: **millones de CLP**. Valores supuestos del equipo. Base no significa costo esperado calculado por PERT monetario; O/P son extremos declarados de categoría. Impuestos, costo integral de equipo, condiciones de proveedor y operación posterior a M12 deben precisarse.

| ID | Categoría | Base | O | P | Técnica / frontera por validar |
| --- | --- | ---: | ---: | ---: | --- |
| COST-01 | Capacidad de equipos | 840 | 840 | 1008 | Referencia del equipo; estrés +20% de tarifa/costo. Rango supuesto, no cotizado; capacidad y esfuerzo se analizan aparte. |
| COST-02 | OMS año 1 y partner de implementación | 180 | 140 | 240 | Supuesto a contrastar; separar partner de E3/configuración propia. |
| COST-03 | Adaptaciones proveedor WMS | 70 | 50 | 100 | Supuesto a contrastar; separar entrega proveedor de integración propia E2. |
| COST-04 | Cloud y observabilidad | 70 | 50 | 100 | Paramétrica supuesta; consumo, herramientas y licencias, no duplicar ingeniería E8. |
| COST-05 | Seguridad externa/herramientas | 35 | 25 | 50 | Analogía hipotética; distinguir pentest externo de trabajo E6. |
| COST-06 | Adopción, capacitación y rollout local | 45 | 30 | 70 | Incluye veinte persona-días de campo 2,1538 MM y bolsa de traslados diez, dentro de 45; resto 32,8462 para adopción/operación. Cotizar y conciliar fronteras con E11. |
| COST-07 | Gobierno PM/Arquitectura/PMO | 90 | 80 | 100 | Analogía hipotética; evitar cobrar otra vez personas ya en equipos. |
| Subtotal | Siete categorías | 1330 | 1215 | 1668 | Sensibilidad combinada; excede techo en extremo alto. |

| Concepto | MM CLP | Lectura |
| --- | ---: | --- |
| Base de categorías | 1330 | Cercana a referencia B del caso 1350, sin probar asequibilidad de todo alcance. |
| Reserva de contingencia | 170 | 12,78% de base; gobernada por comité. |
| Marco preliminar total | 1500 | Base + reserva, igual al techo del caso. |
| Extremo alto de categorías | 1668 | Excede el techo 1.500 en 168; exige revisar alcance, tarifa o compromisos. |

La sensibilidad aislada +20% en COST-01 agrega 168 MM y deja dos de reserva si lo demás se mantiene en base. El extremo combinado bruto 1.668 supera el techo en 168. La respuesta escalonada de la base lleva ese escenario a 1.497,0923 únicamente si se obtienen reducción contractual y topes; la tabla siguiente describe su secuencia. El presupuesto base 1.330 + reserva 170 se conserva como envolvente propuesta; absorber el estrés requiere una decisión sobre alcance/precio/contratos. La reserva se consume una sola vez. Las 104 unidades ya forman parte de la capacidad pagada; su costo no se suma de nuevo sobre 840.

Rango de costo frente a base: −8,65%/+25,41%; esfuerzo O/P frente a 104: −34,62%/+53,85%. No afirmar un ±30–40% calibrado ni presentar esos extremos como intervalos probabilísticos.

El rango de equipos es un estrés académico +20%, sin cotización; 14 MM/equipo-mes equivale a 2,3333 MM/persona-mes bajo seis integrantes. Confirmar dedicación y composición del costo integral antes de defenderlo como tarifa de mercado. La protección de campaña puede comparar cinco equipos en sprints 16–18, +19,3846 MM, o seis en 16–17, +25,8462 MM, frente a cuatro en la referencia. Son opciones de soporte a autorizar con Operaciones; consumen la misma reserva que el resto de riesgos. Se mantiene abierto STK-03 hasta asignar funciones y costo.

Costos que requieren línea de conciliación: dispositivos compatibles = cantidad faltante × costo unitario, o reutilización con inventario/prueba; conteos y operación diaria = minutos activos × volumen/frecuencia × costo por hora; acompañamiento = horas por sitio/turno; operador Ship-from-store = pedidos × tarifa más cargos de prueba/devolución, dentro de su exposición autorizada; OMS/cloud/soporte después de M12 = recurrentes del horizonte económico. Cada línea tendrá categoría, responsable y financiación. Su monto pendiente significa costo por resolver, no exclusión gratuita de la base.

### Política de respuesta al estrés

Diferir E10/E8b permite reducir un equipo externo tras G2; no genera ahorro mientras la capacidad siga contratada. La [tabla EST-01 a EST-06](../registros/base_ejecucion.md) conserva los cálculos verificables:

- Estrés bruto: 1.668 MM.
- Reducción cancelable tras G2: −65,9077; quedan 1.602,0923.
- Tope OMS 180 frente a extremo 240: −60; quedan 1.542,0923.
- Tope WMS 70 frente a 100: −30; quedan 1.512,0923.
- Tope cloud/observabilidad 85 frente a 100: −15; quedan 1.497,0923.

Se propone exigir precio máximo y aceptación por hitos, además de controlar consumo cloud y conservar condiciones obligatorias. Si las ofertas no aceptan los topes o impiden calidad/continuidad, el comité cambia cobertura/arquitectura o reconsidera C antes de comprometer más de 1.500. El margen condicionado de 2,9077 es estrecho; no se presenta como reserva robusta o ahorro ya conseguido. La base de inversión sigue en 1.330 + 170.

## 6.6 Financiación propuesta por tramos

| ID | Momento de autorización propuesto | Cubre | MM CLP |
| --- | --- | --- | ---: |
| T1 | G0/M1 | R0/R1, M1–M5, incluida mayor parte de OMS | 675 |
| T2 | G1/M5 | R2 y campaña, M6–M8 | 345 |
| T3 | G2/M9 | R3, M9–M12 | 310 |
| RES | Comité, por riesgos registrados | Reserva, fuera de las liberaciones base | 170 |

T1+T2+T3 = 1.330; más reserva = 1.500. La suma es correcta. Falta distribución categoría/mes/tramo para demostrar que las cuotas cubren cada obligación contractual y dotación; no simular que los tramos están aprobados. Contrato OMS por hitos/aceptación y VT-01/M2 antes de compromisos irreversibles.

## 6.7 Actualización y decisiones pendientes

### Salida contractual y gasto evitable por gate

Proponer capacidad externa por fase, con opción de reducción/renovación en G1/G2, preaviso, penalidades y transición de soporte acordados antes de contratar. Aplicar hitos de aceptación al OMS y separar compromisos mínimos de licencias de servicios cancelables. Personal interno reasignable libera capacidad, pero solo evita caja si cambia el gasto efectivo. Si el proveedor exige contratar el año completo, mostrar esa obligación y revisar el valor real de los gates.

En G1 quedan **655 MM de base** y en G2 **310 MM**: son saldos máximos por conciliar, no ahorros garantizados. Gasto evitable = saldo futuro − obligaciones irrevocables − penalidades − transición/cierre no incluidos, con piso cero cuando corresponda. La reserva pendiente tampoco es gasto ya comprometido. Finanzas presenta esa tabla contractual antes de solicitar el siguiente tramo.

### Sensibilidad conjunta y respuesta al sobreesfuerzo

La suma de desviaciones de épica es 15,3333. Como extremo de correlación positiva total, E + 1,65 × suma de σ = **129,3 equipo-sprints**, frente a 112,1207 bajo independencia. Es sensibilidad del esfuerzo, sin probabilidad de fecha validada. La holgura aritmética 104/120 existe sin independencia; lo que cambia es su interpretación ante riesgos conjuntos.

Para la suma pesimista 160 frente a referencia 120, diferir E10 completo elimina sus 9 unidades pesimistas y deja 151; diferir además E8b elimina 6 y deja **145**, todavía 25 por encima. La base corregida de 120 efectivos conserva una brecha de 25. Mantener seguridad, monitoreo básico, integración imprescindible y devolución comprometida. El comité debe revisar cobertura, horizonte o alternativa y reestimar; quitar medias PERT de una suma pesimista no demuestra que se cubra la diferencia. Un ERP sin integración viable puede exigir cambiar B, no solo usar reserva.

Reestimar con evidencia de cada equipo/flujo en VT-01 y gates. El inicio del sprint 3 es oportunidad de revisar, no garantía de velocidad representativa. Si la entrega comparable cae por debajo del 80% del forecast interno acordado, investigar dependencia/capacidad y elevar impacto; excluir arranque/estabilización del comparativo. No esperar a G1 para descubrir un bloqueo crítico de API.

Monte Carlo se plantea solo cuando haya histórico suficiente, comparable y razonablemente estable; seis a ocho semanas por sí solas no lo garantizan. Reservas requieren aprobación del comité y no financian alcance nuevo por defecto. Recortar E9 altera objetivo de devolución; no declarar todo R3 prescindible sin actualizar Charter/beneficios.

Antes de cerrar: revisar calendario/carga propuestos en 07, dedicación por especialidad, fronteras de doble conteo y asignación de categorías a PAQ y meses. El piloto Ship-from-store conserva **3 a 5 tiendas** como propone el equipo; 04 concreta máximo cuatro semanas/300 pedidos como hipótesis para ratificación. El techo monetario de exposición se autoriza en G2 antes de iniciar. El gasto del experimento debe permanecer dentro del marco autorizado, sin duplicar E10 sobre la capacidad ya presupuestada.

## 6.8 Revisión de dotación por función y despliegue

La [revisión complementaria](../insumos/evidencia_logistica_y_valor.md) motiva revisar tamaño y composición, sin demostrar una dotación alternativa suficiente. El escenario recibido de 5/6/4 equipos se conserva como referencia por contrastar, no como número de equipos exclusivamente de programadores validado por la industria. Separar tres cargas: desarrollo/integración de producto, habilitación con acompañamiento intensivo y operación/soporte diario por turno.

Rogelio y Maverick proponen una matriz por función × periodo × dedicación que vincule E1–E11 con configuración OMS/WMS, integración, QA, seguridad, producto, tiendas, logística y soporte. Una persona no cubre simultáneamente dos dedicaciones completas. La carga y costo del proveedor se separan de equipos propios; referentes locales, traslados y reemplazos también tienen costo o aporte interno declarado. CAP-01/02/03 y E11 deben cubrir las precisiones de 04; contrastarlo antes de tratarlas como incluidas.

Comparar una alternativa de menor dotación estable de desarrollo y mayor acompañamiento temporal en olas contra el escenario actual. Antes de elegirla, recalcular esfuerzo pendiente, especialidades, ruta de integración, capacidad por tramo, soporte de campaña y presupuesto. Reducir desarrolladores no reduce por regla de tres el PERT de 104 ni garantiza los mismos M5/M7. Si cambia la combinación de perfiles, justificar equivalencias en persona-días/función antes de reutilizar equipo-sprints homogéneos. No se registran ahorros o cambios de capacidad sin ese cálculo.

El [modelo económico logístico](../registros/modelo_retorno_logistico.md) se mantiene separado de este presupuesto: su sensibilidad de ventas/margen no autoriza fondos ni agrega una nueva partida de 9 MM/mes. Conciliar implementación y recurrentes por periodo evita restar un gasto dos veces al proyectar retorno.
