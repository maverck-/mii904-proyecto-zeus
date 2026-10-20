# ZEUS: trabajo grupal de Gestión de Proyectos Informáticos

Espacio para desarrollar juntos la primera etapa del caso M-GesPro Retail. La alternativa **B, plataforma omnicanal modular**, es la base actual de trabajo y puede revisarse al contrastar alcance, riesgos, costos y valor.

Entrega y presentación: **24 de octubre de 2026**, según la clase 2, parte 2, 1:10:32 a 1:10:44. Confirmar hora de carga y formato en el aula. La pauta propone 25 minutos de exposición y 10 de defensa, máximo 35; sugiere hasta 12 diapositivas principales más anexos.

## Empezar

1. Leer la [pauta y cobertura](insumos/pauta.md) y el [enunciado](insumos/enunciado-zeus-etapa1.pdf).
2. Revisar el escenario **ESC-01** de [trabajo](trabajo/README.md) e integrar los aportes del equipo en los tres primeros documentos. Los siete borradores ya incluyen supuestos explícitos, métricas, costos y gates, pendientes de revisión conjunta.
3. Revisar [alcance y backlog](trabajo/04_alcance_y_backlog.md), luego priorización, estimación y roadmap.
4. Registrar lo que se acuerde y lo que se supone en [acuerdos y supuestos](registros/acuerdos_y_supuestos.md).
5. Consultar las [transcripciones](transcripciones/README.md) cuando se necesite evidencia de una indicación docente.

## Estructura

```text
insumos/          enunciado y pauta de evaluación
transcripciones/  clases disponibles con marcas de tiempo
trabajo/          siete entregables, con guía y borrador editable
registros/        acuerdos, supuestos y riesgos comunes
presentacion/     estructura de exposición y defensa
typst/           ejemplo y módulos para un eventual informe
scripts/          comprobación y compilación opcional
```

## Cómo avanzar

Los archivos Markdown son la fuente del contenido. Cada sección debe indicar si contiene datos del caso, una propuesta o un acuerdo. Se pueden sugerir capacidades en el backlog antes de cerrar el alcance; su estado pasa de propuesta a incluida solo cuando se justifica y acuerda. Usar IDs comunes para conectar alcance, estimación y releases.

Para cambios pequeños se puede editar Markdown desde la plataforma del repositorio; para cambios extensos, usar una rama y revisión de otro integrante. El flujo está en [CONTRIBUTING.md](CONTRIBUTING.md). El [plan](PLAN.md) marca el orden de cierre, sin asignar responsables ni reuniones que aún no estén acordados.

## Herramientas

Para contenido basta un editor Markdown. Python 3 permite ejecutar `python3 scripts/verificar.py`. Typst es opcional mientras se acuerda si habrá informe; se incluye [soporte compilable](typst/README.md) con módulos locales. La extensión recomendada de VS Code se ofrece como sugerencia de instalación, no se instala automáticamente.

El repositorio está preparado localmente. Antes de compartirlo, crear un remoto privado e invitar a los compañeros; los materiales docentes y las transcripciones se usan como insumo del grupo. La pauta disponible exige una presentación y defensa y no explicita un informe escrito adicional.

## Avance con supuestos, 20 de octubre

ESC-01 propone piloto de 5 tiendas/un CD, metas intermedias, rangos de costo, capacidad y expansión condicional. Cada supuesto tiene en el registro la revisión académica requerida y la validación empresarial hipotética. Los números permiten discutir una propuesta coherente y se pueden sustituir; no son resultados, cotizaciones o decisiones grupales aprobadas. La [estimación](trabajo/06_estimacion.md) muestra también el escenario que supera el techo y exige replantear.
