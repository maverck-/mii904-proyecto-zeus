# ZEUS: trabajo grupal de Gestión de Proyectos Informáticos

Repositorio de la primera etapa de ZEUS, caso M-GesPro Retail. Contiene siete documentos de trabajo en Markdown, fuentes y registros para construir y defender una propuesta común.

**Estado al 21 de octubre: ESC-02 integra el avance recibido del equipo como base principal.** Diagnóstico/Business Case, enfoque y Charter están integrados; alcance y roadmap se alinean con piloto 10/M5, objetivo 68/M7 y R3 condicionado. Priorización requiere revisión y estimación requiere nueva cuantificación. Son borradores con supuestos, no decisiones colectivas aprobadas.

**Entrega y presentación: 24 de octubre de 2026**, según clase 2, parte 2, 1:10:32 a 1:10:44. Objetivo interno: versión lista y ensayada el viernes 23. Confirmar formato y hora de carga en aula. Pauta: máximo 35 minutos, recomendados 25 de exposición y 10 de defensa; sugerencia de hasta 12 láminas principales más anexos.

## Incorporarse al trabajo

1. Leer la [pauta](insumos/pauta.md), el [estado de entregables](trabajo/README.md) y las [responsabilidades](EQUIPO.md).
2. Revisar el [avance recibido](insumos/avance_equipo_2026-10-21.md) y los [ajustes con fundamento](registros/integracion_avance_equipo.md). Los documentos 01 a 03 son la versión integrada editable.
3. Rogelio revisa priorización/estimación; Maverick alcance/roadmap. Coordinar capacidad/costo antes de cerrar 68 tiendas en M7.
4. Resolver [supuestos](registros/acuerdos_y_supuestos.md), metas piloto, alcance del experimento y financiación inicial. Registrar solo acuerdos efectivamente aceptados.
5. Proponer cambios mediante rama o edición con solicitud de revisión; ver [CONTRIBUTING.md](CONTRIBUTING.md).

| Ubicación | Contenido |
| --- | --- |
| [trabajo/](trabajo/README.md) | Siete componentes de la pauta y estado de revisión. |
| [registros/](registros/acuerdos_y_supuestos.md) | Supuestos/decisiones, [riesgos](registros/riesgos.md) y [revisión de integración](registros/integracion_avance_equipo.md). |
| [insumos/](insumos/README.md) | Enunciado oficial, pauta y avance recibido. |
| [transcripciones/](transcripciones/README.md) | Clases 1 y 2, cuatro partes con tiempos. |
| [presentacion/](presentacion/README.md) | Orientación de exposición y defensa; archivo final pendiente. |
| [typst/](typst/README.md) | Ejemplo y módulos locales para eventual informe. |
| [PLAN.md](PLAN.md) | Orden y condiciones para cerrar. |

## Alcance de la propuesta

B modular sigue siendo una base revisable. Se conserva el avance del equipo con correcciones trazables: observabilidad mínima desde R1, viabilidad técnica temprana, metas y ventanas explícitas, escala condicionada y Ship-from-store experimental en R3. El escenario anterior ESC-01 queda en Git; sus costos y cobertura no son vigentes para este plan.

La estimación sigue abierta: 1.350 MM CLP es referencia B y 1.500 MM es techo del caso. Faltan rangos por paquete, capacidad, reserva y tramos. No afirmar que la nueva cobertura cabe en esos montos. Al ser una empresa ficticia, validación académica significa revisar razonabilidad/coherencia; pruebas con proveedores/tiendas se describen como futuro hipotético.

Los siete Markdown organizan el contenido, sin implicar siete documentos formales separados para entregar. La pauta no explicita un informe adicional. Mantener contenido primero y decidir formato final según aula.

## Herramientas y comprobaciones

Para leer y proponer cambios basta GitHub o un editor Markdown. Con Python 3:

```sh
python3 scripts/verificar.py
```

Comprueba fuentes, enlaces, rúbrica, operaciones disponibles y referencias. Declara la estimación pendiente; no acredita validación del grupo. Typst 0.15.1 es opcional para el ejemplo técnico; `build/` queda fuera de Git.

Repositorio público: se puede leer y clonar con el enlace. Para subir directamente se requiere permiso de colaboración; también se puede proponer desde un fork. No incluir conversaciones privadas ni datos de contacto. Materiales docentes y transcripciones se incluyen como insumos académicos.
