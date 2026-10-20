# 3. Project Charter

**Versión ESC-01, 20-10-2026. Borrador propuesto para revisión del grupo y posterior integración de sus aportes.** No hay autorización empresarial ni aprobación grupal de este escenario. Fuentes: enunciado, pp. 4 a 8; clase 2, parte 1, 48:45 a 52:55.

## Propósito y marco

Mejorar confiabilidad y ejecución omnicanal de M-GesPro Retail, reduciendo cancelaciones y tiempos de preparación con continuidad operacional. B modular es base revisable. Sponsor: **Gerencia General**, según el caso.

Horizonte del caso: 12 meses relativos al inicio empresarial. Obligaciones: primera entrega de valor dentro de M5, Black Friday aproximadamente M8, ERP sin reemplazo, WMS sin reemplazo completo, tiendas y e-commerce operativos, controles de identidad/acceso/trazabilidad/datos/seguridad.

## Objetivos y éxito propuestos

| Objetivo | Piloto M5, SUP-06 | Cobertura aprobada M12 | Dueño propuesto |
| --- | --- | --- | --- |
| KPI-01: cancelación por stock | <4% y mejora frente a base comparable | <2% | Comercial/Logística |
| KPI-02: exactitud inventario | ≥96% sin deterioro | ≥98% | Operaciones |
| KPI-03: preparación media | <4 h y mejora frente a base comparable | <3 h | Logística/Tiendas |

Definiciones, ventanas y limitaciones en [01](01_diagnostico_y_business_case.md). Las bases corporativas no son automáticamente las del piloto. Medir cuatro semanas con volumen evaluable antes del cierre M5, SUP-03/SUP-04. Criterios transversales propuestos: disponibilidad mensual objetivo ≥99,9% del servicio afectado y cero riesgos críticos abiertos. No reemplazan la continuidad exigida durante despliegues.

## Alcance y entregables

CAP-01 diagnóstico/base/prueba; CAP-02 inventario/reserva; CAP-03 pedidos; CAP-04 C&C; CAP-05 controles/observabilidad; CAP-06 adopción/continuidad; CAP-07 escalamiento; CAP-08 devolución elegible. Alcance, aceptación y paquetes PAQ en [04](04_alcance_y_backlog.md).

ESC-01: piloto 5 tiendas/un CD; hasta 20 tiendas M7 y 35 M11, condicional a capacidad y evidencia. SUP-05. Fuera del compromiso base: ERP/WMS completos, IA, data platform corporativa, Ship-from-store y despliegue de todas las tiendas. Datos operacionales y métricas mínimos sí forman parte del alcance.

## Recursos y presupuesto

Proponer sobre de trabajo de **1.350 MM CLP**, incluyendo reserva nominal 150 MM; el techo del caso es 1.500 MM. Modelo ilustrativo: 1.065 MM central antes de reserva y 1.215 MM con ella, con 135 MM no asignados dentro del sobre. Adverso de partidas 1.550 MM; más reserva nominal 1.700 MM. Estos rangos son SUP-07/SUP-08/SUP-10; no son cotización ni costo aceptado por el grupo.

Primer tramo propuesto hasta 100 MM dentro del sobre, para limitar exposición mientras se valida. Liberación posterior por gates. Dos frentes técnicos más especialistas y negocio, con dedicaciones hipotéticas descritas en [06](06_estimacion.md); confirmar SUP-02 antes de prometer paralelismo.

## Gobierno y autoridad propuestos

| Rol empresarial | Decisión / responsabilidad |
| --- | --- |
| Gerencia General | Autorizar mandato, tramos, cobertura de alto nivel y cambios de baseline. |
| Comité con Finanzas, Operaciones, Comercial y Tecnología | Revisar evidencia, costo a término y trade-offs por gate. Composición propuesta. |
| Dirección de proyecto, por designar | Integrar plan, costo, riesgos y dependencias; escalar desvíos. |
| PO E-commerce | Priorizar detalle dentro de objetivos, presupuesto y guardrails. |
| Operaciones/Logística/Tiendas | Aceptar capacidad, procesos, adopción y beneficios operacionales. |
| Tecnología/Arquitectura | Aceptar diseño, integración, rendimiento y recuperación. |
| CISO / responsables de datos | Aceptar controles y exposición; bloquear salida con riesgo crítico. |
| Finanzas | Validar TCO, rangos, forecast y consumo de reserva. |
| Proveedores WMS/cloud | Acordar interfaces, costos, soporte y aceptación contractual. |

Son roles de la empresa ficticia; no asignaciones nominales a los compañeros.

## Hitos y evidencia

| Gate | Fecha relativa | Criterio propuesto |
| --- | --- | --- |
| G0 | Inicio | Propósito, responsables, restricciones y tramo inicial aceptados. |
| G1 | Fin M2 | Prueba de integración, base por cohorte, capacidad de tienda, controles y forecast viables. |
| G2 | Fin M5 | Uso y evidencia de KPI-01/02/03; guardrails; decisión de expansión. |
| G3 | Fin M7 | Carga representativa y reversión probadas, cobertura/capacidad listas para M8. |
| G4 | M9 | Resultados del evento, estabilidad y costo justifican devolución/expansión. |
| G5 | Fin M12 | Aceptación, operación transferida, resultados y beneficios pendientes con dueño. |

El [roadmap](07_roadmap.md) detalla releases, rutas y criterios de continuar/ajustar/detener. El registro de supuestos aporta validación académica y empresarial hipotética. Riesgos R-01 a R-08 en [registro](../registros/riesgos.md).

## Aceptación y cambios

Aprobar este borrador para la tarea requiere revisar objetivos, costos, cobertura y capacidad con el grupo. Una autorización empresarial exigiría aceptación del sponsor y responsables respectivos, aquí solo descrita. No se simulan firmas o pruebas.

Toda nueva capacidad, cambio de presupuesto, hito o beneficio actualiza Business Case, alcance, estimación y roadmap. Si no hay valor M5 o viabilidad dentro del techo, no declarar éxito por completar el desarrollo: replantear el caso.
