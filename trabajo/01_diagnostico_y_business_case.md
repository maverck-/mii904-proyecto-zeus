# 1. Diagnóstico estratégico y Business Case

**ESC-02: versión integrada desde el avance del equipo, 21-10-2026.** Se priorizan su diagnóstico, alternativa B, objetivos y secuencia. Los complementos y correcciones están en la [revisión de integración](../registros/integracion_avance_equipo.md). El [texto recibido](../insumos/avance_equipo_2026-10-21.md) se conserva como antecedente; la pauta y los hechos los establece el enunciado.

## 1.1 Problemas y oportunidad

El negocio presenta alta latencia entre el cambio de inventario y la publicación del stock web (45 a 120 minutos), junto con un 7,8% de cancelaciones por falta de stock. Es consistente plantear la disponibilidad desactualizada como una causa a investigar, pero el caso no permite atribuirle todo ese porcentaje.

Existen múltiples bases con información desalineada de clientes y productos y visibilidad limitada de los pedidos digitales en tiendas. Esto dificulta atención y devoluciones; el caso registra 64% de devoluciones resueltas al primer contacto. Deben revisarse también reglas operativas, dotación y conciliaciones antes de atribuir el problema solo a la plataforma.

ERP y WMS deben mantenerse bajo las restricciones del caso. Evitar reemplazarlos limita el alcance de cambio, pero obliga a integrar y gestionar legacy; no demuestra por sí solo un menor costo total. La oportunidad es construir una experiencia omnicanal confiable con servicios reutilizables, coordinando personas, operación y tecnología (enunciado, pp. 3 a 5).

## 1.2 Drivers estratégicos, métricas e hitos

La propuesta del equipo busca una experiencia omnicanal resiliente, eficiente, sostenible y escalable. Los drivers son crecimiento digital, cumplimiento de promesas, eficiencia de preparación, calidad de atención, continuidad y reducción de complejidad de integración.

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

Recomendamos desarrollar B modular por releases, preservando la elección inicial del equipo. Permite secuenciar capacidades para la campaña y mantener una arquitectura evolutiva. Su inversión y plazo son preliminares del enunciado (p. 7), no cotización ni prueba de que 68 tiendas y el experimento adicional quepan. Si la integración o capacidad no sostienen el plan, revisar cobertura, secuencia o alternativa con criterios explícitos.

## 1.4 Output, outcome, beneficio y valor

| Capacidad / output | Outcome esperado | Beneficio medible | Valor estratégico y condición |
| --- | --- | --- | --- |
| APIs, inventario/reserva y OMS integrado | Clientes y operación usan disponibilidad consistente; menos excepciones no previstas | Menos cancelaciones y reclamos, pedidos retenidos | Crecimiento confiable si datos físicos e integración son correctos. |
| C&C y aplicación de tienda | Personal prepara con estados y promesas visibles | Menor preparación y más pedidos cumplidos | Eficiencia si hay capacidad y adopción, no solo una app disponible. |
| Devoluciones elegibles omnicanal | Atención resuelve casos con trazabilidad y reglas comunes | Mayor resolución al primer contacto | Satisfacción/costo de servir; meta proyecto 85% distingue aporte parcial respecto de 90% corporativo. |
| Observabilidad, controles y soporte | Incidentes se detectan y atienden; liberaciones son operables | Menor exposición y servicio estable | Resiliencia y sostenibilidad; base desde R1, ampliada en R3. |

**Hipótesis de valor:** si datos de inventario, reserva y pedido son consistentes y las tiendas adoptan el proceso con capacidad, disminuirán cancelaciones y preparación. Una devolución integrada puede elevar resolución en primer contacto. Esto sostiene crecimiento y experiencia considerando costos y riesgos. Requiere SUP-01 a SUP-08 y evidencia que permita revisar causalidad y trade-offs.

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

Los denominadores y reglas son propuestas: confirmar antes de comparar la base corporativa con tiendas piloto. En KPI-02 no reemplazar <2 minutos por un percentil favorable sin explicitar el cambio de criterio; observar también frecuencia/duración de incumplimientos. KPI-04 deja una brecha de 5 puntos porcentuales frente a la meta estratégica: el grupo debe justificar el objetivo parcial o elevarlo con costo/plazo coherentes. Los datos solo respaldan 64% corporativo, no una base piloto idéntica.

Para G1/M5 se propone que el piloto esté en uso, KPI-06 supere 80%, haya mejora de cancelación/preparación frente a base comparable y no deterioro material de la operación. Fijar magnitud mínima de mejora y suficiencia de evidencia antes de abrir el piloto; no reutilizar automáticamente las metas intermedias de ESC-01 ni aceptar cualquier oscilación como valor probado. La exactitud de inventario se sigue como habilitador (91% y meta estratégica ≥98%), sin duplicar el beneficio económico de cancelaciones.

Ventana de trabajo propuesta: base por tienda/familia/flujo, piloto en M4 y evaluación de cuatro semanas hasta M5, con volumen suficiente y conteos. Contrastar cambios de demanda/mix y controles comparables cuando sea viable. Un antes/después no prueba causalidad. Si solo hay go-live al final de M5 o evidencia insuficiente, el requisito de valor no queda demostrado. La disponibilidad porcentual no autoriza interrupciones planificadas de tiendas/e-commerce.

## 1.6 Costos, riesgos, supuestos y solicitud

Techo preliminar: 1.500 MM CLP. Referencia B: 1.350 MM. El equipo propone financiación por tramos. La distribución de presupuesto, reservas y primer tramo quedan a reestimar por Rogelio con el alcance 10/68 tiendas, cinco equipos supuestos, OMS comprado y experimento R3. Los totales de ESC-01 no validan ese alcance y se retiran como presupuesto vigente.

La [estimación](06_estimacion.md) conserva método y una tabla para la nueva cobertura. Contemplar licencias por uso/tienda, trabajo interno, integración, datos, formación, operación/transición, seguridad, despliegue y experimento, sin doble conteo. Faltan volumen, margen y flujos para ROI/VAN/payback numéricos. Beneficio potencial = pedidos recuperables × margen incremental, más costos realmente evitados, menos gasto incremental; ajustar sustitución de canal y capacidad liberada, que no es ahorro de caja automático.

Riesgos principales: integración, exactitud de stock, WMS, dotación, escalamiento de 58 tiendas, campaña, sobrecosto y seguridad. Registro común con responsables y disparadores. Se solicita aprobar la formulación de B y financiación inicial por un monto que debe estimarse antes de cerrar autorización; R0/R1 tienen liberación condicionada a evidencia técnica y capacidad, no a una aprobación de todo el proyecto sin límites.
