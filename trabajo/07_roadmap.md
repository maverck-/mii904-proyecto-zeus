# 7. Roadmap y planificación

**Responsable: Maverick. ESC-02, propuesta desarrollada al 23-10-2026 para revisión del equipo.** Meses relativos al inicio empresarial. La entrega académica del 24 de octubre es distinta de M12. Hechos: valor dentro de los primeros cinco meses, Black Friday aproximadamente M8 y horizonte 12 meses (enunciado, p. 5). El [plan de apoyo](../registros/plan_alcance_roadmap.md) contiene calendario de referencia, matriz de esfuerzo y dimensionamiento; sus cantidades nuevas son supuestos explícitos.

## Releases y evidencia

| Release | Ventana propuesta | Capacidades | Cobertura propuesta | Evidencia / condición |
| --- | --- | --- | --- | --- |
| R0 | M1/M2 | CAP-01 + inicio CAP-05/CAP-06 | Datos y sitios representativos | Base por cohorte, arquitectura, OMS por hitos y prueba ERP/WMS; VT-01/M2. Aún no acredita valor comercial. |
| R1 | Construir M2/M4; primera salida al finalizar la semana 16; observar semanas 17–20 y decidir al cierre M5 | CAP-02/CAP-03/CAP-04 y transversales | 10 tiendas, un CD y dos familias como hipótesis de diseño | Medir beneficio frente a base comparable; umbrales SUP-16 para revisión; no basta instalación; G1/M5. |
| R2 | Tras G1, expansión M6/M7 | CAP-07 y transversales | Objetivo 68 tiendas, hasta tres CD, mismas dos familias | Cada ola con datos, dotación, controles y soporte; VE-01/M7. No forzar altas para completar la cifra. |
| Campaña | Aproximadamente M8, fecha por confirmar | Cobertura aceptada y transversales | Solo sitios operables | Carga representativa, monitoreo, respuesta, reversión y promesas protegidas; disponibilidad con ventana acordada. |
| R3 | Tras G2/M9: devoluciones/centralización en M9/M10; medición y experimento M11; cierre M12 | CAP-08/CAP-09 + ampliar CAP-05 | Devoluciones de compras web elegibles; experimento de 3 a 5 tiendas, máximo cuatro semanas/300 pedidos | KPI-04 ≥85% propuesto; reglas y límites de 04; financiación/exposición autorizadas antes de iniciar. |

Observabilidad mínima, seguridad, soporte y formación se incorporan desde R1 y se sostienen en todas las olas. R3 amplía centralización/cobertura. El experimento no compromete Ship-from-store nacional. El [avance del 23](../insumos/avance_equipo_2026-10-23.md) aporta WSJF y estimación con prioridad. El catálogo, la medición y las olas son hipótesis de diseño por ratificar; el esfuerzo de habilitación se integra en E11.

## Calendario de referencia y primera entrega

Se propone una convención de 52 semanas/26 sprints: M1–M5 cubren semanas 1–22; M6/M7, 23–30; M8, 31–35; M9–M12, 36–52. Es una distribución de planificación, no fechas civiles confirmadas. G0 ocurre en M1; VT-01 al finalizar la semana 8; G1 al finalizar la semana 22; VE-01 al finalizar la semana 30 y G2 al inicio de la semana 36. Confirmar feriados/turnos y fecha externa antes de fijar compromisos.

Para primera salida al terminar semana 16 se asignan 36 equipo-sprints a un flujo mínimo completo contra 38 disponibles. Uso 94,74%; el sexto equipo arranca en sprint 5 y produce desde el 6, con disponibilidad desde semana 9. Se resuelve la rampa dentro de 840 MM sin colchón de redondeo. Las 11,7 unidades restantes de F1 completan cobertura/estabilización hasta G1. El [desglose por épica](../registros/plan_alcance_roadmap.md) separa ambas partes: solo puede diferirse trabajo que no sea necesario para aceptar el flujo expuesto.

Base comparable propuesta: semanas 9–12; uso observado: 17–20; análisis y G1 hasta semana 22. SUP-16 propone mejora relativa de 20% en cancelación y 25% en preparación, adopción >80% por tienda y evidencia suficiente. Si el flujo usable se retrasa, recalcular la ventana de evidencia antes de mantener M5; no etiquetar una demo como valor.

## Olas propuestas para revisar capacidad

Las cuatro olas desarrollan la meta condicionada 68/M7. Cuatro células ofrecen 150 persona-días efectivos para 145 de habilitación/acompañamiento; actividad agregada 25 jornadas más diez de preparación cabe en cuarenta. Las 25 jornadas se distribuyen dentro de treinta de olas, con cinco de margen para viajes/relevo/espera. E11/R2 aporta 210 brutos y COST-06 veinte de campo, con preparación preservada. G1 ratifica recursos, sitios y cobertura sobre el mecanismo ya definido.

| Ola | Ventana propuesta | Tiendas adicionales | Total acumulado | Condición previa |
| --- | --- | ---: | ---: | --- |
| Piloto | M4/M5 | 10 | 10 | VT-01, operación/medición/soporte aceptados. |
| O1 | Días hábiles 1 a 8 de M6/M7 | 15 | 25 | G1, células/horas/stock disponibles y CD correspondiente aceptado. |
| O2 | Días 9 a 16 | 15 | 40 | Estabilidad O1, capacidad y costo actualizado. |
| O3 | Días 17 a 23 | 14 | 54 | Estabilidad O2 y pruebas/carga según expansión. |
| O4 | Días 24 a 30 | 14 | 68 | Estabilidad O3 y tiempo para VE-01/correcciones antes de campaña. |

Se proponen treinta días hábiles de altas y diez posteriores de estabilización/carga/VE-01 dentro de los cuarenta de referencia de M6/M7. Cada ola exige aceptación por sitio según 04 y revisión de estabilidad antes de la siguiente. Un sitio fallido no se cuenta como habilitado; una aceptación parcial actualiza la cobertura real y el forecast.

La entrada a cada ola debe contrastar dos capacidades distintas: habilitación del sitio y operación diaria por turno después de abrir. Gerencias de tienda y Logística presentan dotación, carga habitual, dedicación al nuevo flujo y disponibilidad WMS/CD, según 04. Una célula capaz de instalar/configurar no demuestra que la tienda absorba preparación, retiro y excepciones. Sin esa evidencia, Operaciones no acepta el alta y PM eleva el efecto en cobertura/fecha; no se presume sobretiempo para sostener el plan.

La [precisión logística de alcance](04_alcance_y_backlog.md) añade al control existente mapa de esperas/movimientos, responsabilidades WMS/OMS, reserva simple, ventana fija de retiro y acompañamiento intensivo tras apertura. Cupos dinámicos y punto alternativo automático permanecen fuera de la base estimada. R0/VT-01 prueba la cadena física/digital con Logística; R1 calibra tiempos y dedicaciones; cada ola exige stock conciliado y cobertura de atención local/remota hasta salida operativa aceptada. No liberar una célula al siguiente sitio suponiendo que el anterior dejó de necesitar soporte. Revisar solapamiento y costo en E11/COST-06 antes de ratificar el ritmo; si no caben, ajustar olas/cobertura con la autoridad existente.

Mecanismo: cuatro células de dos funciones, 25 jornadas equivalentes y disponibilidad efectiva 75%. Demanda 116 de habilitación más 29 de acompañamiento frente a 150 efectivos. Los 230 brutos de células/preparación se financian con 210 de E11 y veinte de campo en COST-06; viajes tienen bolsa propuesta de diez MM dentro de esa categoría. Calibrar con piloto y ratificar perfiles, relevo y aceptación de cada CD.

Si habilitar cada tienda demanda 1,5 días de célula, con acompañamiento se requieren 34 jornadas de actividad y diez de preparación, total 44; con dos días se requieren 54 en total. Ambos exceden cuarenta. G1 debe resolver refuerzo autorizado, secuencia o cobertura; no consumir silenciosamente la preparación de campaña. El [dimensionamiento y sensibilidad](../registros/plan_alcance_roadmap.md) explicitan estas operaciones.

## Capacidad y financiación recibidas del equipo

R0/R1 propone capacidad 56/carga 47,7; R2 24/23; campaña y R3 40/33,3 equipo-sprints. Total 120/104. R2 usa 95,83% y R1/R2 conjunto 88,375%; el promedio no elimina el pico. La matriz de apoyo asigna cada épica sin modificar su PERT y separa campaña 5 de R3 28,3. También identifica funciones y ventanas; falta contrastar dedicación real por especialidad con Rogelio.

Financiación recibida: G0 675, G1 345 y G2 310 MM, más reserva 170, marco total 1.500. M8 pertenece a tramo 2 y protege campaña; R3 se autoriza desde G2/M9. La opción propuesta conserva seis equipos en sprints 5–15, con arranque del sexto en el 5 y cuatro desde 16, antes de campaña. F3 reserva capacidad 6 para campaña y 34 para R3 posterior a G2; sprint 17 está pagado y dedicado a estabilización, fuera de las 120 unidades efectivas. Rogelio debe revisar contratos y costo mensual: no se declara aprobada esa reducción ni cobertura de soporte.

Si no se dispone del sexto equipo, las opciones son reforzar capacidad con autorización de uso de reserva o priorizar tiendas de mayor venta y completar después de campaña. Es una contingencia que modifica cobertura/plazo: sponsor/comité debe decidirla y actualizar Charter/beneficios; es una contingencia frente a la meta condicionada 68/M7.

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

Para compatibilizar despliegue R2 y protección de campaña, se propone iniciar el congelamiento después de aceptar R2 y superar VE-01 dentro de M7, hasta terminar Black Friday aproximadamente en M8. Las fechas exactas dependen del calendario confirmado. Durante esa ventana no se despliegan funcionalidades ordinarias nuevas en producción; correcciones críticas de seguridad o continuidad requieren evaluación y autorización de Operaciones/Tecnología/CISO, con escalamiento al sponsor si cambian compromisos. La regla requiere ratificación antes de fijar compromisos.

Continúan monitoreo, soporte y estabilización con dotación prevista. El análisis o la preparación en ambientes no productivos solo usa capacidad y gasto autorizados; no convierte M8 en un release R3 ni anticipa financiación de G2. Si R2 no se acepta a tiempo, escalar cobertura, fecha y costo: no superponer automáticamente despliegues ordinarios con el congelamiento para conservar la cifra 68/M7.

### Operación y soporte por etapa

El modelo de tres niveles de [04](04_alcance_y_backlog.md) acompaña cada etapa. El primer nivel crece con las tiendas activas; la guardia de plataforma se mantiene y se refuerza en campaña.

| Etapa | Soporte | Evidencia antes de avanzar | Responsable |
| --- | --- | --- | --- |
| R0, M1 y M2 | Definir dueño del servicio, niveles, guiones, procedimientos operativos y acuerdos de nivel de servicio | Modelo aprobado y herramientas de alertas e incidentes listas en VT-01 | Tecnología con Operaciones |
| R1, piloto | Mesa con guiones de ZEUS, referente por turno en las 10 tiendas, soporte de aplicación y guardia | Mesa lista antes de la semana 16; parámetros de incidentes medidos en semanas 17 a 20 | Dueño del servicio |
| R2, olas | Referentes formados por ola y mesa ajustada según la regla de dimensionamiento | Soporte aceptado en cada sitio antes de contarlo como alta | Dueño del servicio con Operaciones |
| Campaña, M8 | Guardia reforzada y sala de seguimiento desde VE-01 hasta el fin de Black Friday | Prueba de respuesta y recuperación en VE-01 | Tecnología, Operaciones y CISO |
| R3 y cierre | Backlog de mejoras desde problemas recurrentes y traspaso a un equipo estable | Acuerdos de nivel de servicio, responsables y presupuesto recurrente definidos en M12 | Sponsor y dueño del servicio |

## Dependencias y acciones

Cadena que condiciona M5: acceso y viabilidad → inventario/reservas y pedidos → C&C usable → ventana de evidencia. Parte de integración/pedidos puede solaparse una vez acordados contratos y capacidad. No es una ruta crítica CPM calculada: faltan duraciones detalladas, holguras y recursos.

| Punto de control | Evidencia mínima propuesta | Respuesta si no se cumple |
| --- | --- | --- |
| VT-01, semana 8 | Prueba representativa ERP/WMS/OMS con consistencia, conciliación y recuperación; responsables de interfaces disponibles | Reestimar B/integración y efecto en primera salida; elevar antes de comprometer piloto. |
| Primera salida, semana 16 | Flujo completo aceptado por Tecnología/CISO/Operaciones en diez tiendas; base, soporte y medición disponibles | No exponer flujo incompleto; corregir y recalcular evidencia/fecha/costo. |
| G1, semana 22 | Cuatro semanas de uso comparable, adopción/mejora y forecast; recursos y costo de olas revisados | Resultado inconcluso o sin mejora: investigar y condicionar inversión/expansión, sin afirmar valor demostrado. |
| Cada ola y VE-01, hasta semana 30 | Sitios aceptados, pruebas representativas de carga/recuperación, respuesta y promesas sostenibles | Detener siguientes altas, preservar cobertura segura y elevar efecto sobre 68/M7. |
| G2, semana 36 | Campaña evaluada, forecast/financiación R3, reglas de devolución e hipótesis/techo de exposición del experimento | No iniciar capacidad condicionada sin autorización; priorizar objetivo de devolución frente a opcionales. |
| Cierre, semana 52 | Capacidades aceptadas, resultados/brechas KPI, soporte y transferencia, responsables de beneficios pendientes | Registrar pendientes y autoridad que los acepta; no simular que todo beneficio ya se realizó. |

Si el costo previsto supera el techo, revisar alcance y financiación antes de comprometer gasto. La falta de stock confiable o adopción suficiente obliga a corregir antes de ampliar, aunque el despliegue técnico esté terminado.

## Dependencias con evidencia y responsable

### Cadena de hitos y respuesta ante atraso

Cadena de referencia: compra OMS propuesta semana 4 → VT-01 semana 8 → salida usable semana 16 → observación semanas 17–20 → G1 semana 22 → olas autorizadas → VE-01 semana 30 → campaña aproximadamente semanas 31–35. Los intervalos incluyen trabajo y medición; no son holguras CPM calculadas. El análisis entre observación y G1 ocupa dos semanas; el escenario original reserva diez días hábiles para corrección/VE-01. La base de cuatro células requiere 35 jornadas agregadas de actividad/preparación dentro de cuarenta; los cinco días restantes se distribuyen dentro de las ventanas de olas. Esa diferencia es margen de planificación, no holgura CPM calculada.

Al atrasarse compra, integración o salida, recalcular la ventana de observación y el trabajo pendiente antes de ratificar M5. Como contingencia, evaluar CAP-02 sobre el canal existente para las mismas familias, con stock físico conciliado y medición de cancelaciones comparables. Publicar stock más rápido por sí solo no acredita valor. Su viabilidad, esfuerzo y resultado deben demostrarse; sustituir el piloto C&C por ese flujo exige decisión de sponsor/comité y actualización de Charter/beneficios. Si ninguna vía entrega valor en M5, declarar la incompatibilidad y revisar alternativa, no mover la restricción por redacción.

Las dependencias externas también requieren coordinación del proyecto (sesión 04, p. 9, y sesión 06, pp. 5 a 8). La tabla identifica responsable, evidencia y momento necesario.

| Dependencia | Coordinación responsable | Evidencia requerida | Momento necesario / efecto |
| --- | --- | --- | --- |
| ERP/WMS y condiciones de OMS | PM/Tecnología con proveedores | Contratos de datos, acceso, prueba representativa y soporte | VT-01/M2; si falla, afecta inventario/pedido y primera entrega. |
| Stock, turnos, espacio y formación por tienda/CD | Operaciones/Logística/gerencias de tienda | Preparación y aceptación del sitio, roles y soporte | Antes del piloto y de cada ola; condiciona altas. |
| CISO/Arquitectura y ambientes de prueba | Tecnología/CISO | Controles, integración, carga y recuperación | Cada release y VE-01; las revisiones consumen capacidad. |
| Regla de devolución y conciliación | Comercial/Finanzas/Operaciones | Elegibilidad, estados y aceptación | Antes de CAP-08/R3; no suponer que reglas aparecen al construir. |
| Operación y soporte del servicio | Dueño del servicio en Tecnología con Operaciones | Niveles, guiones, guardia y mesa preparados; regla de dimensionamiento calibrada | Antes del piloto; se amplía por ola, se refuerza en campaña y se traspasa en M12. |
| Dotación/contratos/costo por tramo | PM/Finanzas/proveedores | FTE por periodo, compromisos y forecast a término | G0, G1 y G2; cinco equipos nominales no garantizan especialistas disponibles. |

### Relaciones lógicas propuestas

La clase 4 pide construir fechas desde trabajo, dependencias y recursos ([parte 2](../transcripciones/clase-04_parte-2.md), 1:53:35 a 1:56:40). Estas relaciones precisan la secuencia de ZEUS; son propuesta de coordinación, sin duraciones ni holguras CPM calculadas. FS significa fin a inicio y SS, inicio a inicio. Una dependencia puede ser obligatoria y externa al mismo tiempo.

| Relación | Tipo / condición propuesta | Responsable y control |
| --- | --- | --- |
| Accesos, ambientes y contrato de datos → prueba VT-01 | FS obligatoria; incluye entregas de proveedor externas al equipo. | Tecnología/proveedores reservan disponibilidad y presentan evidencia antes de semana 8. |
| Inicio del desarrollo de adaptadores → inicio de configuración OMS | SS condicionado a contrato de interfaz ya acordado; permite solapar trabajo compatible, sin asumir integración ya aceptada. | Arquitectura/QA verifican versiones y pruebas; no esperar al final para descubrir incompatibilidades. |
| Flujo productivo aceptado → cuatro semanas de observación comparable → decisión G1 | FS obligatoria para declarar evidencia de valor; la base comparable se prepara antes. | Operaciones/dueños de beneficio confirman fecha de uso real; PM recalcula ventana si cambia. |
| Tienda aceptada y relevo de soporte → siguiente alta de su célula | FS por capacidad operativa; no bloquea otras células con recursos propios. | Operaciones asigna habilitación y acompañamiento sin doble dedicación. |
| Estabilidad de ola → siguiente ola | Regla discrecional de gobierno propuesta, con aceptación obligatoria por sitio. | Operaciones revisa evidencia; cambiar el solapamiento requiere recalcular carga/soporte y autorizarlo. |
| R2 aceptado y VE-01 → congelamiento / campaña | FS de aceptación; fecha de campaña es externa al desarrollo. | Tecnología/CISO/Operaciones confirman salida y soporte; escalar cobertura si no cabe. |

La disponibilidad del sexto equipo en semana 9 y de cuatro células de campo se comprueba antes de comprometer sus ventanas. Son recursos por función, no personas intercambiables. Si un especialista compartido limita la secuencia, PM ajusta asignación o forecast y comunica el impacto. No se solapan pruebas, aceptación o soporte solo para conservar una fecha.

## Horizonte, referencia y forecast

Mantener horizonte M12 por capacidades y gates; R1 con mayor detalle de interfaces, aceptación y recursos; trabajo cercano por sprint/flujo y preparación operativa. R2 conserva olas con validación de capacidad; R3 permanece por capacidades/hipótesis hasta acercarse G2. Esto aplica planificación progresiva de sesión 04, p. 16, y sesión 06, p. 10; no exige adivinar todas las tareas futuras.

La referencia aprobada registra compromisos y autorización; el forecast muestra la mejor previsión actual. En este ejercicio ambos son propuestas académicas: no existe una referencia empresarial aprobada ni avance ejecutado. En ejecución, un forecast tardío se comunica con causa/impacto; cambiarlo no autoriza por sí solo cambiar el compromiso. PM integra costo/fecha/beneficio, PO reordena dentro de límites y sponsor/comité decide cambios mayores.

En ejecución, PM conserva la versión de referencia, fecha, autoridad y motivo de cada cambio autorizado; publica por separado el forecast con fecha de corte y desviación. Una tarea terminada en desarrollo permanece abierta para el flujo hasta cumplir su aceptación, despliegue y transición aplicables. Una lista de tareas en verde no sustituye hitos aceptados ni beneficios medidos (clase 4, parte 2, 1:38:30 a 1:39:03 y 2:04:23 a 2:06:03).

## Tres señales de flujo propuestas

Según sesión 06, pp. 11 a 17, conectar foro semanal de 02 con estas señales, como mediciones futuras:

| Señal | Definición propuesta | Decisión que ayuda a tomar |
| --- | --- | --- |
| Throughput | Ítems terminados/aceptados por semana y tipo; para rollout, tiendas plenamente aceptadas por semana | Contrastar ritmo con altas pendientes y revisar olas. No mezclar tiendas, historias e interfaces ni sumar puntos de equipos. |
| Tiempo de ciclo | Tiempo desde inicio hasta aceptación, por tipo de ítem o habilitación de tienda | Revisar dispersión/esperas y actualizar rangos cuando exista histórico suficiente. |
| WIP y antigüedad/bloqueos | Ítems iniciados sin terminar, tiempo abiertos/bloqueados, causa y responsable | Resolver restricción dominante y limitar nuevos inicios según especialidad/capacidad; no ocultar QA o revisión como terminados. |

29 altas/mes es ritmo requerido, no rendimiento observado. Los 104/120 equipo-sprints y olas tampoco acreditan por sí solos fecha o cobertura: revisar precedencias, calendario y carga por especialidad. Los límites WIP se acuerdan con capacidad disponible; no aplicar ley de Little o percentiles de esfuerzo como garantía de plazo.

## Cierre académico

El [plan de cierre](../PLAN.md) organiza la revisión del viernes 23 y la entrega/presentación del sábado 24. La hora y el formato de carga siguen pendientes de confirmar en aula. Los siete Markdown organizan el contenido y no implican siete documentos formales obligatorios.
