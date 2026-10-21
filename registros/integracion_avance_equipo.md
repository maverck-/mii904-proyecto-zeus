# Integración del avance del equipo, 21 de octubre

**ESC-02 toma como base principal el avance recibido del equipo.** Se conserva el [texto de entrada](../insumos/avance_equipo_2026-10-21.md) y se integra en los documentos 01, 02 y 03. Los documentos 04 a 07 se alinean con esa base. El escenario ESC-01 anterior queda como antecedente en Git, no como plan vigente.

## Qué se conserva y prioriza

B modular; gobierno predictivo y entrega adaptativa; Kanban para integración/APIs y Scrum de dos semanas para experiencia; PM/PO/Arquitectura/CISO; gates M1/M5/M9; piloto de 10 tiendas; objetivo de C&C en 68 tiendas en M7; devoluciones y experimento Ship-from-store en R3/M12; >80% de preparación C&C por aplicación; exclusiones de IA, data platform completa, amplia migración cloud y nueva plataforma de identidad. Los valores adicionales se mantienen como propuestas/supuestos, no como hechos del caso.

## Correcciones y pendientes con fundamento

| ID | Prioridad | Hallazgo del avance | Tratamiento de integración | Fundamento |
| --- | --- | --- | --- | --- |
| INT-01 | Alta | Business Case queda inconcluso en «1.3 Alternativas» y faltan comparación, beneficios, costos y recomendación desarrollados | Completar desde los datos oficiales y la hipótesis del equipo; distinguir output/outcome/beneficio/valor | Enunciado p. 8 lo exige; p. 9 asigna 15% a diagnóstico/valor y 15% a Business Case/alternativas. |
| INT-02 | Alta | Pasar de 10 tiendas en M5 a 68 en M7 no tiene capacidad ni costo demostrados | Conservar objetivo del equipo condicionado; proponer cuatro olas de 15/15/14/14 adicionales y pedir estimación de capacidad | Son 58 tiendas adicionales en aproximadamente dos meses. Enunciado pp. 5 y 8 exige continuidad, estimación y dependencias; no obliga una cobertura nacional en M7. |
| INT-03 | Alta | R1 en M5 y «primera entrega antes del mes 5» dejan ambigua la evidencia de valor | Usar el requisito correcto «dentro de los primeros cinco meses»; proponer operación piloto desde M4 y evaluación hasta G1/M5 | Enunciado p. 5 exige valor dentro de los primeros 5 meses; poner en producción al final de M5 no prueba un beneficio. |
| INT-04 | Alta | Observabilidad parece entregarse solo en R3 | Observabilidad mínima, controles, alertas y medición desde R1; ampliar centralización/cobertura en R3 | Continuidad/controles p. 5 y valor medible p. 8. No puede medirse beneficio ni protegerse campaña si recién se observa al cierre. |
| INT-05 | Alta | «Integración ERP de baja incertidumbre» y «solución conocida» confunden restricción con viabilidad técnica | Mantener gobierno formal; añadir prueba técnica antes de compromiso irreversible y reconocer incertidumbre API/datos | ERP no se reemplaza (p. 5), pero el caso describe legacy e integraciones complejas (p. 3). Estabilidad del requisito no prueba solución conocida. |
| INT-06 | Alta | Los costos/dedicaciones de ESC-01 corresponden a otra cobertura y excluían Ship-from-store | Retirar sus totales del presupuesto vigente y dejar plantilla paramétrica de reestimación a Rogelio | 5/20/35 tiendas y exclusión del experimento no equivalen a 10/68 y R3 ampliado. No extrapolar ahorro o viabilidad de un alcance distinto. |
| INT-07 | Media | Devoluciones ≥85% en Charter frente a meta estratégica ≥90% | Conservar ≥85% como objetivo propuesto de ZEUS a M12, indicando brecha de 5 puntos porcentuales y evolución por acordar | Enunciado p. 4 fija ≥90%; p. 8 permite decisiones defendibles. Una meta parcial no es errónea si se distingue y justifica, pero no debe presentarse como cumplimiento de 90%. |
| INT-08 | Media | Tabla omite desigualdades de metas | Restituir cancelación <2%, puntualidad ≥95% y exactitud ≥98% | Enunciado p. 4. «2%» no equivale a «menos de 2%». |
| INT-09 | Media | Se atribuye directamente 7,8% a la latencia y se afirma que conservar legacy abarata desarrollo | Redactar asociación e hipótesis; conservar legacy evita un reemplazo, pero no garantiza menor costo total de integrar/operar | Enunciado pp. 3 a 5 informa síntomas y restricciones, no descomposición causal ni comparación económica. |
| INT-10 | Media | API-first/eventos, OMS de mercado y cinco equipos se presentan con distinto grado de certeza | Mantener como decisiones/supuestos propuestos; definir validación, tamaño/dedicación y condiciones de compra | El caso orienta APIs reutilizables y propone gestión de pedidos (pp. 4 y 5), no proveedor, tecnología de eventos ni cinco dotaciones dedicadas. |
| INT-11 | Media | Contrato OMS en M1 sin resolver interfaz/costo; gates solo M1/M5/M9 | Conservar gates financieros del equipo y añadir revisión técnica M2 y preparación M7; contratar con validación/aceptación escalonadas | Enunciado p. 2 exige coherencia; pp. 5/8 requieren continuidad, incertidumbre y viabilidad. La revisión técnica no necesita otro gate financiero. |
| INT-12 | Media | Black Friday «inamovible en M8» y «ruta crítica» sin red calculada | Ubicar campaña aproximadamente en M8; una vez confirmada su fecha externa se protege. Describir precedencias, sin afirmar CPM calculado | Enunciado p. 5 dice aproximadamente 8 meses. Una ruta crítica formal requiere actividades, duraciones y dependencias. |
| INT-13 | Media | Disponibilidad 99,9% solo durante evento, junto con «sin interrupciones» | Medir disponibilidad con ventana definida, proteger campaña y mantener continuidad de despliegue; distinguir objetivo de aceptación de resultado observado | Enunciado pp. 4 y 5: ≥99,9% estratégico y continuidad. Un porcentaje no autoriza una parada planificada ni garantiza cero incidentes futuros. |

## Decisiones que quedan para el grupo

Sostener o ajustar 68 tiendas en M7 tras estimación; aceptar ≥85% como paso intermedio de devoluciones o elevarlo con costo/alcance coherentes; confirmar límites del experimento Ship-from-store y su financiación; validar OMS/equipos; cerrar monto y reserva. No reemplazar estas decisiones por la cobertura del escenario anterior.

## Responsables indicados

Rogelio: priorización y estimación. Maverick: diseño del alcance y roadmap. Los primeros tres entregables conservan la base recibida y se revisan por el equipo; la autoría individual entre los restantes integrantes no se infiere del texto.
