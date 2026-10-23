# 2. Selección y tailoring del enfoque

**ESC-02, propuesta para revisión del equipo. Actualización: 23-10-2026.** El enfoque combina gobierno formal y entrega adaptativa. Las prácticas, dedicaciones y cadencias descritas se proponen para ZEUS; todavía no se han ejecutado. La [revisión de integración](../registros/integracion_avance_equipo.md), INT-05/10/11/12, conserva los fundamentos.

## 2.1 Enfoque propuesto

Recomendamos un enfoque híbrido para coordinar compromisos de inversión, contratos y continuidad con el aprendizaje sobre integración, experiencia y adopción. El gobierno formal define límites y autoridad; la entrega adaptativa prueba soluciones y actualiza la previsión. La elección responde a esas necesidades de ZEUS, sin suponer que otros enfoques carecen de planificación o control.

## 2.2 Fundamentación

ERP, conciliación, seguridad, contratos y preparación comercial requieren trazabilidad, acuerdos y control de cambios. Esos compromisos pueden ser estables sin que la solución técnica sea conocida. Las APIs y datos legacy conservan incertidumbre que debe probarse temprano. La restricción de no reemplazar ERP no reduce por sí sola esa incertidumbre.

La experiencia C&C, devolución, aplicación de tienda y adopción requieren validación temprana y ajuste. El rol logístico de las tiendas y Ship-from-store necesita un experimento con límites y criterios de aprendizaje. La capacidad y madurez ágiles desiguales del caso (p. 5) condicionan cuántos equipos pueden sostener estas prácticas.

La comparación siguiente aplica las tres lógicas al contexto del enunciado (pp. 3, 5 y 7). Es una evaluación de la propuesta, sin resultados empresariales observados.

| Lógica | Aporte posible a ZEUS | Condición o tensión que debe resolver |
| --- | --- | --- |
| Predictiva predominante | Definir interfaces, contratos, aceptación y preparación comercial con una secuencia controlada | Si se aplaza la validación técnica o de usuarios hasta etapas tardías, aumenta la exposición al retrabajo. Requiere pruebas tempranas ante incertidumbre. |
| Ágil predominante | Validar incrementos de C&C, integración y adopción, ajustando el backlog con feedback | Debe coordinar contratos, dependencias entre sistemas y autorizaciones de inversión/operación; la autonomía del equipo no sustituye esas decisiones. |
| Híbrida, recomendada | Integrar controles ejecutivos y contractuales con pruebas técnicas, flujo e incrementos de producto | Exige un mismo roadmap y reglas de decisión; dos planes desconectados o controles duplicados harían perder su ventaja. |

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

El calendario de 06/07 propone equipos de unas seis personas: cinco en sprints 1–4, seis en 5–15 y cuatro desde 16; el sexto arranca en el 5 y entrega desde el 6, antes de campaña. Debe confirmarse que esa reducción permita sostener soporte y continuidad. Son equipos empresariales distintos de los cuatro integrantes académicos, sin disponibilidad/productividad comprobadas. La estimación relativa no sustituye carga por especialidad ni convierte equipos heterogéneos en capacidad perfectamente intercambiable.

## 2.7 Puente de artefactos y autoridad

El Charter define mandato y autoridad. La estructura de desglose del trabajo (EDT) organiza los paquetes PAQ para estimar y controlar el alcance; el backlog prioriza capacidades CAP e historias. El roadmap relaciona R0/R1/R2/R3 con dependencias, evidencia y decisiones de inversión. Los registros conservan supuestos y cambios. PO ordena trabajo dentro de límites; PM integra; comité/sponsor decide inversión y cambios mayores; CISO puede bloquear exposición crítica y Operaciones una salida no operable. La DoD incluye pruebas, controles, telemetría, documentación y soporte, pero el beneficio se evalúa con uso y métricas por gate.

## 2.8 Actualización de un mismo plan

La clase 3 pide conectar gobierno, puente y entrega (sesión 03, p. 15; sesión 04, p. 20; [aplicación](../registros/aportes_clase_03.md)). En la revisión semanal, PO y equipos presentan terminados, bloqueos, evidencia y trabajo próximo; PM/Arquitectura actualizan dependencias y forecast del roadmap. Si cambia costo, cobertura, fecha o beneficio comprometido, PM eleva impacto al sponsor/comité antes de modificar la referencia aprobada. La decisión vuelve al backlog y a los documentos afectados. No mantener una fecha ejecutiva inalterada mientras el equipo ya pronostica otra.

Para APIs/integración, proponer políticas Kanban explícitas: entrada con interfaz/dueño y aceptación definidos; límites WIP acordados según capacidad por especialidad; bloqueos visibles con responsable; priorizar terminar o desbloquear antes de abrir más trabajo. Medir terminados, tiempo de ciclo y antigüedad/bloqueos según 07. Los límites numéricos deben justificarse con SUP-02, no copiarse del tablero de ejemplo (sesión 06, pp. 11 a 17).

A partir del tratamiento de cuellos de la clase 4 ([parte 2](../transcripciones/clase-04_parte-2.md), 2:13:45 a 2:17:12), se propone esta regla para ZEUS: si un bloqueo crítico impide avanzar el flujo, el responsable de integración y PO frenan nuevos inicios que alimenten ese cuello y priorizan desbloquear/terminar. El ítem bloqueado sigue contando como WIP; PM coordina al dueño externo y escala si amenaza un hito. Revisar bloqueos cada día y consolidar su impacto en el foro semanal; otras especialidades continúan solo con capacidad disponible y sin aumentar la cola bloqueada.

## 2.9 Adopción de las prácticas

La adopción parte de la madurez desigual descrita en el caso. En R0 se propone revisar experiencia, disponibilidad de PO/tiendas y capacidad de los equipos, sin suponer que todos parten del mismo nivel. Acordar una forma inicial de trabajar: entrada al backlog, criterios de aceptación y DoD, responsables de decisión, límites WIP y tratamiento de bloqueos. Usar trabajo real del primer flujo para practicarla y ajustarla.

Asignar una función de facilitación para acompañar a los equipos y remover impedimentos; no asumir una contratación adicional ni convertirla en jefatura de tareas. Confirmar quién la realiza y con qué dedicación. PO y representantes de tienda deben disponer de tiempo para decidir y revisar, además de asistir a reuniones.

En las primeras iteraciones, revisar terminados, tiempos de espera, bloqueos y utilidad del feedback. Ajustar prácticas según esa evidencia; contar ceremonias o mantener ocupación alta no demuestra mejora. Formación, facilitación y participación consumen capacidad: conciliarlas con los 840 MM de equipos y las fronteras de COST-06/COST-07 en 06, sin sumar otro cargo automáticamente. Esta adopción propuesta sigue pendiente de revisión del equipo.

## 2.10 Controles proporcionales y autonomía

La tensión entre estándares y autonomía se gestiona con límites explícitos y evidencia compartida. PO y equipos deciden orden, detalle y solución dentro del mandato y los estándares; una misma evidencia de DoD, interfaz o seguridad sirve a la revisión de salida correspondiente. Arquitectura/CISO intervienen según riesgo, sin agregar por defecto un gate ejecutivo a cada historia. El foro semanal existente resuelve dependencias; un bloqueo crítico se escala sin esperar esa reunión. Si las esperas por aprobación deterioran el flujo, revisar el mecanismo y mantener el control necesario, no duplicarlo.

El proveedor WMS conserva su lógica contractual/tradicional: acordar entregas, interfaces y ventanas de prueba que permitan integrar incrementos internos, sin asumir que adoptará Scrum. Para cloud, Tecnología/Arquitectura comparan servicios administrados con las opciones existentes por necesidad, escalabilidad, continuidad, seguridad y costo total; la preferencia del proveedor no autoriza ampliar arquitectura o presupuesto. Estas reglas responden a los intereses y tensiones de las pp. 6/7, detallados en la [matriz de stakeholders](../registros/matriz_stakeholders.md).

## 2.11 Aprendizaje temprano sobre operación y promesa

La [evidencia complementaria](../insumos/evidencia_logistica_y_valor.md) orienta una hipótesis conjunta de producto y logística. En las primeras iteraciones se propone probar reserva, disponibilidad WMS y preparación con usuarios operativos, medir y decidir mantener, corregir o descartar una solución. Un MVP debe completar un flujo acotado con controles y reversión; una demostración o una etiqueta comercial no prueban beneficio.

Se mantienen los sprints propuestos y el gobierno híbrido por las dependencias, contratos, financiación y continuidad de ZEUS. El aprendizaje no exige esperar al gate financiero para corregir una historia dentro del mandato. La velocidad de experimentación protege stock, datos y operación; no se atribuye esta forma de trabajo como política verificada de otra empresa. Logística/Tiendas participan en aceptación y feedback, con dedicación estimada y separada de desarrollo.
