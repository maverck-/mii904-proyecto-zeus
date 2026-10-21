# Acuerdos y supuestos

Versión de trabajo: 20 de octubre de 2026. **ESC-01 es un escenario académico propuesto, sin validación del grupo.** Sirve para desarrollar los siete entregables coherentemente. Las cifras se desarrollan para discutir una propuesta coherente y siguen pendientes de aprobación grupal.

## Hechos del caso

Enunciado: 68 tiendas, 3 CD; cancelación por stock 7,8%, exactitud 91%, preparación media 7,2 horas (pp. 3 y 4); máximo preliminar 1.500 MM CLP, 12 meses, valor en primeros 5, Black Friday aproximadamente M8, ERP sin reemplazo, WMS sin reemplazo completo, continuidad y controles (p. 5); B = 1.350 MM y 9 a 12 meses (p. 7). Son antecedentes de una empresa ficticia. La cobertura y las metas de ESC-01 no vienen dadas por esos antecedentes.

## Decisiones

| ID | Decisión | Estado | Condición para revisar |
| --- | --- | --- | --- |
| DEC-01 | Desarrollar B modular como alternativa base | Base de trabajo revisable | Integración, valor M5, costo o capacidad no sostienen la propuesta. |
| DEC-02 | Inventario/pedidos/C&C primero, controles y soporte desde inicio | Propuesta ESC-01 | Prioridad y dependencias revisadas con el grupo. |
| DEC-03 | IA, data platform corporativa y Ship-from-store fuera del compromiso base | Propuesta ESC-01 | Nueva necesidad, valor o dependencia justificados dentro de límites. |
| DEC-04 | Híbrido con gobierno, releases y aprendizaje conectados | Propuesta ESC-01 | Capacidad de negocio y análisis contextual justifican ajustar prácticas. |
| DEC-05 | Trabajar con piloto y expansión condicionada del escenario | Propuesta ESC-01 | Cobertura y beneficio razonables frente a costo y capacidad. |

## Supuestos de ESC-01

Todos están **propuestos y pendientes de validación**. La columna de revisión académica indica lo que el equipo puede evaluar para defender el caso. La validación empresarial se describe como trabajo futuro hipotético: no se ha contactado una empresa real ni ejecutado pruebas.

| ID | Supuesto y fundamento inicial | Revisión académica requerida | Validación empresarial hipotética / momento | Si falla |
| --- | --- | --- | --- | --- |
| SUP-01 | ERP/WMS admiten integración acotada; B se apoya en mantenerlos | Justificar alternativa y dependencias, sin dar por conocida la API | Tecnología/proveedor prueban contrato, consistencia, carga y recuperación; G1/M2 | Revisar integración, alcance, costo y B. |
| SUP-02 | Negocio, tiendas y especialistas tienen capacidad para piloto y dos frentes técnicos | Revisar dedicaciones y simultaneidad de 06 | Sponsor/Operaciones confirman disponibilidad y dotación; G0/G1 | Limitar trabajo simultáneo o cobertura. |
| SUP-03 | Hay datos comparables y volumen para evaluar cuatro semanas de piloto | Revisar denominadores y sesgos de 01 | Dueños de beneficio validan base por cohorte, eventos y volumen; G1 | No afirmar resultado; anticipar medición o revisar gate. |
| SUP-04 | El flujo puede operar en M4 y producir valor comprobable hasta M5 | Revisar precedencias, capacidad y ventana; el plazo total de B no lo demuestra | Dirección/Operaciones verifican plan y uso real; G1/G2 | Declarar requisito incumplido si solo hay entrega técnica y revisar inversión. |
| SUP-05 | Piloto de 5 tiendas y 1 CD; hasta 20 tiendas en M7 y 35 en M11 | Justificar exposición acotada, diversidad y costo; son coberturas totales, no sumas | Operaciones selecciona sitios y autoriza cada ola por capacidad | Reducir/ampliar cobertura con nuevos costo y beneficio. |
| SUP-06 | Metas piloto: cancelación <4%, exactitud ≥96%, preparación <4 h | Revisar ambición intermedia frente a metas estratégicas y base de cohorte | Dueños de beneficio ratifican metas y definiciones en G1 | Recalibrar; una base mejor que el umbral no permite aceptar deterioro. |
| SUP-07 | Rangos de costo por paquete de 06 son valores didácticos construidos | Revisar componentes, magnitud relativa, cobertura y sensibilidad; no llamarlos cotizaciones | Finanzas contrasta costos internos, proveedores, licencias, transición e impuestos; G1 | Sustituir rangos y reestimar. |
| SUP-08 | Sobre de trabajo 1.350 MM, reserva nominal 150 incluida; primer tramo hasta 100 MM | Acordar límite de exposición y regla de uso; reserva sin probabilidad calibrada | Sponsor/Finanzas aprueban tramos y forecast; G0/G1 | Ajustar gasto/alcance; techo 1.500 sigue vigente. |
| SUP-09 | Pesos y notas de priorización de 05 reflejan el juicio inicial del caso | Revisar ponderaciones, notas y orden por dependencias | PO y comité revisan prioridades con nueva evidencia | Reordenar y actualizar impacto en roadmap/costo. |
| SUP-10 | Costos de 06 incluyen 12 meses, trabajo interno/externo y operación/transición sin doble conteo | Comprobar frontera de paquetes y reconocer ausencia de TCO posterior | Finanzas valida licencias, consumo, soporte y tratamiento tributario | Rehacer costo total antes de comprometer escala. |
| SUP-11 | 99,9% de disponibilidad y cero riesgos críticos abiertos son criterios de salida operativos propuestos | Acordar medición y autoridad; continuidad de despliegue sigue obligatoria | Tecnología/CISO/Operaciones aceptan pruebas y operación por release | Bloquear liberación o expansión y corregir. |

## Control de cambios

| Fecha | Actualización | Estado de revisión del grupo |
| --- | --- | --- |
| 20-10-2026 | Desarrollado ESC-01 con metas, cobertura, costos, roles y gates explícitos | Pendiente |

Al acordar cambios, registrar decisión, motivo, evidencia, revisión y archivos afectados. Aprobar un supuesto para el ejercicio significa aceptar su razonabilidad y coherencia; no demuestra que sea cierto en una operación real. El alcance del informe y las responsabilidades académicas aún no se asignan por inferencia.
