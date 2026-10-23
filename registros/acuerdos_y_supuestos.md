# Acuerdos y supuestos

**ESC-02, revisión 23 de octubre de 2026: integración priorizando el avance del equipo.** La integración es una propuesta para revisar; no acredita aprobación colectiva ni pruebas empresariales. El escenario previo ESC-01 queda en el historial de Git y no sostiene los costos ni la cobertura actuales.

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
| DEC-08 | Desarrollar escenario provisional con las sugerencias: CD/familias, capacidad, umbrales M5 y experimento | Maverick autorizó avanzar el 22-10; no equivale a aprobación colectiva ni financiación empresarial. |
| DEC-09 | Priorizar actualización del equipo del 23: WSJF, 104 equipo-sprints, presupuesto 1.330 + 170 y experimento 3–5 tiendas | Integrado con revisión aritmética y limitaciones; no acredita acuerdos empresariales ni corrige por inferencia calendario/carga faltantes. |

## Supuestos pendientes de validación

Revisión académica: comprobar razonabilidad, coherencia y defensa con el caso. Validación empresarial: trabajo futuro hipotético, sin APIs probadas, cotizaciones ni aprobaciones reales. No confundir ambos niveles.

| ID | Supuesto de ESC-02 | Revisión académica | Validación empresarial hipotética / momento | Si falla |
| --- | --- | --- | --- | --- |
| SUP-01 | ERP/WMS permiten integración acotada por APIs y, donde sea viable, eventos | Defender interfaces y opciones sin suponer solución conocida | Tecnología/proveedores prueban consistencia, carga, recuperación y contratos en VT-01/M2 | Revisar arquitectura, plazo, alcance y B. |
| SUP-02 | Cinco equipos promedio de unas seis personas, sexto de apoyo previo a campaña y cuatro en tramo posterior pueden sostener secuencia | Estimar tamaños, dedicaciones, especialidades y concurrencia en 06; no equivalen a cuatro alumnos | Sponsor/Operaciones confirman dotación antes de comprometer R1/olas | Limitar WIP, cobertura o secuencia y reestimar. |
| SUP-03 | Hay datos comparables y volumen para evaluar unas cuatro semanas de piloto | Definir cohortes, denominadores y sesgos en 01 | Dueños de beneficio fijan base y suficiencia de evidencia antes del piloto | No declarar valor demostrado con evidencia insuficiente. |
| SUP-04 | Flujo usable desde M4 y evidencia de valor hasta G1/M5 | Revisar precedencias y ventana; plazo total de B no prueba primera entrega | PM/Operaciones comprueban uso y KPI en G1 | Revisar inversión y declarar si requisito de valor no se cumple. |
| SUP-05 | Diez tiendas piloto y expansión a 68 en M7 son operables; cuatro olas adicionales de 15/15/14/14 como propuesta de integración | Justificar 58 altas en dos meses, selección de sitios y capacidad; catálogo/CD de SUP-14 por ratificar; capacidad vigente a conciliar en SUP-18, sin sumar brigadas de SUP-15 | Operaciones autoriza cada ola y dependencias de CD antes de exponer clientes | Mantener solo cobertura segura y modificar compromiso explícitamente. |
| SUP-06 | Objetivos del Charter son alcanzables en cobertura acordada: devolución ≥85% a M12 y adopción >80%, entre otros | Justificar brecha frente al ≥90% estratégico y umbrales de mejora para M5 | Negocio ratifica base, metas y ventanas antes de piloto; medición por release | Ajustar objetivo/cobertura/recursos sin confundirlo con cumplimiento estratégico. |
| SUP-07 | Presupuesto recibido 1.330 MM de base y 170 de reserva puede cubrir alcance OMS, 10/68 tiendas y R3 | Rogelio/equipo concilian calendario, fronteras de costo e imputación a PAQ; cifras recibidas son supuestos, no cotizaciones | Finanzas/proveedores contrastan costos y contratos por etapas | Revisar cobertura, experimento, alternativa o financiación; no ocultar exceso. |
| SUP-08 | Financiación recibida 675/345/310 MM y reserva 170 sostienen G0/M1, G1/M5, G2/M9 | Verificar flujo por categoría/mes y condiciones; la suma ya está cuantificada, sin autorización real | Comité/Finanzas aprueban liberaciones y forecast | No comprometer gasto sin tramo/costo aceptados. |
| SUP-09 | WSJF y notas recibidas de 05 ayudan a ordenar épicas junto con dependencias/capacidad | Rogelio/equipo confirman escalas y regla de tamaño; el ranking anterior se retira como método vigente | PO/comité revisan con evidencia | Reordenar manteniendo precedencias/controles. |
| SUP-10 | Se puede calcular costo total de 12 meses sin doble conteo | Incluir interno/externo, adopción, licencias, consumo, transición, impuestos y experimento; declarar TCO posterior | Finanzas valida fronteras e indexación antes de escala | Rehacer costo y beneficio antes de contratar. |
| SUP-11 | Controles, observabilidad, soporte y disponibilidad pueden aceptarse desde R1 | Acordar ventana ≥99,9%, pruebas y autoridad; el porcentaje no habilita interrupciones | CISO/Tecnología/Operaciones aceptan cada salida y VE-01/M7 | Bloquear liberación no operable y corregir. |
| SUP-12 | Un OMS de mercado cubre el flujo con configuración y adaptaciones acotadas | Comparar compra/configuración e interfaces; proveedor no elegido | Selección G0/M1 con aceptación escalonada y prueba VT-01/M2 | Revisar contrato/arquitectura antes de compromisos irreversibles. |
| SUP-13 | Un experimento Ship-from-store cabe en R3 sin poner en riesgo metas/techo | Revisar límites SUP-17 y estimar esfuerzo/costo antes de G2 | Operaciones/Finanzas autorizan experimento M9 y evalúan resultados antes de cierre | Diferir experimento con impacto explícito; no quitar controles. |

## Precisiones para revisión del 22 de octubre

El [antecedente del 22](escenario_provisional.md) conserva cantidades y reglas previas. Al 23, SUP-15 queda como alternativa histórica y SUP-17 se actualiza con prioridad del nuevo aporte; SUP-14/SUP-16 requieren ratificación contra la estimación recibida.

| ID | Supuesto / propuesta nueva | Revisión y validación previstas | Si falla |
| --- | --- | --- | --- |
| SUP-14 | Piloto 10 tiendas/1 CD/2 familias; expansión 68 tiendas/hasta 3 CD con mismas familias; selección en M1 | Equipo revisa frontera; Operaciones/Logística valida sitios, catálogo elegible e interfaces en VT-01 | Ajustar selección/cobertura y actualizar costos/beneficios; no asumir que un CD cubre toda la red. |
| SUP-15 | Antecedente de habilitación del 22: cinco brigadas/dos días, no dotación vigente adicional | No imponerlo al plan 5/6/4 equipos; si se reutiliza, integrarlo a E11 y calendario sin sumar dos veces | Elegir otro mecanismo de habilitación y costearlo con aceptación de operación. |
| SUP-16 | Umbrales M5: −20% relativo en cancelación y −25% en preparación, adopción >80% por tienda, cuatro semanas y piso 1.000 pedidos/fase | Equipo/dueños de beneficio revisan razonabilidad; antes de abrir ratificar bases, denominadores y suficiencia. Piso no es garantía estadística | Si no comparable/suficiente, informar inconcluso; si no hay mejora o solo instalación, no declarar valor cumplido. |
| SUP-17 | Actualizado con avance del 23: experimento Ship-from-store en 3 a 5 tiendas; condiciones 2 tiendas/30 MM del 22 retiradas | Definir duración, pedidos, exposición y economía comparables antes de G2; E10 ya incluido en esfuerzo | Diferir/parar por riesgo, falta de economía evaluable o recursos; no prometer escala nacional. |

## Condiciones de la estimación recibida el 23

| ID | Supuesto a validar | Revisión requerida | Si falla |
| --- | --- | --- | --- |
| SUP-18 | Tabla 26 sprints/año y 24 efectivos con dotación escalonada representa 120 equipo-sprints y aproximadamente 60 equipo-meses | Un calendario de fechas, arranque/estabilización, dotación por periodo/rol y costo; 7 MM es asignación media por unidad efectiva, no tarifa exacta de dos semanas | Recalcular capacidad, carga y presupuesto; no afirmar confianza de fecha con suma de esfuerzo. |
| SUP-19 | Rangos de categorías 1.215/1.330/1.500 y reserva 170 no duplican equipos/proveedor ni omiten costos | Contrastar como supuestos; fronteras OMS/WMS/seguridad/rollout/gobierno, mensualización y PAQ; no hay cotizaciones o históricos verificados | Reestimar antes de comprometer, revisar reserva y alcance; extremo alto ya consume toda reserva. |

## Incorporación de clase 3

Se incorporan [aportes docentes trazables](aportes_clase_03.md) a problema, interesados, alcance, aceptación/DoD, dependencias, actualización del plan y técnicas de estimación/flujo. La clase admite formular con supuestos numéricos explícitos; no valida para ZEUS las cantidades de los ejercicios ni convierte 10/68 en compromiso aprobado. La incorporación docente mantuvo SUP-01 a SUP-13 y responsables; la revisión posterior del 22 agrega SUP-14 a SUP-17. No se modifica automáticamente cobertura ni se sustituye el avance del equipo.

## Control de cambios

Precisiones operativas propuestas para revisión: alcance integrado por Maverick y revisado por los cuatro; adopción de prácticas según madurez/capacidad en 02; alertas y respuesta desde R1; congelamiento desde aceptación R2/VE-01 hasta fin de campaña según 07. No modifican los totales recibidos el 23 ni acreditan aprobación colectiva. Su dedicación y costo deben conciliarse con SUP-02/SUP-18/SUP-19.

| Fecha | Actualización | Estado |
| --- | --- | --- |
| 20-10-2026 | ESC-01: escenario anterior con otra cobertura, costos y exclusiones | Sustituido como propuesta vigente; conservado en Git. |
| 21-10-2026 | ESC-02: avance recibido como base principal, correcciones documentadas y reparto actualizado | Integrado para revisión; no presume consenso del grupo. |
| 21-10-2026 | Clase 3 y presentaciones 03 a 06 incorporadas; trazabilidad, dependencias y prácticas de estimación/flujo desarrolladas | Propuestas para revisión; no cambia objetivos ni acredita pruebas empresariales. |
| 22-10-2026 | Escenario provisional concretado por autorización de Maverick; base de capacidad y guion en Markdown | Pendiente de revisión grupal y estimación de Rogelio; no hay aprobación empresarial. |
| 23-10-2026 | Actualización del equipo integrada: WSJF, esfuerzo/capacidad, presupuesto y tramos; prioridad sobre límites de apoyo del 22 | Cálculos verificados; calendario, asignación de épicas y frontera de costos requieren conciliación. |

Registrar decisiones efectivamente aceptadas, motivo, evidencia y documentos afectados. La [revisión de integración](integracion_avance_equipo.md) conserva los fundamentos de cada ajuste.
