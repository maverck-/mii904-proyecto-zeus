# Acuerdos y supuestos

**ESC-02, 21 de octubre de 2026: integración priorizando el avance del equipo.** La integración es una propuesta para revisar; no acredita aprobación colectiva ni pruebas empresariales. El escenario previo ESC-01 queda en el historial de Git y no sostiene los costos ni la cobertura actuales.

## Hechos y decisiones

Enunciado: 68 tiendas y 3 CD (p. 3); cancelación por stock 7,8%, exactitud 91%, preparación 7,2 h y devolución al primer contacto 64% (p. 4); máximo preliminar 1.500 MM CLP, 12 meses, valor dentro de primeros 5, campaña aproximadamente M8, ERP sin reemplazo, WMS sin reemplazo completo, continuidad y controles (p. 5); B = 1.350 MM y 9 a 12 meses (p. 7). La empresa es ficticia. Estos antecedentes no demuestran que 68 tiendas estén operables en M7.

| ID | Decisión / propuesta | Estado y revisión |
| --- | --- | --- |
| DEC-01 | B modular como base revisable | Retiene la orientación del equipo; cambiar si integración, costo o valor no la sostienen. |
| DEC-02 | Dar prioridad al avance recibido para 01/02/03 y alinear 04 a 07 | Instrucción de integración del usuario; ajustes sujetos a revisión grupal. |
| DEC-03 | Inventario, pedidos y C&C primero; controles, medición y soporte desde inicio | Propuesta integrada, sin aceptación operacional realizada. |
| DEC-04 | Gobierno formal y entrega adaptativa; Kanban y Scrum de dos semanas | Base del equipo; disponibilidad y prácticas por validar. |
| DEC-05 | Piloto 10/M5, objetivo 68/M7, devolución y experimento acotado Ship-from-store/R3 | Base del equipo condicionada a costo/capacidad/evidencia. |
| DEC-06 | IA y data platform completa fuera; Ship-from-store condicionado a G2/M9 | Sustituye exclusión completa de Ship-from-store del escenario anterior. |
| DEC-07 | Rogelio: priorización/estimación; Maverick: alcance/roadmap | Asignación comunicada por Maverick; revisión transversal de los otros contenidos. |

## Supuestos pendientes de validación

Revisión académica: comprobar razonabilidad, coherencia y defensa con el caso. Validación empresarial: trabajo futuro hipotético, sin APIs probadas, cotizaciones ni aprobaciones reales. No confundir ambos niveles.

| ID | Supuesto de ESC-02 | Revisión académica | Validación empresarial hipotética / momento | Si falla |
| --- | --- | --- | --- | --- |
| SUP-01 | ERP/WMS permiten integración acotada por APIs y, donde sea viable, eventos | Defender interfaces y opciones sin suponer solución conocida | Tecnología/proveedores prueban consistencia, carga, recuperación y contratos en VT-01/M2 | Revisar arquitectura, plazo, alcance y B. |
| SUP-02 | Cinco equipos de implementación y funciones de negocio/tienda pueden sostener la secuencia | Estimar tamaños, dedicaciones, especialidades y concurrencia en 06; no equivalen a cuatro alumnos | Sponsor/Operaciones confirman dotación antes de comprometer R1/olas | Limitar WIP, cobertura o secuencia y reestimar. |
| SUP-03 | Hay datos comparables y volumen para evaluar unas cuatro semanas de piloto | Definir cohortes, denominadores y sesgos en 01 | Dueños de beneficio fijan base y suficiencia de evidencia antes del piloto | No declarar valor demostrado con evidencia insuficiente. |
| SUP-04 | Flujo usable desde M4 y evidencia de valor hasta G1/M5 | Revisar precedencias y ventana; plazo total de B no prueba primera entrega | PM/Operaciones comprueban uso y KPI en G1 | Revisar inversión y declarar si requisito de valor no se cumple. |
| SUP-05 | Diez tiendas piloto y expansión a 68 en M7 son operables; cuatro olas adicionales de 15/15/14/14 como propuesta de integración | Justificar 58 altas en dos meses, selección de sitios y capacidad; cobertura CD/familias por definir | Operaciones autoriza cada ola y dependencias de CD antes de exponer clientes | Mantener solo cobertura segura y modificar compromiso explícitamente. |
| SUP-06 | Objetivos del Charter son alcanzables en cobertura acordada: devolución ≥85% a M12 y adopción >80%, entre otros | Justificar brecha frente al ≥90% estratégico y umbrales de mejora para M5 | Negocio ratifica base, metas y ventanas antes de piloto; medición por release | Ajustar objetivo/cobertura/recursos sin confundirlo con cumplimiento estratégico. |
| SUP-07 | B puede concretarse bajo techo con OMS, 10/68 tiendas y R3 | Rogelio debe reconstruir rangos por PAQ; montos previos no se trasladan | Finanzas/proveedores contrastan costos y contratos por etapas | Revisar cobertura, experimento, alternativa o financiación; no ocultar exceso. |
| SUP-08 | Financiación por tramos y reserva por definir sostienen G0/M1, G1/M5, G2/M9 | Cuantificar primer tramo, reserva y autorización antes de cerrar Charter | Comité/Finanzas aprueban liberaciones y forecast | No comprometer gasto sin tramo/costo aceptados. |
| SUP-09 | Pesos y notas ilustrativas de 05 ayudan a ordenar el trabajo | Rogelio revisa C/K para 68 tiendas y puntúa CAP-09 si procede | PO/comité revisan con evidencia | Reordenar manteniendo precedencias/controles. |
| SUP-10 | Se puede calcular costo total de 12 meses sin doble conteo | Incluir interno/externo, adopción, licencias, consumo, transición, impuestos y experimento; declarar TCO posterior | Finanzas valida fronteras e indexación antes de escala | Rehacer costo y beneficio antes de contratar. |
| SUP-11 | Controles, observabilidad, soporte y disponibilidad pueden aceptarse desde R1 | Acordar ventana ≥99,9%, pruebas y autoridad; el porcentaje no habilita interrupciones | CISO/Tecnología/Operaciones aceptan cada salida y VE-01/M7 | Bloquear liberación no operable y corregir. |
| SUP-12 | Un OMS de mercado cubre el flujo con configuración y adaptaciones acotadas | Comparar compra/configuración e interfaces; proveedor no elegido | Selección G0/M1 con aceptación escalonada y prueba VT-01/M2 | Revisar contrato/arquitectura antes de compromisos irreversibles. |
| SUP-13 | Un experimento Ship-from-store cabe en R3 sin poner en riesgo metas/techo | Definir hipótesis, tiendas, pedidos, esfuerzo y límite monetario antes de G2 | Operaciones/Finanzas autorizan experimento M9 y evalúan resultados antes de cierre | Diferir experimento con impacto explícito; no quitar controles. |

## Incorporación de clase 3

Se incorporan [aportes docentes trazables](aportes_clase_03.md) a problema, interesados, alcance, aceptación/DoD, dependencias, actualización del plan y técnicas de estimación/flujo. La clase admite formular con supuestos numéricos explícitos; no valida para ZEUS las cantidades de los ejercicios ni convierte 10/68 en compromiso aprobado. Se mantienen SUP-01 a SUP-13 y responsables. No se modifica automáticamente cobertura ni se sustituye el avance del equipo.

## Control de cambios

| Fecha | Actualización | Estado |
| --- | --- | --- |
| 20-10-2026 | ESC-01: escenario anterior con otra cobertura, costos y exclusiones | Sustituido como propuesta vigente; conservado en Git. |
| 21-10-2026 | ESC-02: avance recibido como base principal, correcciones documentadas y reparto actualizado | Integrado para revisión; no presume consenso del grupo. |
| 21-10-2026 | Clase 3 y presentaciones 03 a 06 incorporadas; trazabilidad, dependencias y prácticas de estimación/flujo desarrolladas | Propuestas para revisión; no cambia objetivos ni acredita pruebas empresariales. |

Registrar decisiones efectivamente aceptadas, motivo, evidencia y documentos afectados. La [revisión de integración](integracion_avance_equipo.md) conserva los fundamentos de cada ajuste.
