# 4. Alcance y backlog de capacidades

**ESC-01: borrador desarrollado con supuestos, pendiente de revisión del grupo.** Fuente de restricciones y capacidades candidatas: enunciado, pp. 4, 5 y 8. La cobertura se propone mediante SUP-05 y las metas mediante SUP-06; ninguna fila acredita ejecución.

## Fronteras y cobertura del escenario

Incluir inventario/reserva, pedidos trazables, integración necesaria, C&C, controles, métricas, adopción, continuidad y soporte. Proponer devoluciones elegibles y expansión posteriores, sujetas a evidencia y presupuesto. La referencia B no exige implementar todas las capacidades candidatas del enunciado.

Piloto: **5 tiendas, 1 CD y familias de productos acotadas**, SUP-05. Razón propuesta: limitar exposición y permitir observar diversidad de operación sin abrir todas las tiendas; no hay evidencia que demuestre que cinco es el tamaño óptimo. Selección por volumen, calidad de stock, capacidad local y condiciones de integración, validada hipotéticamente en G1. Operación desde M4 y evaluación hasta M5. Expansión total de hasta 20 tiendas en M7 y hasta 35 en M11; los totales no se suman. Más CD se incorporan solo con plan y costo acordados.

Excluir por el caso: reemplazo de ERP o WMS completo. Fuera del compromiso de ESC-01: motor de IA, data platform corporativa, Ship-from-store y despliegue de 68 tiendas. Datos operacionales mínimos e instrumentación sí se incluyen. Se posterga valor potencial a cambio de foco y menor exposición; revisar si se demuestra una dependencia real o un caso económico adicional.

Interfaces a coordinar: ERP, WMS, POS, e-commerce, pagos, logística y CRM en cuanto afecten el flujo. Cada interfaz necesita dueño, contrato de datos, tratamiento de fallos, prueba y soporte. Su sistema propietario puede seguir fuera del reemplazo.

## Backlog trazable

CAP-xx identifica una capacidad/épica. Los releases se proponen en 07; refinamiento y aceptación final requieren revisión del grupo y, en ejecución hipotética, de responsables empresariales.

| ID | Capacidad | Dependencia | Release propuesto | Criterio de aceptación de ESC-01 | Estado |
| --- | --- | --- | --- | --- | --- |
| CAP-01 | Diagnóstico, base y viabilidad de integración | Acceso a datos y proveedor | R0 | Definiciones por cohorte, volumen evaluable y prueba representativa de datos/recuperación; forecast revisado. | Propuesta |
| CAP-02 | Inventario consistente y reservas | CAP-01; stock físico | R1 | Reserva concurrente y excepciones verificadas; uso real permite medir KPI-01/KPI-02. | Propuesta |
| CAP-03 | Gestión y trazabilidad de pedidos | CAP-01/CAP-02 | R1 | Pedido trazable de confirmación a retiro, idempotencia y recuperación probadas, sin pérdidas no conciliadas. | Propuesta |
| CAP-04 | Preparación y retiro C&C | CAP-02/CAP-03/CAP-05/CAP-06 | R1 | Cliente completa retiro real, tienda acepta proceso/dotación y KPI-03 evaluable. | Propuesta |
| CAP-05 | Seguridad, datos, observabilidad y métricas | Desde inicio | R0 a R4 | Controles obligatorios, eventos auditables, alertas atendidas y cero riesgos críticos abiertos al liberar. | Transversal propuesta |
| CAP-06 | Adopción, continuidad y soporte | Desde inicio | R0 a R4 | Formación y ensayo, transición/reversión probadas, dueño operativo y soporte asignados. | Transversal propuesta |
| CAP-07 | Escalamiento y preparación del evento | Evidencia R1 y capacidad | R2 | Cobertura aceptada, carga representativa y recuperación verificadas antes de M8. | Propuesta |
| CAP-08 | Devoluciones elegibles | CAP-03; reglas Comercial/Finanzas | R3 | Caso completo y trazable, conciliación y responsabilidad de resolución; aceptación y medición propias. | Propuesta posterior |

CAP-05/CAP-06 no se posponen al final ni se someten a descarte por menor atractivo comercial. El objetivo de disponibilidad ≥99,9% no permite programar una interrupción contraria a la continuidad del caso.

## EDT y asignación de costos

La EDT agrupa entregables para estimación y control; el backlog ordena capacidades. Un mismo CAP consume varios paquetes PAQ, sin duplicar su costo por aparecer en dos vistas.

| Paquete | Entregable y frontera de costo | Capacidades vinculadas | Dueño empresarial propuesto |
| --- | --- | --- | --- |
| PAQ-01 | Formulación, gobierno, arquitectura y aprendizaje inicial | CAP-01; coordinación transversal | Dirección de proyecto/Arquitectura |
| PAQ-02 | Integración e inventario: contratos de datos, reserva, reconciliación | CAP-01/CAP-02 | Tecnología/Logística |
| PAQ-03 | Gestión y trazabilidad de pedidos, configuración e interfaces | CAP-03 | Tecnología/PO |
| PAQ-04 | Flujo C&C y formación inicial de piloto/primeras olas | CAP-04/CAP-06 | Operaciones/Tiendas |
| PAQ-05 | Configuración de expansión posterior y devoluciones elegibles | CAP-07/CAP-08 | Operaciones/Comercial |
| PAQ-06 | Controles, QA transversal, observabilidad y resiliencia | CAP-05 y pruebas comunes | CISO/Tecnología |
| PAQ-07 | Transición, soporte y recurrentes de cloud/licencias del horizonte | CAP-06/CAP-07; medición continuada | Operaciones/Tecnología |

El esfuerzo de prueba funcional de cada paquete se diferencia de QA transversal; licencias/cloud recurrentes se concentran en PAQ-07. Cambiar esta frontera obliga a revisar la tabla de costos y el total. PAQ-04 cubre formación inicial; PAQ-05 habilita olas posteriores. No sumar otra vez adopción o expansión por release.

## Historias iniciales y calidad

- Como cliente, necesito comprar sobre stock reservable. Aceptar éxito, vencimiento, concurrencia y tratamiento de inventario obsoleto, con reglas acordadas.
- Como personal de tienda, necesito ver y preparar pedidos con promesa definida. Aceptar estados, prioridad, permisos y excepciones.
- Como responsable de operación, necesito detectar pedidos/stock desactualizados. Aceptar evento, destinatario y procedimiento de respuesta.

DoD propuesta: criterios funcionales cumplidos; pruebas de integración/concurrencia necesarias; controles y trazabilidad; documentación operativa; telemetría; reversión; soporte aceptado. El beneficio requiere además evidencia de uso y KPI en G2, no solo DoD técnica.

## Cambio de alcance

PO puede reordenar detalle dentro de límites. Dirección de proyecto integra impacto. Sponsor/comité aprueba nueva capacidad, cobertura comprometida, presupuesto, hito o beneficio; CISO y Operaciones aceptan sus condiciones. Registrar decisión, capacidad, costo, dependencia, riesgo y documentos afectados. Mantener la integración de aportes del grupo antes de cerrar el alcance.
