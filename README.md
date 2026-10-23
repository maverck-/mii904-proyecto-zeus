# ZEUS: trabajo grupal de Gestión de Proyectos Informáticos

Repositorio de la primera etapa de ZEUS, caso M-GesPro Retail. Contiene siete documentos de trabajo en Markdown, fuentes y registros para construir y defender una propuesta común.

**Estado al 23 de octubre: se integra la nueva actualización del equipo.** WSJF reemplaza la matriz anterior; la estimación incorpora 104 equipo-sprints, capacidad propuesta 120 y presupuesto base 1.330 + reserva 170 = 1.500 MM CLP. Primer tramo propuesto 675 MM. Cálculos verificados, con calendario, carga por rol y frontera de costos pendientes de conciliar. Ver [comparación y ajustes](registros/revision_avance_2026-10-23.md).

Se mantienen B/híbrido, piloto 10/M5 y objetivo 68/M7. El experimento R3 pasa a 3–5 tiendas según el equipo. Los límites de apoyo del 22 (brigadas, 2 tiendas/30 MM) quedan como antecedente, sin agregarse al nuevo presupuesto. Catálogo/CD y umbrales piloto anteriores requieren ratificación. No se presume aprobación colectiva ni empresarial.

**Parte de Maverick desarrollada:** [alcance/backlog](trabajo/04_alcance_y_backlog.md) y [roadmap](trabajo/07_roadmap.md) ya incluyen catálogo propuesto, aceptación, historias, límites experimentales, calendario y olas. El [plan de apoyo](registros/plan_alcance_roadmap.md) distribuye las 104 unidades por épica/etapa y dimensiona 58 altas con tres células dentro de E11. El contenido está listo para revisión; faltan ratificación del grupo y contraste de Rogelio sobre especialidades, contratos y costos. No representa capacidad empresarial validada.

**Entrega y presentación: 24 de octubre de 2026**, según clase 2, parte 2, 1:10:32 a 1:10:44. Objetivo interno: versión lista y ensayada el viernes 23. Confirmar formato y hora de carga en aula. Pauta: máximo 35 minutos, recomendados 25 de exposición y 10 de defensa; sugerencia de hasta 12 láminas principales más anexos.

## Incorporarse al trabajo

1. Leer la [pauta](insumos/pauta.md), el [estado de entregables](trabajo/README.md) y las [responsabilidades](EQUIPO.md).
2. Revisar el [avance recibido del 23](insumos/avance_equipo_2026-10-23.md) y la [comparación](registros/revision_avance_2026-10-23.md). Los documentos 01 a 03 son la versión integrada editable.
3. Rogelio revisa priorización/estimación; Maverick alcance/roadmap. Coordinar capacidad/costo antes de cerrar 68 tiendas en M7.
4. Resolver [supuestos](registros/acuerdos_y_supuestos.md), metas piloto, alcance del experimento y financiación inicial. Registrar solo acuerdos efectivamente aceptados.
5. Proponer cambios mediante rama o edición con solicitud de revisión; ver [CONTRIBUTING.md](CONTRIBUTING.md).

| Ubicación | Contenido |
| --- | --- |
| [trabajo/](trabajo/README.md) | Siete componentes de la pauta y estado de revisión. |
| [registros/](registros/acuerdos_y_supuestos.md) | Supuestos/decisiones, [riesgos](registros/riesgos.md) y [revisión de integración](registros/integracion_avance_equipo.md). |
| [insumos/](insumos/README.md) | Enunciado, pauta, avance recibido y presentaciones 03 a 06. |
| [transcripciones/](transcripciones/README.md) | Clases 1 a 3, seis partes con tiempos. |
| [presentacion/](presentacion/README.md) | Mapa/guion de 12 láminas y 25 minutos, anexos y defensa; archivo final pendiente. |
| [typst/](typst/README.md) | Ejemplo y módulos locales para eventual informe. |
| [PLAN.md](PLAN.md) | Orden y condiciones para cerrar. |

## Alcance de la propuesta

B modular sigue siendo una base revisable. Se conserva el avance del equipo con correcciones trazables: observabilidad mínima desde R1, viabilidad técnica temprana, metas y ventanas explícitas, escala condicionada y Ship-from-store experimental en R3. El escenario anterior ESC-01 queda en Git; sus costos y cobertura no son vigentes para este plan.

La [estimación del equipo](trabajo/06_estimacion.md) ya está cuantificada como base de discusión. No acredita cotizaciones/históricos ni probabilidad validada de plazo. El extremo alto de categorías 1.500 consume toda la reserva nominal; no hay otros 170 disponibles además para cualquier riesgo. Revisar doble conteo entre equipos, OMS/WMS, capacitación y gobierno.

El [antecedente del 22](registros/escenario_provisional.md) conserva un modelo local para sensibilidad; tiene prioridad la nueva base del equipo y su conciliación con alcance/recursos. La [revisión de clase 3](registros/aportes_clase_03.md) conserva referencias docentes.

Los siete Markdown organizan el contenido, sin implicar siete documentos formales separados para entregar. La pauta no explicita un informe adicional. Mantener contenido primero y decidir formato final según aula.

## Herramientas y comprobaciones

Para leer y proponer cambios basta GitHub o un editor Markdown. Con Python 3:

```sh
python3 scripts/verificar.py
```

Comprueba fuentes, presentaciones, transcripciones, enlaces, rúbrica, operaciones disponibles y referencias. Distingue cálculo comprobado de calendario/viabilidad pendientes; no acredita validación del grupo. Typst 0.15.1 es opcional para el ejemplo técnico; `build/` queda fuera de Git.

Repositorio público: se puede leer y clonar con el enlace. Para subir directamente se requiere permiso de colaboración; también se puede proponer desde un fork. No incluir conversaciones privadas ni datos de contacto. Materiales docentes y transcripciones se incluyen como insumos académicos.
