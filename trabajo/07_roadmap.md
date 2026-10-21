# 7. Roadmap y planificación

**Responsable indicado: Maverick. ESC-02, propuesta basada en el equipo.** Meses relativos al inicio empresarial. La entrega académica del 24 de octubre es distinta de M12. Hechos: valor dentro de los primeros cinco meses, Black Friday aproximadamente M8 y horizonte 12 meses (enunciado, p. 5).

## Releases y evidencia

| Release | Ventana propuesta | Capacidades | Cobertura propuesta | Evidencia / condición |
| --- | --- | --- | --- | --- |
| R0 | M1/M2 | CAP-01 + inicio CAP-05/CAP-06 | Datos y sitios representativos | Base por cohorte, arquitectura, OMS por hitos y prueba ERP/WMS; VT-01/M2. Aún no acredita valor comercial. |
| R1 | Construir M2/M4; usar en M4 y evaluar hasta M5 | CAP-02/CAP-03/CAP-04 y transversales | 10 tiendas piloto | Retiro real, adopción >80% propuesta, mejora frente a base comparable con suficiencia de evidencia fijada antes del piloto; G1/M5. |
| R2 | Tras G1, expansión M6/M7 | CAP-07 y transversales | Objetivo 68 tiendas totales, condicionado | Cada ola con datos, dotación, controles y soporte; VE-01/M7. No forzar altas para completar la cifra. |
| Campaña | Aproximadamente M8, fecha por confirmar | Cobertura aceptada y transversales | Solo sitios operables | Carga representativa, monitoreo, respuesta, reversión y promesas protegidas; disponibilidad con ventana acordada. |
| R3 | Preparar reglas antes; ejecutar/autorizar evolución tras G2/M9 y cerrar M12 | CAP-08/CAP-09 + ampliar CAP-05 | Devoluciones elegibles; experimento Ship-from-store acotado | KPI-04 ≥85% propuesto, aprendizaje experimental con límite; aceptación/traspaso y objetivos M12. |

Observabilidad mínima, seguridad, soporte y formación se incorporan desde R1 y se sostienen en todas las olas. R3 amplía centralización/cobertura. El experimento no compromete Ship-from-store nacional. Precisar CD/familias y tiendas experimentales antes de fijar costo.

## Olas propuestas para revisar capacidad

Se conserva la meta del equipo de 68/M7. Las cuatro olas son un complemento de planificación, **no un acuerdo ni una capacidad demostrada**.

| Ola | Ventana propuesta | Tiendas adicionales | Total acumulado | Condición previa |
| --- | --- | ---: | ---: | --- |
| Piloto | M4/M5 | 10 | 10 | VT-01, operación/medición/soporte aceptados. |
| O1 | Primera parte M6 | 15 | 25 | G1 y brigadas/horas/stock disponibles. |
| O2 | Segunda parte M6 | 15 | 40 | Estabilidad O1, capacidad y costo actualizado. |
| O3 | Primera parte M7 | 14 | 54 | Estabilidad O2 y pruebas/carga según expansión. |
| O4 | Segunda parte M7 | 14 | 68 | Estabilidad O3 y tiempo para VE-01/correcciones antes de campaña. |

58 altas en aproximadamente dos meses requieren justificar paralelismo, capacidad de tienda/proveedor y estabilización. Rogelio debe contrastarlas con esfuerzo/costo. Si las primeras olas consumen el margen de preparación, reducir cobertura o mover altas posteriores al evento y actualizar el compromiso; no desplazar seguridad/recuperación ni presentar 68 como logrado.

## Gates financieros y revisiones de salida

| ID | Momento | Evidencia / decisión | Autoridad propuesta |
| --- | --- | --- | --- |
| G0 | M1 | Arquitectura inicial, selección OMS y financiación escalonada; primer tramo debe cuantificarse | Comité/sponsor con Finanzas y Arquitectura. |
| VT-01 | Final M2 | Prueba de interfaces/datos, OMS, capacidad, controles y forecast antes de piloto | Tecnología/Arquitectura, CISO, Operaciones; PM escala desvíos al comité. |
| G1 | M5 | Evidencia de primera entrega de valor y decisión de expandir con costo/capacidad aceptados | Comité/sponsor y dueños de beneficio. |
| VE-01 | M7 | Cobertura segura, carga, recuperación, soporte y preparación de campaña; congelar cambios de alto riesgo | Operaciones/Tecnología/CISO y sponsor. |
| G2 | M9 | Revisar beneficios, campaña, forecast y financiación de devoluciones/experimento R3 | Comité/sponsor, Finanzas y dueños de beneficio. |
| Cierre | M12 | Aceptación, transferencia, costo y beneficios pendientes con responsables | Sponsor/Operaciones y dueños de beneficio. |

VT-01 y VE-01 son revisiones técnicas/operacionales adicionales a los gates del equipo. El contrato OMS de G0 requiere hitos de prueba/aceptación, para no asumir resueltas APIs/licencias antes de validar. Reglas de devoluciones pueden analizarse antes de M9, pero gasto/compromiso R3 requiere autorización y estimación.

## Dependencias y acciones

Cadena que condiciona M5: acceso y viabilidad → inventario/reservas y pedidos → C&C usable → ventana de evidencia. Parte de integración/pedidos puede solaparse una vez acordados contratos y capacidad. No es una ruta crítica CPM calculada: faltan duraciones detalladas, holguras y recursos.

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

29 altas/mes es ritmo requerido por 58 tiendas en dos meses, no rendimiento observado. Las olas y estas señales sostienen la hipótesis 68/M7 sin demostrarla anticipadamente. Límites WIP numéricos requieren capacidad de SUP-02; incorporar costo de apoyo adicional si se decide usarlo. No aplicar ley de Little ni probabilidades como garantía sin sus condiciones/datos.

## Cierre académico

Para el viernes 23: propuesta integrada, estimación cuantificada por Rogelio, alcance/olas revisados por Maverick, supuestos aceptados o corregidos, presentación/anexos y ensayo. Entrega/presentación documentada: sábado 24; confirmar hora/formato de carga en el aula. La pauta exige coherencia y defensa del conjunto, no siete archivos formateados obligatorios por inferencia.
