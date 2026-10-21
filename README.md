# ZEUS: trabajo grupal de Gestión de Proyectos Informáticos

Repositorio de la primera etapa de ZEUS, caso M-GesPro Retail. Contiene los siete entregables en Markdown, sus supuestos y fuentes para revisar y desarrollar la propuesta en conjunto.

**Estado al 21 de octubre:** borradores desarrollados con el escenario propuesto ESC-01, pendientes de revisión del equipo. La alternativa B modular es la base actual y puede cambiar si alcance, costo, riesgo o valor no la sostienen.

**Entrega y presentación: 24 de octubre de 2026**, según clase 2, parte 2, 1:10:32 a 1:10:44. Objetivo de organización propuesto: dejar la versión final lista y ensayada el viernes 23. Confirmar formato y hora de carga en el aula. La pauta recomienda 25 minutos de exposición y 10 de defensa, máximo 35, y hasta 12 láminas principales más anexos.

## Incorporarse al trabajo

1. Leer la [pauta](insumos/pauta.md) y el [estado de los siete entregables](trabajo/README.md).
2. Revisar el [reparto propuesto](EQUIPO.md) y acordarlo antes de asumir responsabilidades.
3. Integrar los aportes ya preparados por el equipo en los primeros tres documentos; conservar una versión común por entregable.
4. Revisar [alcance y backlog](trabajo/04_alcance_y_backlog.md), [supuestos](registros/acuerdos_y_supuestos.md), costos y roadmap. Cada cifra adicional del escenario puede ajustarse con fundamento.
5. Proponer cambios mediante rama o edición web con solicitud de revisión; ver [CONTRIBUTING.md](CONTRIBUTING.md).

## Archivos principales

| Ubicación | Contenido |
| --- | --- |
| [trabajo/](trabajo/README.md) | Diagnóstico/Business Case, enfoque, Charter, alcance/backlog, priorización, estimación y roadmap. |
| [registros/](registros/acuerdos_y_supuestos.md) | Decisiones y supuestos; [riesgos](registros/riesgos.md) compartidos. |
| [insumos/](insumos/README.md) | Enunciado oficial y resumen de pauta. |
| [transcripciones/](transcripciones/README.md) | Clases 1 y 2, cuatro partes con marcas de tiempo. |
| [presentacion/](presentacion/README.md) | Orientación de exposición y defensa. |
| [typst/](typst/README.md) | Ejemplo compilable y módulos locales para un eventual informe. |
| [PLAN.md](PLAN.md) | Orden de revisión y cierre. |

Markdown es la fuente de contenido. Diferenciar datos del caso, propuestas, supuestos y acuerdos. CAP identifica capacidades y PAQ paquetes de costo; sus IDs conectan backlog, estimación y releases. No aprobar automáticamente un ítem por estar escrito.

## Revisar ESC-01

El escenario propone piloto acotado, metas intermedias, costos por rangos, capacidad y expansión condicional. Son hipótesis de trabajo académico, no cotizaciones ni pruebas realizadas. El [registro](registros/acuerdos_y_supuestos.md) indica la revisión requerida y qué se haría si cada supuesto falla. La [estimación](trabajo/06_estimacion.md) incluye un adverso que supera el techo y obliga a revisar alcance o inversión.

Como la empresa es ficticia, validar académicamente significa revisar razonabilidad, coherencia y defensa. Las comprobaciones con proveedores/tiendas se describen como trabajo futuro hipotético. La pauta no explicita un informe escrito adicional; decidir su necesidad antes de maquetarlo.

## Herramientas y comprobaciones

Para leer y proponer cambios basta la interfaz web o un editor Markdown. Con Git y Python 3:

```sh
python3 scripts/verificar.py
```

El script comprueba fuentes, enlaces, rúbrica, cálculos y referencias; no sustituye la revisión del equipo. Typst 0.15.1 es opcional para el ejemplo técnico; las instrucciones están en su carpeta. `build/` contiene salidas locales y queda fuera de Git.

El repositorio es público: cualquier persona con el enlace puede leerlo y clonarlo sin invitación. Para subir cambios directamente, los integrantes deben tener permisos de colaboración; también pueden proponer cambios desde un fork mediante una solicitud de revisión. Los materiales docentes y transcripciones se incluyen como insumo del trabajo académico.
