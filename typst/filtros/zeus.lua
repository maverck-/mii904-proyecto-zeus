-- Convierte bloques ::: franja de Markdown en la función franja de Typst.
function Div(el)
  if el.classes:includes('franja') then
    local blocks = { pandoc.RawBlock('typst', '#franja[') }
    for _, b in ipairs(el.content) do
      table.insert(blocks, b)
    end
    table.insert(blocks, pandoc.RawBlock('typst', ']'))
    return blocks
  end
end

-- El cuerpo se incluye desde otro archivo y necesita importar el estilo.
function Pandoc(doc)
  table.insert(doc.blocks, 1, pandoc.RawBlock('typst', '#import "/typst/modulos/estilo_zeus.typ": franja'))
  return doc
end
