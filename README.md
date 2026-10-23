# ZEUS: trabajo grupal de Gestión de Proyectos Informáticos

Repositorio de la primera etapa de ZEUS, caso M-GesPro Retail. Contiene siete documentos de trabajo en Markdown, fuentes y registros para construir y defender una propuesta común.

**Estado al 23 de octubre: los siete componentes están redactados para revisión del equipo.** La propuesta recomienda B modular con enfoque híbrido, piloto de diez tiendas hasta M5 y expansión a 68 hasta M7, condicionada a evidencia y capacidad. La estimación considera 104 equipo-sprints frente a capacidad propuesta de 120, presupuesto base 1.330 + reserva 170 = 1.500 MM CLP y primer tramo de 675 MM. Son supuestos académicos, sin aprobación empresarial ni resultados ejecutados.

El [alcance](trabajo/04_alcance_y_backlog.md) y el [roadmap](trabajo/07_roadmap.md) desarrollan catálogo, aceptación, historias, experimento, calendario y olas. El [plan de apoyo](registros/plan_alcance_roadmap.md) distribuye el esfuerzo por épica/etapa y dimensiona las 58 altas adicionales dentro de E11. Falta ratificar alcance y criterios de éxito, contrastar dedicación por especialidad y conciliar contratos/costos. La [revisión editorial y argumental](registros/revision_editorial_2026-10-23.md) distingue correcciones realizadas y asuntos que requieren decisión del grupo.

**Entrega y presentación: 24 de octubre de 2026**, según clase 2, parte 2, 1:10:32 a 1:10:44. Objetivo interno: versión lista y ensayada el viernes 23. Confirmar formato y hora de carga en aula. Pauta: máximo 35 minutos, recomendados 25 de exposición y 10 de defensa; sugerencia de hasta 12 láminas principales más anexos.

## Incorporarse al trabajo

1. Leer la [pauta](insumos/pauta.md), el [estado de entregables](trabajo/README.md) y las [responsabilidades](EQUIPO.md).
2. Leer los documentos 01 a 07 como propuesta vigente. El [avance recibido del 23](insumos/avance_equipo_2026-10-23.md) y la [comparación](registros/revision_avance_2026-10-23.md) permiten consultar su procedencia.
3. Rogelio revisa priorización/estimación; Maverick alcance/roadmap. Coordinar capacidad/costo antes de cerrar 68 tiendas en M7.
4. Resolver [supuestos](registros/acuerdos_y_supuestos.md), metas piloto, alcance del experimento y financiación inicial. Registrar solo acuerdos efectivamente aceptados.
5. Proponer cambios mediante rama o edición con solicitud de revisión; ver [CONTRIBUTING.md](CONTRIBUTING.md).

| Ubicación | Contenido |
| --- | --- |
| [trabajo/](trabajo/README.md) | Siete componentes de la pauta y estado de revisión. |
| [registros/](registros/acuerdos_y_supuestos.md) | Supuestos/decisiones, [riesgos](registros/riesgos.md) y [revisión de integración](registros/integracion_avance_equipo.md). |
| [insumos/](insumos/README.md) | Enunciado, pauta, avance recibido y presentaciones 03 a 06. |
| [transcripciones/](transcripciones/README.md) | Clases 1 a 3, seis partes con tiempos. |
| [presentacion/](presentacion/README.md) | Pauta de construcción: 12 láminas/25 minutos, rúbrica, evidencia, visuales y anexos; presentación y guion en una fase posterior. |
| [typst/](typst/README.md) | Ejemplo y módulos locales para eventual informe. |
| [PLAN.md](PLAN.md) | Orden y condiciones para cerrar. |

## Alcance de la propuesta

B modular es una recomendación condicionada: viabilidad técnica temprana, observabilidad y soporte desde R1, valor medido hasta M5 y expansión por sitios aceptados. El catálogo propuesto comprende dos familias, un CD piloto y hasta tres en expansión. R3 incluye devoluciones elegibles y experimento Ship-from-store en 3–5 tiendas, hasta cuatro semanas o 300 pedidos, lo que ocurra primero, con autorización previa de exposición monetaria.

La [estimación del equipo](trabajo/06_estimacion.md) ya está cuantificada como base de discusión. No acredita cotizaciones/históricos ni probabilidad validada de plazo. El extremo alto de categorías 1.500 consume toda la reserva nominal; no hay otros 170 disponibles además para cualquier riesgo. Revisar doble conteo entre equipos, OMS/WMS, capacitación y gobierno.

Los registros conservan la [integración de aportes](registros/revision_avance_2026-10-23.md), el [antecedente del 22](registros/escenario_provisional.md) y las [referencias docentes](registros/aportes_clase_03.md). Las cantidades históricas no sustituyen la propuesta vigente ni se suman a su presupuesto.

Los siete Markdown organizan el contenido, sin implicar siete documentos formales separados para entregar. La pauta no explicita un informe adicional. Mantener contenido primero y decidir formato final según aula.

## Herramientas y comprobaciones

Para leer y proponer cambios basta GitHub o un editor Markdown. Con Python 3:

```sh
python3 scripts/verificar.py
```

Comprueba fuentes, presentaciones, transcripciones, enlaces, rúbrica, operaciones disponibles y referencias. Distingue cálculo comprobado de calendario/viabilidad pendientes; no acredita validación del grupo. Typst 0.15.1 es opcional para el ejemplo técnico; `build/` queda fuera de Git.

Repositorio público: se puede leer y clonar con el enlace. Para subir directamente se requiere permiso de colaboración; también se puede proponer desde un fork. No incluir conversaciones privadas ni datos de contacto. Materiales docentes y transcripciones se incluyen como insumos académicos.
