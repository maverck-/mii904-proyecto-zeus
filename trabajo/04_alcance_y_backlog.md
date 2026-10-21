# 4. Diseño del alcance y backlog

**Responsable indicado: Maverick. ESC-02, propuesta para revisar.** Se completa el alcance que quedó abierto en el Charter del equipo y se preserva su secuencia 10/68/R3. Fuentes: enunciado pp. 5 y 8, [avance recibido](../insumos/avance_equipo_2026-10-21.md) y [supuestos](../registros/acuerdos_y_supuestos.md).

## Alcance del producto y del proyecto

Según sesión 04, pp. 5 a 8, y clase 3, parte 2, 10:44 a 17:49 ([aportes](../registros/aportes_clase_03.md)):

| Vista | Aplicación a ZEUS |
| --- | --- |
| Producto | Inventario/reserva, estados de pedido, C&C/app, devoluciones y capacidades operativas; controles y cualidades del servicio. |
| Proyecto | Formular, adquirir/configurar, integrar, probar, preparar datos/tiendas, formar, desplegar, medir, transicionar y transferir soporte/beneficios. |

El producto continúa evolucionando tras M12. El proyecto no termina con instalar software: requiere aceptación, transferencia y responsables para beneficios pendientes. Ambos alcances se costean sin duplicar trabajo.

## Fronteras y cobertura

Incluye OMS adquirido/configurado e integrado, contratos API/datos, inventario y reserva, pedidos trazables, Click & Collect (C&C), app de preparación en tienda, formación, continuidad, soporte, seguridad, observabilidad y medición. En R3: devoluciones elegibles, ampliación de observabilidad y experimento limitado de Ship-from-store sujeto a G2/M9. La instrumentación básica y controles empiezan con el primer flujo, no en R3.

R1: **10 tiendas piloto hasta M5**, proponiendo uso desde M4. R2: **objetivo de 68 tiendas totales en M7**, sujeto a evidencia y capacidad. Son 58 tiendas adicionales, no 68 nuevas. R3 hasta M12 no implica expandir Ship-from-store a toda la cadena. Número de CD, familias, tiendas experimentales y pedidos elegibles deben definirse con dependencias y costo; el caso informa 3 CD, pero no obliga a incorporarlos todos en R1.

Selección de tiendas propuesta: volumen evaluable, calidad de stock, turnos/dotación, espacio, soporte, diversidad y acceso a interfaces/CD. No hay evidencia de que 10 sea el tamaño óptimo. SUP-05 conserva ese supuesto del equipo para evaluarlo.

Fuera: reemplazo ERP o WMS completo, IA/recomendaciones, data platform corporativa completa, migración amplia a cloud y plataforma corporativa de identidad nueva. Se mantienen adaptaciones acotadas de WMS, datos operacionales, cloud selectivo costeado e identidad/acceso obligatorios. Ship-from-store nacional queda fuera; solo se propone experimento acotado condicionado.

Interfaces: ERP, WMS, POS, e-commerce, pagos, logística y CRM en cuanto afecten flujo/conciliación. Cada una necesita dueño, contrato, prueba, recuperación y soporte. Mantener un sistema no elimina su trabajo de integración.

## Capacidades y aceptación propuesta

| ID | Capacidad | Dependencias | Release | Aceptación propuesta |
| --- | --- | --- | --- | --- |
| CAP-01 | Base, arquitectura y viabilidad de integración/OMS | Acceso a datos/proveedores | R0 | Base por cohorte, contrato de datos, prueba representativa y forecast revisado; VT-01. |
| CAP-02 | Inventario consistente y reservas | CAP-01; stock físico | R1 | Reserva concurrente, vencimiento y excepciones probados; KPI-01/KPI-02 medibles. |
| CAP-03 | OMS y pedidos trazables | CAP-01/CAP-02 | R1 | Estados de confirmación a retiro, idempotencia, conciliación y recuperación sin pérdidas no resueltas. |
| CAP-04 | C&C y app de preparación | CAP-02/CAP-03/CAP-05/CAP-06 | R1 | Retiro real, proceso/dotación aceptados; KPI-03/KPI-06 y evidencia de primera mejora hasta M5. |
| CAP-05 | Seguridad, observabilidad y métricas | Desde inicio | R0 a R3 | Controles, eventos auditables, alertas atendidas y riesgos críticos tratados; ampliación en R3. |
| CAP-06 | Adopción, continuidad y soporte | Desde inicio | R0 a R3 | Formación, dueño operativo, transición/reversión y soporte aceptados por sitio. |
| CAP-07 | Escala a 68 y preparación de campaña | R1/G1, capacidad y costo | R2 | Cada ola operable, evidencia y pruebas de carga/recuperación; VE-01 antes de campaña. |
| CAP-08 | Devoluciones elegibles | CAP-03; reglas Comercial/Finanzas | R3 | Caso completo con conciliación y trazabilidad; medir KPI-04 sin presentar ≥85% como ≥90%. |
| CAP-09 | Experimento Ship-from-store | Pedidos/inventario, logística y G2 | R3 condicionado | Hipótesis y muestra delimitadas, costo máximo y criterios de éxito/parada acordados antes de iniciar; resultado documentado. |

CAP-05/CAP-06 son condiciones del flujo completo. No se eliminan por menor atractivo comercial. La aceptación técnica no sustituye evidencia de beneficio ni una cohorte elegible permite atribuir la mejora a toda la compañía.

## Trazabilidad de objetivos a valor

| Objetivo / condición | Capacidad | Entregable y costo | Aceptación / evidencia | Release / valor esperado |
| --- | --- | --- | --- | --- |
| KPI-01/KPI-02 | CAP-02, apoyada por CAP-03 | Reserva/inventario e interfaces; PAQ-02/PAQ-03 | Concurrencia/excepciones y medición de latencia/cancelación | R1: promesas confiables y menos cancelaciones. |
| KPI-03/KPI-06 | CAP-03/CAP-04/CAP-06 | Pedido trazable, app, proceso y formación; PAQ-03/PAQ-04 | Retiro real, preparación y adopción por cohorte | R1 y olas R2: eficiencia y uso operativo. |
| KPI-05 y continuidad/seguridad | CAP-05/CAP-06 | Controles, observabilidad, recuperación y soporte; PAQ-06/PAQ-07 | Riesgos críticos tratados, servicio operable y ventana de disponibilidad | Desde R1, VE-01/campaña y R3: resiliencia. |
| Cobertura objetivo del equipo | CAP-07 | Habilitación de 58 tiendas adicionales; PAQ-04/PAQ-07 | Cada sitio/ola aceptado con capacidad, stock y soporte | R2: ampliar uso/beneficio; 68/M7 es objetivo, no evidencia de valor por sí solo. |
| KPI-04 | CAP-08 | Devoluciones elegibles; subpartida PAQ-05 | Conciliación, trazabilidad y resolución al primer contacto | R3: atención; distinguir ≥85% proyecto de ≥90% estratégico. |
| Aprendizaje para invertir o detener | CAP-01/CAP-09 | Viabilidad inicial y experimento acotado; PAQ-01/PAQ-05 | Prueba técnica / hipótesis experimental evaluada | R0/R3: reducir incertidumbre; no declarar ventas recuperadas automáticamente. |

La fila vincula vistas; no agrega un nuevo costo a cada aparición del PAQ. La suficiencia de evidencia de beneficio se resuelve en 01 y gates de 07.

## EDT y fronteras de costo

CAP identifica capacidades; PAQ identifica paquetes para estimación/control. Una capacidad puede consumir varios paquetes, sin cobrarla dos veces.

| Paquete | Entregable / frontera de costo | Capacidades vinculadas | Dueño empresarial propuesto |
| --- | --- | --- | --- |
| PAQ-01 | Formulación, gobierno, arquitectura y aprendizaje de viabilidad | CAP-01 y coordinación | PM/Arquitectura |
| PAQ-02 | Integración, inventario, reserva y reconciliación | CAP-01/CAP-02 | Tecnología/Logística |
| PAQ-03 | OMS: configuración, interfaces y trazabilidad de pedidos | CAP-03 | Tecnología/PO |
| PAQ-04 | C&C/app y habilitación local: piloto y 58 altas adicionales | CAP-04/CAP-06/CAP-07 | Operaciones/Tiendas |
| PAQ-05 | Devoluciones y experimento Ship-from-store, separados como subpartidas | CAP-08/CAP-09 | Operaciones/Comercial/Logística |
| PAQ-06 | Controles, QA transversal, rendimiento, observabilidad y resiliencia | CAP-05 y pruebas comunes | CISO/Tecnología |
| PAQ-07 | Transición, soporte y recurrentes cloud/licencias de los 12 meses | CAP-06/CAP-07 y medición | Operaciones/Tecnología |

Jerarquía propuesta: ZEUS → habilitación inicial y gobierno (PAQ-01), flujo omnicanal (PAQ-02/PAQ-03/PAQ-04), evolución condicionada (PAQ-05) y preparación/operación transversal (PAQ-06/PAQ-07). Las ramas organizan el alcance completo comprometido y condicionado, sin repetir un paquete. Las CAP del backlog pueden atravesar ramas; no son nuevos paquetes sumables. Detallar subentregables próximos para estimar, manteniendo lo lejano proporcional a la evidencia (sesión 04, pp. 10/12/16).

PAQ-04 incluye formación/habilitación local de todas las olas; PAQ-05 ya no duplica expansión C&C. PAQ-03 incluye configuración OMS; PAQ-07 sus licencias recurrentes, explicitando cargos de implantación si los hubiera. El esfuerzo funcional se imputa a su paquete; QA transversal a PAQ-06. Separar gasto interno, externo y horas de tienda en 06. Todo cambio de frontera exige reestimar.

## Historias iniciales y calidad

- Cliente: comprar sobre stock reservable; aceptar éxito, vencimiento, concurrencia y manejo de stock obsoleto.
- Personal de tienda: preparar y entregar pedido con promesa visible; aceptar estados, prioridad, permisos y excepciones.
- Operación: detectar y atender desactualización o pedidos detenidos; aceptar señal, destinatario, tiempo y procedimiento de respuesta.
- Atención: resolver devolución elegible con reglas y conciliación; aceptar estados, excepciones y trazabilidad.

DoD propuesta: criterio funcional, pruebas necesarias, controles, telemetría, documentación, soporte, reversión y aceptación operacional. Antes de R1 fijar magnitud mínima de mejora y suficiencia de evidencia para M5. El experimento CAP-09 requiere su propia hipótesis y límite, no una historia abierta de logística sin costo.

Ejemplo de distinción: aceptar CAP-04 exige que un pedido reservable pueda prepararse y retirarse con estados/permiso correctos y que se mida su uso; la DoD exige además pruebas, revisión de seguridad, telemetría, documentación y reversión. Cumplir la función sin esa calidad no habilita liberar; cumplir DoD sin uso/mejora no acredita beneficio.

## Cambios y acuerdos pendientes

Confirmar CD/familias, viabilidad de 58 altas en dos meses, adopción por ola, metas piloto y límites del experimento. PO ordena dentro de límites; PM integra impacto; sponsor/comité acepta cambios de cobertura comprometida, costo, fecha o beneficio. CISO y Operaciones deciden sobre exposición crítica y operabilidad. Actualizar estimación y roadmap al cambiar alcance.
