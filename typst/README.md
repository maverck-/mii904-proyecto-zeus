# Soporte de Typst

La propuesta se desarrolla en Markdown. Este directorio contiene un ejemplo técnico y módulos reutilizables para preparar un informe si se acuerda su necesidad. No hay un informe final ni una plantilla académica obligatoria definida por la pauta.

## Qué se versiona

- [documento_respaldo.typ](documento_respaldo.typ): portada e índice del [documento de respaldo](../documento/README.md); el cuerpo lo genera Pandoc desde `documento/respaldo.md`.
- [modulos/estilo_zeus.typ](modulos/estilo_zeus.typ): estilo alineado con la presentación (colores, tipografía, tablas, franja y portada).
- [filtros/zeus.lua](filtros/zeus.lua): filtro de Pandoc que convierte los bloques `::: franja` y agrega el import del estilo.
- `fuentes/`: Manrope e IBM Plex Mono descargadas de Google Fonts, con sus licencias OFL. `recursos/`: logo PUCV exportado de la presentación.
- [compilar_documento.py](../scripts/compilar_documento.py): compila el documento en `documento/ZEUS_documento_respaldo.pdf`.
- [modulos/base.typ](modulos/base.typ): configuración inicial editable, metadatos y bloques de estado/fuente.
- [ejemplo.typ](ejemplo.typ): muestra compilable que prueba importación, tabla, bloques y lectura de un Markdown como texto literal.
- [.vscode/extensions.json](../.vscode/extensions.json): recomendación opcional de Tinymist para el editor. No incluye el binario de la extensión.
- [compilar_ejemplo.py](../scripts/compilar_ejemplo.py): crea una salida local en `build/`.

## Versiones y compilación

Versión de referencia comprobada en este entorno: Typst **0.15.1**. El script verifica esa versión antes de compilar. Cada compañero instala el compilador para su sistema; no se versionan ejecutables. Python 3 solo es necesario para los scripts, no para escribir Markdown.

```sh
python3 scripts/compilar_ejemplo.py
```

Alternativamente, con Typst 0.15.1, desde la raíz y después de crear `build/`:

```sh
typst compile --root . typst/ejemplo.typ build/ejemplo.pdf
```

El ejemplo usa módulos locales y fuentes incluidas en Typst, sin paquetes externos. La muestra incorpora texto Markdown mediante `read` y `raw`: eso lo muestra literalmente, **no lo convierte en maquetación de informe**. Para un informe, trasladar el contenido acordado a secciones `.typ` o elegir explícitamente un conversor, conservando una fuente de verdad y revisando el resultado.

## Extensiones y paquetes

La [extensión Tinymist](https://marketplace.visualstudio.com/items?itemName=myriad-dreamin.tinymist) ofrece soporte de Typst en VS Code; su identificador se deja como recomendación opcional. [Proyecto oficial](https://github.com/Myriad-Dreamin/tinymist), consultado el 19 de octubre de 2026. La compilación CLI comprobada sigue siendo la referencia si un editor usa otra versión integrada.

Los módulos propios se guardan en `modulos/`. Si más adelante se requiere un paquete externo, registrar nombre, versión exacta, propósito y licencia, fijar su importación y revisar su descarga; hoy no hay dependencias de paquetes externos ni se han instalado extensiones automáticamente. No hace falta añadir un gestor de paquetes o una biblioteca de diagramas para empezar.
