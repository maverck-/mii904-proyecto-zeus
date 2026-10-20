# Riesgos iniciales y dependencias

**ESC-01: evaluación cualitativa propuesta, pendiente de revisión grupal.** Se describe una empresa ficticia; no hay pruebas ni incidentes realizados. Exposición alta/media es juicio de trabajo, sin probabilidades ni pérdidas calibradas. Ver supuestos SUP-01 a SUP-11.

| ID | Causa → riesgo → efecto | Exposición propuesta | Respuesta y evidencia | Dueño empresarial propuesto | Disparador / decisión |
| --- | --- | --- | --- | --- | --- |
| R-01 | API/legacy inciertos → integración inviable/tardía → falla M5 | Alta | Prueba representativa, contrato de datos, carga/recuperación G1 | Tecnología/proveedor WMS | Sin flujo viable en G1: revisar B, costo y alcance antes de seguir. |
| R-02 | Stock físico/datos inconsistentes → disponibilidad falsa → cancelaciones persisten | Alta | Reconciliación, auditoría, concurrencia y KPI-02 | Operaciones/Logística | Stock no confiable: corregir y no ampliar productos/tiendas. |
| R-03 | Dotación/adopción insuficientes → tareas no ejecutadas → preparación/atención deterioradas | Alta | Ensayo de proceso, formación, capacidad local y KPI-03 | Operaciones/Tiendas | Personal no preparado o carga no absorbible: limitar ola. |
| R-04 | Costos/licencias/soporte inciertos → sobrecosto → presión sobre techo | Alta | Rangos, TCO, forecast y revisión de reservas | Finanzas/dirección de proyecto | Forecast >1.350: decidir ajuste; >1.500 sin mitigación: no escalar. |
| R-05 | Despliegue en sistemas activos → interrupción/pedido perdido → daño de servicio | Alta | Salida gradual, idempotencia, monitoreo, reversión y soporte | Tecnología/Operaciones | Interrupción material/pérdida no conciliada: parar rollout y recuperar. |
| R-06 | Acceso/trazabilidad/datos mal controlados → exposición → daño o bloqueo | Alta | Controles desde diseño, pruebas y aceptación CISO | CISO/responsables de datos | Riesgo crítico abierto: bloquear liberación. |
| R-07 | Base/muestra incomparables → beneficio no demostrable → expansión sin evidencia | Media/alta | Definiciones, eventos, conteos y ventana desde M1 | Dueños de beneficio/analítica | G2 sin evidencia: no declarar valor M5 cumplido. |
| R-08 | Carga de campaña/dependencia tardía → capacidad insuficiente → falla M8 | Alta | Prueba de demanda representativa, cobertura estable, recuperación | Operaciones/Tecnología | G3 sin capacidad aceptada: limitar cobertura y diferir expansión. |

## Dependencias que deben tener acuerdo

- Proveedor WMS/ERP: acceso, contrato de datos, prueba, soporte y escalamiento para G1.
- Operaciones: calidad de stock, dotación, espacio y promesas por tienda antes de piloto/ola.
- Comercial/Finanzas: reglas de devolución, conciliación y aceptación antes de CAP-08.
- Tecnología/CISO: controles, carga, observabilidad, reversión y soporte para cada salida.
- Finanzas/proveedores: costo total, modalidad de licencia, consumo, impuestos y operación antes de comprometer contratos.

## Incertidumbre y respuesta

El riesgo identificado admite una respuesta; la ausencia de datos requiere aprender. La tasa de conflictos de reserva, capacidad real de API y tiempo de adopción no se han medido. Una prueba propuesta reduce esa incertidumbre y permite recalibrar exposición, no garantiza eliminarla.

Revisión semanal de bloqueos por dirección de proyecto y revisión mensual/gates del costo y beneficio por sponsor/comité. Son cadencias propuestas en 02. Registrar riesgo residual, responsable y cambio; toda variación de alcance/fecha/costo actualiza el resto de documentos. Seguridad, continuidad y calidad no se recortan para absorber sobrecosto.
