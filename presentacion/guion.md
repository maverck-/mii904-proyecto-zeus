# Guion de exposición ZEUS

**Versión para ensayo, 23-10-2026.** Sigue las 12 láminas construidas en Figma Slides con la [pauta de construcción](pauta_construccion.md). Reparto propuesto, por ajustar cuando el equipo acuerde relevos: Maverick 1, 7 y 10; Bryam 2 a 4; Alejandro 5, 6 y 11; Rogelio 8, 9 y 12.

## Lámina 1 · ZEUS: B Modular, piloto y expansión con evidencia

**Maverick** · 1 min

> Buenos días. Somos Bryam González, Alejandro Malvacias, Rogelio Gonzalez y Maverick Gayoso, y hoy presentamos al Comité nuestra recomendación para ZEUS. Proponemos la alternativa B, la plataforma omnicanal modular, desarrollada por etapas. La ruta tiene tres pasos: probamos el flujo completo de retiro en tienda en diez tiendas, evaluamos en el mes cinco si mejora el servicio y ampliamos la cobertura antes de Black Friday solo con esa evidencia y con la operación aceptada. Al final les pediremos autorizar la primera etapa, con condiciones que les permitan mantener, corregir o detener la inversión. Bryam parte con el problema.

## Lámina 2 · Stock y preparación debilitan la promesa al cliente

**Bryam** · 2 min

> Hoy un cliente puede comprar en la web un producto que ya no está disponible. El stock publicado tarda entre 45 y 120 minutos en actualizarse, y la meta estratégica es menos de dos minutos. Por eso 7,8% de los pedidos se cancelan por falta de stock, cuando la meta es bajar de 2%. Y cuando el pedido avanza, su preparación toma en promedio 7,2 horas, frente a una meta de menos de tres. Al final del recorrido, la tienda que entrega tiene visibilidad limitada del estado del pedido digital.
>
> Estos datos vienen del enunciado. Falta saber cuánto pesa cada causa. Pueden influir la sincronización entre sistemas, el stock físico, las esperas de preparación y la capacidad de cada tienda. Las tratamos como hipótesis que el piloto debe contrastar. Esa decisión define cómo medimos el valor, que es lo que vemos ahora.

## Lámina 3 · Primero comprobamos si el piloto mejora el servicio

**Bryam** · 2 min

> La primera decisión que proponemos es comprobar si el piloto mejora el servicio. Lo hacemos en cuatro pasos. Primero entregamos el flujo completo en diez tiendas, al terminar la semana dieciséis. Luego medimos el uso: más de 80% de los retiros deben prepararse con la aplicación, en cada tienda. Después medimos la mejora: una cancelación 20% menor y una preparación 25% menor, ambas frente a una base comparable del propio piloto. Con esa evidencia, en G1, al cierre del mes cinco, el Comité decide ampliar, corregir o detener la inversión.
>
> Estos umbrales son nuestra propuesta para el mes cinco. Las metas finales, menos de 2% de cancelación y menos de tres horas de preparación, se evalúan en el mes doce para la operación cubierta. Si no logramos una base válida para comparar, informamos el resultado como inconcluso y la expansión queda condicionada. Con este criterio de valor podemos comparar las alternativas.

**Nota para preguntas, no se lee:** base en semanas 9 a 12 y uso en 17 a 20, con tiendas no piloto de las mismas familias como comparación concurrente. El piso de 1.000 pedidos por fase es operacional, sin potencia estadística calculada. Si C&C es nuevo, el resultado alternativo se ratifica antes de abrir el piloto (01, anexo A).

## Lámina 4 · B debe justificar su mayor inversión frente a C

**Bryam** · 2 min

> El caso propone tres alternativas. A, el reemplazo integral, cuesta 1.850 millones y puede tardar entre 12 y 18 meses. Supera el techo de 1.500 y el horizonte de doce meses, así que la descartamos con estas restricciones. C, el MVP focalizado, cuesta 800 millones, y B, la plataforma modular, 1.350. Ambas caben bajo el techo.
>
> B y C comparten el núcleo inicial: inventario, pedidos y retiro en tienda. B agrega la devolución elegible y una evolución modular sobre servicios reutilizables. Por eso B tiene que justificar su mayor inversión. Nuestra regla es mantener B si ese valor adicional compensa su costo frente a C con igual cobertura; en caso contrario, recomendamos C. El retorno incremental queda por validar, porque el caso no informa volumen ni margen, y el diseño por etapas nos permite tomar esa decisión con datos del piloto. Alejandro explica cómo vamos a trabajar.

**Nota para preguntas, no se lee:** los tramos 1 y 2 suman 1.020 MM para piloto, expansión y campaña, 220 sobre la referencia de C, sin una comparación a igual cobertura. El modelo de volumen requerido y cobertura efectiva está en el anexo H.

## Lámina 5 · Combinamos control de inversión y entregas pequeñas

**Alejandro** · 2 min

> Para ZEUS proponemos un enfoque híbrido, porque el caso mezcla compromisos estables con aprendizaje. Primero acordamos contratos por hitos, el techo de inversión y tres gates: G0, G1 y G2. Esto responde a que el ERP, los contratos y la seguridad exigen trazabilidad. Después entregamos y probamos en piezas pequeñas: sprints de dos semanas para el retiro y la app de tienda, y un flujo con límite de trabajo en curso para la integración, que concentra las dependencias. Cada semana ajustamos con los bloqueos, la evidencia y el forecast.
>
> Las dependencias conectan las tres decisiones. Por ejemplo, si se bloquea una API, cambian el release y el forecast. El Product Owner prioriza desbloquearla, y si eso afecta un compromiso de fecha, costo o alcance, el PM lo eleva al Comité. Así la inversión y el trabajo diario se actualizan con la misma evidencia.

## Lámina 6 · Acelerar requiere una operación segura

**Alejandro** · 2 min

> El mandato define quién decide. El Comité y el sponsor deciden la inversión y los cambios mayores de alcance, costo o fecha. El Product Owner ordena el trabajo dentro de esos límites. La salida a producción tiene un control explícito: el CISO y Operaciones pueden detenerla ante un riesgo crítico o una tienda que no puede operar.
>
> El caso describe tensiones entre interesados, y aquí mostramos la regla para dos de ellas. El sponsor quiere velocidad, mientras Operaciones y el CISO buscan estabilidad y seguridad: ajustamos funcionalidad, cobertura o fecha antes de omitir una condición de salida. Comercial empuja nuevas funcionalidades y Tecnología necesita integración: protegemos stock, integración y controles, y las mejoras opcionales compiten por la capacidad disponible. Las tensiones de Finanzas y de los gerentes de tienda las retomamos en recursos y en el roadmap. Maverick sigue con el alcance.

## Lámina 7 · El primer flujo termina con el retiro en tienda

**Maverick** · 3 min

> El primer flujo termina cuando el cliente retira su pedido en la tienda. Tiene cuatro pasos: el stock se reserva sobre un inventario conciliado, el pedido queda trazable en la gestión de pedidos, la tienda lo prepara con una app y una ventana fija de retiro, y se registra la entrega. En cada tienda aplicamos además cinco condiciones: formación, stock conciliado, controles, soporte y la posibilidad de revertir.
>
> El piloto es acotado: diez tiendas, un centro de distribución y dos familias de productos, con la primera salida al terminar la semana dieciséis. Elegimos las familias por su peso en pedidos digitales, cancelaciones y contribución, y por tener stock auditable.
>
> Después de G2 viene R3. Incluye la devolución elegible, que sostiene la meta de 85% de resolución al primer contacto en esos casos, y un experimento de despacho desde tienda en tres a cinco tiendas, con un máximo de cuatro semanas o trescientos pedidos. El Comité debe autorizar antes el techo monetario de ese experimento.
>
> La frontera también está definida. El ERP se conserva y el WMS, el sistema de almacén, se adapta con cambios acotados. Quedan fuera la inteligencia artificial, una data platform completa, los cupos dinámicos y la búsqueda automática de otro punto de retiro. Así respondemos tres preguntas del enunciado: la IA queda para una etapa posterior, los datos entran como habilitador mínimo y el despacho desde tienda se prueba como experimento después del primer release. Rogelio explica cómo ordenamos este trabajo.

**Nota para preguntas, no se lee:** el 85% aplica a devoluciones elegibles de compras web de las familias cubiertas; el 90% estratégico mide otra población, así que la diferencia de cinco puntos compara poblaciones distintas (01, 04).

## Lámina 8 · Integración y stock habilitan el retiro en tienda

**Rogelio** · 2 min

> Para ordenar las épicas usamos un puntaje que combina valor, urgencia, reducción de riesgo y esfuerzo. Ese puntaje ordena las opciones, y las dependencias fijan qué puede empezar. Primero va la integración con ERP, WMS y POS, con contratos de interfaz. Sobre ella construimos un stock y una reserva consistentes, que nos permiten prometer. Luego viene la gestión de pedidos, con estados trazables y conciliación. El retiro en tienda y la app tienen el mayor valor visible y salen cuando lo anterior funciona. El trabajo compatible avanza en paralelo cuando las interfaces ya están acordadas.
>
> Tres condiciones acompañan el flujo desde el inicio, aunque su puntaje sea menor: seguridad, observabilidad mínima y adopción con formación. Forman parte de cualquier salida a producción.

**Nota para preguntas, no se lee:** la matriz WSJF y su sensibilidad están en 05 y en el anexo C. Con medias PERT en el denominador cambian los pares E1/E4, E2/E3 y E10/E9; la secuencia se mantiene por dependencia y obligatoriedad.

## Lámina 9 · El presupuesto llega al límite del caso

**Rogelio** · 3 min

> El presupuesto que proponemos tiene una base de 1.330 millones y una reserva de 170, en total 1.500, exactamente el techo del caso. La estimación de esfuerzo, 104 equipo-sprints frente a una capacidad de 120, está en el anexo; aquí nos concentramos en el dinero.
>
> También probamos un escenario de estrés. Si los equipos cuestan 20% más y cada categoría llega a su extremo alto, el costo sube a 1.668 millones, 168 sobre el techo. Eso supera la reserva. Para volver bajo el techo se necesitan tres condiciones a la vez: diferir los opcionales, reducir capacidad cancelable después de G2 y obtener topes de precio para la gestión de pedidos, el WMS y el cloud. Con las tres, el escenario queda en 1.497,1 millones, con un margen de 2,9. Ese margen es estrecho y las condiciones todavía deben negociarse. Si fallan, el Comité revisa cobertura, arquitectura o la alternativa C antes de superar los 1.500. Todas estas cifras son supuestos del ejercicio, sin cotizaciones.

**Nota para preguntas, no se lee:** escalera 1.668 → 1.602,0923 con un equipo menos durante 8,5 sprints tras G2 → 1.542,0923 con OMS a 180 → 1.512,0923 con WMS a 70 → 1.497,0923 con cloud a 85. Son 130 equipo-sprints pagados, 120 efectivos y 840 MM exactos (06, base de ejecución, anexo D).

## Lámina 10 · La expansión depende de tiendas listas para operar

**Maverick** · 3 min

> Con esos recursos, el calendario queda así. En los meses uno y dos preparamos la base y probamos la integración; al cierre del mes dos, la revisión técnica VT-01 confirma si las interfaces sostienen el piloto. El piloto sale al terminar la semana dieciséis, en el mes cuatro, y G1 decide al cierre del mes cinco. Si G1 lo autoriza, expandimos en los meses seis y siete en cuatro olas: pasamos de diez tiendas a veinticinco, cuarenta, cincuenta y cuatro y sesenta y ocho. Al cierre del mes siete, la revisión VE-01 confirma la preparación para la campaña, y desde ahí congelamos cambios hasta el fin de Black Friday, aproximadamente en el mes ocho. R3 comienza después de G2, en el mes nueve.
>
> La expansión depende de tiendas listas para operar. Proponemos cuatro células de habilitación, y cada tienda se acepta con soporte antes de pasar a la siguiente. Las sesenta y ocho tiendas son una meta condicionada: si el piloto muestra que una tienda toma más tiempo, ajustamos olas o cobertura antes de comprometer la campaña. Estas ventanas tienen poco margen y requieren especialistas disponibles y un sexto equipo desde la semana nueve. La operación diaria de cada tienda, por turno, necesita su propia capacidad aceptada. Alejandro presenta qué hacemos si falla alguna de estas condiciones.

**Nota para preguntas, no se lee:** habilitación y acompañamiento suman 145 persona-días frente a 150 disponibles, en 35 de 40 días hábiles. El corte del piloto usa 36 de 38 equipo-sprints y R2, 23 de 24 (base de ejecución, 07, anexo E).

## Lámina 11 · Si falla una condición, corregimos antes de ampliar

**Alejandro** · 2 min

> Identificamos tres condiciones que pueden frenar la escala, y para cada una definimos una señal, una respuesta y quién decide. La primera es la integración: si la prueba de interfaces falla en VT-01, al cierre del mes dos, reestimamos la integración y la fecha del piloto antes de comprometerlo; Tecnología y Arquitectura lo resuelven y el PM lo eleva al Comité. La segunda es el stock físico: si las discrepancias impiden reservar con confianza, Logística y Tiendas corrigen conteos y conciliación antes de abrir o ampliar. La tercera es la capacidad de cada tienda: si falta capacidad o soporte en un sitio, Operaciones detiene nuevas altas y ajusta olas o cobertura, y si eso cambia la meta, decide el sponsor con el Comité.
>
> En los tres casos, la respuesta queda en el mismo plan y actualiza alcance, costo, fecha y beneficio antes de seguir. Rogelio cierra con la decisión que pedimos.

## Lámina 12 · Pedimos autorizar la primera etapa

**Rogelio** · 1 min

> Pedimos al Comité autorizar la primera etapa: 675 millones para R0 y R1, entre los meses uno y cinco. La autorización tiene tres condiciones. Primero, verificar la integración en VT-01, al cierre del mes dos, antes de exponer el piloto. Segundo, evaluar el piloto en diez tiendas, con la decisión de G1 al cierre del mes cinco. Tercero, liberar los tramos siguientes, 345 millones en G1 y 310 en G2, solo con evidencia de valor, costo y capacidad; la reserva de 170 la administra el Comité. Antes de comprometer gasto conciliaremos categorías, meses y obligaciones contractuales. Quedamos atentos a sus preguntas.
