# Resumen ejecutivo

Recomendamos al Comité Ejecutivo de M-GesPro Retail desarrollar ZEUS con la alternativa B, plataforma omnicanal modular, mediante un enfoque híbrido y por etapas. La primera etapa construye un flujo completo de compra digital con retiro en tienda en diez tiendas, un centro de distribución y dos familias de productos. Con la evidencia de ese piloto, el Comité decide en el mes cinco si amplía la cobertura hacia las 68 tiendas antes de Black Friday, si corrige el plan o si detiene la inversión.

La propuesta respeta las condiciones del caso: techo preliminar de 1.500 MM CLP, horizonte de 12 meses, primera entrega de valor dentro de los primeros cinco meses, Black Friday aproximadamente en el mes ocho, ERP sin reemplazo, WMS sin reemplazo completo y continuidad de tiendas y e-commerce (enunciado, p. 5).

| Elemento | Propuesta |
|:-----------------|:------------------------------------------------------------|
| Alternativa | B modular, por etapas, porque reduce las integraciones punto a punto que pide el caso |
| Primera salida | Flujo completo en 10 tiendas al terminar la semana 16 (mes 4) |
| Decisión de valor | G1 al cierre del mes 5, con umbrales de uso y mejora frente a base comparable |
| Expansión | Meta condicionada de 68 tiendas en el mes 7, en cuatro olas con cuatro células |
| Campaña | Congelamiento de cambios desde VE-01 hasta el fin de Black Friday |
| Evolución | Devolución elegible y experimento acotado de despacho desde tienda, tras G2 |
| Operación y soporte | Dueño del servicio y tres niveles de soporte desde el piloto; traspaso a un equipo estable en el mes 12 |
| Presupuesto | Base de 1.330 MM más reserva de 170 MM, igual al techo de 1.500 MM |
| Solicitud | Primer tramo de 675 MM para R0 y R1, sujeto a VT-01 y G1 |

::: franja
**Estado de las cifras.** Los datos del caso citan la página del enunciado. Metas, umbrales, esfuerzo, costos y calendario son propuestas y supuestos del equipo consultor, sin cotizaciones, contratos ni resultados ejecutados.
:::

## Decisiones que defendemos

| Pregunta del enunciado, p. 8 | Respuesta |
|:-----------------------|:------------------------------------------------------------|
| Capacidades del proyecto inicial | Inventario y reserva, gestión de pedidos, retiro en tienda con app de preparación, controles, observabilidad mínima, soporte y adopción. Devolución elegible en R3. |
| Inteligencia artificial | Queda para una etapa posterior. Esta hipótesis de valor no la necesita y depende de datos que hoy son inconsistentes. |
| Data Platform | Habilitador mínimo: eventos de stock y pedidos, y tableros para los gates. La plataforma corporativa completa queda fuera. |
| Ship-from-store en el primer release | No. Entra como experimento acotado en R3, en 3 a 5 tiendas, tras autorización en G2. |
| Compromisos fijos y adaptables | Fijos: restricciones del caso, controles, techo y gates. Adaptables: detalle del backlog, UX, selección de tiendas y ritmo de olas dentro de límites. |
| Evidencia para mantener, cambiar o detener | VT-01 (interfaces), G1 (uso y mejora), aceptación por sitio, VE-01 (campaña) y G2 (beneficio, costo y forecast). |

# 1. Diagnóstico estratégico y Business Case

## 1.1 Problema y oportunidad

M-GesPro Retail opera 68 tiendas y 3 centros de distribución, con 24% de sus ventas en canal digital (enunciado, p. 3). Sus sistemas se integran mediante procesos batch, archivos e interfaces punto a punto. El resultado es una promesa omnicanal poco confiable: el stock publicado tarda entre 45 y 120 minutos en actualizarse, 7,8% de los pedidos se cancela por falta de stock, la preparación promedio toma 7,2 horas y solo 64% de las devoluciones se resuelve en el primer contacto (p. 4). Además, las tiendas tienen visibilidad limitada del estado de los pedidos digitales (p. 3).

Separamos el problema de la solución. Pueden contribuir a la brecha la sincronización entre sistemas, el stock físico, las esperas de preparación, la capacidad de cada tienda y las conciliaciones. El enunciado no permite separar el peso de cada causa, por eso las tratamos como hipótesis que el piloto debe contrastar. Logística y Operaciones son corresponsables del resultado junto con Tecnología.

La oportunidad es construir una experiencia omnicanal confiable con servicios reutilizables, conservando ERP y WMS, y coordinando personas, operación y tecnología (pp. 3 a 5).

## 1.2 Drivers estratégicos y métricas

Los drivers son crecimiento digital, cumplimiento de promesas, eficiencia de preparación, calidad de atención y continuidad operativa.

| Indicador del caso | Actual | Meta estratégica |
|:--------------------------------|---------:|---------:|
| Ventas digitales sobre ventas totales | 24% | 35% |
| Pedidos entregados a tiempo | 82% | ≥ 95% |
| Cancelaciones por falta de stock | 7,8% | < 2% |
| Exactitud de inventario | 91% | ≥ 98% |
| Actualización de stock web | 45 a 120 min | < 2 min |
| Preparación promedio de pedido | 7,2 h | < 3 h |
| Devoluciones resueltas en primer contacto | 64% | ≥ 90% |
| Disponibilidad e-commerce | 99,3% | ≥ 99,9% |
| NPS canal digital | +32 | ≥ +48 |
| Abandono de carro | 67% | < 55% |

Fuente: enunciado, p. 4. ZEUS contribuye a estas metas corporativas. La atribución de cada mejora a ZEUS se mide con la cobertura y las cohortes definidas en la sección 1.5.

## 1.3 Alternativas evaluadas

| Criterio | A · Reemplazo integral | B · Plataforma modular | C · MVP focalizado | Diferir |
|:------------------|:-----------------|:-----------------|:-----------------|:-----------------|
| Referencia del caso | 1.850 MM, 12 a 18 meses | 1.350 MM, 9 a 12 meses | 800 MM, 5 a 7 meses | Sin monto |
| Techo y horizonte | Excede el techo y puede exceder el horizonte | Compatible; propuesta de 1.330 más reserva de 170 | Compatible; costo a igual cobertura por definir | Conserva caja y el costo de oportunidad |
| Valor en el mes 5 | Requiere un corte temprano no demostrado | Piloto R1 con medición propuesta | Requiere un corte temprano equivalente | Sin mejora |
| Black Friday | Cambio amplio, alta exposición | Olas condicionadas a operación aceptada | Debe presupuestar campaña e integración | Mantiene la exposición actual |
| Integración | Reemplaza componentes con una suite | Capa de APIs reutilizable sobre ERP y WMS | Más conexiones sobre los mismos sistemas | La complejidad continúa |
| Evolución | Suite frente a ERP conservado | Contratos reutilizables y devolución elegible | Su descripción no incluye la capa de APIs; sumarla amplía alcance y costo | Sin evolución |

Fuente: enunciado, pp. 3, 5 y 7; evaluación del equipo.

**Recomendación.** Desarrollar B por etapas. El enunciado señala que cada nueva integración incrementa la complejidad tecnológica y las dependencias, y fija como condición de arquitectura reducir las integraciones punto a punto y avanzar hacia servicios y APIs reutilizables. B responde a esa causa con una capa de APIs sobre ERP y WMS, que sostiene el núcleo de inventario, pedidos y retiro en tienda, la devolución elegible y las capacidades siguientes. C resuelve el mismo núcleo inicial, pero su descripción no incluye esa capa, y para cumplir la condición de arquitectura tendría que ampliar su alcance y su costo de referencia. Los tramos 1 y 2 suman 1.020 MM para piloto, expansión y campaña. El retorno de B se confirma con el piloto y en cada gate, porque el caso no informa volumen ni margen. Descartamos A porque excede el techo y el horizonte.

## 1.4 Entregables, resultados, beneficios y valor

| Output | Outcome | Beneficio medible | Valor estratégico y condición |
|:----------------|:----------------|:----------------|:----------------------|
| APIs, inventario y reserva, gestión de pedidos integrada | Clientes y operación usan una disponibilidad consistente | Menos cancelaciones y reclamos | Crecimiento confiable, si los datos físicos y la integración son correctos |
| Retiro en tienda y app de preparación | El personal prepara con estados y promesas visibles | Menor tiempo de preparación, más pedidos cumplidos | Eficiencia, si hay capacidad y adopción en cada tienda |
| Devolución elegible omnicanal | Atención resuelve con trazabilidad y reglas comunes | Mayor resolución al primer contacto | Satisfacción y costo de servir; meta de proyecto de 85% en casos elegibles |
| Observabilidad, controles y soporte | Incidentes detectados y atendidos; salidas operables | Menor exposición y servicio estable | Resiliencia y sostenibilidad desde R1 |

**Hipótesis de valor.** Si los datos de inventario, reserva y pedido son consistentes y las tiendas adoptan el proceso con capacidad suficiente, bajarán las cancelaciones y el tiempo de preparación. Una devolución integrada puede elevar la resolución en primer contacto. Si la mejora se confirma y compensa sus costos y riesgos, contribuye al crecimiento digital y a la experiencia de compra.

## 1.5 Objetivos y medición

| ID | Indicador propuesto | Objetivo del proyecto | Dueño propuesto |
|:------|:----------------------------|:--------------------|:--------------|
| KPI-01 | Cancelaciones por stock sobre pedidos aceptados comparables | < 2% en el mes 12, operación cubierta | Comercial y Logística |
| KPI-02 | Tiempo desde cambio confirmado de inventario hasta publicación web | < 2 min en el mes 12, interfaces cubiertas | Tecnología y Operaciones |
| KPI-03 | Tiempo desde pedido confirmado hasta listo para retiro, por flujo | < 3 h en el mes 12, operación cubierta | Logística y Tiendas |
| KPI-04 | Devoluciones elegibles resueltas en primer contacto | ≥ 85% en el mes 12; referencia corporativa ≥ 90% | Operaciones y Comercial |
| KPI-05 | Disponibilidad de servicios ZEUS críticos, con prueba transaccional | ≥ 99,9%, con seguimiento del e-commerce completo | Tecnología y Operaciones |
| KPI-06 | Retiros preparados con la app sobre retiros de la cohorte | > 80% en el piloto y en cada ola | Operaciones y Tiendas |

La meta de 85% en devoluciones aplica a compras web elegibles de las familias cubiertas. El 90% estratégico mide otra población, de modo que ambas cifras se reportan por separado.

**Criterios para G1, mes 5.** Proponemos como criterios una reducción relativa de al menos 20% en la cancelación y de al menos 25% en el tiempo de preparación, ambas frente a una base comparable del piloto, una adopción superior a 80% por tienda y un servicio operable. La base se mide en las semanas 9 a 12 y el uso en las semanas 17 a 20, con tiendas no piloto de las mismas familias como comparación concurrente. El piso operacional es de 1.000 pedidos elegibles por fase. Si el retiro en tienda es un flujo nuevo sin base comparable, el resultado alternativo se ratifica antes de abrir el piloto. Sin base válida, el resultado se informa como inconcluso.

## 1.6 Costos, financiación y riesgos

El presupuesto propuesto es de 1.330 MM de base más 170 MM de reserva, igual al techo del caso. Se libera en tres tramos: 675 MM en G0 (mes 1), 345 MM en G1 (mes 5) y 310 MM en G2 (mes 9). La reserva la administra el Comité. El detalle de esfuerzo, categorías y respuesta al estrés está en la sección 6.

Los riesgos principales son la integración con ERP y WMS, la exactitud del stock físico, la dependencia del proveedor WMS, la capacidad de tiendas y equipos, la carga de campaña, el sobrecosto y la seguridad (anexo B).

## 1.7 Evidencia económica para decidir

El caso no informa volumen de pedidos, margen ni flujos, por lo que el retorno de ZEUS queda por validar con datos del piloto. Proponemos decidir con el volumen requerido para recuperar la inversión.

| Fórmula | Uso |
|:------------------------------------------|:------------------------------|
| Pedidos adicionales por mes = (I / H + O − A) / m | Volumen que recupera la implementación I en H meses, con recurrente adicional O, ahorro A y contribución m por pedido |
| Recuperación por cancelación = Vd × sP × f × (q0 − q1) | Pedidos recuperados según volumen digital, participación de las dos familias, fracción cubierta y caída de la cancelación |

Con supuestos ilustrativos (I de 1.500 MM, O de 9 MM al mes, m de 8.000 CLP por pedido y A igual a cero), el equilibrio operativo exige 1.125 pedidos adicionales al mes, recuperar en 36 meses exige 6.334 y en 60 meses, 4.250. Estas cifras muestran la mecánica y no constituyen un forecast de ZEUS. En G1 y G2 se comparan con el volumen cubierto, el margen y la capacidad de tienda.

La literatura revisada asocia una logística confiable con más ventas y advierte que prometer más de lo que se cumple aumenta devoluciones y reduce retención (anexo E). Los estudios son de despacho en marketplaces y su transferencia al retiro en tienda es limitada. Por eso la hipótesis de R1 se acota a disponibilidad confiable, preparación y cumplimiento de la ventana de retiro.

# 2. Selección y tailoring del enfoque

## 2.1 Recomendación

Recomendamos un enfoque híbrido. ZEUS combina compromisos estables (inversión, contratos, ERP, seguridad, campaña) con aprendizaje sobre integración, experiencia de retiro y adopción en tiendas. El gobierno formal define límites y autoridad; la entrega adaptativa prueba soluciones y actualiza el forecast.

## 2.2 Comparación de lógicas

| Lógica | Aporte a ZEUS | Condición que debe resolver |
|:------------------|:----------------------------|:----------------------------|
| Predictiva predominante | Interfaces, contratos, aceptación y preparación comercial con secuencia controlada | Aplazar la validación técnica o de usuarios aumenta el retrabajo; requiere pruebas tempranas |
| Ágil predominante | Incrementos de retiro en tienda, integración y adopción ajustados con feedback | Debe coordinar contratos, dependencias entre sistemas y autorizaciones de inversión |
| Híbrida, recomendada | Controles ejecutivos y contractuales junto con pruebas técnicas, flujo e incrementos | Exige un único roadmap y reglas de decisión compartidas |

## 2.3 Qué necesita estabilidad y qué requiere aprendizaje

| Componente | Lógica | Justificación |
|:----------------------|:----------------------------|:----------------------------|
| ERP, contabilidad y conciliaciones | Gobierno predictivo de interfaz y aceptación, con pruebas técnicas tempranas | Alta exigencia de trazabilidad; la viabilidad de APIs no se asume |
| Contratos WMS y OMS | Hitos contractuales, aceptación y compra escalonada | El proveedor WMS planifica de forma tradicional (p. 7) |
| Seguridad y accesos | Controles formales y validación en cada incremento | Obligatorios desde el inicio (p. 5) |
| Black Friday | Plan de preparación, dependencias, capacidad y salida operable | Fecha externa crítica, aproximadamente en el mes 8 |
| APIs y disponibilidad | Kanban con límites de trabajo en curso por especialidad | Flujo con dependencias y bloqueos que deben verse |
| Retiro, app y devoluciones | Scrum con sprints de dos semanas y feedback de tiendas y PO | Aprender sobre flujo y adopción con usuarios reales |
| Ship-from-store | Experimento acotado en R3 | Hipótesis operacional con límites, criterios de aprendizaje y reversión |

Son estables el propósito, el techo, las restricciones del caso, los gates y los controles. Son adaptables el detalle de cada release, el orden del backlog, el diseño de experiencia, la selección de tiendas y el ritmo de olas. Un cambio de cobertura comprometida pasa por el sponsor y el Comité.

## 2.4 Controles formales y retroalimentación

- Gates de financiación G0 (mes 1), G1 (mes 5) y G2 (mes 9), y cierre en el mes 12.
- Revisión técnica VT-01 al final del mes 2 y revisión de preparación VE-01 al final del mes 7.
- Control de cambios para techo, financiación, alcance mayor y fechas comprometidas, con su efecto en beneficios.
- Arquitectura y seguridad antes de cada release; observabilidad, soporte y reversión desde R1.
- Revisión de sprint cada dos semanas con tiendas piloto y PO de e-commerce; revisión semanal de flujo y bloqueos; foro semanal de integración con PM, PO y Arquitectura.

En la revisión semanal, PO y equipos presentan terminados, bloqueos y evidencia; PM y Arquitectura actualizan dependencias y forecast. Si cambia un compromiso de costo, cobertura, fecha o beneficio, el PM eleva el impacto al Comité antes de modificar la referencia aprobada.

## 2.5 Flujo y bloqueos

Para la integración proponemos políticas explícitas: cada ítem entra con interfaz, dueño y criterio de aceptación; los límites de trabajo en curso se acuerdan por especialidad; los bloqueos quedan visibles con responsable. Si un bloqueo crítico frena el flujo, se detienen los nuevos inicios que alimentan ese cuello y se prioriza desbloquear. El ítem bloqueado sigue contando como trabajo en curso y el PM escala si amenaza un hito (clase 4, parte 2).

## 2.6 Adopción de las prácticas

El caso describe una madurez ágil desigual (p. 5). En R0 se revisan experiencia, disponibilidad de PO y tiendas, y capacidad de los equipos. Se acuerda una forma inicial de trabajo con entrada al backlog, criterios de aceptación, definición de terminado, responsables, límites de trabajo en curso y tratamiento de bloqueos, y se practica con el primer flujo real. Una función de facilitación acompaña a los equipos. Las prácticas se ajustan según terminados, esperas y utilidad del feedback.

# 3. Project Charter

## 3.1 Propósito y sponsor

**ZEUS: Plataforma Omnicanal Modular.** Construir una plataforma que integre inventario, pedidos, tiendas y devoluciones mediante servicios reutilizables, para ofrecer una experiencia omnicanal consistente y reducir la complejidad de integración. **Sponsor:** Gerente General.

ZEUS contribuye a las metas de 35% de ventas digitales, NPS ≥ +48, entregas a tiempo ≥ 95% y abandono de carro < 55%. Sus objetivos medibles son KPI-01 a KPI-06 (sección 1.5).

## 3.2 Alcance inicial

**Incluye:** gestión de pedidos adquirida, configurada e integrada; inventario, reserva y disponibilidad mediante APIs; pedidos trazables; retiro en tienda con app de preparación; formación y adopción; controles, observabilidad mínima, continuidad y soporte desde R1; expansión por olas; devolución elegible y ampliación de observabilidad en R3; experimento acotado de despacho desde tienda, condicionado a G2.

**Excluye:** reemplazo del ERP o reemplazo completo del WMS, IA y recomendaciones, data platform corporativa completa, migración amplia a cloud y nueva plataforma de identidad de clientes. Los controles de identidad y acceso obligatorios se mantienen. Cloud selectivo se usa solo si el flujo lo necesita y está costeado.

## 3.3 Entregables por release

| Release | Entregable | Condición |
|:--------------|:------------------------------------|:------------------------------------|
| R0, meses 1 y 2 | Arquitectura, contratación OMS por hitos, prueba de integración y base de medición | VT-01 al final del mes 2 |
| R1, hasta el mes 5 | Retiro en tienda en 10 tiendas, 1 CD y 2 familias; salida al terminar la semana 16 | G1 con evidencia de uso y mejora |
| R2, meses 6 y 7 | Expansión hacia 68 tiendas, hasta 3 CD, mismas familias; preparación de campaña | Meta condicionada; cada sitio aceptado; VE-01 |
| Campaña, mes 8 | Operación estable y soporte durante Black Friday | Congelamiento desde VE-01 |
| R3, meses 9 a 12 | Devolución elegible, observabilidad centralizada y experimento de despacho desde tienda | G2 autoriza financiación y techo del experimento |

## 3.4 Roles y derechos de decisión

| Rol | Responsabilidad y derecho de decisión |
|:----------------------|:------------------------------------------------------------|
| Comité Ejecutivo | Gates, financiación y cambios de la referencia aprobada que afecten inversión o beneficio |
| Sponsor, Gerente General | Propósito, prioridades y cambios mayores de fecha o alcance dentro de las restricciones |
| PM de ZEUS | Coordina frentes, dependencias, riesgos, cambios y forecast |
| PO e-commerce y representante de tiendas | Priorizan el backlog de cada release dentro de los límites acordados |
| Gerente de Tecnología y Arquitectura | Integración, estándares y desacoplamiento compatibles con la continuidad |
| CISO | Controles de seguridad y facultad de detener una salida ante riesgo crítico |
| Operaciones, Logística y gerencias de tienda | Beneficios, dotación y aceptación operacional; pueden impedir una salida no operable |
| Operación y soporte del servicio | Dueño del servicio en Tecnología; coordina referentes, mesa de ayuda, soporte de aplicación y guardia de plataforma, y recibe el servicio al cierre |
| Finanzas | Costo total, forecast, reservas y liberación de tramos con el Comité |
| Proveedores WMS, OMS y cloud | Compromisos, integración, licencias y soporte según contrato |

## 3.5 Interesados y reglas ante tensiones

El anexo C recoge los trece interesados del caso con su interés, tensión y respuesta. Proponemos estas reglas para las tensiones principales:

| Tensión | Regla propuesta | Quién decide |
|:------------------------|:----------------------------------|:----------------------|
| Velocidad del sponsor frente a estabilidad y seguridad | Ajustar funcionalidad, cobertura o fecha antes de omitir una condición de salida | Sponsor y Comité; CISO y Operaciones pueden bloquear |
| Funcionalidad comercial frente a integración y deuda técnica | Proteger stock, integración y controles; los opcionales compiten por capacidad | Comercial, PO y Tecnología; Comité ante cambios mayores |
| Autonomía de PO y equipos frente a estándares | Decidir el detalle dentro de estándares, con una sola evidencia de calidad por salida | PO y equipos; Arquitectura y CISO según riesgo |
| Escalabilidad cloud frente a inversión y continuidad | Justificar cloud selectivo por necesidad y costo total | Tecnología y Arquitectura proponen; Finanzas, CISO y Operaciones revisan |
| Expansión comercial frente a capacidad de tiendas y WMS | Aceptar cada sitio con turnos, stock, formación, interfaces y soporte | Operaciones acepta; el PM escala efectos en olas o fecha |

## 3.6 Restricciones, supuestos y riesgos iniciales

**Restricciones del caso:** techo preliminar de 1.500 MM, 12 meses, valor dentro de los primeros cinco meses, Black Friday aproximadamente en el mes 8, ERP sin reemplazo, WMS solo modificable, continuidad de e-commerce y tiendas, y controles de seguridad obligatorios (p. 5).

**Supuestos principales:** el ERP expone información mediante APIs o eventos, el proveedor WMS cumple plazos, se adquiere un OMS de mercado, la dotación escalonada de equipos está disponible y las tiendas piloto pueden operar el nuevo flujo (anexo A).

**Riesgos iniciales:** exactitud de stock insuficiente (91% corporativo), retrasos del proveedor WMS, capacidad de tiendas y equipos, carga de campaña, sobrecosto y bloqueo por seguridad (anexo B).

## 3.7 Hitos y criterios de salida

| Hito | Momento | Condición de salida |
|:----------|:----------------|:------------------------------------------------------------|
| G0 | Mes 1 | Arquitectura inicial, financiación del primer tramo y contratación OMS por hitos |
| VT-01 | Fin del mes 2 | Interfaces, datos y recuperación probados antes de exponer el piloto |
| G1 | Fin del mes 5 | Evidencia de primera entrega de valor y decisión de ampliar con capacidad y costo revisados |
| VE-01 | Fin del mes 7 | R2 aceptado, cobertura segura y preparación de campaña; inicia el congelamiento |
| Campaña | Mes 8 | Continuidad y promesas protegidas, con excepciones críticas controladas |
| G2 | Inicio del mes 9 | Beneficios y forecast actualizados; autorización de R3 |
| Cierre | Mes 12 | Aceptación, traspaso a un equipo estable de operación y producto, y responsables de los beneficios pendientes |

**Criterios de éxito:** objetivos medidos según la sección 1.5, adopción superior a 80%, ejecución dentro del costo autorizado y del techo, riesgos críticos de seguridad tratados y campaña operable.

## 3.8 Autorización solicitada

Solicitamos al Comité el primer tramo de **675 MM CLP** para R0 y R1, entre los meses 1 y 5, dentro de un financiamiento por etapas de 1.330 MM más 170 MM de reserva. Proponemos tres condiciones: verificar la integración en VT-01 antes de exponer el piloto, evaluar el piloto en G1 y liberar los tramos siguientes solo con evidencia de valor, costo y capacidad. Antes de comprometer gasto se concilian categorías, meses y obligaciones contractuales.

# 4. Diseño del alcance

## 4.1 Alcance de producto y de proyecto

| Vista | Contenido |
|:------------|:------------------------------------------------------------|
| Producto | Inventario y reserva, estados de pedido, retiro en tienda con app, devolución elegible, controles y cualidades del servicio |
| Proyecto | Formular, adquirir y configurar, integrar, probar, preparar datos y tiendas, formar, desplegar, medir, transferir soporte y beneficios |

El producto continúa evolucionando tras el mes 12. El proyecto termina con aceptación, transferencia y responsables de los beneficios pendientes.

## 4.2 Cobertura y frontera

El piloto cubre **10 tiendas, 1 centro de distribución y 2 familias de productos**, con salida al terminar la semana 16. La expansión apunta a **68 tiendas en el mes 7**, es decir, 58 altas adicionales, con hasta 3 centros de distribución y las mismas familias. Cubrir 68 tiendas significa habilitar el retiro en tienda para ese catálogo.

Las dos familias se eligen en el mes 1 por su participación en pedidos digitales, cancelaciones y contribución, y por tener stock auditable, rotación y logística estándar. Las tiendas piloto se eligen por volumen evaluable, calidad de stock, turnos, espacio, soporte, diversidad y acceso a interfaces.

Las interfaces cubiertas son ERP, WMS, POS, e-commerce, pagos, logística y CRM en lo que afecten al flujo o la conciliación. Cada una tiene dueño, contrato, prueba, recuperación y soporte.

## 4.3 Proceso logístico y corte de R1

En R0 se mapea el recorrido desde el inventario físico hasta la preparación y el retiro, con esperas, trabajo activo, responsables y excepciones. Se distinguen stock físico, disponible y reservable, y se acuerda quién confirma cada movimiento y concilia diferencias entre WMS, ERP, tienda y gestión de pedidos. El WMS ejecuta en el almacén, la gestión de pedidos coordina el cumplimiento y el transporte ejecuta el despacho.

**Corte de R1.** Reserva simple y ventana fija de retiro comunicada por tienda, con horario de corte y volumen de exposición acordados con Operaciones. Los cupos dinámicos, la optimización de ventanas y la búsqueda automática de otro punto de retiro quedan fuera de R1 y de la estimación.

E1 y E11 incluyen la validación inicial de existencias y el conteo cíclico del catálogo piloto. La regla de stock reservable descuenta reservas vigentes y un colchón configurable aprobado por Logística, calibrado con las discrepancias observadas.

## 4.4 Fijo, adaptable y condicionado

| Tratamiento | Elementos | Regla de decisión |
|:--------------------|:------------------------------------|:------------------------------|
| Restricción del caso | Techo, horizonte, valor en cinco meses, continuidad, controles, ERP conservado, WMS sin reemplazo completo | Se respetan; si no caben, se ajusta el alcance o se eleva la incompatibilidad |
| Compromiso propuesto | Flujo completo en 10 tiendas en el mes 5, objetivos y preparación de campaña | Cambios con impacto en beneficio, costo y fecha, por sponsor y Comité |
| Meta condicionada | 68 tiendas en el mes 7 para el catálogo definido | G1 fija la cobertura previa a campaña con recursos y centros aceptados |
| Adaptable | Historias, experiencia, orden técnico, selección de tiendas y olas | PO y equipos ajustan dentro de límites |
| Diferible | Ruteo avanzado, centralización adicional y experimento de despacho | Se evalúa por costo de oportunidad; la devolución sostiene KPI-04 |

## 4.5 Capacidades y aceptación

| ID | Capacidad | Release | Criterio de aceptación |
|:-------|:------------------------------|:------|:------------------------------------------|
| CAP-01 | Base, arquitectura y viabilidad de integración | R0 | Contrato de datos, prueba representativa, base por cohorte y forecast revisado |
| CAP-02 | Inventario consistente y reservas | R1 | Reserva concurrente, vencimiento y excepciones probados |
| CAP-03 | Gestión de pedidos y trazabilidad | R1 | Estados de confirmación a retiro, idempotencia, conciliación y recuperación |
| CAP-04 | Retiro en tienda y app de preparación | R1 | Retiro real con proceso y dotación aceptados; KPI-03 y KPI-06 medibles |
| CAP-05 | Seguridad, observabilidad y métricas | R0 a R3 | Controles, eventos auditables, alertas atendidas y riesgos críticos tratados |
| CAP-06 | Adopción, continuidad y soporte | R0 a R3 | Formación, dueño operativo, transición, reversión y soporte por sitio |
| CAP-07 | Escala a 68 tiendas y campaña | R2 | Cada ola operable, pruebas de carga y recuperación, VE-01 |
| CAP-08 | Devolución elegible | R3 | Caso completo con conciliación y trazabilidad; KPI-04 medido |
| CAP-09 | Experimento de despacho desde tienda | R3 | 3 a 5 tiendas, máximo 4 semanas o 300 pedidos; resultado documentado |

## 4.6 Estructura de desglose del trabajo

| Paquete | Entregable y frontera de costo | Épicas | Dueño propuesto |
|:---------|:----------------------------------------|:-------------|:----------------|
| PAQ-01 | Formulación, gobierno, arquitectura y viabilidad | Coordinación | PM y Arquitectura |
| PAQ-02 | Integración, inventario, reserva y conciliación | E1, E2 | Tecnología y Logística |
| PAQ-03 | Gestión de pedidos: configuración, interfaces y trazabilidad | E3 | Tecnología y PO |
| PAQ-04 | Retiro en tienda, app y habilitación de las 58 altas | E4, E5, E11 | Operaciones y Tiendas |
| PAQ-05 | Devolución elegible y experimento de despacho | E9, E10 | Operaciones, Comercial y Logística |
| PAQ-06 | Controles, pruebas transversales, rendimiento y observabilidad | E6, E7, E8a, E8b | CISO y Tecnología |
| PAQ-07 | Transición, soporte y recurrentes de licencias y cloud | E7, E11 | Operaciones y Tecnología |

Las capacidades, épicas y paquetes son vistas del mismo trabajo y no se suman entre sí.

## 4.7 Backlog inicial

| Historia | Usuario y resultado | Criterio de aceptación |
|:-------|:------------------------------|:----------------------------------------------|
| HU-01 | El cliente compra sobre stock reservable | Con una unidad y dos solicitudes simultáneas se confirma una sola reserva; la expiración libera el stock y queda trazada |
| HU-02 | Operación sigue un pedido completo | Confirmación, preparación y retiro mantienen identificador y estado conciliable; un evento repetido no duplica el pedido |
| HU-03 | El personal prepara y entrega con la app | Un rol habilitado ve la promesa, cambia estados y registra el retiro; permisos y excepciones probados en tienda |
| HU-04 | Operación atiende fallas de stock o pedido | Se simula la falla, la alerta llega al responsable y se ejecuta recuperación o reversión con conciliación |
| HU-05 | Atención resuelve una devolución elegible | Identifica la compra, aplica regla y restitución acordadas, actualiza pedido y stock, y concilia una sola vez |
| HU-06 | Logística evalúa un despacho desde tienda | Solo acepta tiendas y pedidos del experimento; registra promesa, costo y resultado, y permite detener asignaciones |

## 4.8 Aceptación por sitio y definición de terminado

Cada tienda o centro presenta una lista estándar con datos y reservas, formación por turno, pedido completo probado, conciliación, alertas atendidas, soporte y reversión. Tecnología, CISO y Logística aprueban el patrón de cada release; Operaciones acepta cada sitio mediante referentes delegados. Un sitio pendiente permanece cerrado al nuevo flujo y no cuenta como alta.

La apertura incluye acompañamiento intensivo, con referente local por turno y escalamiento hacia integración y soporte. La célula pasa a otra tienda cuando el referente local y el soporte remoto aceptan el relevo.

La definición de terminado exige criterio funcional, pruebas, controles, telemetría, documentación, soporte, reversión y aceptación operacional. Cumplir la función y la definición de terminado habilita la salida; el beneficio se acredita después con uso y métricas.

## 4.9 Operación y soporte del servicio

El servicio necesita un equipo que lo opere durante el proyecto y después del mes 12. Proponemos un dueño del servicio en Tecnología y tres niveles de soporte.

| Nivel | Quién lo presta | Qué atiende | Con qué crece |
|:----------------|:------------------------------|:------------------------------|:----------------------|
| Primer nivel, tiendas | Referente local por turno en cada tienda habilitada y mesa de ayuda corporativa con guiones de ZEUS | Uso de la app, estados de pedido, retiro y excepciones simples | Tiendas activas, turnos y pedidos diarios |
| Segundo nivel, aplicación | Analistas funcionales de los equipos de producto y soporte del partner OMS | Fallas de flujo, datos, conciliación y configuración | Volumen de incidentes y servicios integrados |
| Tercer nivel, plataforma | Guardia rotativa de los equipos de desarrollo, apoyada en la observabilidad | Disponibilidad, integraciones, eventos y recuperación | Servicios críticos y horario de operación; se refuerza en campaña |

El primer nivel crece con el número de tiendas; el segundo y el tercero crecen con los servicios críticos, por eso no se multiplican por tienda. Durante el proyecto, los equipos que construyen cada servicio también lo operan.

Para el primer nivel proponemos la regla: agentes de mesa por turno = tiendas activas × incidentes por tienda y turno × minutos por incidente / minutos disponibles por agente y turno. Los parámetros se miden en el piloto, entre las semanas 17 y 20, y se recalculan antes de cada ola. La operación participa en la definición de terminado con procedimientos operativos, alertas con responsable, reversión probada y guion de atención. Los incidentes y problemas recurrentes alimentan el backlog de mejoras. Al cierre, el servicio pasa a un equipo estable de operación y producto, con dueño, acuerdos de nivel de servicio y presupuesto recurrente fuera del proyecto.

## 4.10 Experimento de despacho desde tienda

El experimento parte en tres tiendas, se amplía a cinco solo tras una primera semana operable y termina al cumplir cuatro semanas o 300 pedidos elegibles, lo que ocurra primero. Se ejecuta en el mes 11, con stock del catálogo acordado, operador logístico y conciliación definidos. Registra cumplimiento, cancelación, esfuerzo de tienda, transporte y margen incremental. Se detiene ante pérdidas no conciliadas, exposición crítica, promesas insostenibles o perjuicio al retiro en tienda. Antes de iniciar, G2 autoriza su techo monetario de exposición.

# 5. Priorización

## 5.1 Método y criterios

Usamos tres pasos. El WSJF ordena las opciones, las dependencias ajustan la precedencia y la capacidad limita el contenido de cada release. WSJF es el costo del retraso relativo dividido por el tamaño relativo; el costo del retraso suma valor, urgencia y reducción de riesgo o habilitación en la escala 1, 2, 3, 5, 8, 13 y 20.

| Criterio de la pauta | Aplicación en ZEUS |
|:----------------------|:------------------------------------------------------------|
| Valor | Aporte esperado a los KPI del Charter |
| Urgencia | Primera entrega en el mes 5 y campaña en el mes 8 |
| Dependencia y riesgo | Habilitación y reducción de exposición; una precedencia puede adelantar una épica |
| Costo | Tamaño relativo según la media PERT de la sección 6 |
| Incertidumbre | Aprendizaje temprano y experimento acotado |
| Capacidad | 120 equipo-sprints efectivos y carga por periodo |

Seguridad (E6), preparación de campaña (E7), despliegue y cambio (E11) y observabilidad básica (E8a) son condiciones obligatorias y acompañan todo servicio en producción.

## 5.2 Matriz WSJF

| Épica | Valor | Urgencia | Riesgo | Costo del retraso | Tamaño | WSJF |
|:--------------------------------|------:|------:|------:|------:|------:|------:|
| E8a Observabilidad básica | 3 | 13 | 13 | 29 | 3 | 9,7 |
| E4 Retiro en tienda | 20 | 13 | 5 | 38 | 8 | 4,8 |
| E1 Disponibilidad de stock | 20 | 20 | 20 | 60 | 13 | 4,6 |
| E5 App de preparación | 13 | 13 | 8 | 34 | 8 | 4,3 |
| E3 Gestión de pedidos | 13 | 13 | 13 | 39 | 13 | 3,0 |
| E8b Observabilidad centralizada | 3 | 2 | 8 | 13 | 5 | 2,6 |
| E2 Integración ERP, WMS y POS | 8 | 20 | 20 | 48 | 20 | 2,4 |
| E9 Devoluciones | 13 | 3 | 3 | 19 | 8 | 2,4 |
| E10 Experimento de despacho | 5 | 1 | 5 | 11 | 5 | 2,2 |

El tamaño aproxima la media PERT al valor más cercano de la escala. Con medias PERT sin redondear cambian los pares E1/E4, E2/E3 y E10/E9; la secuencia se mantiene porque la deciden las dependencias y la obligatoriedad. E2 y E3 se adelantan a R0 y R1 porque el retiro en tienda depende de ellas.

## 5.3 Secuencia por release

| Release | Contenido | Condición |
|:---------------|:----------------------------------------|:------------------------------|
| R0, meses 1 y 2 | Arquitectura, contratación OMS escalonada, acuerdo WMS, entornos y controles base | G0 y VT-01 |
| R1, hasta el mes 5 | E1, flujos necesarios de E2 y E3, E8a y piloto de E4 y E5; E6 y E11 desde el inicio | Uso en el mes 4 y evidencia en G1 |
| R2, meses 6 y 7 | E4 y E5 en las olas, E7 carga y contingencia, E11 preparación y adopción | Costo, personal y operación aceptados antes de VE-01 |
| Campaña, mes 8 | Estabilización y soporte, sin funcionalidades nuevas en producción | Excepciones críticas controladas |
| R3, meses 9 a 12 | E9, E8b, E10 en 3 a 5 tiendas, integraciones restantes y ruteo avanzado | Autorización en G2 |

## 5.4 Compromisos y adaptación

Proponemos comprometer el flujo de R1 y la preparación de campaña. Las 68 tiendas son una meta condicionada que G1 confirma con capacidad, centros y acompañamiento conciliados. El PO reordena el detalle dentro de los límites; el sponsor y el Comité deciden cambios de compromiso, fecha, cobertura o presupuesto.

Las primeras opciones de diferimiento son E10, el ruteo avanzado y los incrementos opcionales. E9 sostiene la meta de devolución: diferirla obliga a revisar el Charter y sus beneficios. Seguridad, observabilidad básica y continuidad se mantienen siempre.

# 6. Estimación e incertidumbre

## 6.1 Técnicas

| Componente | Técnica | Base y límite |
|:------------------------|:----------------------------|:------------------------------------|
| Integración, conciliación, controles y campaña | Analogía y estimación de tres puntos (PERT) | Rangos supuestos por el equipo |
| APIs y disponibilidad | PERT de alto nivel; throughput y tiempo de ciclo para recalibrar | Monte Carlo solo con histórico suficiente y estable |
| OMS, cambios WMS y cloud | Paramétrica, con cotización prevista como contraste | Montos actuales sin ofertas |
| Retiro, app, devoluciones y experimento | Comparación relativa por equipo, convertida a equipo-sprints | Seis personas por equipo como normalización |
| Proyecto | PERT agregado, presupuesto por categoría y reserva | Escenarios aritméticos sin probabilidad de fecha |

## 6.2 Esfuerzo por épica

| Épica | O | M | P | E | σ |
|:--------------------------------|------:|------:|------:|------:|------:|
| E1 Disponibilidad de stock | 10 | 14 | 22 | 14,7 | 2,0 |
| E2 Integración ERP, WMS y POS | 12 | 16 | 26 | 17,0 | 2,3 |
| E3 Gestión de pedidos | 10 | 14 | 24 | 15,0 | 2,3 |
| E4 Retiro en tienda | 6 | 9 | 14 | 9,3 | 1,3 |
| E5 App de preparación | 6 | 8 | 13 | 8,5 | 1,2 |
| E6 Seguridad | 4 | 6 | 9 | 6,2 | 0,8 |
| E7 Preparación de campaña | 3 | 5 | 8 | 5,2 | 0,8 |
| E8a Observabilidad básica | 2 | 3 | 4 | 3,0 | 0,3 |
| E8b Observabilidad centralizada | 2 | 4 | 6 | 4,0 | 0,7 |
| E9 Devoluciones | 6 | 9 | 15 | 9,5 | 1,5 |
| E10 Experimento de despacho | 3 | 5 | 9 | 5,3 | 1,0 |
| E11 Despliegue y cambio | 4 | 6 | 10 | 6,3 | 1,0 |
| **Total** | **68** | **99** | **160** | **104,0** | **4,9** |

Unidad: equipo-sprint de referencia. E = (O + 4M + P) / 6 y σ = (P − O) / 6. La σ total de 4,9 supone independencia entre épicas.

## 6.3 Sensibilidad

| Escenario | Equipo-sprints | Uso de 120 |
|:------------------------------------------|------:|------:|
| Esfuerzo esperado | 104,0 | 86,67% |
| Aproximación normal 80%, bajo independencia | 108,1 | 90,11% |
| Aproximación normal 95%, bajo independencia | 112,1 | 93,43% |
| 95% con correlación total entre épicas | 129,3 | 107,75% |
| Suma pesimista de épicas | 160,0 | 133,33% |

Estas cifras describen la sensibilidad del esfuerzo y no equivalen a una probabilidad de entregar antes de la campaña, porque no modelan la red de actividades ni los recursos. Ante el escenario pesimista, diferir E10 y E8b deja 145 equipo-sprints, todavía 25 sobre la capacidad. En ese caso el Comité revisa cobertura u horizonte con una reestimación.

## 6.4 Capacidad y dotación

| Periodo | Sprints efectivos | Capacidad | Carga | Uso |
|:----------------------|:----------------------|------:|------:|------:|
| F1 · R0 y R1 | 2 a 11 | 56 | 47,7 | 85,18% |
| F2 · R2 | 12 a 15 | 24 | 23,0 | 95,83% |
| F3 · campaña y R3 | 16 y 18 a 26 | 40 | 33,3 | 83,25% |
| **Total** | **24** | **120** | **104,0** | **86,67%** |

Proponemos cinco equipos en los sprints 1 a 4, seis en los sprints 5 a 15 y cuatro desde el sprint 16. El sexto equipo debe estar disponible en la semana 9, arranca en el sprint 5 y produce desde el 6. Se pagan 130 equipo-sprints, de los cuales 10 son de arranque y estabilización, y quedan 120 efectivos. Son 60 equipo-meses a 14 MM, es decir, 840 MM exactos.

El corte del piloto usa 36 de 38 equipo-sprints disponibles hasta la semana 16 (94,74%) y R2 usa 23 de 24 (95,83%). Ambas ventanas tienen poco margen y dependen de especialidades disponibles.

El soporte durante el proyecto se financia con las categorías existentes. La guardia de plataforma y el soporte de aplicación los prestan los equipos de la capacidad contratada, incluido el sprint 17 de estabilización en campaña; el soporte del partner forma parte del contrato OMS; las herramientas, de cloud y observabilidad; la formación de referentes, de adopción y despliegue local. La mesa corporativa absorbe el primer nivel con guiones de ZEUS. Si la regla medida en el piloto exige agentes adicionales, ese refuerzo queda fuera de la base y G1 lo autoriza con cargo a la reserva o ajustando la cobertura. El equipo estable posterior al mes 12 es un costo recurrente del negocio y entra en el horizonte económico.

## 6.5 Presupuesto por categoría

| Categoría, MM CLP | Base | O | P |
|:----------------------------------|------:|------:|------:|
| Capacidad de equipos | 840 | 840 | 1.008 |
| Gestión de pedidos (OMS) y partner | 180 | 140 | 240 |
| Cambios WMS | 70 | 50 | 100 |
| Cloud y observabilidad | 70 | 50 | 100 |
| Seguridad externa y herramientas | 35 | 25 | 50 |
| Adopción, capacitación y despliegue local | 45 | 30 | 70 |
| Gobierno PM y PMO | 90 | 80 | 100 |
| **Total** | **1.330** | **1.215** | **1.668** |

La reserva de 170 MM representa 12,78% de la base y se consume una sola vez. El extremo P de equipos aplica un estrés de 20% sobre su costo. Dentro de la adopción y despliegue local se asignan 2,2 MM a veinte persona-días de campo y 10 MM a traslados de las células.

## 6.6 Financiación y gasto evitable

| Tramo | Autorización | Cubre | MM CLP |
|:------|:--------------|:------------------------------------|------:|
| T1 | G0, mes 1 | R0 y R1, meses 1 a 5, incluida la mayor parte del OMS | 675 |
| T2 | G1, mes 5 | R2 y campaña, meses 6 a 8 | 345 |
| T3 | G2, mes 9 | R3, meses 9 a 12 | 310 |
| Reserva | Comité | Riesgos registrados | 170 |

Para que los gates tengan opciones reales, proponemos contratar la capacidad externa por fase, con reducción o renovación en G1 y G2, y separar compromisos mínimos de servicios cancelables. En G1 quedan 655 MM de base por liberar y en G2, 310 MM. El gasto evitable en cada gate es ese saldo menos obligaciones irrevocables, penalidades y costos de cierre.

## 6.7 Respuesta al estrés de costo

| Paso | Reducción, MM | Total, MM | Exceso sobre 1.500 |
|:----------------------------------------------|------:|------:|------:|
| Estrés combinado bruto | 0 | 1.668,0 | 168,0 |
| Diferir E10 y E8b, que habilita reducir capacidad | 0 | 1.668,0 | 168,0 |
| Un equipo menos tras G2, durante 8,5 sprints | 65,9 | 1.602,1 | 102,1 |
| Tope de OMS en 180 | 60,0 | 1.542,1 | 42,1 |
| Tope de WMS en 70 | 30,0 | 1.512,1 | 12,1 |
| Tope de cloud y observabilidad en 85 | 15,0 | 1.497,1 | 0,0 |

Con las tres palancas, el escenario queda 2,9 MM bajo el techo. Los topes son condiciones de contratación por negociar. Si no se consiguen, el Comité ajusta cobertura o arquitectura antes de superar 1.500 MM.

## 6.8 Actualización de la estimación

La estimación se recalibra con evidencia de cada equipo y flujo en VT-01 y en cada gate, excluyendo los sprints de arranque y estabilización. Si la entrega comparable cae bajo 80% del forecast interno, se investigan dependencia y capacidad y se eleva el impacto. Las reservas requieren aprobación del Comité y no financian alcance nuevo.

# 7. Roadmap y planificación

## 7.1 Releases y momentos de valor

| Release | Ventana | Cobertura | Evidencia |
|:--------|:----------------------|:----------------------|:------------------------------|
| R0 | Meses 1 y 2 | Datos y sitios representativos | Arquitectura, OMS por hitos y prueba ERP y WMS; VT-01 |
| R1 | Construcción en meses 2 a 4; salida en la semana 16; observación en semanas 17 a 20 | 10 tiendas, 1 CD, 2 familias | Uso y mejora frente a base comparable; G1 |
| R2 | Meses 6 y 7, tras G1 | Meta de 68 tiendas, hasta 3 CD | Cada ola con datos, dotación, controles y soporte; VE-01 |
| Campaña | Mes 8 | Solo sitios operables | Carga representativa, monitoreo, respuesta y reversión |
| R3 | Meses 9 a 12, tras G2 | Devolución elegible; experimento en 3 a 5 tiendas | KPI-04 y límites del experimento |

## 7.2 Calendario de referencia

Usamos 52 semanas y 26 sprints de referencia. Los meses 1 a 5 cubren las semanas 1 a 22; los meses 6 y 7, las semanas 23 a 30; el mes 8, las semanas 31 a 35; y los meses 9 a 12, las semanas 36 a 52. G0 ocurre en el mes 1, VT-01 al final de la semana 8, G1 al final de la semana 22, VE-01 al final de la semana 30 y G2 al inicio de la semana 36. Estas fechas son relativas al inicio del proyecto y se convierten a calendario real antes de ejecutar.

## 7.3 Olas de expansión

| Ola | Ventana | Tiendas adicionales | Total | Condición previa |
|:-------|:----------------------|------:|------:|:------------------------------|
| Piloto | Meses 4 y 5 | 10 | 10 | VT-01, operación, medición y soporte aceptados |
| O1 | Días hábiles 1 a 8 | 15 | 25 | G1, células, horas y stock disponibles; CD aceptado |
| O2 | Días 9 a 16 | 15 | 40 | Estabilidad de O1, capacidad y costo actualizado |
| O3 | Días 17 a 23 | 14 | 54 | Estabilidad de O2 y pruebas de carga |
| O4 | Días 24 a 30 | 14 | 68 | Estabilidad de O3 y tiempo para VE-01 |

Proponemos cuatro células de dos funciones, con 75% de disponibilidad efectiva. La habilitación demanda 116 persona-días y el acompañamiento 29, en total 145 frente a 150 disponibles en 25 jornadas. Con diez días de corrección y VE-01, la expansión usa 35 de los 40 días hábiles. Si cada tienda tomara 1,5 días de célula, se requerirían 44 días; con dos días, 54. En ese caso G1 decide refuerzo, secuencia o cobertura antes de comprometer la campaña. La operación diaria de cada tienda por turno requiere su propia capacidad aceptada.

## 7.4 Gates y revisiones de salida

| ID | Momento | Evidencia y decisión | Autoridad |
|:------|:--------------|:----------------------------------------|:----------------------|
| G0 | Mes 1 | Arquitectura inicial, OMS por hitos y primer tramo | Comité y sponsor con Finanzas y Arquitectura |
| VT-01 | Fin del mes 2 | Interfaces, datos, OMS, capacidad y controles probados | Tecnología, Arquitectura, CISO y Operaciones |
| G1 | Fin del mes 5 | Primera entrega de valor y decisión de expandir | Comité, sponsor y dueños de beneficio |
| VE-01 | Fin del mes 7 | Cobertura segura, carga, recuperación y soporte; inicia congelamiento | Operaciones, Tecnología, CISO y sponsor |
| G2 | Inicio del mes 9 | Beneficios, campaña, forecast y financiación de R3 | Comité, sponsor, Finanzas y dueños de beneficio |
| Cierre | Mes 12 | Aceptación, transferencia, costo y beneficios pendientes | Sponsor, Operaciones y dueños de beneficio |

## 7.5 Black Friday y congelamiento

El congelamiento comienza al aceptar R2 y superar VE-01, al final del mes 7, y dura hasta que termina Black Friday, aproximadamente en el mes 8. En esa ventana no se despliegan funcionalidades nuevas en producción; las correcciones críticas de seguridad o continuidad requieren autorización de Operaciones, Tecnología y CISO. Continúan el monitoreo, el soporte y la estabilización con la dotación prevista.

## 7.6 Operación y soporte por etapa

| Etapa | Soporte | Evidencia antes de avanzar | Responsable |
|:--------------|:------------------------------|:------------------------------|:----------------|
| R0, meses 1 y 2 | Dueño del servicio, niveles, guiones, procedimientos y acuerdos de nivel de servicio | Modelo aprobado y herramientas de alertas e incidentes listas en VT-01 | Tecnología con Operaciones |
| R1, piloto | Mesa con guiones de ZEUS, referente por turno en las 10 tiendas, soporte de aplicación y guardia | Mesa lista antes de la semana 16; incidentes medidos en las semanas 17 a 20 | Dueño del servicio |
| R2, olas | Referentes formados por ola y mesa ajustada según la regla de dimensionamiento | Soporte aceptado en cada sitio antes de contarlo como alta | Dueño del servicio con Operaciones |
| Campaña, mes 8 | Guardia reforzada y sala de seguimiento desde VE-01 hasta el fin de Black Friday | Prueba de respuesta y recuperación en VE-01 | Tecnología, Operaciones y CISO |
| R3 y cierre | Mejoras desde problemas recurrentes y traspaso a un equipo estable | Acuerdos de nivel de servicio, responsables y presupuesto recurrente en el mes 12 | Sponsor y dueño del servicio |

## 7.7 Dependencias

| Dependencia | Coordinación | Evidencia requerida | Momento |
|:------------------------|:----------------------|:------------------------------|:------------------------|
| ERP, WMS y condiciones del OMS | PM y Tecnología con proveedores | Contratos de datos, acceso, prueba representativa y soporte | VT-01; afecta la primera entrega |
| Stock, turnos, espacio y formación | Operaciones, Logística y gerencias de tienda | Preparación y aceptación de cada sitio | Antes del piloto y de cada ola |
| CISO, Arquitectura y ambientes de prueba | Tecnología y CISO | Controles, integración, carga y recuperación | Cada release y VE-01 |
| Reglas de devolución y conciliación | Comercial, Finanzas y Operaciones | Elegibilidad, estados y aceptación | Antes de R3 |
| Operación y soporte del servicio | Dueño del servicio con Operaciones | Niveles, guiones, guardia y mesa preparados | Antes del piloto; crece por ola y se refuerza en campaña |
| Dotación, contratos y costo por tramo | PM, Finanzas y proveedores | Dotación por periodo, compromisos y forecast | G0, G1 y G2 |

La cadena que condiciona el mes 5 es contrato OMS (semana 4), VT-01 (semana 8), salida del piloto (semana 16), observación (semanas 17 a 20) y G1 (semana 22). Si se atrasa un eslabón, se recalcula la ventana de evidencia antes de mantener el compromiso del mes 5. Como contingencia, se evalúa publicar stock conciliado de las mismas familias en el canal existente y medir cancelaciones comparables; sustituir el piloto requiere decisión del Comité.

## 7.8 Señales de flujo

| Señal | Definición | Decisión que apoya |
|:----------------|:------------------------------------|:------------------------------------|
| Throughput | Ítems aceptados por semana y tipo; tiendas aceptadas por semana | Contrastar el ritmo con las altas pendientes y revisar olas |
| Tiempo de ciclo | Tiempo desde inicio hasta aceptación, por tipo de ítem | Revisar dispersión y esperas; recalibrar rangos con histórico |
| Trabajo en curso y bloqueos | Ítems iniciados sin terminar, antigüedad, causa y responsable | Resolver la restricción dominante y limitar nuevos inicios |

# Anexos

## A. Supuestos principales

| ID | Supuesto | Validación prevista | Si falla |
|:-------|:----------------------------------|:----------------------------|:----------------------------|
| SUP-01 | ERP y WMS permiten integración acotada por APIs y, donde sea viable, eventos | Pruebas de consistencia, carga y recuperación en VT-01 | Revisar arquitectura, plazo y alcance |
| SUP-02 | La dotación escalonada de equipos sostiene la secuencia | Sponsor y Operaciones confirman antes de R1 | Limitar trabajo en curso, cobertura o secuencia |
| SUP-03 | Hay datos comparables y volumen para evaluar el piloto | Dueños de beneficio fijan base y suficiencia antes del piloto | Informar resultado inconcluso |
| SUP-05 | 10 tiendas piloto y 68 en el mes 7 son operables | Operaciones autoriza cada ola y sus centros | Mantener solo la cobertura segura |
| SUP-07 | 1.330 MM más 170 de reserva cubren el alcance | Finanzas contrasta costos y contratos por etapa | Revisar cobertura o experimento |
| SUP-12 | Un OMS de mercado cubre el flujo con configuración acotada | Selección en G0 y prueba en VT-01 | Revisar contrato y arquitectura |
| SUP-14 | Piloto con 1 CD y 2 familias; expansión con hasta 3 CD | Logística valida sitios y catálogo en VT-01 | Ajustar selección y cobertura |
| SUP-16 | Umbrales de G1: −20% cancelación, −25% preparación, adopción > 80% | Dueños de beneficio ratifican bases antes de abrir | Informar inconcluso o sin mejora |
| SUP-17 | Experimento en 3 a 5 tiendas, máximo 4 semanas o 300 pedidos | G2 autoriza límites y techo monetario | Diferir el experimento |
| SUP-21 | Cuatro células con 145 de 150 persona-días efectivos | Calibración con el piloto | Ajustar olas o cobertura en G1 |
| SUP-22 | El flujo mínimo requiere 36 de 38 equipo-sprints hasta la semana 16 | Tecnología y Operaciones revisan el corte | Recalcular la primera salida |
| SUP-23 | R1 con reserva simple y ventana fija de retiro | Logística y Tecnología prueban en VT-01 | Revisar diseño y estimación |
| SUP-25 | Una promesa confiable contribuye a conversión y contribución neta | Comercial y Finanzas miden por cohorte | Mantener la hipótesis condicionada |
| SUP-26 | La mesa corporativa absorbe el primer nivel de soporte con guiones de ZEUS | Incidentes por tienda medidos en el piloto y regla aplicada antes de cada ola | Refuerzo autorizado en G1 o ajuste de olas |

## B. Registro de riesgos

| ID | Causa, evento y efecto | Respuesta | Dueño | Disparador |
|:------|:------------------------------|:------------------------------|:--------------|:------------------------------|
| R-01 | Interfaces legacy desconocidas; integración tardía; costo, plazo y valor afectados | Pruebas representativas, contrato de datos e hitos OMS | Tecnología y Arquitectura | VT-01 no demuestra el flujo |
| R-02 | Stock físico inexacto; reservas sin existencias; cancelaciones | Conteos, conciliación, cohortes y colchón reservable | Logística y Tiendas | La cohorte no sostiene la promesa |
| R-03 | Proveedor WMS dependiente; entrega tardía; flujo incompleto en el mes 5 | Compromisos, ventanas de integración y escalamiento contractual | Tecnología y proveedor | Hito del proveedor incumplido |
| R-04 | Dotación limitada en tienda; baja adopción; preparación sin mejora | Medir carga, formar por turno y separar habilitación de operación | Operaciones y PM | Uso de la app insuficiente |
| R-05 | 58 altas en dos meses; estabilización insuficiente antes de campaña | Cuatro células calibradas con el piloto y aceptación por sitio | Operaciones y PM | Más de un día de célula por tienda |
| R-06 | Muestra insuficiente o salida tardía; sin evidencia en el mes 5 | Base e instrumentación desde R0 y umbrales ratificados | Dueños de beneficio | G1 solo acredita instalación |
| R-08 | Controles insuficientes; exposición de datos o accesos | Controles desde el diseño y aceptación del CISO | CISO | Riesgo crítico abierto |
| R-09 | Carga de campaña superior a la capacidad; degradación | Pruebas de carga y recuperación, cobertura segura | Tecnología y Operaciones | VE-01 no aceptado |
| R-10 | Costos subestimados; costo a término sobre el techo | Reestimación, compras por hitos y topes | Finanzas y PM | Estimación sobre el límite |
| R-15 | Promesa más agresiva que el stock y la capacidad; incumplimiento | Ventana fija, stock conciliado y medición de promesa cumplida | Comercial y Logística | Punto o ventana no sostenible |
| R-16 | Contrato OMS tarda más de cuatro semanas; valor del mes 5 en riesgo | Requisitos en R0, contrato por hitos y seguimiento semanal | PM y Tecnología con Compras | Sin contrato al cierre de la semana 4 |
| R-17 | Soporte dimensionado para el piloto y no para 68 tiendas o campaña; incidentes sin atención | Tres niveles con dueño, regla calibrada, referentes por ola y guardia reforzada | Dueño del servicio con Operaciones | Tiempos de atención sobre lo acordado |

## C. Interesados del caso

| Interesado | Interés | Tensión | Respuesta de ZEUS |
|:----------------------|:----------------------|:----------------------|:------------------------------------|
| Gerente General, sponsor | Resultados visibles y velocidad | Presión por acelerar decisiones | Primera salida y medición antes de G1; financiación por tramos |
| Gerente Comercial | Conversión, ventas y experiencia | Prioriza funcionalidades sobre deuda técnica | Retiro y app por valor; habilitadores protegidos; opcionales compiten por capacidad |
| Gerente de Operaciones | Eficiencia y promesas de servicio | Busca estabilidad y procesos predecibles | Aceptación por sitio, soporte, reversión y congelamiento |
| Gerente de Logística | Inventario, picking y despacho | Dependencia de WMS y operación física | Conciliación, prueba WMS y selección de CD y catálogo |
| Gerente de Tecnología | Arquitectura sostenible e integración | Modernización frente a continuidad | ERP conservado, APIs reutilizables y cloud selectivo |
| CISO | Seguridad y resiliencia | Puede detener liberaciones | Controles en la definición de terminado y bloqueo de salida |
| Gerente de Finanzas | Retorno y control de inversión | Exige evidencia económica y forecast | Tramos, reserva, volumen requerido y gasto evitable por gate |
| Gerentes de Tienda | Operación local y dotación | Temen nuevas funciones sin capacidad | Formación por turno, acompañamiento, aceptación del sitio y soporte continuo con referente y mesa |
| PO E-commerce | Valor y priorización | Autonomía para adaptar el backlog | Decide orden y detalle dentro de los límites |
| Arquitectura Empresarial | Estándares y desacoplamiento | Puede introducir gates y controles | Evidencia común en VT-01 y definición de terminado |
| Equipos de desarrollo | Flujo y autonomía | Reducir dependencias y burocracia | Límites de trabajo en curso y controles proporcionales |
| Proveedor WMS | Cumplimiento contractual | Planificación tradicional | Hitos, contratos de datos y ventanas de prueba |
| Proveedor Cloud | Escalabilidad y servicios administrados | Promueve cambios de arquitectura | Cloud selectivo justificado por necesidad y costo total |

Fuente: enunciado, pp. 6 y 7, para intereses y tensiones; respuestas propuestas por el equipo.

## D. Respuestas ante cambios de condición

| Si cambia | Respuesta propuesta | Decide |
|:----------------------|:----------------------------------------|:----------------------------|
| Black Friday en el mes 7 | Recalcular hacia atrás la salida y el congelamiento; reducir la expansión antes que la preparación de campaña | Sponsor y Operaciones fijan la cobertura |
| Techo de 1.200 MM | La base de 1.330 excede en 130; reestimar B con menor cobertura y diferir opcionales, sin tocar el núcleo | Comité, con cálculo monetario |
| ERP sin API viable | Probar la interfaz soportada, su consistencia y latencia, y cuantificar el cambio | Si rompe costo, valor o continuidad, se revisa la arquitectura antes del piloto |
| Sin sexto equipo | La capacidad hasta la salida baja de 38 a 35 y el corte de 36 deja de caber | El PM eleva al Comité |
| G1 inconcluso | Mantener la cobertura segura, revisar medición y causas, y acotar compromisos | Comité y Finanzas |
| El CISO bloquea | Detener la exposición afectada y corregir | El CISO conserva su autoridad; el sponsor revisa fecha o cobertura |

## E. Fuentes

- Enunciado oficial del caso ZEUS, primera etapa, MII904 Gestión de Proyectos Informáticos, PUCV, 2026, pp. 2 a 9.
- Presentaciones docentes de las sesiones 03 a 06 y clases 1 a 4 del curso.
- Cui, R., Li, M. y Li, Q. (2020). Value of High-Quality Logistics: Evidence from a Clash Between SF Express and Alibaba. *Management Science*, 66(9), 3879-3902. https://doi.org/10.1287/mnsc.2019.3411
- Deshpande, V. y Pendem, P. K. (2023). Logistics Performance, Ratings, and Its Impact on Customer Purchasing Behavior and Sales in E-Commerce Platforms. *Manufacturing & Service Operations Management*, 25(3), 827-845. https://doi.org/10.1287/msom.2021.1045
- Cui, R., Lu, Z., Sun, T. y Golden, J. M. (2024). Sooner or Later? Promising Delivery Speed in Online Retail. *Manufacturing & Service Operations Management*, 26(1), 233-251. https://doi.org/10.1287/msom.2021.0174

Los tres artículos se consultaron a nivel de resumen y metadatos del editor. Respaldan el mecanismo logístico y sus límites; no aportan cifras transferibles a ZEUS.
