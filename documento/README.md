# Documento de respaldo

[ZEUS_documento_respaldo.pdf](ZEUS_documento_respaldo.pdf) reúne los siete componentes de la primera etapa en una versión de entrega para el Comité Ejecutivo: diagnóstico y Business Case, enfoque, Charter, alcance, priorización, estimación y roadmap, con anexos de supuestos, riesgos, interesados, cambios de condición y fuentes. Complementa la presentación; la pauta no exige un informe escrito.

La fuente es [respaldo.md](respaldo.md), una versión curada de los documentos de [trabajo/](../trabajo/README.md) sin notas internas del grupo. Si cambia una cifra o decisión, se actualiza primero en `trabajo/` y después aquí.

## Compilar

Requiere Pandoc 3 y Typst 0.15.1. Desde la raíz del repositorio:

```sh
python3 scripts/compilar_documento.py
```

Pandoc convierte el Markdown a Typst con el filtro [zeus.lua](../typst/filtros/zeus.lua), y Typst aplica el estilo de la presentación definido en [estilo_zeus.typ](../typst/modulos/estilo_zeus.typ): Manrope e IBM Plex Mono, fondo #FAFBFF, texto #000614, azul #2569ED y portada oscura con el logo PUCV. Las fuentes están en [typst/fuentes/](../typst/fuentes/) con sus licencias OFL.
