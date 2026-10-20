# 6. Estimación y tratamiento de incertidumbre

Estado: estructura de estimación para completar. Los 1.350 MM CLP y 9 a 12 meses de B son referencias preliminares del enunciado, p. 7. No prueban costo final ni cumplimiento de M5. Techo preliminar: 1.500 MM CLP.

## Método propuesto

Estimar por paquetes de alcance; usar rangos optimista, más probable y pesimista con fundamento. Se puede usar `E = (O + 4M + P) / 6` como escenario central declarado, sin asignarle una probabilidad de éxito no validada. Separar esfuerzo, duración, disponibilidad y dependencias.

| Paquete de alcance | O | M | P | Fundamento del rango | Capacidad / dependencia |
| --- | --- | --- | --- | --- | --- |
| Formulación y gobierno | Por estimar | Por estimar | Por estimar | Validaciones y coordinación | Negocio, Tecnología y proveedores |
| Inventario e integración | Por estimar | Por estimar | Por estimar | APIs, stock y concurrencia | ERP/WMS y datos |
| Pedidos | Por estimar | Por estimar | Por estimar | Compra/configuración e interfaces | CAP-01/CAP-02 |
| C&C y adopción | Por estimar | Por estimar | Por estimar | Flujo y preparación de tiendas | Dotación y proceso |
| Expansión / devoluciones | Por estimar | Por estimar | Por estimar | Cobertura y reglas | Alcance acordado |
| Seguridad y calidad | Por estimar | Por estimar | Por estimar | Controles y pruebas | CISO, QA y operación |
| Transición y operación | Por estimar | Por estimar | Por estimar | Soporte, licencias y cloud | Servicio/proveedor |

Acordar unidad, horizonte e inclusión de impuestos antes de llenar la tabla. No sumar nuevamente costos recurrentes ya incluidos en un paquete ni copiar cifras de otro escenario como si fueran del equipo.

## Completar para cerrar

- Separar costos de inversión, operación y transición y definir qué cubre el horizonte de 12 meses.
- Explicar fuente de cada rango o supuesto didáctico cuando no exista cotización.
- Explicitar reserva y si está dentro del presupuesto; distinguir techo del caso y costo estimado.
- Calcular escenario central y adverso, mostrando si alguno supera 1.500 MM y qué alcance se reduciría.
- Validar capacidad dedicada antes de prometer trabajo paralelo.
- Reestimar después de prueba de integración y de cada piloto/release relevante.

Si se mantiene B como base, la descomposición debe justificar su viabilidad y secuencia; no forzar partidas para que sumen exactamente 1.350 MM. Incorporar lo visto en sesiones 5 y 6 cuando el grupo disponga del material.
