# 4. Diseño del alcance y backlog

**Responsable: Maverick. ESC-02, propuesta desarrollada al 23-10-2026 para revisión del equipo.** El alcance prioriza un flujo C&C completo, su expansión a 68 tiendas y una evolución R3 condicionada. Fuentes: enunciado pp. 5 y 8, [avance inicial](../insumos/avance_equipo_2026-10-21.md), [actualización del equipo](../insumos/avance_equipo_2026-10-23.md) y [supuestos](../registros/acuerdos_y_supuestos.md). El [plan de apoyo](../registros/plan_alcance_roadmap.md) detalla las nuevas hipótesis de calendario, carga y habilitación.

## Alcance del producto y del proyecto

Según sesión 04, pp. 5 a 8, y clase 3, parte 2, 10:44 a 17:49 ([aportes](../registros/aportes_clase_03.md)):

| Vista | Aplicación a ZEUS |
| --- | --- |
| Producto | Inventario/reserva, estados de pedido, C&C/app, devoluciones y capacidades operativas; controles y cualidades del servicio. |
| Proyecto | Formular, adquirir/configurar, integrar, probar, preparar datos/tiendas, formar, desplegar, medir, transicionar y transferir soporte/beneficios. |

El producto continúa evolucionando tras M12. El proyecto no termina con instalar software: requiere aceptación, transferencia y responsables para beneficios pendientes. Ambos alcances se costean sin duplicar trabajo.

CAP-02 incluye el servicio de disponibilidad y reserva de inventario, sus interfaces y la gestión de excepciones. La actualización web en menos de dos minutos es una meta del servicio (KPI-02), con horizonte y método definidos en 01/03. Esta separación permite identificar tanto el entregable como el resultado que se evaluará.

## Fronteras y cobertura

Incluye OMS adquirido/configurado e integrado, contratos API/datos, inventario y reserva, pedidos trazables, Click & Collect (C&C), app de preparación en tienda, formación, continuidad, soporte, seguridad, observabilidad y medición. En R3: devoluciones elegibles, ampliación de observabilidad y experimento limitado de Ship-from-store sujeto a G2/M9. La instrumentación básica y controles empiezan con el primer flujo, no en R3.

R1: **10 tiendas piloto hasta M5**, proponiendo flujo usable al terminar semana 16, durante M4. R2: **objetivo de 68 tiendas totales en M7**, sujeto a evidencia y capacidad. Son 58 tiendas adicionales, no 68 nuevas. SUP-14 delimita la cobertura propuesta: **dos familias de productos, un CD en piloto y hasta tres CD en expansión, manteniendo las mismas familias**. El grupo debe ratificar esta frontera y contrastarla con el esfuerzo 104 y costo 1.330. Su inclusión en la estimación original todavía no está verificada.

Las dos familias se seleccionan en M1 por su participación en pedidos digitales, cancelaciones y contribución, junto con stock auditable, rotación y logística estándar, sin cadena de frío ni tratamiento especial. Registrar esas participaciones y volumen elegible en la ficha económica antes de sostener la inversión. La selección concreta queda pendiente. Preparar cada CD exige prueba de datos/contratos y soporte; un CD piloto no demuestra cobertura nacional. Cubrir 68 tiendas significa habilitar el flujo C&C definido para ese catálogo, no todo producto, canal o modalidad logística de la compañía.

En R3 se proponen devoluciones de compras web de esas familias, identificables en el OMS y atendidas en tiendas habilitadas, con reglas de elegibilidad, conciliación y forma de restitución acordadas con Comercial/Finanzas. No incluye cualquier devolución histórica o de cualquier canal por inferencia. Esta frontera explica por qué ≥85% de casos elegibles no acredita ≥90% corporativo. Ampliarla requiere reestimar.

Selección de tiendas propuesta: volumen evaluable, calidad de stock, turnos/dotación, espacio, soporte, diversidad y acceso a interfaces/CD. No hay evidencia de que 10 sea el tamaño óptimo. SUP-05 conserva ese supuesto del equipo para evaluarlo.

Fuera: reemplazo ERP o WMS completo, IA/recomendaciones, data platform corporativa completa, migración amplia a cloud y plataforma corporativa de identidad nueva. Se mantienen adaptaciones acotadas de WMS, datos operacionales, cloud selectivo costeado e identidad/acceso obligatorios. Las familias concretas deben identificarse en M1; Ship-from-store nacional queda fuera; solo se propone experimento acotado condicionado.

Interfaces: ERP, WMS, POS, e-commerce, pagos, logística y CRM en cuanto afecten flujo/conciliación. Cada una necesita dueño, contrato, prueba, recuperación y soporte. Mantener un sistema no elimina su trabajo de integración.

### Proceso logístico y contrato funcional con WMS

Como precisión de CAP-01/CAP-02/CAP-03, proponer en R0 un mapa desde inventario físico hasta preparación y retiro/entrega, con tiempos de espera, trabajo activo, responsables y excepciones. Distinguir stock físico, disponible y reservable; acordar quién confirma cada movimiento, evita doble reserva y concilia discrepancias entre WMS/ERP/tienda/OMS. La asignación concreta se valida con los sistemas existentes, sin asumir al OMS como dueño único del stock.

El WMS gestiona ejecución y recursos del almacén/CD; el OMS coordina pedidos y su cumplimiento; transporte/operador ejecuta el trayecto de despacho, con fronteras por verificar. Las [referencias funcionales EXT-07 a EXT-09](../insumos/evidencia_logistica_y_valor.md) orientan esa distinción, sin seleccionar nuevos productos. Antes del piloto, probar disponibilidad/movimientos, reserva o liberación según contrato, confirmación de preparación, cancelación y recuperación de eventos repetidos o tardíos. Tecnología, CISO y Logística validan el patrón en VT-01 y por release; responsables delegados aplican la lista por sitio y escalan excepciones.

**Corte R1:** reserva simple y ventana de retiro fija comunicada por tienda, con horario de corte y volumen de exposición acordados por Operaciones. La admisión puede limitarse mediante configuración existente o control operativo documentado. HU-01/HU-03 conservan la prueba de reserva y el flujo de preparación/retiro. Cupos dinámicos, optimización de ventanas y búsqueda automática de un punto alternativo quedan fuera de R1 y de las 104 unidades estimadas; una incorporación posterior requiere refinamiento, estimación y autorización de cambio. Si la plataforma necesita desarrollo adicional incluso para el corte simple, actualizar E1–E5 y la fecha antes de abrir.

E1/E11 deben incluir validación inicial de existencias y conteo cíclico del catálogo piloto, con responsable de ajustes y conciliación. La regla de stock reservable descuenta reservas vigentes y un colchón configurable aprobado por Logística; el parámetro se calibra con discrepancias y riesgo de sobreventa, sin inferirlo del 91% corporativo. Ese porcentaje de exactitud no equivale a una tasa de 9% de pedidos fallidos. Registrar frecuencia, unidades a contar y minutos activos por unidad/turno como carga operativa a costear; estos trabajos deben conciliarse con E1/E11/COST-06 antes de afirmar su cabida.

Se propone reutilizar zonas de servicio y puntos elegibles existentes. La indexación hexagonal H3 es una opción técnica de análisis espacial, no un componente seleccionado. Motor de ruteo avanzado, adquisición de TMS, rediseño nacional de transporte, nueva infraestructura física y entregas domiciliarias ultrarrápidas quedan fuera de la base estimada; cualquier evaluación posterior requiere caso y autorización. No se confirma el uso de hexágonos por retailers concretos.

Cloud selectivo se justifica por necesidad del flujo, capacidad y costo total, con revisión de Tecnología/Arquitectura, Finanzas, CISO y Operaciones. La propuesta del proveedor no convierte una migración amplia en alcance incluido; cualquier cambio de frontera debe evaluarse y autorizarse con impacto en PAQ/categorías de costo.

## Alcance fijo, adaptable y condicionado

| Tratamiento | Elementos de esta propuesta | Regla de decisión |
| --- | --- | --- |
| Restricción del caso | Techo 1.500 MM, horizonte 12 meses, valor dentro de cinco, continuidad, controles, ERP conservado y WMS sin reemplazo completo | No flexibilizarlas para declarar cumplimiento; cambiar alternativa o elevar incompatibilidad. |
| Compromiso propuesto sujeto a autorización | Flujo completo en diez tiendas/M5, objetivos del Charter y preparación de campaña | Cambiar con impacto en beneficios, costo y fechas, mediante sponsor/comité. |
| Meta de expansión por dimensionar | 68 tiendas/M7 para el catálogo definido | G1 fija cobertura previa a campaña con recursos, CD y acompañamiento conciliados; 68/M7 sigue como objetivo condicionado. |
| Adaptable dentro de límites | Historias, UX, orden técnico, selección de tiendas y distribución de olas | PO y equipos ajustan sin eliminar aceptación, controles o cobertura comprometida. |
| Condicionado / diferible | Ruteo avanzado, centralización adicional y experimento Ship-from-store tras G2 | Evaluar costo de oportunidad; no eliminar devoluciones si se mantiene KPI-04. |

### Experimento de Ship-from-store propuesto

SUP-17 se concreta en una prueba con tres tiendas inicialmente, ampliable a cinco solo tras una primera semana operable, máximo cuatro semanas o 300 pedidos elegibles totales, lo que ocurra primero. Se propone ejecutarla en M11, con stock del catálogo acordado, operador logístico y conciliación definidos, tras autorizarla en G2. Estos límites son supuestos del diseño, pendientes de ratificación.

Hipótesis: despachar desde tienda puede cumplir la promesa sin deteriorar C&C ni inventario, con costo por pedido y contribución evaluables frente a un flujo comparable desde CD. Registrar cumplimiento, cancelación, esfuerzo de tienda, transporte y margen incremental; no fijar una rentabilidad sin datos. Detener por pérdida no conciliada, exposición crítica, promesas no sostenibles o perjuicio al flujo C&C. Si hay poca evidencia, declarar inconcluso.

E10 conserva su media de 5,3333 equipo-sprints dentro de las 104 unidades; no es una bolsa adicional de gasto. Antes de iniciar, Finanzas debe fijar un techo monetario de exposición y explicar transporte, devoluciones y horas de tienda dentro del presupuesto autorizado. Sin esa autorización no se ejecuta. La duración de cuatro semanas no incluye preparación y evaluación, que también forman parte de E10.

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
| CAP-09 | Experimento Ship-from-store | Pedidos/inventario, logística y G2 | R3 condicionado | Experimento en 3 a 5 tiendas, hasta cuatro semanas/300 pedidos propuestos; ratificar límites/hipótesis y autorizar exposición monetaria en G2; resultado documentado, incluso inconcluso. |

CAP-05/CAP-06 son condiciones del flujo completo. No se eliminan por menor atractivo comercial. La aceptación técnica no sustituye evidencia de beneficio ni una cohorte elegible permite atribuir la mejora a toda la compañía.

## Correspondencia de épicas del equipo con alcance y EDT

E identifica épicas usadas por WSJF/estimación; CAP identifica capacidades y PAQ paquetes de alcance. Las tres vistas no se suman como trabajo distinto. La separación entre trabajo de equipos y servicios de proveedores debe conciliarse en 06.

| Épica | Capacidad vinculada | Paquete de alcance principal / coordinación |
| --- | --- | --- |
| E1 | CAP-02 | PAQ-02: disponibilidad, stock/reserva. |
| E2 | CAP-01/CAP-02/CAP-03 | PAQ-02: interfaces y contratos de datos; coordinar interfaces OMS sin duplicarlas. |
| E3 | CAP-03 | PAQ-03: configuración e integración OMS. |
| E4 | CAP-04 | PAQ-04: flujo C&C cliente. |
| E5 | CAP-04/CAP-06 | PAQ-04: app/proceso de preparación. |
| E6 | CAP-05 | PAQ-06: seguridad/calidad; distinguir herramientas y pruebas externas. |
| E7 | CAP-07/CAP-05 | PAQ-06 y coordinación PAQ-07: carga, contingencia y campaña. |
| E8a | CAP-05 | PAQ-06/PAQ-07: ingeniería básica y recurrentes separados. |
| E8b | CAP-05 | PAQ-06/PAQ-07: centralización adicional y recurrentes separados. |
| E9 | CAP-08 | PAQ-05: devolución elegible. |
| E10 | CAP-09 | PAQ-05: experimento Ship-from-store. |
| E11 | CAP-06/CAP-07 | PAQ-04: rollout/formación; coordinar PAQ-07 para soporte. |

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

PAQ-04 incluye formación/habilitación local de todas las olas; PAQ-05 se reserva para devoluciones y el experimento. PAQ-03 incluye configuración OMS; PAQ-07 sus licencias recurrentes, explicitando cargos de implantación si los hubiera. El esfuerzo funcional se imputa a su paquete; QA transversal a PAQ-06. Separar gasto interno, externo y horas de tienda en 06. Todo cambio de frontera exige reestimar.

## Historias iniciales y calidad

Backlog inicial propuesto para refinar dentro de las épicas ya estimadas, sin agregar esfuerzo como una lista independiente:

| Historia | Usuario y resultado | Criterio de aceptación concreto | Capacidad / momento |
| --- | --- | --- | --- |
| HU-01 | Cliente compra sobre stock reservable | Con una unidad y dos solicitudes simultáneas, no se confirman dos reservas sobre esa unidad; expiración libera stock y queda trazada | CAP-02; antes de piloto. |
| HU-02 | Operación sigue un pedido completo | Confirmación, preparación y retiro mantienen identificador/estado conciliable; un evento repetido no duplica pedido ni movimiento | CAP-03; antes de piloto. |
| HU-03 | Personal prepara y entrega con la app | Un rol habilitado ve la promesa, cambia estados y registra retiro; permisos y ruta de excepción se prueban con tienda | CAP-04/CAP-06; piloto y olas. |
| HU-04 | Operación atiende fallos de stock o pedido | Se simula falla/desactualización y llega alerta a responsable; se ejecuta recuperación o reversión con conciliación | CAP-05/CAP-06; antes de cada exposición. |
| HU-05 | Atención resuelve una devolución elegible | Identifica compra, aplica regla y restitución acordadas, actualiza pedido/stock y deja conciliación; no duplica restitución al reintentar | CAP-08; R3. |
| HU-06 | Logística evalúa un despacho desde tienda | Solo acepta tienda/pedido del experimento; registra promesa, costo y resultado, y permite detener nuevas asignaciones | CAP-09; después de G2. |

### Aceptación por sitio, por release y del proyecto

Cada tienda/CD presenta una lista estándar con evidencia de datos/reservas, formación por turno, pedido completo, conciliación, alertas atendidas, soporte y reversión. Tecnología, CISO y Logística aprueban el patrón por release; Operaciones acepta cada sitio mediante referentes delegados. Cambios de patrón, fallas o riesgos críticos vuelven a los especialistas; CISO mantiene su autoridad de bloqueo. Un sitio pendiente permanece cerrado al nuevo flujo y fuera del conteo de altas. La delegación consume dedicación a incluir en E11, no una reunión de todos los aprobadores por tienda.

La capacidad de habilitar tiendas no demuestra capacidad para operarlas a diario. Antes de cada alta se propone contrastar, por turno, pedidos previstos y dedicación activa por pedido, más formación/excepciones/soporte, contra horas disponibles después del trabajo habitual. Las 7,2 h de preparación del caso y la meta <3 h miden tiempo del flujo; no se convierten automáticamente en horas de mano de obra. Confirmar dotación, reemplazos y costo con Tiendas/Operaciones en COST-06 o aporte interno declarado, sin asumir sobretiempo gratuito ni duplicar E11. Si no cabe la operación, ajustar proceso, dotación o cobertura antes de aceptar el sitio.

La apertura incluye acompañamiento intensivo con relevo local/remoto. La base supone 0,5 persona-día efectivo por alta: 29 adicionales a los 116 de habilitación, total **145 frente a 150** disponibles en cuatro células durante 25 jornadas equivalentes. Se distribuyen dentro de treinta días de olas más diez de preparación/VE-01. La dedicación bruta de células 200 más treinta de preparación suma 230: E11/R2 aporta 210 y COST-06 veinte de campo. La carga de desarrollo R2 permanece 23/24.

La [base de ejecución](../registros/base_ejecucion.md) asigna dentro de COST-06 2,1538 MM al campo y diez MM de bolsa de traslados, conservando treinta persona-días de preparación. El referente local acepta el relevo antes de liberar la célula al siguiente sitio. Operación diaria, conteos y dispositivos se concilian con las partidas y dedicaciones existentes; si no caben, reestimar antes de abrir. Los parámetros sustentan una meta condicionada, no disponibilidad observada.

La aceptación del release reúne sitios, funciones y calidad, además de las métricas de uso/mejora que correspondan. G1 requiere evidencia de valor según 01/SUP-16; VE-01 exige preparación de campaña. Al cierre M12, sponsor y Operaciones reciben capacidades aceptadas, documentación, soporte, pendientes y responsables de beneficios, con resultados y brechas visibles. La entrega de software no reemplaza esas condiciones.

La definición de terminado (DoD) propuesta exige criterio funcional, pruebas necesarias, controles, telemetría, documentación, soporte, reversión y aceptación operacional. Antes de abrir R1 se acuerdan los criterios de medición de SUP-16; la mejora se evalúa con uso real hasta G1. Cada ola repite la aceptación de datos, proceso, formación, soporte y controles. El experimento CAP-09 requiere su propia hipótesis y límite, no una historia abierta de logística sin costo.

Ejemplo de distinción: aceptar CAP-04 exige que un pedido reservable pueda prepararse y retirarse con estados/permiso correctos y que se mida su uso; la DoD exige además pruebas, revisión de seguridad, telemetría, documentación y reversión. Cumplir la función sin esa calidad no habilita liberar; cumplir DoD sin uso/mejora no acredita beneficio.

## Operación y soporte del servicio

El servicio necesita un equipo que lo opere durante el proyecto y después del mes 12. Esta función concreta CAP-06 y PAQ-07: un dueño del servicio en Tecnología y tres niveles de soporte con responsables y escalamiento explícitos.

| Nivel | Quién lo presta | Qué atiende | Con qué crece |
| --- | --- | --- | --- |
| Primer nivel, tiendas | Referente local por turno en cada tienda habilitada y mesa de ayuda corporativa con guiones de ZEUS | Uso de la app, estados de pedido, retiro y excepciones simples | Tiendas activas, turnos y pedidos diarios |
| Segundo nivel, aplicación | Analistas funcionales de los equipos de producto y soporte del partner OMS | Fallas de flujo, datos, conciliación y configuración | Volumen de incidentes y servicios integrados |
| Tercer nivel, plataforma | Guardia rotativa de los equipos de desarrollo, apoyada en la observabilidad de E8a y E8b | Disponibilidad, integraciones, eventos y recuperación | Servicios críticos y horario de operación; se refuerza en campaña |

El primer nivel crece con el número de tiendas. El segundo y el tercero crecen con los servicios críticos y su exigencia de disponibilidad, por eso no se multiplican por tienda. Durante el proyecto, los equipos que construyen cada servicio también lo operan.

Para dimensionar el primer nivel se propone la regla: agentes de mesa por turno = tiendas activas × incidentes por tienda y turno × minutos por incidente / minutos disponibles por agente y turno. Los parámetros se miden en el piloto, entre las semanas 17 y 20, y se recalculan antes de cada ola. Si el resultado excede la capacidad de la mesa existente, el refuerzo es un costo incremental que G1 debe autorizar (SUP-26, R-17).

La operación participa en la definición de terminado de cada salida: procedimientos operativos, alertas con responsable, reversión probada y guion de atención antes de abrir cada sitio. El soporte registra incidentes y problemas recurrentes, que alimentan el backlog de mejoras con su análisis de causa. Al cierre del mes 12, el servicio pasa a un equipo estable de operación y producto, con dueño, acuerdos de nivel de servicio y presupuesto recurrente fuera del proyecto, considerado en el horizonte económico del Business Case.

## Cambios y acuerdos pendientes

Maverick integra este documento y los cuatro integrantes revisan inclusiones, exclusiones y diferimientos antes de cerrar la propuesta. Si el diagnóstico o la evaluación de alternativas cambia esa frontera, actualizar también Business Case, Charter, priorización, estimación y roadmap; no limitar la corrección a una lista de backlog.

El [plan de apoyo](../registros/plan_alcance_roadmap.md) distribuye el esfuerzo por épica y dimensiona cuatro células con 210 persona-días de E11 y veinte adicionales de campo en COST-06. La ratificación del alcance y la revisión de especialidades, costos y contratos siguen pendientes. PO ordena dentro de límites; PM integra impacto; sponsor/comité acepta cambios de cobertura comprometida, costo, fecha o beneficio. CISO y Operaciones deciden sobre exposición crítica y operabilidad. Actualizar estimación y roadmap al cambiar alcance.
