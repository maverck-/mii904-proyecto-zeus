// Módulos locales de apoyo. Formato inicial editable, no plantilla del curso.
#let documento(titulo: "ZEUS", subtitulo: "", body) = {
  set document(title: titulo, author: "Equipo ZEUS")
  set page(paper: "a4", margin: (x: 24mm, y: 22mm), numbering: "1")
  set text(font: "Libertinus Serif", size: 11pt, lang: "es")
  set par(justify: true)
  set heading(numbering: "1.")
  align(center)[
    #text(size: 19pt, weight: "bold", titulo)
    #parbreak()
    #text(size: 10pt, subtitulo)
  ]
  v(10pt)
  body
}

#let estado(body) = block(
  width: 100%, inset: 9pt, radius: 3pt,
  fill: rgb("eef3f7"), stroke: 0.5pt + rgb("aabcc9"), body,
)

#let fuente(body) = block[
  #text(size: 9pt, fill: rgb("46525b"))[Fuente: #body]
]
