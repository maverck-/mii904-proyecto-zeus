# 3. Project Charter

**ZEUS: Plataforma Omnicanal Modular. ESC-02, propuesta integrada desde el equipo, revisión 22-10-2026.** Las condiciones empresariales aún no están autorizadas. La [revisión de integración](../registros/integracion_avance_equipo.md) identifica correcciones y decisiones pendientes.

## Propósito y contribución

Construir una plataforma que integre inventario, pedidos, tiendas y devoluciones mediante servicios reutilizables, para ofrecer una experiencia omnicanal consistente y reducir complejidad de integración. Sponsor: **Gerente General**.

Contribuye a las metas estratégicas de 35% de ventas digitales, NPS ≥+48, puntualidad ≥95% y abandono de carro <55%. No se garantiza atribución íntegra a ZEUS. La creación de tecnología debe traducirse en uso, beneficio y valor.

## Objetivos medibles del equipo, con horizonte propuesto

| ID | Objetivo del proyecto | Horizonte/cobertura propuestos | Referencia |
| --- | --- | --- | --- |
| KPI-01 | Cancelaciones por stock de 7,8% corporativo a <2% | M12, operación cubierta; validar base comparable | Meta estratégica p. 4; objetivo del equipo. |
| KPI-02 | Actualización web de 45 a 120 min a <2 min | M12, interfaces cubiertas | Meta del caso; precisión de método en 01. |
| KPI-03 | Preparación media de 7,2 h a <3 h | M12, separar flujos de retiro/despacho | Meta del caso; validar base por cohorte. |
| KPI-04 | Devoluciones de 64% corporativo a ≥85% primer contacto | M12, casos elegibles del alcance | Objetivo propuesto del equipo; meta estratégica ≥90%, brecha explícita de 5 pp. |
| KPI-05 | Disponibilidad e-commerce ≥99,9%, protegida en Black Friday | Campaña M8 y ventanas regulares acordadas | Meta del caso y criterio operativo propuesto. |
| KPI-06 | >80% de pedidos C&C preparados mediante la aplicación | Piloto y cada ola aceptada; validar fechas por release | Criterio de adopción propuesto por equipo. |

El horizonte M12 y la cobertura/ventanas se proponen para hacer verificables los objetivos. En G1/M5 debe existir evidencia de primera entrega de valor, no solo una instalación. Definiciones y evaluación en [01](01_diagnostico_y_business_case.md). SUP-16 propone para M5 reducciones relativas de 20% en cancelación y 25% en preparación frente a bases comparables, salvo base ya mejor que meta final, con adopción >80% por tienda y evidencia suficiente; revisar antes de autorizar. No equivale a las metas finales de M12.

## Alcance incluido

OMS adquirido/configurado e integrado; inventario, reserva y disponibilidad mediante APIs/servicios; pedidos, C&C y aplicación para preparación; formación y adopción; controles, métricas, observabilidad mínima, continuidad y soporte desde R1; expansión por olas; devoluciones y ampliación de observabilidad en R3. Experimento acotado de Ship-from-store en R3, condicionado a hipótesis, capacidad y financiación aprobadas en M9.

## Alcance excluido

Reemplazo del ERP o reemplazo completo del WMS; se permiten adaptaciones acotadas del WMS. IA/recomendaciones, data platform corporativa completa, migración amplia a cloud y nueva plataforma corporativa de identidad. La exclusión de una plataforma de identidad nueva no elimina controles de identidad/acceso obligatorios. Cloud selectivo puede usarse si es necesario y se costea.

## Entregables principales y cobertura

| Release | Propuesta del equipo integrada | Condición |
| --- | --- | --- |
| R0, M1/M2 | Formulación, arquitectura, selección/contratación escalonada OMS, prueba de integración y base | No sustituye primera entrega de valor. |
| R1, hasta M5 | Piloto C&C en 10 tiendas, 1 CD y 2 familias de productos, con habilitación al inicio de M4 y evaluación hasta M5 | Sitios, volumen, métricas y operación aceptados; número 10 es supuesto. |
| R2, hasta M7 | Objetivo C&C en las 68 tiendas, listo para campaña M8 | Ampliar 58 tiendas en olas, hasta 3 CD y las mismas 2 familias, solo si capacidad, coste y operación lo sostienen. El caso no exige esa fecha de cobertura. |
| R3, hasta M12 | Devoluciones, ampliación de observabilidad y piloto Ship-from-store | Gate M9: experimento propuesto de 2 tiendas, máximo 4 semanas/200 pedidos y exposición incremental ≤30 MM CLP incluida en presupuesto; estimación por completar. No posponer toda observabilidad a R3. |

Si el objetivo 68/M7 no es defendible, el grupo debe cambiarlo explícitamente con su impacto. No se lo reemplaza por la cobertura 5/20/35 del escenario anterior por conveniencia.

## Roles y derechos de decisión

| Rol | Responsabilidad / derecho |
| --- | --- |
| Comité Ejecutivo | Gates, financiación y aceptación de cambios de baseline que afecten inversión/beneficio. |
| Sponsor Gerente General | Propósito, prioridades y cambios de fecha/alcance mayor dentro de límites; escalar los que alteran condiciones del caso. |
| PM de ZEUS | Coordinar frentes, dependencias, riesgos, cambios y forecast. ZEUS se trata aquí como proyecto con frentes; no se presupone un programa formal sin definirlo. |
| PO e-commerce y función PO/representante de tiendas | Priorizar backlog por release dentro de objetivos/guardrails. El rol adicional de tiendas es propuesta organizacional. |
| Gerente de Tecnología / Arquitectura Empresarial | Estándares, interfaces y viabilidad técnica. |
| CISO | Controles y facultad de detener release ante riesgo crítico. |
| Logística / Operaciones / gerencias de tienda | Beneficios, dotación, capacidad y aceptación operacional; pueden impedir una salida no operable. |
| Finanzas | Costo total, forecast, reservas y liberación financiera con comité. |
| Proveedores WMS, OMS y cloud | Compromisos, integración, licencias y soporte según contrato. OMS comprado es supuesto del equipo. |

Stakeholders adicionales: Comercial, equipos de desarrollo y usuarios de las tiendas. Los cuatro integrantes académicos no son los cinco equipos empresariales supuestos.

La sesión 03, p. 11, pide mostrar decisiones y dependencias además de listar interesados. Se propone este vínculo de participación, sin atribuir validaciones ya realizadas:

| Interesado | Impacto / aportación | Decisión o dependencia que debe coordinarse |
| --- | --- | --- |
| Clientes y personal de tiendas | Viven compra, preparación, retiro y devolución | Feedback y aceptación del flujo con PO/Operaciones; no aprueban por sí solos cambios de presupuesto. |
| Gerencias de tienda / Logística | Absorben formación, turnos, stock y carga | Disponibilidad y aceptación de cada sitio/ola; condición de operabilidad. |
| Proveedores ERP/WMS/OMS | Condicionan datos, interfaz y soporte | Hitos contractuales y evidencia antes de VT-01/olas; PM/Tecnología coordinan. |
| Finanzas, CISO y Arquitectura | Evalúan costo, exposición y viabilidad | Evidencia para comité y aceptación de controles/arquitectura según derechos anteriores. |

Si cambia un objetivo, límite o financiación, actualizar este Charter y comunicar a los interesados afectados; no dejar el cambio solo en una reunión (clase 3, parte 2, 55:53 a 57:57). El detalle operativo permanece en 04 a 07.


## Restricciones, supuestos y riesgos

Techo máximo preliminar **1.500 MM CLP**, horizonte 12 meses, valor dentro de los primeros cinco meses, Black Friday aproximadamente M8; ERP no reemplazado, WMS solo modificado, continuidad y controles obligatorios (enunciado p. 5).

Supuestos: API/eventos útiles del ERP, cumplimiento WMS, OMS de mercado, cinco equipos disponibles, diez tiendas piloto, escalamiento a 68, evidencia a M5 y recursos para experimento. Todos requieren validación académica de coherencia y validación empresarial hipotética descrita en el [registro](../registros/acuerdos_y_supuestos.md).

Riesgos: exactitud de stock insuficiente (91% corporativo como condición base), retrasos de WMS, capacidad de tiendas/equipos, campaña, sobrecosto y bloqueo por seguridad. El 91% es una condición que puede generar promesas erróneas; formular riesgo como evento/efecto, no llamar riesgo a la cifra por sí sola. [Registro de riesgos](../registros/riesgos.md).

## Presupuesto y financiación

El equipo propone un marco máximo preliminar de **1.500 MM CLP** liberado por tramos. Esto es un techo para formular, no una estimación bottom-up ni una aprobación de gasto. Referencia B del caso: **1.350 MM CLP**. Rogelio debe reestimar alcance 10/68, cinco equipos, licencias/operación y R3/experimento, definir reservas y primer tramo antes de cerrar el Charter.

Se retiran los totales 1.215/1.700 MM y dedicaciones de ESC-01 como cifras vigentes: correspondían a otra cobertura/exclusiones. Métodos y estructura de estimación permanecen como apoyo en [06](06_estimacion.md).

## Hitos y criterios de salida

G0/M1: aprobación de arquitectura inicial y selección/contratación OMS por hitos, con financiación y validación técnica condicionadas. VT-01/M2: revisión de viabilidad antes del piloto/escala. G1/M5: evidencia de primera entrega y decisión de ampliar. VE-01/M7: preparación, cobertura segura y congelamiento de cambios de alto riesgo, con excepciones críticas controladas. Campaña aproximadamente M8. G2/M9: beneficios/forecast y financiación de R3. Cierre M12: aceptación y traspaso con responsables de beneficios pendientes.

Éxito propuesto: objetivos medidos, adopción >80%, ejecución dentro del costo autorizado compatible con techo, riesgos críticos de seguridad tratados y campaña operable. «Sin interrupciones» es objetivo de continuidad, no garantía anticipada de resultado. Para aprobación de release exigir pruebas y soporte, además de medir disponibilidad con ventana definida.

## Precisión del escenario del 22 de octubre

El [escenario provisional del 22 de octubre](../registros/escenario_provisional.md) desarrolla SUP-14 a SUP-17: selección de familias, aceptación por sitio/ola, base de brigadas y CD, umbrales M5 y experimento. Se conserva devolución ≥85% en casos elegibles a M12 como aporte parcial, sin prometer el ≥90% corporativo ni la misma población de medición. Ampliar catálogo o Ship-from-store nacional requiere cambio explícito y nueva estimación. No hay consenso grupal ni disponibilidad empresarial acreditados por esta actualización.

## Solicitud de autorización

Solicitar al Comité aprobar la formulación y las condiciones de financiación inicial de R0/R1. Cuantificar el primer tramo antes de cerrar la solicitud; no dar por autorizado todo el presupuesto. Cada liberación depende de evidencia técnica, operación, costo y riesgos, manteniendo trazabilidad entre Business Case, alcance y roadmap.
