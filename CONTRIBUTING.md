# Cómo trabajar juntos

Cada entregable tiene un archivo de trabajo. Integrar los aportes existentes dentro de ese archivo y conservar su trazabilidad. Los tres primeros documentos pueden incorporarse desde el material que el equipo ya esté preparando.

## Cambios pequeños

Editar el Markdown correspondiente, describir el cambio y solicitar revisión si altera una decisión. Un cambio de costo, alcance, objetivo o fecha debe actualizar todos los documentos afectados. Un ítem propuesto del backlog no se vuelve compromiso al crear una fila.

## Cambios desde Git

Una vez que exista un remoto compartido y se haya clonado, partir de una rama actualizada. Ejemplo de trabajo para alcance:

```sh
git switch main
git pull --ff-only
git switch -c trabajo/alcance
```

Editar los archivos, comprobarlos y registrar solo los cambios pertinentes:

```sh
python3 scripts/verificar.py
git add trabajo/04_alcance_y_backlog.md
git commit -m "Ajusta alcance y dependencias del primer release"
git push -u origin trabajo/alcance
```

Abrir una solicitud de revisión y explicar qué decisión cambia. Si el cambio requiere registros o roadmap, incluirlos en el mismo conjunto. Este ejemplo presupone un remoto `origin` ya configurado; no lo crea.

## Regla editorial y de fuentes

Citar enunciado con página y transcripción con clase, parte y tiempo. Diferenciar hecho, supuesto y propuesta. Usar el mismo ID de capacidad en backlog, estimación y releases. No atribuir a ZEUS los datos del ejercicio financiero de onboarding. Mantener las transcripciones como insumo del reconocimiento de voz y anotar correcciones documentales en un apunte aparte.

## Typst y archivos derivados

Aprobar contenido en Markdown antes de pasarlo al formato final. Los módulos `.typ` del repo se versionan; `build/` contiene salidas locales. La muestra sirve para probar el entorno y no contiene un informe terminado. La [guía de Typst](typst/README.md) explica compilación y extensiones.

## Publicar la copia local

Crear en la plataforma elegida un repositorio **privado y vacío**, sin README inicial. Copiar su URL real y ejecutar desde esta carpeta, sustituyendo el marcador:

```sh
git remote add origin URL_REAL_DEL_REPOSITORIO_PRIVADO
git push -u origin main
```

Invitar a los compañeros con acceso de colaboración. Si el remoto contiene archivos, revisar primero ese historial antes de integrar; no forzar una sobrescritura. No hace falta copiar el historial de otro repositorio para comenzar este espacio.
