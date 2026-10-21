# Avance del equipo recibido el 21 de octubre de 2026

Documento de entrada conservado sin correcciones de contenido. Es un borrador del equipo, no el enunciado oficial ni una versión ya revisada. Las secciones integradas están en [diagnóstico](../trabajo/01_diagnostico_y_business_case.md), [enfoque](../trabajo/02_enfoque.md) y [Charter](../trabajo/03_charter.md); los cambios se explican en la [revisión](../registros/integracion_avance_equipo.md).

## Texto recibido


1. Diagnóstico estratégico y Business Case

Problema/oportunidad, drivers estratégicos, alternativas, beneficios, costos, riesgos, supuestos y recomendación. Debe distinguir claramente output, outcome, beneficio y valor.

1.1 Problemas

Entre los principales problemas que tiene actualmente el negocio con su sistema digital se tiene que:
El sistema actual tiene una alta latencia entre la actualización del inventario y la actualización del stock en la página web, llevando a un 7,8% de cancelaciones forzadas post-compra debido a quiebres de stock no detectados al momento del pago. 
Existen bases duplicadas y desalineadas de clientes y productos, y las tiendas físicas carecen de visibilidad para las compras digitales. Lo que limita la capacidad de resolver disputas y devoluciones, siendo solo el 64% resueltas en el primer contacto. Empeorando la calidad de atención al cliente.
Se tienen limitaciones sobre partes del sistema antiguo que no se pueden cambiar, las cuales a pesar de abaratar los costos de desarrollo hacen que el desarrollo tenga que trabajar alrededor de los mismos.

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

Para el desarrollo 

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
