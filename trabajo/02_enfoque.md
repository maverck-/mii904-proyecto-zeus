# 2. Selección y tailoring del enfoque

**ESC-02: base del equipo integrada con correcciones de fundamento, 21-10-2026.** Véase [revisión](../registros/integracion_avance_equipo.md), INT-05/10/11/12. Se conserva su gobierno predictivo, entrega adaptativa, Kanban y Scrum de dos semanas. Propuesta pendiente de revisión, no prácticas ejecutadas.

## 2.1 Enfoque propuesto

Recomendamos un enfoque híbrido: una capa de gobierno formal y una capa de entrega adaptativa, asignadas según restricción, incertidumbre, contrato y costo de error. Otros enfoques también pueden planificar y gobernar; la elección se justifica por cómo estas prácticas resuelven las tensiones de ZEUS, no por afirmar que ningún enfoque distinto podría hacerlo.

## 2.2 Fundamentación

ERP, conciliación, seguridad, contratos y preparación comercial requieren trazabilidad, acuerdos y control de cambios. Esos compromisos pueden ser estables sin que la solución técnica sea conocida. Las APIs y datos legacy conservan incertidumbre que debe probarse temprano. La restricción de no reemplazar ERP no reduce por sí sola esa incertidumbre.

La experiencia C&C, devolución, aplicación de tienda y adopción requieren validación temprana y ajuste. El rol logístico de las tiendas y Ship-from-store necesita un experimento con límites y criterios de aprendizaje. La capacidad y madurez ágiles desiguales del caso (p. 5) condicionan cuántos equipos pueden sostener estas prácticas.

## 2.3 Asignación por componente

| Componente | Lógica propuesta del equipo, precisada | Justificación y evidencia |
| --- | --- | --- |
| ERP, contabilidad y conciliaciones | Gobierno predictivo de interfaz/aceptación y pruebas técnicas tempranas | Alta exigencia de trazabilidad; viabilidad API/datos no asumida. |
| Contratos WMS/OMS | Hitos contractuales, aceptación y compra escalonada | WMS trabaja tradicionalmente según caso; modalidad de OMS es supuesto de compra por validar. |
| Seguridad y accesos | Controles formales + validación dentro de cada incremento y DoD | Obligatorios desde inicio; no basta una auditoría final. |
| Black Friday | Plan de preparación, dependencias, capacidad y salida operable | Fecha externa una vez confirmada; el caso la ubica aproximadamente en M8. No se declara CPM calculado aún. |
| APIs y disponibilidad | Kanban con límites WIP acordados según capacidad | Flujo de dependencias y excepciones; hacer visibles bloqueos y validar consistencia. |
| C&C, app y devoluciones | Scrum propuesto con sprints de dos semanas y feedback de tiendas/PO | Aprender sobre flujo y adopción. Confirmar roles, dedicación y capacidad para sostener Scrum. |
| Ship-from-store | Experimento acotado en R3, sujeto a gate M9 y presupuesto | Una hipótesis operacional, criterios de aprendizaje y reversión; no promesa de despliegue nacional. |

## 2.4 Estables y adaptables

Estables: propósito, techo presupuestario, restricciones ERP/WMS/continuidad, principios y controles acordados. Gates M1/M5/M9 son diseño de gobierno propuesto; la campaña se protege una vez confirmada su fecha externa.

API-first y orientación a eventos se conservan como decisiones de arquitectura propuestas, no condiciones impuestas por el enunciado. El caso pide APIs/servicios reutilizables; evaluar eventos donde aporte y sea compatible con legacy.

Adaptables: detalle del release, orden del backlog, diseño UX, selección de piloto y olas. La propuesta de 10 y 68 tiendas debe validarse; si cambia cobertura comprometida, actualizar objetivos/costo/hitos con sponsor y comité. No cambiar el número de tiendas silenciosamente por decisión del PO.

## 2.5 Controles formales

- Gates de financiación G0/M1, G1/M5 y G2/M9, según propuesta del equipo; cierre M12.
- Revisión técnica VT-01 al final de M2 antes de exposición de piloto/compra irreversible; revisión de preparación VE-01/M7 antes de campaña. Son controles de salida, no gates financieros adicionales por obligación.
- Control de cambios para techo, financiación, alcance mayor y fechas comprometidas; revisar también efecto sobre beneficios.
- Arquitectura y seguridad antes de cada release; observabilidad, soporte y reversión desde R1.

El contrato OMS en M1 se plantea con hitos de validación y aceptación; no asumir que integración/licencias ya están resueltas antes de evaluar la solución.

## 2.6 Retroalimentación

Revisión de sprint cada dos semanas con responsables de tienda piloto y PO de e-commerce; revisión semanal de métricas de flujo y bloqueos; foro de integración semanal PM/PO/Arquitectura para dependencias. Son propuestas del equipo y requieren disponibilidad, SUP-02.

Se conserva el supuesto de cinco equipos de implementación, distintos de los cuatro integrantes académicos. Tamaños, dedicaciones, especialidades y concurrencia requieren estimación; no se heredan los 92,5 persona-meses ni los dos frentes de ESC-01 como equivalentes.

## 2.7 Puente de artefactos y autoridad

Charter define mandato; EDT PAQ costo y cobertura; backlog CAP prioridades; roadmap R0/R1/R2/R3 evidencia y gates; registros decisiones y supuestos. PO ordena trabajo dentro de límites; PM integra; comité/sponsor decide inversión y cambios mayores; CISO puede bloquear exposición crítica y Operaciones una salida no operable. La DoD incluye pruebas, controles, telemetría, documentación y soporte, pero el beneficio se evalúa con uso y métricas por gate.
