# Mapa de consulta para diseño y defensa de ZEUS

**Versión vigente, 23-10-2026.** Se conserva el nombre del archivo por compatibilidad con enlaces anteriores. La [pauta de construcción](pauta_construccion.md) contiene los únicos títulos, tiempos y composiciones vigentes. Este mapa sirve para revisar el argumento y localizar el respaldo; el texto hablado por lámina está en el [guion](guion.md).

La versión anterior quedó sustituida: sus tres células y el rango de costo que terminaba en 1.500 no describen la base actual. Las fuentes vigentes son los siete documentos de trabajo, la [base de ejecución](../registros/base_ejecucion.md) y los [aportes de clase 4](../registros/aportes_clase_04.md). Los cambios no significan aprobación del equipo o de la empresa ficticia.

## Lectura del argumento

| Bloque | Láminas de la pauta | Qué debe quedar claro | Respaldo |
| --- | --- | --- | --- |
| Recomendación y valor | 1–3 | B es una propuesta para comprobar valor; los síntomas del caso y los umbrales del piloto tienen poblaciones/estados distintos. | [01](../trabajo/01_diagnostico_y_business_case.md), anexo A. |
| Alternativa, enfoque y mandato | 4–6 | B resuelve la causa del problema, la complejidad de integración, dentro del techo; prácticas y derechos de decisión responden a tensiones concretas. | [01](../trabajo/01_diagnostico_y_business_case.md), [02](../trabajo/02_enfoque.md), [03](../trabajo/03_charter.md), anexos D/E. |
| Alcance y prioridades | 7–8 | R1 es reserva simple/ventana fija; un ratio alto no elimina dependencias ni controles. | [04](../trabajo/04_alcance_y_backlog.md), [05](../trabajo/05_priorizacion.md). |
| Recursos y calendario | 9–10 | La capacidad no certifica fechas; cuatro células y sexto equipo anticipado sostienen una meta condicionada. El estrés solo cabe con reducción/topes. | [06](../trabajo/06_estimacion.md), [07](../trabajo/07_roadmap.md), [base](../registros/base_ejecucion.md), anexos B/C. |
| Respuesta y autorización | 11–12 | La evidencia puede frenar escala/inversión; se solicita el primer tramo, con límites y autoridad para continuar. | [riesgos](../registros/riesgos.md), [03](../trabajo/03_charter.md), anexos B/D. |

## Formato del guion

El [guion](guion.md) indica por lámina la persona que habla y el texto exacto que debe decir. Las transiciones van dentro del texto hablado. Añadir únicamente una nota breve para preguntas cuando haga falta precisar un dato, un límite o una fuente. No agregar apartados de salida, instrucciones escénicas ni explicaciones sobre el propio guion por defecto.

Las filas siguientes son respaldo de contenido para preparar la defensa. No se copian completas al guion ni obligan a agregar notas a cada lámina. El reparto de expositores del guion es una propuesta hasta que el equipo acuerde los relevos.

## Preguntas que la presentación debe poder responder

| Pregunta | Criterio de respuesta y límite | Lámina / anexo |
| --- | --- | --- |
| ¿Por qué B frente a C? | El enunciado dice que cada nueva integración aumenta complejidad y dependencias (p. 3) y pide reducir las integraciones punto a punto (p. 5). B agrega una capa de APIs reutilizable sobre ERP y WMS; C resuelve el retiro con más conexiones sobre los mismos sistemas. El retorno se confirma en el piloto, porque el caso no informa volumen ni margen. | 4, E. |
| ¿Por qué híbrido? | WMS requiere hitos y pruebas; producto admite incrementos y feedback; dependencias se gestionan por flujo. Un bloqueo modifica forecast y puede exigir una decisión ejecutiva. | 5, D/C. |
| ¿Cómo se escala de 10 a 68? | Cuatro olas, cuatro células, habilitación y acompañamiento explícitos, campo adicional en COST-06 y calibración con piloto. La capacidad diaria de tiendas/CD se acepta aparte. Si el esfuerzo por sitio crece, revisar cobertura/fecha. | 10, C. |
| ¿El esfuerzo demuestra la fecha? | 104/120 es comparación aritmética. Corte piloto 36/38 y R2 23/24 requieren especialidades y dependencias disponibles; no hay CPM detallado ni probabilidad validada de fecha. | 9/10, B/C. |
| ¿Qué permite el sexto equipo anticipado? | Disponibilidad en semana 9, arranque en sprint 5 y producción desde el 6; 130 unidades pagadas, 120 efectivas y 840 MM exactos, sin colchón de redondeo. | 10, B/C. |
| ¿Qué ocurre si el costo llega a 1.668? | Diferir E10/E8b habilita cancelar un equipo tras G2; los topes OMS/WMS/cloud completan la respuesta hasta 1.497,0923. Sin esas condiciones, ajustar cobertura o arquitectura antes de superar el techo. No sumar ahorros por esfuerzo y por contrato dos veces. | 9, B. |
| ¿Qué pasa si falla WMS o el stock físico? | Corregir interfaz/conciliación y recalcular salida/observación; no exponer reservas no confiables ni declarar una demo como valor. VT-01 y aceptación operativa son evidencia para decidir. | 10/11, C/D. |
| ¿Cómo se demuestra valor M5? | Uso, mejora y operación aceptada, contra base y comparación concurrente; cuatro semanas/piso de pedidos no garantizan causalidad. Si falta comparación válida de C&C, ratificar otro resultado comparable antes del piloto. | 3, A. |
| ¿La logística ya demuestra retorno? | Es una hipótesis plausible; el cálculo usa volumen, margen, cobertura efectiva por pedidos y gasto incremental. Los estudios externos no dan el efecto local y la sensibilidad ilustrativa no es forecast. | 3/4/9, E. |
| ¿Por qué 85% en devolución frente a 90% estratégico? | El proyecto trata casos elegibles y la meta corporativa tiene otra población. Justificar cobertura y contribución; no presentar cinco puntos como brecha corporativa medida. | 7, A. |
| ¿Ship-from-store es opcional? | El experimento es condicionado y diferible, 3–5 tiendas, cuatro semanas/300 pedidos como límites propuestos y exposición monetaria autorizada en G2. Devolución sostiene KPI-04; no retirar todo R3 como si fuera prescindible. | 7/11, B. |
| ¿Quién opera y da soporte a ZEUS? | Dueño del servicio en Tecnología y tres niveles: referente por turno y mesa de ayuda, que crecen con las tiendas; soporte de aplicación de los equipos y del partner OMS; guardia de plataforma, que crece con los servicios críticos y se refuerza en campaña. Se financia con las categorías existentes; un refuerzo de mesa se mide en el piloto y lo autoriza G1. En M12 el servicio pasa a un equipo estable de operación y producto. | 6/10, C. |
| ¿Quién cambia una fecha? | PM actualiza/comunica forecast y opciones; sponsor/comité autoriza cambios de compromiso conforme al Charter. PO reordena dentro de límites; CISO/Operaciones bloquean una salida crítica/no operable. | 5/6/12, D. |
| ¿Qué pasa con 20% menos presupuesto? | Nuevo techo 1.200 MM. Reestimar B con menor cobertura, diferir opcionales y revisar contratos evitables y horizonte, sin tocar el núcleo; recortar tareas no ahorra caja automáticamente. Conservar controles y continuidad. | 4/9/12, B/E. |

Ante un cambio de condición: identificar objetivo/compromiso afectado, seguir dependencias, recalcular capacidad/costo/beneficio y presentar opciones con autoridad de decisión. El diseño debe facilitar encontrar el anexo correspondiente. Estas respuestas son criterios de defensa, no una locución ni párrafos para pegar en las láminas.

## Cierre de contenido antes de entregar

El equipo ratifica catálogo/CD, umbrales del piloto, devolución elegible, dotación y límites experimentales. Rogelio concilia capacidad por especialidad, categorías/tramos y fronteras con proveedores. El caso no trae datos de volumen/margen: mantener su efecto en la recomendación como incertidumbre explícita, sin fabricar resultados.

Las láminas están construidas con esas propuestas rotuladas y el guion está listo para ensayar. Los anexos A a E ya están en Figma como respaldo; D reúne las respuestas ante cambios de condición. Falta acordar relevos y ensayar 25 + 10. Confirmar hora/formato del aula y enviar la presentación al exponer, según clase 4.
