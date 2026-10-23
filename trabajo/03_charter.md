# 3. Project Charter

**ZEUS: Plataforma Omnicanal Modular. ESC-02, propuesta para revisión del equipo. Actualización: 23-10-2026.** Este Charter propone el mandato y las condiciones de autorización; no registra una aprobación empresarial. La [revisión de integración](../registros/integracion_avance_equipo.md) identifica correcciones y decisiones pendientes.

## Propósito y contribución

Construir una plataforma que integre inventario, pedidos, tiendas y devoluciones mediante servicios reutilizables, para ofrecer una experiencia omnicanal consistente y reducir complejidad de integración. Sponsor: **Gerente General**.

Se espera que contribuya a las metas estratégicas de 35% de ventas digitales, NPS ≥+48, puntualidad ≥95% y abandono de carro <55%. No se garantiza atribución íntegra a ZEUS. La creación de tecnología debe traducirse en uso, beneficio y valor.

## Objetivos medibles del equipo, con horizonte propuesto

| ID | Objetivo del proyecto | Horizonte/cobertura propuestos | Referencia |
| --- | --- | --- | --- |
| KPI-01 | Cancelaciones por stock <2%; referencia corporativa actual: 7,8% | M12, operación cubierta; validar base comparable | Meta estratégica p. 4; objetivo del equipo. |
| KPI-02 | Actualización web de 45 a 120 min a <2 min | M12, interfaces cubiertas | Meta del caso; precisión de método en 01. |
| KPI-03 | Preparación media <3 h; referencia corporativa actual: 7,2 h | M12, separar flujos de retiro/despacho | Meta del caso; validar base por cohorte. |
| KPI-04 | Resolución al primer contacto ≥85% en casos elegibles; referencia corporativa actual: 64% | M12, casos elegibles del alcance | Objetivo propuesto del equipo; meta estratégica ≥90%, diferencia nominal de 5 pp entre metas con poblaciones distintas. |
| KPI-05 | Servicios ZEUS críticos ≥99,9%; seguimiento del e-commerce extremo a extremo | Campaña M8 y ventanas regulares; meta corporativa e-commerce ≥99,9% se conserva | Delimitación propuesta: ZEUS controla sus servicios y gestiona dependencias con operación del canal. |
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
| R1, hasta M5 | Piloto C&C en 10 tiendas, 1 CD y 2 familias de productos, con primera salida al finalizar la semana 16, durante M4, y evaluación hasta M5 | Sitios, volumen, métricas y operación aceptados; número 10 es supuesto. |
| R2, hasta M7 | Objetivo C&C en las 68 tiendas, listo para campaña M8 | Ampliar 58 tiendas en olas, hasta 3 CD y las mismas 2 familias, solo si capacidad, costo y operación lo sostienen. El caso no exige esa fecha de cobertura. |
| R3, hasta M12 | Devoluciones, ampliación de observabilidad y piloto Ship-from-store | Gate M9: experimento de 3 a 5 tiendas; propuesta de Maverick de máximo cuatro semanas/300 pedidos, con techo monetario de exposición y costo autorizados antes de iniciar. No posponer toda observabilidad a R3. |

La cobertura 68/M7 es una meta de expansión condicionada. G1 fija la cobertura previa a campaña con capacidad, CD, costo y acompañamiento conciliados. Ese número pasa a ser compromiso cuando se autoriza; sus cambios actualizan beneficios, financiación y fechas. La [base de ejecución](../registros/base_ejecucion.md) aporta un mecanismo de cuatro células con acompañamiento y preparación, sujeto a recursos/costo/aceptación por sitio.

## Roles y derechos de decisión

| Rol | Responsabilidad / derecho |
| --- | --- |
| Comité Ejecutivo | Gates, financiación y aceptación de cambios de la referencia aprobada que afecten inversión/beneficio. |
| Sponsor Gerente General | Propósito, prioridades y cambios de fecha/alcance mayor dentro de límites; escalar los que alteran condiciones del caso. |
| Gerente Comercial | Resultados de conversión, ventas y experiencia; revisar con PO el valor y costo de oportunidad sin desplazar controles/habilitadores indispensables. |
| PM de ZEUS | Coordinar frentes, dependencias, riesgos, cambios y forecast. ZEUS se trata aquí como proyecto con frentes; no se presupone un programa formal sin definirlo. |
| PO e-commerce y función PO/representante de tiendas | Priorizar backlog por release dentro de objetivos y límites acordados. El rol adicional de tiendas es propuesta organizacional. |
| Gerente de Tecnología | Integración y modernización compatibles con continuidad; coordinar viabilidad y operación técnica. |
| Arquitectura Empresarial | Estándares y desacoplamiento; justificar decisiones y controles sin duplicar evidencia o crear gates por defecto para cada historia. |
| CISO | Controles y facultad de detener release ante riesgo crítico. |
| Logística / Operaciones / gerencias de tienda | Beneficios, dotación, capacidad y aceptación operacional; pueden impedir una salida no operable. |
| Finanzas | Costo total, forecast, reservas y liberación financiera con comité. |
| Proveedores WMS, OMS y cloud | Compromisos, integración, licencias y soporte según contrato. OMS comprado es supuesto del equipo. |

Los trece stakeholders de las pp. 6/7 del enunciado están trazados en la [matriz de intereses, tensiones y respuesta](../registros/matriz_stakeholders.md). Comercial y equipos de desarrollo son interesados oficiales del caso; clientes y usuarios operativos se añaden como participantes de validación de necesidad/uso. Los equipos empresariales propuestos son distintos de los cuatro integrantes académicos.

La sesión 03, p. 11, pide mostrar decisiones y dependencias además de listar interesados. Se proponen las siguientes reglas para resolver tensiones; la matriz enlazada conserva los trece intereses, su respuesta y la evidencia pendiente, sin atribuir aprobaciones reales:

| Intereses en tensión | Regla propuesta | Autoridad y evidencia |
| --- | --- | --- |
| Velocidad del sponsor frente a estabilidad/seguridad | Revisar funcionalidad, cobertura o fecha antes de omitir condiciones de salida | PM presenta opciones; CISO/Operaciones pueden impedir salida crítica/no operable; sponsor/comité decide compromisos compatibles con restricciones. |
| Funcionalidad comercial frente a integración/deuda técnica | Proteger habilitadores imprescindibles y controles; priorizar opcionales por valor y capacidad | Comercial/PO/Tecnología revisan evidencia y dependencias de 05; comité acepta cambios mayores. |
| Autonomía PO/desarrollo frente a estándares y controles | Decidir detalle dentro de límites y reutilizar la evidencia de calidad; no elevar cada historia al comité | PO/equipos con Arquitectura/CISO según riesgo; foro de 02 resuelve bloqueos y PM escala impactos mayores. |
| Escalabilidad cloud frente a inversión/continuidad | Justificar cloud selectivo por necesidad y costo total; el proveedor no determina el alcance | Tecnología/Arquitectura proponen; Finanzas/CISO/Operaciones revisan; autoridad de cambio según impacto. |
| Expansión comercial frente a capacidad de tiendas/WMS | Aceptar cada sitio con turnos, stock, formación, interfaces y soporte; calibrar ritmo antes de escalar | Operaciones/Tiendas/Logística y proveedor presentan evidencia; G1/olas revisan forecast y PM escala cambios. |

Si cambia un objetivo, límite o financiación, actualizar este Charter y comunicar a los interesados afectados; no dejar el cambio solo en una reunión (clase 3, parte 2, 55:53 a 57:57). El detalle operativo permanece en 04 a 07.

## Restricciones, supuestos y riesgos

Techo máximo preliminar **1.500 MM CLP**, horizonte 12 meses, valor dentro de los primeros cinco meses, Black Friday aproximadamente M8; ERP no reemplazado, WMS solo modificado, continuidad y controles obligatorios (enunciado p. 5).

Supuestos: APIs/eventos útiles del ERP, cumplimiento del proveedor WMS, OMS de mercado, dotación escalonada 5/6/4, diez tiendas piloto, escalamiento a 68, evidencia a M5 y recursos para el experimento. Todos requieren validación académica de coherencia y validación empresarial hipotética descrita en el [registro](../registros/acuerdos_y_supuestos.md).

Riesgos: exactitud de stock insuficiente (91% corporativo como condición base), retrasos de WMS, capacidad de tiendas/equipos, campaña, sobrecosto y bloqueo por seguridad. La inexactitud puede generar reservas sin existencias y afectar promesas, cancelaciones y adopción. [Registro de riesgos](../registros/riesgos.md).

## Presupuesto y financiación

Presupuesto preliminar propuesto: **1.330 MM CLP + 170 MM de contingencia = 1.500 MM**, sin exceder nominalmente el techo. Referencia B del caso: 1.350 MM. Sensibilidad de categorías revisada 1.215 a 1.668 al añadir estrés +20% en equipos; el extremo bruto excede el techo en 168. La respuesta propuesta de reducción/topes lo lleva a 1.497,0923 si se obtienen esas condiciones contractuales; si fallan, revisar cobertura/alternativa antes de comprometer gasto. No existen cotizaciones o históricos verificados detrás de esos montos.

Propuesta de financiación: **675 MM en G0/M1** para R0/R1, 345 en G1/M5 para R2/campaña y 310 en G2/M9 para R3; reserva 170 gestionada por comité. La [estimación 06](06_estimacion.md) documenta 104 equipo-sprints y capacidad propuesta 120, así como la conciliación pendiente de calendario/roles, costos que podrían duplicarse y cuotas por categoría. El marco preliminar no acredita financiación ya aprobada ni confianza garantizada de fecha.

## Hitos y criterios de salida

| Hito | Condición de salida propuesta |
| --- | --- |
| G0/M1 | Arquitectura inicial, financiación y selección/contratación OMS por hitos, con validación técnica condicionada. |
| VT-01/M2 | Viabilidad de interfaces, datos y recuperación antes de exponer el piloto. |
| G1/M5 | Evidencia de primera entrega de valor y decisión de ampliar con capacidad/costo revisados. |
| VE-01/M7 | R2 aceptado, cobertura segura y preparación de campaña; iniciar congelamiento propuesto con soporte activo. |
| Campaña/M8 | Proteger continuidad y promesas; confirmar fecha externa. Excepciones críticas controladas según [07](07_roadmap.md). |
| G2/M9 | Beneficios y previsión actualizados, con autorización de financiación y condiciones de R3. |
| Cierre/M12 | Aceptación y transferencia, con responsables de beneficios pendientes. |

Éxito propuesto: objetivos medidos, adopción >80%, ejecución dentro del costo autorizado compatible con techo, riesgos críticos de seguridad tratados y campaña operable. «Sin interrupciones» es objetivo de continuidad, no garantía anticipada de resultado. Para aprobación de release exigir pruebas y soporte, además de medir disponibilidad con ventana definida.

## Precisiones pendientes para cerrar el mandato

Se da prioridad a la [revisión del avance del 23](../registros/revision_avance_2026-10-23.md): WSJF, nueva base de esfuerzo/costo y experimento de 3 a 5 tiendas. La propuesta desarrollada de Maverick concreta 1 CD/2 familias piloto, hasta tres CD para las mismas familias en expansión, calendario y matriz por épica en 04/07. Los umbrales SUP-16 se mantienen como hipótesis académica; el grupo debe ratificarlos y Rogelio contrastar dedicaciones/costos; la geografía 68 tiendas no define por sí sola todo el catálogo ni costo.

Las devoluciones ≥85% en casos elegibles siguen siendo objetivo M12. Si se difieren E9 o integraciones necesarias, revisar este Charter y los beneficios; no afirmar que todo R3 puede recortarse sin impacto. La observabilidad básica y controles se mantienen desde R1 aunque se difiera centralización adicional.

## Solicitud de autorización

Se solicita al Comité un primer tramo de **675 MM CLP**, con financiación total por etapas y contingencia del marco 1.500. Condicionar compromiso irreversible a evidencia técnica, operación y contratos por hitos; VT-01/M2 y G1/M5 revisan viabilidad y valor. Antes de presentar como solicitud cerrada, conciliar calendario de equipos, flujo financiero y frontera de costos. No simular una autorización empresarial ya obtenida.
