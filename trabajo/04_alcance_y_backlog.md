# 4. Alcance y backlog de capacidades

Estado: propuestas para discusión conjunta. B modular orienta el trabajo; estas filas todavía no son compromisos de alcance. Fuente: enunciado, pp. 4, 5 y 8.

## Fronteras propuestas

**Incluir para evaluar:** inventario y reservas, gestión/visibilidad de pedidos, integración ERP/WMS/e-commerce, Click & Collect, métricas, seguridad, continuidad, adopción y soporte. Devoluciones se evalúa como capacidad posterior según prioridad y costo.

**Excluir por restricción:** reemplazo ERP y WMS completo. **Postergar como propuesta:** motor de IA, plataforma analítica corporativa y Ship-from-store en el primer release. Justificar estas últimas decisiones y sus trade-offs antes de aprobarlas.

**Interfaces a coordinar:** ERP, WMS, POS, e-commerce, logística, pagos y CRM cuando corresponda al flujo. Estar fuera del reemplazo no significa estar fuera de la coordinación.

## Backlog inicial

Usar IDs CAP-xx en priorización, estimación y roadmap. Son capacidades/épicas; refinar historias y criterios cuando el trabajo se acerque. No exige implementar todas las filas.

| ID | Capacidad / resultado | Dependencia inicial | Criterio de aceptación a precisar | Estado |
| --- | --- | --- | --- | --- |
| CAP-01 | Diagnóstico, línea base y viabilidad de integración | Acceso a datos y proveedor WMS | Evidencia de causas, base comparable y prueba representativa de integración. | Propuesta |
| CAP-02 | Inventario consistente y reservas | CAP-01; control de stock físico | Stock reservable, concurrencia y excepciones verificadas; métricas acordadas. | Propuesta |
| CAP-03 | Gestión y trazabilidad de pedidos | CAP-01/CAP-02 | Pedido visible entre canales, sin pérdida ni duplicación, con manejo de fallos. | Propuesta |
| CAP-04 | Preparación y retiro Click & Collect | CAP-02/CAP-03/CAP-05/CAP-06 | Pedido real preparado y retirado; plazo, dotación y atención aceptados. | Propuesta |
| CAP-05 | Seguridad, datos, observabilidad y medición | Desde inicio, transversal | Controles obligatorios y eventos auditables; alertas con dueño. | Propuesta transversal |
| CAP-06 | Adopción, continuidad y soporte | Desde inicio, transversal | Personal y operación preparados, transición/reversión y soporte aceptados. | Propuesta transversal |
| CAP-07 | Escalamiento y preparación del evento | Evidencia del flujo inicial | Capacidad representativa del evento probada y cobertura aceptada. | Propuesta |
| CAP-08 | Devoluciones omnicanal elegibles | CAP-03; reglas Comercial/Finanzas | Caso completo y trazable, indicadores y responsabilidad de resolución. | Propuesta posterior |

CAP-05 y CAP-06 comienzan en paralelo al diagnóstico: son condiciones de cada release, no últimas tareas. Si se propone otra capacidad, añadir valor esperado, dependencia, aceptación y costo/capacidad antes de incluirla.

## Estructura de trabajo

Agrupar paquetes por entregables: (1) formulación/gobierno; (2) inventario/integración; (3) pedidos; (4) C&C/adopción; (5) expansión/devoluciones; (6) seguridad/calidad; (7) transición/operación. Esta EDT de alto nivel es propuesta y puede ajustarse. Asignar a cada costo un único paquete para no contarlo en EDT y backlog dos veces.

## Cómo acordarlo

Añadir responsable de revisión, inclusión/exclusión, release y decisión en el registro común. Fijar alcance mínimo que produce un resultado usable y cómo medirlo antes de M5. No cerrar número de tiendas, nuevos umbrales o proveedor sin justificarlos como supuestos.
