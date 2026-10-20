# 1. Diagnóstico estratégico y Business Case

**Borrador desarrollado con ESC-01, propuesto y pendiente de revisión del grupo.** Fuente de hechos: enunciado, pp. 3 a 8. Los supuestos están en el [registro común](../registros/acuerdos_y_supuestos.md). Integrar aquí los aportes del equipo cuando estén disponibles.

## Problema, prioridad y drivers

M-GesPro Retail presenta inconsistencias entre inventario publicado y disponible, demoras en el traspaso de pedidos y visibilidad limitada entre canales. El caso informa cancelaciones por falta de stock de 7,8%, entregas a tiempo de 82% y preparación media de 7,2 horas. Estas condiciones dificultan sostener la experiencia omnicanal y crecer digitalmente con eficiencia. No se conoce cuánto aporta cada causa a cada indicador.

La prioridad es aumentar ventas digitales, eficiencia operacional y satisfacción. Drivers: confiabilidad de promesa, capacidad logística, continuidad, adopción y reducción de dependencias frágiles. La tecnología, los datos físicos y la capacidad de tienda deben evaluarse juntos.

## Recomendación revisable

Desarrollar B modular: preservar ERP/WMS y habilitar inventario, reservas, pedidos y C&C por releases. ESC-01 propone 5 tiendas/un CD como piloto, operación en M4 y evaluación hasta M5; hasta 20 tiendas en M7 y 35 en M11, solo con evidencia y capacidad. Estas coberturas son SUP-05, no datos del enunciado ni decisiones grupales aprobadas.

## Hipótesis y cadena de valor

Si reconciliamos disponibilidad y reservas y hacemos trazable el pedido, y las tiendas adoptan el flujo con capacidad suficiente, la cohorte cubierta debería registrar menos cancelaciones y preparación más rápida. Eso puede retener pedidos y mejorar confianza. Requiere SUP-01 a SUP-06 y medición comparable.

| Nivel | Definición aplicada |
| --- | --- |
| Output | APIs, inventario/reserva, pedido y C&C operativos con controles. |
| Outcome | Tiendas y logística usan información consistente y ejecutan pedidos con menor espera y menos excepciones. |
| Beneficio | Menos cancelación, preparación más rápida y mayor cumplimiento. |
| Valor | Contribución a crecimiento y eficiencia considerando costos, riesgos, sostenibilidad y costo de oportunidad. |

## Tres indicadores principales y metas propuestas

Los valores base corporativos y metas estratégicas proceden de la p. 4. La base de una cohorte piloto todavía no está definida. Los umbrales piloto son SUP-06; son una aspiración intermedia para discutir, sin evidencia empírica de factibilidad. Las metas M12 se proponen para operaciones cubiertas, tomando como referencia las corporativas.

| ID | Indicador y fórmula propuesta | Base corporativa | Piloto M5, propuesta | Cobertura aprobada M12, propuesta | Dueño empresarial propuesto |
| --- | --- | --- | --- | --- | --- |
| KPI-01 | Cancelaciones por stock / pedidos aceptados de cohorte con seguimiento completo | 7,8% | <4% y mejora frente a base comparable | <2% | Comercial/Logística |
| KPI-02 | Registros SKU-ubicación correctos / registros SKU-ubicación auditados | 91% | ≥96% sin deterioro frente a base comparable | ≥98% | Operaciones |
| KPI-03 | Tiempo medio de confirmación de pedido a listo para retiro/despacho, en horas | 7,2 h | <4 h y mejora frente a base comparable | <3 h | Logística/Tiendas |

El mecanismo de KPI-01 captura beneficio para el cliente; KPI-02 detecta si el habilitador funciona y por sí solo no acredita valor; KPI-03 captura eficiencia operacional, pero necesita revisión de mix y carga. No sumar una mejora de estos tres como si fueran beneficios financieros independientes.

**Señales tempranas:** antigüedad de stock web, conflictos de reserva y pedidos pendientes sin consumir; permiten ajustar antes del cierre mensual. Definir eventos y umbrales técnicos en G1, sin inventar carga real. **Guardrails:** disponibilidad del servicio afectado objetivo ≥99,9%, método mensual propuesto; cero riesgos críticos abiertos al liberar. La continuidad de e-commerce/tiendas durante despliegues sigue siendo restricción del caso y no se sustituye por el porcentaje de disponibilidad.

### Cómo se evaluaría

Registrar línea base por tienda, familia y flujo con cuatro semanas históricas comparables si existen. Acordar tiempos, reglas de rechazo/cancelación, reintentos y seguimiento de cohorte. Comparar piloto con período y/o tiendas equivalentes, informando numerador, denominador y mix; un antes/después aislado no prueba causalidad.

Operar R1 en M4, medir cuatro semanas hasta M5 y revisar suficiencia del volumen. No se ha determinado un tamaño muestral ni calculado significancia. Si la base piloto ya es mejor que los umbrales, recalibrar antes de autorizar: cumplir un umbral más débil no justifica deteriorar el desempeño.

Las metas estratégicas restantes (35% digital, puntualidad ≥95%, devoluciones ≥90%, NPS ≥+48, carro <55%, stock web <2 min) se mantienen como contexto y se asignan a capacidades pertinentes. No asegurar que el piloto por sí solo produzca esos resultados corporativos. El caso no especifica el horizonte de realización de todas ellas.

## Alternativas

| Alternativa | Inversión preliminar del caso | Horizonte | Juicio de trabajo |
| --- | ---: | --- | --- |
| A. Reemplazo integral | 1.850 MM CLP | 12 a 18 meses | Excede techo en 350 MM y puede exceder 12 meses; no recomendar con límites actuales. |
| B. Plataforma modular | 1.350 MM CLP | 9 a 12 meses | Base revisable; requiere primer valor M5, integración viable y costo a término compatible. |
| C. MVP focalizado | 800 MM CLP | 5 a 7 meses | Menor exposición; no garantiza valor M5 por su plazo total y debe estimar expansión posterior. |
| Diferir / no actuar | Sin cifra informada | Por evaluar | Evita inversión inmediata pero persisten fricción, costos y riesgo; no equivale a costo cero. |

B ofrece capacidad reutilizable y evolución dentro de 12 meses, a cambio de mayor esfuerzo de integración y coordinación. El flujo mínimo retoma inventario/pedidos/C&C; no se suman los 800 MM de C a los 1.350 MM de B. Una alternativa D solo se necesita si se justifica un cambio material.

## Economía y asequibilidad de ESC-01

El [modelo de 06](06_estimacion.md) propone rangos por paquete: costo central 1.065 MM; con reserva nominal de 150, **1.215 MM**. El sobre de trabajo de **1.350 MM** usa la referencia B como límite propuesto, no como precio confirmado. Quedan 135 MM no asignados dentro del sobre y 150 MM entre sobre y techo de 1.500. No son dos reservas ya autorizadas.

Adverso de partidas: 1.550 MM; manteniendo además la reserva nominal como prueba conservadora, **1.700 MM**. Incluso sin esa reserva el adverso supera el techo en 50 MM. No hay promesa de que B siempre quepa; reducir cobertura/capacidades secundarias o detener escala. No recortar controles ni contar una contingencia materializada dos veces.

Para beneficios económicos: `pedidos comparables × reducción de cancelación atribuible × margen incremental recuperable`, más costos de reproceso efectivamente evitables, menos operación incremental. Corregir sustitución entre canales y evitar doble conteo. Faltan volumen, margen, costo de servir, costos y flujos confirmados para ROI/VAN/payback numéricos. Mantener esos valores sin calcular hasta disponer de supuestos económicos explícitos adicionales o evidencia.

## Decisión y condiciones

Proponer autorización inicial hasta 100 MM incluida en el sobre para diagnóstico y validación, SUP-08; no es el costo calculado de M1 ni una aprobación real. G1 decide construcción/piloto según datos, integración, capacidad y costo. G2/M5 decide expansión según beneficio y guardrails. Si valor M5, controles o presupuesto no son viables, revisar B y el alcance; dejar C como opción de repliegue que también debe probar sus condiciones.
