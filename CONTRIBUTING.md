# Cómo trabajar juntos

Cada entregable tiene un archivo canónico en `trabajo/`. Integrar los aportes existentes, revisar supuestos y actualizar dependencias cuando cambia una decisión. El reparto sugerido está en [EQUIPO.md](EQUIPO.md) y requiere acuerdo.

## Entrar al repositorio

El repositorio es público y puede leerse o clonarse sin invitación. Para subir ramas al repositorio, aceptar una invitación de colaboración con la cuenta correcta. Quien no tenga permisos puede usar un fork y proponer una solicitud de revisión. Para clonar:

```sh
git clone https://github.com/maverck-/mii904-proyecto-zeus.git
cd mii904-proyecto-zeus
```

Para cambios pequeños también se puede editar Markdown desde GitHub: abrir el archivo, editar y proponer el cambio en una nueva rama con solicitud de revisión. El contenido puede leerse sin instalar Typst.

## Trabajar en una rama

Antes de empezar, comprobar cambios locales, actualizar `main` y crear una rama del frente:

```sh
git status
git switch main
git pull --ff-only
git switch -c trabajo/alcance
```

Si hay cambios sin guardar, registrarlos o resolverlos antes de cambiar de rama; no descartarlos para actualizar. Elegir un nombre distinto si esa rama ya existe.

Después de editar y revisar:

```sh
python3 scripts/verificar.py
git add trabajo/04_alcance_y_backlog.md
git commit -m "Ajusta alcance y dependencias del primer release"
git push -u origin trabajo/alcance
```

Abrir una solicitud de revisión hacia `main`, explicar la decisión y pedir revisión de otro integrante. Si cambia costo, objetivo, cobertura o hito, incluir en el mismo conjunto el registro y los demás archivos afectados. Usar la plantilla disponible. Integrar después de revisar y resolver contradicciones.

## Cómo formular un aporte

Citar enunciado por página y transcripción por clase, parte y tiempo. Diferenciar hecho del caso, propuesta, supuesto y acuerdo del grupo. Conservar IDs CAP/PAQ/KPI. Los costos por rangos son un escenario académico y se pueden corregir con fundamento; no son cotizaciones. Las transcripciones mantienen las palabras reconocidas, con aclaraciones en los documentos de trabajo.

Un ítem de backlog sigue propuesto hasta acordar su inclusión. No sustituir los datos del retail por cifras del ejercicio financiero de onboarding. Una comprobación del script valida operaciones/documentos, no factibilidad empresarial.

También se puede aportar una sección desde Word o Google Docs, indicando el documento afectado, el texto propuesto y las dudas pendientes. Quien integra lleva el cambio al Markdown canónico y pide revisión del contenido incorporado. No hay sincronización automática: resolver diferencias antes de generar una versión para entregar y evitar copias finales contradictorias. No es necesario cambiar de herramienta para participar.

## Archivos derivados y Typst

Editar contenido en Markdown. Decidir si habrá informe antes de pasarlo al formato final. Versionar módulos propios `.typ`; guardar compilaciones en `build/`, ignorado por Git. La muestra técnica y su compilación están en [Typst](typst/README.md).

## Accesos para el equipo

La lectura es pública. El propietario invita desde la configuración del repositorio, sección de colaboradores/acceso, para otorgar permisos de escritura al equipo. Usar las cuentas de GitHub confirmadas por cada integrante y el nivel de colaboración acordado. Una invitación pendiente debe aceptarse para activar esos permisos. Confirmar que todos puedan proponer cambios antes del cierre.
