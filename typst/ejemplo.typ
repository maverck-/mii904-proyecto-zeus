#import "modulos/base.typ": documento, estado, fuente
#show: documento.with(
  titulo: "ZEUS · Muestra técnica de Typst",
  subtitulo: "Ejemplo de herramientas; contenido final pendiente",
)

#estado[Este archivo comprueba el entorno y los módulos. El informe se preparará cuando se acuerden formato y contenido.]

= Capacidades del módulo

La base permite definir metadatos, encabezados, tablas y bloques de estado y fuente con archivos locales.

#table(
  columns: (1fr, 2fr), inset: 7pt,
  [*Elemento*], [*Uso*],
  [Markdown], [Contenido de trabajo y revisión del equipo.],
  [Typst], [Representación de documento cuando se decida producirlo.],
)

#fuente[Enunciado ZEUS, primera etapa, páginas 8 y 9.]

= Ejemplo de lectura literal

El siguiente extracto se muestra como código literal para demostrar una importación de archivo. No es conversión automática de Markdown.

#raw(read("../trabajo/03_charter.md").split("\n").slice(0, 3).join("\n"), lang: "markdown")
