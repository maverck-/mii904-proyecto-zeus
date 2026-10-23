# Aportes de clase 3 al proyecto ZEUS

Revisión del 21 de octubre de 2026. La clase del **9 de octubre** reúne las sesiones temáticas **03 y 04**, con dos grabaciones. Se incorporan también las presentaciones 05/06 como complemento posterior disponible, sin atribuirles una transcripción inexistente. Se prioriza el avance del equipo integrado en ESC-02.

## Qué aporta y qué cambia

El material refuerza la propuesta B modular e híbrida, sin imponerla como única respuesta para ZEUS. Los cambios desarrollan trazabilidad, aceptación, dependencias y actualización de decisiones. No se cambian automáticamente objetivos, cobertura o presupuesto ni se agregan entregables obligatorios.

| Hallazgo docente | Evidencia local | Aplicación a ZEUS / ubicación |
| --- | --- | --- |
| Formular el problema sin anticipar solución; objetivos describen resultados | [Sesión 03](../insumos/presentaciones/sesion-03_inicio_y_formulacion.pdf), pp. 6/7; [parte 1](../transcripciones/clase-03_parte-1.md), 25:02 a 27:28 | Declaración breve del problema en 01, sin incorporar OMS como problema; mantener KPI como cambios esperados. |
| Business Case decide si invertir y compara opciones; Charter formaliza mandato y autoridad | Sesión 03, pp. 8/10/12; parte 1, 30:25 a 32:47 y 42:07 a 43:59 | Conservar alternativas/no actuar y recomendación condicionada de 01. En 03 mantener mandato sintético y enlazar detalle; financiación inicial sigue pendiente de cuantificar. |
| Supuestos numéricos explícitos permiten formular; requieren validación | Parte 1, 1:12:35 a 1:13:16, discusión del objetivo supuesto 21% del ejercicio | Mantener 10/68 y ≥85% como propuestas defendibles, sin presentarlas como hechos o aprobación del docente. El 21% no se traslada a ZEUS. |
| Interesados deben mostrar decisiones, dependencias y aceptación | Sesión 03, p. 11; parte 1, 39:37 a 41:32 | Precisar en 03 aporte de usuarios/clientes, tienda, operación y proveedores. Tener sponsor no reemplaza feedback del personal operativo. |
| Alcance de producto y proyecto son distintos; ambos deben contemplarse | [Sesión 04](../insumos/presentaciones/sesion-04_alcance_y_planificacion.pdf), pp. 5/7; [parte 2](../transcripciones/clase-03_parte-2.md), 10:44 a 15:49 | Separar capacidades de solución del trabajo de integración, formación, transición y soporte en 04, sin dejarlos fuera del costo. |
| Objetivo → capacidad → entregable → aceptación → valor | Sesión 04, p. 6; parte 2, 11:53 a 13:01 | Agregar matriz compacta KPI/CAP/PAQ/release en 04; la capacidad no equivale a beneficio observado. |
| Criterio de aceptación y DoD se complementan | Sesión 04, p. 8; parte 2, 15:54 a 17:49 | Mantener aceptación específica por capacidad y estándar transversal en 04. Ejemplo de C&C muestra ambas decisiones. |
| EDT organiza alcance, evita doble conteo; backlog ordena trabajo próximo | Sesión 03, p. 17; sesión 04, pp. 10/12; parte 2, 19:59 a 24:41 | Precisar jerarquía ZEUS/entregables/PAQ y conservar fronteras de costo. No replicar cada ítem en todos los artefactos. |
| Lo externo al control sigue dentro de la coordinación | Sesión 04, p. 9; parte 2, 17:57 a 19:53 | Mapa de dependencias en 07 con responsable, evidencia y fecha necesaria; el ERP no se reemplaza pero sus interfaces necesitan prueba. |
| Gobierno, puente y entrega deben compartir decisiones y retroalimentación | Sesión 03, p. 15; sesión 04, pp. 16/20; parte 1, 52:54 a 55:09; parte 2, 32:58 a 39:58 | Conectar actualización de backlog/roadmap/forecast/Charter en 02/07. Detallar trabajo próximo y mantener R3 por capacidades/hipótesis. |
| Charter y alcance son registros vivos; distinguir cambio de compromiso de repriorización | Parte 2, 55:53 a 57:57 y 1:17:24 a 1:19:41; sesión 04, p. 19 | Registrar impacto, decisión y comunicación. PO cambia orden dentro de límites; sponsor/comité decide cambios mayores según Charter de ZEUS. |

## Cómo defender las 68 tiendas

La clase no determina que esa expansión sea imposible ni demuestra que sea viable. Permite avanzar con una meta y supuestos visibles. **68/M7 se mantiene como objetivo propuesto por el equipo.** Las olas 15/15/14/14 son una forma de explicar la secuencia y revisar capacidad; no una condición impuesta por el profesor.

Defender plataforma común reutilizable, preparación por tienda, equipos paralelos, costo, soporte y evidencia para pasar a la siguiente ola. La revisión de recursos de la sesión 06, p. 8, ayuda a distinguir una secuencia lógica de un plan ejecutable. Si una condición falla, actualizar el compromiso por la autoridad prevista y comunicar impactos. No hace falta implementar una cadena real para defender el ejercicio, pero la explicación debe ser coherente.

## Complemento de sesiones 05 y 06

| Material docente disponible | Aplicación incorporada | Límite de evidencia |
| --- | --- | --- |
| [Sesión 05](../insumos/presentaciones/sesion-05_estimacion_y_priorizacion.pdf), pp. 4 a 11 | Separar objetivo, estimación y compromiso; elegir técnica por horizonte y datos; dejar base reproducible de estimación en 06. | Sin históricos suficientes no afirmar percentiles, P80/P90 o simulaciones calibradas. Story points no equivalen automáticamente a horas. |
| Sesión 05, pp. 12 a 15 | Conservar matriz multicriterio de 05; explicar urgencia/costo de demora relativo a M5/M8 y respetar dependencias/capacidad. | WSJF/CoD son herramientas posibles, no requisitos adicionales. No inventar pérdidas diarias ni duplicar score para aumentar artefactos. |
| [Sesión 06](../insumos/presentaciones/sesion-06_cronograma_y_flujo.pdf), pp. 5 a 10 | Dependencias, capacidad por periodo, diferencia entre referencia aprobada y forecast; planificación progresiva en 07. | Las olas por sí solas no prueban dotación ni ruta crítica calculada. |
| Sesión 06, pp. 11 a 17 | Políticas de flujo, límites WIP por capacidad y métricas de terminados, tiempo de ciclo y bloqueos en 02/07. | 29 altas/mes es ritmo requerido por el objetivo, no throughput histórico. No aplicar ley de Little como garantía en un sistema inestable. |

## Qué no se traslada desde los ejercicios

Abandono 42%, objetivo 25% de sesión 04, fecha de siete meses, biometría, fraude y sponsor Director de Canales corresponden a onboarding. Los ocho integrantes empresariales del ejemplo de sesión 05, el SDK en seis semanas y los 12 ítems en progreso de sesión 06 también pertenecen a sus ejercicios. ZEUS conserva enunciado propio, sponsor Gerente General y supuestos empresariales diferenciados del equipo académico de cuatro.

Las anécdotas sobre costos de nube, modalidades contractuales o legislación ilustran experiencias y no son cotizaciones, comparaciones universales ni verificación legal para ZEUS. Se preservan en las transcripciones sin adoptar esas afirmaciones como hechos del caso.

## Pendientes que permanecen

Rogelio: cuantificar estimación, revisar capacidad/puntajes y financiación. Maverick: cerrar CD/familias, aceptación por ola y dependencias del alcance/roadmap. Equipo: resolver metas piloto, devolución parcial y límites experimentales; integrar presentación/ensayo y confirmar formato/hora de carga.

En el material revisado de clase 3 no se identifica una nueva fecha ni obligación de informe adicional. Se conserva entrega/presentación del 24 de octubre respaldada por clase 2 y pauta; viernes 23 sigue siendo cierre interno propuesto. La transcripción automática no fue cotejada con audio y no equivale a una solución docente aprobada para ZEUS.

Actualización 22 de octubre: CD/familias, aceptación por ola, umbrales y límites experimentales ya tienen propuesta en el [escenario provisional](escenario_provisional.md). Siguen pendientes de revisión del equipo y costo; no son incógnitas sin una alternativa de trabajo.
