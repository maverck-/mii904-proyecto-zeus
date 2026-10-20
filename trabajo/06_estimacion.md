# 6. Estimación y tratamiento de incertidumbre

**ESC-01: escenario cuantificado hipotético para discusión.** SUP-07/SUP-08/SUP-10. El usuario autorizó avanzar con supuestos explícitos; el grupo aún no los valida. Las cifras por paquete son valores didácticos construidos, sin cotizaciones ni historial de costos. Los únicos montos y plazos de referencia del caso son las alternativas de p. 7 y el techo de p. 5.

## Método, alcance y trazabilidad

Referencia B: 1.350 MM CLP, 9 a 12 meses. Estimar por paquetes PAQ de 04, con tres puntos optimista O, más probable M y pesimista P. Calcular E = (O + 4M + P) / 6 como escenario central; sin una distribución validada no implica probabilidad de éxito, intervalo de confianza ni compromiso de precio.

Unidad: **millones de CLP**. ESC-01 supone 12 meses, costo interno/externo, integración, configuración, licencias, seguridad/calidad, adopción y transición; PAQ-07 concentra recurrentes y soporte. Revisión financiera debe precisar impuestos, moneda, indexación y qué operación posterior a M12 requiere TCO adicional. No se investigaron tarifas de mercado.

## Rangos propuestos

| Paquete | O | M | P | E | Fundamento y validación pendiente |
| --- | ---: | ---: | ---: | ---: | --- |
| PAQ-01 | 40 | 60 | 90 | 61,67 | Gobierno/arquitectura/aprendizaje; revisar duración de coordinación y pruebas. |
| PAQ-02 | 180 | 240 | 360 | 250,00 | Mayor incertidumbre de integración, stock y concurrencia; revisar WMS/API y datos. |
| PAQ-03 | 150 | 220 | 320 | 225,00 | Configuración/compra y estados del pedido; validar alcance/licencia e interfaces. |
| PAQ-04 | 80 | 120 | 180 | 123,33 | C&C/formación piloto y primeras olas; validar carga y dotación de tiendas. |
| PAQ-05 | 70 | 100 | 160 | 105,00 | Devoluciones y expansión posterior; validar reglas y cobertura de SUP-05. |
| PAQ-06 | 100 | 150 | 220 | 153,33 | QA, controles, rendimiento y observabilidad transversales; precisar cobertura y entornos. |
| PAQ-07 | 100 | 140 | 220 | 146,67 | Transición, cloud/licencias y soporte del horizonte; validar consumo, modalidad y SLA. |
| Total | 720 | 1030 | 1550 | 1065,00 | Suma calculada con valores completos antes de redondear filas. |

La amplitud refleja áreas de incertidumbre conocidas del caso, no cuantifica su probabilidad. El peso relativo de integración/pedidos se propone porque sostiene el flujo. El monto absoluto requiere revisión académica de razonabilidad y, en una ejecución real, contraste de Finanzas/proveedores. Una fórmula precisa no transforma valores supuestos en evidencia.

## Reserva y asequibilidad

| Concepto | MM CLP | Origen / interpretación |
| --- | ---: | --- |
| Central de paquetes | 1065,00 | Cálculo de ESC-01. |
| Reserva nominal | 150,00 | SUP-08, sin calibración probabilística. |
| Central más reserva | 1215,00 | Propuesta de costo de trabajo con colchón. |
| Sobre de trabajo | 1350,00 | Límite propuesto anclado a referencia B; incluye la reserva. |
| Margen no asignado del sobre | 135,00 | 1350 − 1215; no es gasto ya comprometido. |
| Techo preliminar del caso | 1500,00 | Enunciado, p. 5. |
| Diferencia techo/sobre | 150,00 | No es una segunda reserva autorizada. |
| Adverso de partidas | 1550,00 | Suma P; ya excede techo por 50. |
| Adverso más reserva nominal | 1700,00 | Test conservador de asequibilidad; excede techo por 200. |

No contabilizar dos veces un riesgo ya materializado en partidas y consumo de reserva. Mostrar adverso con y sin reserva evita ocultar que las propias partidas pueden rebasar el techo. La reserva nominal no garantiza cobertura. Un costo central inferior a B no demuestra ahorro conseguido.

Primer tramo propuesto hasta 100 MM dentro del sobre para limitar exposición de validación; no es el costo calculado de todo M1 ni de PAQ-01. Finanzas/sponsor hipotéticamente deben determinar composición, disponibilidad y liberación de cada tramo.

## Capacidad y esfuerzo ilustrativos

SUP-02: dedicaciones hipotéticas, sin productividad o disponibilidad comprobadas. Persona-mes = dedicación FTE × meses activos; no convertir automáticamente esfuerzo en duración. Negocio/tiendas deben revisar además turnos y carga local, fuera de una mera equivalencia de personas centrales.

| Rol propuesto | FTE durante actividad | Meses activos | Persona-meses | Dependencia / observación |
| --- | ---: | ---: | ---: | --- |
| Dirección de proyecto | 0,75 | 12 | 9,00 | Gobierno y coordinación. |
| PO / representante de negocio | 0,50 | 12 | 6,00 | Decisión y aceptación disponibles. |
| Arquitectura / liderazgo técnico | 0,50 | 10 | 5,00 | Interfaces y soporte de especialistas. |
| Ingeniería de integración/inventario | 3,00 | 9 | 27,00 | Frente técnico con carga WMS/datos. |
| Ingeniería de pedidos/experiencia | 2,00 | 7 | 14,00 | Frente coordinado, no autónomo de interfaces. |
| QA | 1,00 | 10 | 10,00 | Pruebas integradas y regresión. |
| DevOps / confiabilidad | 0,75 | 10 | 7,50 | Entornos, observabilidad y recuperación. |
| Seguridad / datos | 0,50 | 10 | 5,00 | Controles, pruebas y revisión. |
| Analítica / medición | 0,50 | 10 | 5,00 | Base, eventos y evidencia. |
| Adopción / formación central | 0,50 | 8 | 4,00 | Dotación de tienda adicional por validar. |
| Total | No sumable como dotación fija | No aplica | 92,50 | Dedicaciones y meses no son tarifas ni plan de contratación. |

Los 92,5 persona-meses no se suman otra vez a los montos PAQ: el escenario de costo ya supone trabajo interno/externo. Tampoco se presenta como estimación bottom-up monetaria calibrada, porque faltan tarifas y asignación detallada por paquete. El cuadro permite discutir capacidad y costos de oportunidad, no cerrar precio.

## Duración y dependencias

M1/M2: base y prueba de interfaces; M2/M4: inventario y pedidos en paralelo parcial, sujeto a contratos; M3/M4: C&C y preparación de operación; M4/M5: uso y evaluación. M5/M7: estabilización y expansión; M8: protección del evento; M9/M11: evolución/devoluciones; M11/M12: transición y resultados.

La cadena de precedencias que limita M5 es viabilidad → inventario/pedidos → flujo usable → ventana de evidencia. Son ventanas de planificación, no una ruta CPM calculada ni una garantía de dotación. Si no cabe la medición en M5, ajustar antes de comprometer; no etiquetar go-live como beneficio.

## Sensibilidad y acciones

Si PAQ-02/PAQ-03 toman P y las demás E: costo = 1.270 MM, con reserva nominal = **1.420 MM**. Supera el sobre 1.350 por 70, aunque permanece bajo techo 1.500. Requiere decisión previa; no se utiliza automáticamente la diferencia con el techo.

Si el techo baja 20% a 1.200, central más reserva 1.215 supera el nuevo límite por 15. Reevaluar cobertura, PAQ-05 y alternativa C, manteniendo controles y actualizando beneficios. No afirmar que quitar PAQ-05 ahorra exactamente 105 MM: hay costos compartidos y transición.

Reestimar en G1/G2/G3 y ante nueva dependencia. Sustituir supuestos por evidencia o rangos revisados, registrar costo total a término y consumo de reserva, y actualizar alcance/beneficios. El grupo puede sustituir cualquier cifra didáctica; conservar coherencia y fundamento es más importante que conservar el total.
