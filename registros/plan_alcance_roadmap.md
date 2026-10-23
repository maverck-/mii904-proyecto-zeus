# Desarrollo del alcance y roadmap de Maverick

**Propuesta académica completa para revisión, 23-10-2026.** Apoya los documentos [04](../trabajo/04_alcance_y_backlog.md) y [07](../trabajo/07_roadmap.md). Conserva las medias PERT, capacidad, presupuesto y tramos recibidos el 23. Las distribuciones, ventanas y mecanismos siguientes son supuestos nuevos de planificación; no provienen del profesor ni acreditan dotación, productividad o aprobación del grupo.

## Convención de calendario y autorización

Se usan 52 semanas de referencia y 26 sprints de dos semanas. Los meses siguientes son bloques relativos de planificación, no meses civiles de duración idéntica. Antes de ejecutar se convierten a fechas reales, feriados, turnos y fecha de Black Friday. No existe fecha empresarial de inicio en el corpus.

| Mes | Semanas de referencia | Resultado principal / condición |
| --- | --- | --- |
| M1 | 1 a 4 | G0: mandato, selección piloto, contratación por hitos, responsables y medición. |
| M2 | 5 a 8 | VT-01: interfaces/datos y recuperación representativos antes de exponer clientes. |
| M3 | 9 a 13 | Construcción integrada y base comparable; preparación de las diez tiendas. |
| M4 | 14 a 17 | Flujo mínimo aceptado al terminar semana 16; empieza uso y observación. |
| M5 | 18 a 22 | Completar cuatro semanas de observación, analizar y decidir G1 al cierre. |
| M6 | 23 a 26 | Olas O1/O2 y preparación de sitios/soporte siguientes. |
| M7 | 27 a 30 | Olas O3/O4, estabilización, VE-01 y congelamiento posterior a aceptación R2. |
| M8 | 31 a 35 | Campaña y continuidad; sprint 17 reservado para estabilización. |
| M9 | 36 a 39 | G2 al inicio de semana 36; habilitar evolución R3 después de autorización. |
| M10 | 40 a 43 | Devoluciones elegibles y ampliación de observabilidad aceptadas. |
| M11 | 44 a 48 | Medir devoluciones y ejecutar experimento autorizado, máximo cuatro semanas. |
| M12 | 49 a 52 | Evaluar experimento, objetivos, transferencia y cierre con responsables. |

Se proponen cinco equipos en sprints 1–5, seis en 6–15 y cuatro en 16–26. La reducción ocurre **antes de campaña**, desde semana 31; esa es la opción explícita para conservar la tabla recibida, pendiente de aceptar su cobertura de soporte. Si Operaciones exige seis equipos durante campaña, reestimar y autorizar el costo en vez de afirmar que ya está incluido.

Capacidad efectiva F1: 4 × 5 + 6 × 6 = 56 en sprints 2–11. F2: 4 × 6 = 24 en 12–15. F3: 10 × 4 = 40 en 16 y 18–26. Sprint 1 usa cinco equipos para arranque y sprint 17 cuatro para estabilización: están pagados, pero se excluyen de las 120 unidades efectivas. El trabajo reservado de esos dos sprints no se cuenta otra vez en la matriz de carga efectiva.

F3 se separa en campaña, con capacidad 6 (sprint 16 completo y primera semana del 18), y R3 después de G2, con capacidad 34 (segunda semana del 18 y sprints 19–26). Sprint 18 cruza M8/M9; no autoriza trabajo R3 durante su primera semana.

El calendario suma 129 equipo-sprints pagados. Con 26 periodos por 12 meses, son 59,5385 equipo-meses; a 14 MM se obtienen 833,5385 MM. Se propone conservar 840 como provisión redondeada, con diferencia 6,4615 MM dentro de COST-01. No son reserva nueva ni tarifa de 7 MM por cada sprint pagado. Rogelio debe revisar condiciones contractuales y flujo financiero; esta conciliación es una convención propuesta, no una cotización.

## Distribución de esfuerzo por etapa

Unidad: equipo-sprint de referencia. F1 incluye R0/R1; F2 expansión y preparación; campaña excluye la estabilización ya reservada del sprint 17; R3 comienza tras G2. Los cuatro decimales conservan medias y sumas, no precisión observada. La descomposición supone cortes funcionales separables que Tecnología debe validar: todo control imprescindible del flujo que se abre debe estar terminado, aunque la épica continúe para otras interfaces.

| Épica | F1: R0/R1 | F2: R2 | Campaña M8 | R3 tras G2 | Total PERT |
| --- | ---: | ---: | ---: | ---: | ---: |
| E1 | 14,6667 | 0,0000 | 0,0000 | 0,0000 | 14,6667 |
| E2 | 9,0000 | 3,0000 | 1,0000 | 4,0000 | 17,0000 |
| E3 | 8,0000 | 3,0000 | 1,0000 | 3,0000 | 15,0000 |
| E4 | 4,5333 | 4,0000 | 0,5000 | 0,3000 | 9,3333 |
| E5 | 4,0000 | 4,0000 | 0,5000 | 0,0000 | 8,5000 |
| E6 | 2,0000 | 1,5000 | 1,0000 | 1,6667 | 6,1667 |
| E7 | 0,5000 | 4,0000 | 0,6667 | 0,0000 | 5,1667 |
| E8a | 3,0000 | 0,0000 | 0,0000 | 0,0000 | 3,0000 |
| E8b | 0,0000 | 0,0000 | 0,0000 | 4,0000 | 4,0000 |
| E9 | 0,0000 | 0,0000 | 0,0000 | 9,5000 | 9,5000 |
| E10 | 0,0000 | 0,0000 | 0,0000 | 5,3333 | 5,3333 |
| E11 | 2,0000 | 3,5000 | 0,3333 | 0,5000 | 6,3333 |
| Total | 47,7000 | 23,0000 | 5,0000 | 28,3000 | 104,0000 |

Las cargas F1/F2/F3 son exactamente 47,7/23/33,3 antes del redondeo de filas. Campaña usa 5/6 = 83,33%; R3 usa 28,3/34 = 83,24%. R2 mantiene 23/24 = 95,83%. Estas holguras agregadas no demuestran disponibilidad por especialidad ni financian automáticamente trabajo adicional.

### Primera salida usable antes de medir

No se supone que las 47,7 unidades estén terminadas al inicio de M4. Se propone un corte mínimo de 36 hasta el fin del sprint 8, semana 16, contra capacidad efectiva acumulada 38: 94,74% de uso. Las 11,7 restantes se distribuyen en sprints 9–11, con capacidad 18, para completar cobertura, estabilizar y preparar expansión. Es un punto exigente del plan y debe contrastarse con Tecnología antes de comprometerlo.

| Épica con carga F1 | Hasta primera salida, semana 16 | Después de salida, hasta G1 |
| --- | ---: | ---: |
| E1 | 11,0000 | 3,6667 |
| E2 | 7,0000 | 2,0000 |
| E3 | 6,5000 | 1,5000 |
| E4 | 3,5000 | 1,0333 |
| E5 | 3,0000 | 1,0000 |
| E6 | 1,5000 | 0,5000 |
| E7 | 0,0000 | 0,5000 |
| E8a | 2,0000 | 1,0000 |
| E11 | 1,5000 | 0,5000 |
| Total | 36,0000 | 11,7000 |

El corte de 36 debe incluir el flujo real completo en diez tiendas: disponibilidad/reserva, pedido/conciliación, preparación/retiro, permisos, alertas atendidas y reversión. No basta cumplir una suma de esfuerzo. La parte posterior solo amplía o mejora un flujo que ya cumple su aceptación. Si el corte mínimo no cabe, revisar viabilidad/capacidad de inmediato; no esperar G1 ni reducir controles.

Base de cuatro semanas propuesta en semanas 9–12; uso comparable en 17–20; análisis hasta semana 22. Un piso de 1.000 pedidos por fase en 28 días calendario equivale a unos 35,7 diarios entre diez tiendas; confirmar horarios y volumen elegible. Es demanda requerida para ese piso, no volumen observado ni garantía estadística. Si no hay muestra comparable, reportar resultado inconcluso y revisar la decisión de expansión.

## Roles que deben confirmar dedicación

| Función empresarial propuesta | Trabajo / periodo | Fuente de capacidad por conciliar |
| --- | --- | --- |
| Tecnología/integración y proveedor WMS | Datos, interfaces, reservas, conciliación y recuperación; desde R0 y cada ola | E1/E2/E3 y COST-01; cambios específicos del proveedor en COST-03, sin duplicar horas. |
| PO e-commerce y representante de tiendas | Criterios, prioridades y aceptación funcional; disponibles desde M1 | Dedicación empresarial explícita entre COST-01/COST-07, según roles y frontera de costo. |
| QA, seguridad y operación técnica | Pruebas, controles, alertas, carga y atención; antes de cada exposición | E6/E7/E8a; separar pentest externo COST-05 y herramientas COST-04. |
| Habilitación local/remota | Tres células de dos funciones durante treinta días de olas | Dedicación dentro de E11 y COST-01/COST-06; no sumar nuevas brigadas. |
| Personal y gerencia de tienda/CD | Preparación de datos, turnos, formación y aceptación del sitio | Costo y reemplazo de turnos dentro de COST-06 o aporte interno declarado; confirmar antes de G1. |
| PM/Arquitectura/Finanzas y facilitación | Dependencias, forecast, autorización y acompañamiento | COST-07 o dedicación ya incluida en equipos; una persona no se cobra en ambos. |

La tabla asigna funciones y ventanas, sin inventar nombres empresariales ni FTE disponibles. La revisión de Rogelio debe comprobar carga por especialidad y fronteras de costo. Esa validación no se sustituye con el promedio de seis personas por equipo.

## Dimensionamiento propuesto de las 58 altas

En los cuarenta días hábiles de referencia de M6/M7 se destinan treinta a altas y diez a corrección/VE-01. Se proponen tres células, cada una con una función técnica remota y una de habilitación operativa. Un sitio consume en promedio un día de célula, es decir, dos persona-días. Es hipótesis a calibrar con las diez tiendas piloto; viaje, turnos, CD y configuración especial pueden invalidarla.

| Parámetro | Valor propuesto | Uso |
| --- | ---: | --- |
| CEL-01 | 58 | Tiendas adicionales. |
| CEL-02 | 3 | Células, sin contratación adicional automática. |
| CEL-03 | 2 | Personas/funciones por célula. |
| CEL-04 | 30 | Días hábiles de habilitación. |
| CEL-05 | 0,75 | Disponibilidad efectiva supuesta. |
| CEL-06 | 1 | Días de célula por tienda. |
| CEL-07 | 3,5 | Equipo-sprints de E11 asignados a R2. |
| CEL-08 | 6 | Personas por equipo de referencia. |
| CEL-09 | 10 | Días hábiles por sprint de referencia. |

Requerimiento: 58 × 2 × 1 = 116 persona-días efectivos. Disponibilidad: 3 × 2 × 30 × 0,75 = 135; diferencia 19 para reintentos/aceptación. La dedicación bruta de células es 180 persona-días y cabe en 3,5 × 6 × 10 = 210 de E11/R2; los 30 brutos restantes cubren preparación/formación transversal. No sumar 210 y 180: el segundo es parte del primero. Estas funciones deben existir en la dotación o en COST-06 con frontera explícita; no son recursos demostrados por la operación aritmética.

| Tiempo medio por tienda | Días de célula requeridos | Días hábiles de altas necesarios | Decisión frente a ventana de 30 |
| --- | ---: | ---: | --- |
| 1 día | 58 | 26 | Cabe bajo supuestos, sujeto a precedencias y disponibilidad. |
| 1,5 días | 87 | 39 | Consume nueve días adicionales y casi todo el colchón de preparación; escalar. |
| 2 días | 116 | 52 | No cabe en M6/M7 con este mecanismo; revisar capacidad/cobertura/fecha. |

No trasladar al proyecto la geografía o tiempos de viaje que el enunciado no informa. Agrupar sitios por interfaz/CD y soporte; abrir un CD adicional exige su propia aceptación antes de la ola. Si el piloto desmiente el rendimiento, actualizar olas y decisión en G1 sin prometer 68 por suma de tiendas.

## Estado para integrar y defender

El contenido de Maverick queda desarrollado: frontera/catálogo, backlog/EDT, aceptación, releases, calendario relativo, dependencia, olas, capacidad propuesta y respuestas a desvíos. Falta revisión colectiva del alcance y contraste de Rogelio sobre especialidades, precios/contratos y flujo por tramo. La fecha de carga y el formato final siguen sujetos al aula. No se declara ejecución, financiación o aprobación empresarial.
