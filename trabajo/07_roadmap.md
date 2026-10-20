# 7. Roadmap y planificación

**ESC-01: plan hipotético desarrollado, pendiente de revisión grupal.** Los meses son relativos al inicio empresarial; el 24 de octubre es entrega académica. Hechos: valor dentro de M5, Black Friday aproximadamente M8, horizonte M12 (enunciado, p. 5). Piloto/cobertura y ventanas de evidencia son SUP-03/SUP-04/SUP-05.

## Releases, dependencias y evidencia

| Release | Ventana propuesta | Capacidades | Cobertura SUP-05 | Resultado y decisión |
| --- | --- | --- | --- | --- |
| R0 | M1 a M2 | CAP-01 + inicio CAP-05/CAP-06 | Sitios y datos representativos | Base por cohorte, prueba ERP/WMS, controles, capacidad y forecast. G1 autoriza piloto o revisa. No acredita todavía valor comercial. |
| R1 | Construcción M2 a M4; evaluación hasta M5 | CAP-02/CAP-03/CAP-04 y transversales | 5 tiendas, 1 CD y familias acotadas | Pedidos reales desde M4; cuatro semanas de medición hasta M5. KPI-01 <4%, KPI-02 ≥96%, KPI-03 <4 h, sujetos a base comparable y sin deterioro. |
| R2 | M5 a M7, tras G2 | CAP-07 + estabilización y transversales | Hasta 20 tiendas en total | Ampliación por evidencia y capacidad; prueba de carga/recuperación y soporte antes de M8. |
| Evento | Aproximadamente M8 | Cobertura R2 aceptada y transversales | Cobertura segura ya aceptada | Proteger operación y promesas, monitoreo y respuesta. No forzar nueva funcionalidad de alto riesgo. |
| R3 | Diseño M6/M7; despliegue M9 a M11 | CAP-08 + expansión autorizada | Hasta 35 tiendas en total | Devolución elegible y nueva cobertura con reglas, costos y capacidad aceptadas; revisar evidencia del evento. |
| R4 | M11 a M12 | Aceptación y transición | Cobertura efectivamente aprobada | KPI-01 <2%, KPI-02 ≥98%, KPI-03 <3 h propuestos para cobertura; servicio/beneficios pendientes con dueño. |

La cobertura es un tope propuesto condicionado, no compromiso automático ni suma de 5+20+35. No se garantiza cubrir 68 tiendas ni 3 CD. La devolución tiene aceptación propia en CAP-08 y no se usa para atribuir todo el beneficio corporativo al proyecto.

## Gates y autoridades

| Gate | Momento | Evidencia / decisión | Autoridad propuesta |
| --- | --- | --- | --- |
| G0 | Inicio | Aceptar hipótesis, límites, responsables, escenario y tramo inicial hasta 100 MM dentro del sobre | Sponsor con Finanzas y responsables |
| G1 | Fin M2 | Interfaces/datos viables, base, volumen, capacidad de tiendas, controles y costo a término; continuar, cambiar o parar | Sponsor/comité, evidencia de Tecnología/Operaciones/Finanzas/CISO |
| G2 | Fin M5 | Uso y beneficio con conteos/definiciones; guardrails; decidir ampliar, corregir o detener expansión | Sponsor/comité y dueños de beneficios |
| G3 | Fin M7 | Capacidad de campaña, operación, soporte y reversión aceptadas | Operaciones/Tecnología/CISO; sponsor decide cobertura |
| G4 | M9 | Datos de M8, estabilidad, riesgo y forecast sostienen evolución | Sponsor/comité y negocio |
| G5 | Fin M12 | Entregables, resultados, costos y transición; beneficios aún pendientes con dueño y fecha | Sponsor y responsables de servicio/beneficio |

No escalar por cumplir calendario cuando falta evidencia. Si G2 solo acredita output técnico o no hay volumen evaluable, registrar que el requisito de valor M5 no se ha demostrado. La base del caso y las metas piloto deben compararse correctamente antes de aceptar.

## Precedencias y plan cercano

CAP-01 reduce incertidumbre; CAP-05/CAP-06 trabajan en paralelo desde inicio. Inventario/reserva y pedidos requieren contratos de interfaz antes de paralelizar. El flujo C&C requiere ambos y capacidad local. Expansión requiere evidencia del piloto; la preparación del evento requiere capacidad y reversión; devolución requiere estados y reglas Comercial/Finanzas.

Detalle propuesto para M1/M2:

| Ventana | Trabajo y evidencia esperada |
| --- | --- |
| M1, primera mitad | Selección de piloto, responsables, definición KPI/base y acceso proveedor/datos. |
| M1, segunda mitad | Prueba representativa de contratos/stock, mapa de excepciones y capacidad física del proceso. |
| M2, primera mitad | Concurrencia/recuperación, restricciones de seguridad y primeras validaciones con tiendas. |
| M2, segunda mitad | Alcance mínimo refinado, rangos/capacidad revisados y gate G1. |

Estas son actividades a planificar para la empresa ficticia; no pruebas realizadas. Especialistas/proveedor pueden limitar el paralelismo, SUP-01/SUP-02. No se presenta una ruta CPM validada sin red detallada y duración estimada de actividades.

## Qué haría cambiar el plan

- API no viable o WMS retrasado: revisar integración, cobertura y costo; si M5 deja de ser posible, escalar y revisar B.
- Stock/adopción insuficientes: priorizar corrección del proceso y reducir exposición; no sumar tiendas para aparentar avance.
- Forecast >1.350: revisar sobre antes de comprometer; >1.500 sin reducción viable: no autorizar escala.
- Evento adelantado: conservar cobertura estable disponible y reordenar expansión.
- Riesgo crítico o interrupción material: pausar rollout, activar recuperación y no liberar por presión comercial.

Todo cambio actualiza [supuestos](../registros/acuerdos_y_supuestos.md), [riesgos](../registros/riesgos.md), alcance, costos y beneficios. La validación académica comprueba coherencia y defensa; no transforma estas ventanas en resultados operacionales.
