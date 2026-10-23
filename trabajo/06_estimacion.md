# 6. Estimación y tratamiento de incertidumbre

**Responsable indicado: Rogelio. ESC-02 pendiente de cuantificación.** Se conserva el método de trabajo, pero se retiran como vigentes los montos y 92,5 persona-meses de ESC-01: estimaban otra cobertura y excluían el experimento. No demuestran viabilidad de 10/68 tiendas ni de cinco equipos. Este documento prepara la estimación y declara lo que falta para cumplirla.

## Referencias y unidad

Enunciado: B = **1.350 MM CLP**, 9 a 12 meses (p. 7); máximo preliminar **1.500 MM CLP**, 12 meses, primera entrega de valor dentro de M5 (p. 5). Son referencia y restricción, no costos descompuestos ni autorización de gasto. MM CLP significa millones de pesos chilenos. La diferencia nominal 150 no es reserva aprobada ni dinero libre.

SUP-07/SUP-08/SUP-10: reconstruir costo de ESC-02 con alcance de 04 y secuencia de 07. Para el ejercicio pueden usarse rangos supuestos defendidos por el equipo, identificados como tales. No hacen falta cotizaciones reales de una empresa ficticia, pero no deben inventarse como obtenidas. No se investigaron tarifas de mercado.

## Técnica según decisión y horizonte

La sesión 05, pp. 4 a 11 ([material](../insumos/presentaciones/README.md)), distingue objetivo, estimación y compromiso. 68/M7 es un objetivo de cobertura; una estimación debe mostrar si costo y capacidad lo sostienen; el compromiso se acepta por la autoridad con riesgo explícito. Ni el techo 1.500 ni la referencia B calculan por sí solos la nueva solución.

| Decisión | Técnica propuesta | Evidencia / límite |
| --- | --- | --- |
| Formular inversión ejecutiva | Referencia B como orientación y descomposición por PAQ con rangos | Ajustar por alcance, licencias, personas, sitios y riesgo; no tratar B como histórico comparable demostrado. |
| Resolver R0/R1 próximo | Descomposición por entregable y tres puntos para incertidumbre; cantidades × tarifas donde sea defendible | Detallar interfaces/aceptación, dedicación y pruebas; supuestos identificados si faltan datos. |
| Ampliar tiendas | Paramétrica por habilitación local, separando plataforma común y sitios | Validar tiempo/costo por tienda y paralelismo; no multiplicar toda la plataforma por número de locales. |
| Refinar backlog de equipo | Comparación relativa de tamaño/complejidad para conversar y dividir | Sin equivalencia automática de story points a horas ni comparación de puntos entre cinco equipos. |
| Actualizar forecast durante ejecución | Terminados/tiempos de ciclo con unidades comparables y sistema suficientemente estable | Sin histórico real de ZEUS no atribuir P80/P90 ni Monte Carlo calibrado a los rangos supuestos. |

Cada rango debe registrar alcance, unidad, base, técnica, supuestos, riesgos, fecha y quién lo revisa. Las demostraciones y cantidades del onboarding de sesión 05 no son datos de ZEUS. La estimación cuantificada sigue pendiente de Rogelio.

## Método y tabla de trabajo

Descomponer por PAQ. Estimar optimista O, más probable M y pesimista P con fundamento; E = (O + 4M + P) / 6. Es un escenario central de trabajo, sin confianza probabilística demostrada. Comparar también suma P, riesgos correlacionados y reserva, evitando doble conteo. Usar cantidades × tarifas para las subpartidas con unidad identificable.

| Paquete | Base de cálculo de ESC-02 | O | M | P | E | Información / decisión pendiente |
| --- | --- | --- | --- | --- | --- | --- |
| PAQ-01 | Meses de gobierno, arquitectura y pruebas iniciales | Pendiente | Pendiente | Pendiente | Pendiente | Dedicaciones, hitos y actividades de viabilidad. |
| PAQ-02 | Interfaces × esfuerzo, datos/reconciliación y adaptación WMS | Pendiente | Pendiente | Pendiente | Pendiente | Contratos, número/complejidad, carga y calidad stock. |
| PAQ-03 | Configuración OMS, estados e interfaces de pedido | Pendiente | Pendiente | Pendiente | Pendiente | Compra/configuración, implantación y personalizaciones. |
| PAQ-04 | App/C&C común + habilitar 10 piloto y 58 adicionales | Pendiente | Pendiente | Pendiente | Pendiente | Costo fijo/reusable y costo local por ola, turnos y formación. |
| PAQ-05 | Devoluciones + experimento Ship-from-store delimitado | Pendiente | Pendiente | Pendiente | Pendiente | Separar subpartidas y techo experimental antes de G2. |
| PAQ-06 | QA transversal, controles, carga, observabilidad y recuperación | Pendiente | Pendiente | Pendiente | Pendiente | Entornos, pruebas y especialidades desde R1. |
| PAQ-07 | Licencias/consumo/soporte/transición de 12 meses | Pendiente | Pendiente | Pendiente | Pendiente | Base por tienda/pedido/usuario, fechas de alta y recurrentes. |

No sumar un precio de solución que ya incluye ingeniería y volver a cargar todos sus FTE. Licencias se concentran en PAQ-07; configuración OMS en PAQ-03. La formación local de las 68 tiendas está en PAQ-04. Costos comunes de C&C no se multiplican automáticamente por 6,8 al pasar de 10 a 68. Más sitios sí afectan soporte, consumo, licencias y operación.

## Capacidad y calendario

SUP-02 conserva cinco equipos de implementación como supuesto recibido; faltan tamaño, especialidad, dedicación y meses. No significa cinco personas ni los cuatro integrantes académicos. Definir funciones de integración/datos, OMS/pedidos, experiencia/tiendas, calidad/confiabilidad y coordinación según arquitectura, sin asumir que la división propuesta acredita cinco equipos disponibles.

Persona-meses = suma de FTE por rol y periodo × meses. Costo de trabajo = persona-meses × tarifa por rol, cuando se use ese método. Separar trabajo de proveedor incluido en contrato y capacidad interna. Horas de formación/operación por tienda se estiman con participantes × horas y cobertura de turnos; registrar costos de oportunidad aunque no sean desembolso externo.

## Cantidades de apoyo listas para costear

El [escenario provisional del 22 de octubre](../registros/escenario_provisional.md) concreta alcance y capacidad sin inventar tarifas. Son supuestos de apoyo a la estimación de Rogelio, que puede cambiarlos dejando su impacto.

| Componente | Cantidad propuesta / unidad | Imputación y cuidado de costo |
| --- | --- | --- |
| Habilitación piloto | 40 jornadas-persona; 2 brigadas × 2 personas × 10 días hábiles | PAQ-04; soporte y preparación previos no quedan absorbidos automáticamente. |
| Expansión, trabajo local | 232 jornadas-persona de trabajo requerido para 58 tiendas | PAQ-04; no sumarlas otra vez si ya se paga la disponibilidad de brigadas. |
| Brigadas disponibles para expansión y margen | 5 × 2 × 40 = 400 jornadas-persona de disponibilidad nominal; 320 efectivas al 80% | Costear según contrato/dedicación: incluye 30 días de expansión y 10 protegidos. Trabajo requerido no equivale a facturación. |
| Personal local formado | 1.632 horas-participante: 240 piloto y 1.392 expansión | PAQ-04; horas de participantes diferentes de formadores incluidos en brigadas. Costear turnos/oportunidad sin asumir 408 nuevas contrataciones. |
| Preparación de CD | Hasta 30 jornadas-persona para los 3 CD: 10 piloto y 20 adicionales | PAQ-02; revisar complejidad real y recursos de integración compartidos. |
| Experimento Ship-from-store | 2 tiendas, 4 semanas/200 pedidos máximos; exposición incremental propuesta ≤30 MM CLP | Estimar subpartidas PAQ-05 y recurrentes de PAQ-07; el límite incluye todo el incremento, dentro del techo general, sin duplicar componentes reutilizados. |

Costos por brigada deben aclarar viajes, equipamiento, disponibilidad y soporte. El factor 80% no elimina el pago del tiempo no productivo; para contrato por disponibilidad se costean jornadas nominales. Identificar si la dotación se contrata aparte o sale de los cinco equipos de implementación, reduciendo capacidad concurrente de desarrollo. Licencias por tienda/usuario/pedido crecen con fechas de alta; cobertura nacional se limita a las familias incluidas, no todo el catálogo.

El modelo muestra 58 altas con 240 jornadas-persona efectivas planificadas frente a 232 requeridas, y 80 efectivas adicionales de margen. No garantiza que cinco equipos nominales sostengan construcción, revisiones CISO/QA, operación y brigadas a la vez. La prueba de asequibilidad sigue pendiente del costo total, reserva y financiación; 29 altas por mes es ritmo requerido, no histórico observado.

## Presupuesto, reserva y autorización por completar

| Concepto | Valor / estado | Regla de cierre |
| --- | --- | --- |
| Referencia B del caso | 1.350 MM CLP | Comparar con propuesta descompuesta; no reemplaza su cálculo. |
| Techo preliminar del caso | 1.500 MM CLP | Restricción de asequibilidad. |
| Central de paquetes | Pendiente | Sumar E sin redondear antes de total. |
| Reserva propuesta | Pendiente | Justificar por riesgos, exclusiones y regla de uso; no asumir automáticamente 150. |
| Central más reserva | Pendiente | Comparar con límite y financiación propuesta. |
| Escenario adverso | Pendiente | Mostrar P y tratamiento de reserva sin ocultar excedentes. |
| Primer tramo G0 y compromisos hasta VT-01 | Pendiente | Cuantificar exposición, actividades y aceptación contractual. |
| Liberaciones G1/M5 y G2/M9 | Pendiente | Costos a término, beneficios y condiciones por gate. |

Precisar impuestos, moneda/indexación, inversión/gasto, contratos recurrentes y operación posterior a M12. Declarar TCO posterior separado cuando no esté dentro del horizonte, sin ocultar obligaciones asumidas durante el proyecto.

## Sensibilidades que debe defender el equipo

1. WMS/integración demora o toma el rango alto: efecto en costo y primera evidencia hasta M5.
2. Las 58 altas requieren más brigadas, soporte o licencias: efecto en M7 y techo.
3. Menor adopción/stock confiable: se mantiene costo pero baja beneficio; no escalar sin mejora verificable.
4. OMS por transacción o consumo de campaña mayor: costo recurrente y dependencia contractual.
5. Experimento R3 no cabe: diferirlo con cambio explícito de alcance, sin retirar controles/soporte.
6. Techo disminuye 20%: nuevo límite 1.200 MM; recalcular propuesta cuando exista, sin afirmar un ahorro no estimado.

Antes del viernes: completar rangos y capacidad, total/reserva/adverso, financiación inicial y sensibilidad. **Este apartado aún no cumple una estimación cuantificada terminada.** Reestimar con evidencia en VT-01 y gates G1/G2; cualquier ajuste de cobertura modifica 04/07 y los beneficios de 01/03.
