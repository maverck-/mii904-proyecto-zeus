# Actualización del equipo recibida el 23 de octubre de 2026

Fuente recibida conservada sin correcciones de contenido. No acredita cotizaciones, históricos ni aprobación empresarial. Véase la [comparación](../registros/revision_avance_2026-10-23.md) y las versiones integradas en `trabajo/`.

## Texto recibido

Rogelio - Priorización y Estimación
Maverick - Diseño del alcance y roadmap


1. Diagnóstico estratégico y Business Case

1.1 Problemas

Entre los principales problemas que tiene actualmente el negocio con su sistema digital se tiene que:
El sistema actual tiene una alta latencia entre la actualización del inventario y la actualización del stock en la página web, llevando a un 7,8% de cancelaciones forzadas post-compra debido a quiebres de stock no detectados al momento del pago. 
Existen bases duplicadas y desalineadas de clientes y productos, y las tiendas físicas carecen de visibilidad para las compras digitales. Lo que limita la capacidad de resolver disputas y devoluciones, siendo solo el 64% resueltas en el primer contacto. Empeorando la calidad de atención al cliente.
Se tienen limitaciones sobre partes del sistema antiguo que no se pueden cambiar, como el ERP y el WMS. Las cuales a pesar de abaratar los costos de desarrollo hacen que el desarrollo tenga que trabajar alrededor de los mismos.

1.2 drivers estratégicos

Este proyecto busca crear un sistema que logre crear una experiencia omnicanal que sea resiliente y eficiente, que sea sostenible y escalable para el crecimiento futuro.

Las métricas claves para medir el éxito son:

Indicador
Situación actual
Meta estratégica
Ventas digitales
24%
35%
Pedidos entregados a tiempo
82%
95%
Cancelaciones por falta de stock
7,8%
2%
Exactitud de inventario
91%
98%
Actualización de stock web
45–120 min
<2 min 


Siendo los principales Hitos

Hito
Descripción
Horizonte
12 meses
Primera entrega de
valor
Debe existir dentro de los primeros 5 meses.
Hito comercial
Black Friday ocurrirá en aproximadamente 8 meses y es crítico para el
negocio.


1.3 Alternativas

Para el desarrollo se va a centrar en crear una plataforma omnicanal modular. Para ello mantendremos los sistemas ERP y WMS actuales, y construiremos alrededor de estos las funcionalidades de click and collect y gestión de pedidos, a su vez remodelando la capa de apis.

1.4 Supuestos

Por último entre las asunciones 

2. Selección y tailoring del enfoque

2.1 Enfoque propuesto

Nosotros recomendamos un enfoque híbrido, ya que el proyecto posee una combinación de fuentes de alta y baja incertidumbre. Este enfoque combina una capa de gobierno de naturaleza predictiva con una capa de entrega adaptativa, cada una se asigna según el nivel de incertidumbre y de restricción de cada componente del proyecto.

2.2 Fundamentación

ZEUS contiene dos condiciones que ningún enfoque puro resuelve por sí solo:
Alta restricción y baja incertidumbre en integración con el ERP, datos contables, seguridad, contratos con proveedores y preparación de Black Friday. Estos elementos requieren planificación anticipada, trazabilidad y control formal de cambios.
Alta incertidumbre en la experiencia de Click & Collect, devoluciones omnicanal y el rol de las tiendas como puntos logísticos. Estos elementos requieren validación temprana con usuarios reales y ajuste iterativo.

2.3 Asignación por componente

Componente
Lógica de gestión
Justificación
Integración con ERP, datos contables y conciliaciones
Predictiva 
Solución conocida, alta exigencia de trazabilidad y alto costo de error 
Contratos con proveedores WMS y OMS 
Predictiva 
Contrapartes con planificación tradicional y obligaciones formales 
Seguridad y control de accesos 
Predictiva 
Requisito obligatorio, incorporado en la Definition of Done 
Preparación de Black Friday 
Predictiva, gestionada por ruta crítica 
Fecha comprometida e inamovible 
Capa de APIs y servicio de disponibilidad 
Kanban con límites de WIP 
Flujo continuo con múltiples dependencias entre equipos 
Click & Collect, app de tienda y devoluciones 
Ágil (Scrum, sprints de dos semanas) 
Alta incertidumbre; requiere validación con tiendas piloto 
Ship-from-store 
Experimento acotado 
Componente de mayor incertidumbre del caso 


2.4 Elementos estables y elementos adaptables

Elementos estables: propósito, envolvente presupuestaria, fechas de los gates, fecha de Black Friday, principios de arquitectura (API-first y orientación a eventos) y controles de seguridad.
Elementos adaptables: detalle funcional de cada release, orden del backlog, selección y número de tiendas piloto, y diseño de la experiencia de usuario.
2.5 Controles formales
Gates ejecutivos en los meses 1, 5 y 9. En cada uno, el Comité evalúa evidencia y decide si libera el siguiente tramo de financiamiento.
Control de cambios sobre presupuesto, fechas comprometidas y alcance mayor.
Revisión de arquitectura y seguridad previa a cada release.
2.6 Instancias de retroalimentación
La retroalimentación del proyecto se organiza en tres instancias. Cada dos semanas se realizan revisiones de sprint con los gerentes de las tiendas piloto y el Product Owner de e-commerce, para validar los incrementos con usuarios reales y ajustar el backlog según la evidencia obtenida. Además, se hace un seguimiento semanal de las métricas de flujo que permite detectar cuellos de botella o identificar problemas. Por último, un foro de integración semanal reúne al PM, los Product Owners y Arquitectura Empresarial para coordinar a los equipos.

3. Project Charter

Nombre del proyecto
ZEUS: Plataforma Omnicanal Modular
Propósito
Construir una plataforma que integre inventario, pedidos, tiendas y devoluciones mediante servicios reutilizables, para ofrecer una experiencia omnicanal consistente y reducir la complejidad de integración
Objetivos medibles
Reducir las cancelaciones por falta de stock de 7,8% a menos de 2%. 
Reducir la actualización del stock web de 45–120 minutos a menos de 2 minutos. 
Reducir la preparación promedio de pedidos de 7,2 horas a menos de 3 horas. 
Elevar las devoluciones resueltas al primer contacto de 64% a al menos 85%. 
Mantener la disponibilidad del e-commerce en al menos 99,9% durante Black Friday
Contribución estratégica
Contribuye a alcanzar las metas de 35% de ventas digitales, NPS >= 48,95% de pedidos entregados a tiempo y abandono de carro bajo 55%.
Alcance incluido
Inventario omnicanal 
Click and collect
Sistema de gestión de pedidos 
Capa de APIs 
Servicio de disponibilidad de stock 
Observabilidad centralizada 
Piloto de ship-from-store
Alcance excluido
Reemplazo del ERP o WMS, iniciativas de inteligencia artificial y recomendaciones, plataforma de datos completa, migración amplia a cloud y nueva plataforma de identidad de clientes
Entregables principales
R1 (mes 5): piloto de Click & Collect en 10 tiendas. 
R2 (mes 7): Click & Collect en las 68 tiendas, preparado para Black Friday. 
R3 (mes 12): devoluciones omnicanal, observabilidad centralizada y piloto de Ship-from-store
Sponsor
Gerente General
Roles clave
PM del programa 
Product Owners de e-commerce y tiendas
Gerente de Tecnología y Arquitectura Empresarial 
CISO 
Gerentes de Logística y Operaciones como responsables de la realización de beneficios
Stakeholders
Gerencia Comercial 
Gerencia de Finanzas 
Gerentes de Tienda 
Equipos de desarrollo 
Proveedores WMS 
OMS y cloud
Restricciones
Presupuesto máximo de $1.500 MM 
Horizonte de 12 meses 
Primera entrega de valor antes del mes 5 
Black Friday en el mes 8 
El ERP no se reemplaza 
El WMS sólo puede modificarse 
Continuidad operativa del e-commerce y las tiendas
Cumplimiento obligatorio de controles de seguridad
Supuestos
El ERP puede exponer información de stock mediante eventos o API, el proveedor WMS cumple los plazos acordados, se adquiere un OMS de mercado, existen cinco equipos disponibles y diez tiendas participan del piloto.
Riesgos iniciales
Exactitud de inventario de 91%, que puede comprometer la confiabilidad del stock mostrado 
Atraso del proveedor WMS 
Capacidad insuficiente de las tiendas 
Carga extraordinaria durante Black Friday 
Sobrecosto con margen presupuestario acotado 
Bloqueo de releases por riesgos de seguridad 
Presupuesto preliminar
1500 Millones de CLP, liberado por tramos sujeto a la aprobación de cada fase.
Hitos iniciales
Gate 0 (mes 1): aprobación de arquitectura y contrato OMS. Gate 1 (mes 5): primera entrega de valor. 
Congelamiento de cambios (mes 7). 
Black Friday (mes 8). 
Gate 2 (mes 9): evaluación de beneficios y liberación de fondos para R3. 
Cierre (mes 12)
Criterios de éxito
Cumplimiento de los objetivos medibles
Ausencia de incidentes críticos de seguridad 
Operación de Black Friday sin interrupciones 
Más del 80% de los pedidos de Click & Collect preparados mediante la aplicación 
Ejecución dentro del presupuesto máximo
Derechos de decisión
Comité Ejecutivo: aprobación de gates y liberación de financiamiento. 
Sponsor: cambios de fecha o de alcance mayor. 
Product Owners: priorización del backlog dentro de cada release. 
Arquitectura Empresarial: estándares de integración. 
CISO: facultad de detener releases ante riesgos críticos
Aprobación
Se solicita al Comité Ejecutivo autorizar el proyecto bajo las condiciones descritas y liberar el primer tramo de financiamiento para R0 y R1




5. Priorización
5.1 Método y criterios
La priorización sigue tres pasos: WSJF ordena las épicas, las dependencias definen la secuencia y la capacidad de cada release limita cuánto entra. Los puntajes son estimaciones relativas: se acuerdan en una sesión con los Product Owners, Operaciones y Tecnología, y su función es estructurar esa conversación, no reemplazarla.
Paso 1, WSJF (Weighted Shortest Job First): WSJF = Costo del retraso / Tamaño. El costo del retraso suma tres criterios en escala Fibonacci modificada (1, 2, 3, 5, 8, 13, 20): valor de negocio, criticidad temporal y reducción de riesgo o habilitación. Así el costo del retraso recoge sus tres formas: valor perdido, riesgo o fecha límite (Black Friday) y opción de aprendizaje (por ejemplo, el piloto de Ship-from-store).
Paso 2, ajuste por dependencias: una épica habilitadora se adelanta aunque su WSJF sea menor si otra épica de mayor valor depende de ella.
Paso 3, restricciones obligatorias: seguridad (E6), preparación de Black Friday (E7) y gestión del cambio (E11) no compiten en el ranking. Son condiciones no negociables y se incorporan a la Definition of Done o al plan de cada release.
Relación con los criterios de la pauta:
Criterio de la pauta
Cómo se aplica
Valor
Valor de negocio: impacto en los KPIs del Charter
Urgencia
Criticidad temporal: cuánto pierde el negocio si se atrasa, en especial respecto de Black Friday
Dependencia y riesgo
Reducción de riesgo o habilitación: cuánto habilita otras épicas o reduce riesgo técnico
Costo
Tamaño: esfuerzo esperado PERT de la sección 6, llevado a la misma escala
Incertidumbre
Las épicas de alta incertidumbre entran como experimento acotado, no como compromiso
Capacidad
La carga se planifica hasta cerca del 90% de la capacidad: antes del congelamiento, R1 y R2 suman 88%




5.2 Puntuación de épicas
Épica
Valor
Urgencia
Riesgo / habilitación
Costo del retraso
Tamaño
WSJF
KPI que mueve
E8a Observabilidad básica (stock y pedidos)
3
13
13
29
3
9,7
Disponibilidad ≥ 99,9% en Black Friday
E4 Click & Collect (flujo cliente)
20
13
5
38
8
4,8
Ventas digitales, abandono de carro
E1 Servicio de disponibilidad de stock
20
20
20
60
13
4,6
Stock web < 2 min, cancelaciones < 2%
E5 App de preparación en tienda
13
13
8
34
8
4,3
Preparación < 3 h
E3 OMS (gestión de pedidos)
13
13
13
39
13
3,0
Preparación < 3 h, entregas a tiempo
E8b Observabilidad centralizada
3
2
8
13
5
2,6
Disponibilidad, tiempo de diagnóstico
E2 Capa de APIs / integración ERP-WMS-POS
8
20
20
48
20
2,4
Stock web, menos integraciones punto a punto
E9 Devoluciones omnicanal
13
3
3
19
8
2,4
Devoluciones en primer contacto ≥ 85%
E10 Piloto Ship-from-store
5
1
5
11
5
2,2
Aprendizaje (costo y tiempo por pedido)


Lectura del ranking:
E8a ocupa el primer lugar porque es pequeña y protege la operación de Black Friday. Se construye junto con el servicio de stock en R1, porque ningún servicio crítico debe salir a producción sin monitoreo.
E2 (APIs) y E3 (OMS) quedan abajo por su tamaño, pero E1 y Click & Collect dependen de ellas, por lo que el paso 2 las adelanta a R0 y R1. Por eso el contrato del OMS se cierra en el Gate 0 (mes 1).
Click & Collect tiene el mayor valor, pero no puede ir primero porque depende de E1, E2 y E3.
5.3 Secuencia resultante por release
Release
Contenido
Justificación
R0 (mes 0-1, Gate 0)
Arquitectura de referencia, contrato OMS, acuerdo de cambios con el proveedor WMS, entornos y controles de seguridad base
Prerrequisito de todo lo demás; componentes con lógica predictiva
R1 (mes 5, Gate 1)
E1 stock casi en tiempo real, E2 flujos de stock y pedidos, E3 OMS básico, E8a observabilidad básica, E4 y E5 piloto en 10 tiendas
Primera entrega de valor; habilitadores adelantados por dependencia
R2 (mes 7)
E4 y E5 en las 68 tiendas, E7 pruebas de carga y contingencia, E11 capacitación
Llegar estables a Black Friday; congelamiento de cambios desde el mes 7
Black Friday (mes 8)
Estabilización, sin cambios funcionales
Disponibilidad ≥ 99,9%
R3 (mes 9-12, sujeto a Gate 2)
E9 devoluciones, E8b observabilidad centralizada, E10 piloto Ship-from-store (3 a 5 tiendas), resto de integraciones de E2 y ruteo avanzado del OMS
Menor urgencia y mayor incertidumbre; es la variable de ajuste del proyecto
Fuera de ZEUS
IA y recomendaciones, data platform completa, identidad de clientes, migración amplia a cloud, reemplazo de ERP/WMS
No mueven KPIs críticos del proyecto o dependen de datos que aún no son confiables


5.4 Compromisos y elementos adaptables
Comprometido: contenido mínimo de R1 y R2 (stock, OMS y Click & Collect en las 68 tiendas), fecha de congelamiento de cambios y Black Friday.
Adaptable: orden del backlog dentro de cada release (lo deciden los Product Owners), número de tiendas piloto y todo el contenido de R3. Si la evidencia del Gate 2 o la capacidad real no alcanzan, se recorta R3 antes de modificar la fecha o el presupuesto.
5.5 Decisiones de priorización
Ship-from-store en el primer release: no. Tiene uno de los WSJF más bajos, la mayor incertidumbre del caso y depende del OMS y de la capacidad de las tiendas. Entra como experimento acotado en R3.
IA: etapa posterior. No mueve ningún KPI del proyecto y requiere datos consistentes que hoy no existen.
Data Platform: habilitador mínimo (eventos de stock y pedidos y un tablero de KPIs para los gates, incluidos en E2 y E8). No es un alcance independiente.
6. Estimación
6.1 Enfoque de estimación
La técnica de estimación se elige según la lógica de gestión de cada componente, en coherencia con la sección 2.
Componente
Lógica
Técnica
Por qué
Integración con ERP, conciliaciones, seguridad, Black Friday
Predictiva
Estimación por analogía y de tres puntos (PERT)
Requisitos conocidos y alto costo de error
Capa de APIs y servicio de disponibilidad
Kanban
Ítems de tamaño similar y pronóstico por throughput (ítems por semana); PERT por épica como línea base y Monte Carlo cuando haya historial
Flujo continuo con dependencias entre equipos, según la sección 2.3
OMS de mercado, cambios WMS, cloud
Predictiva
Cotización de proveedores y estimación paramétrica
Precio contractual
Click & Collect, app de tienda, devoluciones, Ship-from-store
Ágil
Talla de camiseta por épica convertida a equipo-sprints; story points y velocidad real desde el sprint 3
Alta incertidumbre; se recalibra con datos
Proyecto total
Híbrida
PERT agregado más reserva de contingencia
Expresar rangos en lugar de un número único


6.2 Supuestos de estimación
5 equipos promedio de cerca de 6 personas (mixtos, internos y externos), según el Charter. La dotación se escalona según la carga: 5 equipos al inicio, un sexto equipo de apoyo entre los meses 3 y 7 y 4 equipos después de Black Friday.
Sprints de 2 semanas: 26 en el año. Como capacidad de entrega se descuentan el sprint 1 (puesta en marcha, R0) y el sprint 17 (estabilización de Black Friday), lo que deja 24 sprints efectivos.
Capacidad total: 120 equipo-sprints efectivos, equivalente a 5 equipos × 24 sprints.
Costo de 14 MM CLP mensuales por equipo: cerca de 60 equipo-meses suman 840 MM, es decir, unos 7 MM por equipo-sprint efectivo.
OMS adquirido en modalidad de suscripción, con partner de implementación.
El ERP puede exponer stock mediante eventos o API (supuesto del Charter). Si no es así, aumenta el esfuerzo de E2.
6.3 Esfuerzo por épica
Unidad: equipo-sprints. Fórmula PERT: E = (O + 4M + P) / 6 y σ = (P − O) / 6.
Épica
Optimista (O)
Más probable (M)
Pesimista (P)
Esperado (E)
σ
E1 Disponibilidad de stock
10
14
22
14,7
2,0
E2 APIs / integración ERP-WMS-POS
12
16
26
17,0
2,3
E3 OMS (configuración e integración)
10
14
24
15,0
2,3
E4 Click & Collect
6
9
14
9,3
1,3
E5 App de preparación en tienda
6
8
13
8,5
1,2
E6 Seguridad (transversal)
4
6
9
6,2
0,8
E7 Preparación Black Friday
3
5
8
5,2
0,8
E8a Observabilidad básica
2
3
4
3,0
0,3
E8b Observabilidad centralizada
2
4
6
4,0
0,7
E9 Devoluciones omnicanal
6
9
15
9,5
1,5
E10 Piloto Ship-from-store
3
5
9
5,3
1,0
E11 Rollout y gestión del cambio
4
6
10
6,3
1,0
Total
68
99
160
104,0
4,9





6.4 Esfuerzo frente a capacidad
Escenario
Equipo-sprints
Uso de la capacidad (120)
Esperado (E)
104
87%
P80 (E + 0,84σ)
108
90%
P95 (E + 1,65σ)
112
93%
Pesimista puro (suma de P)
160
133%


El plan es viable con una confianza de entre 80% y 95%. El escenario pesimista puro no cabe en la capacidad, por lo que el alcance de R3 es la variable de ajuste: el proyecto fija tiempo y costo, y deja adaptable el contenido de R3.
PERT supone que las épicas son independientes, pero algunos riesgos afectan a varias a la vez. Por ejemplo, si el ERP no expone stock por API, se atrasan E1, E2 y E4 al mismo tiempo. Ese riesgo se cubre con la reserva de contingencia y con la revisión del Gate 1.
La carga se concentra antes de Black Friday: 71 de los 104 equipo-sprints esperados deben estar listos antes del congelamiento. Con 5 equipos constantes, la capacidad hasta el mes 7 sería de 70 equipo-sprints, es decir, más del 100%. Por eso la dotación se escalona con el mismo total de 120 equipo-sprints y 840 MM: un sexto equipo entre los meses 3 y 7 y 4 equipos después de Black Friday. R1 incluye E1 completa, cerca de la mitad de E2 y E3 (flujos de stock y pedidos, OMS básico), E8a y la parte piloto de E4 y E5; lo que no se necesita para Black Friday pasa a R3.
Tramo
Sprints efectivos
Equipos
Capacidad
Carga esperada
Uso
R1 (hasta el Gate 1, mes 5)
2 a 11
5; 6 desde el sprint 6
56
47,7
85%
R2 (hasta el congelamiento, mes 7)
12 a 15
6
24
23,0
96%
R3 (meses 8 a 12)
16 y 18 a 26
4
40
33,3
83%
Total
24
5 en promedio
120
104,0
87%

R2 queda al 96%, pero en conjunto R1 y R2 quedan al 88% y la holgura de R1 permite adelantar su preparación (pruebas de carga y material de capacitación). Si no se consigue el sexto equipo, las palancas son usar la reserva para reforzar capacidad o desplegar Click & Collect primero en las tiendas de mayor venta y completar las 68 después de Black Friday.
6.5 Presupuesto por categoría (MM CLP)
Categoría
Base
Rango (O a P)
Técnica
Equipos de desarrollo (120 equipo-sprints × 7)
840
840 (fijo por capacidad contratada)
Paramétrica
OMS: suscripción año 1 e implementación
180
140 a 240
Cotización
Cambios WMS (proveedor, contrato)
70
50 a 100
Cotización
Infraestructura cloud y herramientas de observabilidad
70
50 a 100
Paramétrica
Seguridad (pentest por release, herramientas)
35
25 a 50
Analogía
Gestión del cambio y capacitación (68 tiendas, de Arica a Punta Arenas)
45
30 a 70
Paramétrica
Gobierno del proyecto (PM, arquitectura, PMO)
90
80 a 100
Analogía
Subtotal
1.330
1.215 a 1.500


Reserva de contingencia (cerca de 13%)
170


Gestionada por el Comité
Total
1.500






La base de 1.330 MM es coherente con la inversión preliminar de la alternativa B (1.350 MM). La reserva de 170 MM cubre el escenario pesimista de los costos externos (1.500 − 1.330), de modo que el tope no se supera aunque todas las cotizaciones resulten en su valor alto.


6.6 Liberación por tramos
Tramo
Aprobado en
Cubre
Monto (MM CLP)
1
Gate 0 (mes 1)
R0 y R1 (meses 1-5), incluye la mayor parte del OMS
675
2
Gate 1 (mes 5)
R2 y Black Friday (meses 6-8)
345
3
Gate 2 (mes 9)
R3 (meses 9-12)
310
Reserva
A solicitud del PM
Riesgos materializados
170


Cada tramo suma el costo de los equipos en su período, según la dotación escalonada, más la parte de los costos externos que se ejecuta en él (por ejemplo, la mayor parte del OMS en el tramo 1).
6.7 Tratamiento de la incertidumbre
Cono de incertidumbre: la estimación actual tiene un rango de ±30% a 40%. Se reestima en cada gate con datos reales y el rango se estrecha a medida que avanza el proyecto.
Calibración ágil: desde el sprint 3, las épicas ágiles se reestiman con la velocidad real de los equipos.
Señal de alerta 1: si la velocidad de los sprints 1 a 3 es menor al 80% de lo supuesto, se recorta el piloto de R1 o se escala al Comité en el Gate 1.
Señal de alerta 2: si el ERP no expone stock por API al cierre de R0, se reestima E2 y se evalúa el uso de la reserva.
Uso de la reserva: solo con aprobación del Comité Ejecutivo y por riesgos registrados. No se usa para agregar alcance.
6.8 Base de estimación, nivel de confianza y compromiso
Una estimación defendible explica de dónde proviene. La base de estimación de ZEUS es la siguiente:
Elemento
En ZEUS
Alcance
Épicas E1 a E11 de la sección 5. Fuera: IA, data platform completa, identidad de clientes, migración amplia a cloud y reemplazo de ERP/WMS.
Datos
No hay histórico propio de un proyecto como este: se usan referencias de implementaciones de OMS de mercado y de integraciones anteriores de la empresa, que se reemplazan por velocidad y throughput reales desde el mes 2.
Método
Análoga y PERT para lo predictivo, cotización y paramétrica para proveedores, relativa (tallas) para lo ágil y flujo (throughput) para lo Kanban.
Supuestos
Los de la sección 6.2, más los del Charter (ERP con API, proveedor WMS en plazo, OMS de mercado).
Riesgos
ERP sin API, atraso del proveedor WMS, capacidad de las tiendas y falta del sexto equipo.
Confianza
Esfuerzo: P50 de 104, P80 de 108 y P95 de 112 equipo-sprints. Costo: entre 1.215 y 1.500 MM.


Estimación, compromiso y objetivo se tratan como decisiones distintas:
Concepto
Pregunta
En ZEUS
Estimación
¿Qué creemos que ocurrirá?
104 equipo-sprints esperados (P50) y 1.330 MM de base
Compromiso
¿A qué nos obligamos?
R1 en el mes 5 y R2 antes del congelamiento, al nivel P80, dentro del tope de 1.500 MM
Objetivo
¿Qué resultado queremos lograr?
Los KPIs del Charter: cancelaciones bajo 2%, stock web bajo 2 minutos, preparación bajo 3 horas, devoluciones y disponibilidad


El nivel de confianza es una decisión de riesgo del Comité, no solo un dato estadístico. R1 y R2 se comprometen al P80 porque son compromisos sensibles (primera entrega de valor y Black Friday): su carga P80 antes del congelamiento es de cerca de 74 equipo-sprints, el 92% de los 80 disponibles. R3 se planifica al P50 porque es la variable de ajuste. La tolerancia la fija el Sponsor: el tope de 1.500 MM.
Artefactos del enfoque híbrido: un ROM ejecutivo (esta estimación por rangos) más el backlog estimado en tallas; un forecast ejecutivo que se actualiza con evidencia de flujo, con simulación Monte Carlo cuando haya entre 6 y 8 semanas de historial; un roadmap con backlog y gates; y financiamiento por tramos con un registro de decisiones del Comité (decision log). Las tallas y los story points se usan dentro de cada equipo y no se comparan entre equipos; para el forecast ejecutivo se convierten a equipo-sprints.
