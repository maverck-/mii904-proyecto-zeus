// Estilo del documento de respaldo, alineado con la presentación en Figma Slides.
#let tinta = rgb("000614")
#let cuerpo = rgb("3d4556")
#let tenue = rgb("5b6475")
#let azul = rgb("2569ed")
#let azul-suave = rgb("e8effd")
#let azul-medio = rgb("7fa6f5")
#let borde = rgb("d9deea")
#let fila-alterna = rgb("eef2fa")
#let fondo = rgb("fafbff")
#let ambar = rgb("a55a05")

#let franja(body) = block(
  width: 100%, fill: azul-suave, radius: 6pt, inset: (x: 12pt, y: 10pt), breakable: false,
  grid(
    columns: (12pt, 1fr), column-gutter: 9pt, align: (center + top, left + top),
    pad(top: 2pt, polygon.regular(fill: azul, size: 10pt, vertices: 3)),
    body,
  ),
)

#let portada(titulo: "", subtitulo: "", curso: "", integrantes: "", fecha: "", logo: none) = page(
  fill: rgb("000000"), margin: (x: 22mm, top: 20mm, bottom: 22mm), header: none, footer: none,
)[
  #set text(font: "Manrope", weight: 500, fill: white, lang: "es", tracking: -0.1pt)
  #if logo != none { image(logo, width: 52mm) }
  #v(1fr)
  #text(size: 14pt, weight: 500)[#curso]
  #v(8pt)
  #block(width: 92%)[#text(size: 30pt, weight: 600, tracking: -0.3pt)[#titulo]]
  #v(10pt)
  #text(size: 13pt, weight: 500, fill: rgb("c9d1e2"))[#subtitulo]
  #v(1fr)
  #text(size: 13pt, weight: 700)[#integrantes]
  #v(6pt)
  #text(size: 10pt, weight: 500, fill: rgb("c9d1e2"))[#fecha]
]

#let documento(titulo: "ZEUS", pie: "", body) = {
  set document(title: titulo, author: "Equipo ZEUS")
  set text(font: "Manrope", weight: 500, size: 9.2pt, fill: cuerpo, lang: "es", tracking: -0.1pt)
  set par(leading: 0.62em, spacing: 0.95em, justify: false)
  set page(
    paper: "a4", fill: fondo, margin: (x: 18mm, top: 18mm, bottom: 20mm),
    footer: context [
      #set text(size: 7.5pt)
      #text(fill: tenue)[#pie]
      #h(1fr)
      #text(font: "IBM Plex Mono", weight: 500, fill: azul)[#counter(page).display()]
    ],
  )
  show strong: set text(weight: 700, fill: tinta)
  show link: set text(fill: azul)
  show heading.where(level: 1): it => {
    pagebreak(weak: true)
    block(above: 0pt, below: 14pt)[
      #rect(width: 28pt, height: 3pt, fill: azul, stroke: none)
      #v(6pt)
      #text(size: 19pt, weight: 600, fill: tinta, tracking: -0.3pt)[#it.body]
    ]
  }
  show heading.where(level: 2): it => block(above: 16pt, below: 7pt)[
    #text(size: 11.5pt, weight: 700, fill: azul)[#it.body]
  ]
  show heading.where(level: 3): it => block(above: 12pt, below: 6pt)[
    #text(size: 10pt, weight: 700, fill: tinta)[#it.body]
  ]
  show figure: set block(breakable: true)
  show figure.where(kind: table): set align(left)
  set table(
    stroke: (x, y) => (bottom: 0.5pt + borde),
    inset: (x: 5pt, y: 4pt),
    fill: (x, y) => if y == 0 { tinta } else if calc.even(y) { fila-alterna } else { white },
  )
  show table: set text(size: 8pt)
  show table.cell.where(y: 0): set text(fill: white, weight: 700)
  show table: it => block(radius: 5pt, clip: true, stroke: 0.6pt + borde, it)
  body
}
