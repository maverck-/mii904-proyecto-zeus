# 1. Diagnóstico estratégico y Business Case

**ESC-02, propuesta para revisión del equipo. Actualización: 23-10-2026.** Se recomienda desarrollar la alternativa B por etapas, condicionando la inversión a viabilidad técnica, valor temprano y capacidad operativa. Los datos provienen del enunciado; las metas y decisiones adicionales son propuestas. La [revisión de integración](../registros/integracion_avance_equipo.md) conserva su procedencia.

## 1.1 Problema y oportunidad

**Declaración del problema:** M-GesPro Retail presenta una operación omnicanal con información de inventario desactualizada y visibilidad fragmentada de pedidos entre canales. El caso registra 7,8% de cancelaciones por stock, 7,2 horas de preparación media y 64% de devoluciones resueltas al primer contacto. Estas condiciones afectan el cumplimiento de promesas y la atención, limitando una experiencia de compra confiable. La contribución de cada causa debe verificarse antes de atribuirle toda la brecha.

Se separa problema de solución conforme a sesión 03, pp. 6/7, y clase 3, parte 1, 25:02 a 27:28. La compra/configuración de OMS se evalúa después como alternativa de intervención; no forma parte de la definición del problema. [Fuentes y aplicación](../registros/aportes_clase_03.md).

El diagnóstico relaciona tres condiciones: actualización de stock web entre 45 y 120 minutos, datos de clientes/productos desalineados y visibilidad limitada de pedidos en tiendas. Pueden contribuir a cancelaciones y dificultades de atención, junto con reglas operativas, dotación y conciliaciones. El caso no permite separar el efecto de cada causa; esa relación se mantiene como hipótesis por contrastar.

ERP y WMS deben mantenerse bajo las restricciones del caso. Evitar reemplazarlos limita el alcance de cambio, pero obliga a integrar y gestionar legacy; no demuestra por sí solo un menor costo total. La oportunidad es construir una experiencia omnicanal confiable con servicios reutilizables, coordinando personas, operación y tecnología (enunciado, pp. 3 a 5).

## 1.2 Drivers estratégicos, métricas e hitos

Los drivers estratégicos son crecimiento digital, cumplimiento de promesas, eficiencia de preparación, calidad de atención y continuidad. La integración reutilizable debe contribuir a esos resultados sin aumentar una complejidad operativa que la empresa no pueda sostener.

| Indicador del caso | Actual | Meta estratégica, p. 4 |
| --- | --- | --- |
| Ventas digitales / ventas totales | 24% | 35% |
| Pedidos entregados a tiempo | 82% | ≥95% |
| Cancelaciones por stock | 7,8% | <2% |
| Exactitud de inventario | 91% | ≥98% |
| Actualización de stock web | 45 a 120 min | <2 min |
| Preparación media | 7,2 h | <3 h |
| Devoluciones resueltas en primer contacto | 64% | ≥90% |
| Disponibilidad e-commerce | 99,3% | ≥99,9% |

NPS ≥+48 y abandono de carro <55% son otras metas estratégicas del caso. La propuesta contribuye a ellas sin garantizar que todas sean efectos atribuibles a ZEUS ni fijar por inferencia un horizonte corporativo que el caso no explicita.

Hitos obligatorios del escenario empresarial: horizonte 12 meses, valor dentro de los primeros 5, campaña Black Friday aproximadamente M8. La [secuencia del equipo](07_roadmap.md) propone R1 con 10 tiendas/M5, R2 con objetivo 68/M7 y R3/M12; la cobertura y viabilidad se registran como supuestos y condiciones, no como datos del caso.

## 1.3 Alternativas y recomendación

| Alternativa | Inversión preliminar | Horizonte del caso | Evaluación |
| --- | ---: | --- | --- |
| A. Reemplazo integral | 1.850 MM CLP | 12 a 18 meses | Excede el techo en 350 MM y puede exceder los 12 meses. No recomendada con restricciones actuales. |
| B. Plataforma modular | 1.350 MM CLP | 9 a 12 meses | Mantiene ERP/WMS e incorpora APIs, gestión de pedidos y capacidades digitales; base del equipo, condicionada a viabilidad, valor M5 y costo. |
| C. MVP focalizado | 800 MM CLP | 5 a 7 meses | Menor exposición inicial, pero no prueba valor dentro de M5 ni incluye necesariamente el despliegue nacional y R3 propuestos. |
| Diferir / no actuar | Sin monto informado | Por evaluar | Evita comprometer inversión inmediata, manteniendo problemas y costo de oportunidad. No equivale a costo cero. |

Recomendamos B porque conserva ERP/WMS y permite organizar inventario, pedidos y C&C en entregas sucesivas. Su inversión y plazo son referencias preliminares del enunciado (p. 7); no acreditan que la cobertura de 68 tiendas y el experimento adicional quepan en el presupuesto. Si la integración o capacidad no sostienen el plan, revisar cobertura, secuencia o alternativa con criterios explícitos.

## 1.4 Entregables, resultados, beneficios y valor

| Capacidad / output | Outcome esperado | Beneficio medible | Valor estratégico y condición |
| --- | --- | --- | --- |
| APIs, inventario/reserva y OMS integrado | Clientes y operación usan disponibilidad consistente; menos excepciones no previstas | Menos cancelaciones y reclamos, pedidos retenidos | Crecimiento confiable si datos físicos e integración son correctos. |
| C&C y aplicación de tienda | Personal prepara con estados y promesas visibles | Menor preparación y más pedidos cumplidos | Eficiencia si hay capacidad y adopción, no solo una app disponible. |
| Devoluciones elegibles omnicanal | Atención resuelve casos con trazabilidad y reglas comunes | Mayor resolución al primer contacto | Satisfacción/costo de servir; meta de proyecto ≥85% para casos elegibles, distinta de ≥90% corporativo. |
| Observabilidad, controles y soporte | Incidentes se detectan y atienden; liberaciones son operables | Menor exposición y servicio estable | Resiliencia y sostenibilidad; base desde R1, ampliada en R3. |

**Hipótesis de valor:** si datos de inventario, reserva y pedido son consistentes y las tiendas adoptan el proceso con capacidad, disminuirán cancelaciones y preparación. Una devolución integrada puede elevar resolución en primer contacto. Si la mejora se confirma y compensa sus costos y riesgos, puede contribuir al crecimiento digital y a la experiencia de compra. Requiere SUP-01 a SUP-08 y evidencia que permita revisar causalidad y trade-offs.

## 1.5 Objetivos del proyecto y medición propuesta

Se preservan los objetivos del Charter del equipo, proponiendo horizonte/cobertura explícitos. Son objetivos a evaluar, no resultados. El horizonte M12 es una definición de integración para revisión del grupo.

| ID | Indicador / cálculo propuesto | Objetivo del proyecto | Dueño empresarial propuesto |
| --- | --- | --- | --- |
| KPI-01 | Cancelaciones por stock / pedidos aceptados comparables con seguimiento completo | <2% a M12 en operación cubierta | Comercial/Logística |
| KPI-02 | Tiempo desde cambio confirmado de inventario hasta publicación web consistente | <2 min a M12 en interfaces cubiertas | Tecnología/Operaciones |
| KPI-03 | Promedio de tiempo desde pedido confirmado a listo para retiro/despacho, separado por flujo | <3 h a M12 en operación cubierta | Logística/Tiendas |
| KPI-04 | Devoluciones elegibles resueltas al primer contacto / devoluciones elegibles | ≥85% a M12, propuesta del equipo; referencia estratégica ≥90% | Operaciones/Comercial |
| KPI-05 | Tiempo de servicio disponible / ventana de observación acordada | ≥99,9% en campaña y seguimiento regular con ventanas definidas | Tecnología/Operaciones |
| KPI-06 | Pedidos C&C preparados mediante la app / pedidos C&C preparados de cohorte | >80% en piloto y cada ola aceptada, plazo operativo propuesto para revisión | Operaciones/Tiendas |

Los denominadores y reglas son propuestas: confirmar antes de comparar la base corporativa con tiendas piloto. En KPI-02 no reemplazar <2 minutos por un percentil favorable sin explicitar el cambio de criterio; observar también frecuencia/duración de incumplimientos.

KPI-04 y la meta estratégica difieren nominalmente en 5 puntos porcentuales, pero sus poblaciones son distintas. Esa resta no mide una brecha corporativa ni demuestra el aporte del proyecto. El grupo debe justificar la meta parcial y contrastarla con la cobertura definida en 04. El 64% es una base corporativa, no una base verificada de casos elegibles.

Para decidir la expansión en G1/M5, SUP-16 propone los siguientes criterios, pendientes de ratificación del equipo (véase el [registro vigente](../registros/acuerdos_y_supuestos.md)): cancelación al menos 20% menor en términos relativos y preparación media al menos 25% menor que sus respectivas bases comparables, adopción >80% por conjunto y tienda, servicio operable y evidencia evaluable. Si la base ya cumple una meta final, conservarla sin deterioro. Son umbrales académicos propuestos, no exigencias del enunciado.

La propuesta desarrollada de 04/07 habilita 10 tiendas, 1 CD y 2 familias al finalizar la semana 16, durante M4, y evalúa uso en semanas 17–20, frente a base comparable propuesta en 9–12; G1 al cierre de semana 22. Son bloques relativos de planificación por ratificar, no fechas civiles confirmadas. Piso operacional propuesto: 1.000 pedidos elegibles con seguimiento completo por fase; no es potencia estadística calculada ni garantía causal. Reportar conteos, mix, diferencias por tienda y datos faltantes. Sin evidencia suficiente el resultado es inconcluso, no una primera entrega de valor demostrada.

La exactitud de inventario se sigue como habilitador, sin duplicar beneficio económico. Observar disponibilidad en ventana definida de 28 días, sin autorizar interrupciones planificadas. Ejemplos condicionales de umbrales: 7,8% × 0,80 = 6,24%; 7,2 h × 0,75 = 5,4 h, solo si las bases piloto coincidieran con las corporativas. Las metas finales <2% y <3 h a M12 se mantienen. Un antes/después no demuestra atribución causal ni acredita resultado para todo el catálogo.

## 1.6 Costos, riesgos, supuestos y solicitud

Se integra el presupuesto preliminar del equipo: **base 1.330 MM CLP + contingencia 170 = marco total 1.500 MM**, igual al techo del caso. Referencia B: 1.350 MM. Extremos declarados de categorías: 1.215 a 1.500 MM, sin reserva adicional sobre el extremo alto. Son valores supuestos del ejercicio, no cotizaciones verificadas.

La [estimación 06](06_estimacion.md) incluye 104 equipo-sprints esperados y capacidad efectiva propuesta 120, con refuerzo temporal del sexto equipo. Los totales y el WSJF son aritméticamente consistentes. El [plan de apoyo de alcance/roadmap](../registros/plan_alcance_roadmap.md) propone calendario, carga por épica/tramo y funciones sin alterar los totales. Rogelio debe contrastar dedicación por especialidad y fronteras de costos externos versus capacidad propia. No inferir confianza de fecha 80–95% por sumar esfuerzo.

Financiación base recibida: **675 MM en G0/M1**, 345 en G1/M5 y 310 en G2/M9; contingencia 170 por riesgo y autorización del comité. Son cuotas propuestas; falta asignación categoría/mes para verificar obligaciones. Se solicita el primer tramo de 675 condicionado a arquitectura, contrato por hitos y revisión técnica VT-01, sin simular aprobación empresarial.

Riesgos principales: integración/API, stock, WMS, dotación/sitios, campaña, sobrecosto y seguridad. Si se consumen los 170 para alcanzar el extremo alto de categorías, no quedan los mismos 170 disponibles para otro riesgo. Primeras opciones de diferimiento son capacidades opcionales/experimento, sin eliminar condiciones del flujo ni objetivo de devolución sin cambio formal.

R3 incluye un experimento de Ship-from-store en **3 a 5 tiendas**. El documento 04 propone detener la ejecución al cumplir cuatro semanas o 300 pedidos, lo que ocurra primero, sujeto a ratificación. E10 ya forma parte del esfuerzo incluido en la capacidad presupuestada. G2 debe autorizar techo monetario de exposición y frontera de costos antes de iniciar. Ver [revisión del avance del 23](../registros/revision_avance_2026-10-23.md).

Faltan volumen, margen y flujos para ROI/VAN/payback numéricos. Beneficio potencial = pedidos recuperables × margen incremental, más costos realmente evitados, menos gasto incremental; ajustar sustitución de canal y costos de oportunidad, que no son ahorro de caja automático. El presupuesto es ahora una base cuantificada para discutir inversión, no prueba de esos beneficios.
