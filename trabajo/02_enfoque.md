# 2. Selección y tailoring del enfoque

**Propuesta desarrollada ESC-01, pendiente de revisión del grupo.** Fuente contextual: enunciado, pp. 5 a 8; enfoques en clase 1 y estrategia/valor en clase 2. Integrar aportes existentes del equipo antes de cerrar la versión.

## Comparación

| Enfoque | Aporte en ZEUS | Limitación a gestionar |
| --- | --- | --- |
| Predictivo | Contratos, interfaces, hitos, continuidad y aceptación explícita | Congelar todo el detalle ahora puede convertir incertidumbre en requisitos ficticios. |
| Adaptativo | Feedback y aprendizaje sobre experiencia, integración y operación | Necesita capacidad real de negocio y coordinación con terceros. |
| Híbrido | Conecta decisiones ejecutivas con entrega y aprendizaje | Evitar duplicación entre plan y backlog con resultados y dependencias comunes. |

Se propone híbrido por continuidad operacional, contratos y sistemas compartidos junto con incertidumbre de solución y adopción. La regulación por sí sola no determina el enfoque. La alternativa B tampoco obliga a una metodología específica.

## Tailoring: práctica, necesidad y decisión

| Necesidad | Práctica propuesta | Cadencia de ESC-01 | Decisión habilitada |
| --- | --- | --- | --- |
| APIs y datos legacy inciertos | Prueba representativa y validación de contratos de datos | M1/M2, antes de G1 | Continuar integración o replantear alcance/alternativa. |
| Conocer el trabajo de tienda | Validación del flujo con usuarios y PO | Cada dos semanas, según disponibilidad SUP-02 | Refinar backlog y aceptación antes de expandir. |
| Capacidad técnica limitada | Dos frentes coordinados con límite de trabajo en curso | Revisión semanal de dependencias | Reducir simultaneidad si proveedor o especialistas bloquean. |
| Mantener operación | Despliegue gradual, monitoreo, soporte y reversión aceptados | Cada release | Liberar, pausar o recuperar, con Operaciones/Tecnología. |
| Inversión y beneficios | Forecast y Business Case actualizados | Mensual y G1 a G5 | Liberar tramos, ajustar o detener. |
| Seguridad y datos | Controles desde diseño, pruebas y revisión de salida | Continuo y antes de release | Resolver exposición crítica antes de producción. |

No se presume un equipo con velocidad Scrum conocida. Se pueden usar iteraciones o flujo según capacidad, conservando calidad, feedback y pronóstico. Las frecuencias son propuestas, no actividades ya realizadas.

## Qué se fija y qué se adapta

Límites del caso: techo preliminar, ERP/WMS, continuidad, controles, horizonte y valor dentro de M5. El sponsor no puede asumir por defecto que las restricciones se flexibilizarán.

Adaptables mediante decisión trazable: diseño, proveedor, historias, secuencia fina, familias y cantidad de tiendas por ola. Los cambios que afectan costo, beneficio, alcance de alto nivel o hitos requieren revisión del sponsor/comité. PO reprioriza dentro de guardrails; dirección de proyecto integra dependencias y cambios. CISO y Operaciones pueden bloquear una salida no aceptable en sus ámbitos.

## Artefactos conectados

Charter define autoridad y límites; la EDT PAQ-01 a PAQ-07 permite asignar costo; el backlog CAP-01 a CAP-08 ordena capacidades; roadmap R0 a R4 conecta dependencias y gates; registros comunes conservan supuestos, riesgos y decisiones. Cada capacidad puede consumir varios paquetes, pero el costo se imputa una sola vez. El KPI sigue el resultado, no el número de historias terminadas.

Aceptar como terminado exige criterios funcionales, pruebas necesarias, controles, documentación, telemetría, reversión y responsable de soporte. Esa calidad del incremento no equivale a beneficio ya realizado: G2 evalúa uso y KPI con cohorte comparable.
