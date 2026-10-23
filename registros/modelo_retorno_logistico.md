# Modelo de valor y retorno logístico para ZEUS

**Propuesta de apoyo, 23-10-2026.** Complementa el Business Case con un mecanismo económico y sensibilidad. La [evidencia externa](../insumos/evidencia_logistica_y_valor.md) respalda explorar la relación logística/venta; sus porcentajes no se usan como parámetros. Los parámetros de sensibilidad son ilustrativos; el retorno se discute como volumen requerido, no como forecast de ventas. El enunciado prevalece.

## Qué se intenta explicar

Stock confiable y capacidad logística → promesa cumplible → menos cancelaciones y mejor experiencia → posible mejora de conversión/recompra → contribución económica, después de costos adicionales. El valor depende también de precio, mix, promociones, cobertura y sustitución entre canales. Logística, Comercial y Finanzas comparten el análisis; Tecnología aporta integración y medición.

Separar el tiempo desde confirmación a pedido listo (KPI-03) del tiempo hasta retiro/entrega y del trabajo activo del personal. Preparar en menos de tres horas no equivale a entregar a domicilio en tres horas ni demuestra ahorro de mano de obra. La oferta comercial debe respetar la capacidad del punto y la modalidad efectivamente incluida.

## Variables por periodo y cohorte comparable

| Variable | Significado / unidad | Obtención o supuesto |
| --- | --- | --- |
| S | Sesiones elegibles por mes en catálogo/zona cubiertos | Analítica del canal; no extrapolar a toda la compañía. |
| c0, c1 | Pedidos aceptados / sesiones elegibles, antes y después | Tasas con misma definición; c1 es escenario hasta medir. |
| q0, q1 | Cancelaciones por stock / pedidos aceptados | Base comparable local; 7,8% del caso es corporativo, no base piloto verificada. |
| m | Contribución por pedido completado, CLP/pedido | Después de mercadería, descuentos, comisiones y costos variables habituales, antes de nuevos gastos específicos de ZEUS; confirmar composición. |
| A | Gastos efectivamente evitados, CLP/mes | Ahorro de caja verificable y separado de m; capacidad liberada no es ahorro automático. |
| O | Gasto adicional recurrente de ZEUS, CLP/mes | Soporte, licencias, cloud, operación, transporte u otros incrementales no descontados en m. |
| I | Desembolso de implementación por periodo, CLP | Parte de presupuesto no incluida en O o m. Reconciliar categorías y financiación. |

Si quedan cancelaciones por otras causas, devoluciones o fraude, ajustar las tasas y la contribución para no llamarlas ventas netas realizadas. La recompra se incorpora solo con cohortes y horizonte propios, evitando contar de nuevo pedidos ya incluidos en S/c. Una mayor venta digital que desplaza una compra presencial requiere descontar la contribución perdida en ese canal.

## Cálculo sin duplicar pedidos

Para sesiones equivalentes S, pedidos aceptados base N0 = S × c0:

```text
Pedidos completados base = S × c0 × (1 − q0)
Pedidos completados del escenario = S × c1 × (1 − q1)
ΔQ = S × [c1 × (1 − q1) − c0 × (1 − q0)]

Descomposición equivalente:
Recuperación de pedidos base = N0 × (q0 − q1)
Pedidos adicionales completados = S × (c1 − c0) × (1 − q1)
ΔQ = recuperación + adicionales completados

Contribución incremental bruta = ΔQ × m
Beneficio operativo incremental = ΔQ × m + A − O
Flujo del proyecto en periodo t = ΔQt × mt + At − Ot − It
VAN = suma de flujos descontados al mismo periodo de la tasa
```

Las diferencias de conversión y cancelación no son dos porcentajes sumables de ventas. Si cambian las sesiones, usar S0/S1 y separar efectos de tráfico, campañas y cobertura. En M1–M12 aplicar la entrada progresiva de sitios y la demora hasta que cada beneficio aparece; no suponer doce meses de operación nacional desde el inicio.

Un ROI simple sobre un horizonte acordado puede expresar `(beneficios brutos acumulados − costos incrementales acumulados) / costos incrementales acumulados`. Debe mostrar horizonte, componentes y tratamiento de impuestos; no confundirlo con VAN. Payback requiere que el flujo acumulado recupere la inversión; si no ocurre, informar «no recuperada en el horizonte». No hay tasa de descuento ni flujos verificados para calcularlos como resultado de ZEUS.

## Volumen requerido y participación de las familias

Se reemplaza el ejemplo de sesiones/conversión por un umbral paramétrico. Definir por separado:

- `sP`: participación de las dos familias en pedidos digitales aceptados.
- `sC`: participación de esas familias en cancelaciones por stock.
- `Vd`: pedidos digitales aceptados mensuales en la población de referencia.
- `f_t`: fracción de pedidos de esas familias efectivamente expuestos al flujo/sitios cubiertos en el periodo t, entre cero y uno; se pondera por pedidos, no por número de tiendas.
- `q0f/q1f`: cancelación antes/después en familias y sitios cubiertos.

La recuperación por menor cancelación es `Vd × sP × f_t × (q0f − q1f)`, con tasas calculadas en la cohorte cubierta. Si Vd ya se limita a esa cohorte, f_t se fija en uno para evitar aplicar dos veces la cobertura. S en el cálculo anterior también representa sesiones de la cohorte cubierta; no se le descuenta nuevamente f_t. sC permite comprobar concentración del problema y conciliar conteos; no se multiplica de nuevo por sP. También se requiere margen por familia y costo de servir. El catálogo se elige combinando potencial económico y factibilidad física/digital.

Para recuperar implementación I en H meses de operación estable, con contribución m, ahorro A y recurrente adicional O, todos sin doble conteo:

```text
ΔQ requerido por mes = (I / H + O − A) / m
Equilibrio operativo = (O − A) / m
sP mínimo, si solo hay recuperación por cancelación =
    ΔQ requerido / [Vd × f_t × (q0f − q1f)]
```

Con f_t = 0 no existe recuperación por este flujo. Si sP mínimo supera uno o la participación real es menor, ese mecanismo resulta insuficiente bajo los parámetros. Conversión/recompra pueden aportar, pero requieren medición y población explícitas. El horizonte H se cuenta desde operación estable; incorporar por separado rampa, gastos previos, impuestos y descuento para evaluar el proyecto completo.

### Sensibilidad de recuperación, sin atribuirla a ZEUS

Supuestos exclusivamente ilustrativos: **I = 1.500 MM de implementación**, **O = 9 MM/mes**, **m = 8.000 CLP/pedido** y A = 0. I y O se suponen gastos distintos. Esta estructura todavía no corresponde a nuestro presupuesto mixto de 1.330 + 170.

| Horizonte desde estabilización | Pedidos adicionales completados requeridos por mes | Mínimo entero, redondeado hacia arriba |
| --- | ---: | ---: |
| Equilibrio operativo, sin recuperar I | 1125,00 | 1125 |
| Recuperar I en 36 meses | 6333,33 | 6334 |
| Recuperar I en 60 meses | 4250,00 | 4250 |

La operación correcta de 1.500 / 9,7456 arroja aproximadamente 153,92 meses **si** 1.500 fuera implementación separada y 9,7456 una contribución neta estable. En el ejemplo anterior esa contribución era inventada para sensibilidad y los 1.500 mezclan gastos del primer año. Por eso ese cociente no es el payback de ZEUS. El ejemplo tampoco demostraba viabilidad: su contribución era insuficiente para recuperar esa inversión hipotética en tres o cinco años.

El criterio de decisión es confrontar el volumen requerido con Vd, sP, sC, margen y capacidad de tiendas. Mientras esos parámetros sigan abiertos, la superioridad económica de B frente a C queda por justificar. Se conserva el escenario de beneficio nulo o negativo como posibilidad; los umbrales no autorizan asumir que habrá demanda suficiente.

## Cómo conciliarlo con 1.330 + 170 MM

El presupuesto vigente de 1.330 MM mezcla equipos, proveedores, licencias, cloud, adopción y gobierno durante doce meses; no se lo puede tratar íntegramente como I y restar otra vez las partidas que ya se registraron en O. Finanzas/Rogelio deben asignar cada gasto una sola vez por categoría/mes, como implementación u operación, según su naturaleza y momento de pago. Los tramos 675/345/310 son financiación propuesta, no beneficios ni ingresos operacionales.

Los 9 MM del ejemplo tampoco se agregan automáticamente a los 1.330. Si corresponden a gastos ya incluidos, forman parte de su distribución; si son nuevos costos, se actualizan estimación, reserva y asequibilidad antes de asumirlos. La reserva de 170 no es ingreso ni gasto ejecutado: modelar su consumo por escenario y verificar máximo 1.500. Los costos reales de operación posteriores a M12 pertenecen al horizonte económico que se elija, aunque excedan el horizonte de ejecución del proyecto.

## Evidencia y decisiones propuestas por etapa

| Momento | Trabajo / responsable empresarial propuesto | Decisión |
| --- | --- | --- |
| R0 / VT-01 | Logística/Tiendas mapean esperas, stock y movimientos WMS; R1 conserva reserva simple y ventana fija; Comercial define cohorte/promesa; Finanzas construye márgenes y costos | Mantener o reformular hipótesis antes de contratar o abrir exposición material. |
| Piloto / G1 | Comparar tiendas/cohortes elegibles; medir cancelación, preparación, promesa cumplida, uso y costo. Separar precio/promociones, mix y cobertura; informar evidencia insuficiente | Expandir, corregir o condicionar inversión; no trasladar automáticamente ventas de otro retailer. |
| Olas / VE-01 | Operaciones prueba capacidad por turno, acompañamiento y costo de servir, con stock/reservas conciliados | Abrir solo sitios aceptados; proteger campaña ante datos o capacidad insuficientes. |
| G2 / M12 | Revisar contribución, devoluciones, recompra observable, costos y forecast, con límites de atribución | Mantener, acotar, cambiar alternativa o detener compromisos futuros con impacto explícito. |

Promesa cumplida: pedidos elegibles entregados o listos para retiro dentro de la ventana comunicada / pedidos elegibles cuya ventana ya venció, conservando cancelaciones e incumplimientos en el seguimiento. Separar C&C y domicilio; acordar tratamiento de rechazo del cliente y fecha de retiro voluntario. Es una señal diagnóstica propuesta, no un séptimo KPI comprometido ni una sustitución del ≥95% estratégico de pedidos a tiempo.

La medición piloto ya prevista puede recoger estos datos sin crear un estudio académico separado. Un antes/después no prueba causalidad; si no existe comparación adecuada, presentar escenarios y asociación, con sus límites. La validación empresarial queda como actividad hipotética futura del caso.
