// Documento de respaldo ZEUS. El cuerpo se genera con Pandoc desde documento/respaldo.md.
#import "modulos/estilo_zeus.typ": *

#portada(
  titulo: "ZEUS: B Modular, piloto y expansión con evidencia",
  subtitulo: "Documento de respaldo para el Comité Ejecutivo de M-GesPro Retail · Primera etapa",
  curso: "MII904 Gestión de Proyectos Informáticos",
  integrantes: "Bryam González · Alejandro Malvacias · Rogelio Gonzalez · Maverick Gayoso",
  fecha: "24 de octubre de 2026",
  logo: "/typst/recursos/logo-pucv-blanco.png",
)

#show: documento.with(
  titulo: "ZEUS · Documento de respaldo",
  pie: "ZEUS · Documento de respaldo · MII904",
)

#block(below: 14pt)[
  #rect(width: 28pt, height: 3pt, fill: azul, stroke: none)
  #v(6pt)
  #text(size: 19pt, weight: 600, fill: tinta)[Contenido]
]
#outline(title: none, depth: 1, indent: 0pt)

#include "/build/respaldo_cuerpo.typ"
