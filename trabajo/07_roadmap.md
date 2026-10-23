# 7. Roadmap y planificación

**Responsable: Maverick. ESC-02, propuesta desarrollada al 23-10-2026 para revisión del equipo.** Meses relativos al inicio empresarial. La entrega académica del 24 de octubre es distinta de M12. Hechos: valor dentro de los primeros cinco meses, Black Friday aproximadamente M8 y horizonte 12 meses (enunciado, p. 5). El [plan de apoyo](../registros/plan_alcance_roadmap.md) contiene calendario de referencia, matriz de esfuerzo y dimensionamiento; sus cantidades nuevas son supuestos explícitos.

## Releases y evidencia

| Release | Ventana propuesta | Capacidades | Cobertura propuesta | Evidencia / condición |
| --- | --- | --- | --- | --- |
| R0 | M1/M2 | CAP-01 + inicio CAP-05/CAP-06 | Datos y sitios representativos | Base por cohorte, arquitectura, OMS por hitos y prueba ERP/WMS; VT-01/M2. Aún no acredita valor comercial. |
| R1 | Construir M2/M4; primera salida al fin de semana 16; observar semanas 17–20 y decidir al cierre M5 | CAP-02/CAP-03/CAP-04 y transversales | 10 tiendas, un CD y dos familias como hipótesis de diseño | Medir beneficio frente a base comparable; umbrales SUP-16 para revisión; no basta instalación; G1/M5. |
| R2 | Tras G1, expansión M6/M7 | CAP-07 y transversales | Objetivo 68 tiendas, hasta tres CD, mismas dos familias | Cada ola con datos, dotación, controles y soporte; VE-01/M7. No forzar altas para completar la cifra. |
| Campaña | Aproximadamente M8, fecha por confirmar | Cobertura aceptada y transversales | Solo sitios operables | Carga representativa, monitoreo, respuesta, reversión y promesas protegidas; disponibilidad con ventana acordada. |
| R3 | Tras G2/M9: devoluciones/centralización en M9/M10; medición y experimento M11; cierre M12 | CAP-08/CAP-09 + ampliar CAP-05 | Devoluciones de compras web elegibles; experimento de 3 a 5 tiendas, máximo cuatro semanas/300 pedidos | KPI-04 ≥85% propuesto; reglas y límites de 04; financiación/exposición autorizadas antes de iniciar. |

Observabilidad mínima, seguridad, soporte y formación se incorporan desde R1 y se sostienen en todas las olas. R3 amplía centralización/cobertura. El experimento no compromete Ship-from-store nacional. El [avance del 23](../insumos/avance_equipo_2026-10-23.md) aporta WSJF y estimación con prioridad. El catálogo, la medición y las olas se concretan como propuesta de Maverick para ratificación; no se suman brigadas históricas ni se vuelve al experimento de dos tiendas/30 MM.

## Calendario de referencia y primera entrega

Se propone una convención de 52 semanas/26 sprints: M1–M5 cubren semanas 1–22; M6/M7, 23–30; M8, 31–35; M9–M12, 36–52. Es una distribución de planificación, no fechas civiles confirmadas. G0 ocurre en M1; VT-01 al fin de semana 8; G1 al fin de 22; VE-01 al fin de 30 y G2 al inicio de 36. Confirmar feriados/turnos y fecha externa antes de fijar compromisos.

Para primera salida al terminar semana 16 se asignan 36 equipo-sprints a un flujo mínimo completo contra 38 disponibles. Uso previsto 94,74%: es una ventana exigente, no una garantía. Las 11,7 unidades restantes de F1 completan cobertura/estabilización hasta G1. El [desglose por épica](../registros/plan_alcance_roadmap.md) separa ambas partes: solo puede diferirse trabajo que no sea necesario para aceptar el flujo expuesto.

Base comparable propuesta: semanas 9–12; uso observado: 17–20; análisis y G1 hasta semana 22. SUP-16 propone mejora relativa de 20% en cancelación y 25% en preparación, adopción >80% por tienda y evidencia suficiente. Si el flujo usable se retrasa, recalcular la ventana de evidencia antes de mantener M5; no etiquetar una demo como valor.

## Olas propuestas para revisar capacidad

Se conserva la meta del equipo de 68/M7. Las cuatro olas son un complemento de planificación, **no un acuerdo ni una capacidad demostrada**.

| Ola | Ventana propuesta | Tiendas adicionales | Total acumulado | Condición previa |
| --- | --- | ---: | ---: | --- |
| Piloto | M4/M5 | 10 | 10 | VT-01, operación/medición/soporte aceptados. |
| O1 | Días hábiles 1 a 8 de M6/M7 | 15 | 25 | G1, células/horas/stock disponibles y CD correspondiente aceptado. |
| O2 | Días 9 a 16 | 15 | 40 | Estabilidad O1, capacidad y costo actualizado. |
| O3 | Días 17 a 23 | 14 | 54 | Estabilidad O2 y pruebas/carga según expansión. |
| O4 | Días 24 a 30 | 14 | 68 | Estabilidad O3 y tiempo para VE-01/correcciones antes de campaña. |

Se proponen treinta días hábiles de altas y diez posteriores de estabilización/carga/VE-01 dentro de los cuarenta de referencia de M6/M7. Cada ola exige aceptación por sitio según 04 y revisión de estabilidad antes de la siguiente. Un sitio fallido no se cuenta como habilitado; una aceptación parcial actualiza la cobertura real y el forecast.

Mecanismo propuesto: tres células de dos funciones durante treinta días, con disponibilidad efectiva 75% y un día de célula por tienda. Ofrecen 135 persona-días efectivos frente a 116 requeridos. Su dedicación bruta 180 cabe dentro de 210 de E11/R2, sin cobrarla otra vez. Es una hipótesis distinta de las cinco brigadas históricas, no personal contratado. Calibrar tiempos con el piloto y confirmar que perfiles, viajes/soporte y turnos caben en COST-01/COST-06.

Si el promedio fuera 1,5 días por tienda se requieren 39 días de altas; si fueran dos, 52. Ambos desvían la ventana de treinta y el segundo supera los cuarenta totales. G1 debe resolver refuerzo autorizado, secuencia o cobertura; no consumir silenciosamente la preparación de campaña. El [dimensionamiento y sensibilidad](../registros/plan_alcance_roadmap.md) explicitan estas operaciones.

## Capacidad y financiación recibidas del equipo

R0/R1 propone capacidad 56/carga 47,7; R2 24/23; campaña y R3 40/33,3 equipo-sprints. Total 120/104. R2 usa 95,83% y R1/R2 conjunto 88,375%; el promedio no elimina el pico. La nueva matriz de apoyo asigna cada épica sin modificar su PERT y separa campaña 5 de R3 28,3. También identifica funciones y ventanas; falta contrastar dedicación real por especialidad con Rogelio.

Financiación recibida: G0 675, G1 345 y G2 310 MM, más reserva 170, marco total 1.500. M8 pertenece a tramo 2 y protege campaña; R3 se autoriza desde G2/M9. La opción propuesta conserva seis equipos en sprints 6–15 y cuatro desde 16, antes de campaña. F3 reserva capacidad 6 para campaña y 34 para R3 posterior a G2; sprint 17 está pagado y dedicado a estabilización, fuera de las 120 unidades efectivas. Rogelio debe revisar contratos y coste mensual: no se declara aprobada esa reducción ni cobertura de soporte.

Sin sexto equipo, la fuente plantea refuerzo mediante reserva o priorizar tiendas de mayor venta y completar después de campaña. Es una contingencia que modifica cobertura/plazo: sponsor/comité debe decidirla y actualizar Charter/beneficios; no constituye el compromiso base ni una renuncia anticipada a 68/M7.

## Gates financieros y revisiones de salida

| ID | Momento | Evidencia / decisión | Autoridad propuesta |
| --- | --- | --- | --- |
| G0 | M1 | Arquitectura inicial, OMS por hitos y primer tramo propuesto 675 MM; flujo categoría/mes por conciliar | Comité/sponsor con Finanzas y Arquitectura. |
| VT-01 | Final M2 | Prueba de interfaces/datos, OMS, capacidad, controles y forecast antes de piloto | Tecnología/Arquitectura, CISO, Operaciones; PM escala desvíos al comité. |
| G1 | M5 | Evidencia de primera entrega de valor y decisión de expandir con costo/capacidad aceptados | Comité/sponsor y dueños de beneficio. |
| VE-01 | M7, después de aceptar R2 | Cobertura segura, carga, recuperación, soporte y preparación de campaña; iniciar congelamiento propuesto | Operaciones/Tecnología/CISO y sponsor. |
| G2 | M9 | Revisar beneficios, campaña, forecast y financiación de devoluciones/experimento R3 | Comité/sponsor, Finanzas y dueños de beneficio. |
| Cierre | M12 | Aceptación, transferencia, costo y beneficios pendientes con responsables | Sponsor/Operaciones y dueños de beneficio. |

VT-01 y VE-01 son revisiones técnicas/operacionales adicionales a los gates del equipo. El contrato OMS de G0 requiere hitos de prueba/aceptación, para no asumir resueltas APIs/licencias antes de validar. Reglas de devoluciones pueden analizarse antes de M9, pero gasto/compromiso R3 requiere autorización y estimación.

### Preparación operativa y congelamiento propuestos

E8a debe permitir detectar stock desactualizado, pedidos detenidos y fallos del servicio desde R1. Antes de abrir, probar que las alertas llegan a un responsable, que existe un procedimiento de respuesta y que se puede recuperar o revertir el flujo. Antes de cada ola, revisar su cobertura y capacidad de atención; VE-01 añade carga representativa de campaña y prueba de respuesta/recuperación. E8b en R3 amplía la centralización, no inaugura el monitoreo.

Para compatibilizar despliegue R2 y protección de campaña, se propone iniciar el congelamiento después de aceptar R2 y superar VE-01 dentro de M7, hasta terminar Black Friday aproximadamente en M8. Las fechas exactas dependen del calendario confirmado. Durante esa ventana no se despliegan funcionalidades ordinarias nuevas en producción; correcciones críticas de seguridad o continuidad requieren evaluación y autorización de Operaciones/Tecnología/CISO, con escalamiento al sponsor si cambian compromisos. Esto precisa la regla general de congelar cambios de alto riesgo y requiere ratificación.

Continúan monitoreo, soporte y estabilización con dotación prevista. El análisis o la preparación en ambientes no productivos solo usa capacidad y gasto autorizados; no convierte M8 en un release R3 ni anticipa financiación de G2. Si R2 no se acepta a tiempo, escalar cobertura, fecha y costo: no superponer automáticamente despliegues ordinarios con el congelamiento para conservar la cifra 68/M7.

## Dependencias y acciones

Cadena que condiciona M5: acceso y viabilidad → inventario/reservas y pedidos → C&C usable → ventana de evidencia. Parte de integración/pedidos puede solaparse una vez acordados contratos y capacidad. No es una ruta crítica CPM calculada: faltan duraciones detalladas, holguras y recursos.

| Punto de control | Evidencia mínima propuesta | Respuesta si no se cumple |
| --- | --- | --- |
| VT-01, semana 8 | Prueba representativa ERP/WMS/OMS con consistencia, conciliación y recuperación; responsables de interfaces disponibles | Reestimar B/integración y efecto en primera salida; elevar antes de comprometer piloto. |
| Primera salida, semana 16 | Flujo completo aceptado por Tecnología/CISO/Operaciones en diez tiendas; base, soporte y medición disponibles | No exponer flujo incompleto; corregir y recalcular evidencia/fecha/costo. |
| G1, semana 22 | Cuatro semanas de uso comparable, adopción/mejora y forecast; recursos y coste de olas revisados | Resultado inconcluso o sin mejora: investigar y condicionar inversión/expansión, sin afirmar valor demostrado. |
| Cada ola y VE-01, hasta semana 30 | Sitios aceptados, pruebas representativas de carga/recuperación, respuesta y promesas sostenibles | Detener siguientes altas, preservar cobertura segura y elevar efecto sobre 68/M7. |
| G2, semana 36 | Campaña evaluada, forecast/financiación R3, reglas de devolución e hipótesis/techo de exposición del experimento | No iniciar capacidad condicionada sin autorización; priorizar objetivo de devolución frente a opcionales. |
| Cierre, semana 52 | Capacidades aceptadas, resultados/brechas KPI, soporte y transferencia, responsables de beneficios pendientes | Registrar pendientes y autoridad que los acepta; no simular que todo beneficio ya se realizó. |

M5 sin evidencia suficiente: no declarar primera entrega de valor cumplida; investigar base/uso y revisar inversión. WMS tardío: replantear interfaces/plazo/alternativa, sin pruebas ficticias. Stock o adopción deficientes: corregir antes de ampliar. Escala no operable o campaña amenazada: mantener sitios seguros y diferir altas con impacto explícito. Costo mayor que techo: revisar alcance y financiación antes de comprometer. R3 experimental sin hipótesis/costo: no iniciar experimento.

## Dependencias con evidencia y responsable

Complemento propuesto desde sesión 04, p. 9, y sesión 06, pp. 5 a 8. Externo al control del proyecto no significa ajeno a su coordinación.

| Dependencia | Coordinación responsable | Evidencia requerida | Momento necesario / efecto |
| --- | --- | --- | --- |
| ERP/WMS y condiciones de OMS | PM/Tecnología con proveedores | Contratos de datos, acceso, prueba representativa y soporte | VT-01/M2; si falla, afecta inventario/pedido y primera entrega. |
| Stock, turnos, espacio y formación por tienda/CD | Operaciones/Logística/gerencias de tienda | Preparación y aceptación del sitio, roles y soporte | Antes del piloto y de cada ola; condiciona altas. |
| CISO/Arquitectura y ambientes de prueba | Tecnología/CISO | Controles, integración, carga y recuperación | Cada release y VE-01; las revisiones consumen capacidad. |
| Regla de devolución y conciliación | Comercial/Finanzas/Operaciones | Elegibilidad, estados y aceptación | Antes de CAP-08/R3; no suponer que reglas aparecen al construir. |
| Dotación/contratos/costo por tramo | PM/Finanzas/proveedores | FTE por periodo, compromisos y forecast a término | G0, G1 y G2; cinco equipos nominales no garantizan especialistas disponibles. |

## Horizonte, referencia y forecast

Mantener horizonte M12 por capacidades y gates; R1 con mayor detalle de interfaces, aceptación y recursos; trabajo cercano por sprint/flujo y readiness. R2 conserva olas con validación de capacidad; R3 permanece por capacidades/hipótesis hasta acercarse G2. Esto aplica planificación progresiva de sesión 04, p. 16, y sesión 06, p. 10; no exige adivinar todas las tareas futuras.

La referencia aprobada registra compromisos y autorización; el forecast muestra la mejor previsión actual. Hoy los dos son propuestas académicas: no hay baseline empresarial aprobada ni avance real. En ejecución, un forecast tardío se comunica con causa/impacto; cambiarlo no autoriza por sí solo cambiar el compromiso. PM integra costo/fecha/beneficio, PO reordena dentro de límites y sponsor/comité decide cambios mayores.

## Tres señales de flujo propuestas

Según sesión 06, pp. 11 a 17, conectar foro semanal de 02 con estas señales, sin inventar mediciones:

| Señal | Definición propuesta | Decisión que ayuda a tomar |
| --- | --- | --- |
| Throughput | Ítems terminados/aceptados por semana y tipo; para rollout, tiendas plenamente aceptadas por semana | Contrastar ritmo con altas pendientes y revisar olas. No mezclar tiendas, historias e interfaces ni sumar puntos de equipos. |
| Tiempo de ciclo | Tiempo desde inicio hasta aceptación, por tipo de ítem o habilitación de tienda | Revisar dispersión/esperas y actualizar rangos cuando exista histórico suficiente. |
| WIP y antigüedad/bloqueos | Ítems iniciados sin terminar, tiempo abiertos/bloqueados, causa y responsable | Resolver restricción dominante y limitar nuevos inicios según especialidad/capacidad; no ocultar QA o revisión como terminados. |

29 altas/mes es ritmo requerido, no rendimiento observado. Los 104/120 equipo-sprints y olas tampoco acreditan por sí solos fecha o cobertura: revisar precedencias, calendario y carga por especialidad. Los límites WIP se acuerdan con capacidad disponible; no aplicar ley de Little o percentiles de esfuerzo como garantía de plazo.

## Cierre académico

Para el viernes 23: propuesta integrada, estimación recibida revisada con Rogelio, alcance/olas y recursos conciliados por Maverick, supuestos aceptados o corregidos, presentación/anexos y ensayo. Entrega/presentación documentada: sábado 24; confirmar hora/formato de carga en el aula. La pauta exige coherencia y defensa del conjunto, no siete archivos formateados obligatorios por inferencia.
